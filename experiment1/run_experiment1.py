"""
实验一入口：
分阶段独立评估下，扫描不同攻击类型与攻击强度，分析侦察阶段与打击阶段中
物理层、通信层、任务层性能的退化差异，并比较阶段切换后的解耦效应。

本实验生成：
    图1 figure_1_stage_comparison_multilayer_intensity.png
        侦察/打击阶段下通信层、任务层与综合性能的 3x2 对比图
    图2 figure_2_physical_layer_intensity.png
        不区分阶段的物理层退化强度图
    图3 figure_3_qmis_stage_comparison.png
        不同攻击类型下任务层性能 Q_mis 的阶段对比图
    图4 figure_4_decoupling_comparison.png
        物理层与任务层表现不一致的解耦对比图

运行方式：
    python experiment1/run_experiment1.py
    python experiment1/run_experiment1.py --quick
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

CURRENT_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = CURRENT_DIR / ".mplconfig"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from attack import AttackModule
from experiment1_config import Experiment1Config
from experiment_common import get_attack_reference_graph, initialize_nodes, save_csv, update_networks
from network_layers import CommunicationLayer, MissionLayer, PhysicalLayer
from node import NodeType
from performance import PerformanceEvaluator

matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False


def build_scenario_legend_handles(scenarios: Iterable[Dict], linewidth: float = 2.0, markersize: float = 5):
    """显式构造场景图例，并按 2x3 图例的视觉阅读顺序重排。"""
    scenario_list = list(scenarios)
    scenario_map = {scenario["id"]: scenario for scenario in scenario_list}
    preferred_order = [
        "hard_random",
        "soft_random",
        "hard_topology",
        "soft_topology",
        "hard_role_decider",
        "soft_role_decider",
    ]

    ordered_scenarios = [scenario_map[scenario_id] for scenario_id in preferred_order if scenario_id in scenario_map]
    ordered_scenarios.extend(
        scenario for scenario in scenario_list if scenario["id"] not in {item["id"] for item in ordered_scenarios}
    )

    return [
        Line2D(
            [0],
            [0],
            label=scenario["label"],
            color=scenario["color"],
            linestyle=scenario["linestyle"],
            marker=scenario["marker"],
            linewidth=linewidth,
            markersize=markersize,
        )
        for scenario in ordered_scenarios
    ]


def build_stage_legend_handles(stage_styles: Iterable[Dict], linewidth: float = 2.2, markersize: float = 5):
    """显式构造阶段图例，保证侦察/打击阶段的线型在图例中清晰可见。"""
    return [
        Line2D(
            [0],
            [0],
            label=style["label"],
            color=style["color"],
            linestyle=style["linestyle"],
            marker="o",
            linewidth=linewidth,
            markersize=markersize,
        )
        for style in stage_styles
    ]


def build_decoupling_metric_legend_handles(metric_specs: Iterable[Tuple[str, str, str]], linewidth: float = 2.2):
    """图4上方第一行：颜色对应的性能指标。"""
    return [
        Line2D(
            [0],
            [0],
            label=metric_label,
            color=color,
            linestyle="-",
            marker="o",
            linewidth=linewidth,
            markersize=5,
        )
        for _, metric_label, color in metric_specs
    ]


def build_decoupling_style_legend_handles(linewidth: float = 2.2):
    """图4上方第二行：线型对应的攻击机制。"""
    return [
        Line2D([0], [0], label="Physical Destruction (Solid)", color="#444444", linestyle="-", linewidth=linewidth),
        Line2D([0], [0], label="Network Suppression (Dashed)", color="#444444", linestyle="--", linewidth=linewidth),
    ]


def build_run_config(base_config, stage_name: str, attack_scenario: Dict, attack_ratio: float, seed: int):
    """按阶段、攻击场景和强度构造单次运行配置。"""
    stage_cfg = base_config.STAGE_SCENARIOS[stage_name]
    role_target = attack_scenario.get("role_target") or base_config.ATTACK_ROLE_TARGET
    attack_nodes = int(round(base_config.N_TOTAL * attack_ratio))

    attrs = {
        "TASK_PHASE_SCHEDULE": list(stage_cfg["schedule"]),
        "ATTACK_MODE": attack_scenario["mode"],
        "ATTACK_STRATEGY": attack_scenario["strategy"],
        "ATTACK_ROLE_TARGET": role_target,
        "ATTACK_RATIO": None,
        "ATTACK_NODES": attack_nodes,
        "RANDOM_SEED": seed,
        "SNAPSHOT_TIMES": [],
    }

    class_name = (
        f"Experiment1RunConfig_{stage_name}_{attack_scenario['id']}_"
        f"{int(round(attack_ratio * 100))}_{seed}"
    )
    run_config = type(class_name, (base_config,), attrs)
    run_config.validate()
    return run_config

def evaluate_single_run(config) -> Dict:
    """
    单次评估：
    先计算无损基线，再在固定阶段下施加一次攻击并记录攻击后的稳定性能。
    """
    nodes = initialize_nodes(config)
    physical_layer = PhysicalLayer(config)
    comm_layer = CommunicationLayer(config)
    mission_layer = MissionLayer(config)
    performance_evaluator = PerformanceEvaluator(config)
    attack_module = AttackModule(config)

    update_networks(config, nodes, physical_layer, comm_layer, mission_layer, attack_module, t=0)
    performance_evaluator.calculate_overall_performance(nodes, physical_layer, comm_layer, mission_layer)

    attack_start_time = max(1, config.ATTACK_TIME - getattr(config, "ATTACK_DURATION", 1) + 1)
    for current_time in range(attack_start_time, config.ATTACK_TIME + 1):
        attack_graph = get_attack_reference_graph(config, physical_layer, comm_layer)
        attack_module.execute_attack(nodes, current_time, graph=attack_graph)
        update_networks(
            config,
            nodes,
            physical_layer,
            comm_layer,
            mission_layer,
            attack_module,
            t=current_time,
        )

    q_phy, q_comm, q_mis, q_overall = performance_evaluator.calculate_overall_performance(
        nodes,
        physical_layer,
        comm_layer,
        mission_layer,
    )

    attacked_count = len(attack_module.attacked_nodes)
    jammed_count = len(attack_module.jammed_nodes)
    affected_node_ids = attack_module.attacked_nodes or attack_module.jammed_nodes
    node_by_id = {node.id: node for node in nodes}
    affected_sensor_count = 0
    affected_decider_count = 0
    affected_influencer_count = 0
    for node_id in affected_node_ids:
        node = node_by_id.get(node_id)
        if node is None:
            continue
        if node.type == NodeType.SENSOR:
            affected_sensor_count += 1
        elif node.type == NodeType.DECIDER:
            affected_decider_count += 1
        elif node.type == NodeType.INFLUENCER:
            affected_influencer_count += 1

    return {
        "Q_phy": q_phy,
        "Q_comm": q_comm,
        "Q_mis": q_mis,
        "Q_overall": q_overall,
        "alive_nodes": sum(1 for node in nodes if node.is_alive),
        "phy_edges": physical_layer.graph.number_of_edges(),
        "comm_edges": comm_layer.graph.number_of_edges(),
        "mis_edges": mission_layer.graph.number_of_edges(),
        "valid_paths": len(mission_layer.valid_paths),
        "attacked_count": attacked_count,
        "jammed_count": jammed_count,
        "affected_sensor_count": affected_sensor_count,
        "affected_decider_count": affected_decider_count,
        "affected_influencer_count": affected_influencer_count,
    }


def aggregate_results(raw_rows: List[Dict]) -> List[Dict]:
    """按阶段、攻击类型和攻击强度聚合均值与标准差。"""
    grouped: Dict[Tuple[str, str, float], List[Dict]] = defaultdict(list)
    for row in raw_rows:
        key = (row["stage"], row["scenario_id"], row["attack_ratio"])
        grouped[key].append(row)

    summary_rows: List[Dict] = []
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
        "affected_sensor_count",
        "affected_decider_count",
        "affected_influencer_count",
    ]

    for (stage, scenario_id, attack_ratio), rows in sorted(grouped.items()):
        summary = {
            "stage": stage,
            "scenario_id": scenario_id,
            "attack_ratio": attack_ratio,
            "num_runs": len(rows),
            "scenario_label": rows[0]["scenario_label"],
            "stage_label": rows[0]["stage_label"],
        }
        for metric in metric_names:
            values = np.array([row[metric] for row in rows], dtype=float)
            summary[f"{metric}_mean"] = float(np.mean(values))
            summary[f"{metric}_std"] = float(np.std(values))
        summary_rows.append(summary)

    return summary_rows


def build_lookup(summary_rows: List[Dict]) -> Dict[Tuple[str, str, float], Dict]:
    return {
        (row["stage"], row["scenario_id"], row["attack_ratio"]): row
        for row in summary_rows
    }


def intensity_labels(intensities: List[float]) -> List[str]:
    return [f"{int(round(value * 100))}%" for value in intensities]


def configure_axis(ax, xlabel: str, ylabel: str, ylim: Tuple[float, float] = (0.0, 1.05)) -> None:
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_ylim(*ylim)
    ax.set_xlim(0.0, Experiment1Config.X_AXIS_MAX)
    ax.set_xticks(np.arange(0, Experiment1Config.X_AXIS_MAX + 1, 20))
    ax.grid(True, alpha=0.3)


def get_staggered_marker_indices(total_points: int, offset: int, step: int) -> List[int]:
    """
    交错设置标记点位置：
    不改变曲线本身的 x 坐标，仅让不同系列在不同的数据点上显示 marker，
    从而减少重合曲线在同一 x 位置上的标记遮挡。
    """
    if total_points <= 0:
        return []

    effective_step = max(1, step)
    start = offset % total_points
    indices = list(range(start, total_points, effective_step))
    if not indices:
        indices = [start]
    return indices


def get_attack_scenario_markevery(scenario_id: str, total_points: int) -> List[int]:
    """
    攻击场景的等差交错 marker：
    软杀伤三条线采用 (0,6)、(2,6)、(4,6)；
    硬杀伤三条线采用 (1,6)、(3,6)、(5,6)。
    """
    offset_map = {
        "soft_random": 0,
        "hard_random": 1,
        "soft_topology": 2,
        "hard_topology": 3,
        "soft_role_decider": 4,
        "hard_role_decider": 5,
    }
    return get_staggered_marker_indices(total_points, offset_map.get(scenario_id, 0), 6)


def get_stage_markevery(stage_name: str, total_points: int) -> List[int]:
    offset_map = {
        "recon": 0,
        "strike": 2,
    }
    return get_staggered_marker_indices(total_points, offset_map.get(stage_name, 0), 4)


def get_metric_markevery(metric_key: str, total_points: int) -> List[int]:
    offset_map = {
        "Q_phy_mean": 0,
        "Q_comm_mean": 2,
        "Q_mis_mean": 4,
    }
    return get_staggered_marker_indices(total_points, offset_map.get(metric_key, 0), 6)


def get_metric_plot_style(metric_key: str, scenario_id: str) -> Dict[str, float | str]:
    """为易重合的指标提供更强的可读性设置。"""
    if metric_key != "Q_mis_mean":
        return {
            "linewidth": 2.0,
            "markersize": 5.0,
            "markerfacecolor": "auto",
            "markeredgecolor": "auto",
            "markeredgewidth": 0.0,
            "zorder": 2.0,
        }

    order_map = {
        "soft_random": 2.0,
        "hard_random": 2.2,
        "soft_topology": 2.4,
        "hard_topology": 2.6,
        "soft_role_decider": 2.8,
        "hard_role_decider": 3.0,
    }
    role_scenarios = {"soft_role_decider", "hard_role_decider"}
    return {
        "linewidth": 2.35 if scenario_id in role_scenarios else 2.2,
        "markersize": 6.2 if scenario_id in role_scenarios else 5.8,
        "markerfacecolor": "white",
        "markeredgecolor": "auto",
        "markeredgewidth": 1.3 if scenario_id in role_scenarios else 1.1,
        "zorder": order_map.get(scenario_id, 2.0),
    }


def get_metric_display_offset(metric_key: str, scenario_id: str) -> float:
    """
    为严重重合的任务层曲线增加极小的仅显示偏移，
    不改变原始数据，只改善图面可分辨性。
    """
    if metric_key != "Q_mis_mean":
        return 0.0

    offset_map = {
        "hard_random": 0.012,
        "hard_topology": -0.012,
        "soft_random": 0.008,
        "soft_topology": -0.008,
        "hard_role_decider": 0.014,
        "soft_role_decider": -0.014,
    }
    return offset_map.get(scenario_id, 0.0)


def plot_attack_scenario_metric_curves(
    ax,
    config,
    lookup: Dict[Tuple[str, str, float], Dict],
    stage_name: str,
    metric_key: str,
    intensities: List[float],
) -> None:
    """在给定坐标轴上绘制某阶段、某指标的六类攻击曲线。"""
    x = np.array(intensities) * 100.0
    for scenario in config.ATTACK_SCENARIOS:
        style = get_metric_plot_style(metric_key, scenario["id"])
        y = []
        for attack_ratio in intensities:
            row = lookup[(stage_name, scenario["id"], attack_ratio)]
            y.append(row[metric_key])
        display_offset = get_metric_display_offset(metric_key, scenario["id"])
        if display_offset != 0.0:
            y = [float(np.clip(value + display_offset, 0.0, 1.02)) for value in y]
        markerfacecolor = style["markerfacecolor"]
        markeredgecolor = scenario["color"] if style["markeredgecolor"] == "auto" else style["markeredgecolor"]
        ax.plot(
            x,
            y,
            color=scenario["color"],
            linestyle=scenario["linestyle"],
            marker=scenario["marker"],
            linewidth=style["linewidth"],
            markersize=style["markersize"],
            markevery=get_attack_scenario_markevery(scenario["id"], len(intensities)),
            markerfacecolor=scenario["color"] if markerfacecolor == "auto" else markerfacecolor,
            markeredgecolor=markeredgecolor,
            markeredgewidth=style["markeredgewidth"],
            zorder=style["zorder"],
        )


def plot_stage_comparison_multilayer(
    config,
    summary_rows: List[Dict],
    intensities: List[float],
    output_path: Path,
) -> None:
    """绘制侦察/打击阶段下通信层、任务层与综合性能的 3x2 对比图。"""
    lookup = build_lookup(summary_rows)
    stage_names = ["recon", "strike"]
    metrics = [
        ("Q_comm_mean", "Communication-Layer Performance\n$Q_{comm}$"),
        ("Q_mis_mean", "Mission-Layer Performance\n$Q_{mis}$"),
        ("Q_overall_mean", "Integrated Performance\n$Q$"),
    ]

    fig, axes = plt.subplots(
        len(metrics),
        len(stage_names),
        figsize=config.FIGSIZE_STAGE_COMPARISON,
        sharex=True,
        sharey="row",
    )
    fig.suptitle(
        "Stage Comparison of Communication, Mission, and Integrated Performance Under Different Attack Intensities",
        fontsize=15,
        fontweight="bold",
        y=0.985,
    )

    for col_index, stage_name in enumerate(stage_names):
        axes[0, col_index].set_title(config.STAGE_SCENARIOS[stage_name]["label"], fontsize=12, pad=10)
        for row_index, (metric_key, ylabel) in enumerate(metrics):
            ax = axes[row_index, col_index]
            plot_attack_scenario_metric_curves(ax, config, lookup, stage_name, metric_key, intensities)
            configure_axis(
                ax,
                "Disrupted Node Ratio in the Swarm (%)" if row_index == len(metrics) - 1 else "",
                ylabel if col_index == 0 else "",
            )
            if row_index != len(metrics) - 1:
                ax.tick_params(axis="x", labelbottom=False)
            if col_index > 0:
                ax.tick_params(axis="y", labelleft=False)

    fig.legend(
        handles=build_scenario_legend_handles(config.ATTACK_SCENARIOS),
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.945),
        handlelength=3.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.86))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_physical_layer_intensity(
    config,
    summary_rows: List[Dict],
    intensities: List[float],
    output_path: Path,
) -> None:
    """绘制不区分阶段的物理层退化强度图。"""
    lookup = build_lookup(summary_rows)
    stage_names = ["recon", "strike"]
    x = np.array(intensities) * 100.0

    fig, ax = plt.subplots(figsize=config.FIGSIZE_PHYSICAL)
    fig.suptitle(
        "Stage-Invariant Physical-Layer Degradation Under Different Attack Intensities",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    for scenario in config.ATTACK_SCENARIOS:
        style = get_metric_plot_style("Q_phy_mean", scenario["id"])
        y = []
        for attack_ratio in intensities:
            stage_values = [lookup[(stage_name, scenario["id"], attack_ratio)]["Q_phy_mean"] for stage_name in stage_names]
            y.append(float(np.mean(stage_values)))
        markerfacecolor = style["markerfacecolor"]
        markeredgecolor = scenario["color"] if style["markeredgecolor"] == "auto" else style["markeredgecolor"]
        ax.plot(
            x,
            y,
            color=scenario["color"],
            linestyle=scenario["linestyle"],
            marker=scenario["marker"],
            linewidth=style["linewidth"],
            markersize=style["markersize"],
            markevery=get_attack_scenario_markevery(scenario["id"], len(intensities)),
            markerfacecolor=scenario["color"] if markerfacecolor == "auto" else markerfacecolor,
            markeredgecolor=markeredgecolor,
            markeredgewidth=style["markeredgewidth"],
            zorder=style["zorder"],
            label=scenario["label"],
        )

    configure_axis(ax, "Disrupted Node Ratio in the Swarm (%)", "Physical-Layer Performance $Q_{phy}$")
    ax.text(
        0.985,
        0.06,
        "Recon and strike stages coincide\nat the physical layer",
        transform=ax.transAxes,
        ha="right",
        va="bottom",
        fontsize=10,
        color="#555555",
        bbox={"boxstyle": "round,pad=0.25", "facecolor": "white", "edgecolor": "#cccccc", "alpha": 0.85},
    )

    fig.legend(
        handles=build_scenario_legend_handles(config.ATTACK_SCENARIOS),
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.91),
        handlelength=3.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.82))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_qmis_stage_comparison(
    config,
    summary_rows: List[Dict],
    intensities: List[float],
    output_path: Path,
) -> None:
    """展示同一攻击策略在不同阶段下任务层脆弱性的差异。"""
    lookup = build_lookup(summary_rows)
    scenario_map = {scenario["id"]: scenario for scenario in config.ATTACK_SCENARIOS}
    selected_ids = config.QMIS_STAGE_COMPARISON_SCENARIOS

    fig, axes = plt.subplots(1, len(selected_ids), figsize=config.FIGSIZE_COMPARISON)
    if len(selected_ids) == 1:
        axes = [axes]

    fig.suptitle(
        "Comparison of Mission-Layer Vulnerability Across Mission Stages",
        fontsize=15,
        fontweight="bold",
        y=0.99,
    )

    x = np.array(intensities) * 100.0
    stage_styles = {
        "recon": {"label": "Intelligence Aggregation Stage", "color": "#1f77b4", "linestyle": "-"},
        "strike": {"label": "Tactical Execution Stage", "color": "#d62728", "linestyle": "--"},
    }
    decider_exhaustion_percent = 100.0 * config.N_DECIDER / config.N_TOTAL
    for ax, scenario_id in zip(axes, selected_ids):
        scenario = scenario_map[scenario_id]
        for stage_name, style in stage_styles.items():
            y = []
            for attack_ratio in intensities:
                row = lookup[(stage_name, scenario_id, attack_ratio)]
                y.append(row["Q_mis_mean"])
            ax.plot(
                x,
                y,
                label=style["label"],
                color=style["color"],
                linestyle=style["linestyle"],
                marker=scenario["marker"],
                linewidth=2.2,
                markersize=5,
                markevery=get_stage_markevery(stage_name, len(intensities)),
            )

        if "role_decider" in scenario_id:
            ax.axvline(
                x=decider_exhaustion_percent,
                color="#555555",
                linestyle=":",
                linewidth=1.8,
                alpha=0.9,
            )
            ax.text(
                decider_exhaustion_percent + 1.5,
                0.94,
                f"Decider Exhaustion Threshold ({decider_exhaustion_percent:.0f}%)",
                color="#555555",
                fontsize=10,
                ha="left",
                va="top",
            )

        ax.set_title(scenario["label"], fontsize=12)
        configure_axis(ax, "Disrupted Node Ratio in the Swarm (%)", "Mission-Layer Performance $Q_{mis}$")

    fig.legend(
        handles=build_stage_legend_handles(stage_styles.values()),
        loc="upper center",
        ncol=2,
        frameon=False,
        bbox_to_anchor=(0.5, 0.935),
        handlelength=3.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.84))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def plot_decoupling_comparison(
    config,
    summary_rows: List[Dict],
    intensities: List[float],
    output_path: Path,
) -> None:
    """展示硬杀伤与软杀伤对三层的解耦影响差异。"""
    lookup = build_lookup(summary_rows)
    scenario_map = {scenario["id"]: scenario for scenario in config.ATTACK_SCENARIOS}
    stage_name = config.DECOUPLING_STAGE
    selected_ids = config.DECOUPLING_SCENARIOS

    metric_specs = [
        ("Q_phy_mean", "$Q_{phy}$", "#1f77b4"),
        ("Q_comm_mean", "$Q_{comm}$", "#2ca02c"),
        ("Q_mis_mean", "$Q_{mis}$", "#d62728"),
    ]

    fig, axes = plt.subplots(1, len(selected_ids), figsize=config.FIGSIZE_DECOUPLING)
    if len(selected_ids) == 1:
        axes = [axes]

    fig.suptitle(
        f"Layer-Wise Response Differences Under Distinct Attack Mechanisms in the {config.STAGE_SCENARIOS[stage_name]['label']}",
        fontsize=15,
        fontweight="bold",
        y=0.99,
    )

    x = np.array(intensities) * 100.0
    for ax, scenario_id in zip(axes, selected_ids):
        scenario = scenario_map[scenario_id]
        for metric_key, metric_label, color in metric_specs:
            y = []
            for attack_ratio in intensities:
                row = lookup[(stage_name, scenario_id, attack_ratio)]
                y.append(row[metric_key])
            ax.plot(
                x,
                y,
                label=metric_label,
                color=color,
                linestyle=scenario["linestyle"],
                marker="o",
                linewidth=2.2,
                markersize=5,
                markevery=get_metric_markevery(metric_key, len(intensities)),
            )
        ax.set_title(scenario["label"], fontsize=12)
        configure_axis(ax, "Disrupted Node Ratio in the Swarm (%)", "Normalized Performance")

    metric_legend = fig.legend(
        handles=build_decoupling_metric_legend_handles(metric_specs),
        loc="upper center",
        ncol=3,
        frameon=False,
        bbox_to_anchor=(0.5, 0.945),
        handlelength=3.0,
    )
    fig.add_artist(metric_legend)
    fig.legend(
        handles=build_decoupling_style_legend_handles(),
        loc="upper center",
        ncol=2,
        frameon=False,
        bbox_to_anchor=(0.5, 0.905),
        handlelength=3.0,
        columnspacing=2.0,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.80))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def run_suite(config, quick: bool = False) -> Tuple[List[Dict], List[Dict]]:
    """执行阶段 × 攻击类型 × 强度 × 随机种子的全组合扫描。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    intensities = config.QUICK_ATTACK_INTENSITY_RATIOS if quick else config.ATTACK_INTENSITY_RATIOS

    raw_rows: List[Dict] = []
    total_runs = len(config.STAGE_SCENARIOS) * len(config.ATTACK_SCENARIOS) * len(intensities) * len(seeds)
    run_index = 0

    for stage_name, stage_cfg in config.STAGE_SCENARIOS.items():
        for scenario in config.ATTACK_SCENARIOS:
            for attack_ratio in intensities:
                for seed in seeds:
                    run_index += 1
                    print(
                        f"[{run_index}/{total_runs}] "
                        f"stage={stage_name}, scenario={scenario['id']}, ratio={attack_ratio:.1%}, seed={seed}"
                    )
                    run_config = build_run_config(config, stage_name, scenario, attack_ratio, seed)
                    result = evaluate_single_run(run_config)
                    raw_rows.append(
                        {
                            "stage": stage_name,
                            "stage_label": stage_cfg["label"],
                            "scenario_id": scenario["id"],
                            "scenario_label": scenario["label"],
                            "attack_ratio": attack_ratio,
                            "seed": seed,
                            **result,
                        }
                    )

    summary_rows = aggregate_results(raw_rows)
    return raw_rows, summary_rows


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验一：分阶段独立评估下的攻击机理与多层退化特性分析")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用少量强度点和一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment1Config
    config.validate()
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows, summary_rows = run_suite(config, quick=args.quick)
    intensities = config.QUICK_ATTACK_INTENSITY_RATIOS if args.quick else config.ATTACK_INTENSITY_RATIOS

    raw_fieldnames = [
        "stage",
        "stage_label",
        "scenario_id",
        "scenario_label",
        "attack_ratio",
        "seed",
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
        "affected_sensor_count",
        "affected_decider_count",
        "affected_influencer_count",
    ]
    summary_fieldnames = [
        "stage",
        "stage_label",
        "scenario_id",
        "scenario_label",
        "attack_ratio",
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
        "affected_sensor_count_mean",
        "affected_sensor_count_std",
        "affected_decider_count_mean",
        "affected_decider_count_std",
        "affected_influencer_count_mean",
        "affected_influencer_count_std",
    ]

    save_csv(config.OUTPUT_DIR / "experiment1_raw_results.csv", raw_rows, raw_fieldnames)
    save_csv(config.OUTPUT_DIR / "experiment1_summary_results.csv", summary_rows, summary_fieldnames)

    metadata = {
        "quick_mode": args.quick,
        "random_seeds": config.QUICK_RANDOM_SEEDS if args.quick else config.RANDOM_SEEDS,
        "attack_intensity_ratios": intensities,
        "stage_scenarios": config.STAGE_SCENARIOS,
        "attack_scenarios": config.ATTACK_SCENARIOS,
        "degree_reference_layer": config.ATTACK_DEGREE_LAYER,
        "role_attack_cascade_enabled": config.ATTACK_ROLE_CASCADE_ENABLED,
        "role_attack_cascade_sequence": config.ATTACK_ROLE_CASCADE_SEQUENCE,
        "recovery_speed": config.RECOVERY_SPEED,
    }
    with (config.OUTPUT_DIR / "experiment1_summary.json").open("w", encoding="utf-8") as file:
        json.dump(
            {
                "metadata": metadata,
                "summary_rows": summary_rows,
            },
            file,
            ensure_ascii=False,
            indent=2,
        )

    plot_stage_comparison_multilayer(
        config,
        summary_rows,
        intensities=intensities,
        output_path=config.OUTPUT_DIR / "figure_1_stage_comparison_multilayer_intensity.png",
    )
    plot_physical_layer_intensity(
        config,
        summary_rows,
        intensities=intensities,
        output_path=config.OUTPUT_DIR / "figure_2_physical_layer_intensity.png",
    )
    plot_qmis_stage_comparison(
        config,
        summary_rows,
        intensities=intensities,
        output_path=config.OUTPUT_DIR / "figure_3_qmis_stage_comparison.png",
    )
    plot_decoupling_comparison(
        config,
        summary_rows,
        intensities=intensities,
        output_path=config.OUTPUT_DIR / "figure_4_decoupling_comparison.png",
    )

    for obsolete_path in (
        config.OUTPUT_DIR / "figure_1_recon_stage_multilayer_intensity.png",
        config.OUTPUT_DIR / "figure_2_strike_stage_multilayer_intensity.png",
    ):
        obsolete_path.unlink(missing_ok=True)

    print(f"实验一完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
