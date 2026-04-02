"""
恢复策略模块：实现基于局部通信效能与角色导向的恢复策略
"""
import numpy as np
from typing import List
from node import Node, NodeType
from network_layers import CommunicationLayer
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

    @staticmethod
    def _get_comm_neighbors(comm_layer: CommunicationLayer, node_id: int):
        """获取通信层中与节点相关的所有邻居（兼容有向图）。"""
        graph = comm_layer.graph
        if node_id not in graph:
            return []
        if graph.is_directed():
            return list(set(graph.predecessors(node_id)) | set(graph.successors(node_id)))
        return list(graph.neighbors(node_id))

    def calculate_local_communication_utility(self, node: Node, nodes: List[Node],
                                              comm_layer: CommunicationLayer):
        """
        计算节点局部综合通信效能 U_j(t)

        Args:
            node: 目标节点
            nodes: 所有节点列表
            comm_layer: 通信层网络

        Returns:
            节点局部综合通信效能（越大越好）
        """
        if not node.is_alive:
            return 0.0

        alive_node_ids = [n.id for n in nodes if n.is_alive and n.id != node.id]
        if not alive_node_ids:
            return 0.0

        # 与通信层性能保持一致：按发送方 j 的有向概率 P(j->k) 计算强度与有序度。
        outgoing_probs = []
        for other_id in alive_node_ids:
            p_jk = comm_layer.activation_probabilities.get((node.id, other_id), 0.0)
            if p_jk > 0:
                outgoing_probs.append(p_jk)

        sum_p = sum(outgoing_probs)
        h_max = np.log(len(alive_node_ids)) if len(alive_node_ids) > 1 else 1.0
        if h_max <= 0:
            h_max = 1e-10

        if sum_p > 0:
            probs_array = np.array(outgoing_probs, dtype=np.float64) / sum_p
            h_j = -np.sum(probs_array * np.log(probs_array + 1e-10))
        else:
            h_j = h_max

        intensity_weight = 1.0 - np.exp(-sum_p)
        order_score = max(0.0, 1.0 - (h_j / h_max))
        return intensity_weight * order_score

    def find_highest_utility_neighbor(self, node: Node, nodes: List[Node],
                                      comm_layer: CommunicationLayer,
                                      use_sensor_range: bool = False):
        """
        找到局部综合通信效能最高的邻居节点

        Args:
            node: 当前节点
            nodes: 所有节点列表（用于节点ID到节点的映射）
            comm_layer: 通信层网络
            use_sensor_range: 是否使用感知范围（True）或通信范围（False）

        Returns:
            效能最高的邻居节点，如果没有则返回None
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

        # 计算每个候选节点的局部综合通信效能 U_j(t)，选择最高者。
        max_utility = -np.inf
        best_node = None

        for candidate in candidate_nodes:
            utility = self.calculate_local_communication_utility(candidate, nodes, comm_layer)
            if utility > max_utility:
                max_utility = utility
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

    def execute_recovery(self, nodes: List[Node], comm_layer: CommunicationLayer,
                        current_time: int):
        """
        执行恢复策略

        策略：
        1. 如果节点有邻居，向局部综合通信效能最高的邻居移动
        2. 如果节点完全孤立，执行基于角色与记忆的全局恢复

        Args:
            nodes: 节点列表
            comm_layer: 通信层网络
            current_time: 当前时刻
        """
        # 更新集群重心
        cluster_center = self.calculate_cluster_center(nodes)
        self.cluster_center_history.append(cluster_center)
        
        # 更新所有节点的记忆
        for node in nodes:
            if node.is_alive:
                node.update_memory(cluster_center, current_time)
        
        # 预先按类型对节点进行分组，以优化查找
        alive_nodes = [n for n in nodes if n.is_alive]
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
                highest_utility_neighbor = self.find_highest_utility_neighbor(
                    node, alive_nodes, comm_layer, use_sensor_range=False)

                if highest_utility_neighbor is not None:
                    target_pos = self._calculate_target_with_min_distance(
                        node.position, highest_utility_neighbor.position)
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
        for node in nodes:
            if not node.is_alive or node.id not in target_positions:
                continue
            
            node.move_towards(target_positions[node.id], other_nodes=nodes)
    
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
