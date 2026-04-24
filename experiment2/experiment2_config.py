"""
实验二配置：多场景自适应重构策略效果与韧性评估
"""

from pathlib import Path


class Experiment2Config:
    """实验二公共配置。"""

    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    OUTPUT_DIR = PROJECT_ROOT / "result" / "experiment2"

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
    # 实验二沿用论文当前设定，不启用额外通信负载惩罚
    USE_LOGIC_LOAD_CORRECTION = False

    # 任务阶段：固定于打击阶段，突出授权与协同恢复
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

    # 攻击强度：在 t=20 前采用更离散的不均匀打击批次，形成更明显的阶段性跌落
    ATTACK_TIME = 20
    ATTACK_DURATION = 10
    ATTACK_BATCH_WEIGHTS = [0, 2, 0, 4, 1, 0, 6, 3, 0, 9]
    ATTACK_RATIO = 0.25
    ATTACK_NODES = 25
    ATTACK_DEGREE_LAYER = "physical"
    ATTACK_ROLE_TARGET = "DECIDER"
    ATTACK_ROLE_CASCADE_ENABLED = True
    ATTACK_ROLE_CASCADE_SEQUENCE = ["TOPOLOGY"]
    ATTACK_RECOVER_TIME = TIME_STEPS

    # 任务层阈值
    MISSION_PROB_THRESHOLD = 0.01

    # 重构参数：前段先短暂停滞，再多次间歇式恢复，后段回到正常速度
    RECOVERY_SPEED = 1.25
    RECOVERY_SPEED_PROFILE = [
        (21, 24, 0.0),
        (24, 28, 0.38),
        (28, 30, 0.0),
        (30, 35, 0.55),
        (35, 37, 0.0),
        (37, 43, 0.78),
        (43, 45, 0.0),
        (45, TIME_STEPS + 1, 1.0),
    ]
    SEARCH_RADIUS = 40.0
    MIN_NODE_DISTANCE = None
    RECONFIGURE_TRIGGER_TIME = ATTACK_TIME
    BASELINE_TRIGGER_PHYSICAL_DEGREE = 2
    UTILITY_MIN_ACCEPTANCE = 0.10

    # 随机种子
    RANDOM_SEED = 11
    RANDOM_SEEDS = [11, 17, 23, 29, 35]
    QUICK_RANDOM_SEEDS = [11]
    ATTACK_INTENSITY_RATIOS = [0.10, 0.20, 0.30, 0.40, 0.50]
    QUICK_ATTACK_INTENSITY_RATIOS = [0.10, 0.30, 0.50]

    # 六类攻击场景：破坏模式 × 目标选择策略
    ATTACK_SCENARIOS = [
        {
            "id": "physical_random",
            "label": "Physical Destruction-Random Attack",
            "mode_label": "Physical Destruction",
            "targeting_label": "Random Attack",
            "mode": "physical",
            "strategy": "random",
            "role_target": None,
        },
        {
            "id": "physical_topology",
            "label": "Physical Destruction-Topology-Oriented Deliberate Attack",
            "mode_label": "Physical Destruction",
            "targeting_label": "Topology-Oriented Deliberate Attack",
            "mode": "physical",
            "strategy": "topology",
            "role_target": None,
        },
        {
            "id": "physical_role_decider",
            "label": "Physical Destruction-Role-Oriented Targeted Attack (D)",
            "mode_label": "Physical Destruction",
            "targeting_label": "Role-Oriented Targeted Attack",
            "mode": "physical",
            "strategy": "role",
            "role_target": "DECIDER",
        },
        {
            "id": "cyber_random",
            "label": "Network Suppression-Random Attack",
            "mode_label": "Network Suppression",
            "targeting_label": "Random Attack",
            "mode": "cyber",
            "strategy": "random",
            "role_target": None,
        },
        {
            "id": "cyber_topology",
            "label": "Network Suppression-Topology-Oriented Deliberate Attack",
            "mode_label": "Network Suppression",
            "targeting_label": "Topology-Oriented Deliberate Attack",
            "mode": "cyber",
            "strategy": "topology",
            "role_target": None,
        },
        {
            "id": "cyber_role_decider",
            "label": "Network Suppression-Role-Oriented Targeted Attack (D)",
            "mode_label": "Network Suppression",
            "targeting_label": "Role-Oriented Targeted Attack",
            "mode": "cyber",
            "strategy": "role",
            "role_target": "DECIDER",
        },
    ]

    RECOVERY_STRATEGIES = [
        {
            "id": "no_reconfiguration",
            "label": "Static Baseline",
            "color": "#4d4d4d",
            "linestyle": "-",
            "marker": "o",
        },
        {
            "id": "distance_driven",
            "label": "Nearest-Neighbor Reconfiguration",
            "color": "#1f77b4",
            "linestyle": "--",
            "marker": "s",
        },
        {
            "id": "degree_driven",
            "label": "Maximum-Degree Reconfiguration",
            "color": "#ff7f0e",
            "linestyle": "-.",
            "marker": "^",
        },
        {
            "id": "utility_role_mismatch_recon",
            "label": "Phase-Mismatched Utility Reconfiguration",
            "color": "#2ca02c",
            "linestyle": ":",
            "marker": "P",
        },
        {
            "id": "utility_role_driven",
            "label": "Utility-Guided and Role-Driven Reconfiguration",
            "color": "#d62728",
            "linestyle": "-",
            "marker": "D",
        },
    ]

    DYNAMIC_SCENARIO_GRID = [
        ["physical_random", "physical_topology", "physical_role_decider"],
        ["cyber_random", "cyber_topology", "cyber_role_decider"],
    ]
    DECOUPLING_SCENARIO = "cyber_role_decider"
    ATTACK_INTENSITY_FOCUS_SCENARIO = "cyber_role_decider"
    SNAPSHOT_SCENARIO = "physical_role_decider"
    SNAPSHOT_SEED = 11
    SNAPSHOT_COMPARE_TIME = 60

    # 绘图参数
    FIG_DPI = 300
    FIGSIZE_DYNAMIC = (16, 8.8)
    FIGSIZE_DECOUPLING = (13, 5.2)
    FIGSIZE_RESILIENCE = (13, 4.8)
    FIGSIZE_SNAPSHOTS = (16.2, 8.6)
    FIGSIZE_LAYER_DYNAMIC = (16, 8.8)
    FIGSIZE_LAYER_FINAL = (16, 5.6)
    FIGSIZE_RESILIENCE_BARS = (14.5, 5.8)
    FIGSIZE_ATTACK_INTENSITY = (16, 8.8)
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
        if getattr(cls, "ATTACK_BATCH_WEIGHTS", None) is not None:
            assert len(cls.ATTACK_BATCH_WEIGHTS) == cls.ATTACK_DURATION
            assert sum(max(0.0, float(weight)) for weight in cls.ATTACK_BATCH_WEIGHTS) > 0.0
        if getattr(cls, "RECOVERY_SPEED_PROFILE", None):
            for start, end, multiplier in cls.RECOVERY_SPEED_PROFILE:
                assert cls.RECONFIGURE_TRIGGER_TIME < end
                assert start < end
                assert multiplier >= 0.0
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
        assert cls.ATTACK_SCENARIOS
        assert cls.RECOVERY_STRATEGIES
        assert cls.ATTACK_INTENSITY_RATIOS
        assert cls.QUICK_ATTACK_INTENSITY_RATIOS
        for ratio in cls.ATTACK_INTENSITY_RATIOS + cls.QUICK_ATTACK_INTENSITY_RATIOS:
            assert 0.0 < ratio <= 1.0
        assert 0 <= cls.SNAPSHOT_COMPARE_TIME <= cls.TIME_STEPS
