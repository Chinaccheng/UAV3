"""
实验公共工具：复用主项目、实验一、实验二的通用初始化与评估逻辑。
"""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, Iterable, List

import numpy as np

from attack import AttackModule
from network_layers import CommunicationLayer, MissionLayer, PhysicalLayer
from node import Node, NodeType


def initialize_nodes(config) -> List[Node]:
    """按统一规则初始化三类节点。"""
    np.random.seed(config.RANDOM_SEED)
    nodes: List[Node] = []
    node_id = 0

    for _ in range(config.N_SENSOR):
        position = np.random.uniform(0, config.AREA_SIZE, size=2)
        nodes.append(Node(node_id, NodeType.SENSOR, position, config))
        node_id += 1

    for _ in range(config.N_DECIDER):
        position = np.random.uniform(0, config.AREA_SIZE, size=2)
        nodes.append(Node(node_id, NodeType.DECIDER, position, config))
        node_id += 1

    for _ in range(config.N_INFLUENCER):
        position = np.random.uniform(0, config.AREA_SIZE, size=2)
        nodes.append(Node(node_id, NodeType.INFLUENCER, position, config))
        node_id += 1

    return nodes


def update_networks(
    config,
    nodes: List[Node],
    physical_layer: PhysicalLayer,
    comm_layer: CommunicationLayer,
    mission_layer: MissionLayer,
    attack_module: AttackModule,
    t: int,
) -> None:
    """复用主工程一致的跨层更新顺序。"""
    physical_layer.update(nodes)
    comm_layer.update(nodes, physical_layer, t)
    attack_module.apply_communication_suppression(comm_layer, t)
    mission_layer.update(nodes, comm_layer)


def get_attack_reference_graph(config, physical_layer: PhysicalLayer, comm_layer: CommunicationLayer):
    """根据配置返回拓扑攻击使用的参考图。"""
    if getattr(config, "ATTACK_DEGREE_LAYER", "comm") == "physical":
        return physical_layer.graph
    return comm_layer.graph


def save_csv(path: Path, rows: Iterable[Dict], fieldnames: List[str]) -> None:
    """保存 CSV。"""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def calculate_resilience(history: Dict, trigger_time: int, q_min: float, lambda_: float) -> float:
    """依据带底线门控和时间衰减的积分公式计算韧性。"""
    times = np.array(history["time"], dtype=float)
    q_values = np.array(history["Q_overall"], dtype=float)
    mask = times >= trigger_time
    times_after = times[mask]
    q_after = q_values[mask]
    if len(times_after) <= 1:
        return 0.0

    q_ideal = q_values[0]
    numerator = 0.0
    denominator = 0.0
    for index in range(1, len(times_after)):
        dt = times_after[index] - times_after[index - 1]
        weight = np.exp(-lambda_ * (times_after[index] - trigger_time))
        numerator += max(0.0, q_after[index] - q_min) * weight * dt
        denominator += max(0.0, q_ideal - q_min) * weight * dt

    if denominator <= 0.0:
        return 0.0
    return float(numerator / denominator)
