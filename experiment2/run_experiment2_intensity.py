"""
实验二强度边界入口：
仅运行攻击强度扫描并保存结果表。

运行方式：
    python experiment2/run_experiment2_intensity.py
    python experiment2/run_experiment2_intensity.py --quick
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
from run_experiment2 import run_attack_intensity_suite, save_intensity_outputs


def main() -> None:
    parser = argparse.ArgumentParser(description="运行实验二强度边界部分：攻击强度扫描与结果导出")
    parser.add_argument("--quick", action="store_true", help="快速模式，仅使用一个随机种子进行冒烟测试")
    args = parser.parse_args()

    config = Experiment2Config
    config.validate()
    config.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    intensity_raw_rows, intensity_summary_rows, attack_ratios = run_attack_intensity_suite(
        config,
        quick=args.quick,
        scenario_ids=[config.ATTACK_INTENSITY_FOCUS_SCENARIO],
    )
    save_intensity_outputs(config, intensity_raw_rows, intensity_summary_rows)

    print(f"实验二攻击强度部分完成，结果保存在: {config.OUTPUT_DIR}")


if __name__ == "__main__":
    main()
