"""
节点类：定义无人机节点及其属性
"""
import numpy as np
from enum import Enum

class NodeType(Enum):
    """节点类型枚举"""
    SENSOR = 0    # 侦察节点 (V_S)
    DECIDER = 1   # 通信节点 (V_D)
    INFLUENCER = 2  # 打击节点 (V_I)

class Node:
    """无人机节点类"""
    
    def __init__(self, node_id, node_type, position, config):
        """
        初始化节点
        
        Args:
            node_id: 节点唯一标识
            node_type: 节点类型 (NodeType)
            position: 节点位置 [x, y]
            config: 配置对象
        """
        self.id = node_id
        self.type = node_type
        self.position = np.array(position, dtype=np.float64)
        self.config = config
        
        # 节点状态
        self.is_alive = True  # 是否存活
        self.is_attacked = False  # 是否被攻击
        
        # 节点属性向量（One-hot编码）
        self.attribute_vector = self._get_attribute_vector()
        
        # 记忆信息（用于恢复策略）
        self.memory_center = None  # 记忆中的集群重心
        self.last_update_time = 0
        
    def _get_attribute_vector(self):
        """获取节点功能属性向量 [Sensor, Decider, Influencer]"""
        vec = np.zeros(3, dtype=int)
        if self.type == NodeType.SENSOR:
            vec[0] = 1
        elif self.type == NodeType.DECIDER:
            vec[1] = 1
        elif self.type == NodeType.INFLUENCER:
            vec[2] = 1
        return vec
    
    def get_distance(self, other_node):
        """计算到另一个节点的欧氏距离"""
        if not other_node.is_alive:
            return np.inf
        return np.linalg.norm(self.position - other_node.position)
    
    def is_in_communication_range(self, other_node):
        """判断是否在通信范围内"""
        return self.get_distance(other_node) <= self.config.R_COMM
    
    def is_in_sensor_range(self, other_node):
        """判断是否在感知范围内"""
        return self.get_distance(other_node) <= self.config.R_SENSOR
    
    def move_towards(self, target_position, speed=None, other_nodes=None):
        """
        向目标位置移动，同时避免与其他节点距离过近
        
        Args:
            target_position: 目标位置 [x, y]
            speed: 移动速度（默认使用配置中的速度）
            other_nodes: 其他节点列表（用于避免碰撞），如果为None则不检查
        """
        if speed is None:
            speed = self.config.RECOVERY_SPEED
        
        min_distance = self.config.get_min_node_distance()
        
        direction = np.array(target_position) - self.position
        distance = np.linalg.norm(direction)
        
        if distance > 0:
            # 归一化方向向量
            direction = direction / distance
            # 移动距离不超过速度
            move_distance = min(distance, speed * self.config.DT)
            new_position = self.position + direction * move_distance
            
            # 如果提供了其他节点列表，检查并避免碰撞
            if other_nodes is not None:
                new_position = self._avoid_collision(new_position, other_nodes, min_distance)
            
            self.position = new_position
            
            # 确保节点在区域内
            self.position = np.clip(self.position, 0, self.config.AREA_SIZE)
    
    def _avoid_collision(self, new_position, other_nodes, min_distance):
        """
        调整新位置以避免与其他节点距离过近
        
        Args:
            new_position: 计划的新位置
            other_nodes: 其他节点列表
            min_distance: 最小距离
            
        Returns:
            调整后的位置
        """
        adjusted_position = np.array(new_position)
        max_iterations = 10  # 最大调整次数
        iteration = 0
        
        while iteration < max_iterations:
            too_close = False
            repulsion_force = np.zeros(2)
            
            # 检查与其他节点的距离
            for other_node in other_nodes:
                if not other_node.is_alive or other_node.id == self.id:
                    continue
                
                distance = np.linalg.norm(adjusted_position - other_node.position)
                
                if distance < min_distance and distance > 0:
                    too_close = True
                    # 计算排斥力方向（从其他节点指向当前节点）
                    repulsion_dir = (adjusted_position - other_node.position) / distance
                    # 排斥力大小与距离成反比
                    repulsion_strength = (min_distance - distance) / min_distance
                    repulsion_force += repulsion_dir * repulsion_strength
            
            if not too_close:
                break
            
            # 应用排斥力调整位置
            adjustment = repulsion_force * min_distance * 0.5
            adjusted_position += adjustment
            
            # 确保在区域内
            adjusted_position = np.clip(adjusted_position, 0, self.config.AREA_SIZE)
            
            iteration += 1
        
        return adjusted_position
    
    def attack(self):
        """攻击节点"""
        self.is_attacked = True
        self.is_alive = False
    
    def recover(self):
        """恢复节点（如果节点只是受损而非完全摧毁）"""
        if self.is_attacked and not self.is_alive:
            # 这里可以根据需要实现部分恢复逻辑
            pass
    
    def update_memory(self, cluster_center, current_time):
        """更新记忆中的集群重心"""
        self.memory_center = np.array(cluster_center)
        self.last_update_time = current_time
    
    def __repr__(self):
        return f"Node(id={self.id}, type={self.type.name}, pos={self.position}, alive={self.is_alive})"

