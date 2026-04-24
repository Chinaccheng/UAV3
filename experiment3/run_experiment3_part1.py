"""
实验三第一部分：物理与逻辑耦合阈值分析（eta 与 tau_mis）。

本实验不再使用系统总性能 Q(t) 作为主观察量，而是刻意剥离物理层指标对结论的稀释效应，
构造一个“攻击触发后进入渐进离散”的紧凑编队场景。集群在物理层仍保持全连通时，
节点间距离已开始通过通信概率 P_ij(t) 发生跨层传导，继而在任务层阈值 tau_mis 的放大下，
诱发通信层的渐进衰退与任务层的断崖式崩溃。该实验用于直接验证多层解耦框架对
“隐性退化”和“提前失效”的识别能力。

本实验生成：
    图1 figure_1_eta_tau_coupling_matrix.png
        上图为通信层渐进衰退，下图为任务层性能 Q_mis 在不同 eta 与 tau_mis 组合下的崩溃对比图

运行方式：
    python experiment3/run_experiment3_part1.py
    python experiment3/run_experiment3_part1.py --quick
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

from experiment3_common import build_lookup, build_run_config

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.lines import Line2D

from experiment_common import save_csv
from experiment3_config import Experiment3Config
from network_layers import CommunicationLayer, PhysicalLayer
from node import Node, NodeType


class Part1CommunicationLayer(CommunicationLayer):
    """第一部分专用通信层：仅保留关键 OODA 链路，避免底噪边淹没阈值效应。"""

    def _f_logic(self, node_sender: Node, node_receiver: Node, phase: int, physical_layer: PhysicalLayer):
        role_pair = (node_sender.type, node_receiver.type)
        key_link_weights = {
            (NodeType.SENSOR, NodeType.DECIDER): 0.30,
            (NodeType.DECIDER, NodeType.DECIDER): 0.08,
            (NodeType.DECIDER, NodeType.INFLUENCER): 0.65,
        }
        return key_link_weights.get(role_pair, 0.0)


def initialize_part1_nodes(config) -> Tuple[List[Node], np.ndarray]:
    """将三类节点初始化为紧凑编队，确保初始时刻处于物理全连通与强通信区。"""
    np.random.seed(config.RANDOM_SEED)
    center = np.array([config.AREA_SIZE / 2.0, config.AREA_SIZE / 2.0], dtype=float)
    nodes: List[Node] = []
    node_id = 0

    def sample_position() -> np.ndarray:
        angle = np.random.uniform(0.0, 2.0 * np.pi)
        radius = config.PART1_INITIAL_CLUSTER_RADIUS * np.sqrt(np.random.uniform(0.0, 1.0))
        offset = radius * np.array([np.cos(angle), np.sin(angle)], dtype=float)
        return center + offset

    for _ in range(config.N_SENSOR):
        nodes.append(Node(node_id, NodeType.SENSOR, sample_position(), config))
        node_id += 1

    for _ in range(config.N_DECIDER):
        nodes.append(Node(node_id, NodeType.DECIDER, sample_position(), config))
        node_id += 1

    for _ in range(config.N_INFLUENCER):
        nodes.append(Node(node_id, NodeType.INFLUENCER, sample_position(), config))
        node_id += 1

    return nodes, center


def build_dispersion_directions(nodes: List[Node], center: np.ndarray, seed: int) -> Dict[int, np.ndarray]:
    """为每个节点生成从集群中心向外的离散方向。"""
    rng = np.random.default_rng(seed + 20260415)
    directions: Dict[int, np.ndarray] = {}

    for node in nodes:
        direction = node.position - center
        norm = np.linalg.norm(direction)
        if norm <= 1e-12:
            angle = rng.uniform(0.0, 2.0 * np.pi)
            direction = np.array([np.cos(angle), np.sin(angle)], dtype=float)
        else:
            direction = direction / norm
        directions[node.id] = direction

    return directions


def apply_progressive_dispersion(config, nodes: List[Node], directions: Dict[int, np.ndarray]) -> None:
    """在触发时刻之后让节点沿径向缓慢离散。"""
    step_distance = config.PART1_DISPERSION_SPEED * config.DT
    for node in nodes:
        if not node.is_alive:
            continue
        new_position = node.position + directions[node.id] * step_distance
        node.position = np.clip(new_position, 0.0, config.AREA_SIZE)


def calculate_mean_pair_distance(nodes: List[Node]) -> float:
    """计算当前存活节点的平均两两距离。"""
    alive_nodes = [node for node in nodes if node.is_alive]
    if len(alive_nodes) <= 1:
        return 0.0

    distances = []
    for index, node_i in enumerate(alive_nodes):
        for node_j in alive_nodes[index + 1:]:
            distances.append(node_i.get_distance(node_j))
    return float(np.mean(distances)) if distances else 0.0


def is_physical_layer_complete(physical_layer: PhysicalLayer) -> int:
    """判断当前物理层是否仍然保持全连通。"""
    node_count = physical_layer.graph.number_of_nodes()
    if node_count <= 1:
        return 1
    full_edge_count = node_count * (node_count - 1) // 2
    return int(physical_layer.graph.number_of_edges() == full_edge_count)


def aggregate_part1_time_series(raw_rows: List[Dict], key_fields: List[str]) -> List[Dict]:
    """按 key_fields + time 聚合第一部分核心指标。"""
    grouped: Dict[Tuple, List[Dict]] = defaultdict(list)
    for row in raw_rows:
        grouped[tuple(row[field] for field in key_fields + ["time"])].append(row)

    metric_names = ["Q_comm", "Q_mis", "mean_pair_distance", "valid_path_count", "physical_complete"]
    summary_rows: List[Dict] = []
    for _, rows in sorted(grouped.items()):
        summary = {field: rows[0][field] for field in key_fields}
        summary["time"] = rows[0]["time"]
        summary["num_runs"] = len(rows)
        for metric_name in metric_names:
            values = np.array([row[metric_name] for row in rows], dtype=float)
            summary[f"{metric_name}_mean"] = float(np.mean(values))
            summary[f"{metric_name}_std"] = float(np.std(values))
        summary_rows.append(summary)
    return summary_rows


def is_valid_task_transition(from_type: NodeType, to_type: NodeType) -> bool:
    """检查节点类型转换是否符合任务链传输规则。"""
    valid_rules = {
        (NodeType.SENSOR, NodeType.SENSOR),
        (NodeType.SENSOR, NodeType.DECIDER),
        (NodeType.DECIDER, NodeType.DECIDER),
        (NodeType.DECIDER, NodeType.SENSOR),
        (NodeType.DECIDER, NodeType.INFLUENCER),
    }
    return (from_type, to_type) in valid_rules


def build_part1_task_graph(nodes: List[Node], comm_layer: CommunicationLayer, prob_threshold: float) -> nx.DiGraph:
    """基于阈值通信概率构造第一部分任务图。"""
    task_graph = nx.DiGraph()
    node_dict = {node.id: node for node in nodes if node.is_alive}
    for node in node_dict.values():
        task_graph.add_node(node.id, node=node)

    for (node_i_id, node_j_id), prob in comm_layer.activation_probabilities.items():
        if prob < prob_threshold:
            continue
        node_i = node_dict.get(node_i_id)
        node_j = node_dict.get(node_j_id)
        if node_i is None or node_j is None:
            continue
        if is_valid_task_transition(node_i.type, node_j.type):
            task_graph.add_edge(node_i_id, node_j_id)

    return task_graph


def calculate_part1_communication_raw_score(nodes: List[Node], comm_layer: CommunicationLayer) -> float:
    """计算关键通信链路平均激活概率，作为第一部分的通信层原始得分。"""
    node_dict = {node.id: node for node in nodes if node.is_alive}
    sensor_nodes = [node_id for node_id, node in node_dict.items() if node.type == NodeType.SENSOR]
    decider_nodes = [node_id for node_id, node in node_dict.items() if node.type == NodeType.DECIDER]
    influencer_nodes = [node_id for node_id, node in node_dict.items() if node.type == NodeType.INFLUENCER]

    possible_edge_count = (
        len(sensor_nodes) * len(decider_nodes)
        + len(decider_nodes) * max(0, len(decider_nodes) - 1)
        + len(decider_nodes) * len(influencer_nodes)
    )
    if possible_edge_count <= 0:
        return 0.0

    probability_sum = 0.0
    for sensor_id in sensor_nodes:
        for decider_id in decider_nodes:
            probability_sum += comm_layer.activation_probabilities.get((sensor_id, decider_id), 0.0)
    for decider_id in decider_nodes:
        for other_decider_id in decider_nodes:
            if decider_id == other_decider_id:
                continue
            probability_sum += comm_layer.activation_probabilities.get((decider_id, other_decider_id), 0.0)
    for decider_id in decider_nodes:
        for influencer_id in influencer_nodes:
            probability_sum += comm_layer.activation_probabilities.get((decider_id, influencer_id), 0.0)

    return probability_sum / possible_edge_count


def evaluate_part1_mission_state(nodes: List[Node], task_graph: nx.DiGraph) -> int:
    """统计当前可达的 S-I 有效杀伤链对数量。"""
    node_dict = {node.id: node for node in nodes if node.is_alive}
    sensor_nodes = [node_id for node_id, node in node_dict.items() if node.type == NodeType.SENSOR]
    influencer_nodes = [node_id for node_id, node in node_dict.items() if node.type == NodeType.INFLUENCER]

    if not sensor_nodes or not influencer_nodes or task_graph.number_of_edges() == 0:
        return 0

    valid_chain_count = 0
    for sensor_id in sensor_nodes:
        lengths = nx.single_source_shortest_path_length(task_graph, sensor_id, cutoff=4)
        valid_chain_count += sum(
            1
            for influencer_id in influencer_nodes
            if influencer_id in lengths and lengths[influencer_id] > 0
        )

    return valid_chain_count


def simulate_part1_hidden_degradation(config) -> Dict[str, object]:
    """执行受控渐进离散场景，记录通信层与任务层的隐性退化轨迹。"""
    nodes, center = initialize_part1_nodes(config)
    directions = build_dispersion_directions(nodes, center, config.RANDOM_SEED)
    physical_layer = PhysicalLayer(config)
    comm_layer = Part1CommunicationLayer(config)
    initial_comm_raw_score = None
    initial_valid_chain_count = None

    history = {
        "time": [],
        "Q_comm": [],
        "Q_mis": [],
        "mean_pair_distance": [],
        "valid_path_count": [],
        "physical_complete": [],
    }

    def record_state(current_time: int) -> None:
        nonlocal initial_comm_raw_score, initial_valid_chain_count
        physical_layer.update(nodes)
        comm_layer.update(nodes, physical_layer, current_time)
        comm_raw_score = calculate_part1_communication_raw_score(nodes, comm_layer)
        task_graph = build_part1_task_graph(nodes, comm_layer, config.MISSION_PROB_THRESHOLD)
        valid_chain_count = evaluate_part1_mission_state(nodes, task_graph)
        if initial_comm_raw_score is None:
            initial_comm_raw_score = comm_raw_score if comm_raw_score > 0 else 1.0
        if initial_valid_chain_count is None:
            initial_valid_chain_count = valid_chain_count if valid_chain_count > 0 else 1.0
        q_comm = comm_raw_score / initial_comm_raw_score if initial_comm_raw_score > 0 else 0.0
        q_mis = valid_chain_count / initial_valid_chain_count if initial_valid_chain_count > 0 else 0.0
        history["time"].append(current_time)
        history["Q_comm"].append(float(np.clip(q_comm, 0.0, 1.0)))
        history["Q_mis"].append(float(np.clip(q_mis, 0.0, 1.0)))
        history["mean_pair_distance"].append(calculate_mean_pair_distance(nodes))
        history["valid_path_count"].append(valid_chain_count)
        history["physical_complete"].append(is_physical_layer_complete(physical_layer))

    record_state(0)
    for current_time in range(1, config.TIME_STEPS + 1):
        if current_time > config.PART1_DISPERSION_START_TIME:
            apply_progressive_dispersion(config, nodes, directions)
        record_state(current_time)

    disconnect_time = next(
        (time_step for time_step, is_complete in zip(history["time"], history["physical_complete"]) if is_complete < 1),
        config.TIME_STEPS,
    )

    return {
        "history": history,
        "mu_comm": float(1.0 / initial_comm_raw_score) if initial_comm_raw_score and initial_comm_raw_score > 0 else 1.0,
        "physical_disconnect_time": disconnect_time,
    }


def plot_part1_eta_tau_coupling(
    config,
    summary_rows: List[Dict],
    physical_disconnect_time: float,
    output_path: Path,
) -> None:
    """图 1：上图展示通信层渐进衰退，下图展示任务层断崖式崩溃。"""
    lookup = build_lookup(summary_rows, ["eta", "tau_mis", "time"])
    time_axis = list(range(config.TIME_STEPS + 1))

    eta_colors = {
        config.PART1_ETA_VALUES[0]: "#1f77b4",
        config.PART1_ETA_VALUES[1]: "#ff7f0e",
        config.PART1_ETA_VALUES[2]: "#2ca02c",
    }
    eta_styles = {
        config.PART1_ETA_VALUES[0]: "-",
        config.PART1_ETA_VALUES[1]: "--",
        config.PART1_ETA_VALUES[2]: "-.",
    }
    tau_palette = ["#264653", "#2a9d8f", "#d62828"]
    tau_colors = {
        tau_value: tau_palette[index % len(tau_palette)]
        for index, tau_value in enumerate(config.PART1_TAU_VALUES)
    }

    fig, (ax_comm, ax_mis) = plt.subplots(
        2,
        1,
        figsize=config.FIGSIZE_PART1,
        sharex=True,
        gridspec_kw={"height_ratios": [1.0, 1.2]},
    )
    fig.suptitle(
        "Latent Degradation and Early Collapse Under Distance Attenuation and Mission-Threshold Coupling",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    representative_tau = config.PART1_TAU_VALUES[0]
    for eta_value in config.PART1_ETA_VALUES:
        values = [lookup[(eta_value, representative_tau, time_step)]["Q_comm_mean"] for time_step in time_axis]
        ax_comm.plot(
            time_axis,
            values,
            color=eta_colors[eta_value],
            linestyle=eta_styles[eta_value],
            linewidth=2.2,
            label=fr"$\eta={eta_value:.1f}$",
        )

    for eta_value in config.PART1_ETA_VALUES:
        for tau_value in config.PART1_TAU_VALUES:
            values = [lookup[(eta_value, tau_value, time_step)]["Q_mis_mean"] for time_step in time_axis]
            ax_mis.plot(
                time_axis,
                values,
                color=tau_colors[tau_value],
                linestyle=eta_styles[eta_value],
                linewidth=1.8,
                alpha=0.96,
            )

    reference_line_color = "#b2182b"
    for ax in (ax_comm, ax_mis):
        ax.axvline(
            x=physical_disconnect_time,
            color=reference_line_color,
            linestyle="--",
            linewidth=1.7,
            alpha=0.95,
        )
        ax.set_xlim(0, config.TIME_STEPS)
        ax.set_ylim(0.0, 1.05)
        ax.set_xticks(np.arange(0, config.TIME_STEPS + 1, config.TIME_AXIS_TICK_STEP))
        ax.grid(True, alpha=0.28)

    ax_comm.set_ylabel("Communication-Layer Performance $Q_{comm}(t)$")
    ax_comm.legend(
        frameon=False,
        loc="lower center",
        bbox_to_anchor=(0.5, 1.02),
        ncol=len(config.PART1_ETA_VALUES),
    )
    ax_comm.annotate(
        "Reference Time of First Physical-Layer Disconnection",
        xy=(physical_disconnect_time, 0.80),
        xytext=(physical_disconnect_time + 6.0, 0.96),
        color=reference_line_color,
        fontsize=9,
        ha="left",
        va="center",
        arrowprops={
            "arrowstyle": "->",
            "color": reference_line_color,
            "lw": 1.2,
            "shrinkA": 4,
            "shrinkB": 3,
        },
        bbox={
            "boxstyle": "round,pad=0.25",
            "facecolor": "white",
            "edgecolor": "none",
            "alpha": 0.78,
        },
    )

    ax_mis.set_xlabel("Time Step $t$")
    ax_mis.set_ylabel("Mission-Layer Performance $Q_{mis}(t)$")
    tau_handles = [
        Line2D([0], [0], color=tau_colors[tau_value], linewidth=2.2, label=fr"$\tau_{{mis}}={tau_value:.2f}$")
        for tau_value in config.PART1_TAU_VALUES
    ]
    eta_handles = [
        Line2D([0], [0], color="#444444", linestyle=eta_styles[eta_value], linewidth=2.2, label=fr"$\eta={eta_value:.1f}$")
        for eta_value in config.PART1_ETA_VALUES
    ]
    tau_legend = ax_mis.legend(
        handles=tau_handles,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.32, -0.18),
        ncol=len(config.PART1_TAU_VALUES),
    )
    ax_mis.add_artist(tau_legend)
    ax_mis.legend(
        handles=eta_handles,
        frameon=False,
        loc="upper center",
        bbox_to_anchor=(0.82, -0.18),
        ncol=len(config.PART1_ETA_VALUES),
    )

    plt.tight_layout(rect=(0.0, 0.06, 1.0, 0.93))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def run_part1(config, quick: bool) -> Tuple[List[Dict], List[Dict], List[Dict], float]:
    """执行第一部分：eta 与 tau_mis 耦合阈值分析。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    raw_rows: List[Dict] = []
    run_metadata_rows: List[Dict] = []
    total_runs = len(config.PART1_ETA_VALUES) * len(config.PART1_TAU_VALUES) * len(seeds)
    run_index = 0

    for eta_value in config.PART1_ETA_VALUES:
        for tau_value in config.PART1_TAU_VALUES:
            for seed in seeds:
                run_index += 1
                print(f"[part1 {run_index}/{total_runs}] eta={eta_value:.2f}, tau={tau_value:.2f}, seed={seed}")
                run_config = build_run_config(
                    config,
                    f"part1_eta_{eta_value:.2f}_tau_{tau_value:.2f}_seed_{seed}",
                    {
                        "ETA": eta_value,
                        "MISSION_PROB_THRESHOLD": tau_value,
                        "RANDOM_SEED": seed,
                    },
                )
                result = simulate_part1_hidden_degradation(run_config)
                history = result["history"]
                run_metadata_rows.append(
                    {
                        "eta": eta_value,
                        "tau_mis": tau_value,
                        "seed": seed,
                        "mu_comm": result["mu_comm"],
                        "physical_disconnect_time": result["physical_disconnect_time"],
                    }
                )

                for time_index, time_step in enumerate(history["time"]):
                    raw_rows.append(
                        {
                            "eta": eta_value,
                            "tau_mis": tau_value,
                            "seed": seed,
                            "time": time_step,
                            "Q_comm": history["Q_comm"][time_index],
                            "Q_mis": history["Q_mis"][time_index],
                            "mean_pair_distance": history["mean_pair_distance"][time_index],
                            "valid_path_count": history["valid_path_count"][time_index],
                            "physical_complete": history["physical_complete"][time_index],
                        }
                    )

    summary_rows = aggregate_part1_time_series(raw_rows, ["eta", "tau_mis"])
    reference_rows = [
        row
        for row in run_metadata_rows
        if row["eta"] == config.PART1_ETA_VALUES[0] and row["tau_mis"] == config.PART1_TAU_VALUES[0]
    ]
    reference_disconnect_time = float(np.mean([row["physical_disconnect_time"] for row in reference_rows]))
    return raw_rows, summary_rows, run_metadata_rows, reference_disconnect_time


def execute_part1(config, quick: bool) -> Dict[str, List[Dict] | float]:
    """执行并保存第一部分结果。"""
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows, summary_rows, run_metadata_rows, reference_disconnect_time = run_part1(config, quick=quick)

    save_csv(
        config.OUTPUT_DIR / "experiment3_part1_raw_timeseries.csv",
        raw_rows,
        [
            "eta",
            "tau_mis",
            "seed",
            "time",
            "Q_comm",
            "Q_mis",
            "mean_pair_distance",
            "valid_path_count",
            "physical_complete",
        ],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment3_part1_timeseries_summary.csv",
        summary_rows,
        [
            "eta",
            "tau_mis",
            "time",
            "num_runs",
            "Q_comm_mean",
            "Q_comm_std",
            "Q_mis_mean",
            "Q_mis_std",
            "mean_pair_distance_mean",
            "mean_pair_distance_std",
            "valid_path_count_mean",
            "valid_path_count_std",
            "physical_complete_mean",
            "physical_complete_std",
        ],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment3_part1_run_metadata.csv",
        run_metadata_rows,
        ["eta", "tau_mis", "seed", "mu_comm", "physical_disconnect_time"],
    )
    plot_part1_eta_tau_coupling(
        config,
        summary_rows,
        physical_disconnect_time=reference_disconnect_time,
        output_path=config.OUTPUT_DIR / "figure_1_eta_tau_coupling_matrix.png",
    )

    return {
        "raw_rows": raw_rows,
        "summary_rows": summary_rows,
        "run_metadata_rows": run_metadata_rows,
        "physical_disconnect_time": reference_disconnect_time,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验三第一部分：eta 与 tau_mis 耦合阈值分析")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment3Config
    config.validate()
    execute_part1(config, quick=args.quick)
    print(f"实验三第一部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
