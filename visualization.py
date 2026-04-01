"""
可视化模块：绘制实验结果
"""
import matplotlib.pyplot as plt
import numpy as np
from typing import Dict
import matplotlib
from matplotlib.lines import Line2D
from node import NodeType

matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

class Visualizer:
    """可视化器"""
    
    def __init__(self, figsize=(12, 8)):
        self.figsize = figsize

    @staticmethod
    def _draw_directed_edge(ax, start_pos, end_pos, color, linewidth, alpha,
                            linestyle='-', label=None):
        """绘制有向边，并在需要时补一条可进图例的线段。"""
        ax.annotate(
            '',
            xy=(end_pos[0], end_pos[1]),
            xytext=(start_pos[0], start_pos[1]),
            arrowprops=dict(
                arrowstyle='->',
                color=color,
                lw=linewidth,
                alpha=alpha,
                linestyle=linestyle,
                shrinkA=8,
                shrinkB=8,
            ),
        )
        if label:
            ax.plot(
                [start_pos[0], end_pos[0]],
                [start_pos[1], end_pos[1]],
                color=color,
                linewidth=linewidth,
                alpha=min(alpha, 0.4),
                linestyle=linestyle,
                label=label,
            )
    
    def plot_performance_curves(self, history: Dict, save_path: str = None):
        """
        绘制性能曲线
        
        Args:
            history: 实验历史数据
            save_path: 保存路径（可选）
        """
        fig, axes = plt.subplots(2, 2, figsize=self.figsize)
        fig.suptitle('无人机集群性能曲线', fontsize=16, fontweight='bold')
        
        time = np.array(history['time'])
        
        # 物理层性能
        axes[0, 0].plot(time, history['Q_phy'], 'b-', linewidth=2, label='物理层性能')
        axes[0, 0].axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='性能阈值')
        axes[0, 0].set_xlabel('时间步')
        axes[0, 0].set_ylabel('性能值')
        axes[0, 0].set_title('物理层性能 Q_phy(t)')
        axes[0, 0].grid(True, alpha=0.3)
        axes[0, 0].legend()
        
        # 通信层性能
        axes[0, 1].plot(time, history['Q_comm'], 'g-', linewidth=2, label='通信层性能')
        axes[0, 1].axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='性能阈值')
        axes[0, 1].set_xlabel('时间步')
        axes[0, 1].set_ylabel('性能值')
        axes[0, 1].set_title('通信层性能 Q_comm(t)')
        axes[0, 1].grid(True, alpha=0.3)
        axes[0, 1].legend()
        
        # 任务层性能
        axes[1, 0].plot(time, history['Q_mis'], 'm-', linewidth=2, label='任务层性能')
        axes[1, 0].axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='性能阈值')
        axes[1, 0].set_xlabel('时间步')
        axes[1, 0].set_ylabel('性能值')
        axes[1, 0].set_title('任务层性能 Q_mis(t)')
        axes[1, 0].grid(True, alpha=0.3)
        axes[1, 0].legend()
        
        # 综合性能
        axes[1, 1].plot(time, history['Q_overall'], 'k-', linewidth=2, label='综合性能')
        axes[1, 1].axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='性能阈值')
        axes[1, 1].axvline(x=20, color='orange', linestyle=':', alpha=0.7, label='攻击时刻')
        axes[1, 1].set_xlabel('时间步')
        axes[1, 1].set_ylabel('性能值')
        axes[1, 1].set_title('系统综合性能 Q_overall(t)')
        axes[1, 1].grid(True, alpha=0.3)
        axes[1, 1].legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"性能曲线已保存至: {save_path}")
        
        plt.show()
    
    def plot_network_statistics(self, history: Dict, save_path: str = None):
        """
        绘制网络统计信息
        
        Args:
            history: 实验历史数据
            save_path: 保存路径（可选）
        """
        fig, axes = plt.subplots(2, 1, figsize=(10, 8))
        fig.suptitle('网络统计信息', fontsize=16, fontweight='bold')
        
        time = np.array(history['time'])
        
        # 存活节点数
        axes[0].plot(time, history['num_alive_nodes'], 'b-', linewidth=2, label='存活节点数')
        axes[0].axvline(x=20, color='r', linestyle='--', alpha=0.7, label='攻击时刻')
        axes[0].set_xlabel('时间步')
        axes[0].set_ylabel('节点数量')
        axes[0].set_title('存活节点数量变化')
        axes[0].grid(True, alpha=0.3)
        axes[0].legend()
        
        # 边数量
        axes[1].plot(time, history['num_edges_phy'], 'b-', linewidth=1.5, label='物理层边数', alpha=0.7)
        axes[1].plot(time, history['num_edges_comm'], 'g-', linewidth=1.5, label='通信层边数', alpha=0.7)
        axes[1].plot(time, history['num_edges_mis'], 'm-', linewidth=1.5, label='任务层边数', alpha=0.7)
        axes[1].axvline(x=20, color='r', linestyle='--', alpha=0.7, label='攻击时刻')
        axes[1].set_xlabel('时间步')
        axes[1].set_ylabel('边数量')
        axes[1].set_title('各层网络边数量变化')
        axes[1].grid(True, alpha=0.3)
        axes[1].legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"网络统计图已保存至: {save_path}")
        
        plt.show()
    
    def plot_node_positions(self, nodes, physical_layer, t: int, 
                           comm_layer=None, mission_layer=None,
                           layer='physical', save_path: str = None):
        """
        绘制节点位置和网络拓扑
        
        Args:
            nodes: 节点列表
            physical_layer: 物理层网络
            t: 当前时刻
            comm_layer: 通信层网络（可选）
            mission_layer: 任务层网络（可选）
            layer: 要绘制的网络层 ('physical', 'communication', 'mission', 'all')
            save_path: 保存路径（可选）
        """
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # 用于跟踪是否已添加图例标签
        legend_added = {'physical': False, 'communication': False, 'mission': False}
        
        # 根据选择的层绘制边
        if layer == 'physical' or layer == 'all':
            # 绘制物理层边（灰色，细线）
            for i, edge in enumerate(physical_layer.graph.edges()):
                node_i = next(n for n in nodes if n.id == edge[0])
                node_j = next(n for n in nodes if n.id == edge[1])
                if node_i.is_alive and node_j.is_alive:
                    # 只在第一条边时添加图例标签
                    if layer == 'physical' and not legend_added['physical']:
                        label = '物理层'
                        legend_added['physical'] = True
                    elif layer == 'all' and not legend_added['physical']:
                        label = '物理层'
                        legend_added['physical'] = True
                    else:
                        label = ''
                    ax.plot([node_i.position[0], node_j.position[0]],
                           [node_i.position[1], node_j.position[1]],
                           'gray', linewidth=0.5, alpha=0.3, label=label)
        
        if (layer == 'communication' or layer == 'all') and comm_layer is not None:
            # 绘制通信层边（绿色，中等粗细，有向箭头）
            for edge in comm_layer.graph.edges():
                node_i = next(n for n in nodes if n.id == edge[0])
                node_j = next(n for n in nodes if n.id == edge[1])
                if node_i.is_alive and node_j.is_alive:
                    if layer == 'communication' and not legend_added['communication']:
                        label = '通信层'
                        legend_added['communication'] = True
                    elif layer == 'all' and not legend_added['communication']:
                        label = '通信层'
                        legend_added['communication'] = True
                    else:
                        label = ''
                    self._draw_directed_edge(
                        ax,
                        node_i.position,
                        node_j.position,
                        color='green',
                        linewidth=1.2,
                        alpha=0.55,
                        linestyle='--',
                        label=label,
                    )
        
        if (layer == 'mission' or layer == 'all') and mission_layer is not None:
            # 绘制任务层边（红色，粗线，有向箭头）
            for i, edge in enumerate(mission_layer.graph.edges()):
                node_i = next(n for n in nodes if n.id == edge[0])
                node_j = next(n for n in nodes if n.id == edge[1])
                if node_i.is_alive and node_j.is_alive:
                    # 只在第一条边时添加图例标签
                    if layer == 'mission' and not legend_added['mission']:
                        label = '任务层'
                        legend_added['mission'] = True
                    elif layer == 'all' and not legend_added['mission']:
                        label = '任务层'
                        legend_added['mission'] = True
                    else:
                        label = ''
                    self._draw_directed_edge(
                        ax,
                        node_i.position,
                        node_j.position,
                        color='red',
                        linewidth=1.5,
                        alpha=0.65,
                        label=label,
                    )
        
        # 绘制节点
        colors = {'SENSOR': 'blue', 'DECIDER': 'green', 'INFLUENCER': 'red'}
        markers = {'SENSOR': 'o', 'DECIDER': 's', 'INFLUENCER': '^'}
        
        for node_type in NodeType:
            type_nodes = [n for n in nodes if n.type == node_type]
            alive_nodes = [n for n in type_nodes if n.is_alive]
            dead_nodes = [n for n in type_nodes if not n.is_alive]
            
            if alive_nodes:
                x_alive = [n.position[0] for n in alive_nodes]
                y_alive = [n.position[1] for n in alive_nodes]
                ax.scatter(x_alive, y_alive, c=colors[node_type.name], 
                          marker=markers[node_type.name], s=100, 
                          alpha=0.7, label=f'{node_type.name} (存活)')
            
            if dead_nodes:
                x_dead = [n.position[0] for n in dead_nodes]
                y_dead = [n.position[1] for n in dead_nodes]
                ax.scatter(x_dead, y_dead, c='black', marker='x', 
                          s=150, alpha=0.5, label=f'{node_type.name} (被攻击)')
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('X坐标')
        ax.set_ylabel('Y坐标')
        
        # 设置标题
        layer_names = {
            'physical': '物理层',
            'communication': '通信层',
            'mission': '任务层',
            'all': '三层网络'
        }
        ax.set_title(f'时刻 {t} 的节点分布和{layer_names.get(layer, "网络")}拓扑')
        ax.grid(True, alpha=0.3)
        
        # 添加图例
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        if by_label:
            ax.legend(by_label.values(), by_label.keys(), loc='upper right')
        
        ax.set_aspect('equal')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"节点位置图已保存至: {save_path}")
        
        plt.show()
    
    def plot_all_layers_subplots(self, nodes, physical_layer, t: int, 
                                 comm_layer=None, mission_layer=None,
                                 save_path: str = None):
        """
        将物理层、通信层、任务层绘制为三个子图
        
        Args:
            nodes: 节点列表
            physical_layer: 物理层网络
            t: 当前时刻
            comm_layer: 通信层网络（可选）
            mission_layer: 任务层网络（可选）
            save_path: 保存路径（可选）
        """
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        fig.suptitle(f'时刻 {t} 的三层网络拓扑', fontsize=16, fontweight='bold')
        
        # 节点颜色和标记
        colors = {'SENSOR': 'blue', 'DECIDER': 'green', 'INFLUENCER': 'red'}
        markers = {'SENSOR': 'o', 'DECIDER': 's', 'INFLUENCER': '^'}
        
        # 绘制物理层
        ax = axes[0]
        # 绘制物理层边
        for edge in physical_layer.graph.edges():
            node_i = next(n for n in nodes if n.id == edge[0])
            node_j = next(n for n in nodes if n.id == edge[1])
            if node_i.is_alive and node_j.is_alive:
                ax.plot([node_i.position[0], node_j.position[0]],
                       [node_i.position[1], node_j.position[1]],
                       'gray', linewidth=0.8, alpha=0.4)
        
        # 绘制节点
        for node_type in NodeType:
            type_nodes = [n for n in nodes if n.type == node_type]
            alive_nodes = [n for n in type_nodes if n.is_alive]
            dead_nodes = [n for n in type_nodes if not n.is_alive]
            
            if alive_nodes:
                x_alive = [n.position[0] for n in alive_nodes]
                y_alive = [n.position[1] for n in alive_nodes]
                ax.scatter(x_alive, y_alive, c=colors[node_type.name], 
                          marker=markers[node_type.name], s=80, 
                          alpha=0.7, label=f'{node_type.name} (存活)')
            
            if dead_nodes:
                x_dead = [n.position[0] for n in dead_nodes]
                y_dead = [n.position[1] for n in dead_nodes]
                ax.scatter(x_dead, y_dead, c='black', marker='x', 
                          s=120, alpha=0.5, label=f'{node_type.name} (被攻击)')
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('X坐标')
        ax.set_ylabel('Y坐标')
        ax.set_title('物理层拓扑', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=8)
        ax.set_aspect('equal')
        
        # 绘制通信层
        ax = axes[1]
        if comm_layer is not None:
            # 绘制通信层边（有向）
            for edge in comm_layer.graph.edges():
                node_i = next(n for n in nodes if n.id == edge[0])
                node_j = next(n for n in nodes if n.id == edge[1])
                if node_i.is_alive and node_j.is_alive:
                    self._draw_directed_edge(
                        ax,
                        node_i.position,
                        node_j.position,
                        color='green',
                        linewidth=1.2,
                        alpha=0.6,
                        linestyle='--',
                    )
        
        # 绘制节点
        for node_type in NodeType:
            type_nodes = [n for n in nodes if n.type == node_type]
            alive_nodes = [n for n in type_nodes if n.is_alive]
            dead_nodes = [n for n in type_nodes if not n.is_alive]
            
            if alive_nodes:
                x_alive = [n.position[0] for n in alive_nodes]
                y_alive = [n.position[1] for n in alive_nodes]
                ax.scatter(x_alive, y_alive, c=colors[node_type.name], 
                          marker=markers[node_type.name], s=80, 
                          alpha=0.7, label=f'{node_type.name} (存活)')
            
            if dead_nodes:
                x_dead = [n.position[0] for n in dead_nodes]
                y_dead = [n.position[1] for n in dead_nodes]
                ax.scatter(x_dead, y_dead, c='black', marker='x', 
                          s=120, alpha=0.5, label=f'{node_type.name} (被攻击)')
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('X坐标')
        ax.set_ylabel('Y坐标')
        ax.set_title('通信层拓扑', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        comm_legend = [
            Line2D([0], [0], color='green', linestyle='--', lw=1.2, label='有向通信链路'),
        ]
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles + comm_legend, labels + ['有向通信链路'], loc='upper right', fontsize=8)
        ax.set_aspect('equal')
        
        # 绘制任务层
        ax = axes[2]
        if mission_layer is not None:
            # 绘制任务层边（有向箭头）
            for edge in mission_layer.graph.edges():
                node_i = next(n for n in nodes if n.id == edge[0])
                node_j = next(n for n in nodes if n.id == edge[1])
                if node_i.is_alive and node_j.is_alive:
                    self._draw_directed_edge(
                        ax,
                        node_i.position,
                        node_j.position,
                        color='red',
                        linewidth=1.5,
                        alpha=0.7,
                    )
        
        # 绘制节点
        for node_type in NodeType:
            type_nodes = [n for n in nodes if n.type == node_type]
            alive_nodes = [n for n in type_nodes if n.is_alive]
            dead_nodes = [n for n in type_nodes if not n.is_alive]
            
            if alive_nodes:
                x_alive = [n.position[0] for n in alive_nodes]
                y_alive = [n.position[1] for n in alive_nodes]
                ax.scatter(x_alive, y_alive, c=colors[node_type.name], 
                          marker=markers[node_type.name], s=80, 
                          alpha=0.7, label=f'{node_type.name} (存活)')
            
            if dead_nodes:
                x_dead = [n.position[0] for n in dead_nodes]
                y_dead = [n.position[1] for n in dead_nodes]
                ax.scatter(x_dead, y_dead, c='black', marker='x', 
                          s=120, alpha=0.5, label=f'{node_type.name} (被攻击)')
        
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_xlabel('X坐标')
        ax.set_ylabel('Y坐标')
        ax.set_title('任务层拓扑', fontsize=12, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend(loc='upper right', fontsize=8)
        ax.set_aspect('equal')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"三层网络拓扑图已保存至: {save_path}")
        
        plt.show()
    
    def plot_resilience_comparison(self, histories: Dict[str, Dict], save_path: str = None):
        """
        绘制不同策略的韧性对比
        
        Args:
            histories: 不同策略的历史数据字典 {策略名: 历史数据}
            save_path: 保存路径（可选）
        """
        fig, ax = plt.subplots(figsize=(10, 6))
        
        for strategy_name, history in histories.items():
            time = np.array(history['time'])
            Q_overall = np.array(history['Q_overall'])
            ax.plot(time, Q_overall, linewidth=2, label=strategy_name)
        
        ax.axhline(y=0.3, color='r', linestyle='--', alpha=0.5, label='性能阈值')
        ax.axvline(x=20, color='orange', linestyle=':', alpha=0.7, label='攻击时刻')
        ax.set_xlabel('时间步')
        ax.set_ylabel('综合性能')
        ax.set_title('不同恢复策略的韧性对比')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
            print(f"韧性对比图已保存至: {save_path}")
        
        plt.show()
