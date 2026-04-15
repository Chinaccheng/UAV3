"""
实验二基础部分入口：
仅运行六类攻击场景 × 四种恢复策略的基础矩阵扫描，并生成图 1、3-9。

运行方式：
    python experiment2/run_experiment2_base.py
    python experiment2/run_experiment2_base.py --quick
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

from experiment2_config import Experiment2Config
from run_experiment2 import generate_base_figures, run_suite, save_base_outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验二基础部分：基础场景矩阵与图 1、3-9")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment2Config
    config.validate()
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    raw_rows, time_summary_rows, resilience_summary_rows, snapshot_store = run_suite(config, quick=args.quick)
    save_base_outputs(config, raw_rows, time_summary_rows, resilience_summary_rows, quick=args.quick)
    generate_base_figures(config, time_summary_rows, resilience_summary_rows, snapshot_store)

    print(f"实验二基础部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
