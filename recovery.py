"""
恢复策略模块：实现基于熵值的恢复策略
"""
import numpy as np
from typing import List, Optional
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
        
        neighbors = list(comm_layer.graph.neighbors(node.id))
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
            neighbor_ids = list(comm_layer.graph.neighbors(node.id))
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
        1. 如果节点有邻居，向熵值最低的邻居移动
        2. 如果节点完全孤立，向记忆中的集群重心移动，或执行广域搜索
        
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

