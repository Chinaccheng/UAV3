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

    # 攻击强度：默认上调至 25%，使性能跌落更显著，同时保留少量 D 节点作为重构空间
    ATTACK_TIME = 20
    ATTACK_DURATION = 4
    ATTACK_RATIO = 0.25
    ATTACK_NODES = 25
    ATTACK_DEGREE_LAYER = "physical"
    ATTACK_ROLE_TARGET = "DECIDER"
    ATTACK_ROLE_CASCADE_ENABLED = True
    ATTACK_ROLE_CASCADE_SEQUENCE = ["TOPOLOGY"]
    ATTACK_RECOVER_TIME = TIME_STEPS

    # 任务层阈值
    MISSION_PROB_THRESHOLD = 0.01

    # 重构参数
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
    ATTACK_INTENSITY_RATIOS = [0.10, 0.20, 0.30, 0.40, 0.50]
    QUICK_ATTACK_INTENSITY_RATIOS = [0.10, 0.30, 0.50]

    # 六类攻击场景：破坏模式 × 目标选择策略
    ATTACK_SCENARIOS = [
        {
            "id": "physical_random",
            "label": "物理摧毁-随机攻击",
            "mode_label": "物理摧毁",
            "targeting_label": "随机攻击",
            "mode": "physical",
            "strategy": "random",
            "role_target": None,
        },
        {
            "id": "physical_topology",
            "label": "物理摧毁-拓扑蓄意攻击",
            "mode_label": "物理摧毁",
            "targeting_label": "拓扑蓄意攻击",
            "mode": "physical",
            "strategy": "topology",
            "role_target": None,
        },
        {
            "id": "physical_role_decider",
            "label": "物理摧毁-角色蓄意攻击(D)",
            "mode_label": "物理摧毁",
            "targeting_label": "角色蓄意攻击",
            "mode": "physical",
            "strategy": "role",
            "role_target": "DECIDER",
        },
        {
            "id": "cyber_random",
            "label": "网络压制-随机攻击",
            "mode_label": "网络压制",
            "targeting_label": "随机攻击",
            "mode": "cyber",
            "strategy": "random",
            "role_target": None,
        },
        {
            "id": "cyber_topology",
            "label": "网络压制-拓扑蓄意攻击",
            "mode_label": "网络压制",
            "targeting_label": "拓扑蓄意攻击",
            "mode": "cyber",
            "strategy": "topology",
            "role_target": None,
        },
        {
            "id": "cyber_role_decider",
            "label": "网络压制-角色蓄意攻击(D)",
            "mode_label": "网络压制",
            "targeting_label": "角色蓄意攻击",
            "mode": "cyber",
            "strategy": "role",
            "role_target": "DECIDER",
        },
    ]

    RECOVERY_STRATEGIES = [
        {
            "id": "no_reconfiguration",
            "label": "静态无重构",
            "color": "#4d4d4d",
            "linestyle": "-",
            "marker": "o",
        },
        {
            "id": "distance_driven",
            "label": "最短距离重构",
            "color": "#1f77b4",
            "linestyle": "--",
            "marker": "s",
        },
        {
            "id": "degree_driven",
            "label": "最高度数重构",
            "color": "#ff7f0e",
            "linestyle": "-.",
            "marker": "^",
        },
        {
            "id": "utility_role_driven",
            "label": "效用与角色重构",
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
    FIGSIZE_SNAPSHOTS = (16, 5.4)
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
