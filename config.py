"""
配置文件：定义实验参数
"""

class Config:
    """实验配置参数"""
    
    # 网络参数
    N_TOTAL = 100  # 总节点数
    N_SENSOR = 50  # 侦察节点数 (V_S)
    N_DECIDER = 30  # 通信节点数 (V_D)
    N_INFLUENCER = 20  # 打击节点数 (V_I)
    
    # 空间参数
    AREA_SIZE = 100.0  # 区域大小（正方形区域边长）
    R_COMM = 20.0  # 通信半径
    R_SENSOR = 25.0  # 感知半径（用于恢复策略）
    
    # 通信概率参数
    ETA = 0.2  # 距离影响因子（强信号区比例）
    USE_LOGIC_LOAD_CORRECTION = False  # 是否启用逻辑层负载修正项 eta_load
    
    # 任务阶段参数
    # 采用“时间区间 -> 阶段”配置，便于实验时灵活调整
    # 格式: (start_inclusive, end_exclusive, phase)
    # phase: 1=侦察阶段, 2=打击阶段
    # TASK_PHASE_SCHEDULE = [
    #     (0, 50, 1),
    #     (50, 101, 2),
    # ]
    TASK_PHASE_SCHEDULE = [
        (0, 101, 1)
    ]
    
    # 性能评估参数
    ALPHA = 0.4  # 平均度权重
    BETA = 0.3   # 聚类系数权重
    GAMMA = 0.3  # 全局效率权重
    
    # 综合性能权重参数
    W1 = 1.0 / 3.0  # 物理层性能权重
    W2 = 1.0 / 3.0  # 通信层性能权重
    W3 = 1.0 / 3.0  # 任务层性能权重

    # 韧性评估参数
    Q_MIN = 0.3  # 最小性能阈值
    LAMBDA = 0.05  # 时间敏感系数
    
    # 攻击参数
    ATTACK_TIME = 20  # 攻击发生时刻 t_d

    # 攻击方式（打击手段）
    # 'physical': 物理实体打击（硬杀伤，节点永久移除）
    # 'cyber': 网络压制攻击（软杀伤，仅通信压制）
    ATTACK_MODE = 'physical'

    # 目标选择策略
    # 'random': 随机打击
    # 'topology': 拓扑蓄意打击（按度数降序优先）
    # 'role': 角色导向打击（按节点类型优先）
    ATTACK_STRATEGY = 'topology'

    # 攻击规模（二选一，优先使用 ATTACK_RATIO）
    ATTACK_RATIO = None   # 从当前存活节点中按比例打击
    ATTACK_NODES = 40    # 当 ATTACK_RATIO=None 时生效

    # 角色导向策略参数
    ATTACK_ROLE_TARGET = 'DECIDER'  # 'SENSOR' | 'DECIDER' | 'INFLUENCER'

    # 网络压制恢复时刻（含端点）：t_d <= t <= t_recover
    ATTACK_RECOVER_TIME = 40

    # 恢复参数
    # 任务层参数
    MISSION_PROB_THRESHOLD = 0.01  # 任务层链路的最小通信概率阈值

    # 恢复参数
    RECOVERY_SPEED = 1.0  # 恢复移动速度
    SEARCH_RADIUS = 50.0  # 广域搜索半径
    MIN_NODE_DISTANCE = None  # 节点间最小距离，None表示使用R_COMM的某个比例
    # 如果为None，将使用 R_COMM * 0.3 作为最小距离
    
    # 仿真参数
    TIME_STEPS = 100  # 总时间步数
    DT = 1.0  # 时间步长
    
    # 可视化参数（None表示使用默认值）
    SNAPSHOT_TIMES = [19,21,50]
    # 默认值：攻击前、攻击后、最终时刻
    # 示例：[0, 10, 20, 30, 50, 100] 或 [ATTACK_TIME - 1, ATTACK_TIME + 1, TIME_STEPS]
    
    # 随机种子
    RANDOM_SEED = 42
    
    @classmethod
    def get_snapshot_times(cls):
        """获取要保存快照的时间点列表"""
        if cls.SNAPSHOT_TIMES is not None:
            return cls.SNAPSHOT_TIMES
        else:
            # 默认值：攻击前、攻击后、最终时刻
            return [cls.ATTACK_TIME - 1, cls.ATTACK_TIME + 1, cls.TIME_STEPS]
    
    @classmethod
    def get_min_node_distance(cls):
        """获取节点间最小距离"""
        if cls.MIN_NODE_DISTANCE is not None:
            return cls.MIN_NODE_DISTANCE
        else:
            # 默认使用通信半径的30%作为最小距离
            return cls.R_COMM * 0.3
    
    @classmethod
    def validate(cls):
        """验证配置参数"""
        assert cls.N_SENSOR + cls.N_DECIDER + cls.N_INFLUENCER == cls.N_TOTAL, \
            "节点数量总和必须等于总节点数"
        assert cls.N_SENSOR > cls.N_DECIDER > cls.N_INFLUENCER, \
            "节点数量必须满足 |V_S| > |V_D| > |V_I|"
        assert 0 <= cls.ETA <= 1, "ETA必须在[0,1]范围内"
        assert abs((cls.ALPHA + cls.BETA + cls.GAMMA) - 1.0) < 1e-9, \
            "物理层指标权重系数之和必须为1"
        assert abs((cls.W1 + cls.W2 + cls.W3) - 1.0) < 1e-9, \
            "综合性能权重系数 W1+W2+W3 必须为1"

        # 验证攻击配置
        assert cls.ATTACK_MODE in ('physical', 'cyber'), \
            "ATTACK_MODE 仅支持 'physical' 或 'cyber'"
        assert cls.ATTACK_STRATEGY in ('random', 'topology', 'role', 'high_degree', 'critical'), \
            "ATTACK_STRATEGY 不在支持范围内"
        assert cls.ATTACK_ROLE_TARGET in ('SENSOR', 'DECIDER', 'INFLUENCER'), \
            "ATTACK_ROLE_TARGET 仅支持 'SENSOR'|'DECIDER'|'INFLUENCER'"
        if cls.ATTACK_RATIO is not None:
            assert 0 <= cls.ATTACK_RATIO <= 1, "ATTACK_RATIO 必须在[0,1]范围内"
        assert cls.ATTACK_RECOVER_TIME >= cls.ATTACK_TIME, \
            "ATTACK_RECOVER_TIME 必须不小于 ATTACK_TIME"

        # 验证任务阶段区间配置
        assert isinstance(cls.TASK_PHASE_SCHEDULE, list) and len(cls.TASK_PHASE_SCHEDULE) > 0, \
            "TASK_PHASE_SCHEDULE 必须是非空列表"

        # 按起始时间排序后验证连续覆盖与不重叠
        schedule = sorted(cls.TASK_PHASE_SCHEDULE, key=lambda x: x[0])
        expected_start = 0
        expected_end = cls.TIME_STEPS + 1  # 因为仿真时刻是[0, TIME_STEPS]

        for idx, item in enumerate(schedule):
            assert isinstance(item, (list, tuple)) and len(item) == 3, \
                f"TASK_PHASE_SCHEDULE 第{idx}项必须是(start, end, phase)"

            start, end, phase = item
            assert isinstance(start, int) and isinstance(end, int), \
                f"TASK_PHASE_SCHEDULE 第{idx}项 start/end 必须为整数"
            assert start < end, f"TASK_PHASE_SCHEDULE 第{idx}项必须满足 start < end"
            assert phase in (1, 2), f"TASK_PHASE_SCHEDULE 第{idx}项 phase 仅支持1或2"

            assert start == expected_start, \
                f"TASK_PHASE_SCHEDULE 区间不连续或有重叠：期望start={expected_start}，实际start={start}"
            expected_start = end

        assert expected_start == expected_end, \
            f"TASK_PHASE_SCHEDULE 未覆盖完整时域 [0, {cls.TIME_STEPS}]"
        
        # 验证快照时间点
        snapshot_times = cls.get_snapshot_times()
        for t in snapshot_times:
            assert 0 <= t <= cls.TIME_STEPS, \
                f"快照时间点 {t} 必须在 [0, {cls.TIME_STEPS}] 范围内"

