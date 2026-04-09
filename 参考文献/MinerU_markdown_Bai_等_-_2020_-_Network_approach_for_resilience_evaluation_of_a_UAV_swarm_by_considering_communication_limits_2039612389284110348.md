# 考虑通信限制的无人机集群韧性评估的网络方法

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/d0a31e2bb828be377241eb6582cb6f6d6c8dd8c434cccae413e02db92ec7d954.jpg)


白广汉, 李艳军, 方一宁, 张云安*, 陶军勇

综合物流保障科学技术实验室，国防科技大学，长沙，中国

# 文章信息

关键词：

系统韧性

无人机集群

动态距离

复杂网络

信息交换

# ABSTRACT

无人机(UAV)集群是一组在自组织和自适应方式下执行任务以实现整体任务目标的无人机。目前，无人机集群的模型基于复杂网络，其中每个无人机表示为一个节点，每个链接表示无人机之间的信息交换。然而，现有研究未考虑每个无人机的有限通信范围。在本研究中，通过将有限通信范围的影响纳入现有模型，提出了改进的无人机集群模型。无人机集群通过自适应来减轻可能的威胁和中断的影响；因此，使用韧性来评估其性能是合适的。基于集群性能与其标准系统性能之间的差异，提出了改进的韧性指标。进行了一项案例研究，其中调用无人机游泳来执行监视任务。结果与现有研究的比较表明，提出的模型和指标为评估无人机集群的韧性提供了一种更现实的方法。提出的模型和指标可用于支持任务规划和无人机集群的设计。

# 1.简介

无人驾驶航空器（无人机）的使用带来了敏捷性和低成本，并且允许在不危及人类的情况下实施枯燥、肮脏和危险的任务。最近，人们越来越关注无人机在民用和军事领域的应用。例如，长时间重复任务、受威胁环境下的监视任务以及核生化环境下的监视任务。

无人机当前的其中一个趋势是集群使用，其中一组大量无人机以自组织和自适应的方式执行任务，以实现整体任务目标。自组织意味着无人机集群通过局部交互自发地形成一个完全去中心化的秩序。自适应意味着无人机集群通过局部交互自发地展现出适应环境变化、威胁和破坏性事件的能力。自组织和自适应需要敏捷且具有弹性的信息交换（简称IE）网络，以实现无人机集群在链路连接、链路通信和链路重配置方面的要求。因此，在本研究中，无人机集群被表示为IE网络，其中节点代表无人机，链路代表无人机之间交换的信息。

未来数量将继续增加。尽管集群的复杂性不断增加，但关于上述类型的大规模网络的性能评估研究仍然不足。常见的性能指标是可靠性，它用于评估系统维持正常运行的能力。具体来说，已开发并应用于评估网络化系统性能的几种可靠性指标，包括二元网络的连通性指标和多状态网络的性能指标 [23]。在上述报告中提到的指标中，如果组件和网络不可修复，则可靠性表示组件或网络在指定时间内处于某种状态的概率。如果组件和网络可修复，则可靠性表示当时间趋于无穷时组件或系统处于某种状态的概率。概率指标基于组件和系统在历史中的故障数据。此外，在网络可靠性分析中通常假设网络拓扑保持不变。因此，降低故障概率的主要方法是在设计阶段使用高可靠性组件和/或增加系统冗余。

目前，集群中的无人机数量已超过数百，并且

然而，无人机集群通常用于在冲突环境中执行肮脏和危险的任务。这种困难特别体现在军事任务中，其中不可预测的威胁和

不可避免的破坏性事件对应于集群失效的主要原因。因此，收集历史失效数据既困难又无意义。为了减轻不可预见的威胁和不受欢迎的事件，传统方法（包括使用高可靠性组件和/或增加系统冗余）并非成本效益[2]。相反，无人机集群被设计为适应破坏性事件，并通过系统重构和/或改革来恢复其性能。例如，在指定战场上执行监视任务的无人机集群可能会暴露于敌方的防空系统[3]。当一些无人机被摧毁，这是不可预测且不可避免的，其与其他无人机的连接会丢失。随后，鉴于自组织和自适应的能力，丢失连接的无人机及时重新连接到其余活跃的无人机。因此，无人机集群恢复了其性能并继续其任务目标。如前所述的场景所示，无人机集群能够适应破坏性事件，并恢复其预期性能以完成其分配的任务。弹性为工程系统的设计和分析提供了一种新方法，以增强上述系统抵御不确定威胁和从破坏性事件中恢复的能力。因此，使用弹性对无人机集群的性能评估更为合适。

给出系统韧性评估的一般步骤如下。首先，开发一个适当的网络模型来描述无人机集群。其次，开发一个适当的韧性评估方法。我们讨论这两个步骤的现有研究如下。

# 1.1. 无人机集群作为网络的模型

无人机集群的模型包括三种场景：初始集群拓扑模型、集群损伤模型和集群恢复模型。考虑到无人机的巨大规模和沉重的数据传输负载[1]，无人机集群难以完全连接。复杂网络方法被广泛应用于建模几个现实世界系统。Tran等人[2]应用复杂网络方法来建模无人机集群的三种场景。初始网络拓扑是使用具有优先连接的幂律网络[5,6]生成的。网络损伤是通过以目标方式[3]移除节点来实现的，其中在每个威胁事件中优先移除具有更多邻居的节点(s)。网络恢复是通过优先模式[4]中的链路重连来实现的，其中优先重连具有更多邻居的节点。

然而，现有研究中使用的复杂网络模型[2-4]没有考虑无人机之间的地理距离和距离的动态变化。目前，无人机集群被设计为使用无线通信进行无人机之间的信息共享和交互[1]。每架无人机都使用多跳通信接收和发送信息。显然，数据传输的连通性和可靠性受每对无人机之间距离的影响。因此，假设相距较远的两架无人机具有与相距较近的两架无人机相同的通信质量是不现实的。此外，每对无人机之间的连接会发生变化。这是因为每对无人机在任务期间的相对位置会迅速变化。将距离及其动态变化的影响纳入无人机集群模型非常重要。

基于优先连接模型 [6], Barthelemy [7] 考虑了复杂网络模型中节点间距离的影响，通过引入调整参数和距离函数。Barrat等人 [8] 在 [7] 中通过考虑带权重的节点改进了该模型。Manna和Sen [9] 提出了不同的距离函数，并将调整因子引入优先连接函数中。在已报告的研究中，节点的优先连接受候选节点距离的影响呈下降趋势。然而，已报告的模型存在两个局限性，使其不适用于无人机集群。

首先，已报告的模型[7-10]生成的网络可能包含孤立簇和节点。孤立簇和节点存在于少数真实网络中。然而，这不适用于无人机集群。集群是完全自组织和自适应的；因此，其意识和行动基于无人机间的局部交互。鉴于每个单个无人机的能力有限，如果存在孤立簇和/或节点，集群的联合能力将显著降低。我们以监视任务中的无人机集群为例。如果存在孤立簇和/或节点，则每个孤立簇或节点仅获取有限的目标场信息，且不包含其他无人机的位置信息及其对目标场的意识。因此，少数区域可能被过多无人机监控，而多个盲区可能仍然存在。因此，无人机集群无法获得目标场的完整态势感知，任务失败。因此，有必要通过引入节点间距离的影响来改进已报告的模型，这样可以避免生成孤立簇和/或节点。

其次，已报告的模型[7-10]没有考虑每对无人机之间距离的动态变化。[7-10]检查的网络主要对应于静态网络，包括交通和移动网络、互联网和电网。然而，无人机集群高度机动化，并且无人机集群的拓扑结构在任务期间可以迅速变化。因此，有必要改进已报告的模型，通过结合任务操作期间每对无人机相对位置的动态变化来实现。

# 1.2. 无人机集群的韧性评估

韧性及其评估方法已被发展和应用于多个现实世界的复杂系统，包括基础设施 [11,12,22], 生态系统 [13,14], 和复杂工程系统 [15,17]。韧性评估方法的总结见 [16]。

最近，Nan和Sansavini[12]提出了一种评估相互依赖的基础设施韧性的方法，其中基于时间尺度和性能水平提出了一个综合指标。每个因素都与定义的韧性能力概念一致，韧性指标表现出一个范围 $[0,\infty)$ 。Tran等人[17,2]提出了一种韧性评估方法，其中考虑了破坏性事件前和恢复事件后的系统性能数据。此外，它还可以用于评估受多重破坏影响的系统。然而，现有研究并未考虑无人机集群的韧性评估。据作者所知，只有Tran等人[3]将提出的韧性评估方法应用于[17]进行无人机集群的韧性评估。

[3,17] 中的韧性指标主要关注系统的拓扑结构。首先，通过一个综合无人机集群的多个关键性能因子的函数获得每个破坏-恢复事件的韧性值，其中每个因子通过使用恢复后的相应能力与破坏前的相应能力的比率获得。其次，通过对每个破坏-恢复事件的韧性值进行加权平均来计算系统总韧性。如前所述的步骤所示，所报告的韧性度量是使用无人机集群的当前性能与无人机集群在最后稳定状态下的性能之间的差值获得的。这反映了集群网络拓扑适应破坏事件并恢复其预期性能的能力。

然而，韧性指标可能不适用于无人机集群，其中目标涉及完成分配的任务。实际上，无人机集群是任务导向的，这表明存在一个合格的系统性能，可以完成分配的任务。管理员或指挥官希望了解每次中断后无人机集群的当前性能，并将其与标准系统性能进行比较。他们还希望确定无人机集群的整体性能，并在任务期间将其与标准系统性能进行比较。

随后，他们可以确定是否开始任务，或者中止任务并通过增加无人机来重新规划任务，使集群实现所需的韧性。这最终有助于无人机集群完成分配的任务。报告的韧性仅反映集群网络拓扑从破坏性事件中恢复的一般能力。然而，它无法帮助管理员或指挥官在决定集群是否能够完成其分配的任务方面做出决策。因此，单个破坏-恢复事件的韧性应反映每次单个事件后系统性能与标准系统性能之间的差异。因此，有必要为无人机集群开发一个适当的韧性指标，以评估其完成分配任务的能力。

# 1.3. 研究组织

如前述文献综述所述，有必要为无人机集群开发一个更现实的改进模型和韧性指标，以便在任务操作中进行决策支持和无人机集群的最佳设计。在本研究中，基于使用无标度网络的无人机集群报告模型，我们通过结合无人机之间的动态距离效应，提出了一个改进的无人机集群模型。此外，报告的韧性指标进一步改进，以反映集群在每次单个事件后的性能与标准系统性能之间的差异。本研究的其余部分组织如下。第2节提出了一个考虑无人机之间动态距离效应的改进无人机集群模型。第3节基于改进的无人机集群模型提出了任务导向的韧性指标。第4节基于多智能体仿真进行案例研究，随后进行比较和讨论。第5节总结本研究。

# 2. 改进的无人机集群模型

在本节中，通过结合无人机之间动态距离的影响，提出了一种改进的无人机集群模型。该模型有两个改进点。首先，基于考虑节点间距离影响的现有方程，提出了一种改进的方程，该方程结合了节点间通信限制的影响，并避免了生成孤立簇和/或节点。其次，提出了处理无人机间距离动态变化机制，并将其整合到提出的模型中。在2.1节中，我们简要介绍了考虑节点间距离影响的现有网络模型，并讨论了它们的局限性。2.2节详细介绍了结合节点间动态距离影响的提出模型的发展，随后是实验验证。处理无人机间距离动态变化机制的细节在2.4节中提供。

# 2.1.基础知识

在Tran等人 [2-4], 中, 初始网络拓扑使用具有优先连接算法的无标度网络生成。例如, 给定初始时完全连接节点的数量对应于 $\mathrm{m}_{0}$ , 新节点j创建 $< = \mathrm{mm} \mathrm{m}()_{0}$ 个链接到现有节点, 其中节点j与现有节点i建立链接的概率如下:

$$
P _ {j \rightarrow i} = \frac {k _ {i}}{\sum_ {l = 1} ^ {N _ {t}} k _ {l}}, \tag {1}
$$

其中 $\mathrm{N}_t$ 表示网络中当前的节点数量， $\mathbf{k}_i$ 表示节点 $i$ 的自由度。

同样地，网络恢复是通过优先模式下的链路重连实现的，其中节点j（即与丢失节点相连）重连剩余节点i的概率与公式(1)相同。

同样地，网络恢复是通过优先模式下的链路重连实现的，其中节点j（即与丢失节点相连）重连剩余节点i的概率与公式(1)相同。

基于优先连接模型[6]，，Barthelemy[7],Barrat等人[8]，以及Manna和Sen[9,10]基于以下公式，针对优先附著概率函数提出了不同的距离函数和调整因子：

$$
P _ {j \rightarrow i} = \theta k _ {i} F \left(d _ {j \rightarrow i}\right), \tag {2}
$$

其中 $\theta$ 表示调整因子， $\mathbf{k}_i$ 表示节点 $i$ 的自由度， $\mathrm{F}(\cdot)$ 表示表示地理距离对无人机之间数据传输的连通性和可靠性的影响的距离函数，以及 $\mathrm{d}j \rightarrow \mathrm{i}$ 表示节点 $j$ 和 $i$ 之间的距离。

Barthelemy [7] 通过结合调整参数和距离函数，根据以下公式，考虑了复杂网络模型中节点之间的距离效应。

$$
P _ {j \rightarrow i} = \theta k _ {i} F \left(d _ {j \rightarrow i}\right) = \frac {1}{\sum_ {l} e ^ {- d _ {j \rightarrow l} / r _ {\mathrm {c}}}} k _ {i} e ^ {- d _ {j \rightarrow i} / r _ {\mathrm {c}}}, \tag {3}
$$

其中， $\mathrm{k}_i$ 表示节点i. $\mathrm{d}_j\rightarrow \mathrm{l}$ 的**自由度**， $\mathrm{d}_j\rightarrow \mathrm{l}$ 表示节点j与先前连接的节点l之间的距离， $\mathrm{r_c}$ 表示**通信范围**， $\mathrm{d}_j\rightarrow \mathrm{i}$ 表示节点j与i之间的距离。

Barrat等人 [8]在 [7]中通过考虑带权重的节点改进了模型，其依据如下方程：

$$
P _ {j \rightarrow i} = \theta s _ {i} ^ {w} F \left(d _ {j \rightarrow i}\right) = \frac {1}{\sum_ {l} s _ {l} ^ {w} e ^ {- d _ {j \rightarrow l / r _ {c}}}} s _ {i} ^ {w} e ^ {- d _ {j \rightarrow i / r _ {c}}}, \tag {4}
$$

其中 $\mathbf{s}_i^w$ 表示节点 $i$ 的权重， $\mathrm{d}_j\rightarrow 1$ 表示节点j和前一个链接节点l之间的距离， $\mathbf{r_c}$ 表示通信范围， $\mathrm{d}_j\rightarrow \mathrm{i}$ 表示节点j和i之间的距离。

Manna和Sen [9] 提出了一种不同的距离函数，并将调整因子整合到优先连接概率函数中，如下所示：

$$
P _ {j \rightarrow i} = \theta k _ {i} ^ {\beta_ {k}} F \left(d _ {j \rightarrow i}\right) = \theta k _ {i} ^ {\beta_ {k}} d _ {j \rightarrow i} ^ {\gamma}, \tag {5}
$$

其中 $\theta$ 表示调整因子， $\beta_{k}$ 表示自由度调整因子， $\gamma$ 表示距离调整因子， $k_{i}$ 表示节点 $i$ 的自由度， $d_{j} \rightarrow i$ 分别表示节点 $j$ 和节点 $i$ 之间的距离。三种调整因子的影响在 [10] 中进行了讨论。

在上述研究中，节点的优先连接概率受候选节点距离的影响，具体表现为函数 $\mathrm{F}(\mathrm{d}_j\rightarrow \mathrm{i})$ 。如图1(a)所示，根据公式(2)-(4)，由于其指数形式，当距离增加时， $\mathrm{F}(\mathrm{d}_j\rightarrow \mathrm{i})$ 会迅速下降，而调整因子很难对其进行修改。此外，如图1(b)所示，根据公式(2)和(4)，当节点的自由度为0时，其优先连接概率也为0。因此，已报告的模型[7-10]生成的网络可能包含孤立簇和节点。

# 2.2.改进模型

一个无人机集群是完全自组织和自适应的，因此其感知和行动基于无人机之间的局部交互。鉴于每个单个无人机表现出有限的能力，如果存在孤立簇和/或节点，则集群的联合能力将显著降低。因此，我们提出了一种用于无人机集群初始网络拓扑生成的新模型，并且不太可能生成孤立簇和/或节点。

图2显示了无人机集群的初始网络拓扑生成。考虑到初始时完全连接的节点数对应于一个新的节点j，j创建 $< = \mathrm{mm}(\cdot)_{0}$ 个链接到现有节点，其中节点j与现有节点i建立链接的概率如下：

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/28f09852559e702f3eca02d13e44bdd156920675eed49b67174dd78bb8c17e1c.jpg)



(a) Isolated cluster generation


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/f409de3ffd3a8436e492e5927bee1695de881a7bb4523c0f1d4addf769983650.jpg)



(b) Isolated node generation



图1。使用已报告的模型生成孤立簇和节点


$$
P _ {j \rightarrow i} = \alpha \left(k _ {i} + \varepsilon\right) F \left(d _ {j \rightarrow i}\right) = \left\{\begin{array}{l}\frac {\left(k _ {i} + \varepsilon\right) F \left(d _ {j \rightarrow i}\right)}{\sum_ {l = 1} ^ {N _ {t}} F \left(d _ {j \rightarrow l}\right)\left(k _ {l} + \varepsilon\right)}, \sum_ {l = 1} ^ {N _ {t}} F \left(d _ {j \rightarrow l}\right) > 0\\0, \text {o t h e r w i s e}\end{array}, \right. \tag {6}
$$

其中 $\mathrm{N}_t$ 表示网络中当前的节点数， $\varepsilon$ 表示调整因子， $\mathbf{k}_i$ 表示节点 $i$ 的自由度。

函数 $\mathrm{F}(\mathrm{d}_j\rightarrow \mathrm{i})$ 定义如下：

$$
F \left(d _ {j \rightarrow i}\right) = \left\{\begin{array}{l}1, d _ {j \rightarrow i} <   \eta \mathrm {r} _ {c}\\\frac {\left(\mathrm {r} _ {c} - d _ {j \rightarrow i}\right)}{\left(1 - \eta\right) \mathrm {r} _ {c}}, \eta \mathrm {r} _ {c} \leq d _ {j \rightarrow i} <   \mathrm {r} _ {c},\\0, d _ {j \rightarrow i} \geq \mathrm {r} _ {c}\end{array}\right. \tag {7}
$$

其中 $r_c$ denotes 表示通信范围， $d_j \rightarrow i$ 表示节点 $j$ 和 $i$ 之间的距离， $\eta$ 表示距离影响因子。需要注意的是，当 $\sum_{l=1}^{N_l} F(d_{j \rightarrow l}) = 0$ 时，节点 $j$ 连接所有现有节点的概率对应于 0，这意味着节点 $j$ 的最大通信范围内存在节点。在这种情况下，节点 $j$ 保持活跃状态，直到新加入的节点或少数节点出现在节点 $j$ 的通信范围内。

在网络恢复方面，节点j（其连接的节点(们)丢失）重新连接剩余节点i的概率与公式(6)相同。函数 $F(d_{j\rightarrow i})$ 与公式(7)相同。表1总结了

# 表1


所提出的方程与现有方程的比较


<table><tr><td>Name</td><td colspan="2">Equation</td></tr><tr><td>Barthelemy [7]</td><td colspan="2">Pj→i = θkiF(dj→i) = 1/∑l e−dj→l/rckl e−dj→i/rc,</td></tr><tr><td>Barrat et al. [8]</td><td colspan="2">Pj→i = θsiwF(dj→i) = 1/∑l siw e−dj→l/rscsiw e−dj→i/rc,</td></tr><tr><td>Manna and Sen [9]</td><td colspan="2">Pj→i = θkiβkF(dj→i) = θkiβk dj→i,</td></tr><tr><td>Proposed equation</td><td colspan="2">Pj→i = α(ki + ε)F(dj→i) = (ki + ε)F(dj→i)/∑l=1Nt F(dj→l)(kl + ε), ∑l=1Nt F(dj→l) &gt; 0</td></tr><tr><td></td><td>0,</td><td>otherwise</td></tr><tr><td></td><td>1,</td><td>dj→i &lt; ηrc</td></tr><tr><td></td><td>F(dj→i) = {rc - dj→i}/(1 - ηrc},</td><td>ηrc ≤ dj→i &lt; rc</td></tr><tr><td></td><td>0,</td><td>dj→i ≥ rc</td></tr></table>

所提出的和现有公式。

我们通过以下实验将提出的模型与其他已报告的模型进行比较来说明该模型。无人机的网络拓扑结构是使用四个模型生成的，即

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/cccd2ca55615851252010fd131f020c0c1223eccd7ca91c82b4bca4fe66b6ec0.jpg)



图2。无人机集群的初始网络拓扑生成



表2 实验参数。


<table><tr><td>参数</td><td>含义</td><td>值</td></tr><tr><td>N</td><td>网络大小</td><td>100</td></tr><tr><td>m0</td><td>初始网络中的节点数</td><td>2</td></tr><tr><td>m</td><td>新添加的链路数</td><td>1</td></tr><tr><td>rc</td><td>通信范围</td><td>100</td></tr><tr><td>βk</td><td>自由度调整因子</td><td>0.8</td></tr><tr><td>γ</td><td>距离调整因子</td><td>-5</td></tr><tr><td>ε</td><td>调整因子</td><td>0.1</td></tr><tr><td>η</td><td>距离影响因子</td><td>0.8</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/78bb0155290adcfa1384bd0e7577201dba261de19b10d002f52394bbbdd47273.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/53ff7b94681e7a00e8f32c1f570c46821848592b33cde72b6f7879b87af2cd88.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/335c2950ae3ae4cf67d49b251e91143d02a12da07ccc4e132fb487f380b7740b.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/9e4eee0ba4a0a7f6264f8507a1cca0fc129f150399905f61bfff25fa228c484c.jpg)



(d)



图3。使用(a) [7], (b) [8], (c) [9], 和(d)提出的模型生成的网络。


Barthelemy [7], Barratet al. [8], Manna和Sen [9,10], 以及提出的模型。参数见表2。每个生成的网络中节点的位置是相同的。实验用 $\mathrm{C} + +$ 编码，并在OpenCV [21]中绘制。

结果如图3所示。如图所示，使用Barthelemy [7], Barrat等人[8], 和Manna和Sen [9] 模型生成的网络包含孤立簇和节点。相反，使用提出的模型生成的网络不包含任何孤立簇和节点。

# 2.3. 相对距离的动态变化

在2.1节中引入的已报告模型未考虑每对无人机之间的动态变化。无人机集群高度机动化，因此每对无人机之间的相对位置随时间变化。因此，无人机集群的拓扑结构在任务期间可能经历快速变化。为无人机集群开发了一种处理动态变化的机制，如图4所示。如图所示，当两架无人机之间的距离超过通信范围r时，相应的链路会被移除。主机节点（被移除链路所属的节点）根据公式(6)-(7)重新连接链路。需要注意的是，当 $\sum_{l=1}^{N_t} F(d_{j\rightarrow l}) = 0$ 时，节点j链接所有现有节点的概率对应于0。在这种情况下，节点j保持活动状态，直到其他节点移动到其通信范围内。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/dc540c4d0a95b7538e79d22f7aa7e2c5fe8a8f2c03706a589ba480c8412e3507.jpg)



图4。无人机集群动态变化处理机制


# 3. 无人机集群的任务导向韧性指标

在本节中，基于已报告的韧性指标，开发了一种任务导向的无人机集群韧性指标。通常，韧性评估方法包括系统性能指标选择和韧性指标构建。在3.1节中，我们讨论了系统性能指标选择。在[3,17]中讨论了已报告的韧性指标及其局限性。3.3节讨论了改进的韧性指标。

# 3.1.系统性能指标

回顾一下，无人机集群通过信息共享和交互以自组织和自适应的方式执行任务。因此，我们关注信息交换能力作为无人机集群的系统性能。在研究中，我们使用与Tran等人[2,17]，中详细描述的相同系统性能指标，这表示无人机集群中接收到的总信息。

每个无人机定期生成信息，并通过最短路径将其发送到目标无人机。每个无人机在时间t生成的信息的概率如下[2]：

$$
\mu_ {t} = \frac {\mu_ {0} N}{N _ {t}}, \tag {8}
$$

其中 $\mu_0$ 表示初始信息生成概率，N表示无人机总数， $\mathrm{N}_t$ 表示当前无人机数量。Tran [2]将无人机集群在时间t的IE网络中接收到的总信息数定义为系统性能。这是因为每条信息的最短路径长度降低了无人机集群信息交换的实时性能。IE网络中接收到的总信息数如下[2]:

$$
y (t) = \sum_ {i = 1} ^ {N _ {t}} \sum_ {j = 1} ^ {R _ {i} (t)} \Delta^ {d _ {j} ^ {i}}, \tag {9}
$$

where $\mathrm{Rt}(.)_{i}$ 表示节点 $i$ 接收到的信息数量， $\mathrm{d}_j^i$ 

表示通过最短路径算法（例如迪杰斯特拉算法[19]）获得的最短路径长度，对于节点i接收到的 $\mathrm{j}_{th}$ 消息）， $\mathrm{N}_t$ 表示当前无人机数量， $\Delta$ 表示时间敏感因子。 $\Delta$ 的范围对应于 $0 < \Delta \leq 1$ ，并根据任务要求给出。 $\Delta = 1$ 当忽略实时性能时。这是因为每个无人机的信息生成是一个随机变量。Tran [2]使用多次模拟来获得y(t)的平均原始值。Savitzky-Golay(S-G)滤波器[18]进一步应用于计算y(t)的平滑值。

# 3.2.报告的韧性指标

给定系统性能指标，下一步涉及开发一个适当的韧性指标。Tran等人 [3] 提出了一种在多个中断情况下评估系统韧性的方法，该方法用于无人机集群的韧性评估。报告的方法主要有两个步骤。首先，通过公式 [3] 计算每个中断-恢复事件的韧性，如下所示：

$$
S _ {i} = \left\{ \begin{array}{l l} \sigma \rho [ \delta + \varsigma + 1 - \tau^ {\rho - \delta} ], & \text {i f} \rho \geq \delta \\ \delta \rho (\delta + \varsigma), & \text {o t h e r w i s e} \end{array} , \right. \tag {10}
$$

其中 $\sigma$ 、 $\delta$ 、 $\rho$ 、 $\tau$ 和 $\zeta$ 分别表示性能因子、吸收因子、恢复因子、恢复时间因子和波动因子。这些因子通过中断前和恢复后的相应能力之比计算得出，如下 [3]:

如图5所示，我们假设 $\mathrm{y}_D$ 、 $\mathrm{y}_{\mathrm{min}}$ 和 $\mathbf{y}_R$ 分别表示中断前、恢复前和恢复后的 $\mathrm{y(t)}$ 。

给定单个事件的周期 $\left[\mathrm{t}_{0},\mathrm{t}_{\text {final }}\right]$ ，令 $t_{th}$ 、 $t_{\min}$ 和 $t_{ss}$ 分别表示中断发生时、系统在中断后稳定时和恢复开始时的时间。因此，我们得到以下表达式：

$y_{D} = \frac{\sum_{t_{0}}^{th}y(t)}{t_{th} - t_{0}},\quad y_{\min} = \frac{\sum_{t_{\min}}^{ts}s}{t_{ss} - t_{\min}},\quad y_{R} = \frac{\sum_{t_{ss}}^{tfinal}y(t)}{t_{final} - t_{ss}},\quad \sigma = \frac{\sum_{t_{0}}^{t_{final}}y(t)}{y_{D}(t_{final} - t_{0})},$ $\delta = \frac{y_{\mathrm{min}}}{y_D}$ $\tau = \frac{t_{ss} - t_0}{t_{final} - t_0},\rho = \frac{y_R}{y_D}$ and $\zeta = \frac{1}{1 + \exp[-0.25(SNR_{dB} - 15)]}$ The calcula-信噪比（SNRdB）的定义在[18]中给出。

其次，给定每个中断-恢复事件的韧性，系统总韧性表示为以下公式[3]:

$$
S _ {t o t a l} = \sum_ {i = 1} ^ {N _ {t h r e a t}} \frac {w _ {S} ^ {i}}{\sum_ {j = 1} ^ {N _ {t}} w _ {S} ^ {j}} S _ {i}, \tag {11}
$$

其中 $w_{R}^{i} = (1 - \beta)^{N_{t} - i}$ 表示 $\mathrm{i}_{th}$ 事件的权重， $\beta$ 表示

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/82a49c67ab130272b7076890e7014e5a9101ca8d55bb942a74573f5ce00e0e5f.jpg)



图5. $\mathrm{y}_D,\mathrm{y}_{\min},\mathrm{y}_R,\mathrm{t}_0,\mathrm{t}^{final},\mathrm{t}_{th},\mathrm{t}_{\min},$ 和 $\mathrm{t_{ss}}$ 的示意图。


权重因子， $\mathrm{N}_{\text {threat }}$ 表示中断-恢复事件的数量，而 $\mathrm{N}_t$ 表示当前无人机数量。

# 3.3. 改进的韧性指标

然而，公式(10)中的因素是基于中断前和恢复事件后的相应能力比率计算的，这对于无人机集群可能不合适。无人机集群的最终目标是完成分配的任务。存在一个合格的标准系统性能来完成分配的任务。因此，每个中断-恢复事件的韧性应反映每次事件后系统性能与标准系统性能之间的差异。因此，基于[3]中的韧性指标，我们提出一个新的韧性度量方法如下。

首先，通过一个综合无人机集群多个关键性能因素的函数获得每个破坏-恢复事件的韧性值，其中每个因素是通过每次事件后系统性能与标准系统性能之间的差异获得的。我们修改方程以获得因子 $y_{D}$ ，如下所示：

$$
\bar {y _ {D}} = \mu_ {t} N _ {t} = \left(\mu_ {0} \frac {N}{N _ {t}}\right) N _ {t} = \mu_ {0} N, \tag {12}
$$

其中 $\mu_0$ 表示初始信息生成概率，N表示无人机总数。根据公式(12)， $\mathrm{y}_D$ 对应于 $N_{t} \geq \mu_{0} N$ （表示标准系统性能）时 $\mathrm{y}(t)$ 的期望值。根据 $\mathrm{y}_D$ 吸收因子定义如下：

$$
\bar {\rho} = \frac {y _ {R}}{\bar {y} _ {D}}. \tag {13}
$$

关于恢复时间因子，从中断发生的时间开始更为合适。因此，恢复时间因子定义如下：

$$
\bar {\tau} = \frac {t _ {\mathrm {s s}} - t _ {\mathrm {m i n}}}{t _ {\text {f i n a l}} - t _ {\mathrm {m i n}}}, \tag {14}
$$

其中与 $\tau$ 的区别在于 $\mathbf{t}_0$ 被替换为 $\mathrm{t}_{\mathrm{min}}$ 。根据上述公式，性能因子定义如下：

$$
\bar {\sigma} = \frac {\sum_ {t _ {\operatorname* {m i n}}} ^ {t _ {\text {f i n a l}}} y (t)}{\overline {{y _ {D}}} \left(t _ {\text {f i n a l}} - t _ {\operatorname* {m i n}}\right)}, \tag {15}
$$

给定新定义的因子，每个中断-恢复事件的弹性按与公式(10)类似的方式计算如下：

$$
\bar {S} _ {i} = \left\{ \begin{array}{l} \bar {\sigma} \bar {\rho} [ \delta + \varsigma + 1 - (\bar {\tau}) ^ {(\bar {\rho} - \delta)} ], \text {i f} \bar {\rho} \geq \delta \\ \delta \bar {\rho} (\delta + \varsigma), \text {o t h e r w i s e} \end{array} , \right. \tag {16}
$$

其次，使用与(11)相同的方程计算总弹性。表3总结了所提出的弹性度量方法和现有方法。

如前所述的步骤所示，所提出的弹性度量方法捕捉了集群当前性能与其标准系统性能之间的差异，这反映了集群适应破坏性事件和恢复其预期性能的能力，同时也反映了集群完成其分配任务的能力。

# 4. 案例研究

在本节中，基于多智能体仿真进行了一项案例研究，其中调用无人机游泳在受控区域执行监视任务。我们将提出的模型和韧性指标与Tran等人提出的进行比较[2,17]。在4.1节中，我们介绍了任务背景和


表3



所提出的韧性度量与现有度量的比较。


<table><tr><td>差异</td><td>所提出的韧性度量</td><td>报告韧性度量 [3]</td></tr><tr><td rowspan="3">不同</td><td>= σρ [δ + s + 1 - τ f-δ] σ ≥ δ S{()，如</td><td rowspan="2">= {σρ[δ + s + 1 - τf-δ] σ ≥ δ S if ()</td></tr><tr><td>- δσ ψ δ + s</td></tr><tr><td>果()，否则i()}</td><td>otherwise</td></tr><tr><td>不同</td><td>yD = μtNt = (μ0Nt)Nt = μ0N</td><td>yD = Σtth y(t)/Σtth - t0</td></tr><tr><td rowspan="2">same</td><td>ymin = Σtmin y(t)/ts - tmin</td><td>yD = y ttss y t</td></tr><tr><td>yR = Σtfinal y(t)/tfinal - ts</td><td>tss tmin min() min</td></tr><tr><td>same</td><td>yR = Σtfinal y(t)/tfinal - ts</td><td>yR = Σtfinal y(t)/tfinal - ts</td></tr><tr><td>不同</td><td>σ = Σtfinal y(t)/yD(tfinal - tmin)</td><td>σ = Σt0 y(t)/yD(tfinal - t0)</td></tr><tr><td>same</td><td>δ = ymin yD - ts</td><td>δ = ymin yD</td></tr><tr><td>不同</td><td>t tfinal tmin min</td><td>τ = ts - t0 / tfinal - t0</td></tr><tr><td>不同</td><td>ρ =</td><td>ρ =</td></tr><tr><td rowspan="2">same</td><td>yR yD = 1 + [-0.25 - 15]</td><td>yR yD = 1 + [-0.25 - 15]</td></tr><tr><td>SNRdB指数.]</td><td>SNRdB指数.]</td></tr><tr><td>不同</td><td>Stotal = Σl=1Nthreat wS^l/ΣNi j=1wS^j S_l</td><td>Stotal = Σl=1Nthreat wS^l/ΣNi j=1wS^j S_l</td></tr></table>

实验设置。4.2节详细介绍了仿真结果、比较和讨论

# 4.1. 任务背景和实验设置

任务背景与[4]相似。一架无人机游泳被调用，以在图6所示的指定战场上执行监视任务。一架武器飞机在安全区内释放N架相同的无人机。无人机使用公式(6)和(7)形成初始网络拓扑，并向战场移动。无人机集群的目标是覆盖整个战场，以最小化盲区。信息交换能力（即每个时间步长接收的总信息量）被用作无人机集群的系统性能。其他背景信息如下：

- 群中有 N 个相同无人机，任务是保持对战场的感知。每个无人机在战场上以蛇形搜索模式移动。每个无人机通过多跳无线通信接收和发送关于探测到的对手和其他无人机的位置信息。无人机均匀分布在战场上以保持对战场的感知。当无人机探测到其探测范围内的其他无人机时，它会转身向相反方向移动。

- 有 M 个具有防御能力的相同地面对手。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/80be93c69347b4bad5db6eb8407a9cbb403b61d601a3c0e719c177b13a889ee8.jpg)



图6。在指定战场上进行的监视任务


攻击以 $\mathrm{T}_{\text {threat }}$ 的时间步长发生。每次攻击以目标方式移除无人机，其中在每次威胁事件中移除具有更多邻居数的节点(们)。移除的无人机数量对应于 $\mathrm{m}_{d}$ 。当出现平局时，将任意打破。在tadapt之后，无人机集群开始重连。网络恢复通过使用公式(7)和(8)的链路重连来实现。

- 战场对应于一个大小为 $S = 500 \times 600$ 的矩形网格。网格的单位是一个区域。无人机的移动速度为 vuav 区域/秒，地面对手的速度对应于 vepatch/秒。

- 为了比较, 无人机的通信范围 rc 设置为 $\infty$ 、100/区域、150/区域、200/区域、250/区域。对于 $= \infty \mathrm{rc}$ 的情况表示 Tran 等人 [2,3] 中的情况。需要注意的是, 不同的无人机通信范围会产生不同的集群网络拓扑。因此, 不同的无人机通信范围代表了不同的集群网络拓扑。

基于代理的模型用于无人机集群和背景设置在Anylogic [20]中开发。模拟在第一个10个中断-恢复事件后终止。模拟的复制次数对应于 $\mathrm{N}_{\mathrm{s}}$ 。最短路径长度d通过迪杰斯特拉算法[19]获得。任务和无人机的参数设置在表4中。

# 4.2.结果和讨论

首先，我们通过公式(11)获得每次运行中接收到的总信息数，y(t)。随后，我们获得y(t)的平均原始值，并应用S-G滤波器以获得y(t)的平滑值。在不同无人机通信范围，rc，下的结果如下


表4



实验参数。


<table><tr><td>参数</td><td>值</td><td>参数</td><td>值</td></tr><tr><td>N</td><td>50</td><td>md</td><td>2</td></tr><tr><td>M</td><td>20</td><td>η</td><td>0.8</td></tr><tr><td>Threat</td><td>200</td><td>μ0</td><td>0.5</td></tr><tr><td>t适应</td><td>100</td><td>Ns</td><td>100</td></tr><tr><td>νuav</td><td>1</td><td>[θ0, tfinal]</td><td>[0, 2300]</td></tr><tr><td>νe</td><td>0.3</td><td>N威胁</td><td>10</td></tr><tr><td>m0</td><td>2</td><td>β</td><td>0.2</td></tr><tr><td>m</td><td>1</td><td>Δ</td><td>0.9</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/d1ad2712391c4283df4bdc753913e592e169aaa17e497d4a0d880c9f5a66ffb6.jpg)



图7.在不同的无人机通信范围下的y(t)。


图7。如图所示，y(t)在每个时间点都随着rc的增加而增加。信息交换能力y(t)表示无人机集群的性能，并且随着无人机通信能力的提高而提高。当 $r_c = \infty$ 时，该案例表示Tran等人[2-4]，中使用的模型，并且y(t)保持在标准性能附近，即 $\mu_0N = 25$ 。图7中的结果验证了所提出的无人机集群模型可以用于捕获无人机之间动态距离对无人机集群系统性能的影响。

需要注意的是，第一个中断-恢复事件中的y(t)相对其他事件较高。这是因为无人机在战场上分布不均匀。在每种通信范围内，y(t)在其余八个中断-恢复事件中保持稳定。此外，在每种通信范围内，y(t)也保持稳定。具体解释如下。根据公式(8)，当 $N_{t}$ 减少时， $\mu_{t}$ 增加。因此，在最初几个中断中，无人机集群的性能不受影响。这显示了集群的优势，即系统能够承受某些外部威胁和中断。

其次，给定 $y(t)$ ，我们采用Tran等人[3]，中提出的韧性指标，该指标对应于公式(10)，以获得在不同无人机通信范围 $r_c$ 下每个中断-恢复事件的韧性。如图8所示，在不同的无人机通信范围 $r_c$ 下，韧性值没有明显差异。因此，韧性指标未能反映无人机集群（这表示信息交换能力）的性能随无人机通信能力增强而提高的趋势，如图7所示。这是因为Tran等人[3]报道的韧性指标是基于恢复后的相应能力与中断前的相应能力之比计算的。因此，韧性是一个相对值，与标准系统性能无关。此外，给定每个无人机通信范围 $r$ [3]，即使经过前两个中断-恢复事件后，韧性指标也不稳定。

该指标是根据恢复后的相应能力与中断前的相应能力之比计算的。因此，韧性是一个相对值，与标准系统性能无关。此外，给定每个无人机通信范围 $r_c$ ，即使经过前两个中断-恢复事件后，韧性指标也不稳定。

第三，我们应用提出的韧性指标（对应公式(16)）来获取在不同无人机通信范围r下每个中断-恢复事件的韧性。结果如图9所示。如图9所示，不同无人机通信范围r下的韧性值存在明显差异。因此，提出的韧性指标反映了无人机集群性能（即信息交换能力）随着无人机通信能力增加的趋势，如图7所示。这是因为提出的韧性指标反映了每次事件后系统性能与标准系统性能之间的差异。因此，随着通信范围r的增加，韧性增加，因为系统性能随着通信范围r的增加而提高。此外，除了对应 $= \infty$ r的情况外，第一个中断-恢复事件的韧性较高，并在每种通信范围内其余九个中断-恢复事件中保持稳定。

最后，我们使用公式(11)根据Eqs. (10)和(16)计算出的每个中断-恢复事件的韧性值，得到系统总韧性。结果如图10所示。如图所示，在不同无人机通信范围r{v1}下，提出的韧性指标得到的韧性值存在明显的上升趋势。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/3413deefb0b0efbdfb3a1c947f593809052260f2353f6c55c825f09df06c853c.jpg)



图8.基于Tran等人[3]的每个事件的弹性。


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/1580f833db1b4da4f9027480015be4f9bedef080c44e138193def9b035acea1e.jpg)



图9.基于提出的方法的每个事件的弹性


该结果与无人机集群具有更好的通信能力表现出更好的系统韧性的事实一致，并增强了无人机集群在指定战场完成分配的监视任务的能力。相反，Tran等人[3]使用公式(13)没有这种趋势。

提出的模型和指标可用于支持无人机集群的任务规划和设计。例如，基于上述结果，管理员或指挥官确定集群所需无人机数量以实现所需的弹性，这最终有助于无人机集群完成分配的任务。此外，在无人机集群设计阶段，可以在所需弹性要求下，在通信能力和相应成本之间进行权衡。

# 5.结论

鉴于其无线通信能力的局限性，无人机的连通性和数据传输可靠性受每对无人机之间距离的影响。此外，无人机是便携的，在任务期间无人机之间的物理距离会动态变化。因此，基于无人机集群的已报告模型，我们通过引入无人机之间距离及其动态变化的影响，提出了一种改进的无人机集群模型。使用该模型生成的网络不太可能包含孤立簇和节点。此外，还引入了一种处理动态变化的机制。不可预测的威胁和不可避免的破坏性事件是故障的主要原因。因此，设计了一种无人机集群来适应破坏性事件并恢复其性能。因此，基于改进的无人机集群网络模型，提出了一种改进的韧性指标，该指标反映了集群在每次事件后的性能与其标准系统性能之间的差异。

不可预测的威胁和不可避免的破坏性事件是故障的主要原因。因此，设计了一种无人机集群来适应破坏性事件并恢复其性能。因此，基于改进的无人机集群网络模型，提出了一种改进的韧性指标，该指标反映了集群在每次事件后的性能与其标准系统性能之间的差异。

案例研究表明，无人机集群的性能在最初几次中断期间保持稳定。这表明集群的优势在于系统能够承受某些外部威胁和中断。与传统网络可靠性指标相比，提出的韧性指标捕捉了无人机集群的主要优势（即适应破坏性事件），并在系统重构和/或重组方面保留了其预期性能以完成分配的任务。此外，在不同无人机通信范围内，提出的韧性指标获得的韧性值呈上升趋势， $\mathbf{r}_{\mathrm{c}}$ 。结果表明，具有更好通信能力的无人机集群表现出更好的系统韧性。这增强了无人机集群在指定战场完成分配的监视任务的能力。与无人机集群的报告韧性指标相比，提出的韧性指标反映了无人机集群性能（即信息交换能力）随无人机通信能力增加的趋势。

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/7d303c07-2632-48b9-bd7b-2a8de415403c/4eb36a5c60d5ee15776401734a298ae0113e75e92b20097b0f5f9f1d0954e15f.jpg)



图10.基于提出方法的每个事件的弹性


在该研究中，我们关注由外部威胁和中断（如对手的恶意攻击）引起的无人机故障。我们没有考虑节点（无人机）因自身故障而导致的故障，即我们承认每个无人机的可靠性对应于1。然而，在冲突环境中，无人机也可能因自身故障而失效。我们计划在未来的研究中纳入节点的可靠性。此外，无人机集群高度机动化，无人机集群的拓扑结构在任务期间可能经历快速变化。因此，无人机速度也会影响无人机集群拓扑结构变化的频率。我们计划在未来的研究中检验不同无人机速度对无人机集群韧性的影响。

# 致谢

本研究由国家自然科学基金（资助号71701207和51705526）和国家可靠性与环境工程重点实验室资助。

# 参考文献



[1] Li Y, St-Hilaire M, Kunz T. Improving routing in networks of UAVs via scoped flooding and mobility prediction. IEEE; 2013. Wireless Days. 





[2] Tran HT. A complex networks approach to designing resilient system-of-systems[D]. Georgia Institute of Technology; 2016. 





[3] Tran HT, Domercant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Procedia Comput Sci 2016;95:126-33. 





[4] Tran HT, Domercant JC, Mavris DN. Evaluating the agility of adaptive command and control networks from a cyber complex adaptive systems perspective. J Defense Model Simul 2015;12(4). 





[5] Barabasi AL, Albert R. Emergence of scaling in random networks. Science 1999;286(5439):509. 





[6] Barabasi AL, Albert R, Jeong H. Mean-field theory for scale-free random networks. Phys A Stat Mech Appl 1999;272(1-2):173-87. 





[7] Barthelemy M. Crossover from scale-free to spatial networks. Europhys Lett 2002;63(6):915. 





[8] Barrat A, Barthelemy M, Vespignani A. The effects of spatial constraints on the evolution of weighted complex networks. J Stat Mech Theory Exp 2005;2005(05):799-803. 





[9] Manna SS, Sen P. A-059: modulated scale-free network in euclidean space. Phys Rev E Stat Nonlinear Soft Matter Phys 2002;66(2):066114. 





[10] Sen P, Banerjee K, Biswas T. Phase transitions in a network with a range-dependent connection probability. Phys Rev E 2002;66(3):037102. 





[11] Labaka L, Hernantes J, Sarriegi JM. Resilience framework for critical infrastructures: an empirical study in a nuclear plant. Reliab Eng Syst Saf 2015;141:92-105. 





[12] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35-53. 





[13] Biggs R, Schlitter M, Biggs D, Bohensky EL, Burnsilver S, Cundill G, et al. Toward principles for enhancing the resilience of ecosystem services. Soc Sci Electron Publ 2012;37:421-48. 





[14] Hipsey MR, Hamilton DP, Hanson PC, Carey CC, Coletti JZ, Read JS. Predicting the resilience and recovery of aquatic systems: a framework for model evolution within environmental observatories. Water Resour Res 2015;51(9):7023-43. 





[15] Henry D, Ramirez-Marquez JE. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99:114-22. 





[16] Hosseini S, Barker K, Ramirez-Marquez JE. A review of definitions and measures of system resilience. Reliab Eng Syst Saf 2016;145:47-61. 





[17] Tran HT, Balchanos M, Domercant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng & System Safety 2017;158:73-84. 





[18] Schafer RW. What is a savitzky-golay filter? IEEE Signal Process Mag 2011;28(4):111-7. 





[19] Dijkstra EW. A note on two problems in connexion with graphs. Numerische Mathematik 1959;1(1):269-71. 





[20] Borschchev A. Multi-method modelling: AnyLogic. Discr-Event Simul Syst Dyn Manag Decis Mak 2014. 





[21] Bradski G., Kaehler A. Learning openCV, 1st Edition. O'Reilly Media, Inc. 2008. 





[22] Ouyang M, Zhenghua W. Resilience assessment of interdependent infrastructure systems: With a focus on joint restoration modeling and analysis. Reliab Eng Syst Saf 2015;141:74-82. 





[23] Ball MO, Colbourn CJ, Provan JS. Network reliability. Handbook Oper Res Manag Sci 1995;7:673-762. 

