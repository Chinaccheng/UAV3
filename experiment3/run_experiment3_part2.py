"""
实验三第二部分入口：
多维层级权重敏感度分析：软杀伤下的效能盲区与策略响应。

本实验通过三类网络压制策略与三类层级权重配置的交叉组合，比较不同评估视角下
系统综合性能 Q 的终态差异，用于展示物理主导型评估在软杀伤场景中的误判风险。

本实验生成：
    图2 figure_2_softkill_weight_sensitivity_grouped_bars.png
        三类软杀伤策略下，不同权重配置对应的终态综合性能分组柱状图

运行方式：
    python experiment3/run_experiment3_part2.py
    python experiment3/run_experiment3_part2.py --quick
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, List, Tuple

from experiment3_common import (
    aggregate_final_metrics,
    aggregate_time_series,
    build_lookup,
    build_run_config,
    simulate_run,
)

import matplotlib.pyplot as plt
import numpy as np

from experiment_common import save_csv
from experiment3_config import Experiment3Config


def plot_part2_grouped_bars(config, final_rows: List[Dict], output_path: Path) -> None:
    """图 2：三类软杀伤策略下不同评估权重的终态综合性能对比。"""
    lookup = build_lookup(final_rows, ["scenario_id", "profile_id"])
    scenarios = config.PART2_SCENARIOS
    profiles = config.PART2_WEIGHT_PROFILES

    fig, ax = plt.subplots(figsize=config.FIGSIZE_PART2_BARS)
    fig.suptitle(
        "Evaluation-Weight-Induced Blind Spots Under Electronic Soft-Kill Attacks",
        fontsize=15,
        fontweight="bold",
        y=0.98,
    )

    x = np.arange(len(scenarios), dtype=float)
    bar_width = 0.22
    offset_center = (len(profiles) - 1) / 2.0

    for scenario_index, scenario in enumerate(scenarios):
        if scenario.get("highlight"):
            ax.axvspan(
                scenario_index - 0.48,
                scenario_index + 0.48,
                color="#f6d5d5",
                alpha=0.26,
                ymin=0.0,
                ymax=0.86,
                zorder=0,
            )

    for profile_index, profile in enumerate(profiles):
        values = [lookup[(scenario["id"], profile["id"])]["Q_overall_mean"] for scenario in scenarios]
        errors = [lookup[(scenario["id"], profile["id"])]["Q_overall_std"] for scenario in scenarios]
        offset = (profile_index - offset_center) * bar_width
        bars = ax.bar(
            x + offset,
            values,
            width=bar_width,
            color=profile["color"],
            alpha=0.9,
            label=profile["label"],
            yerr=errors,
            error_kw={"elinewidth": 1.0, "ecolor": "#444444", "capsize": 3},
            zorder=3,
        )
        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width() / 2.0,
                min(1.03, value + 0.03),
                f"{value:.2f}",
                ha="center",
                va="bottom",
                fontsize=8.5,
                color="#333333",
            )

    ax.set_xticks(x)
    ax.set_xticklabels(
        [f"{scenario['label']}\n({int(round(scenario['attack_ratio'] * 100))}% suppressed)" for scenario in scenarios]
    )
    ax.set_xlabel("Network Suppression Strategy")
    ax.set_ylabel("Final Integrated Performance $Q$")
    ax.set_ylim(0.0, 1.08)
    ax.grid(True, axis="y", alpha=0.28, zorder=0)
    ax.legend(frameon=False, ncol=len(profiles), loc="upper center", bbox_to_anchor=(0.5, 1.02))

    role_index = next(
        index for index, scenario in enumerate(scenarios)
        if scenario["id"] == "cyber_role_decider"
    )
    ax.text(
        role_index + 0.02,
        0.985,
        "Role-oriented suppression:\nstrongest physical-overestimation / mission-underestimation gap",
        ha="center",
        va="center",
        fontsize=9.5,
        color="#8b1e1e",
        bbox={
            "boxstyle": "round,pad=0.25",
            "facecolor": "white",
            "edgecolor": "none",
            "alpha": 0.75,
        },
    )

    plt.tight_layout(rect=(0.0, 0.0, 1.0, 0.93))
    fig.savefig(output_path, dpi=config.FIG_DPI, bbox_inches="tight")
    plt.close(fig)


def run_part2(config, quick: bool) -> Tuple[List[Dict], List[Dict], List[Dict]]:
    """执行第二部分：软杀伤策略与评估权重的交叉敏感度分析。"""
    seeds = config.QUICK_RANDOM_SEEDS if quick else config.RANDOM_SEEDS
    raw_rows: List[Dict] = []
    total_runs = len(config.PART2_SCENARIOS) * len(config.PART2_WEIGHT_PROFILES) * len(seeds)
    run_index = 0

    for scenario in config.PART2_SCENARIOS:
        for profile in config.PART2_WEIGHT_PROFILES:
            w1, w2, w3 = profile["weights"]
            for seed in seeds:
                run_index += 1
                print(
                    f"[part2 {run_index}/{total_runs}] "
                    f"scenario={scenario['id']}, profile={profile['id']}, seed={seed}"
                )
                run_config = build_run_config(
                    config,
                    f"part2_{scenario['id']}_{profile['id']}_{seed}",
                    {
                        "W1": w1,
                        "W2": w2,
                        "W3": w3,
                        "ATTACK_MODE": scenario["mode"],
                        "ATTACK_STRATEGY": scenario["strategy"],
                        "ATTACK_RATIO": scenario["attack_ratio"],
                        "ATTACK_ROLE_TARGET": scenario.get("role_target") or config.ATTACK_ROLE_TARGET,
                        "ATTACK_ROLE_CASCADE_ENABLED": False,
                        "ATTACK_RECOVER_TIME": config.PART2_ATTACK_RECOVER_TIME,
                        "RANDOM_SEED": seed,
                    },
                )
                history = simulate_run(run_config, recovery_strategy_id=None)
                for time_index, time_step in enumerate(history["time"]):
                    raw_rows.append(
                        {
                            "scenario_id": scenario["id"],
                            "scenario_label": scenario["label"],
                            "strategy_label": scenario["strategy_label"],
                            "attack_ratio": scenario["attack_ratio"],
                            "profile_id": profile["id"],
                            "profile_label": profile["label"],
                            "w1": w1,
                            "w2": w2,
                            "w3": w3,
                            "seed": seed,
                            "time": time_step,
                            "Q_phy": history["Q_phy"][time_index],
                            "Q_comm": history["Q_comm"][time_index],
                            "Q_mis": history["Q_mis"][time_index],
                            "Q_overall": history["Q_overall"][time_index],
                            "alive_nodes": history["alive_nodes"][time_index],
                        }
                    )

    group_fields = [
        "scenario_id",
        "scenario_label",
        "strategy_label",
        "attack_ratio",
        "profile_id",
        "profile_label",
        "w1",
        "w2",
        "w3",
    ]
    summary_rows = aggregate_time_series(raw_rows, group_fields)
    final_rows = aggregate_final_metrics(
        [row for row in raw_rows if row["time"] == config.TIME_STEPS],
        group_fields,
    )
    return raw_rows, summary_rows, final_rows


def execute_part2(config, quick: bool) -> Dict[str, List[Dict]]:
    """执行并保存第二部分结果。"""
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows, summary_rows, final_rows = run_part2(config, quick=quick)

    raw_fields = [
        "scenario_id",
        "scenario_label",
        "strategy_label",
        "attack_ratio",
        "profile_id",
        "profile_label",
        "w1",
        "w2",
        "w3",
        "seed",
        "time",
        "Q_phy",
        "Q_comm",
        "Q_mis",
        "Q_overall",
        "alive_nodes",
    ]
    summary_fields = [
        "scenario_id",
        "scenario_label",
        "strategy_label",
        "attack_ratio",
        "profile_id",
        "profile_label",
        "w1",
        "w2",
        "w3",
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
    ]
    final_fields = [
        "scenario_id",
        "scenario_label",
        "strategy_label",
        "attack_ratio",
        "profile_id",
        "profile_label",
        "w1",
        "w2",
        "w3",
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
    ]

    save_csv(config.OUTPUT_DIR / "experiment3_part2_raw_timeseries.csv", raw_rows, raw_fields)
    save_csv(config.OUTPUT_DIR / "experiment3_part2_timeseries_summary.csv", summary_rows, summary_fields)
    save_csv(config.OUTPUT_DIR / "experiment3_part2_final_summary.csv", final_rows, final_fields)

    plot_part2_grouped_bars(
        config,
        final_rows,
        output_path=config.OUTPUT_DIR / "figure_2_softkill_weight_sensitivity_grouped_bars.png",
    )

    return {
        "raw_rows": raw_rows,
        "summary_rows": summary_rows,
        "final_rows": final_rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验三第二部分：软杀伤下的层级权重敏感度分析")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment3Config
    config.validate()
    execute_part2(config, quick=args.quick)
    print(f"实验三第二部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
