import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random

# 设置随机种子
np.random.seed(42)
random.seed(42)


def generate_uav_networks(N=100, rc=20, area_size=100, eta=0.8):
    # --- 1. 节点初始化 ---
    pos = {i: np.random.rand(2) * area_size for i in range(N)}
    nodes = list(range(N))

    shuffled_nodes = nodes.copy()
    np.random.shuffle(shuffled_nodes)
    types = {}
    type_vectors = {}

    # 50 Sensor, 30 Decider, 20 Influencer
    for n in shuffled_nodes[:50]:
        types[n] = 'Sensor'
        type_vectors[n] = np.array([1, 0, 0])
    for n in shuffled_nodes[50:80]:
        types[n] = 'Decider'
        type_vectors[n] = np.array([0, 1, 0])
    for n in shuffled_nodes[80:]:
        types[n] = 'Influencer'
        type_vectors[n] = np.array([0, 0, 1])

    # --- 2. 物理层 (无向) ---
    G_phy = nx.Graph()
    G_phy.add_nodes_from(nodes)
    for i in range(N):
        for j in range(i + 1, N):
            dist = np.linalg.norm(pos[i] - pos[j])
            if dist <= rc:
                G_phy.add_edge(i, j)

    # --- 3. 通信层 (有向, 概率) ---
    G_comm = nx.DiGraph()
    G_comm.add_nodes_from(nodes)
    epsilon = 0.1
    Omega = np.array([[epsilon, 1.0, 1.0], [epsilon, 1.0, 1.0], [1.0, 1.0, epsilon]])

    for i in range(N):
        for j in range(i + 1, N):
            dist = np.linalg.norm(pos[i] - pos[j])
            if dist > rc: continue

            f_phy = 1 if dist < eta * rc else (rc - dist) / (rc * (1 - eta))
            score_ij = np.dot(np.dot(type_vectors[i], Omega), type_vectors[j])
            score_ji = np.dot(np.dot(type_vectors[j], Omega), type_vectors[i])
            P_ij = f_phy * score_ij
            P_ji = f_phy * score_ji

            if random.random() < P_ij:
                G_comm.add_edge(i, j)
            if random.random() < P_ji:
                G_comm.add_edge(j, i)

    # --- 4. 任务层 (有向) ---
    G_mis = nx.DiGraph()
    G_mis.add_nodes_from(nodes)
    valid_flows = set([
        ('Sensor', 'Sensor'), ('Sensor', 'Decider'), ('Sensor', 'Influencer'),
        ('Decider', 'Decider'), ('Decider', 'Sensor'), ('Decider', 'Influencer')
    ])
    for u, v in G_comm.edges():
        if (types[u], types[v]) in valid_flows:
            G_mis.add_edge(u, v)

    return G_phy, G_comm, G_mis, pos, types


def plot_3d_stacked_final(G_phy, G_comm, G_mis, pos, types, area_size=100):
    fig = plt.figure(figsize=(15, 12))
    ax = fig.add_subplot(111, projection='3d')

    # --- 高度配置 ---
    z_mis = 0  # 底部：任务层
    z_phy = 60  # 中部：物理层
    z_comm = 120  # 顶部：通信层

    color_map = {'Sensor': '#2ecc71', 'Decider': '#3498db', 'Influencer': '#e74c3c'}

    # --- 1. 绘制“玻璃板”背景 ---
    pad = 10
    xx, yy = np.meshgrid(np.linspace(-pad, area_size + pad, 2), np.linspace(-pad, area_size + pad, 2))
    layers = [z_mis, z_phy, z_comm]

    for z_h in layers:
        ax.plot_surface(xx, yy, np.full_like(xx, z_h), alpha=0.03, color='gray', shade=False)
        ax.plot([-pad, area_size + pad, area_size + pad, -pad, -pad],
                [-pad, -pad, area_size + pad, area_size + pad, -pad],
                [z_h] * 5, c='k', lw=0.8, alpha=0.3)

    # --- 2. 绘制层间连线 (彩色虚线) ---
    sample_nodes = random.sample(list(G_phy.nodes()), int(len(G_phy.nodes()) * 0.20))
    for n in sample_nodes:
        x = [pos[n][0], pos[n][0]]
        y = [pos[n][1], pos[n][1]]
        z = [z_mis, z_comm]
        line_color = color_map[types[n]]
        ax.plot(x, y, z, c=line_color, linestyle='--', alpha=0.5, linewidth=1.0)

    # --- 3. 绘制各层内部的边 ---

    # >>> 关键修改：任务层 (Mission Layer) - 增强显示的有向箭头 <<<
    for u, v in G_mis.edges():
        x_start, y_start = pos[u]
        x_end, y_end = pos[v]

        # 使用 quiver 绘制箭头
        # arrow_length_ratio=0.2 增大箭头头部
        # linewidth=1.5 加粗线条
        # alpha=0.9 加深颜色
        ax.quiver(x_start, y_start, z_mis,
                  x_end - x_start, y_end - y_start, 0,
                  color='#8e44ad',  # 深紫色
                  alpha=0.9,
                  arrow_length_ratio=0.2,
                  linewidth=1.5)

    # 物理层 (灰色无向线)
    for u, v in G_phy.edges():
        ax.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], [z_phy, z_phy],
                c='gray', alpha=0.2, linewidth=0.6)

    # 通信层 (橙色有向线)
    for u, v in G_comm.edges():
        ax.quiver(pos[u][0], pos[u][1], z_comm,
                  pos[v][0] - pos[u][0], pos[v][1] - pos[u][1], 0,
                  color='orange', alpha=0.6, arrow_length_ratio=0.15, linewidth=0.8)

    # --- 4. 绘制节点 ---
    def draw_nodes(G, z_height):
        xs = [pos[n][0] for n in G.nodes()]
        ys = [pos[n][1] for n in G.nodes()]
        zs = [z_height] * len(G.nodes())
        cs = [color_map[types[n]] for n in G.nodes()]
        ax.scatter(xs, ys, zs, c=cs, s=40, edgecolors='white', linewidth=0.8, alpha=1.0)

    draw_nodes(G_mis, z_mis)
    draw_nodes(G_phy, z_phy)
    draw_nodes(G_comm, z_comm)

    # --- 5. 标签与修饰 ---
    label_x = -15
    label_y = -15
    ax.text(label_x, label_y, z_mis, "Mission Layer\n(Directed Flow)", fontsize=11, fontweight='bold', color='#8e44ad')
    ax.text(label_x, label_y, z_phy, "Physical Layer\n(Distance)", fontsize=11, fontweight='bold', color='gray')
    ax.text(label_x, label_y, z_comm, "Comm Layer\n(Probabilistic)", fontsize=11, fontweight='bold', color='orange')

    ax.set_xlim(-20, area_size + 20)
    ax.set_ylim(-20, area_size + 20)
    ax.set_zlim(z_mis - 10, z_comm + 10)
    ax.set_axis_off()
    ax.view_init(elev=20, azim=-50)

    # Legend
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Sensor', markerfacecolor=color_map['Sensor'], markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Decider', markerfacecolor=color_map['Decider'], markersize=8),
        Line2D([0], [0], marker='o', color='w', label='Influencer', markerfacecolor=color_map['Influencer'],
               markersize=8),
        Line2D([0], [0], color='#8e44ad', lw=2, label='Mission Flow (Bold Arrow)'),  # 更新图例说明
        Line2D([0], [0], color='gray', linestyle='--', label='Cross-Layer Link'),
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    plt.tight_layout()
    plt.show()


# --- 运行 ---
G_phy, G_comm, G_mis, pos, types = generate_uav_networks()
plot_3d_stacked_final(G_phy, G_comm, G_mis, pos, types)
