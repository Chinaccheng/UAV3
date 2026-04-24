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
        self.attack_duration = max(1, int(getattr(config, 'ATTACK_DURATION', 1)))
        self.attack_start_time = max(1, self.attack_time - self.attack_duration + 1)
        self.attack_end_time = self.attack_time

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
        self._attack_batches = None
        self._last_applied_batch_index = -1

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
        if current_time < self.attack_start_time or current_time > self.attack_end_time:
            return False

        if self._attack_batches is None:
            alive_nodes = [n for n in nodes if n.is_alive]
            if not alive_nodes:
                return False
            targets = self._select_targets(alive_nodes, graph)
            self._attack_batches = self._split_targets(targets, self.attack_duration)

        batch_index = current_time - self.attack_start_time
        if batch_index <= self._last_applied_batch_index or batch_index >= len(self._attack_batches):
            return False

        targets = self._attack_batches[batch_index]
        attack_mode = str(self.config.ATTACK_MODE).lower()

        if attack_mode == 'physical':
            for node in targets:
                if node.is_alive:
                    node.attack()
                if node.id not in self.attacked_nodes:
                    self.attacked_nodes.append(node.id)

        elif attack_mode == 'cyber':
            for node in targets:
                if node.id not in self.jammed_nodes:
                    self.jammed_nodes.append(node.id)
            self.active_jam_node_ids = set(self.jammed_nodes)

        else:
            raise ValueError(
                f"不支持的 ATTACK_MODE={self.config.ATTACK_MODE}，"
                f"仅支持 'physical' 或 'cyber'"
            )

        self._last_applied_batch_index = batch_index
        return len(targets) > 0

    def update_cyber_window(self, current_time: int):
        """根据压制时间窗更新当前生效的受压节点集合。"""
        if str(self.config.ATTACK_MODE).lower() != 'cyber':
            self.active_jam_node_ids = set()
            return

        recover_time = getattr(self.config, 'ATTACK_RECOVER_TIME', self.attack_end_time)
        if self.attack_start_time <= current_time <= recover_time:
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
            return self._role_attack(nodes, attack_count, role_type, graph)

        # 兼容旧配置
        if strategy == 'high_degree':
            return self._topology_attack(nodes, attack_count, graph)
        if strategy == 'critical':
            role_type = str(getattr(self.config, 'ATTACK_TARGET_TYPE', 'DECIDER')).upper()
            return self._role_attack(nodes, attack_count, role_type, graph)

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

    def _role_attack(self, nodes: List[Node], attack_count: int, target_type='DECIDER', graph=None):
        """角色导向打击：优先指定角色中的关键节点，不足时按级联规则补齐。"""
        type_map = {
            'SENSOR': NodeType.SENSOR,
            'DECIDER': NodeType.DECIDER,
            'INFLUENCER': NodeType.INFLUENCER,
        }
        target_enum = type_map.get(target_type, NodeType.DECIDER)

        typed_nodes = [n for n in nodes if n.type == target_enum]
        if graph is not None and typed_nodes:
            typed_nodes.sort(key=lambda node: (-graph.degree(node.id) if node.id in graph else 0, node.id))
        if len(typed_nodes) >= attack_count:
            return typed_nodes[:attack_count]

        targets = typed_nodes.copy()
        remaining = attack_count - len(targets)
        if remaining <= 0:
            return targets

        cascade_enabled = getattr(self.config, 'ATTACK_ROLE_CASCADE_ENABLED', False)
        cascade_sequence = getattr(self.config, 'ATTACK_ROLE_CASCADE_SEQUENCE', None)

        if cascade_enabled and cascade_sequence:
            selected_ids = {node.id for node in targets}
            for rule in cascade_sequence:
                if remaining <= 0:
                    break

                available_nodes = [n for n in nodes if n.id not in selected_ids]
                if not available_nodes:
                    break

                rule_upper = str(rule).upper()
                chosen_nodes = []

                if rule_upper in type_map:
                    cascade_enum = type_map[rule_upper]
                    role_nodes = [n for n in available_nodes if n.type == cascade_enum]
                    if role_nodes:
                        take_count = min(remaining, len(role_nodes))
                        chosen_nodes = np.random.choice(
                            role_nodes, size=take_count, replace=False
                        ).tolist()
                elif rule_upper in ('TOPOLOGY', 'DEGREE', 'HIGH_DEGREE'):
                    chosen_nodes = self._topology_attack(available_nodes, remaining, graph)
                elif rule_upper == 'RANDOM':
                    take_count = min(remaining, len(available_nodes))
                    chosen_nodes = np.random.choice(
                        available_nodes, size=take_count, replace=False
                    ).tolist()

                if not chosen_nodes:
                    continue

                targets.extend(chosen_nodes)
                selected_ids.update(node.id for node in chosen_nodes)
                remaining = attack_count - len(targets)

        if remaining > 0:
            selected_ids = {node.id for node in targets}
            available_nodes = [n for n in nodes if n.id not in selected_ids]
            if available_nodes:
                take_count = min(remaining, len(available_nodes))
                targets.extend(
                    np.random.choice(available_nodes, size=take_count, replace=False).tolist()
                )
        return targets

    @staticmethod
    def _allocate_weighted_batch_sizes(total: int, weights: List[float]) -> List[int]:
        """按权重分配每个时刻的打击数量，并保证总数守恒。"""
        if total <= 0:
            return [0 for _ in weights]

        safe_weights = [max(0.0, float(weight)) for weight in weights]
        weight_sum = sum(safe_weights)
        if weight_sum <= 0.0:
            raise ValueError("ATTACK_BATCH_WEIGHTS 的权重和必须大于 0")

        raw_sizes = [total * weight / weight_sum for weight in safe_weights]
        batch_sizes = [int(np.floor(size)) for size in raw_sizes]
        remainder = total - sum(batch_sizes)
        if remainder > 0:
            ranked_indices = sorted(
                range(len(raw_sizes)),
                key=lambda index: (raw_sizes[index] - batch_sizes[index], safe_weights[index], -index),
                reverse=True,
            )
            for index in ranked_indices[:remainder]:
                batch_sizes[index] += 1
        return batch_sizes

    def _split_targets(self, targets: List[Node], parts: int) -> List[List[Node]]:
        """将目标节点分摊到多个连续时间步，可按显式权重生成不均匀批次。"""
        if parts <= 1:
            return [list(targets)]

        targets = list(targets)
        total = len(targets)
        configured_weights = getattr(self.config, 'ATTACK_BATCH_WEIGHTS', None)
        if configured_weights is not None:
            if len(configured_weights) != parts:
                raise ValueError(
                    f"ATTACK_BATCH_WEIGHTS 长度必须与 ATTACK_DURATION 一致: {len(configured_weights)} != {parts}"
                )
            batch_sizes = self._allocate_weighted_batch_sizes(total, configured_weights)
        else:
            base_size, remainder = divmod(total, parts)
            batch_sizes = []
            for batch_index in range(parts):
                batch_sizes.append(base_size + (1 if batch_index < remainder else 0))

        batches: List[List[Node]] = []
        start = 0
        for batch_size in batch_sizes:
            end = start + batch_size
            batches.append(targets[start:end])
            start = end
        return batches
