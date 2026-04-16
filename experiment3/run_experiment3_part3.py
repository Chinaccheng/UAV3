"""
实验三第三部分入口：
极限任务约束与自适应重构效能边界测试。

本实验以随机物理节点摧毁为起点，对比最临近重构、最大度重构与效用驱动重构
三类策略在不同任务底线 Q_min 和时间敏感性 lambda 下的韧性表现，
并重点展示效用驱动策略相对传统策略的韧性增益边界。

本实验生成：
    图3 figure_3_constraint_delta_heatmaps.png
        左图为相对最临近重构的韧性增益 ΔR_1，右图为相对最大度重构的韧性增益 ΔR_2

运行方式：
    python experiment3/run_experiment3_part3.py
    python experiment3/run_experiment3_part3.py --quick
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from experiment3_common import aggregate_time_series, build_lookup, build_run_config, simulate_run

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import TwoSlopeNorm

from experiment_common import calculate_resilience, save_csv
from experiment3_config import Experiment3Config


def compute_part3_delta_rows(
    config,
    resilience_rows: List[Dict],
) -> List[Dict]:
    """基于同种子配对结果计算效用策略相对传统策略的韧性增益。"""
    lookup = build_lookup(resilience_rows, ["strategy_id", "seed", "q_min", "lambda"])
    delta_specs = [
        ("distance_driven", "delta_vs_nearest", "相对最临近重构的韧性增益 $\\Delta R_1$"),
        ("degree_driven", "delta_vs_degree", "相对最大度重构的韧性增益 $\\Delta R_2$"),
    ]

    delta_rows: List[Dict] = []
    seeds = sorted({int(row["seed"]) for row in resilience_rows})
    for baseline_id, delta_id, delta_label in delta_specs:
        for q_min in config.PART3_QMIN_VALUES:
            for lambda_value in config.PART3_LAMBDA_VALUES:
                deltas = []
                for seed in seeds:
                    utility_row = lookup.get(("utility_role_driven", seed, q_min, lambda_value))
                    baseline_row = lookup.get((baseline_id, seed, q_min, lambda_value))
                    if utility_row is None or baseline_row is None:
                        continue
                    deltas.append(utility_row["resilience"] - baseline_row["resilience"])

                if not deltas:
                    continue

                delta_rows.append(
                    {
                        "delta_id": delta_id,
                        "delta_label": delta_label,
                        "baseline_id": baseline_id,
                        "q_min": q_min,
                        "lambda": lambda_value,
                        "num_runs": len(deltas),
                        "delta_resilience_mean": float(np.mean(deltas)),
                        "delta_resilience_std": float(np.std(deltas)),
                    }
                )
    return delta_rows


def plot_part3_constraint_heatmaps(config, delta_rows: List[Dict], output_path: Path) -> None:
    """图 3：效用驱动重构相对传统策略的双热力图。"""
    lookup = build_lookup(delta_rows, ["delta_id", "q_min", "lambda"])
    q_values = config.PART3_QMIN_VALUES
    lambda_values = config.PART3_LAMBDA_VALUES

    delta_specs = [
        ("delta_vs_nearest", "相对最临近重构的韧性增益 $\\Delta R_1$"),
        ("delta_vs_degree", "相对最大度重构的韧性增益 $\\Delta R_2$"),
    ]

    matrices = []
    for delta_id, _ in delta_specs:
        matrix = np.zeros((len(lambda_values), len(q_values)))
        for row_index, lambda_value in enumerate(lambda_values):
            for col_index, q_min in enumerate(q_values):
                matrix[row_index, col_index] = lookup[(delta_id, q_min, lambda_value)]["delta_resilience_mean"]
        matrices.append(matrix)

    max_abs = max(float(np.max(np.abs(matrix))) for matrix in matrices)
    max_abs = max(max_abs, 1e-6)
    norm = TwoSlopeNorm(vmin=-max_abs, vcenter=0.0, vmax=max_abs)

    fig, axes = plt.subplots(1, 2, figsize=config.FIGSIZE_PART3_HEATMAP, sharey=True)
    fig.suptitle(
        "极限任务约束下效用驱动重构的相对韧性增益边界",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    for ax, matrix, (_, subplot_title) in zip(axes, matrices, delta_specs):
        image = ax.imshow(matrix, cmap="RdYlGn", norm=norm, aspect="auto")
        for row_index in range(matrix.shape[0]):
            for col_index in range(matrix.shape[1]):
                ax.text(
                    col_index,
                    row_index,
                    f"{matrix[row_index, col_index]:.3f}",
                    ha="center",
                    va="center",
                    fontsize=8.5,
                    color="#222222",
                )

        ax.set_title(subplot_title, fontsize=11)
        ax.set_xticks(np.arange(len(q_values)))
        ax.set_xticklabels([f"{value:.2f}" for value in q_values])
        ax.set_yticks(np.arange(len(lambda_values)))
        ax.set_yticklabels([f"{value:.2f}" for value in lambda_values])
        ax.set_xlabel("$Q_{min}$")
        ax.set_ylabel("$\\lambda$")

    fig.subplots_adjust(left=0.07, right=0.84, bottom=0.12, top=0.80, wspace=0.12)
    cbar_ax = fig.add_axes([0.87, 0.14, 0.018, 0.68])
    colorbar = fig.colorbar(image, cax=cbar_ax)
    colorbar.set_label("相对韧性增益 $\\Delta R$")
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def run_part3(config, quick: bool) -> Tuple[List[Dict], List[Dict], List[Dict], List[Dict]]:
    """执行第三部分：随机物理摧毁下的恢复边界测试。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    trajectory_rows: List[Dict] = []
    resilience_rows: List[Dict] = []
    total_runs = len(config.PART3_RECOVERY_STRATEGIES) * len(seeds)
    run_index = 0

    for strategy in config.PART3_RECOVERY_STRATEGIES:
        strategy_histories: Dict[int, Dict] = {}
        for seed in seeds:
            run_index += 1
            print(f"[part3 {run_index}/{total_runs}] strategy={strategy['id']}, seed={seed}")
            run_config = build_run_config(
                config,
                f"part3_{strategy['id']}_{seed}",
                {
                    "ATTACK_MODE": config.PART3_SCENARIO["mode"],
                    "ATTACK_STRATEGY": config.PART3_SCENARIO["strategy"],
                    "ATTACK_RATIO": config.PART3_ATTACK_RATIO,
                    "ATTACK_ROLE_TARGET": config.PART3_SCENARIO.get("role_target") or config.ATTACK_ROLE_TARGET,
                    "ATTACK_RECOVER_TIME": config.TIME_STEPS,
                    "RANDOM_SEED": seed,
                },
            )
            history = simulate_run(run_config, recovery_strategy_id=strategy["id"])
            strategy_histories[seed] = history
            for time_index, time_step in enumerate(history["time"]):
                trajectory_rows.append(
                    {
                        "strategy_id": strategy["id"],
                        "strategy_label": strategy["label"],
                        "seed": seed,
                        "time": time_step,
                        "Q_phy": history["Q_phy"][time_index],
                        "Q_comm": history["Q_comm"][time_index],
                        "Q_mis": history["Q_mis"][time_index],
                        "Q_overall": history["Q_overall"][time_index],
                        "alive_nodes": history["alive_nodes"][time_index],
                    }
                )

        for q_min in config.PART3_QMIN_VALUES:
            for lambda_value in config.PART3_LAMBDA_VALUES:
                for seed, history in strategy_histories.items():
                    resilience_rows.append(
                        {
                            "strategy_id": strategy["id"],
                            "strategy_label": strategy["label"],
                            "seed": seed,
                            "q_min": q_min,
                            "lambda": lambda_value,
                            "resilience": calculate_resilience(
                                history,
                                trigger_time=config.ATTACK_TIME,
                                q_min=q_min,
                                lambda_=lambda_value,
                            ),
                        }
                    )

    trajectory_summary_rows = aggregate_time_series(trajectory_rows, ["strategy_id", "strategy_label"])
    delta_rows = compute_part3_delta_rows(config, resilience_rows)
    return trajectory_rows, trajectory_summary_rows, resilience_rows, delta_rows


def execute_part3(config, quick: bool) -> Dict[str, List[Dict]]:
    """执行并保存第三部分结果。"""
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    trajectory_rows, trajectory_summary_rows, resilience_rows, delta_rows = run_part3(config, quick=quick)

    save_csv(
        config.OUTPUT_DIR / "experiment3_part3_trajectory_raw.csv",
        trajectory_rows,
        ["strategy_id", "strategy_label", "seed", "time", "Q_phy", "Q_comm", "Q_mis", "Q_overall", "alive_nodes"],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment3_part3_trajectory_summary.csv",
        trajectory_summary_rows,
        [
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
        ],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment3_part3_resilience_surface.csv",
        resilience_rows,
        ["strategy_id", "strategy_label", "seed", "q_min", "lambda", "resilience"],
    )
    save_csv(
        config.OUTPUT_DIR / "experiment3_part3_delta_surface.csv",
        delta_rows,
        ["delta_id", "delta_label", "baseline_id", "q_min", "lambda", "num_runs", "delta_resilience_mean", "delta_resilience_std"],
    )
    plot_part3_constraint_heatmaps(
        config,
        delta_rows,
        output_path=config.OUTPUT_DIR / "figure_3_constraint_delta_heatmaps.png",
    )

    return {
        "trajectory_rows": trajectory_rows,
        "trajectory_summary_rows": trajectory_summary_rows,
        "resilience_rows": resilience_rows,
        "delta_rows": delta_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验三第三部分：极限任务约束与自适应重构效能边界测试")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment3Config
    config.validate()
    execute_part3(config, quick=args.quick)
    print(f"实验三第三部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
