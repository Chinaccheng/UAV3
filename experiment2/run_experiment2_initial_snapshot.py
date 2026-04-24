"""
生成实验二在 t=0 的三层网络实例化快照。

特性：
    1. 使用与 figure_4_spatial_reconfiguration_snapshots.png 子图 (a) 相同的随机种子；
    2. 采用与 result/main/node_positions_all_layers_t16.png 接近的三子图布局风格；
    3. 图中标题、坐标轴、图例均使用英文；
    4. 输出保存到 result/experiment2/figure_2_initial_three_layer_snapshot.png。

运行方式：
    python experiment2/run_experiment2_initial_snapshot.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Dict

CURRENT_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = CURRENT_DIR / ".mplconfig"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

from attack import AttackModule
from experiment_common import initialize_nodes, update_networks
from experiment2_config import Experiment2Config
from network_layers import CommunicationLayer, MissionLayer, PhysicalLayer

matplotlib.rcParams["font.sans-serif"] = ["SimHei", "Arial Unicode MS", "DejaVu Sans"]
matplotlib.rcParams["axes.unicode_minus"] = False


def resolve_snapshot_scenario() -> Dict:
    """返回与实验二 Figure 4 子图 (a) 一致的快照场景配置。"""
    scenario_id = Experiment2Config.SNAPSHOT_SCENARIO
    for scenario in Experiment2Config.ATTACK_SCENARIOS:
        if scenario["id"] == scenario_id:
            return scenario
    raise ValueError(f"未找到 SNAPSHOT_SCENARIO={scenario_id}")


def build_initial_snapshot_config():
    """构造与实验二快照一致的运行配置。"""
    scenario = resolve_snapshot_scenario()
    seed = Experiment2Config.SNAPSHOT_SEED
    attrs = {
        "ATTACK_MODE": scenario["mode"],
        "ATTACK_STRATEGY": scenario["strategy"],
        "ATTACK_ROLE_TARGET": scenario.get("role_target") or Experiment2Config.ATTACK_ROLE_TARGET,
        "ATTACK_RECOVER_TIME": (
            Experiment2Config.TIME_STEPS
            if scenario["mode"] == "cyber"
            else Experiment2Config.ATTACK_TIME
        ),
        "RANDOM_SEED": seed,
        "SCENARIO_ID": scenario["id"],
    }
    class_name = f"Experiment2InitialSnapshot_{scenario['id']}_{seed}"
    config = type(class_name, (Experiment2Config,), attrs)
    config.validate()
    return config, scenario


NODE_STYLES = {
    "SENSOR": {"color": "#1f77b4", "marker": "o", "label": "Sensor"},
    "DECIDER": {"color": "#ff7f0e", "marker": "s", "label": "Decider"},
    "INFLUENCER": {"color": "#d62728", "marker": "^", "label": "Influencer"},
}


def draw_directed_edge(
    ax,
    start_pos,
    end_pos,
    *,
    color: str,
    linewidth: float,
    alpha: float,
    linestyle: str = "-",
) -> None:
    """绘制有向边。"""
    ax.annotate(
        "",
        xy=(end_pos[0], end_pos[1]),
        xytext=(start_pos[0], start_pos[1]),
        arrowprops=dict(
            arrowstyle="->",
            color=color,
            lw=linewidth,
            alpha=alpha,
            linestyle=linestyle,
            shrinkA=8,
            shrinkB=8,
        ),
    )


def _scatter_alive_nodes(ax, nodes) -> None:
    """按角色绘制存活节点。"""
    for node_type, style in NODE_STYLES.items():
        typed_nodes = [node for node in nodes if node.is_alive and node.type.name == node_type]
        if not typed_nodes:
            continue
        ax.scatter(
            [node.position[0] for node in typed_nodes],
            [node.position[1] for node in typed_nodes],
            s=80,
            c=style["color"],
            marker=style["marker"],
            edgecolors="white",
            linewidths=0.55,
            alpha=1.0,
            zorder=4,
            label=style["label"],
        )


def _style_axis(ax, title: str) -> None:
    """统一坐标轴样式。"""
    ax.set_title(title, fontsize=12, fontweight="bold")
    ax.set_xlim(0.0, 100.0)
    ax.set_ylim(0.0, 100.0)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.3)
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")


def build_node_handles() -> list[Line2D]:
    """构造节点图例句柄。"""
    handles = []
    for node_type in ("SENSOR", "DECIDER", "INFLUENCER"):
        style = NODE_STYLES[node_type]
        handles.append(
            Line2D(
                [0],
                [0],
                marker=style["marker"],
                color="w",
                markerfacecolor=style["color"],
                markeredgecolor="white",
                markeredgewidth=0.7,
                markersize=8.5,
                linestyle="None",
                label=style["label"],
            )
        )
    return handles


def _draw_physical_panel(ax, nodes, physical_layer: PhysicalLayer) -> None:
    """绘制物理层子图。"""
    alive_lookup = {node.id: node for node in nodes if node.is_alive}
    for u, v in physical_layer.graph.edges():
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u].position
        pos_v = alive_lookup[v].position
        ax.plot(
            [pos_u[0], pos_v[0]],
            [pos_u[1], pos_v[1]],
            color="gray",
            linewidth=0.8,
            alpha=0.4,
            zorder=1,
        )

    _scatter_alive_nodes(ax, nodes)
    _style_axis(ax, "Physical Layer Topology")


def _draw_communication_panel(ax, nodes, comm_layer: CommunicationLayer) -> None:
    """绘制通信层子图。"""
    alive_lookup = {node.id: node for node in nodes if node.is_alive}
    for u, v in comm_layer.graph.edges():
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u].position
        pos_v = alive_lookup[v].position
        draw_directed_edge(
            ax,
            pos_u,
            pos_v,
            color="green",
            linewidth=1.0,
            linestyle="--",
            alpha=0.6,
        )

    _scatter_alive_nodes(ax, nodes)
    _style_axis(ax, "Communication Layer Topology")


def _draw_mission_panel(ax, nodes, mission_layer: MissionLayer) -> None:
    """绘制任务层子图。"""
    alive_lookup = {node.id: node for node in nodes if node.is_alive}
    for u, v in mission_layer.graph.edges():
        if u not in alive_lookup or v not in alive_lookup:
            continue
        pos_u = alive_lookup[u].position
        pos_v = alive_lookup[v].position
        draw_directed_edge(
            ax,
            pos_u,
            pos_v,
            color="#b2182b",
            linewidth=1.7,
            alpha=0.7,
        )

    _scatter_alive_nodes(ax, nodes)
    _style_axis(ax, "Mission Layer Topology")


def plot_initial_snapshot(output_path: Path) -> None:
    """生成并保存 t=0 三层网络快照。"""
    config, _scenario = build_initial_snapshot_config()

    nodes = initialize_nodes(config)
    physical_layer = PhysicalLayer(config)
    comm_layer = CommunicationLayer(config)
    mission_layer = MissionLayer(config)
    attack_module = AttackModule(config)

    update_networks(
        config,
        nodes,
        physical_layer,
        comm_layer,
        mission_layer,
        attack_module,
        t=0,
    )

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    fig.suptitle(
        "Initial Three-Layer Network Snapshot at t = 0",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    _draw_physical_panel(axes[0], nodes, physical_layer)
    _draw_communication_panel(axes[1], nodes, comm_layer)
    _draw_mission_panel(axes[2], nodes, mission_layer)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    legend_handles = build_node_handles() + [
        Line2D([0], [0], color="gray", linewidth=1.2, alpha=0.6, label="Physical Link"),
        Line2D([0], [0], color="green", linewidth=1.2, linestyle="--", alpha=0.8, label="Directed Communication Link"),
        Line2D([0], [0], color="#b2182b", linewidth=1.5, alpha=0.85, label="Mission Link"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper center",
        ncol=6,
        frameon=False,
        bbox_to_anchor=(0.5, 0.92),
        handlelength=2.8,
        fontsize=9.2,
        columnspacing=1.0,
        handletextpad=0.6,
    )
    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.88))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)

    print(f"Initial snapshot saved to: {output_path}")


def main() -> None:
    output_path = Experiment2Config.OUTPUT_DIR / "figure_2_initial_three_layer_snapshot.png"
    plot_initial_snapshot(output_path)


if __name__ == "__main__":
    main()
