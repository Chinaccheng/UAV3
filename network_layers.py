"""
网络层类：实现物理层、通信层、任务层
"""
import numpy as np
import networkx as nx
from typing import List, Dict
from node import Node, NodeType
from config import Config

class PhysicalLayer:
    """物理实体层：基于距离的连边"""
    
    def __init__(self, config: Config):
        self.config = config
        self.graph = nx.Graph()
        
    def update(self, nodes: List[Node]):
        """更新物理层网络拓扑"""
        self.graph.clear()
        
        # 添加所有存活节点
        for node in nodes:
            if node.is_alive:
                self.graph.add_node(node.id, node=node)
        
        # 根据距离添加边
        for i, node_i in enumerate(nodes):
            if not node_i.is_alive:
                continue
            for node_j in nodes[i+1:]:
                if not node_j.is_alive:
                    continue
                if node_i.is_in_communication_range(node_j):
                    self.graph.add_edge(node_i.id, node_j.id, 
                                       distance=node_i.get_distance(node_j))
    
    def get_adjacency_matrix(self):
        """获取邻接矩阵"""
        n = len(self.graph.nodes())
        if n == 0:
            return np.zeros((0, 0))
        adj = nx.adjacency_matrix(self.graph, nodelist=sorted(self.graph.nodes()))
        return adj.toarray()
    
    def get_neighbors(self, node_id):
        """获取节点的邻居"""
        return list(self.graph.neighbors(node_id))

class CommunicationLayer:
    """通信网络层：基于概率的连边"""
    
    def __init__(self, config: Config):
        self.config = config
        self.graph = nx.DiGraph()
        self.activation_probabilities = {}  # 存储激活概率
        
    def _f_phy(self, distance):
        """
        物理层约束函数
        
        Args:
            distance: 节点间距离
            
        Returns:
            物理层通信概率
        """
        r_c = self.config.R_COMM
        eta = self.config.ETA
        
        if distance < eta * r_c:
            return 1.0
        elif distance <= r_c:
            return (r_c - distance) / (r_c * (1 - eta))
        else:
            return 0.0
    
    def _f_logic(self, node_sender: Node, node_receiver: Node, phase: int, physical_layer: PhysicalLayer):
        """
        逻辑层交互倾向函数（基于OODA任务链 + 负载修正）

        Args:
            node_sender: 发送方节点
            node_receiver: 接收方节点
            phase: 任务阶段 (1=侦察阶段, 2=打击阶段)
            physical_layer: 物理层网络（用于计算负载修正项）

        Returns:
            从 sender 指向 receiver 的逻辑层交互概率
        """
        type_i = node_sender.type
        type_j = node_receiver.type

        # 允许的传输规则 R = {(S->S), (S->D), (D->D), (D->S), (D->I)}
        allowed_rules = [
            (NodeType.SENSOR, NodeType.SENSOR),
            (NodeType.SENSOR, NodeType.DECIDER),
            (NodeType.DECIDER, NodeType.DECIDER),
            (NodeType.DECIDER, NodeType.SENSOR),
            (NodeType.DECIDER, NodeType.INFLUENCER),
        ]

        # 1) 基础匹配得分（等价于 X_i^T * Omega(\Phi) * X_j）
        match_score = 0.0
        EPSILON = 0.05  # 极小底噪，对应公式中的 \epsilon（代表静默状态下的最低限度心跳）

        if (type_i, type_j) in allowed_rules:

            if phase == 1:  # 侦察阶段 (\Phi = 1)
                # --- 发送方为 SENSOR ---
                if type_i == NodeType.SENSOR and type_j == NodeType.SENSOR:
                    match_score = 0.25  # 1/4: S->S 情报共享与局部避让
                elif type_i == NodeType.SENSOR and type_j == NodeType.DECIDER:
                    match_score = 0.75  # 3/4: S->D 核心情报汇聚上传

                # --- 发送方为 DECIDER ---
                elif type_i == NodeType.DECIDER and type_j == NodeType.SENSOR:
                    match_score = 0.67  # 2/3 (近似): D->S 决策反馈与闭环控制
                elif type_i == NodeType.DECIDER and type_j == NodeType.DECIDER:
                    match_score = 0.33  # 1/3 (近似): D->D 骨干态势同步

                # --- 其他链路 ---
                else:
                    # 包含所有涉及 INFLUENCER 的链路，以及非主流的 S->I 等，全部降级为底噪
                    match_score = EPSILON

            else:  # 打击阶段 (\Phi = 2)
                # --- 发送方为 DECIDER ---
                if type_i == NodeType.DECIDER and type_j == NodeType.DECIDER:
                    match_score = 0.20  # 1/5: D->D 火力分配解冲突与协同
                elif type_i == NodeType.DECIDER and type_j == NodeType.INFLUENCER:
                    match_score = 0.80  # 4/5: D->I 指令授权与火力下达

                # --- 其他链路 ---
                else:
                    # 侦察节点(S)的通信频率大幅下降让出带宽，打击节点(I)专注于接收指令
                    match_score = EPSILON

        else:
            match_score = EPSILON

        # 若关闭负载修正，直接返回基础匹配得分
        if not self.config.USE_LOGIC_LOAD_CORRECTION:
            return match_score

        # 2) 负载修正项 eta_load(j,t) = 1 - k_j(t)/K_max(t)
        degrees = dict(physical_layer.graph.degree())
        k_j = degrees.get(node_receiver.id, 0)
        k_max = max(degrees.values()) if degrees else 1

        eta_load = 1.0 - (k_j / k_max) if k_max > 0 else 1.0
        eta_load = max(0.1, eta_load)  # 极小保底，避免完全断连

        # 3) 返回最终逻辑层概率
        return match_score * eta_load
    
    def update(self, nodes: List[Node], physical_layer: PhysicalLayer, t: int):
        """
        更新通信层网络拓扑
        
        Args:
            nodes: 节点列表
            physical_layer: 物理层网络
            t: 当前时刻
        """
        self.graph.clear()
        self.activation_probabilities.clear()
        
        # 确定任务阶段（仅使用时间区间配置）
        phase = None
        for start, end, p in self.config.TASK_PHASE_SCHEDULE:
            if start <= t < end:
                phase = p
                break
        if phase is None:
            raise ValueError(f"时刻 {t} 未匹配到 TASK_PHASE_SCHEDULE，请检查配置区间是否覆盖全时域")
        
        # 添加所有存活节点
        for node in nodes:
            if node.is_alive:
                self.graph.add_node(node.id, node=node)
        
        node_dict = {node.id: node for node in nodes if node.is_alive}

        # 基于物理层和概率模型添加有向边
        for node_i_id, node_j_id in physical_layer.graph.edges():
            node_i = node_dict.get(node_i_id)
            node_j = node_dict.get(node_j_id)

            if node_i is None or node_j is None:
                continue

            distance = node_i.get_distance(node_j)
            p_phy = self._f_phy(distance)

            # 对同一条物理边分别尝试两个方向的通信意愿
            for sender, receiver in ((node_i, node_j), (node_j, node_i)):
                p_logic = self._f_logic(sender, receiver, phase, physical_layer)
                p_ij = p_phy * p_logic
                edge_key = (sender.id, receiver.id)
                self.activation_probabilities[edge_key] = p_ij

                if np.random.random() < p_ij:
                    self.graph.add_edge(
                        sender.id,
                        receiver.id,
                        probability=p_ij,
                        distance=distance,
                    )
    
    def get_adjacency_matrix(self):
        """获取邻接矩阵"""
        n = len(self.graph.nodes())
        if n == 0:
            return np.zeros((0, 0))
        adj = nx.adjacency_matrix(self.graph, nodelist=sorted(self.graph.nodes()))
        return adj.toarray()

class MissionLayer:
    """任务逻辑层：基于OODA规则的有向边"""
    
    def __init__(self, config: Config):
        self.config = config
        self.graph = nx.DiGraph()  # 有向图
        self.valid_paths = []  # 存储有效任务链
        
    def _is_valid_transition(self, from_type: NodeType, to_type: NodeType):
        """检查节点类型转换是否符合传输规则"""
        valid_rules = [
            (NodeType.SENSOR, NodeType.SENSOR),
            (NodeType.SENSOR, NodeType.DECIDER),
            (NodeType.DECIDER, NodeType.DECIDER),
            (NodeType.DECIDER, NodeType.SENSOR),
            (NodeType.DECIDER, NodeType.INFLUENCER),
        ]
        return (from_type, to_type) in valid_rules
    
    def _find_valid_paths(self, nodes: List[Node], task_graph):
        """
        搜索有效的OODA任务链（从S到I的完整闭环）
        
        Args:
            nodes: 节点列表
            task_graph: 任务层有向图（DiGraph）或通信层无向图（Graph）
            
        Returns:
            有效路径列表
        """
        valid_paths = []
        node_dict = {node.id: node for node in nodes if node.is_alive}
        
        # 找到所有侦察节点和打击节点
        sensor_nodes = [nid for nid, node in node_dict.items() 
                       if node.type == NodeType.SENSOR]
        influencer_nodes = [nid for nid, node in node_dict.items() 
                           if node.type == NodeType.INFLUENCER]
        
        # 调试信息
        if len(task_graph.edges()) == 0:
            return valid_paths
        
        if len(sensor_nodes) == 0 or len(influencer_nodes) == 0:
            return valid_paths
        
        # 对每个S-I对，搜索有效路径
        # 限制搜索数量以避免性能问题：每个传感器最多搜索最近的N个影响者
        max_targets_per_sensor = 5  # 限制每个传感器搜索的影响者数量
        
        for s_node_id in sensor_nodes:
            # 计算到所有影响者的距离，只搜索最近的几个
            sensor_node = node_dict[s_node_id]
            influencer_distances = []
            for i_node_id in influencer_nodes:
                if i_node_id == s_node_id:
                    continue
                influencer_node = node_dict[i_node_id]
                dist = sensor_node.get_distance(influencer_node)
                influencer_distances.append((i_node_id, dist))
            
            # 按距离排序，只取最近的几个
            influencer_distances.sort(key=lambda x: x[1])
            target_influencers = [iid for iid, _ in influencer_distances[:max_targets_per_sensor]]
            
            for i_node_id in target_influencers:
                # 使用BFS搜索所有从S到I的有效路径
                paths = self._bfs_valid_paths(task_graph, s_node_id, i_node_id, 
                                             node_dict, max_depth=4)  # 减少最大深度
                valid_paths.extend(paths)
                
                # 限制总路径数量，避免内存爆炸
                if len(valid_paths) > 1000:
                    break
            
            if len(valid_paths) > 1000:
                break
        
        return valid_paths
    
    def _bfs_valid_paths(self, graph, start: int, end: int, 
                        node_dict: Dict, max_depth: int = 5):
        """
        使用BFS搜索有效路径
        
        Args:
            graph: 图对象（可以是Graph或DiGraph）
            start: 起点节点ID
            end: 终点节点ID
            node_dict: 节点字典
            max_depth: 最大路径长度
        """
        from collections import deque
        
        paths = []
        
        # 检查起点和终点是否在图中
        if start not in graph or end not in graph:
            return paths
        
        # 移除昂贵的has_path检查，直接进行BFS搜索
        # 如果不存在路径，BFS自然会返回空列表
        
        queue = deque([([start], node_dict[start].type)])
        visited_paths = set()  # 避免重复路径
        
        while queue:
            path, last_type = queue.popleft()
            
            if len(path) > max_depth:
                continue
            
            current = path[-1]
            
            # 如果到达终点
            if current == end and len(path) > 1:
                # 如果使用有向图，边已经符合传输规则，直接添加
                # 如果使用无向图，需要检查最后一步是否有效
                if isinstance(graph, nx.DiGraph):
                    path_tuple = tuple(path)
                    if path_tuple not in visited_paths:
                        paths.append(path)
                        visited_paths.add(path_tuple)
                else:
                    # 无向图需要检查传输规则
                    if self._is_valid_transition(last_type, node_dict[end].type):
                        path_tuple = tuple(path)
                        if path_tuple not in visited_paths:
                            paths.append(path)
                            visited_paths.add(path_tuple)
                continue
            
            # 遍历邻居（有向图使用successors，无向图使用neighbors）
            if current in graph:
                if isinstance(graph, nx.DiGraph):
                    neighbors = graph.successors(current)
                else:
                    neighbors = graph.neighbors(current)
                
                for neighbor in neighbors:
                    if neighbor in path:  # 避免循环
                        continue
                    
                    # 检查节点是否存在
                    if neighbor not in node_dict:
                        continue
                    
                    # 如果使用有向图，边已经符合传输规则，直接添加
                    # 如果使用无向图，需要检查传输规则
                    if isinstance(graph, nx.DiGraph):
                        queue.append((path + [neighbor], node_dict[neighbor].type))
                    else:
                        neighbor_type = node_dict[neighbor].type
                        if self._is_valid_transition(last_type, neighbor_type):
                            queue.append((path + [neighbor], neighbor_type))
        
        return paths
    
    def update(self, nodes: List[Node], comm_layer: CommunicationLayer):
        """
        更新任务层网络拓扑
        
        Args:
            nodes: 节点列表
            comm_layer: 通信层网络
        """
        self.graph.clear()
        self.valid_paths.clear()
        
        # 添加所有存活节点
        for node in nodes:
            if node.is_alive:
                self.graph.add_node(node.id, node=node)
        
        # 创建节点ID到节点的映射以提高查找效率
        node_dict = {node.id: node for node in nodes}

        # 基于通信链路的激活概率和阈值，添加有向边
        prob_threshold = self.config.MISSION_PROB_THRESHOLD
        
        for edge, prob in comm_layer.activation_probabilities.items():
            if prob < prob_threshold:
                continue

            node_i_id, node_j_id = edge
            
            # 使用字典进行O(1)查找
            node_i = node_dict.get(node_i_id)
            node_j = node_dict.get(node_j_id)

            if not node_i or not node_j:
                continue
            
            # 通信层已经是有向边概率，这里只保留符合任务传输规则的方向
            if self._is_valid_transition(node_i.type, node_j.type):
                self.graph.add_edge(node_i_id, node_j_id)
        
        # 搜索有效任务链（使用任务层有向图，而不是通信层无向图）
        # 因为任务链需要遵循有向的传输规则
        self.valid_paths = self._find_valid_paths(nodes, self.graph)
        
        # 调试信息（可选，取消注释以查看）
        # if len(self.valid_paths) == 0:
        #     alive_nodes = [n for n in nodes if n.is_alive]
        #     sensor_count = sum(1 for n in alive_nodes if n.type == NodeType.SENSOR)
        #     decider_count = sum(1 for n in alive_nodes if n.type == NodeType.DECIDER)
        #     influencer_count = sum(1 for n in alive_nodes if n.type == NodeType.INFLUENCER)
        #     comm_edges = comm_layer.graph.number_of_edges()
        #     print(f"任务链为0: S={sensor_count}, D={decider_count}, I={influencer_count}, 通信边={comm_edges}")
    
    def get_adjacency_matrix(self):
        """获取邻接矩阵"""
        n = len(self.graph.nodes())
        if n == 0:
            return np.zeros((0, 0))
        adj = nx.adjacency_matrix(self.graph, nodelist=sorted(self.graph.nodes()))
        return adj.toarray()
    
    def get_total_mission_efficiency(self, initial_efficiency):
        """
        计算累计任务效能
        
        Args:
            initial_efficiency: 初始效能（用于归一化）
            
        Returns:
            归一化的任务效能
        """
        if initial_efficiency == 0:
            return 0.0
        
        total_efficiency = 0.0
        for path in self.valid_paths:
            # 路径效率为路径长度的倒数
            path_length = len(path) - 1  # 跳数
            if path_length > 0:
                total_efficiency += 1.0 / path_length
        
        return total_efficiency / initial_efficiency if initial_efficiency > 0 else 0.0
