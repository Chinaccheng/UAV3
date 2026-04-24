"""
恢复策略模块：实现基于熵值的恢复策略
"""
import numpy as np
from typing import List, Optional
from node import Node, NodeType
from network_layers import CommunicationLayer, PhysicalLayer
from performance import PerformanceEvaluator
from config import Config

class RecoveryStrategy:
    """恢复策略"""
    
    def __init__(self, config: Config, performance_evaluator: PerformanceEvaluator):
        """
        初始化恢复策略
        
        Args:
            config: 配置对象
            performance_evaluator: 性能评估器（用于计算熵值）
        """
        self.config = config
        self.performance_evaluator = performance_evaluator
        self.cluster_center_history = []  # 记录集群重心历史
        self.role_centers = {}

    @staticmethod
    def _get_comm_neighbors(comm_layer: CommunicationLayer, node_id: int):
        """获取通信层中与节点相关的所有邻居（兼容有向图）。"""
        graph = comm_layer.graph
        if node_id not in graph:
            return []
        if graph.is_directed():
            return list(set(graph.predecessors(node_id)) | set(graph.successors(node_id)))
        return list(graph.neighbors(node_id))
    
    def calculate_node_entropy(self, node: Node, nodes: List[Node], 
                             comm_layer: CommunicationLayer):
        """
        计算节点局部熵值（优化版：使用numpy和图的度字典）
        
        Args:
            node: 目标节点
            nodes: 所有节点列表
            comm_layer: 通信层网络
            
        Returns:
            节点熵值（熵值越低越好）
        """
        if not node.is_alive:
            return np.inf
        
        # 获取节点的邻居节点
        if node.id not in comm_layer.graph:
            return np.inf
        
        neighbors = self._get_comm_neighbors(comm_layer, node.id)
        if len(neighbors) == 0:
            return np.inf
        
        # 计算邻居节点的度分布熵（优化：直接使用图的度字典）
        degrees_dict = dict(comm_layer.graph.degree())
        neighbor_degrees = [degrees_dict.get(nid, 0) for nid in neighbors]
        
        if len(neighbor_degrees) == 0:
            return np.inf
        
        # 归一化为概率分布
        total_degree = sum(neighbor_degrees)
        if total_degree == 0:
            return np.inf
        
        # 计算熵（使用numpy优化）
        probs_array = np.array(neighbor_degrees, dtype=np.float64) / total_degree
        probs_array = probs_array[probs_array > 0]  # 只保留非零概率
        if len(probs_array) == 0:
            return np.inf
        entropy = -np.sum(probs_array * np.log2(probs_array + 1e-10))
        
        return entropy
    
    def find_lowest_entropy_neighbor(self, node: Node, nodes: List[Node],
                                   comm_layer: CommunicationLayer,
                                   use_sensor_range: bool = False):
        """
        找到熵值最低的邻居节点（优化版：直接使用图的邻居结构）
        
        Args:
            node: 当前节点
            nodes: 所有节点列表（用于节点ID到节点的映射）
            comm_layer: 通信层网络
            use_sensor_range: 是否使用感知范围（True）或通信范围（False）
            
        Returns:
            熵值最低的邻居节点，如果没有则返回None
        """
        if not node.is_alive:
            return None
        
        # 创建节点ID到节点的映射
        node_dict = {n.id: n for n in nodes if n.is_alive}
        
        # 如果使用通信范围，直接使用图的邻居（更快）
        if not use_sensor_range and node.id in comm_layer.graph:
            neighbor_ids = self._get_comm_neighbors(comm_layer, node.id)
            candidate_nodes = [node_dict[nid] for nid in neighbor_ids if nid in node_dict]
        else:
            # 使用感知范围时，需要遍历所有节点（但这种情况较少）
            candidate_nodes = []
            for other_node in nodes:
                if not other_node.is_alive or other_node.id == node.id:
                    continue
                if use_sensor_range:
                    if node.is_in_sensor_range(other_node):
                        candidate_nodes.append(other_node)
                else:
                    if node.is_in_communication_range(other_node):
                        candidate_nodes.append(other_node)
        
        if len(candidate_nodes) == 0:
            return None
        
        # 计算每个候选节点的熵值（只计算一次）
        min_entropy = np.inf
        best_node = None
        
        for candidate in candidate_nodes:
            entropy = self.calculate_node_entropy(candidate, nodes, comm_layer)
            if entropy < min_entropy:
                min_entropy = entropy
                best_node = candidate
        
        return best_node
    
    def calculate_cluster_center(self, nodes: List[Node]):
        """计算集群重心"""
        alive_nodes = [n for n in nodes if n.is_alive]
        if len(alive_nodes) == 0:
            return np.array([self.config.AREA_SIZE / 2, self.config.AREA_SIZE / 2])
        
        positions = np.array([n.position for n in alive_nodes])
        center = np.mean(positions, axis=0)
        return center

    def _update_memory(self, alive_nodes: List[Node], current_time: int):
        """同步维护集群中心和各角色中心记忆。"""
        cluster_center = self.calculate_cluster_center(alive_nodes)
        self.cluster_center_history.append(cluster_center)

        self.role_centers = {}
        for node_type in NodeType:
            typed_nodes = [node for node in alive_nodes if node.type == node_type]
            if typed_nodes:
                typed_positions = np.array([node.position for node in typed_nodes], dtype=float)
                self.role_centers[node_type] = np.mean(typed_positions, axis=0)

        for node in alive_nodes:
            node.update_memory(cluster_center, current_time)
        return cluster_center

    def _resolve_recovery_speed(self, current_time: int) -> float:
        """按时间解析当前时刻的恢复移动速度。默认返回固定 RECOVERY_SPEED。"""
        base_speed = float(getattr(self.config, "RECOVERY_SPEED", 0.0))
        speed_profile = getattr(self.config, "RECOVERY_SPEED_PROFILE", None)
        if not speed_profile:
            return max(0.0, base_speed)

        for start, end, multiplier in speed_profile:
            if start <= current_time < end:
                return max(0.0, base_speed * float(multiplier))
        return max(0.0, base_speed)

    def _move_alive_nodes_to_targets(
        self,
        nodes: List[Node],
        target_positions,
        current_time: int,
    ) -> None:
        """按当前恢复速度统一执行移动。"""
        current_speed = self._resolve_recovery_speed(current_time)
        for node in nodes:
            if not node.is_alive or node.id not in target_positions:
                continue
            node.move_towards(
                target_positions[node.id],
                speed=current_speed,
                other_nodes=nodes,
            )

    def _find_local_candidates(self, current_node: Node, nodes: List[Node]):
        """在局部视野内查找除自身外的存活节点。"""
        return [
            node for node in nodes
            if node.is_alive
            and node.id != current_node.id
            and current_node.get_distance(node) <= self.config.SEARCH_RADIUS
        ]

    def _find_nearest_node(self, current_node: Node, candidate_nodes: List[Node]):
        """查找最近的候选节点。"""
        if not candidate_nodes:
            return None
        return min(
            candidate_nodes,
            key=lambda node: (current_node.get_distance(node), node.id),
        )

    def _find_highest_degree_node(
        self,
        current_node: Node,
        candidate_nodes: List[Node],
        comm_layer: CommunicationLayer,
        physical_layer: Optional[PhysicalLayer] = None,
    ):
        """查找局部视野内通信层度数最高的候选节点。"""
        if not candidate_nodes:
            return None

        degree_graph = physical_layer.graph if physical_layer is not None else comm_layer.graph
        degrees_dict = dict(degree_graph.degree()) if len(degree_graph) > 0 else {}
        return max(
            candidate_nodes,
            key=lambda node: (
                degrees_dict.get(node.id, 0),
                -current_node.get_distance(node),
                -node.id,
            ),
        )

    def _is_baseline_impaired(
        self,
        node: Node,
        physical_layer: Optional[PhysicalLayer] = None,
        comm_layer: Optional[CommunicationLayer] = None,
    ) -> bool:
        """判断基线重构策略下节点是否满足触发条件。"""
        if not node.is_alive:
            return False
        if physical_layer is None:
            return False

        degrees_dict = dict(physical_layer.graph.degree()) if len(physical_layer.graph) > 0 else {}
        physical_degree = degrees_dict.get(node.id, 0)
        threshold = getattr(self.config, "BASELINE_TRIGGER_PHYSICAL_DEGREE", 0)
        if physical_degree <= threshold:
            return True

        # 基线策略仍然只服务于物理毁伤场景；在物理攻击下，通信完全孤立也视为需要恢复。
        if getattr(self.config, "ATTACK_MODE", "physical") == "physical" and comm_layer is not None:
            comm_degree = comm_layer.graph.degree(node.id) if node.id in comm_layer.graph else 0
            if comm_degree == 0:
                return True

        return False

    def _has_required_role_partner(
        self,
        node: Node,
        alive_lookup,
        comm_layer: CommunicationLayer,
        jammed_ids,
        utility_phase: int,
    ) -> bool:
        """判断节点是否已连接到指定任务阶段所需的关键角色。"""
        neighbor_ids = self._get_comm_neighbors(comm_layer, node.id)
        if utility_phase == 1:
            if node.type == NodeType.SENSOR:
                required_types = {NodeType.DECIDER}
            elif node.type == NodeType.DECIDER:
                required_types = {NodeType.SENSOR, NodeType.DECIDER}
            else:
                # 侦察阶段不以 I 节点闭环为首要目标
                required_types = set()
        else:
            if node.type == NodeType.DECIDER:
                required_types = {NodeType.INFLUENCER}
            else:
                required_types = {NodeType.DECIDER}

        if not required_types:
            return True

        for neighbor_id in neighbor_ids:
            if neighbor_id in jammed_ids:
                continue
            neighbor = alive_lookup.get(neighbor_id)
            if neighbor is not None and neighbor.type in required_types:
                return True
        return False

    def _pick_role_memory_target(self, node: Node, alive_nodes: List[Node], jammed_ids, utility_phase: int):
        """为孤立节点选择角色优先的全局恢复目标。"""
        eligible_nodes = [other for other in alive_nodes if other.id not in jammed_ids]

        if utility_phase == 1:
            if node.type == NodeType.SENSOR:
                deciders = [other for other in eligible_nodes if other.type == NodeType.DECIDER]
                nearest_decider = self._find_nearest_node(node, deciders)
                if nearest_decider is not None:
                    return nearest_decider.position

                remembered_decider = self.role_centers.get(NodeType.DECIDER)
                if remembered_decider is not None:
                    return remembered_decider

            elif node.type == NodeType.DECIDER:
                sensors = [other for other in eligible_nodes if other.type == NodeType.SENSOR]
                nearest_sensor = self._find_nearest_node(node, sensors)
                if nearest_sensor is not None:
                    return nearest_sensor.position

                deciders = [other for other in eligible_nodes if other.type == NodeType.DECIDER and other.id != node.id]
                nearest_decider = self._find_nearest_node(node, deciders)
                if nearest_decider is not None:
                    return nearest_decider.position

                remembered_sensor = self.role_centers.get(NodeType.SENSOR)
                if remembered_sensor is not None:
                    return remembered_sensor

                remembered_decider = self.role_centers.get(NodeType.DECIDER)
                if remembered_decider is not None:
                    return remembered_decider
            else:
                # 错配阶段下 I 节点不再被优先纳入闭环，只回归记忆中心/集群中心
                remembered_decider = self.role_centers.get(NodeType.DECIDER)
                if remembered_decider is not None:
                    return remembered_decider
        else:
            if node.type == NodeType.DECIDER:
                influencers = [other for other in eligible_nodes if other.type == NodeType.INFLUENCER]
                nearest_influencer = self._find_nearest_node(node, influencers)
                if nearest_influencer is not None:
                    return nearest_influencer.position

                deciders = [other for other in eligible_nodes if other.type == NodeType.DECIDER and other.id != node.id]
                nearest_decider = self._find_nearest_node(node, deciders)
                if nearest_decider is not None:
                    return nearest_decider.position

                remembered_influencer = self.role_centers.get(NodeType.INFLUENCER)
                if remembered_influencer is not None:
                    return remembered_influencer
            else:
                deciders = [other for other in eligible_nodes if other.type == NodeType.DECIDER]
                nearest_decider = self._find_nearest_node(node, deciders)
                if nearest_decider is not None:
                    return nearest_decider.position

                remembered_decider = self.role_centers.get(NodeType.DECIDER)
                if remembered_decider is not None:
                    return remembered_decider

        if node.memory_center is not None:
            return node.memory_center
        return self.calculate_cluster_center(alive_nodes)

    def _calculate_order_score(self, node_id: int, comm_layer: CommunicationLayer) -> float:
        """计算候选节点邻域的有序度分数。"""
        neighbors = self._get_comm_neighbors(comm_layer, node_id)
        if not neighbors:
            return 0.0

        degrees_dict = dict(comm_layer.graph.degree())
        neighbor_degrees = np.array([degrees_dict.get(neighbor_id, 0) for neighbor_id in neighbors], dtype=float)
        positive_degrees = neighbor_degrees[neighbor_degrees > 0]
        if len(positive_degrees) == 0:
            return 0.0
        if len(positive_degrees) == 1:
            return 1.0

        probabilities = positive_degrees / np.sum(positive_degrees)
        entropy = -np.sum(probabilities * np.log(probabilities + 1e-12))
        h_max = np.log(len(probabilities))
        if h_max <= 0.0:
            return 1.0
        return float(max(0.0, 1.0 - entropy / h_max))

    def _get_phase(self, current_time: int) -> int:
        """根据时刻确定任务阶段。"""
        for start, end, phase in self.config.TASK_PHASE_SCHEDULE:
            if start <= current_time < end:
                return phase
        raise ValueError(f"时刻 {current_time} 未匹配到 TASK_PHASE_SCHEDULE")

    def _calculate_pair_utility(
        self,
        node: Node,
        candidate: Node,
        physical_layer: PhysicalLayer,
        comm_layer: CommunicationLayer,
        current_time: int,
        utility_phase_override: Optional[int] = None,
    ) -> float:
        """计算效用与角色驱动策略中的局部重构效用。"""
        phase = utility_phase_override if utility_phase_override is not None else self._get_phase(current_time)
        distance = node.get_distance(candidate)
        p_phy = comm_layer._f_phy(distance)
        if p_phy <= 0.0:
            return 0.0

        p_forward = p_phy * comm_layer._f_logic(node, candidate, phase, physical_layer)
        p_backward = p_phy * comm_layer._f_logic(candidate, node, phase, physical_layer)
        link_strength = max(p_forward, p_backward)

        degrees_dict = dict(comm_layer.graph.degree())
        degree_max = max(degrees_dict.values()) if degrees_dict else 1
        degree_score = degrees_dict.get(candidate.id, 0) / degree_max if degree_max > 0 else 0.0
        order_score = self._calculate_order_score(candidate.id, comm_layer)

        role_bonus_map = {
            NodeType.SENSOR: {
                NodeType.SENSOR: 0.85,
                NodeType.DECIDER: 1.40,
                NodeType.INFLUENCER: 0.55,
            },
            NodeType.DECIDER: {
                NodeType.SENSOR: 0.70,
                NodeType.DECIDER: 0.95,
                NodeType.INFLUENCER: 1.45,
            },
            NodeType.INFLUENCER: {
                NodeType.SENSOR: 0.50,
                NodeType.DECIDER: 1.50,
                NodeType.INFLUENCER: 0.80,
            },
        }
        role_bonus = role_bonus_map[node.type][candidate.type]
        utility = link_strength * (0.65 + 0.35 * order_score) * role_bonus + 0.03 * degree_score
        return float(utility)

    def _select_utility_role_target(
        self,
        node: Node,
        alive_nodes: List[Node],
        alive_lookup,
        physical_layer: PhysicalLayer,
        comm_layer: CommunicationLayer,
        current_time: int,
        jammed_ids,
        utility_phase_override: Optional[int] = None,
    ):
        """选择效用与角色驱动策略的目标位置。"""
        if node.id in jammed_ids:
            return node.position

        utility_phase = utility_phase_override if utility_phase_override is not None else self._get_phase(current_time)
        candidate_pool = [other for other in alive_nodes if other.id not in jammed_ids]
        local_candidates = self._find_local_candidates(node, candidate_pool)
        best_node = None
        best_utility = -np.inf
        for candidate in local_candidates:
            utility = self._calculate_pair_utility(
                node,
                candidate,
                physical_layer,
                comm_layer,
                current_time,
                utility_phase_override=utility_phase,
            )
            if utility > best_utility:
                best_utility = utility
                best_node = candidate

        is_isolated = node.id not in comm_layer.graph or comm_layer.graph.degree(node.id) == 0
        has_required_partner = self._has_required_role_partner(
            node,
            alive_lookup,
            comm_layer,
            jammed_ids,
            utility_phase,
        )

        if is_isolated or not has_required_partner:
            return self._pick_role_memory_target(node, alive_nodes, jammed_ids, utility_phase)
        if best_node is None or best_utility < getattr(self.config, "UTILITY_MIN_ACCEPTANCE", 0.0):
            return node.position
        return best_node.position
    
    def _find_nearest_node_in_list(self, current_node: Node, target_nodes: List[Node]):
        """
        在给定的节点列表中查找最近的节点
        
        Args:
            current_node: 当前节点
            target_nodes: 目标节点列表 (已按类型预筛选)
            
        Returns:
            最近的目标节点，如果没有则返回None
        """
        # 筛选出除自身以外的候选节点
        candidate_nodes = [n for n in target_nodes if n.id != current_node.id]

        if not candidate_nodes:
            return None
            
        min_dist = np.inf
        nearest_node = None
        
        for target_node in candidate_nodes:
            dist = current_node.get_distance(target_node)
            if dist < min_dist:
                min_dist = dist
                nearest_node = target_node
                
        return nearest_node

    def _execute_entropy_recovery(self, nodes: List[Node], comm_layer: CommunicationLayer, current_time: int):
        """执行原有基于熵值与角色记忆的恢复策略。"""
        alive_nodes = [n for n in nodes if n.is_alive]
        cluster_center = self._update_memory(alive_nodes, current_time)
        decider_nodes = [n for n in alive_nodes if n.type == NodeType.DECIDER]

        # 对每个存活节点执行恢复策略
        # 先计算所有节点的目标位置，再统一移动（避免顺序影响）
        target_positions = {}
        
        # 预先计算所有节点的度（避免重复计算）
        degrees_dict = dict(comm_layer.graph.degree()) if len(comm_layer.graph) > 0 else {}
        
        for node in alive_nodes:
            target_pos = None
            is_isolated = (node.id not in comm_layer.graph) or (degrees_dict.get(node.id, 0) == 0)

            if not is_isolated:
                # 策略1: 节点已连接，优化局部网络结构
                lowest_entropy_neighbor = self.find_lowest_entropy_neighbor(
                    node, alive_nodes, comm_layer, use_sensor_range=False)
                
                if lowest_entropy_neighbor is not None:
                    target_pos = self._calculate_target_with_min_distance(
                        node.position, lowest_entropy_neighbor.position)
                else:
                    target_pos = node.position  # 保持不动
            else:
                # 策略2: 节点孤立，执行基于角色的全局恢复
                if node.type == NodeType.SENSOR or node.type == NodeType.INFLUENCER:
                    # S和I节点优先寻找最近的D节点
                    nearest_decider = self._find_nearest_node_in_list(node, decider_nodes)
                    if nearest_decider:
                        target_pos = nearest_decider.position
                    else:
                        target_pos = node.memory_center if node.memory_center is not None else cluster_center
                
                elif node.type == NodeType.DECIDER:
                    # D节点优先寻找最近的其他D节点，重建骨干网络
                    nearest_decider = self._find_nearest_node_in_list(node, decider_nodes)
                    if nearest_decider:
                        target_pos = nearest_decider.position
                    else:
                        target_pos = node.memory_center if node.memory_center is not None else cluster_center
                
                else:
                    target_pos = node.memory_center if node.memory_center is not None else cluster_center

            target_positions[node.id] = target_pos
        
        # 统一执行移动，传入其他节点列表以进行碰撞避免
        self._move_alive_nodes_to_targets(nodes, target_positions, current_time)

    def _execute_distance_driven_recovery(
        self,
        nodes: List[Node],
        comm_layer: CommunicationLayer,
        current_time: int,
        physical_layer: Optional[PhysicalLayer] = None,
    ):
        """
        基于最短距离的重构：
        受损节点或孤立节点仅以恢复物理连通性为目标，
        在局部视野内寻找距离最近的存活节点靠拢。
        """
        alive_nodes = [n for n in nodes if n.is_alive]
        cluster_center = self._update_memory(alive_nodes, current_time)
        target_positions = {}

        for node in alive_nodes:
            if not self._is_baseline_impaired(node, physical_layer, comm_layer):
                continue
            local_candidates = self._find_local_candidates(node, alive_nodes)
            nearest_node = self._find_nearest_node(node, local_candidates)
            if nearest_node is None:
                target_positions[node.id] = node.memory_center if node.memory_center is not None else cluster_center
                continue

            target_positions[node.id] = self._calculate_target_with_min_distance(
                node.position,
                nearest_node.position,
            )

        self._move_alive_nodes_to_targets(nodes, target_positions, current_time)

    def _execute_degree_driven_recovery(
        self,
        nodes: List[Node],
        comm_layer: CommunicationLayer,
        current_time: int,
        physical_layer: Optional[PhysicalLayer] = None,
    ):
        """
        基于最高度数的重构：
        受损节点或孤立节点在局部视野内寻找度数最高的拓扑枢纽进行靠拢。
        """
        alive_nodes = [n for n in nodes if n.is_alive]
        cluster_center = self._update_memory(alive_nodes, current_time)
        target_positions = {}

        for node in alive_nodes:
            if not self._is_baseline_impaired(node, physical_layer, comm_layer):
                continue
            local_candidates = self._find_local_candidates(node, alive_nodes)
            hub_node = self._find_highest_degree_node(node, local_candidates, comm_layer, physical_layer)
            if hub_node is None:
                target_positions[node.id] = node.memory_center if node.memory_center is not None else cluster_center
                continue

            target_positions[node.id] = self._calculate_target_with_min_distance(
                node.position,
                hub_node.position,
            )

        self._move_alive_nodes_to_targets(nodes, target_positions, current_time)

    def _execute_utility_role_recovery(
        self,
        nodes: List[Node],
        comm_layer: CommunicationLayer,
        current_time: int,
        physical_layer: PhysicalLayer,
        jammed_ids,
        utility_phase_override: Optional[int] = None,
    ):
        """执行实验二中的效用与角色驱动恢复。"""
        alive_nodes = [n for n in nodes if n.is_alive]
        self._update_memory(alive_nodes, current_time)
        target_positions = {}
        alive_lookup = {node.id: node for node in alive_nodes}

        for node in alive_nodes:
            target_positions[node.id] = self._select_utility_role_target(
                node,
                alive_nodes,
                alive_lookup,
                physical_layer,
                comm_layer,
                current_time,
                jammed_ids,
                utility_phase_override=utility_phase_override,
            )

        self._move_alive_nodes_to_targets(nodes, target_positions, current_time)

    def execute_recovery(
        self,
        nodes: List[Node],
        comm_layer: CommunicationLayer,
        current_time: int,
        physical_layer: Optional[PhysicalLayer] = None,
        jammed_ids=None,
        strategy_override: Optional[str] = None,
    ):
        """
        根据配置执行恢复策略。

        Args:
            nodes: 节点列表
            comm_layer: 通信层网络
            current_time: 当前时刻
        """
        strategy = strategy_override or getattr(self.config, 'RECOVERY_STRATEGY', 'entropy')
        effective_jammed_ids = set() if jammed_ids is None else set(jammed_ids)

        if strategy in ('no_reconfiguration', 'none'):
            return
        if strategy == 'entropy':
            self._execute_entropy_recovery(nodes, comm_layer, current_time)
        elif strategy == 'distance_driven':
            self._execute_distance_driven_recovery(nodes, comm_layer, current_time, physical_layer)
        elif strategy == 'degree_driven':
            self._execute_degree_driven_recovery(nodes, comm_layer, current_time, physical_layer)
        elif strategy == 'utility_role_driven':
            if physical_layer is None:
                raise ValueError("utility_role_driven 恢复需要 physical_layer")
            self._execute_utility_role_recovery(
                nodes,
                comm_layer,
                current_time,
                physical_layer,
                effective_jammed_ids,
            )
        elif strategy == 'utility_role_mismatch_recon':
            if physical_layer is None:
                raise ValueError("utility_role_mismatch_recon 恢复需要 physical_layer")
            # 反面教材：在打击任务中仍按侦察阶段的链路偏好恢复，导致 S-D 被过度修复而 D-I 被忽视。
            self._execute_utility_role_recovery(
                nodes,
                comm_layer,
                current_time,
                physical_layer,
                effective_jammed_ids,
                utility_phase_override=1,
            )
        else:
            raise ValueError(f"不支持的恢复策略: {strategy}")
    
    def _calculate_target_with_min_distance(self, current_pos, target_pos):
        """
        计算目标位置，确保与目标保持最小距离
        
        Args:
            current_pos: 当前位置
            target_pos: 原始目标位置
            
        Returns:
            调整后的目标位置（保持最小距离）
        """
        min_distance = self.config.get_min_node_distance()
        direction = np.array(target_pos) - np.array(current_pos)
        distance = np.linalg.norm(direction)
        
        if distance > min_distance:
            # 如果距离大于最小距离，移动到保持最小距离的位置
            direction_normalized = direction / distance
            adjusted_target = np.array(current_pos) + direction_normalized * (distance - min_distance)
            return adjusted_target
        else:
            # 如果距离已经小于最小距离，保持当前位置（不移动）
            return current_pos
    
    def get_cluster_center(self):
        """获取当前集群重心"""
        if len(self.cluster_center_history) > 0:
            return self.cluster_center_history[-1]
        return None
