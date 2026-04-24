"""
实验二入口：
基于“破坏模式 × 攻击策略 × 重构策略”组合评估自适应重构的恢复性能与韧性。
该总入口会先运行基础场景矩阵扫描，再可选运行攻击强度扫描。

本入口生成：
    基础部分图1、3-9
        figure_1_dynamic_recovery_matrix.png
        figure_3_resilience_heatmap.png
        figure_4_spatial_reconfiguration_snapshots.png
        figure_5_qphy_recovery_matrix.png
        figure_6_qcomm_recovery_matrix.png
        figure_7_qmis_recovery_matrix.png
        figure_8_final_layer_performance_bars.png
        figure_9_resilience_grouped_bars.png
    攻击强度部分
        仅导出强度扫描结果表，不再生成 figure_10 图像

运行方式：
    python experiment2/run_experiment2.py
    python experiment2/run_experiment2.py --quick
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

CURRENT_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = CURRENT_DIR / ".mplconfig"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from matplotlib.patches import FancyArrowPatch
from matplotlib import colors as mcolors

PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from attack import AttackModule
from experiment2_config import Experiment2Config
from experiment_common import (
    calculate_resilience,
    get_attack_reference_graph,
    initialize_nodes,
    save_csv,
    update_networks,
)
from network_layers import CommunicationLayer, MissionLayer, PhysicalLayer
from node import Node, NodeType
from performance import PerformanceEvaluator
from recovery import RecoveryStrategy

matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False


def get_phase(config, current_time: int) -> int:
    """根据时刻查询任务阶段。"""
    for start, end, phase in config.TASK_PHASE_SCHEDULE:
        if start <= current_time < end:
            return phase
    raise ValueError(f"时刻 {current_time} 未匹配到 TASK_PHASE_SCHEDULE")

def build_run_config(base_config, scenario: Dict, strategy: Dict, seed: int, attack_ratio: Optional[float] = None):
    """按场景、策略与随机种子构造单次运行配置。"""
    resolved_attack_ratio = base_config.ATTACK_RATIO if attack_ratio is None else attack_ratio
    attack_nodes = int(round(base_config.N_TOTAL * resolved_attack_ratio))
    attrs = {
        "ATTACK_MODE": scenario["mode"],
        "ATTACK_STRATEGY": scenario["strategy"],
        "ATTACK_ROLE_TARGET": scenario.get("role_target") or base_config.ATTACK_ROLE_TARGET,
        "ATTACK_RECOVER_TIME": base_config.TIME_STEPS if scenario["mode"] == "cyber" else base_config.ATTACK_TIME,
        "ATTACK_RATIO": resolved_attack_ratio,
        "ATTACK_NODES": attack_nodes,
        "RANDOM_SEED": seed,
        "RECOVERY_STRATEGY_ID": strategy["id"],
        "SCENARIO_ID": scenario["id"],
    }
    ratio_tag = int(round(resolved_attack_ratio * 100))
    class_name = f"Experiment2RunConfig_{scenario['id']}_{strategy['id']}_{ratio_tag}_{seed}"
    run_config = type(class_name, (base_config,), attrs)
    run_config.validate()
    return run_config

def clip_metric(value: float) -> float:
    """将指标裁剪到 [0, 1] 区间。"""
    return float(np.clip(value, 0.0, 1.0))


def build_snapshot_payload(
    nodes: List[Node],
    physical_layer: PhysicalLayer,
    comm_layer: CommunicationLayer,
    mission_layer: MissionLayer,
    jammed_ids: set[int],
) -> Dict:
    """提取用于空间可视化的快照信息。"""
    return {
        "nodes": [
            {
                "id": node.id,
                "type": node.type.name,
                "position": node.position.tolist(),
                "is_alive": node.is_alive,
                "is_jammed": node.id in jammed_ids,
            }
            for node in nodes
        ],
        "physical_edges": [(u, v) for u, v in physical_layer.graph.edges()],
        "comm_edges": [
            {
                "u": u,
                "v": v,
                "probability": float(comm_layer.activation_probabilities.get((u, v), 0.0)),
            }
            for u, v in comm_layer.graph.edges()
        ],
        "mission_edges": [(u, v) for u, v in mission_layer.graph.edges()],
        "valid_paths_count": len(mission_layer.valid_paths),
        "alive_nodes": sum(1 for node in nodes if node.is_alive),
    }


def maybe_store_snapshot(
    snapshot_store: Optional[Dict[str, Dict]],
    scenario: Dict,
    strategy: Dict,
    seed: int,
    current_time: int,
    config,
    nodes: List[Node],
    physical_layer: PhysicalLayer,
    comm_layer: CommunicationLayer,
    mission_layer: MissionLayer,
    jammed_ids: set[int],
) -> None:
    """按预设规则保存用于图 4 的拓扑快照。"""
    if snapshot_store is None:
        return
    if scenario["id"] != config.SNAPSHOT_SCENARIO or seed != config.SNAPSHOT_SEED:
        return
    attack_break_time = config.ATTACK_TIME

    if strategy["id"] == "no_reconfiguration" and current_time == attack_break_time:
        snapshot_store["attack_break"] = build_snapshot_payload(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            jammed_ids,
        )
    if strategy["id"] == "distance_driven" and current_time == config.SNAPSHOT_COMPARE_TIME:
        snapshot_store["distance_compare"] = build_snapshot_payload(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            jammed_ids,
        )
    if strategy["id"] == "degree_driven" and current_time == config.SNAPSHOT_COMPARE_TIME:
        snapshot_store["degree_compare"] = build_snapshot_payload(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            jammed_ids,
        )
    if strategy["id"] == "utility_role_mismatch_recon" and current_time == config.SNAPSHOT_COMPARE_TIME:
        snapshot_store["mismatch_compare"] = build_snapshot_payload(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            jammed_ids,
        )
    if strategy["id"] == "utility_role_driven" and current_time == config.SNAPSHOT_COMPARE_TIME:
        snapshot_store["utility_compare"] = build_snapshot_payload(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            jammed_ids,
        )


def simulate_single_run(
    config,
    scenario: Dict,
    strategy: Dict,
    snapshot_store: Optional[Dict[str, Dict]],
) -> Tuple[List[Dict], Dict]:
    """执行单个场景 + 单个重构策略 + 单个随机种子的恢复仿真。"""
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
    }
    raw_rows: List[Dict] = []

    def record_state(current_time: int) -> None:
        q_phy, q_comm, q_mis, q_overall = performance_evaluator.calculate_overall_performance(
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
        )
        row = {
            "scenario_id": scenario["id"],
            "scenario_label": scenario["label"],
            "mode_label": scenario["mode_label"],
            "targeting_label": scenario["targeting_label"],
            "strategy_id": strategy["id"],
            "strategy_label": strategy["label"],
            "seed": config.RANDOM_SEED,
            "time": current_time,
            "Q_phy": clip_metric(q_phy),
            "Q_comm": clip_metric(q_comm),
            "Q_mis": clip_metric(q_mis),
            "Q_overall": clip_metric(q_overall),
            "alive_nodes": sum(1 for node in nodes if node.is_alive),
            "phy_edges": physical_layer.graph.number_of_edges(),
            "comm_edges": comm_layer.graph.number_of_edges(),
            "mis_edges": mission_layer.graph.number_of_edges(),
            "valid_paths": len(mission_layer.valid_paths),
            "attacked_count": len(attack_module.attacked_nodes),
            "jammed_count": len(attack_module.jammed_nodes),
        }
        raw_rows.append(row)
        for key in history:
            history[key].append(row[key])

    update_networks(config, nodes, physical_layer, comm_layer, mission_layer, attack_module, t=0)
    record_state(0)

    for current_time in range(1, config.TIME_STEPS + 1):
        attack_graph = get_attack_reference_graph(config, physical_layer, comm_layer)
        attack_module.execute_attack(nodes, current_time, graph=attack_graph)
        attack_module.update_cyber_window(current_time)

        if current_time > config.RECONFIGURE_TRIGGER_TIME:
            recovery_strategy.execute_recovery(
                nodes,
                comm_layer,
                current_time,
                physical_layer=physical_layer,
                jammed_ids=set(attack_module.active_jam_node_ids),
                strategy_override=strategy["id"],
            )

        update_networks(config, nodes, physical_layer, comm_layer, mission_layer, attack_module, t=current_time)
        record_state(current_time)
        maybe_store_snapshot(
            snapshot_store,
            scenario,
            strategy,
            config.RANDOM_SEED,
            current_time,
            config,
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            set(attack_module.active_jam_node_ids),
        )

    resilience = calculate_resilience(
        history,
        trigger_time=config.RECONFIGURE_TRIGGER_TIME,
        q_min=config.Q_MIN,
        lambda_=config.LAMBDA,
    )
    resilience_row = {
        "scenario_id": scenario["id"],
        "scenario_label": scenario["label"],
        "mode_label": scenario["mode_label"],
        "targeting_label": scenario["targeting_label"],
        "strategy_id": strategy["id"],
        "strategy_label": strategy["label"],
        "attack_ratio": config.ATTACK_RATIO,
        "seed": config.RANDOM_SEED,
        "resilience": resilience,
        "final_Q_phy": history["Q_phy"][-1],
        "final_Q_comm": history["Q_comm"][-1],
        "final_Q_mis": history["Q_mis"][-1],
        "final_Q_overall": history["Q_overall"][-1],
    }
    return raw_rows, resilience_row


def aggregate_time_series(raw_rows: List[Dict]) -> List[Dict]:
    """按场景 + 策略 + 时刻聚合均值与标准差。"""
    grouped: Dict[Tuple[str, str, int], List[Dict]] = defaultdict(list)
    for row in raw_rows:
        grouped[(row["scenario_id"], row["strategy_id"], row["time"])].append(row)

    metric_names = [
        "Q_phy",
        "Q_comm",
        "Q_mis",
        "Q_overall",
        "alive_nodes",
        "phy_edges",
        "comm_edges",
        "mis_edges",
        "valid_paths",
        "attacked_count",
        "jammed_count",
    ]
    summary_rows: List[Dict] = []
    for (scenario_id, strategy_id, time_step), rows in sorted(grouped.items()):
        summary = {
            "scenario_id": scenario_id,
            "scenario_label": rows[0]["scenario_label"],
            "mode_label": rows[0]["mode_label"],
            "targeting_label": rows[0]["targeting_label"],
            "strategy_id": strategy_id,
            "strategy_label": rows[0]["strategy_label"],
            "time": time_step,
            "num_runs": len(rows),
        }
        for metric_name in metric_names:
            values = np.array([row[metric_name] for row in rows], dtype=float)
            summary[f"{metric_name}_mean"] = float(np.mean(values))
            summary[f"{metric_name}_std"] = float(np.std(values))
        summary_rows.append(summary)
    return summary_rows


def aggregate_resilience_summary(resilience_rows: List[Dict]) -> List[Dict]:
    """按场景 + 策略聚合韧性与最终状态。"""
    grouped: Dict[Tuple[str, str], List[Dict]] = defaultdict(list)
    for row in resilience_rows:
        grouped[(row["scenario_id"], row["strategy_id"])].append(row)

    summary_rows: List[Dict] = []
    for (scenario_id, strategy_id), rows in sorted(grouped.items()):
        resilience_values = np.array([row["resilience"] for row in rows], dtype=float)
        q_phy_values = np.array([row["final_Q_phy"] for row in rows], dtype=float)
        q_comm_values = np.array([row["final_Q_comm"] for row in rows], dtype=float)
        q_mis_values = np.array([row["final_Q_mis"] for row in rows], dtype=float)
        q_values = np.array([row["final_Q_overall"] for row in rows], dtype=float)
        summary_rows.append(
            {
                "scenario_id": scenario_id,
                "scenario_label": rows[0]["scenario_label"],
                "mode_label": rows[0]["mode_label"],
                "targeting_label": rows[0]["targeting_label"],
                "strategy_id": strategy_id,
                "strategy_label": rows[0]["strategy_label"],
                "attack_ratio": rows[0]["attack_ratio"],
                "num_runs": len(rows),
                "resilience_mean": float(np.mean(resilience_values)),
                "resilience_std": float(np.std(resilience_values)),
                "final_Q_phy_mean": float(np.mean(q_phy_values)),
                "final_Q_phy_std": float(np.std(q_phy_values)),
                "final_Q_comm_mean": float(np.mean(q_comm_values)),
                "final_Q_comm_std": float(np.std(q_comm_values)),
                "final_Q_mis_mean": float(np.mean(q_mis_values)),
                "final_Q_mis_std": float(np.std(q_mis_values)),
                "final_Q_overall_mean": float(np.mean(q_values)),
                "final_Q_overall_std": float(np.std(q_values)),
            }
        )
    return summary_rows


def build_time_lookup(summary_rows: List[Dict]) -> Dict[Tuple[str, str, int], Dict]:
    """按场景 + 策略 + 时间建立查找表。"""
    return {
        (row["scenario_id"], row["strategy_id"], row["time"]): row
        for row in summary_rows
    }


def build_resilience_lookup(summary_rows: List[Dict]) -> Dict[Tuple[str, str], Dict]:
    """按场景 + 策略建立查找表。"""
    return {
        (row["scenario_id"], row["strategy_id"]): row
        for row in summary_rows
    }


def aggregate_attack_intensity_summary(resilience_rows: List[Dict]) -> List[Dict]:
    """按场景 + 策略 + 攻击强度聚合韧性与终态性能。"""
    grouped: Dict[Tuple[str, str, float], List[Dict]] = defaultdict(list)
    for row in resilience_rows:
        grouped[(row["scenario_id"], row["strategy_id"], row["attack_ratio"])].append(row)

    summary_rows: List[Dict] = []
    for (scenario_id, strategy_id, attack_ratio), rows in sorted(grouped.items()):
        resilience_values = np.array([row["resilience"] for row in rows], dtype=float)
        q_phy_values = np.array([row["final_Q_phy"] for row in rows], dtype=float)
        q_comm_values = np.array([row["final_Q_comm"] for row in rows], dtype=float)
        q_mis_values = np.array([row["final_Q_mis"] for row in rows], dtype=float)
        q_values = np.array([row["final_Q_overall"] for row in rows], dtype=float)
        summary_rows.append(
            {
                "scenario_id": scenario_id,
                "scenario_label": rows[0]["scenario_label"],
                "mode_label": rows[0]["mode_label"],
                "targeting_label": rows[0]["targeting_label"],
                "strategy_id": strategy_id,
                "strategy_label": rows[0]["strategy_label"],
                "attack_ratio": attack_ratio,
                "num_runs": len(rows),
                "resilience_mean": float(np.mean(resilience_values)),
                "resilience_std": float(np.std(resilience_values)),
                "final_Q_phy_mean": float(np.mean(q_phy_values)),
                "final_Q_phy_std": float(np.std(q_phy_values)),
                "final_Q_comm_mean": float(np.mean(q_comm_values)),
                "final_Q_comm_std": float(np.std(q_comm_values)),
                "final_Q_mis_mean": float(np.mean(q_mis_values)),
                "final_Q_mis_std": float(np.std(q_mis_values)),
                "final_Q_overall_mean": float(np.mean(q_values)),
                "final_Q_overall_std": float(np.std(q_values)),
            }
        )
    return summary_rows


def get_marker_positions(total_points: int, offset: int, step: int) -> List[int]:
    """交错设置 marker 位置，减少重叠。"""
    if total_points <= 0:
        return []
    indices = list(range(offset % total_points, total_points, max(1, step)))
    if not indices:
        indices = [offset % total_points]
    return indices


def build_strategy_legend_handles(strategy_specs: Iterable[Dict]) -> List[Line2D]:
    """显式构造策略图例。"""
    return [
        Line2D(
            [0],
            [0],
            label=strategy["label"],
            color=strategy["color"],
            linestyle=strategy["linestyle"],
            marker=strategy["marker"],
            linewidth=2.2,
            markersize=6,
        )
        for strategy in strategy_specs
    ]


def build_strategy_patch_handles(strategy_specs: Iterable[Dict]) -> List[Patch]:
    """为柱状图显式构造策略图例。"""
    return [
        Patch(
            facecolor=strategy["color"],
            edgecolor="none",
            alpha=0.88,
            label=strategy["label"],
        )
        for strategy in strategy_specs
    ]


def get_scenario_compact_labels(config) -> List[str]:
    """生成紧凑场景标签。"""
    mode_abbrev = {
        "Physical Destruction": "PD",
        "Network Suppression": "NS",
    }
    targeting_abbrev = {
        "Random Attack": "Random",
        "Topology-Oriented Deliberate Attack": "Topo",
        "Role-Oriented Targeted Attack": "Role",
    }
    return [
        f"{mode_abbrev.get(scenario['mode_label'], scenario['mode_label'])}-"
        f"{targeting_abbrev.get(scenario['targeting_label'], scenario['targeting_label'])}"
        for scenario in config.ATTACK_SCENARIOS
    ]


def configure_time_axis(ax, config, ylabel: str, ylim: Tuple[float, float] = (0.0, 1.05)) -> None:
    """统一时间轴样式。"""
    ax.set_xlabel("Time Step $t$")
    ax.set_ylabel(ylabel)
    ax.set_xlim(0.0, config.TIME_STEPS)
    ax.set_ylim(*ylim)
    ax.set_xticks(np.arange(0, config.TIME_STEPS + 1, config.TIME_AXIS_TICK_STEP))
    ax.grid(True, alpha=0.3)
    ax.axvline(
        x=config.ATTACK_TIME,
        color="#777777",
        linestyle=":",
        linewidth=1.7,
        alpha=0.9,
    )


def plot_dynamic_recovery_matrix(config, time_summary_rows: List[Dict], output_path: Path) -> None:
    """图 1：六个攻击场景下四种重构策略的综合性能动态恢复曲线。"""
    scenario_map = {scenario["id"]: scenario for scenario in config.ATTACK_SCENARIOS}
    lookup = build_time_lookup(time_summary_rows)
    time_axis = list(range(config.TIME_STEPS + 1))

    fig, axes = plt.subplots(2, 3, figsize=config.FIGSIZE_DYNAMIC, sharex=True, sharey=True)
    fig.suptitle(
        "Dynamic Recovery of Integrated Performance $Q(t)$ Under Different Disruption Modes and Attack Strategies",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )

    for row_index, scenario_row in enumerate(config.DYNAMIC_SCENARIO_GRID):
        for col_index, scenario_id in enumerate(scenario_row):
            ax = axes[row_index, col_index]
            scenario = scenario_map[scenario_id]
            for strategy_index, strategy in enumerate(config.RECOVERY_STRATEGIES):
                mean_values = []
                std_values = []
                for time_step in time_axis:
                    row = lookup[(scenario_id, strategy["id"], time_step)]
                    mean_values.append(row["Q_overall_mean"])
                    std_values.append(row["Q_overall_std"])
                mean_array = np.array(mean_values, dtype=float)
                std_array = np.array(std_values, dtype=float)
                ax.plot(
                    time_axis,
                    mean_array,
                    color=strategy["color"],
                    linestyle=strategy["linestyle"],
                    marker=strategy["marker"],
                    linewidth=2.0,
                    markersize=4.5,
                    markevery=get_marker_positions(len(time_axis), strategy_index, 15),
                )
                ax.fill_between(
                    time_axis,
                    np.clip(mean_array - std_array, 0.0, 1.05),
                    np.clip(mean_array + std_array, 0.0, 1.05),
                    color=strategy["color"],
                    alpha=0.08,
                )

            configure_time_axis(ax, config, "Integrated Performance $Q(t)$")
            ax.axhline(y=config.Q_MIN, color="#999999", linestyle="--", linewidth=1.1, alpha=0.8)
            ax.set_title(f"{scenario['mode_label']} | {scenario['targeting_label']}", fontsize=11)

    fig.legend(
        handles=build_strategy_legend_handles(config.RECOVERY_STRATEGIES),
        loc="upper center",
        ncol=len(config.RECOVERY_STRATEGIES),
        frameon=False,
        bbox_to_anchor=(0.5, 0.945),
        handlelength=3.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.90))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_layer_recovery_matrix(
    config,
    time_summary_rows: List[Dict],
    metric_name: str,
    ylabel: str,
    title: str,
    output_path: Path,
) -> None:
    """绘制不同场景下指定层级性能的动态恢复曲线矩阵。"""
    scenario_map = {scenario["id"]: scenario for scenario in config.ATTACK_SCENARIOS}
    lookup = build_time_lookup(time_summary_rows)
    time_axis = list(range(config.TIME_STEPS + 1))

    fig, axes = plt.subplots(2, 3, figsize=config.FIGSIZE_LAYER_DYNAMIC, sharex=True, sharey=True)
    fig.suptitle(
        title,
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )

    for row_index, scenario_row in enumerate(config.DYNAMIC_SCENARIO_GRID):
        for col_index, scenario_id in enumerate(scenario_row):
            ax = axes[row_index, col_index]
            scenario = scenario_map[scenario_id]
            for strategy_index, strategy in enumerate(config.RECOVERY_STRATEGIES):
                mean_values = []
                std_values = []
                for time_step in time_axis:
                    row = lookup[(scenario_id, strategy["id"], time_step)]
                    mean_values.append(row[f"{metric_name}_mean"])
                    std_values.append(row[f"{metric_name}_std"])
                mean_array = np.array(mean_values, dtype=float)
                std_array = np.array(std_values, dtype=float)
                ax.plot(
                    time_axis,
                    mean_array,
                    color=strategy["color"],
                    linestyle=strategy["linestyle"],
                    marker=strategy["marker"],
                    linewidth=2.0,
                    markersize=4.5,
                    markevery=get_marker_positions(len(time_axis), strategy_index, 15),
                )
                ax.fill_between(
                    time_axis,
                    np.clip(mean_array - std_array, 0.0, 1.05),
                    np.clip(mean_array + std_array, 0.0, 1.05),
                    color=strategy["color"],
                    alpha=0.08,
                )

            configure_time_axis(ax, config, ylabel)
            ax.set_title(f"{scenario['mode_label']} | {scenario['targeting_label']}", fontsize=11)

    fig.legend(
        handles=build_strategy_legend_handles(config.RECOVERY_STRATEGIES),
        loc="upper center",
        ncol=len(config.RECOVERY_STRATEGIES),
        frameon=False,
        bbox_to_anchor=(0.5, 0.945),
        handlelength=3.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.90))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_resilience_heatmap(config, resilience_summary_rows: List[Dict], output_path: Path) -> None:
    """图 3：六种攻击场景下四类重构策略的韧性热力图。"""
    scenario_ids = [scenario["id"] for scenario in config.ATTACK_SCENARIOS]
    scenario_labels = get_scenario_compact_labels(config)
    strategy_ids = [strategy["id"] for strategy in config.RECOVERY_STRATEGIES]
    strategy_labels = [strategy["label"] for strategy in config.RECOVERY_STRATEGIES]
    lookup = build_resilience_lookup(resilience_summary_rows)

    matrix = np.zeros((len(strategy_ids), len(scenario_ids)))
    for row_index, strategy_id in enumerate(strategy_ids):
        for col_index, scenario_id in enumerate(scenario_ids):
            matrix[row_index, col_index] = lookup[(scenario_id, strategy_id)]["resilience_mean"]

    fig, ax = plt.subplots(figsize=config.FIGSIZE_RESILIENCE)
    fig.suptitle(
        "Comparison of Integrated Resilience $R$ Under Different Disruption Modes and Attack Strategies",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )
    image = ax.imshow(matrix, cmap="YlOrRd", aspect="auto", vmin=0.0, vmax=max(1.0, float(np.max(matrix))))
    for row_index in range(matrix.shape[0]):
        for col_index in range(matrix.shape[1]):
            ax.text(
                col_index,
                row_index,
                f"{matrix[row_index, col_index]:.3f}",
                ha="center",
                va="center",
                fontsize=9,
                color="#222222",
            )

    ax.set_xticks(np.arange(len(scenario_ids)))
    ax.set_xticklabels(scenario_labels, rotation=18)
    ax.set_yticks(np.arange(len(strategy_ids)))
    ax.set_yticklabels(strategy_labels)
    ax.set_xlabel("Attack Scenario")
    ax.set_ylabel("Recovery Strategy")
    cbar = fig.colorbar(image, ax=ax)
    cbar.set_label("Integrated Resilience Score $R$")
    plt.tight_layout()
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_resilience_grouped_bars(config, resilience_summary_rows: List[Dict], output_path: Path) -> None:
    """图 9：不同攻击场景下四种恢复策略的综合韧性分组柱状图。"""
    scenario_ids = [scenario["id"] for scenario in config.ATTACK_SCENARIOS]
    scenario_labels = get_scenario_compact_labels(config)
    lookup = build_resilience_lookup(resilience_summary_rows)

    fig, ax = plt.subplots(figsize=config.FIGSIZE_RESILIENCE_BARS)
    fig.suptitle(
        "Comparison of Integrated Resilience Scores Across Recovery Strategies and Attack Scenarios",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    x = np.arange(len(scenario_ids), dtype=float)
    bar_width = 0.18
    offset_center = (len(config.RECOVERY_STRATEGIES) - 1) / 2.0

    for strategy_index, strategy in enumerate(config.RECOVERY_STRATEGIES):
        means = []
        stds = []
        for scenario_id in scenario_ids:
            row = lookup[(scenario_id, strategy["id"])]
            means.append(row["resilience_mean"])
            stds.append(row["resilience_std"])
        offset = (strategy_index - offset_center) * bar_width
        ax.bar(
            x + offset,
            means,
            width=bar_width,
            color=strategy["color"],
            alpha=0.88,
            yerr=stds,
            capsize=3.5,
            linewidth=0.0,
            error_kw={"elinewidth": 1.0, "alpha": 0.7},
        )

    ax.set_xticks(x)
    ax.set_xticklabels(scenario_labels, rotation=18)
    ax.set_xlabel("Attack Scenario")
    ax.set_ylabel("Mission-Oriented Integrated Resilience $R$")
    ax.set_ylim(0.0, 1.05)
    ax.grid(True, axis="y", alpha=0.3)
    ax.legend(
        handles=build_strategy_patch_handles(config.RECOVERY_STRATEGIES),
        loc="upper center",
        ncol=len(config.RECOVERY_STRATEGIES),
        frameon=False,
        bbox_to_anchor=(0.5, 0.93),
    )
    fig.subplots_adjust(
        left=0.05,
        right=0.985,
        bottom=0.065,
        top=0.845,
        wspace=0.08,
        hspace=0.14,
    )
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def build_layer_impact_summary(resilience_summary_rows: List[Dict]) -> List[Dict]:
    """生成按场景、策略和层级展开的终态性能影响汇总。"""
    layer_specs = [
        ("Q_phy", "Physical-Layer Performance"),
        ("Q_comm", "Communication-Layer Performance"),
        ("Q_mis", "Mission-Layer Performance"),
    ]
    baseline_lookup = {
        row["scenario_id"]: row
        for row in resilience_summary_rows
        if row["strategy_id"] == "no_reconfiguration"
    }

    summary_rows: List[Dict] = []
    grouped: Dict[Tuple[str, str], List[Dict]] = defaultdict(list)
    for row in resilience_summary_rows:
        baseline_row = baseline_lookup[row["scenario_id"]]
        for layer_id, layer_label in layer_specs:
            summary_row = {
                "scenario_id": row["scenario_id"],
                "scenario_label": row["scenario_label"],
                "mode_label": row["mode_label"],
                "targeting_label": row["targeting_label"],
                "strategy_id": row["strategy_id"],
                "strategy_label": row["strategy_label"],
                "layer_id": layer_id,
                "layer_label": layer_label,
                "final_mean": row[f"final_{layer_id}_mean"],
                "final_std": row[f"final_{layer_id}_std"],
                "static_baseline_mean": baseline_row[f"final_{layer_id}_mean"],
                "absolute_gain_vs_static": row[f"final_{layer_id}_mean"] - baseline_row[f"final_{layer_id}_mean"],
                "relative_gain_vs_static_pct": (
                    100.0
                    * (row[f"final_{layer_id}_mean"] - baseline_row[f"final_{layer_id}_mean"])
                    / baseline_row[f"final_{layer_id}_mean"]
                    if baseline_row[f"final_{layer_id}_mean"] > 1e-12
                    else 0.0
                ),
            }
            summary_rows.append(summary_row)
            grouped[(row["scenario_id"], layer_id)].append(summary_row)

    for group_rows in grouped.values():
        ranked_rows = sorted(
            group_rows,
            key=lambda item: (-item["final_mean"], item["strategy_label"]),
        )
        best_value = max(item["final_mean"] for item in group_rows)
        for rank, summary_row in enumerate(ranked_rows, start=1):
            summary_row["rank_within_scenario_layer"] = rank
            summary_row["is_best_strategy"] = int(abs(summary_row["final_mean"] - best_value) <= 1e-12)

    return sorted(
        summary_rows,
        key=lambda item: (
            item["scenario_id"],
            item["layer_id"],
            item["rank_within_scenario_layer"],
            item["strategy_id"],
        ),
    )


def plot_final_layer_performance_bars(config, resilience_summary_rows: List[Dict], output_path: Path) -> None:
    """图 8：不同恢复策略在各场景下的层级终态性能柱状对比。"""
    scenario_ids = [scenario["id"] for scenario in config.ATTACK_SCENARIOS]
    scenario_labels = get_scenario_compact_labels(config)
    lookup = build_resilience_lookup(resilience_summary_rows)
    layer_specs = [
        ("Q_phy", "Final Physical-Layer Performance $Q_{phy}(t_r)$"),
        ("Q_comm", "Final Communication-Layer Performance $Q_{comm}(t_r)$"),
        ("Q_mis", "Final Mission-Layer Performance $Q_{mis}(t_r)$"),
    ]

    fig, axes = plt.subplots(1, 3, figsize=config.FIGSIZE_LAYER_FINAL, sharey=True)
    fig.suptitle(
        "Impact of Recovery Strategies on Final Layer-Wise Performance",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    x = np.arange(len(scenario_ids), dtype=float)
    bar_width = 0.18
    offset_center = (len(config.RECOVERY_STRATEGIES) - 1) / 2.0

    for axis_index, (metric_name, subplot_title) in enumerate(layer_specs):
        ax = axes[axis_index]
        for strategy_index, strategy in enumerate(config.RECOVERY_STRATEGIES):
            values = [
                lookup[(scenario_id, strategy["id"])][f"final_{metric_name}_mean"]
                for scenario_id in scenario_ids
            ]
            offset = (strategy_index - offset_center) * bar_width
            ax.bar(
                x + offset,
                values,
                width=bar_width,
                color=strategy["color"],
                alpha=0.88,
            )

        ax.set_title(subplot_title, fontsize=11)
        ax.set_xticks(x)
        ax.set_xticklabels(scenario_labels, rotation=18)
        ax.set_ylim(0.0, 1.05)
        ax.grid(True, axis="y", alpha=0.3)
        ax.set_xlabel("Attack Scenario")
        if axis_index == 0:
            ax.set_ylabel("Mean Final Performance")

    fig.legend(
        handles=build_strategy_patch_handles(config.RECOVERY_STRATEGIES),
        loc="upper center",
        ncol=len(config.RECOVERY_STRATEGIES),
        frameon=False,
        bbox_to_anchor=(0.5, 0.91),
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.86))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def _draw_snapshot_panel(ax, snapshot: Dict, title: str) -> None:
    """绘制单个拓扑快照。"""
    node_styles = {
        "SENSOR": {"color": "#1f77b4", "marker": "o", "label": "S"},
        "DECIDER": {"color": "#ff7f0e", "marker": "s", "label": "D"},
        "INFLUENCER": {"color": "#d62728", "marker": "^", "label": "I"},
    }
    alive_lookup = {
        node["id"]: node
        for node in snapshot["nodes"]
        if node["is_alive"]
    }

    for u, v in snapshot["physical_edges"]:
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u]["position"]
        pos_v = alive_lookup[v]["position"]
        ax.plot(
            [pos_u[0], pos_v[0]],
            [pos_u[1], pos_v[1]],
            color="#d0d0d0",
            linewidth=0.7,
            alpha=0.45,
            zorder=1,
        )

    norm = mcolors.Normalize(vmin=0.0, vmax=1.0)
    cmap = plt.cm.Greens
    for edge in snapshot["comm_edges"]:
        u = edge["u"]
        v = edge["v"]
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u]["position"]
        pos_v = alive_lookup[v]["position"]
        ax.plot(
            [pos_u[0], pos_v[0]],
            [pos_u[1], pos_v[1]],
            color=cmap(norm(edge["probability"])),
            linewidth=1.0,
            linestyle="--",
            alpha=0.5,
            zorder=2,
        )

    for u, v in snapshot["mission_edges"]:
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u]["position"]
        pos_v = alive_lookup[v]["position"]
        ax.annotate(
            "",
            xy=(pos_v[0], pos_v[1]),
            xytext=(pos_u[0], pos_u[1]),
            zorder=3,
            arrowprops=dict(
                arrowstyle="->",
                color="#b2182b",
                lw=1.7,
                alpha=0.7,
                linestyle="-",
                shrinkA=8,
                shrinkB=8,
            ),
        )

    for node_type, style in node_styles.items():
        typed_nodes = [
            node for node in snapshot["nodes"]
            if node["is_alive"] and node["type"] == node_type and not node["is_jammed"]
        ]
        if typed_nodes:
            positions = np.array([node["position"] for node in typed_nodes], dtype=float)
            ax.scatter(
                positions[:, 0],
                positions[:, 1],
                s=42,
                c=style["color"],
                marker=style["marker"],
                edgecolors="white",
                linewidths=0.5,
                zorder=4,
            )

        jammed_nodes = [
            node for node in snapshot["nodes"]
            if node["is_alive"] and node["type"] == node_type and node["is_jammed"]
        ]
        if jammed_nodes:
            positions = np.array([node["position"] for node in jammed_nodes], dtype=float)
            ax.scatter(
                positions[:, 0],
                positions[:, 1],
                s=54,
                facecolors="none",
                edgecolors=style["color"],
                marker=style["marker"],
                linewidths=1.2,
                zorder=5,
            )

    ax.set_title(
        f"{title}\nAlive Nodes={snapshot['alive_nodes']}  Valid Kill Chains={snapshot['valid_paths_count']}",
        fontsize=9.4,
        pad=6,
    )
    ax.set_xlim(0.0, 100.0)
    ax.set_ylim(0.0, 100.0)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.2)
    ax.set_xlabel("x")
    ax.set_ylabel("y")


def plot_snapshot_evolution(config, snapshot_store: Dict[str, Dict], output_path: Path) -> None:
    """图 4：受击后不同重构方式的空间拓扑演化快照。"""
    required_keys = [
        "attack_break",
        "distance_compare",
        "degree_compare",
        "mismatch_compare",
        "utility_compare",
    ]
    if any(key not in snapshot_store for key in required_keys):
        return

    fig = plt.figure(figsize=(13.2, 9.6))
    panel_size = 0.285
    top_row_bottom = 0.53
    bottom_row_bottom = 0.12
    top_row_lefts = [0.045, 0.3575, 0.67]
    bottom_row_lefts = [0.20, 0.5125]
    axes = [
        fig.add_axes([top_row_lefts[0], top_row_bottom, panel_size, panel_size]),
        fig.add_axes([top_row_lefts[1], top_row_bottom, panel_size, panel_size]),
        fig.add_axes([top_row_lefts[2], top_row_bottom, panel_size, panel_size]),
        fig.add_axes([bottom_row_lefts[0], bottom_row_bottom, panel_size, panel_size]),
        fig.add_axes([bottom_row_lefts[1], bottom_row_bottom, panel_size, panel_size]),
    ]
    fig.suptitle(
        "Spatial Topology Evolution After Attack and Reconfiguration",
        fontsize=15,
        fontweight="bold",
        y=0.975,
    )

    attack_break_time = config.ATTACK_TIME
    compare_time = config.SNAPSHOT_COMPARE_TIME
    _draw_snapshot_panel(axes[0], snapshot_store["attack_break"], f"(a) Attack Fragmentation ($t={attack_break_time}$)")
    _draw_snapshot_panel(axes[1], snapshot_store["distance_compare"], f"(b) Nearest-Neighbor ($t={compare_time}$)")
    _draw_snapshot_panel(axes[2], snapshot_store["degree_compare"], f"(c) Maximum-Degree ($t={compare_time}$)")
    _draw_snapshot_panel(axes[3], snapshot_store["mismatch_compare"], f"(d) Phase-Mismatched Utility ($t={compare_time}$)")
    _draw_snapshot_panel(axes[4], snapshot_store["utility_compare"], f"(e) Utility-Guided and Role-Driven ($t={compare_time}$)")

    for ax in axes[:3]:
        ax.set_xlabel("")
        ax.tick_params(axis="x", labelbottom=False)

    for ax in (axes[1], axes[2], axes[4]):
        ax.set_ylabel("")
        ax.tick_params(axis="y", labelleft=False)

    legend_handles = [
        Line2D([0], [0], marker="o", color="w", markerfacecolor="#1f77b4", markeredgecolor="white", markersize=8, label="Sensor Node"),
        Line2D([0], [0], marker="s", color="w", markerfacecolor="#ff7f0e", markeredgecolor="white", markersize=8, label="Decider Node"),
        Line2D([0], [0], marker="^", color="w", markerfacecolor="#d62728", markeredgecolor="white", markersize=8, label="Influencer Node"),
        Line2D([0], [0], color="#d0d0d0", linewidth=1.2, label="Physical Edge"),
        Line2D([0], [0], color=plt.cm.Greens(0.75), linewidth=1.2, linestyle="--", label="Communication Edge ($P_{ij}(t)$)"),
        Line2D([0], [0], color="#b2182b", linewidth=1.8, label="Mission Edge"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        ncol=6,
        frameon=False,
        bbox_to_anchor=(0.5, 0.925),
        handlelength=2.8,
        fontsize=9.5,
        columnspacing=1.0,
        handletextpad=0.6,
    )
    fig.savefig(output_path, dpi=config.FIG_DPI)
    plt.close(fig)


def run_suite(config, quick: bool = False) -> Tuple[List[Dict], List[Dict], List[Dict], Dict[str, Dict]]:
    """执行实验二的全组合扫描。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    raw_rows: List[Dict] = []
    resilience_rows: List[Dict] = []
    snapshot_store: Dict[str, Dict] = {}

    total_runs = len(config.ATTACK_SCENARIOS) * len(config.RECOVERY_STRATEGIES) * len(seeds)
    run_index = 0
    for scenario in config.ATTACK_SCENARIOS:
        for strategy in config.RECOVERY_STRATEGIES:
            for seed in seeds:
                run_index += 1
                print(
                    f"[{run_index}/{total_runs}] "
                    f"scenario={scenario['id']}, strategy={strategy['id']}, seed={seed}"
                )
                run_config = build_run_config(config, scenario, strategy, seed)
                run_raw_rows, resilience_row = simulate_single_run(
                    run_config,
                    scenario,
                    strategy,
                    snapshot_store,
                )
                raw_rows.extend(run_raw_rows)
                resilience_rows.append(resilience_row)

    time_summary_rows = aggregate_time_series(raw_rows)
    resilience_summary_rows = aggregate_resilience_summary(resilience_rows)
    return raw_rows, time_summary_rows, resilience_summary_rows, snapshot_store


def run_attack_intensity_suite(
    config,
    quick: bool = False,
    scenario_ids: Optional[List[str]] = None,
) -> Tuple[List[Dict], List[Dict], List[float]]:
    """执行场景 × 策略 × 强度 × 随机种子的韧性边界扫描。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    attack_ratios = config.QUICK_ATTACK_INTENSITY_RATIOS if quick else config.ATTACK_INTENSITY_RATIOS
    selected_scenarios = [
        scenario for scenario in config.ATTACK_SCENARIOS
        if scenario_ids is None or scenario["id"] in scenario_ids
    ]

    raw_rows: List[Dict] = []
    total_runs = len(selected_scenarios) * len(config.RECOVERY_STRATEGIES) * len(attack_ratios) * len(seeds)
    run_index = 0

    for scenario in selected_scenarios:
        for strategy in config.RECOVERY_STRATEGIES:
            for attack_ratio in attack_ratios:
                for seed in seeds:
                    run_index += 1
                    print(
                        f"[intensity {run_index}/{total_runs}] "
                        f"scenario={scenario['id']}, strategy={strategy['id']}, "
                        f"ratio={attack_ratio:.0%}, seed={seed}"
                    )
                    run_config = build_run_config(
                        config,
                        scenario,
                        strategy,
                        seed,
                        attack_ratio=attack_ratio,
                    )
                    _, resilience_row = simulate_single_run(
                        run_config,
                        scenario,
                        strategy,
                        snapshot_store=None,
                    )
                    raw_rows.append(resilience_row)

    summary_rows = aggregate_attack_intensity_summary(raw_rows)
    return raw_rows, summary_rows, attack_ratios


def get_base_output_fieldnames() -> Dict[str, List[str]]:
    """返回基础场景扫描所需的 CSV 字段。"""
    return {
        "raw": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "seed",
            "time",
            "Q_phy",
            "Q_comm",
            "Q_mis",
            "Q_overall",
            "alive_nodes",
            "phy_edges",
            "comm_edges",
            "mis_edges",
            "valid_paths",
            "attacked_count",
            "jammed_count",
        ],
        "time_summary": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "time",
            "num_runs",
            "Q_phy_mean",
            "Q_phy_std",
            "Q_comm_mean",
            "Q_comm_std",
            "Q_mis_mean",
            "Q_mis_std",
            "Q_overall_mean",
            "Q_overall_std",
            "alive_nodes_mean",
            "alive_nodes_std",
            "phy_edges_mean",
            "phy_edges_std",
            "comm_edges_mean",
            "comm_edges_std",
            "mis_edges_mean",
            "mis_edges_std",
            "valid_paths_mean",
            "valid_paths_std",
            "attacked_count_mean",
            "attacked_count_std",
            "jammed_count_mean",
            "jammed_count_std",
        ],
        "resilience_summary": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "attack_ratio",
            "num_runs",
            "resilience_mean",
            "resilience_std",
            "final_Q_phy_mean",
            "final_Q_phy_std",
            "final_Q_comm_mean",
            "final_Q_comm_std",
            "final_Q_mis_mean",
            "final_Q_mis_std",
            "final_Q_overall_mean",
            "final_Q_overall_std",
        ],
        "layer_impact": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "layer_id",
            "layer_label",
            "final_mean",
            "final_std",
            "static_baseline_mean",
            "absolute_gain_vs_static",
            "relative_gain_vs_static_pct",
            "rank_within_scenario_layer",
            "is_best_strategy",
        ],
    }


def get_intensity_output_fieldnames() -> Dict[str, List[str]]:
    """返回攻击强度扫描所需的 CSV 字段。"""
    return {
        "raw": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "attack_ratio",
            "seed",
            "resilience",
            "final_Q_phy",
            "final_Q_comm",
            "final_Q_mis",
            "final_Q_overall",
        ],
        "summary": [
            "scenario_id",
            "scenario_label",
            "mode_label",
            "targeting_label",
            "strategy_id",
            "strategy_label",
            "attack_ratio",
            "num_runs",
            "resilience_mean",
            "resilience_std",
            "final_Q_phy_mean",
            "final_Q_phy_std",
            "final_Q_comm_mean",
            "final_Q_comm_std",
            "final_Q_mis_mean",
            "final_Q_mis_std",
            "final_Q_overall_mean",
            "final_Q_overall_std",
        ],
    }


def save_base_outputs(
    config,
    raw_rows: List[Dict],
    time_summary_rows: List[Dict],
    resilience_summary_rows: List[Dict],
    quick: bool,
) -> List[Dict]:
    """保存基础场景扫描结果。"""
    fieldnames = get_base_output_fieldnames()
    layer_impact_rows = build_layer_impact_summary(resilience_summary_rows)

    save_csv(config.OUTPUT_DIR / "experiment2_raw_timeseries.csv", raw_rows, fieldnames["raw"])
    save_csv(config.OUTPUT_DIR / "experiment2_timeseries_summary.csv", time_summary_rows, fieldnames["time_summary"])
    save_csv(
        config.OUTPUT_DIR / "experiment2_resilience_summary.csv",
        resilience_summary_rows,
        fieldnames["resilience_summary"],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment2_layer_impact_summary.csv",
        layer_impact_rows,
        fieldnames["layer_impact"],
    )

    metadata = {
        "quick_mode": quick,
        "random_seeds": config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS,
        "attack_time": config.ATTACK_TIME,
        "attack_duration": config.ATTACK_DURATION,
        "attack_batch_weights": getattr(config, "ATTACK_BATCH_WEIGHTS", None),
        "attack_ratio": config.ATTACK_RATIO,
        "attack_nodes": config.ATTACK_NODES,
        "task_phase_schedule": config.TASK_PHASE_SCHEDULE,
        "q_min": config.Q_MIN,
        "lambda": config.LAMBDA,
        "reconfigure_trigger_time": config.RECONFIGURE_TRIGGER_TIME,
        "recovery_speed": config.RECOVERY_SPEED,
        "recovery_speed_profile": getattr(config, "RECOVERY_SPEED_PROFILE", None),
        "search_radius": config.SEARCH_RADIUS,
        "baseline_trigger_physical_degree": config.BASELINE_TRIGGER_PHYSICAL_DEGREE,
        "utility_min_acceptance": config.UTILITY_MIN_ACCEPTANCE,
        "use_logic_load_correction": config.USE_LOGIC_LOAD_CORRECTION,
        "attack_scenarios": config.ATTACK_SCENARIOS,
        "recovery_strategies": config.RECOVERY_STRATEGIES,
        "snapshot_scenario": config.SNAPSHOT_SCENARIO,
        "snapshot_compare_time": config.SNAPSHOT_COMPARE_TIME,
    }
    with (config.OUTPUT_DIR / "experiment2_summary.json").open("w", encoding="utf-8") as file:
        json.dump(
            {
                "metadata": metadata,
                "resilience_summary_rows": resilience_summary_rows,
            },
            file,
            ensure_ascii=False,
            indent=2,
        )

    return layer_impact_rows


def generate_base_figures(
    config,
    time_summary_rows: List[Dict],
    resilience_summary_rows: List[Dict],
    snapshot_store: Dict[str, Dict],
) -> None:
    """生成基础场景扫描对应图 1、3-9。"""
    plot_dynamic_recovery_matrix(
        config,
        time_summary_rows,
        output_path=config.OUTPUT_DIR / "figure_1_dynamic_recovery_matrix.png",
    )
    plot_resilience_heatmap(
        config,
        resilience_summary_rows,
        output_path=config.OUTPUT_DIR / "figure_3_resilience_heatmap.png",
    )
    plot_snapshot_evolution(
        config,
        snapshot_store,
        output_path=config.OUTPUT_DIR / "figure_4_spatial_reconfiguration_snapshots.png",
    )
    plot_layer_recovery_matrix(
        config,
        time_summary_rows,
        metric_name="Q_phy",
        ylabel="Physical-Layer Performance $Q_{phy}(t)$",
        title="Dynamic Impact of Recovery Strategies on Physical-Layer Performance",
        output_path=config.OUTPUT_DIR / "figure_5_qphy_recovery_matrix.png",
    )
    plot_layer_recovery_matrix(
        config,
        time_summary_rows,
        metric_name="Q_comm",
        ylabel="Communication-Layer Performance $Q_{comm}(t)$",
        title="Dynamic Impact of Recovery Strategies on Communication-Layer Performance",
        output_path=config.OUTPUT_DIR / "figure_6_qcomm_recovery_matrix.png",
    )
    plot_layer_recovery_matrix(
        config,
        time_summary_rows,
        metric_name="Q_mis",
        ylabel="Mission-Layer Performance $Q_{mis}(t)$",
        title="Dynamic Impact of Recovery Strategies on Mission-Layer Performance",
        output_path=config.OUTPUT_DIR / "figure_7_qmis_recovery_matrix.png",
    )
    plot_final_layer_performance_bars(
        config,
        resilience_summary_rows,
        output_path=config.OUTPUT_DIR / "figure_8_final_layer_performance_bars.png",
    )
    plot_resilience_grouped_bars(
        config,
        resilience_summary_rows,
        output_path=config.OUTPUT_DIR / "figure_9_resilience_grouped_bars.png",
    )


def save_intensity_outputs(
    config,
    intensity_raw_rows: List[Dict],
    intensity_summary_rows: List[Dict],
) -> None:
    """保存攻击强度扫描结果。"""
    fieldnames = get_intensity_output_fieldnames()
    save_csv(
        config.OUTPUT_DIR / "experiment2_attack_intensity_raw.csv",
        intensity_raw_rows,
        fieldnames["raw"],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment2_attack_intensity_summary.csv",
        intensity_summary_rows,
        fieldnames["summary"],
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验二：自适应重构策略效果与韧性评估")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    parser.add_argument("--skip-intensity", action="store_true", help="跳过攻击强度扫描，只生成基础场景对比图")
    args = parser.parse_args()

    config = Experiment2Config
    config.validate()
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows, time_summary_rows, resilience_summary_rows, snapshot_store = run_suite(config, quick=args.quick)
    save_base_outputs(config, raw_rows, time_summary_rows, resilience_summary_rows, quick=args.quick)
    generate_base_figures(config, time_summary_rows, resilience_summary_rows, snapshot_store)

    if not args.skip_intensity:
        intensity_raw_rows, intensity_summary_rows, attack_ratios = run_attack_intensity_suite(
            config,
            quick=args.quick,
            scenario_ids=[config.ATTACK_INTENSITY_FOCUS_SCENARIO],
        )
        save_intensity_outputs(config, intensity_raw_rows, intensity_summary_rows)

    print(f"实验二完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
