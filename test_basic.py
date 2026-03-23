"""
基本功能测试脚本
"""
import numpy as np
from config import Config
from node import Node, NodeType
from network_layers import PhysicalLayer, CommunicationLayer, MissionLayer
from performance import PerformanceEvaluator

def test_basic():
    """测试基本功能"""
    print("开始基本功能测试...")
    
    # 验证配置
    try:
        Config.validate()
        print("✓ 配置验证通过")
    except Exception as e:
        print(f"✗ 配置验证失败: {e}")
        return
    
    # 创建测试节点
    nodes = []
    for i in range(10):
        node_type = NodeType.SENSOR if i < 5 else NodeType.DECIDER
        position = np.random.uniform(0, 50, size=2)
        node = Node(i, node_type, position, Config)
        nodes.append(node)
    print(f"✓ 创建了 {len(nodes)} 个测试节点")
    
    # 测试物理层
    try:
        physical_layer = PhysicalLayer(Config)
        physical_layer.update(nodes)
        print(f"✓ 物理层创建成功，边数: {physical_layer.graph.number_of_edges()}")
    except Exception as e:
        print(f"✗ 物理层创建失败: {e}")
        return
    
    # 测试通信层
    try:
        comm_layer = CommunicationLayer(Config)
        comm_layer.update(nodes, physical_layer, 0)
        print(f"✓ 通信层创建成功，边数: {comm_layer.graph.number_of_edges()}")
    except Exception as e:
        print(f"✗ 通信层创建失败: {e}")
        return
    
    # 测试任务层
    try:
        mission_layer = MissionLayer(Config)
        mission_layer.update(nodes, comm_layer)
        print(f"✓ 任务层创建成功，边数: {mission_layer.graph.number_of_edges()}")
    except Exception as e:
        print(f"✗ 任务层创建失败: {e}")
        return
    
    # 测试性能评估
    try:
        evaluator = PerformanceEvaluator(Config)
        Q_phy, Q_comm, Q_mis, Q_overall = evaluator.calculate_overall_performance(
            nodes, physical_layer, comm_layer, mission_layer)
        print(f"✓ 性能评估成功: Q_phy={Q_phy:.3f}, Q_comm={Q_comm:.3f}, "
              f"Q_mis={Q_mis:.3f}, Q_overall={Q_overall:.3f}")
    except Exception as e:
        print(f"✗ 性能评估失败: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n所有基本功能测试通过！")

if __name__ == '__main__':
    test_basic()

