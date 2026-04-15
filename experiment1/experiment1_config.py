"""
实验一配置：分阶段独立评估下的攻击机理与多层退化特性分析
"""

from pathlib import Path


class Experiment1Config:
    """实验一公共配置。单次运行时会在脚本中动态覆写部分参数。"""

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = PROJECT_ROOT / "result" / "experiment1"

    # 网络参数
    N_TOTAL = 100
    N_SENSOR = 50
    N_DECIDER = 30
    N_INFLUENCER = 20

    # 空间参数
    AREA_SIZE = 100.0
    R_COMM = 20.0
    R_SENSOR = 25.0

    # 通信参数
    ETA = 0.2
    USE_LOGIC_LOAD_CORRECTION = False

    # 任务阶段：默认会在运行脚本中按场景覆写
    TASK_PHASE_SCHEDULE = [
        (0, 101, 1),
    ]

    # 性能评估参数
    ALPHA = 0.4
    BETA = 0.3
    GAMMA = 0.3
    W1 = 1.0 / 3.0
    W2 = 1.0 / 3.0
    W3 = 1.0 / 3.0

    # 韧性相关参数：本实验以退化分析为主，但保留统一接口
    Q_MIN = 0.3
    LAMBDA = 0.05

    # 攻击参数：默认会在运行脚本中按场景和强度覆写
    ATTACK_TIME = 20
    ATTACK_DURATION = 3
    ATTACK_MODE = "physical"
    ATTACK_STRATEGY = "random"
    ATTACK_DEGREE_LAYER = "physical"
    ATTACK_RATIO = None
    ATTACK_NODES = 0
    ATTACK_ROLE_TARGET = "DECIDER"
    ATTACK_ROLE_CASCADE_ENABLED = True
    ATTACK_ROLE_CASCADE_SEQUENCE = ["TOPOLOGY"]
    ATTACK_RECOVER_TIME = 40

    # 任务层阈值
    MISSION_PROB_THRESHOLD = 0.01

    # 恢复参数：实验一关闭恢复，仅分析纯退化
    RECOVERY_SPEED = 0.0
    SEARCH_RADIUS = 50.0
    MIN_NODE_DISTANCE = None

    # 仿真参数
    TIME_STEPS = 100
    DT = 1.0
    SNAPSHOT_TIMES = []
    RANDOM_SEED = 11

    # 批量实验参数
    RANDOM_SEEDS = [11, 17, 23, 29, 35]
    QUICK_RANDOM_SEEDS = [11]
    ATTACK_INTENSITY_RATIOS = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    QUICK_ATTACK_INTENSITY_RATIOS = [0.0, 0.5, 1.0]

    STAGE_SCENARIOS = {
        "recon": {
            "label": "侦察阶段（固定 $\\Phi=1$）",
            "schedule": [(0, 101, 1)],
        },
        "strike": {
            "label": "打击阶段（固定 $\\Phi=2$）",
            "schedule": [(0, 101, 2)],
        },
    }

    # 默认纳入绘图的六类场景，覆盖硬/软杀伤与主要选靶机制
    ATTACK_SCENARIOS = [
        {
            "id": "hard_random",
            "label": "硬杀伤-随机攻击",
            "mode": "physical",
            "strategy": "random",
            "role_target": None,
            "color": "#1f77b4",
            "linestyle": "-",
            "marker": "o",
        },
        {
            "id": "hard_topology",
            "label": "硬杀伤-拓扑导向",
            "mode": "physical",
            "strategy": "topology",
            "role_target": None,
            "color": "#ff7f0e",
            "linestyle": "-",
            "marker": "s",
        },
        {
            "id": "hard_role_decider",
            "label": "硬杀伤-角色导向(D→拓扑)",
            "mode": "physical",
            "strategy": "role",
            "role_target": "DECIDER",
            "color": "#d62728",
            "linestyle": "-",
            "marker": "^",
        },
        {
            "id": "soft_random",
            "label": "网络压制-随机攻击",
            "mode": "cyber",
            "strategy": "random",
            "role_target": None,
            "color": "#2ca02c",
            "linestyle": "--",
            "marker": "o",
        },
        {
            "id": "soft_topology",
            "label": "网络压制-拓扑导向",
            "mode": "cyber",
            "strategy": "topology",
            "role_target": None,
            "color": "#9467bd",
            "linestyle": "--",
            "marker": "s",
        },
        {
            "id": "soft_role_decider",
            "label": "网络压制-角色导向(D→拓扑)",
            "mode": "cyber",
            "strategy": "role",
            "role_target": "DECIDER",
            "color": "#8c564b",
            "linestyle": "--",
            "marker": "^",
        },
    ]

    # 用于展示阶段非对称脆弱性的重点场景
    QMIS_STAGE_COMPARISON_SCENARIOS = [
        "hard_random",
        "hard_topology",
        "hard_role_decider",
    ]

    # 用于展示“物理层完好不等于任务层有效”的重点对比
    DECOUPLING_STAGE = "strike"
    DECOUPLING_SCENARIOS = ["hard_topology", "soft_topology"]

    # 绘图参数
    FIG_DPI = 300
    FIGSIZE_STAGE = (13, 9)
    FIGSIZE_COMPARISON = (15, 4.5)
    FIGSIZE_DECOUPLING = (12, 4.8)
    X_AXIS_MAX = 80.0

    @classmethod
    def get_snapshot_times(cls):
        return list(cls.SNAPSHOT_TIMES)

    @classmethod
    def get_min_node_distance(cls):
        if cls.MIN_NODE_DISTANCE is not None:
            return cls.MIN_NODE_DISTANCE
        return cls.R_COMM * 0.3

    @classmethod
    def validate(cls):
        assert cls.N_SENSOR + cls.N_DECIDER + cls.N_INFLUENCER == cls.N_TOTAL
        assert cls.N_SENSOR > cls.N_DECIDER > cls.N_INFLUENCER
        assert 0.0 <= cls.ETA <= 1.0
        assert abs((cls.ALPHA + cls.BETA + cls.GAMMA) - 1.0) < 1e-9
        assert abs((cls.W1 + cls.W2 + cls.W3) - 1.0) < 1e-9
        assert cls.ATTACK_MODE in ("physical", "cyber")
        assert cls.ATTACK_STRATEGY in ("random", "topology", "role", "high_degree", "critical")
        assert cls.ATTACK_DEGREE_LAYER in ("comm", "physical")
        assert cls.ATTACK_ROLE_TARGET in ("SENSOR", "DECIDER", "INFLUENCER")
        if cls.ATTACK_RATIO is not None:
            assert 0.0 <= cls.ATTACK_RATIO <= 1.0
        assert cls.ATTACK_DURATION >= 1
        assert cls.ATTACK_RECOVER_TIME >= cls.ATTACK_TIME
        assert isinstance(cls.TASK_PHASE_SCHEDULE, list) and cls.TASK_PHASE_SCHEDULE
        schedule = sorted(cls.TASK_PHASE_SCHEDULE, key=lambda item: item[0])
        expected_start = 0
        expected_end = cls.TIME_STEPS + 1
        for start, end, phase in schedule:
            assert start == expected_start
            assert start < end
            assert phase in (1, 2)
            expected_start = end
        assert expected_start == expected_end
