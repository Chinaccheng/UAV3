"""
主实验流程模块
"""
from typing import List, Dict, Tuple
from node import Node, NodeType
from network_layers import PhysicalLayer, CommunicationLayer, MissionLayer
from performance import PerformanceEvaluator
from attack import AttackModule
from recovery import RecoveryStrategy
from config import Config
from experiment_common import (
    calculate_resilience,
    get_attack_reference_graph,
    initialize_nodes,
    update_networks,
)

class Experiment:
    """实验主类"""
    
    def __init__(self, config: Config):
        """
        初始化实验
        
        Args:
            config: 配置对象
        """
        self.config = config
        self.nodes: List[Node] = []
        self.physical_layer = PhysicalLayer(config)
        self.comm_layer = CommunicationLayer(config)
        self.mission_layer = MissionLayer(config)
        self.performance_evaluator = PerformanceEvaluator(config)
        self.attack_module = AttackModule(config)
        self.recovery_strategy = RecoveryStrategy(config, self.performance_evaluator)
        
        # 记录实验数据
        self.history = {
            'time': [],
            'Q_phy': [],
            'Q_comm': [],
            'Q_mis': [],
            'Q_overall': [],
            'num_alive_nodes': [],
            'num_edges_phy': [],
            'num_edges_comm': [],
            'num_edges_mis': [],
        }
        
        # 保存关键时刻的节点状态快照
        self.snapshots = {}
    
    def initialize_nodes(self):
        """初始化节点"""
        self.nodes = initialize_nodes(self.config)
        print(f"初始化完成：{self.config.N_SENSOR}个侦察节点，"
              f"{self.config.N_DECIDER}个通信节点，"
              f"{self.config.N_INFLUENCER}个打击节点")
    
    def update_networks(self, t: int):
        """更新三层网络"""
        update_networks(
            self.config,
            self.nodes,
            self.physical_layer,
            self.comm_layer,
            self.mission_layer,
            self.attack_module,
            t,
        )
    
    def run(self):
        """运行实验"""
        print("开始实验...")
        
        # 初始化节点
        self.initialize_nodes()
        
        # 初始化网络
        self.update_networks(0)
        
        # 记录初始性能
        Q_phy, Q_comm, Q_mis, Q_overall = self.performance_evaluator.calculate_overall_performance(
            self.nodes, self.physical_layer, self.comm_layer, self.mission_layer)
        
        self._record_state(0, Q_phy, Q_comm, Q_mis, Q_overall)
        
        # 主循环
        for t in range(1, self.config.TIME_STEPS + 1):
            attack_graph = self._get_attack_reference_graph()

            # 执行攻击（打击时刻选择并作用目标）
            self.attack_module.execute_attack(
                self.nodes,
                t,
                graph=attack_graph,
            )

            # 执行恢复策略（仅对物理毁伤场景生效）
            if t > self.config.ATTACK_TIME and self.config.ATTACK_MODE == 'physical':
                self.recovery_strategy.execute_recovery(
                    self.nodes, self.comm_layer, t)

            # 更新网络（内部包含物理层->通信层->网络压制->任务层的时序）
            self.update_networks(t)
            
            # 计算性能
            Q_phy, Q_comm, Q_mis, Q_overall = self.performance_evaluator.calculate_overall_performance(
                self.nodes, self.physical_layer, self.comm_layer, self.mission_layer)
            
            # 记录状态
            self._record_state(t, Q_phy, Q_comm, Q_mis, Q_overall)
            
            # 保存关键时刻的快照
            snapshot_times = self.config.get_snapshot_times()
            if t in snapshot_times:
                self._save_snapshot(t)
            
            # 打印进度
            if t % 10 == 0:
                num_alive = sum(1 for n in self.nodes if n.is_alive)
                print(f"时刻 {t}: 存活节点={num_alive}, "
                      f"综合性能={Q_overall:.3f}")
        
        print("实验完成！")
        return self.history

    def _get_attack_reference_graph(self):
        """根据配置返回拓扑蓄意打击使用的度数参考网络层。"""
        return get_attack_reference_graph(self.config, self.physical_layer, self.comm_layer)
    
    def _record_state(self, t: int, Q_phy: float, Q_comm: float, 
                     Q_mis: float, Q_overall: float):
        """记录实验状态"""
        self.history['time'].append(t)
        self.history['Q_phy'].append(Q_phy)
        self.history['Q_comm'].append(Q_comm)
        self.history['Q_mis'].append(Q_mis)
        self.history['Q_overall'].append(Q_overall)
        
        num_alive = sum(1 for n in self.nodes if n.is_alive)
        self.history['num_alive_nodes'].append(num_alive)
        self.history['num_edges_phy'].append(self.physical_layer.graph.number_of_edges())
        self.history['num_edges_comm'].append(self.comm_layer.graph.number_of_edges())
        self.history['num_edges_mis'].append(self.mission_layer.graph.number_of_edges())
    
    def _save_snapshot(self, t: int):
        """保存关键时刻的快照"""
        import copy
        # 保存节点位置和状态
        node_states = []
        for node in self.nodes:
            node_states.append({
                'id': node.id,
                'type': node.type,
                'position': node.position.copy(),
                'is_alive': node.is_alive,
            })
        self.snapshots[t] = {
            'nodes': node_states,
            'physical_layer': copy.deepcopy(self.physical_layer.graph),
            'comm_layer': copy.deepcopy(self.comm_layer.graph),
            'mission_layer': copy.deepcopy(self.mission_layer.graph),
        }
    
    def get_snapshot(self, t: int):
        """获取指定时刻的快照"""
        return self.snapshots.get(t, None)
    
    def calculate_resilience(self):
        """
        计算韧性度量指标 R
        
        Returns:
            韧性值
        """
        return calculate_resilience(
            self.history,
            trigger_time=self.config.ATTACK_TIME,
            q_min=self.config.Q_MIN,
            lambda_=self.config.LAMBDA,
        )
