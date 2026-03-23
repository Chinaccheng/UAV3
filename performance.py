"""
性能评估模块：计算物理层、通信层、任务层性能
"""
import numpy as np
import networkx as nx
from typing import List
from node import Node
from network_layers import PhysicalLayer, CommunicationLayer, MissionLayer
from config import Config

class PerformanceEvaluator:
    """性能评估器"""
    
    def __init__(self, config: Config):
        self.config = config
        self.initial_values = {}  # 存储初始值用于归一化
        
    def calculate_physical_performance(self, nodes: List[Node], 
                                     physical_layer: PhysicalLayer):
        """
        计算物理层性能 Q_phy(t)
        
        Args:
            nodes: 节点列表
            physical_layer: 物理层网络
            
        Returns:
            物理层性能值
        """
        alive_nodes = [n for n in nodes if n.is_alive]
        n_alive = len(alive_nodes)
        n_total = self.config.N_TOTAL
        
        if n_alive == 0:
            return 0.0
        
        graph = physical_layer.graph
        if len(graph.nodes()) == 0:
            return 0.0
        
        # 计算平均度
        degrees = dict(graph.degree())
        avg_degree = np.mean(list(degrees.values())) if degrees else 0.0
        
        # 计算平均聚类系数
        clustering = nx.clustering(graph)
        avg_clustering = np.mean(list(clustering.values())) if clustering else 0.0
        
        # 计算全局效率（平均路径长度的倒数）
        try:
            global_efficiency = nx.global_efficiency(graph)
        except:
            global_efficiency = 0.0
        
        # 初始化时存储初始值
        if 'K0' not in self.initial_values:
            self.initial_values['K0'] = avg_degree if avg_degree > 0 else 1.0
            self.initial_values['C0'] = avg_clustering if avg_clustering > 0 else 1.0
            self.initial_values['GE0'] = global_efficiency if global_efficiency > 0 else 1.0
        
        # 归一化
        K_norm = avg_degree / self.initial_values['K0'] if self.initial_values['K0'] > 0 else 0.0
        C_norm = avg_clustering / self.initial_values['C0'] if self.initial_values['C0'] > 0 else 0.0
        GE_norm = global_efficiency / self.initial_values['GE0'] if self.initial_values['GE0'] > 0 else 0.0
        
        # 节点数量归一化
        n_norm = n_alive / n_total
        
        # 综合性能
        alpha = self.config.ALPHA
        beta = self.config.BETA
        gamma = self.config.GAMMA

        Q_phy = n_norm * (alpha * K_norm + beta * C_norm + gamma * GE_norm)
        
        return Q_phy
    
    def calculate_communication_performance(self, comm_layer: CommunicationLayer):
        """
        计算通信层性能 Q_comm(t)
        采用强度与有序度解耦方案：结合通信总概率(强度)与分布倾向(信息熵)
        修复低概率残存链路导致的“假性低熵”评分飙升问题
        """
        graph = comm_layer.graph
        nodes = list(graph.nodes())
        N = len(nodes)
        
        # 如果节点数太少，无法形成有效通信
        if N <= 1:
            return 0.0
            
        # 理论最大熵 H_max = ln(N-1) (用于归一化和孤立节点惩罚)
        h_max = np.log(N - 1) if N > 1 else 1.0
        if h_max <= 0:
            h_max = 1e-10
            
        total_q_comm = 0.0
        
        # 1. 遍历每个存活节点，计算局部通信性能
        for node_id in nodes:
            # 获取该节点与其他所有节点的激活概率 P_ij
            p_ij_list = []
            for other_id in nodes:
                if node_id == other_id:
                    continue
                    
                # 从通信层字典中读取理论交互概率 P_ij
                edge_key = tuple(sorted([node_id, other_id]))
                p_ij = comm_layer.activation_probabilities.get(edge_key, 0.0)
                
                if p_ij > 0:
                    p_ij_list.append(p_ij)
                    
            sum_p = sum(p_ij_list)
            
            # 2. 计算通信倾向分布 π_ij 和 个体熵 H_i
            if sum_p > 0:
                h_i = 0.0
                for p_ij in p_ij_list:
                    pi_ij = p_ij / sum_p  # 归一化得到 π_ij
                    if pi_ij > 0:
                        h_i -= pi_ij * np.log(pi_ij)  # -Σ π_ij * ln(π_ij)
            else:
                # 节点完全孤立，给予最大混乱度惩罚
                h_i = h_max
                
            # 3. 核心修改：强度与有序度双变量解耦计算
            # 强度乘数：节点总连接概率越低，惩罚越严重；概率越大，越趋近于1
            intensity_weight = 1.0 - np.exp(-sum_p)
            
            # 有序度得分：原本的信息熵得分逻辑
            order_score = max(0.0, 1.0 - (h_i / h_max))
            
            # 节点 i 的真实通信性能 = 通信能力强度 × 目标指向有序度
            q_i = intensity_weight * order_score
            
            total_q_comm += q_i
            
        # 4. 计算全网平均绝对通信性能
        raw_avg_q_comm = total_q_comm / N

        # 5. 引入归一化参数 μ：令初始时刻 Q_comm(0)=1
        if 'MU_comm' not in self.initial_values:
            self.initial_values['MU_comm'] = 1.0 / raw_avg_q_comm if raw_avg_q_comm > 0 else 1.0

        mu = self.initial_values['MU_comm']
        final_q_comm = mu * raw_avg_q_comm
        
        # 确保在 [0, 1] 范围内
        return max(0.0, min(final_q_comm, 1.0))
    
    def calculate_mission_performance(self, mission_layer: MissionLayer):
        """
        计算任务层性能 Q_mis(t)
        
        Args:
            mission_layer: 任务层网络
            
        Returns:
            任务层性能值
        """
        # 计算累计任务效能
        total_efficiency = 0.0
        for path in mission_layer.valid_paths:
            path_length = len(path) - 1  # 跳数
            if path_length > 0:
                total_efficiency += 1.0 / path_length
        
        # 初始化时存储初始效能
        if 'E0' not in self.initial_values:
            self.initial_values['E0'] = total_efficiency if total_efficiency > 0 else 1.0
        
        # 归一化
        E0 = self.initial_values['E0']
        if E0 == 0:
            return 0.0
        
        Q_mis = total_efficiency / E0
        
        return Q_mis
    
    def calculate_overall_performance(self, nodes: List[Node],
                                     physical_layer: PhysicalLayer,
                                     comm_layer: CommunicationLayer,
                                     mission_layer: MissionLayer):
        """
        计算系统综合性能
        
        Returns:
            (Q_phy, Q_comm, Q_mis, Q_overall)
        """
        Q_phy = self.calculate_physical_performance(nodes, physical_layer)
        Q_comm = self.calculate_communication_performance(comm_layer)
        Q_mis = self.calculate_mission_performance(mission_layer)
        
        # 综合性能（按配置权重计算）
        Q_overall = (
            self.config.W1 * Q_phy
            + self.config.W2 * Q_comm
            + self.config.W3 * Q_mis
        )
        
        return Q_phy, Q_comm, Q_mis, Q_overall
    
    def reset_initial_values(self):
        """重置初始值（用于新的实验）"""
        self.initial_values.clear()

