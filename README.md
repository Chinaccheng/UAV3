# 无人机集群多维任务韧性评估系统

基于信息熵驱动的无人机集群多维任务韧性评估实验系统，实现了三层网络架构（物理层、通信层、任务层）的建模与仿真。

## 项目结构

```
UAV3/
├── config.py              # 配置文件（实验参数）
├── node.py                 # 节点类定义
├── network_layers.py       # 三层网络实现
├── performance.py          # 性能评估模块
├── attack.py               # 攻击模块
├── recovery.py             # 恢复策略模块
├── experiment.py           # 主实验流程
├── visualization.py        # 可视化模块
├── main.py                 # 主程序入口
├── requirements.txt        # 依赖包
└── README.md              # 说明文档
```

## 功能特性

### 1. 三层网络架构

- **物理层（Physical Layer）**：基于节点距离判断连边（d_ij ≤ r_c）
- **通信层（Communication Layer）**：基于通信概率 P_ij(t) 确定连边
- **任务层（Mission Layer）**：基于OODA规则的有向边

### 2. 节点类型

- **侦察节点（V_S）**：负责感知和信息收集
- **通信节点（V_D）**：负责中继和决策
- **打击节点（V_I）**：负责执行打击任务

### 3. 性能评估

- **物理层性能 Q_phy(t)**：基于平均度、聚类系数、全局效率
- **通信层性能 Q_comm(t)**：基于信息熵度量交互有序度
- **任务层性能 Q_mis(t)**：基于有效OODA任务链的数量和质量

### 4. 攻击与恢复

- **攻击模块**：支持随机攻击、高度数攻击、关键节点攻击
- **恢复策略**：邻居节点向熵值最低的邻居移动；孤立节点向集群重心移动或执行广域搜索

### 5. 韧性度量

基于基线阈值的时间加权积分法计算系统韧性值 R。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 基本运行

```bash
python main.py
```

### 自定义配置

修改 `config.py` 中的参数：

```python
N_TOTAL = 100
R_COMM = 20.0
ATTACK_TIME = 20
ATTACK_STRATEGY = 'critical'         # 'random' | 'high_degree' | 'critical'
ATTACK_TARGET_TYPE = 'DECIDER'       # critical时生效
ATTACK_TARGET_COUNT = 20             # critical时生效
TASK_PHASE_SCHEDULE = [
    (0, 40, 1),
    (40, 101, 2),
]
TIME_STEPS = 100
```

### 代码示例

```python
from config import Config
from experiment import Experiment
from visualization import Visualizer

# 创建实验
experiment = Experiment(Config)

# 运行实验
history = experiment.run()

# 计算韧性值
resilience = experiment.calculate_resilience()
print(f"系统韧性值: {resilience}")

# 可视化
visualizer = Visualizer()
visualizer.plot_performance_curves(history)
```

## 输出结果

运行后会生成以下可视化结果，所有图像保存在 `result/` 文件夹中：

1. **performance_curves.png**：各层性能曲线
2. **network_statistics.png**：网络统计信息
3. **node_positions_all_layers_t*.png**：关键时刻的三层网络子图（物理层/通信层/任务层）

## 数学模型

本实现基于以下数学模型：

1. **通信概率模型**：
   - P_ij(t) = f_phy(d_ij(t)) × f_logic(i, j, t)
   - 物理层约束：分段线性衰减函数
   - 逻辑层约束：基于OODA任务链的供需匹配

2. **性能函数**：
   - Q_phy(t) = n(t) × (α·K/K₀ + β·C/C₀ + γ·GE/GE₀)
   - Q_comm(t) 基于信息熵
   - Q_mis(t) = E_total(t) / E_total(0)

3. **韧性度量**：
   - R = ∫[max(0, Q(t)-Q_min)·e^(-λ(t-t_d))]dt / ∫[(Q_ideal-Q_min)·e^(-λ(t-t_d))]dt

## 参数说明

主要参数在 `config.py` 中定义：

- `N_TOTAL`: 总节点数（默认100）
- `R_COMM`: 通信半径（默认20）
- `ETA`: 距离影响因子（默认0.7）
- `TASK_PHASE_SCHEDULE`: 任务阶段时间表，格式为 `(start, end, phase)`，例如 `[(0, 50, 1), (50, 101, 2)]`
- `Q_MIN`: 最小性能阈值（默认0.3）
- `LAMBDA`: 时间敏感系数（默认0.05）

## 注意事项

1. 确保已安装所有依赖包
2. 节点数量需满足 |V_S| > |V_D| > |V_I|
3. 通信半径应小于区域大小
4. 攻击时刻应小于总时间步数

## 作者

基于信息熵驱动的无人机集群多维任务韧性评估模型实现。

