"""
攻击模块：实现物理毁伤与网络压制攻击
"""
import numpy as np
from typing import List
from node import Node, NodeType


class AttackModule:
    """攻击模块"""

    def __init__(self, config):
        """
        初始化攻击模块

        Args:
            config: 配置对象
        """
        self.config = config
        self.attack_time = config.ATTACK_TIME

        # 默认攻击规模：优先使用比例配置
        alive_base = getattr(config, 'N_TOTAL', 0)
        ratio = getattr(config, 'ATTACK_RATIO', None)
        if ratio is not None:
            self.default_attack_count = max(0, int(round(alive_base * ratio)))
        else:
            self.default_attack_count = getattr(config, 'ATTACK_NODES', 0)

        # 执行记录
        self.attacked_nodes = []          # 物理毁伤节点ID
        self.jammed_nodes = []            # 网络压制节点ID
        self.active_jam_node_ids = set()  # 当前处于压制窗口的节点ID

    def execute_attack(self,
                       nodes: List[Node],
                       current_time: int,
                       graph=None):
        """
        在攻击时刻执行一次目标选择与打击。

        Args:
            nodes: 节点列表
            current_time: 当前时刻
            graph: 用于度数蓄意打击的图（建议传通信层图）

        Returns:
            是否在本时刻执行了“首次打击动作”
        """
        # 非打击时刻不选新目标
        if current_time != self.attack_time:
            return False

        alive_nodes = [n for n in nodes if n.is_alive]
        if not alive_nodes:
            return False

        targets = self._select_targets(alive_nodes, graph)
        attack_mode = str(self.config.ATTACK_MODE).lower()

        if attack_mode == 'physical':
            # 硬杀伤：节点永久剔除
            for node in targets:
                node.attack()
                self.attacked_nodes.append(node.id)

        elif attack_mode == 'cyber':
            # 软杀伤：节点仍存活，仅压制通信
            self.jammed_nodes = [node.id for node in targets]
            self.active_jam_node_ids = set(self.jammed_nodes)

        else:
            raise ValueError(
                f"不支持的 ATTACK_MODE={self.config.ATTACK_MODE}，"
                f"仅支持 'physical' 或 'cyber'"
            )

        return True

    def update_cyber_window(self, current_time: int):
        """根据压制时间窗更新当前生效的受压节点集合。"""
        if str(self.config.ATTACK_MODE).lower() != 'cyber':
            self.active_jam_node_ids = set()
            return

        recover_time = getattr(self.config, 'ATTACK_RECOVER_TIME', self.attack_time)
        if self.attack_time <= current_time <= recover_time:
            self.active_jam_node_ids = set(self.jammed_nodes)
        else:
            self.active_jam_node_ids = set()

    def apply_communication_suppression(self, comm_layer, current_time: int):
        """
        对通信层施加网络压制效果：
        对任意 i∈V_jam，强制 P_ij(t)=0，并移除通信图中的相关边。
        """
        self.update_cyber_window(current_time)
        if not self.active_jam_node_ids:
            return

        # 概率强制清零
        for edge_key in list(comm_layer.activation_probabilities.keys()):
            i, j = edge_key
            if i in self.active_jam_node_ids or j in self.active_jam_node_ids:
                comm_layer.activation_probabilities[edge_key] = 0.0

        # 已激活边同步移除，保持图/概率一致
        for u, v in list(comm_layer.graph.edges()):
            if u in self.active_jam_node_ids or v in self.active_jam_node_ids:
                comm_layer.graph.remove_edge(u, v)

    def _select_targets(self, nodes: List[Node], graph=None):
        """按配置的目标选择策略挑选打击对象。"""
        strategy = str(self.config.ATTACK_STRATEGY).lower()
        attack_count = self._resolve_attack_count(len(nodes))

        if attack_count <= 0:
            return []

        if strategy == 'random':
            return self._random_attack(nodes, attack_count)
        if strategy == 'topology':
            return self._topology_attack(nodes, attack_count, graph)
        if strategy == 'role':
            role_type = str(self.config.ATTACK_ROLE_TARGET).upper()
            return self._role_attack(nodes, attack_count, role_type)

        # 兼容旧配置
        if strategy == 'high_degree':
            return self._topology_attack(nodes, attack_count, graph)
        if strategy == 'critical':
            role_type = str(getattr(self.config, 'ATTACK_TARGET_TYPE', 'DECIDER')).upper()
            return self._role_attack(nodes, attack_count, role_type)

        return self._random_attack(nodes, attack_count)

    def _resolve_attack_count(self, alive_count: int) -> int:
        """计算本轮攻击节点数量。"""
        ratio = getattr(self.config, 'ATTACK_RATIO', None)
        if ratio is not None:
            count = int(round(alive_count * ratio))
        else:
            count = self.default_attack_count
        return max(0, min(count, alive_count))

    @staticmethod
    def _random_attack(nodes: List[Node], attack_count: int):
        """随机打击。"""
        if attack_count <= 0:
            return []
        return np.random.choice(nodes, size=attack_count, replace=False).tolist()

    def _topology_attack(self, nodes: List[Node], attack_count: int, graph=None):
        """拓扑蓄意打击：优先攻击高度数节点。"""
        if attack_count <= 0:
            return []

        # 无图信息时退化为随机
        if graph is None:
            return self._random_attack(nodes, attack_count)

        node_degrees = []
        for node in nodes:
            degree = graph.degree(node.id) if node.id in graph else 0
            node_degrees.append((node, degree))

        # 度数降序，ID升序保证稳定
        node_degrees.sort(key=lambda x: (-x[1], x[0].id))
        return [node for node, _ in node_degrees[:attack_count]]

    def _role_attack(self, nodes: List[Node], attack_count: int, target_type='DECIDER'):
        """角色导向打击：优先指定角色节点，不足则补齐。"""
        type_map = {
            'SENSOR': NodeType.SENSOR,
            'DECIDER': NodeType.DECIDER,
            'INFLUENCER': NodeType.INFLUENCER,
        }
        target_enum = type_map.get(target_type, NodeType.DECIDER)

        typed_nodes = [n for n in nodes if n.type == target_enum]
        if len(typed_nodes) >= attack_count:
            return np.random.choice(typed_nodes, size=attack_count, replace=False).tolist()

        targets = typed_nodes.copy()
        other_nodes = [n for n in nodes if n.type != target_enum]
        remaining = attack_count - len(targets)
        if remaining > 0 and other_nodes:
            targets.extend(
                np.random.choice(other_nodes, size=min(remaining, len(other_nodes)), replace=False).tolist()
            )
        return targets
