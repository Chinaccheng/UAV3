"""
主程序：运行无人机集群韧性评估实验
"""
import os
import numpy as np
from config import Config
from experiment import Experiment
from visualization import Visualizer

def main():
    """主函数"""
    # 创建结果文件夹
    result_dir = os.path.join('result', 'main')
    if not os.path.exists(result_dir):
        os.makedirs(result_dir)
        print(f"创建结果文件夹: {result_dir}")
    
    # 验证配置
    Config.validate()
    
    # 创建实验
    experiment = Experiment(Config)
    
    # 运行实验
    history = experiment.run()
    
    # 计算韧性值
    resilience = experiment.calculate_resilience()
    print(f"\n系统韧性值 R = {resilience:.4f}")
    
    # 可视化结果
    visualizer = Visualizer()
    
    # 绘制性能曲线
    print("\n绘制性能曲线...")
    save_path = os.path.join(result_dir, 'performance_curves.png')
    visualizer.plot_performance_curves(history, save_path=save_path)
    
    # 绘制网络统计信息
    print("\n绘制网络统计信息...")
    save_path = os.path.join(result_dir, 'network_statistics.png')
    visualizer.plot_network_statistics(history, save_path=save_path)
    
    # 绘制关键时刻的节点分布（三层网络子图）
    print("\n绘制关键时刻的节点分布...")
    
    # 从快照中恢复节点状态并绘制
    snapshot_times = Config.get_snapshot_times()
    print(f"可视化时间点: {snapshot_times}")
    
    for t in snapshot_times:
        snapshot = experiment.get_snapshot(t)
        if snapshot:
            # 恢复节点状态
            for node_state in snapshot['nodes']:
                node = next(n for n in experiment.nodes if n.id == node_state['id'])
                node.position = node_state['position'].copy()
                node.is_alive = node_state['is_alive']
            
            # 恢复各层网络
            experiment.physical_layer.graph = snapshot['physical_layer']
            comm_graph = snapshot.get('comm_layer', None)
            mission_graph = snapshot.get('mission_layer', None)
            
            # 如果快照中没有通信层和任务层，需要重新计算
            if comm_graph is None or mission_graph is None:
                experiment.update_networks(t)
                comm_graph = experiment.comm_layer.graph
                mission_graph = experiment.mission_layer.graph
            else:
                # 恢复通信层和任务层
                experiment.comm_layer.graph = comm_graph
                experiment.mission_layer.graph = mission_graph
            
            # 绘制三层网络子图
            save_path = os.path.join(result_dir, f'node_positions_all_layers_t{t}.png')
            print(f"  绘制时刻 {t} 的三层网络拓扑...")
                
            visualizer.plot_all_layers_subplots(
                    experiment.nodes, 
                    experiment.physical_layer, 
                    t,
                comm_layer=experiment.comm_layer,
                mission_layer=experiment.mission_layer,
                    save_path=save_path
                )
    
    print(f"\n实验完成！所有结果已保存到 {result_dir} 文件夹。")

if __name__ == '__main__':
    main()
