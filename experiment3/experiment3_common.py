"""
实验三公共运行逻辑。
"""

from __future__ import annotations

import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

CURRENT_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = CURRENT_DIR / ".mplconfig"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

import matplotlib

matplotlib.use("Agg")
import numpy as np

PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from attack import AttackModule
from experiment_common import get_attack_reference_graph, initialize_nodes, update_networks
from network_layers import CommunicationLayer, MissionLayer, PhysicalLayer
from performance import PerformanceEvaluator
from recovery import RecoveryStrategy

matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False


def clip_metric(value: float) -> float:
    return float(np.clip(value, 0.0, 1.0))


def build_run_config(base_config, name: str, attrs: Dict):
    """动态构造单次运行配置。"""
    class_name = f"Experiment3RunConfig_{name}"
    run_config = type(class_name, (base_config,), attrs)
    run_config.validate()
    return run_config


def simulate_run(
    config,
    recovery_strategy_id: Optional[str] = None,
) -> Dict[str, List[float]]:
    """执行单次多层动态仿真，返回完整时序。"""
    nodes = initialize_nodes(config)
    physical_layer = PhysicalLayer(config)
    comm_layer = CommunicationLayer(config)
    mission_layer = MissionLayer(config)
    performance_evaluator = PerformanceEvaluator(config)
    attack_module = AttackModule(config)
    recovery_strategy = RecoveryStrategy(config, performance_evaluator)

    history = {
        "time": [],
        "Q_phy": [],
        "Q_comm": [],
        "Q_mis": [],
        "Q_overall": [],
        "alive_nodes": [],
        "attacked_count": [],
        "jammed_count": [],
    }

    def record_state(current_time: int) -> None:
        q_phy, q_comm, q_mis, q_overall = performance_evaluator.calculate_overall_performance(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
        )
        history["time"].append(current_time)
        history["Q_phy"].append(clip_metric(q_phy))
        history["Q_comm"].append(clip_metric(q_comm))
        history["Q_mis"].append(clip_metric(q_mis))
        history["Q_overall"].append(clip_metric(q_overall))
        history["alive_nodes"].append(sum(1 for node in nodes if node.is_alive))
        history["attacked_count"].append(len(attack_module.attacked_nodes))
        history["jammed_count"].append(len(attack_module.jammed_nodes))

    update_networks(config, nodes, physical_layer, comm_layer, mission_layer, attack_module, t=0)
    record_state(0)

    for current_time in range(1, config.TIME_STEPS + 1):
        attack_graph = get_attack_reference_graph(config, physical_layer, comm_layer)
        attack_module.execute_attack(nodes, current_time, graph=attack_graph)
        attack_module.update_cyber_window(current_time)

        if recovery_strategy_id is not None and current_time > config.RECONFIGURE_TRIGGER_TIME:
            recovery_strategy.execute_recovery(
                nodes,
                comm_layer,
                current_time,
                physical_layer=physical_layer,
                jammed_ids=set(attack_module.active_jam_node_ids),
                strategy_override=recovery_strategy_id,
            )

        update_networks(config, nodes, physical_layer, comm_layer, mission_layer, attack_module, t=current_time)
        record_state(current_time)

    return history


def aggregate_time_series(raw_rows: List[Dict], key_fields: List[str]) -> List[Dict]:
    """按 key_fields + time 聚合时序均值与标准差。"""
    grouped: Dict[Tuple, List[Dict]] = defaultdict(list)
    for row in raw_rows:
        grouped[tuple(row[field] for field in key_fields + ["time"])].append(row)

    metric_names = ["Q_phy", "Q_comm", "Q_mis", "Q_overall", "alive_nodes"]
    summary_rows: List[Dict] = []
    for group_key, rows in sorted(grouped.items()):
        summary = {field: rows[0][field] for field in key_fields}
        summary["time"] = rows[0]["time"]
        summary["num_runs"] = len(rows)
        for metric_name in metric_names:
            values = np.array([row[metric_name] for row in rows], dtype=float)
            summary[f"{metric_name}_mean"] = float(np.mean(values))
            summary[f"{metric_name}_std"] = float(np.std(values))
        summary_rows.append(summary)
    return summary_rows


def aggregate_final_metrics(raw_rows: List[Dict], key_fields: List[str]) -> List[Dict]:
    """按 key_fields 聚合终态指标。"""
    grouped: Dict[Tuple, List[Dict]] = defaultdict(list)
    for row in raw_rows:
        grouped[tuple(row[field] for field in key_fields)].append(row)

    metric_names = ["Q_phy", "Q_comm", "Q_mis", "Q_overall", "alive_nodes"]
    summary_rows: List[Dict] = []
    for group_key, rows in sorted(grouped.items()):
        summary = {field: rows[0][field] for field in key_fields}
        summary["num_runs"] = len(rows)
        for metric_name in metric_names:
            values = np.array([row[metric_name] for row in rows], dtype=float)
            summary[f"{metric_name}_mean"] = float(np.mean(values))
            summary[f"{metric_name}_std"] = float(np.std(values))
        summary_rows.append(summary)
    return summary_rows


def build_lookup(rows: List[Dict], key_fields: List[str]) -> Dict[Tuple, Dict]:
    """构造查找表。"""
    return {
        tuple(row[field] for field in key_fields): row
        for row in rows
    }
