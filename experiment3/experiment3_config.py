"""
实验三配置：多层退化特性分析与极限约束下的重构效能评估
"""

from pathlib import Path


class Experiment3Config:
    """实验三公共配置。"""

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = PROJECT_ROOT / "result" / "experiment3"

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

    # 任务阶段：固定在打击阶段，突出任务链约束
    TIME_STEPS = 100
    DT = 1.0
    TASK_PHASE_SCHEDULE = [
        (0, TIME_STEPS + 1, 2),
    ]

    # 性能评估参数
    ALPHA = 0.4
    BETA = 0.3
    GAMMA = 0.3
    W1 = 0.05
    W2 = 0.45
    W3 = 0.5

    # 韧性参数
    Q_MIN = 0.45
    LAMBDA = 0.05

    # 攻击参数
    ATTACK_TIME = 20
    ATTACK_DURATION = 4
    ATTACK_MODE = "physical"
    ATTACK_STRATEGY = "random"
    ATTACK_DEGREE_LAYER = "physical"
    ATTACK_RATIO = 0.25
    ATTACK_NODES = 25
    ATTACK_ROLE_TARGET = "DECIDER"
    ATTACK_ROLE_CASCADE_ENABLED = True
    ATTACK_ROLE_CASCADE_SEQUENCE = ["TOPOLOGY"]
    ATTACK_RECOVER_TIME = TIME_STEPS

    # 任务层阈值
    MISSION_PROB_THRESHOLD = 0.01

    # 恢复参数
    RECOVERY_SPEED = 1.6
    SEARCH_RADIUS = 40.0
    MIN_NODE_DISTANCE = None
    RECONFIGURE_TRIGGER_TIME = ATTACK_TIME
    BASELINE_TRIGGER_PHYSICAL_DEGREE = 2
    UTILITY_MIN_ACCEPTANCE = 0.10

    # 随机种子
    RANDOM_SEED = 11
    RANDOM_SEEDS = [11, 17, 23, 29, 35]
    QUICK_RANDOM_SEEDS = [11]

    # 第一部分：eta 与 tau_mis 耦合阈值分析
    PART1_SCENARIO = {
        "id": "progressive_dispersion_hidden_degradation",
        "label": "触发后渐进离散场景",
        "mode": "progressive_dispersion",
        "strategy": "triggered_drift",
        "role_target": None,
    }
    PART1_ETA_VALUES = [0.2, 0.5, 0.8]
    PART1_TAU_VALUES = [0.05, 0.15, 0.25]
    PART1_INITIAL_CLUSTER_RADIUS = 1.5
    PART1_DISPERSION_SPEED = 0.17
    PART1_DISPERSION_START_TIME = ATTACK_TIME

    # 第二部分：多维层级权重敏感度分析
    PART2_ATTACK_RECOVER_TIME = TIME_STEPS
    PART2_SCENARIOS = [
        {
            "id": "cyber_random",
            "label": "随机压制",
            "strategy_label": "Random",
            "attack_ratio": 0.40,
            "mode": "cyber",
            "strategy": "random",
            "role_target": None,
            "highlight": False,
        },
        {
            "id": "cyber_topology",
            "label": "拓扑导向压制",
            "strategy_label": "Topology-oriented",
            "attack_ratio": 0.40,
            "mode": "cyber",
            "strategy": "topology",
            "role_target": None,
            "highlight": False,
        },
        {
            "id": "cyber_role_decider",
            "label": "角色导向压制",
            "strategy_label": "Role-oriented",
            "attack_ratio": 0.25,
            "mode": "cyber",
            "strategy": "role",
            "role_target": "DECIDER",
            "highlight": True,
        },
    ]
    PART2_WEIGHT_PROFILES = [
        {
            "id": "physical_dominant",
            "label": "物理主导型",
            "weights": (0.8, 0.1, 0.1),
            "color": "#1f77b4",
            "linestyle": "-",
            "marker": "o",
        },
        {
            "id": "communication_dominant",
            "label": "通信主导型",
            "weights": (0.1, 0.8, 0.1),
            "color": "#2ca02c",
            "linestyle": "--",
            "marker": "s",
        },
        {
            "id": "mission_dominant",
            "label": "任务主导型",
            "weights": (0.1, 0.1, 0.8),
            "color": "#d62728",
            "linestyle": "-.",
            "marker": "^",
        },
    ]

    # 第三部分：极限任务约束与重构边界测试
    PART3_ATTACK_RATIO = 0.30
    PART3_SCENARIO = {
        "id": "physical_random",
        "label": "随机物理节点摧毁",
        "mode": "physical",
        "strategy": "random",
        "role_target": None,
    }
    PART3_RECOVERY_STRATEGIES = [
        {
            "id": "distance_driven",
            "label": "最临近重构",
            "color": "#1f77b4",
            "linestyle": "--",
            "marker": "s",
        },
        {
            "id": "degree_driven",
            "label": "最大度重构",
            "color": "#ff7f0e",
            "linestyle": "-.",
            "marker": "^",
        },
        {
            "id": "utility_role_driven",
            "label": "效用驱动重构",
            "color": "#d62728",
            "linestyle": "-",
            "marker": "D",
        },
    ]
    PART3_QMIN_VALUES = [0.30, 0.40, 0.50, 0.60, 0.70]
    PART3_LAMBDA_VALUES = [0.01, 0.03, 0.05, 0.07, 0.10]

    # 绘图参数
    FIG_DPI = 300
    FIGSIZE_PART1 = (11.0, 7.8)
    FIGSIZE_PART2_TIMESERIES = (10.5, 5.4)
    FIGSIZE_PART2_BARS = (11.5, 5.4)
    FIGSIZE_PART3_TRAJECTORY = (10.5, 5.4)
    FIGSIZE_PART3_HEATMAP = (13.5, 5.2)
    TIME_AXIS_TICK_STEP = 10

    @classmethod
    def get_snapshot_times(cls):
        return []

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
        assert 0.0 <= cls.ATTACK_RATIO <= 1.0
        assert cls.ATTACK_DURATION >= 1
        assert cls.ATTACK_RECOVER_TIME >= cls.ATTACK_TIME
        assert cls.RECOVERY_SPEED >= 0.0
        assert cls.SEARCH_RADIUS > 0.0
        assert cls.BASELINE_TRIGGER_PHYSICAL_DEGREE >= 0
        assert cls.UTILITY_MIN_ACCEPTANCE >= 0.0
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
        assert cls.PART1_ETA_VALUES and cls.PART1_TAU_VALUES
        assert cls.PART1_INITIAL_CLUSTER_RADIUS > 0.0
        assert cls.PART1_DISPERSION_SPEED > 0.0
        assert cls.PART1_DISPERSION_START_TIME >= 0
        assert 2.0 * cls.PART1_INITIAL_CLUSTER_RADIUS <= min(cls.PART1_ETA_VALUES) * cls.R_COMM
        assert cls.PART2_SCENARIOS
        assert cls.PART2_WEIGHT_PROFILES
        assert cls.PART3_RECOVERY_STRATEGIES
        assert cls.PART3_QMIN_VALUES and cls.PART3_LAMBDA_VALUES
