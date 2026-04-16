"""
实验三总入口：
统一调度实验三的三个部分，可按部分单独运行，也可一次性全量运行。

本入口可运行：
    part1
        eta 与 tau_mis 耦合阈值分析
        生成 figure_1_eta_tau_coupling_matrix.png
    part2
        软杀伤下的层级权重敏感度分析
        生成 figure_2_softkill_weight_sensitivity_grouped_bars.png
    part3
        极限任务约束下的重构韧性增益边界测试
        生成 figure_3_constraint_delta_heatmaps.png
    all
        依次运行 part1、part2、part3

运行方式：
    python experiment3/run_experiment3.py
    python experiment3/run_experiment3.py --quick
    python experiment3/run_experiment3.py --part 1
    python experiment3/run_experiment3.py --part 2
    python experiment3/run_experiment3.py --part 3
    python experiment3/run_experiment3.py --part all
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
MPLCONFIG_DIR = CURRENT_DIR / ".mplconfig"
MPLCONFIG_DIR.mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(MPLCONFIG_DIR))

PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from experiment3_config import Experiment3Config
from run_experiment3_part1 import execute_part1
from run_experiment3_part2 import execute_part2
from run_experiment3_part3 import execute_part3


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验三总入口：支持单独运行各部分或一次性全量运行")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    parser.add_argument(
        "--part",
        choices=["1", "2", "3", "all"],
        default="all",
        help="选择运行实验三的某一部分，默认 all",
    )
    args = parser.parse_args()

    config = Experiment3Config
    config.validate()
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if args.part in ("1", "all"):
        execute_part1(config, quick=args.quick)
        print(f"实验三第一部分完成，结果保存在: {config.OUTPUT_DIR}")

    if args.part in ("2", "all"):
        execute_part2(config, quick=args.quick)
        print(f"实验三第二部分完成，结果保存在: {config.OUTPUT_DIR}")

    if args.part in ("3", "all"):
        execute_part3(config, quick=args.quick)
        print(f"实验三第三部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
