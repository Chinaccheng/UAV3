# A Multistate Network Approach for Resilience Analysis of UAV Swarm Considering Information Exchange Capacity

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/a61a5ffebee7f9be49f28533c38a933ffed537fd65f327df440df88c49015fc1.jpg)


Tao Liu a,b, Guanghan Bai a,\*, Junyong Tao a, Yun-An Zhang a, Yining Fang a 

$^{a}$ Laboratory of Science and Technology on Integrated Logistics Support, College of Intelligence Science and Technology, National University of Defense Technology, Changsha, 410073, China 

$^{b}$ School of Mechanical Engineering, Xihua University, Chengdu, 410000, PR China 

# ARTICLEINFO

# Keywords:

UAV swarm 

multistate network 

resilience 

information exchange network 

resilient behavior 

# ABSTRACT

Unmanned aerial vehicle (UAV) swarms can perform tasks in a self-organized and self-adaptive manner, and are thus appropriate for resilience research. An efficient and resilient information exchange (IE) network among drones is essential for a UAV swarm to accomplish its mission. In this study, we incorporated conditional probability into a multistate network to model the IE of a UAV swarm. Subsequently, we modeled two resilient behaviors based on the actions of the drones: formation transformation and redeployment. For the former, a semi-Markov-based model was adopted to represent the changes in the state probability distribution of the IE link during this resilient behavior. A resilience-based swarm IE topology reconstruction optimal approach for UAV redeployment strategy was presented. Finally, an application case of a UAV swarm was evaluated, for which real experiments were conducted to obtain the state distributions of the IE capacity among UAVs at different distances. The simulation results show that the proposed model and method can help gain understanding of the resilience process of a UAV swarm and can be used to select appropriate recovery strategies, further supporting mission planning and improving the resilience of UAV swarms. 

# Notations

$d$ Units of flow can be transmitted from source node to sink node. 

$QIE(t)$ Performance of swarm information exchange network at time $t$ . 

$PQ(t)$ Ideal (expected) performance of network at time $t$ 

$\overline{Q} (t)$ Minimum performance requirement for current mission. 

$R(T)$ Resilience of network at time $T$ 

MO Formation of UAV swarm. 

$T_{d}$ Time at which disturbance occurs. 

$T_{s}$ Time recovery started. 

$\Delta_{d}$ Probability that the flow from the source to the sink is not less than $d$ 

$\Lambda_{d}$ Probability that the flow from the source node to the sink node is equal to $d$ 

$p^i (t)$ State probability distribution vector of flow throughout of component $i$ 

$p b^{i}(t)$ Conditional probability distribution vector of component $i$ 

$C^i (t)$ Conditional operation probability matrix of component $i$ 

$F_{jl}^{i}(u)$ Distribution function of sojourn time $u$ in state $j$ ; the next state is $l$ . 

$\Phi_{jl}^{i}(t)$ Probability of component $i$ transitioning from state $j$ to state $l$ in time period $[0,t]$ . 

$\theta_{jl}^{i}(t)$ Probability of component $i$ transitioning from state $j$ to state $l$ at time $t$ . 

II Set of damaged UAVs. 

K Set of remaining UAVs. 

$\Gamma_{\nu}$ Set of links connected to $\nu$ 

$l_{uv}$ Shortest path of UAV $u$ and $\nu$ in original topology. 

$s$ Distance between drones. 

$\gamma$ Demand accuracy of $\Delta_{d}$ 

# 1. Introduction

Unmanned aerial vehicles (UAVs) have been widely employed in civil and military fields owing to their agility and low cost, with the benefit of allowing dull, dirty, and dangerous missions to be conducted 

without posing risks to humans. However, owing to the limited capability of a single UAV, some researchers have begun to focus on UAV swarms, i.e., a group of numerous UAVs. Recent studies have shown that the success rate of performing more complex tasks can be significantly improved using a UAV swarm rather than a single UAV [1]. 

Accordingly, abundant research has been conducted on UAV swarms such as task assignment [2,3], path planning [4-6], cooperative control [7-9], and task performance [10-12]. These studies aimed to improve the mission capabilities of UAV swarms. For a swarm with numerous agents, efficient and reliable data interactions between the agents are vital for mission accomplishment [13-16]. With the increasing scale and complexity of UAV swarms, network approaches have been used to evaluate the performance of the information exchange (IE) network for a UAV swarm [17-20]. Metrics such as robustness [21-23], reliability [15,17,24-26], and vulnerability [27,28] have been considered to evaluate the performance of such a network. These features are the critical capacities of a UAV swarm and enhance the ability of a swarm to avoid external disturbances. 

However, a UAV swarm is typically used in dirty, dangerous, and complex environments, where unpredictable threats and inevitable disruptive events may occur. In addition, UAV swarms operate in a self-organized and self-adaptive manner, hence, a swarm may perform self-healing actions when disturbances occur [19]. For example, when a UAV swarm implements a reconnaissance mission over a specified battlefield, it may be exposed to an enemy's air defense system [29]. Functional loss or degeneration of UAVs caused by disturbances may lead to changes in the IE topology, which will further deteriorate the performance of the entire swarm. In this scenario, the UAV swarm can change its formation to avoid danger and recover the performance of the IE. 

Resilience represents the ability of a system to resist disturbance, including prediction of extreme events, evaluation of the impact of events, absorption of shock, response, adaptation, and recovery [30,31]. Research on UAV swarm resilience has become popular [32-37]. A network model is a useful tool for describing systems, in which agents and relationships among UAVs are represented by nodes and arcs, respectively. Therefore, several scholars have begun to study the network resilience of UAV swarms. Tran et al. [38] applied scale-free network and random network to model the IE network of a UAV swarm, and proposed a framework for evaluating the resilience of a UAV swarm. Bai et al. [19] also modeled the IE of a UAV swarm as a complex network, further considering communication limits. Li et al. [20] considered a heterogeneous communication network of a UAV swarm and proposed a baseline resilience assessment. Cheng et al. [39] believed that a command-and-control network is essential for mission completion. This type of IE network can be described using complex network models. 

The network models mentioned above are binary networks, so the network components can only be in one of two states: total failure or perfect operation. However, the state of data flow among UAVs can differ because of various conditions including low transmission range, inter-agent distances, and extraneous noise [40]. Thus, a multistate network whose components can work in independent, discrete, finite, and multiple states is more appropriate for characterizing the IE link capacity. Xu et al. [17] first modeled the IE network of a UAV swarm as a multistate network and evaluated its reliability. The state distributions of the IE links are determined based on the accumulated time of the links at different distances during the mission. More specifically, the state distributions are statistical values for the entire mission time that are suitable for the mission reliability evaluation. 

However, to assess and analyze resilience, the time-dependent network performance should be determined. Thus, it is necessary to understand the changes in the link state distribution during the resilience process, rather than a statistical value over the entire mission time. Experiments on UAV communication have indicated that the IE may operate in different states at a fixed communication distance. Then, the state distribution can be used to represent the performance of an IE link 

at a certain communication distance. Thus, by analyzing the changes in these conditions, the performance of the IE network during the mission time can be determined. 

In addition, current research on swarm resilience assumes that the link capacity decreases to zero because of the loss of function of the disturbance agent [18-20]. The recovery of the IE link is based on rewiring the remaining UAVs. However, the effects of UAV movements in response to external disturbances on swarm resilience have rarely been studied. For example, when a swarm suffers from internal failures or external disruptions, reasonable dispersion and/or aggregation behaviors help it resist and recover from disturbances. In a biological swarm, fish disperse when they encounter a predator and return to a tight state when they are a certain distance from the predator. These types of behaviors are also common in classic swarm models, such as Boid model [41], Vicsek model [42] and Couzin model [43]. Thus, it is necessary to consider separation actions to decrease the risk of disturbance, and aggregation actions to recover the swarm's performance. In our previous study, we adopted a semi-Markov process to model the recovery of network components [44]. Separation and aggregation are related to the degeneration and recovery of networks. Therefore, it was necessary to extend the recovery model in [44] to the entire resilience process. 

Based on the discussion above, we propose a multistate network approach for analyzing the resilience of a swarm IE network. The expected contributions of this study are as follows. 

First, we incorporated conditional probability to extend the multi-state network model. The state probability distribution of the component in such a model represents the IE capacity of the swarm IE link at a certain communication distance. Thus, time-dependent performance changes can be determined, and can be further employed to assess and analyze UAV swarm resilience. 

Second, the UAV swarm resilient behavior transformation, which includes aggregation and separation, was modeled using a semi-Markov-based model, where changes in the UAV positions lead to a transformation in the IE link capacity distribution. 

Third, for another UAV swarm resilient behavior, a resilience-based swarm IE topology optimization method was considered for UAV redeployment. 

Finally, the state probability distributions of the swarm IE capacity between UAVs at different distances were obtained through a real experiment. An application case study was evaluated based on the experimental data. The simulation results show that the proposed method can help assess and improve the resilience of a UAV swarm. 

The rest of the paper is organized as follows. In Section 2, the multistate network-based swarm IE network model is detailed. In Section 3, the resilience model of the UAV movement is introduced. Section 4 presents an application case study involving a UAV swarm. Finally, Section 5 concludes the study. 

# 2. Multistate information exchange (IE) network model of UAV swarm

In this section, we first introduce the multistate network model of a UAV swarm IE network. The probability distributions of the network components in the resilience process are then provided. Third, a performance metric for the swarm-IE network is proposed. 

# 2.1. Multistate IE network model

Consider a direct network $G(V, E)$ comprising a finite set of nodes $V$ and a set of arcs $E$ . The nodes in the network are referred to as UAV agents, and the arcs are the data links between the UAVs. The numbers of nodes and arcs are represented by $m$ and $n$ ; $i$ denotes an arc; thus, $E = \{1, 2, \dots, n\}$ . For each arc $i \in E$ , $c_i \in \{0, 1, \dots, m_i\}$ refers to the capacity of this component, where $m_i$ is the maximum capacity (maximum state) of arc $i$ . We considered that the data throughput state of a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/1ffbfef450ccfe95577480a29b9a9182a14419ab0b43c66997d68a34bff576f7.jpg)



Fig. 1. Transformation process of (unmanned aerial vehicle) UAV swarm formation.


component follows a distribution $\pmb{p}^i = (p_0^i, p_1^i, \dots, p_{m_i}^i)$ , where $p_c^i$ denotes the probability of component $i$ working in state $c$ . $\pmb{P} = (\pmb{p}^1, \pmb{p}^2, \dots, \pmb{p}^n)^T$ is the probability distribution matrix of the network. 

# 2.2. Probability distribution of components

In the real world, the operational state of the components in a network is typically based on certain conditions. For example, a UAV swarm IE network provides a certain throughput of data flow among the UAVs. The communication distance of the UAVs is an important condition that affects the state probability distribution of the communication link. The availability of a transceiver device in a UAV is another condition for normal data transmission between UAVs. 

For data link $i$ in a swarm IE network, incompatible events $B_1^i (t)$ , $B_{2}^{i}(t)$ ..., $B_{u}^{i}(t)$ are the conditions of component operation. We have $\bigcup_{j = 1}^{u}B_{j}^{i}(t) = \Omega$ , where $\Omega$ denotes the sample space. $Pr\{A^i (t) = c_i|B_j^i (t)\}$ denotes the probability that the state of component $i$ is $c_{i}$ under the condition of $B_{j}^{i}$ at time $t$ . According to the total probability theory, the probability of component $i$ operating in state $c_{i}$ at time $t$ can be determined by: 

$$
p _ {c _ {i}} ^ {i} (t) = \sum_ {j = 1} ^ {u} P r \left\{A ^ {i} (t) = c _ {i} \mid B _ {j} ^ {i} (t) \right\} * P r \left(B _ {j} ^ {i} (t)\right) \tag {1}
$$

The condition vector is defined as: 

$$
\boldsymbol {p} \boldsymbol {b} ^ {i} (t) = \left(\Pr \left(B _ {1} ^ {i} (t)\right), \Pr \left(B _ {2} ^ {i} (t)\right), \dots , \Pr \left(B _ {u} ^ {i} (t)\right)\right) \tag {2}
$$

Let $\pmb{C}^i(t)$ be the conditional operation probability matrix of component $i$ , given by: 

$$
\boldsymbol {C} ^ {i} (t) = \left[ \begin{array}{c c c c} P r \left\{A ^ {i} (t) = 0 | B _ {1} ^ {i} (t) \right\} & P r \left\{A ^ {i} (t) = 1 | B _ {1} ^ {i} (t) \right\} & \dots & P r \left\{A ^ {i} (t) = m _ {i} | B _ {1} ^ {i} (t) \right\} \\ P r \left\{A ^ {i} (t) = 0 | B _ {2} ^ {i} (t) \right\} & P r \left\{A ^ {i} (t) = 1 | B _ {2} ^ {i} (t) \right\} & & P r \left\{A ^ {i} (t) = m _ {i} | B _ {2} ^ {i} (t) \right\} \\ \vdots & & \ddots & \vdots \\ P r \left\{A ^ {i} (t) = 0 | B _ {u} ^ {i} (t) \right\} & P r \left\{A ^ {i} (t) = 1 | B _ {u} ^ {i} (t) \right\} & \dots & P r \left\{A ^ {i} (t) = m _ {i} | B _ {u} ^ {i} (t) \right\} \end{array} \right] \tag {3}
$$

Then, the state probability distribution of component $i$ is: 

$$
\boldsymbol {p} ^ {i} (t) = \boldsymbol {p} \boldsymbol {b} ^ {i} (t) * \boldsymbol {C} ^ {i} (t) \tag {4}
$$

# 2.3. Performance of swarm IE network

Liu et al. [44] defined the performance of a multistate network as the expectation of flow, expressed as: 

$$
Q = \sum_ {d = 0} ^ {M} \Lambda_ {d} * d \tag {5}
$$

where $d \in \{1, 2, \dots, M\}$ is the units of data flow that can be transmitted from the source node to the sink node; $M$ is the max flow of network; $\Lambda_d = Pr(\phi(x) = d)$ is the probability that the flow from the source node to the sink node is equal to $d$ . According to [44], the first step to obtain $\Lambda_d$ is to calculate probability $\Delta_d = Pr(\phi(x) \geq d)$ . Based on the network configurations and the probability distribution matrix, several methods can be used to determine $\Delta_d$ , including the state-space decomposition method [55]. For a swarm IE network, with an increase in the hop count between agents, the network performance worsens [50]. In this study, the minimum hop count is based on the shortest path in the network. First, we used the shortest path-searching algorithm [49] to find the shortest path between two UAVs. The minimum hop count of these two UAVs is the sum of the number of components in this path. Finally, we considered the source and sink nodes as the two agents whose minimum hop counts are the largest in the swarm. Thus, the performance of the swarm IE network at time $t$ , $QIE(t)$ , can be expressed as: 

$$
Q I E (t) = \min  \left(Q _ {1} (t), Q _ {2} (t), \dots , Q _ {s} (t)\right) \tag {6}
$$

where $Q_{1}(t), Q_{2}(t), \ldots, Q_{s}(t)$ denote the node pairs whose minimum hop counts have the same largest values. 

# 3. Resilience model of UAV swarm

The UAV swarm may be attacked, for example by ground air defense forces, during a mission. For such disturbances, the swarm can exhibit flexible behavior to reduce the impact. In this section, we consider two types of resilient behaviors of a UAV swarm: formation transformation and UAV redeployment. Subsequently, the corresponding resilience models are provided. 

# 3.1. Resilient behavior of UAV swarm

Reasonable separation and aggregation are typical self-organization behaviors of an intelligent swarm [41-43]. For example, it is assumed that a swarm has three formations based on the distance between UAV individuals: dense formation, $MO = 1$ ; compact formation, $MO = 2$ ; and sparse formation, $MO = 3$ . As depicted in Fig. 1, at the beginning of the mission, the UAV swarm operated in a dense formation. As suggested, the UAVs are close to each other, resulting in the strongest IE capacity; however, they are vulnerable to enemy disturbances. When entering the area covered by the enemy's anti-air fire at any time $T_{d}$ , all the UAVs exhibit decentralized behavior and switch to a sparse formation to reduce the probability of individual damage. Owing to the sparse spacing between UAVs, transmission of large amounts of information 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/707f99cf5cfcbf95a771013ef7520487cce8dad3711d86b12dcbb84234071f9a.jpg)



Fig. 2. Redeployment process of UAV swarm formation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/cb4e8b69ff2d15b977294be07bb2deb85fbf556b64688a8dce36c4716bb58908.jpg)



Fig. 3. Transfer of condition state of component.


becomes difficult. The swarm formation conversion is complete at time $T_{p}$ . The formation lasts for a period $h$ until it is no longer under fire from the enemy. When leaving the enemy's fire coverage at $T_{s}$ , the swarm shifts to a dense formation at $T_{r}$ to restore high-throughput IE capabilities. 

After the swarm enters the area covered by the enemy's anti-air fire, an individual UAV may be damaged by the enemy, causing a decline in the performance level of the entire IE network. In addition to the above formation transformation behavior, the swarm can also improve the system resilience by adjusting the topology. As shown in Fig. 2, after leaving the enemy fire coverage area, the swarm first switches to a compact formation $(MO = 2)$ . The distance between UAVs is moderate in compact formations, where UAVs can easily implement network reconfiguration measures. Therefore, the positions of individual UAVs can be altered to adjust the network topology. Subsequently, the swarm switches to a dense formation $(MO = 1)$ and continues its mission. 

# 3.2. Transformation of UAV swarm

Based on the above discussion, we focused on the effect of the resilient behaviors on link capacity. According to Equation (4), the link capacity is based on conditional operation probability matrix $C^i(t)$ and condition vector $p b^i(t)$ . Probability matrix $C^i(t)$ is mostly a statistical result under various conditions, such as the distribution of data flow in one second under the condition of a certain spacing. Therefore, we assumed that $C^i(t)$ does not change over time. However, the disturbance may cause the operational condition $p b^i(t)$ to change, which ultimately 

changes the state distribution of component $\pmb{p}^i(t)$ . The essence of the formation transformation is the adjustment of the UAV distance. 

Component $i \in E$ has $m_i + 1$ states, including zero to $m_i$ . The condition (distance between drones) of the component has $u$ states and the initial probability distribution of the condition state is $p b^i(0)$ . Initially, the state distribution of component $i$ obeys $I^i = p b^i(0) * C^i$ . 

When a swarm is disturbed or recovered during a task, the distance between the drones may also be transferred between different states. The sojourn time in any state of the Markov process follows an exponential distribution, which limits the practical application of the Markov model. Because the distribution of the sojourn time in any state in a semi-Markov process can be arbitrary, it is an excellent choice for modeling the resilience of components [45]. 

As shown in Fig. 3, conditions $B_1^i, B_2^i, \ldots, B_u^i$ may transfer at different stages of the resilience process, where $B_j^i$ is the condition state of component $i$ . In this study, we assumed that a larger number of $j$ denotes a smaller distance between the drones. During the resilience process, the condition state may transfer from one to another. Before using the semi-Markov process, the corresponding kernel matrix $\Phi^i(t)$ should be built, where element $\Phi_{jl}^i(t)$ , in the matrix represents the probability of component $i$ transitioning from state $j$ to state $l$ in time period $[0,t]$ . Then, we have [46]: 

$$
\boldsymbol {\Phi} ^ {i} (t) = \left[ \begin{array}{c c c c c} 0 & \Phi_ {0 1} ^ {i} (t) & \dots & \Phi_ {0 (u - 1)} ^ {i} (t) & \Phi_ {0 u} ^ {i} (t) \\ \Phi_ {1 0} ^ {i} (t) & 0 & \dots & \Phi_ {1 (u - 1)} ^ {i} (t) & \Phi_ {1 u} ^ {i} (t) \\ \vdots & \vdots & \ddots & \vdots & \vdots \\ \Phi_ {(u - 1) 0} ^ {i} (t) & \Phi_ {(u - 1) 1} ^ {i} (t) & \dots & 0 & \Phi_ {(u - 1) u} ^ {i} (t) \\ \Phi_ {u 0} ^ {i} (t) & \Phi_ {u 1} ^ {i} (t) & \dots & \Phi_ {u (u - 1)} ^ {i} (t) & 0 \end{array} \right] \tag {7}
$$

$$
\Phi_ {j l} ^ {i} (t) = \int_ {0} ^ {t} \prod_ {k = 0, k \neq l} ^ {m _ {i}} \left[ 1 - F _ {j k} ^ {i} (\tau) \right] d F _ {j l} ^ {i} (\tau) \tag {8}
$$

where $F_{jl}^{i}(u), j, l \in \{0, 1, \dots, m_{i}\}$ is the distribution function of sojourn time $u$ in state $j$ , and the next state is $l$ . 

The transition probability matrix of a semi-Markov process $\Theta^i(t)$ , is referred to as the probability of the component being transferred from the initial state to a new state at time $t$ . $\Theta^i(t)$ can be obtained by solving the Markov-Renewal Equation as follows: 

$$
\theta_ {j l} ^ {i} (t) = \delta_ {j l} \left[ 1 - \sum_ {s = 0} ^ {m _ {i}} \Phi_ {j s} ^ {i} (t) \right] + \sum_ {s = 0} ^ {m _ {i}} \int_ {0} ^ {t} \varphi_ {j s} ^ {i} (\tau) \theta_ {s l} ^ {i} (t - \tau) d \tau \tag {9}
$$

where $\varphi_{js}^{i}(\tau) = d\Phi_{js}^{i}(\tau) / d\tau$ , $\delta_{jl} = \{ \begin{array}{l}1j = l\\ 0j\neq l \end{array}$ , and $j,l\in \{0,1,\dots,m_i\}$ . This equation can be solved by applying Laplace and inverse Laplace transforms [46]. Then, we obtain the state distribution of the component condition: 

$$
\boldsymbol {p} \boldsymbol {b} ^ {i} (t) = \boldsymbol {p} \boldsymbol {b} ^ {i} (0) * \boldsymbol {\Theta} ^ {i} (t) \tag {10}
$$

In addition, considering that the condition of the component operation has two states, $\Phi^i(t)$ and $\Theta^i(t)$ are two-dimensional matrices related only to the two states: complete fault and complete operation. 

# 1). Separation

As shown in Fig. 1, a disturbance occurred at $T_{d}$ . Subsequently, the condition state of the component begins to transfer and the distance between the drones reaches its maximum value at $T_{p}$ . Let the kernel matrix of this process be $\Phi^{i - d}(t) = [\Phi_{jl}^{i - d}(t)]$ , where if $j < l$ , then $\Phi_{jl}^{i - d}(t) = 0$ . Based on the kernel matrix, we can obtain the transition probability matrix $\Theta^{i - d}(t)$ . Therefore, for any $t \in [T_d,T_p]$ , the probability distribution of component $i$ can be expressed as: 

$$
\boldsymbol {p} ^ {i} (t) = \boldsymbol {p} \boldsymbol {b} ^ {i} (0) * \boldsymbol {\Theta} ^ {i - d} (t) * \boldsymbol {C} ^ {i} \tag {11}
$$

# 2).Aggregation

With the implementation of aggregation, the probability distribution of the conditions of the component transfers to a dense state, and the component state distribution changes with time. For any $t \in [T_s, T_r]$ , the kernel matrix of this process $\Phi^{i-r}(t) = [\Phi_{jl}^{i-dr}(t)]$ , where if $j > l$ , $\Phi_{jl}^{i-r}(t) = 0$ . Then, the transition probability matrix $\Theta^{i-r}(t)$ can be obtained. Finally, the probability distribution vector of the component is: 

$$
\boldsymbol {p} ^ {i} (t) = \boldsymbol {p} \boldsymbol {b} ^ {i} (0) * \boldsymbol {\Theta} ^ {i - d} (t) * \boldsymbol {\Theta} ^ {i - r} (t) * \mathbf {C} ^ {i} \tag {12}
$$

# 3). Probability distribution matrix of network

Based on the above discussion, at any time of resilience, $t \in [T_d, T]$ , the kernel matrix of the entire resilience process is defined as: 

$$
\widetilde {\Phi} ^ {i} (t) = \left\{ \begin{array}{c} \Phi^ {i - d} (t) T _ {d} \leq t <   T _ {p} \\ 0 T _ {p} \leq t <   T _ {s} \\ \Phi^ {i - p} \left(\min  \left(t, T _ {r}\right) - T _ {s}\right) T _ {s} \leq t \leq T \end{array} \right. \tag {13}
$$

Therefore, the transfer probability matrix of the whole resilience process can be obtained by: 

$$
\widetilde {\Theta} ^ {i} (t) = \left\{ \begin{array}{c} \Theta^ {i - d} \left(\min  \left(t, T _ {p}\right)\right) T _ {d} \leq t <   T _ {s} \\ \Theta^ {i - d} \left(T _ {p}\right) * \Theta^ {i - p} \left(\min  \left(t, T _ {r}\right) - T _ {s}\right) T _ {s} \leq t \leq T \end{array} \right. \tag {14}
$$

Thus, the state distribution of component $i$ in the resilience process can be written as: 

$$
\boldsymbol {p} ^ {i} (t) = \boldsymbol {p} \boldsymbol {b} ^ {i} (0) * \widetilde {\boldsymbol {\Theta}} ^ {i} (t) * \boldsymbol {C} ^ {i} \tag {15}
$$

For each disturbed component, the probability distribution $\pmb{p}^i(t)$ of the component state at any time could be obtained using the proposed resilience process model. Subsequently, the state probability distribution matrix $\pmb{P}(t)$ of the network was determined. Therefore, the transfer of the state probability distribution of the components eventually results in a change in the performance of the multistate network. 

# 4). Swarm formation intermediate state

Based on the above model, the state distribution of the distance of any IE link $\pmb{p}\pmb{b}^{i}(t) = (pb_{B_{1}^{i}}^{i}(t),pb_{B_{2}^{i}}^{i}(t),\dots pb_{B_{0}^{i}}^{i}(t))$ can be obtained, where $p b_{B_{1}^{i}}^{i}(t)$ is the probability that link $i$ is at distance $B_{j}^{i}$ . The positions of the 

UAVs during formation switching are random because of the semi-Markov model. Then, we defined a thread value $\theta$ . Only when all the components in the network satisfy $p b_{B_{j}^{i}}^{i}(t) \geq \theta$ , $i \in E$ , then the swarm is assumed to be in the formation corresponding to distance $B_{j}^{i}$ . Otherwise, the swarm was in an intermediate state between the two formations. Thus, the formation of a swarm can be determined at any time during the resilience. 

# 3.3. UAV redeployment

In addition to the formation transformation, the network topology of a swarm can be adjusted depending on the position of the existing UAVs according to the position of the damaged UAV and the task requirements. 

The set of damaged UAVs is expressed as $\Pi$ . The set of remaining UAVs is K, excluding the source and sink nodes. If a UAV $u \in \mathbf{K}$ is assigned the position of $\nu$ in $\Pi$ , the following steps are taken: First, the UAV leaves its original position $\nu$ , so all its IE link connections $(i \epsilon \Gamma_{\nu})$ lose their functions. Second, suppose that the shortest path of UAVs $u$ and $\nu$ in the original topology is $l_{uv}$ , then UAV $u$ needs to fly $s * l_{uv} \mathrm{~m}$ to the destination in a compact formation, where $s$ is the distance between drones. Third, it was assumed that the flight time of a UAV follows a normal distribution. Assuming that the travel time expectation is $s * l_{uv} / \nu_c$ and variance is 1, the probability of reaching the specified position at any time $t$ is given as $p^{\nu}(t)$ . Finally, with the movement of the replaced UAV, the original damaged component $j \epsilon \Gamma_u$ starts to recover its function, and the probability distribution after recovery is as follows: 

$$
\boldsymbol {p} ^ {j} (t) = \left[ \begin{array}{l l} 1 - p ^ {\nu} (t) & p ^ {\nu} (t) \end{array} \right] * \left[ \begin{array}{l} \boldsymbol {e} \\ \boldsymbol {p c} ^ {j} \end{array} \right] \tag {16}
$$

where $\pmb{e} = (1, 0, \dots, 0)$ , and $\pmb{pc}^j = (pc_0^j, pc_1^j, \dots, pc_{m_i}^j)$ denotes the probability distribution of component $j$ in compact formation. 

From the perspective of mission resilience, a key problem when implementing a placement strategy in a swarm is finding a UAV among many individuals to perform the placement action to achieve the highest swarm resilience. Swarm resilience $R(T)$ is used as the optimization object to achieve this goal. In this study, we chose the mission-oriented resilience metric proposed in [47], given by: 

$$
R (T) = \beta * \frac {\int_ {T _ {0}} ^ {T} [ Q (t) - \bar {Q} (t) \geq 0 ] d t}{T - T _ {0}} + (1 - \beta) \frac {\int_ {T _ {0}} ^ {T} Q (t) [ Q (t) - \bar {Q} (t) \geq 0 ] d t}{\int_ {T _ {0}} ^ {T} P Q (t) d t} \tag {17}
$$

where $Q(t)$ refers to the performance of the multistate network at time $t$ , $\overline{Q}(t)$ is used to describe the minimum performance requirement for the current mission, $PQ(t)$ is the ideal performance of the system at time $t$ , $[P]$ is the Iverson bracket, which returns 0 if $P$ is false and 1 otherwise, and $\beta \in [0,1]$ is the weight parameter. A larger $\beta$ can be realized when a system engineer concentrates on the system's capacity to sustain the bare minimum required performance following a disturbance. However, if the system engineer is more concerned with the overall performance recovery level throughout a mission, a smaller $\beta$ will be set. 

Therefore, the optimization object is as follows: 

$$
\max  R (T) \tag {18}
$$

The influence of swarm placement behavior on $R(T)$ is mainly reflected in the pairing of the standby and damaged UAVs. The solution to this optimization problem can then be set as the following matrix: 

$$
S = \left[ \begin{array}{l l} u _ {1} & v _ {1} \\ u _ {2} & v _ {2} \\ \vdots & \vdots \\ u _ {z} & v _ {z} \end{array} \right] \tag {19}
$$

where $u_{i}$ and $\nu_{i}, i\in \{1,2,\dots,z\}$ represent the index numbers of the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/b198d44dab45afa59b592902bcbceef38095b70930ab23eb6544677583ac64ea.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/cf441b8fa5393f559fd222b045114298b2b6272c6b0369d5d113c48d2d015cb1.jpg)



Fig. 4. Main screen of Ixchariot Console.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/c0cb47f62a3cd75804878d4cf4bdfb9fe918e4b02ea22e519fad15d4fc91da7b.jpg)



Fig. 5. Test setup.


damaged UAV and UAV assigned to fill the position, respectively, and $z$ is the number of UAVs performing the replacement movement. The constraints of the optimization problem are as follows: 

$$
u _ {i} \in \mathrm {K} \tag {20}
$$

$$
i \neq j, u _ {i} \neq u _ {j} \tag {21}
$$

$$
v _ {i} \in \Pi \tag {22}
$$

$$
0 \leq z \leq \operatorname {s i z e} (\Pi) \tag {23}
$$

$$
M O = 2 \tag {24}
$$

Constraints (20) and (21) indicate that only the UAV in K can participate in the placement. The same backup UAV can fill only one vacancy left by a destroyed UAV. Constraint (23) indicates that the number of UAVs executing the placement is not greater than the total number of damaged UAVs. Constraint (24) indicates that placement can only be performed in a compact formation. 

# 4. Case study

As described in this section, we first conducted a test to obtain the state probability distributions of the data flow between UAVs at different distances. Second, a scenario in which a UAV swarm encounters, and recovers from, disturbances was considered. The proposed methods were then used to analyze the resilience of the UAV swarm. 

# 4.1. Data flow throughput experiment of UAV swarm IE network

An experiment was conducted to determine the wireless IE ability between UAVs using the Ixchariot software platform. This application-layer performance-testing software was developed by the American company IXIA [51]. As shown in Fig. 4, it is a powerful tool that enables the visualization of throughput, packet loss, response time, delay, and additional network characteristics over time. Several researchers have used this tool to measure the performance of telecommunication networks [52], VoIP (Voice over IP) networks [53], and wireless networks [54]. The Ixchariot Console, which is set up on a computer, can control 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/ffa6ee71dde9ead7257955583e74ed211bc22dc1b1c9e74523376a77dd68ba67.jpg)



Fig. 6. Placement of each unit in test.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/01cd576bdd24714e6d8d17be2b4cbdd17ab4c3a106732b32e622189094550193.jpg)



(a) Data flow curve in $10\mathrm{m}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/9c7257cf371f0a1cf4ac1fe15d0d7e7847a6be8bbee056bc580af96cbdb07b88.jpg)



(b) Data flow curve in $20\mathrm{m}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/29057520b5a20737bf073c8a93e7b74a31f55c08f03b732e77eac6843c1876dd.jpg)



(c) Data flow curve in $30\mathrm{m}$ 50 m


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/baff48f4cad9bd6d61c36296b3e1d0b8073ae5b8256720b2d8eef3dc2dea0a63.jpg)



(d) Data flow curve in $40\mathrm{m}$ 60 m


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/13669a67927b242d37e6973ce069350be00cadba7baad28a4c86071420704e65.jpg)



(e) Data flow curve in $50\mathrm{m}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/8914069f0d5cc5bf0f70c36734fb087d856464fe53de51b4c3059ee742edf57e.jpg)



(f) Data flow curve in $60\mathrm{m}$



Fig. 7. Data curves for different distances.



Table 1 Network component status and throughput.


<table><tr><td>State</td><td>Throughput range (Mbps)</td></tr><tr><td>0</td><td>[0,5)</td></tr><tr><td>1</td><td>[5,10)</td></tr><tr><td>2</td><td>[10,15)</td></tr><tr><td>3</td><td>[15,20)</td></tr><tr><td>4</td><td>[20,25)</td></tr><tr><td>5</td><td>[25,30)</td></tr><tr><td>6</td><td>[30,35)</td></tr><tr><td>7</td><td>[35,40)</td></tr><tr><td>8</td><td>[40,45)</td></tr><tr><td>9</td><td>\( \left\lbrack {{45}, + \infty }\right) \)</td></tr></table>

more endpoints to generate a real flow in the network. During the test, the transmission information was collected and recorded. These recorded data were then employed to evaluate the performance of the IE capacity. 

As shown in Fig. 5, the test system constituted three rotor UAVs, three wireless communication transceiver devices, and a ground-processing unit equipped with an Ixchariot Console. The wireless communication transceiver is served by a smartphone with an endpoint APP. Each UAV carries a phone for networking, and the ground information processing unit evaluates the information flow of each link. Specifically, the test included the following steps: 

Step 1: All equipment was started on the ground and relevant software was configured. 

Step 2: As shown in Fig. 6, the UAVs were placed in the start position and controlled to lift to $10\mathrm{m}$ . The ground control unit was then used to evaluate the UAV1-UAV2 and UAV1-UAV3 communication links. Step 3: UAV2 and UAV3 were moved $10\mathrm{m}$ forward. We evaluated the throughputs of the two links and recorded the data. The preceding steps were repeated until the UAVs arrived at their destinations. 

At each distance, we tested the data link for one minute, and recorded the throughput at each sampling time. Missing data is a common problem in engineering applications. After the interpolation of the missing part in the initial data, we obtained a data throughput curve at various distances between the UAVs, as shown in Fig. 7. Table 1 lists the information flow throughput and the network component states. The probability distribution can then be determined by obtaining the proportions of different states within one minute of testing. For example, at the communication distance of $10\mathrm{m}$ , the sum of the times that state 9 occurs is $51.4\mathrm{s}$ , so the probability of state 9 is $51.4 / 60 = 0.856$ . Table 2 lists the probability distributions of the UAV IE data flow. The IE ability is primarily concentrated in a higher state near the test distance. With an increase in the test distance, the information flow starts to focus on the intermediate state, whereas some of the information flows disperse to the high and low states. As the distance between the UAVs is further increased, the throughput of IE significantly reduces, and the 


Table 2 Probability distribution of UAV IE data flow.


<table><tr><td rowspan="2">Distance (m)</td><td colspan="10">State</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>10</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.11</td><td>0.86</td></tr><tr><td>20</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.02</td><td>0.06</td><td>0.16</td><td>0.24</td><td>0.52</td></tr><tr><td>30</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.03</td><td>0.10</td><td>0.28</td><td>0.33</td><td>0.20</td><td>0.06</td></tr><tr><td>40</td><td>0.00</td><td>0.00</td><td>0.09</td><td>0.08</td><td>0.04</td><td>0.30</td><td>0.33</td><td>0.12</td><td>0.03</td><td>0.01</td></tr><tr><td>50</td><td>0.10</td><td>0.15</td><td>0.20</td><td>0.26</td><td>0.18</td><td>0.08</td><td>0.03</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>60</td><td>0.00</td><td>0.22</td><td>0.61</td><td>0.15</td><td>0.02</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/60670991ab89e36f30943ca2649ff2c96a0dcba161670d346147f1dccdf14a0a.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/a12e1af7820f5447fd0a34057d35e82f6eddcacd64e6e3fb90ea52b67ded5d40.jpg)



(b)



Fig. 8. UAV swarm in rectangular formation.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/b0cfc8175308763b96da44d133398aa01a76b7ed08399d9bc2bcd54b568d5d24.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/121b19795aa5308c751be4100c4c64190ae396abf4b652dae23372f5751dda34.jpg)



(b)



Fig. 9. Network topology of UAV swarm.



Table 3 State distributions in each formation.


<table><tr><td rowspan="2">Distance (m)</td><td colspan="3">State</td></tr><tr><td>0</td><td>1</td><td>2</td></tr><tr><td>20</td><td>0.02</td><td>0.078</td><td>0.902</td></tr><tr><td>30</td><td>0.02</td><td>0.401</td><td>0.579</td></tr><tr><td>40</td><td>0.118</td><td>0.735</td><td>0.147</td></tr></table>

information flow status remains generally low. 

# 4.2. Mission resilience evaluation and analysis of UAV swarm IE network

# 1). UAV swarm configuration

Tasks involving a UAV swarm with 20 agents were performed in a rectangular formation, as shown in Fig. 8 (a). As depicted in Fig. 8 (b), agent pairs 1-20 and 4-17 have the same minimum hop count length of seven, which is larger than that of any other node pair. Thus, according 

to Equation (7), the swarm performance can be defined as: 

$$
Q (t) = \min  \left(Q _ {1} (t), Q _ {2} (t)\right) \tag {25}
$$

where $Q_{1}(t)$ and $Q_{2}(t)$ are the expected network capabilities of node pairs 1-20 and 4-17, respectively. For example, considering agent 1 as the source node and agent 20 as the sink node, the network topology comprising 20 nodes and 40 components is shown in Fig. 9 (a). Similarly, Fig. 9 (b) displays the network topology of node pair 4-17. 

From the test described in Section 4.1, the UAVs have varying IE capabilities at different distances. In particular, we assumed that the dense, compact, and sparse formations corresponded to inter-UAV distances of 20, 30, and $40\mathrm{m}$ . Note that in this study, an individual UAV could only switch between these three types of spacing during task execution. 

To reduce computational effort, we set state 0 as the throughput range from 0 to 15 Mbps, state 1 as 15-35 Mbps, and state 2 as the throughput range above 35 Mbps. Assuming that the individual reliability of the UAV is 0.99, the reliability of the data link is 0.98, because it requires both UAVs at the receiving and sending ends to be in a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/6424504602439d3e16e37e723e33e9382c406b1626bdc76a62601b6ad9ece0cd.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/1da051830ee0833c722c57928af7544fa9f22923214634d693588efa87d5fc36.jpg)



(b）



Fig. 10. Classification of IE links.



Table 4 Parameters of normal distribution for different links.


<table><tr><td></td><td>μ01</td><td>μ02</td><td>μ12</td><td>μ21</td><td>μ20</td><td>μ10</td></tr><tr><td>I</td><td>5 /vc</td><td>10 /vc</td><td>5 /vc</td><td>5 /vc</td><td>10 /vc</td><td>5 /vc</td></tr><tr><td>II</td><td>15 /vc</td><td>30 /vc</td><td>15 /vc</td><td>15 /vc</td><td>30 /vc</td><td>15 /vc</td></tr><tr><td>III</td><td>15 /vc</td><td>30 /vc</td><td>15 /vc</td><td>15 /vc</td><td>30 /vc</td><td>15 /vc</td></tr><tr><td>IV</td><td>25 /vc</td><td>50 /vc</td><td>25 /vc</td><td>25 /vc</td><td>50 /vc</td><td>25 /vc</td></tr><tr><td>V</td><td>25 /vc</td><td>50 /vc</td><td>25 /vc</td><td>25 /vc</td><td>50 /vc</td><td>25 /vc</td></tr><tr><td>VI</td><td>35 /vc</td><td>70 /vc</td><td>35 /vc</td><td>35 /vc</td><td>70 /vc</td><td>35 /vc</td></tr></table>

working state. Incorporating the data in Table 2, the probability distribution of the UAV IE capability in the three formations is presented in Table 3. 

Then, we also have the conditional operation probability matrix of component $i$ as: 

$$
\boldsymbol {C} ^ {i} = \left[ \begin{array}{l l l} 0. 0 2 & 0. 0 7 8 & 0. 9 0 2 \\ 0. 0 2 & 0. 4 0 1 & 0. 5 7 9 \\ 0. 1 1 8 & 0. 7 3 5 & 0. 1 4 7 \end{array} \right] \tag {26}
$$

Assuming that the probability distribution of the three distances between the two UAVs corresponding to link $i$ is $p b^{i}(t)$ , the state probability distribution of the link IE capability is $p^{i}(t) = p b^{i}(t) * C^{i}$ . 

# 2). Parameters of formation transformation

There are three conditions, $B_1^i$ , $B_2^i$ and $B_3^i$ , for the distance between two UAVs corresponding to link $i$ , which relate to the three inter-UAV distances of 20, 30, and $40\mathrm{m}$ . The probability of state transition represents the probability that two UAVs will reach the designated position after a period of time from the initial position. In this study, $F$ was assumed to follow the normal distribution with the mean value of $\mu$ and the variance of 1. When the swarm switches to a dense formation, $F_{12} = F_{13} = F_{23} = 0$ was set. When the swarm switches to a compact formation, $F_{13} = F_{31} = F_{21} = F_{23} = 0$ . When the swarm is converted into a sparse formation, $F_{21} = F_{31} = F_{32} = 0$ . 

The parameters of normal distribution $\mu$ represent the expected time required for a UAV to reach a designated position. Taking the swarm transformation from a dense to a sparse formation as an example, it is assumed that UAVs extend outward from the swarm center to increase the spacing. As shown in Fig. 10 (a), the upper and lower swarms divided by dotted line B moved up and down by $10\mathrm{m}$ , respectively. Link set I includes links 3, 11, 13, 21, 23, 31, 33, and 39. The expected travel time of the link in I is $\mu_{13}^{\mathrm{I}} = 10 / \nu_{c}$ , where $\nu_{c}$ is the relative speed of a UAV during position change. The UAVs above dotted line A and below dotted line C must move up and down by $20\mathrm{m}$ , respectively. Thus, the total displacement was $30\mathrm{m}$ for these UAVs and $\mu_{13}^{\mathrm{II}} = 30 / \nu_{c}$ . Meanwhile, link set II includes links 1, 5, 8, 10, 14, 16, 18, 20, 24, 26, 28, 30, 34, 36, 38, and 40. 

The horizontal spacing adjustment when the longitudinal spacing was varied is depicted in Fig. 10 (b). The UAVs on the left and right sides of dotted lines E and F move $20\mathrm{m}$ to both sides, respectively. Link set III (12, 15, 22, and 25) required the total movement of $30\mathrm{m}$ , where $\mu_{13}^{\mathrm{III}} = 30 / \nu_c$ . In addition, link set IV constitutes links 9, 17, 19, and 27, whose UAVs move $50\mathrm{m}$ , so $\mu_{13}^{\mathrm{IV}} = 50 / \nu_c$ . The UAVs on the left and right sides of dotted lines D and G must move $20\mathrm{m}$ to both sides. The UAVs in set V (4, 6, 32 and 35) move $50\mathrm{m}$ , so $\mu_{13}^{\mathrm{V}} = 50 / \nu_c$ . Finally, $\mu_{13}^{\mathrm{VI}} = 70 / \nu_c$ where set VI includes links 2, 7, 29, and 37. 

The transformation of swarms from large-spacing to small-spacing formations can also be regarded as a reverse adjustment of the above processes in the vertical and horizontal directions, respectively. As listed in Table 4, the parameters of the normal distribution for different link-spacing conversions were determined. 


Table 5 Parameters of simulation.


<table><tr><td>Notation</td><td>Description</td><td>Value</td></tr><tr><td>T</td><td>Mission time</td><td>1200 s</td></tr><tr><td>Td1</td><td>The time of the first disturbance</td><td>300 s</td></tr><tr><td>Td2</td><td>The time of the second disturbance</td><td>600 s</td></tr><tr><td>h</td><td>The time of flying through the enemy&#x27;s air defense area</td><td>100 s</td></tr><tr><td>PQ(t)</td><td>Expected performance</td><td>2.55</td></tr><tr><td>Q(t)</td><td>Required performance</td><td>2</td></tr><tr><td>γ</td><td>Accurate of network performance</td><td>10-3</td></tr><tr><td>β</td><td>Resilience weight parameter</td><td>0.5</td></tr><tr><td>νc</td><td>Relative velocity of UAV</td><td>1 m/s</td></tr></table>

# 3). Case simulation and analysis

Based on the above settings for the swarm IE network model and resilient behaviors, simulations were conducted to analyze the resilience of the swarm using different recovery strategies. 

The primary parameters of the simulation are listed in Table 5. When calculating the performance metric, a time-saving method was adopted to obtain an approximate value rather than an exact value [44,55]. Thus, we set $\gamma = 10^{-3}$ , i.e., the accuracy of network performance is less than 0.001. Ideal IE capability $PQ(t)$ is the IE capability of the entire network when the UAV swarm is in a dense formation and no individual is damaged. At this time, the state distribution of all the links follows $p^i = (0.02, 0.078, 0.902)$ . The IE capability of the network in this ideal situation is expected to be 2.55. Assuming that the ideal IE capability does not change during the entire task process, $PQ(t) = 2.55$ . Considering that a large amount of real-time image data must be shared in the process of swarm tasks, the task requirement of IE capability was set to two. The swarm encountered two disturbances during the task at 300 and 600 s respectively. The first disturbance did not damage a UAV. Whereas, the second disturbance caused several UAV agents to lose their functionality. Let $\Gamma_j$ be the set of information links connected to UAV $j$ . If UAV $j$ loses its function, components $ic\Gamma_j$ are also disconnected. Considering Fig. 9 (a) as an example: If node 18 was damaged, links 32, 38, and 39 will also become damaged. Thus, the state probability distribution of a damaged link was set to $(1, 0, 0)$ . 

Two recovery strategies were considered during tasks: 

Strategy 1: Formation transformation only. 

Strategy 2: Formation transformation combined with UAV redeployment. 

The optimal placement of UAVs is determined using a genetic algorithm [48]. In addition, the relative flight path length of the UAV, $l_{uv}$ , is obtained by the shortest path search algorithm [49]. 


Table 6 Resilience value when damage quantity is 1.


<table><tr><td rowspan="2">Index of destroyed UAV</td><td colspan="2">Resilience value</td><td rowspan="2">Redeployment plan</td></tr><tr><td>Strategy 1</td><td>Strategy 2</td></tr><tr><td>2</td><td>0.4</td><td>0.73</td><td>6</td></tr><tr><td>3</td><td>0.4</td><td>0.73</td><td>7</td></tr><tr><td>5</td><td>0.4</td><td>0.75</td><td>9</td></tr><tr><td>6</td><td>0.75</td><td>0.75</td><td>∅</td></tr><tr><td>7</td><td>0.75</td><td>0.75</td><td>∅</td></tr><tr><td>8</td><td>0.4</td><td>0.75</td><td>12</td></tr><tr><td>9</td><td>0.78</td><td>0.78</td><td>∅</td></tr><tr><td>10</td><td>0.78</td><td>0.78</td><td>∅</td></tr><tr><td>11</td><td>0.78</td><td>0.78</td><td>∅</td></tr><tr><td>12</td><td>0.78</td><td>0.78</td><td>∅</td></tr><tr><td>13</td><td>0.4</td><td>0.75</td><td>9</td></tr><tr><td>14</td><td>0.75</td><td>0.75</td><td>∅</td></tr><tr><td>15</td><td>0.75</td><td>0.75</td><td>∅</td></tr><tr><td>16</td><td>0.4</td><td>0.75</td><td>12</td></tr><tr><td>18</td><td>0.4</td><td>0.73</td><td>14</td></tr><tr><td>19</td><td>0.4</td><td>0.73</td><td>15</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/59d07468fc3717bf8fa9f80101416502aeb0a3e8671ef7eb50c0d39781a16b0d.jpg)



Fig. 11. Network performance curves with UAV2 damaged.



Table 7 Resilience value of each group when damage quantity is 2.


<table><tr><td rowspan="2">Index</td><td rowspan="2">Destroyed individuals</td><td colspan="2">Resilience value</td><td rowspan="2">Placement plant</td></tr><tr><td>Strategy 1</td><td>Strategy 2</td></tr><tr><td>1</td><td>2-3</td><td>0.401</td><td>0.705</td><td>10-6</td></tr><tr><td>2</td><td>5-6</td><td>0.401</td><td>0.705</td><td>7-11</td></tr><tr><td>3</td><td>5-9</td><td>0.401</td><td>0.721</td><td>6-10</td></tr><tr><td>4</td><td>6-7</td><td>0.401</td><td>0.705</td><td>6-10</td></tr><tr><td>5</td><td>9-10</td><td>0.401</td><td>0.705</td><td>6-10</td></tr><tr><td>6</td><td>10-11</td><td>0.729</td><td>0.729</td><td>∅</td></tr><tr><td>7</td><td>10-14</td><td>0.733</td><td>0.733</td><td>∅</td></tr><tr><td>8</td><td>15-19</td><td>0.401</td><td>0.705</td><td>7-11</td></tr></table>

The purpose of this experiment is to illustrate the proposed multi-state network approach for resilience evaluation and analysis of UAV swarms, including specific implementation of methods and comparison with different strategies. Thus, three progressive scenarios with different numbers of disturbed UAVs were considered in this experiment. First, we considered a UAV damaged by a disruptive event. Subsequently, two adjacent UAVs lost their function when they passed through the enemy's anti-aircraft fire coverage. Finally, we assumed the largest number of damaged UAVs of three in scenario 3. In addition, to maintain a unified calculation standard, the source and sink nodes in this swarm IE network were excluded from disruptive events. 

a). Case of one damaged UAV. In one case, we considered that a UAV became damaged, indicating that all the components linked to it are total failures. Accordingly, all the UAVs were tested, except for the source and sink nodes. The results are provided in Table 6, where the damage to the UAVs at positions 2, 3, 5, 8, 14, 16, 18, and 19 had a 

greater impact on the swarm IE capability. The UAV at position 2 was damaged, and the performance curve of the cluster is shown in Fig. 11. The transformation of the UAV swarm helps resist and recover from disturbances. The performance of the network was restored to satisfy the mission requirements via aggregation. However, when the UAV at position 2 was damaged in the second disturbance, the transformation cannot meet the mission requirements. At the beginning of strategy 2, owing to the departure of UAV 6 from its original position, the network performance decreased slightly. When a UAV reaches position 2, the network performance recovers to 1.37. As the swarm formation changed to a dense formation, the network performance recovered to 2.36, which met the mission requirements. 

There are no redeployment plans for UAVs at positions 6, 7, 9, 10, 11, 12, 14, and 15 to further improve the resilience of the swarm. Therefore, the functional loss of such UAVs has less effect on the resilience of the network. In addition, the best strategy is to maintain the current topology, and the network can continue completing tasks. 

Among all the UAVs, those in positions 2, 3, 18, and 19 exhibited the lowest resilience values under the two strategies. Thus, they are the most important and sensitive to a network's performance and resilience. 

b). Cases of two damaged UAVs. As listed in Table 7, we considered eight sets of damaged adjacent UAVs, and the resilience values of each set with different recovery strategies were recorded. The first number of placement schemes represents the index of the UAV used to replace the position of the first damaged individual in the damaged UAV set. For example, in the first group of cases, UAV 10 replaced damaged UAV 2. 

As shown in Fig. 12, among the eight damage groups, groups 6 and 7 did not significantly affect network resilience, and the optimization algorithm did not provide a placement scheme to further improve resilience. The other groups showed serious impacts on the performance of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/3783cf4e5319bc33c4223437ad510a1db76e9af957d42fabb0bfb7fe95a11925.jpg)



Fig. 12. Comparison of resilience of each group when two UAVs are damaged.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/5fed225464d58595a2d0e7223eb83a56ec809028f3a9c0f2426d1271c79d02c3.jpg)



Fig. 13. Network performance curves for group 4.



Table 8 Groups of destroyed UAVs.


<table><tr><td>Index</td><td>Destroyed individuals</td></tr><tr><td>1</td><td>5-9-13</td></tr><tr><td>2</td><td>6-10-14</td></tr><tr><td>3</td><td>2-6-10</td></tr><tr><td>4</td><td>5-6-7</td></tr><tr><td>5</td><td>9-10-11</td></tr><tr><td>6</td><td>6-9-10</td></tr><tr><td>7</td><td>6-7-11</td></tr><tr><td>8</td><td>2-3-7</td></tr></table>


Table 9 Resilience value of each group when damage quantity is 3.


<table><tr><td rowspan="2">Index</td><td rowspan="2">Destroyed individuals</td><td colspan="2">Resilience value</td><td rowspan="2">Placement plant</td></tr><tr><td>Strategy 1</td><td>Strategy 2</td></tr><tr><td>1</td><td>5-9-13</td><td>0.413</td><td>0.697</td><td>6-10-14</td></tr><tr><td>2</td><td>6-10-14</td><td>0.717</td><td>0.717</td><td>∅</td></tr><tr><td>3</td><td>2-6-10</td><td>0.401</td><td>0.684</td><td>7-11-15</td></tr><tr><td>4</td><td>5-6-7</td><td>0.401</td><td>0.671</td><td>10-6-14</td></tr><tr><td>5</td><td>9-10-11</td><td>0.401</td><td>0.684</td><td>6-10-14</td></tr><tr><td>6</td><td>6-9-10</td><td>0.401</td><td>0.684</td><td>6-14-10</td></tr><tr><td>7</td><td>6-7-11</td><td>0.710</td><td>0.710</td><td>∅</td></tr><tr><td>8</td><td>2-3-7</td><td>0.401</td><td>0.671</td><td>11-15-7</td></tr></table>

the system. Without a placement strategy, these conditions cannot be restored to the minimum task requirements. Taking group 4 as an example, the performance curves for the two strategies are shown in 

Fig. 13. The performance of strategy 1 can only reach 1.94 after recovery, which does not meet the minimum task requirements. Although the time required for strategy 2 to reach a steady state after placement lags behind that of strategy 1, the performance is recovered to 2.24, which meets the task requirements. Thus, strategy 2 has a higher system resilience. 

c). Case of three damaged UAVs. As shown in Table 8, we considered eight groups of cases in which three adjacent components lost their function. In this case, it was found that regardless of the recovery strategy used, the resilience could not be improved in the simulations. Thus, the recovered network performance cannot satisfy the task requirements. At this point, the swarm can no longer effectively perform its original tasks. To ensure the basic abilities of the swarm, the task requirements were changed to $\overline{Q}(t) = 1, t \in (T_d^2, T)$ . Thus, the basic IE ability between swarm individuals was maintained, and the swarm returned safely without disintegrating. The simulation results are listed in Tables 9 and Fig. 14. The optimal placement scheme was not realized in groups 2 and 7, hence the currently damaged UAV has the least impact on the resilience, and maintaining the current topology is the recovery measure with the highest resilience. The other six groups experienced a significant decline in network performance. Strategy 1 has difficulty restoring network performance, whereas strategy 2 restores basic IE capabilities via swarm topology reconstruction. 

Considering the first group as an example, the performance curve for the task process is displayed in Fig. 15. The network task requirement was initially set to two. After the second disturbance, the task requirements were changed to ensure the basic IE capability of the swarm. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/9861a30dc657ddbe6a67fb332ae0c01f9c48de61bd6d043c4c8fe8cbda07169e.jpg)



Fig. 14. Comparison of resilience of each group when three UAVs are damaged.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/e32a5d733a1aa836e89c9d76a1f7ea280a8fe0d9cc4f5060f98e49178d1105fa.jpg)



Fig. 15. Network performance curves for group 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/c92e5156-8943-41f6-8a3e-8a36296f6d89/560f24db46851c8db3671611059966bd4ed9375785de1102b2cb23725c94b2b9.jpg)



Fig. 16. Network performance curves for group 1 in different optimal objects.


Accordingly, the recovery performance of strategy 1 finally stabilized at 0.867, which did not meet the requirements. Meanwhile, strategy 2 met the new task requirements and finally stabilized at 1.55. Therefore, strategy 2 significantly improved the resilience level of the system after the task requirements were changed, ensuring the basic IE capability of the swarm. 

The optimization objective adopted in strategy 2 is to achieve the highest system resilience; If the optimization objective is to achieve the highest network performance, placement scheme (7-11-15) can also restore the network performance level to 1.55. The performance curves for the two optimization strategies are shown in Fig. 16. Although the two schemes eventually achieve the same performance level, the placement scheme with optimal resilience reduces the relative moving distance of a UAV. Therefore, positions can be filled more quickly, and the performance level of the network can be recovered faster. Meanwhile, if only the performance level is considered, the time factor cannot be considered, which further reflects the comprehensive performance ability of resilience. 

# 5. Conclusions

In this study, we modeled a UAV swarm IE network as a multistate network. A semi-Markov process was adopted to model the change in the state probability distribution of the IE link when the UAV swarm exhibited resilient behaviors. In addition, a resilience-based IE topology reconstruction method was proposed to determine the optimal candidates for damaged drones. Before applying the simulation, a UAV IE test 

was conducted to obtain the probability distributions of the data flow between UAVs. Accordingly, simulations were performed to evaluate the resilience when different recovery strategies were used. The results show that the proposed models help us gain understanding of the performance changes of a UAV swarm during the entire resilience process. Subsequently, based on assessment, the optimized resilience method can improve swarm resilience through UAV redeployment. Consequently, the analysis of the resilience of a UAV swarm using the method proposed in this study can enable unmanned swarm designers to understand the complete mission status, and thus aid the design of a UAV swarm and mission plan. 

Another distinguishing feature of UAV swarms is the highly dynamic topology under certain scenarios. The dynamics of the network configuration pose challenges to the performance and resilience evaluation of a UAV swarm. In future studies, we plan to further consider dynamic and randomness factors in UAV swarm resilience analysis, as well as propose corresponding strategies for resilience enhancement. 

# Author statement

Tao Liu conceived and designed the methodology and model; Guanghan Bai and Junyong Tao proposed the idea of this paper; Yun-an Zhang coded the algorithms; Yining Fang designed the experiments and analyzed the data. All authors have contributed to the editing and proofreading of this paper. 

# CRediT authorship contribution statement

Tao Liu: Writing - original draft, Methodology. Guanghan Bai: Funding acquisition. Junyong Tao: Supervision. Yun-An Zhang: Software, Data curation. Yining Fang: Writing - review & editing. 

# Declaration of Competing Interest

The authors report no conflict of interest and have received no payment in preparation of this manuscript. 

# Data availability

No data was used for the research described in the article. 

# Acknowledgment

This work was supported by the National Natural Science Foundation of China (Grant No.72271242) and the Hunan Provincial Natural Science Foundation of China for Excellent Young Scholars (Grant No.2022JJ20046). 

# References



[1] Zhen Z, Chen Y, Wen L, Han B. An intelligent cooperative mission planning scheme of UAV swarm in uncertain dynamic environment. Aerospace Science and Technology 2020;100:105826. 





[2] Jia, T., Xu, H., Yan, H., & Du, J. (2020). Transactions of Nanjing University of Aeronautics and Astronautics (04), 528-538. doi:10.16356/j.1005-1120.2020.04.004. 





[3] Kim J, Oh H, Yu B, Kim S. Optimal task assignment for UAV swarm operations in hostile environments. International Journal of Aeronautical and Space Sciences 2020;22:456-67. 





[4] Pang B, Hu X, Dai W, Low KH. UAV path optimization with an integrated cost assessment model considering third-party risks in metropolitan environments. Reliability Engineering & System Safety 2022;222:108399. 





[5] Peng R. Joint routing and aborting optimization of cooperative unmanned aerial vehicles. Reliability Engineering & System Safety 2018;177:131-7. 





[6] Gao C, Zhen Z, Gong H. A self-organized search and attack algorithm for multiple unmanned aerial vehicles. Aerospace Science and Technology 2016;54:229-40. 





[7] Chen J, Zhang X, Xin B, Fang H. Coordination between unmanned aerial and ground vehicles: a taxonomy and optimization perspective. IEEE Transactions on Cybernetics 2016;46:959-72. 





[8] Capitan J, Merino L, Ollero A. Cooperative decision-making under uncertainties for multi-target surveillance with multiple UAVs. Journal of Intelligent & Robotic Systems 2016;84:371-86. 





[9] Adamey E, Oguz AE, Ozgüner U. Collaborative multi-MSA multi-target tracking and surveillance: a divide & conquer method using region allocation trees. Journal of Intelligent & Robotic Systems 2017;87:471-85. 





[10] Liu L, Yang J. A dynamic mission abort policy for the swarm executing missions and its solution method by tailored deep reinforcement learning. Reliability Engineering & System Safety 2023;234:109149. 





[11] Levitin G, Xing L, Dai Y. Co-optimizing component allocation and activation sequence in heterogeneous 1-out-of-n standby system exposed to shocks. Reliability Engineering & System Safety 2022;230:108962. 





[12] Zhu X, Yan R, Peng R, Zhang Z. Optimal routing, loading and aborting of UAVs executing both visiting tasks and transportation tasks. Reliability Engineering & System Safety 2020;204:107132. 





[13] Gupta L, Jain R, Vaszkun G. Survey of important issues in UAV communication networks. IEEE Communications Surveys & Tutorials 2016;18:1123-52. 





[14] Valentini G, Moore DG, Hanson JR, Pavlic TP, Pratt SC, Walker SI. Transfer of information in collective decisions by artificial agents. IEEE Symposium on Artificial Life 2018. 





[15] Dui H, Zhang C, Bai G, Chen L. Mission reliability modeling of UAV swarm and its structure optimization based on importance measure. Reliability Engineering & System Safety 2021;215:107879. 





[16] Bekmezci I, Sahingoz OK, Temel S. Flying ad-hoc networks (FANETs): a survey. Ad Hoc Networks 2013;11:1254-70. 





[17] Xu B, Liu T, Bai G, Tao J, Zhang Y, Fang Y. A multistate network approach for reliability evaluation of unmanned swarms by considering information exchange capacity. Reliability Engineering & System Safety 2021;219:108221. 





[18] Tran HT, Balchanos M, Domercant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliability Engineering & System Safety 2017;158:73-84. 





[19] Bai G, Li Y, Fang Y, Zhang Y, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliability Engineering & System Safety 2020;193:106602. 





[20] Li H, Sun Q, Wang M, Liu C, Xie Y, Zhang Y. A baseline-resilience assessment method for UAV swarms under heterogeneous communication networks. IEEE Systems Journal 2022;16:6107-18. 





[21] Wang X, Zhang Y, Wang L, Lu D, Zeng G. Robustness evaluation method for unmanned aerial vehicle swarms based on complex network theory. Chinese Journal of Aeronautics 2020;33:352-64. 





[22] Liu C, Zhang Z. Towards a robust FANET: distributed node importance estimation-based connectivity maintenance for UAV swarms. Ad Hoc Networks 2021;125: 102734. 





[23] Cai Q, Alam S, Pratama M, Liu J. Robustness evaluation of multipartite complex networks based on percolation theory. IEEE Transactions on Systems, Man, and Cybernetics: Systems 2021;51:6244-57. 





[24] Feng Q, Liu M, Dui H, Ren Y, Sun B, Yang D, Wang Z. Importance measure-based phased mission reliability and UAV number optimization for swarm. Reliability Engineering & System Safety 2022;223:108478. 





[25] Wang L, Zhao X, Zhang Y, Wang X, Ma T, Gao X. Unmanned aerial vehicle swarm mission reliability modeling and evaluation method oriented to systematic and networked mission. Chinese Journal of Aeronautics 2020;34(2):466-78. 





[26] Wang C, Xing L, Yu J, Guan Q, Yang C, Yu M. Phase reduction for efficient reliability analysis of dynamic k-out-of-n phased mission systems. Reliability Engineering & System Safety 2023;237:109349. 





[27] Xie X, Li J, Huang Z, Yang Q, Kwak KS. Coupled-map-lattices-based vulnerability assessment of UAV network in interference scenarios. Wireless Communications and Mobile Computing 2022;5:1-14. 





[28] Yang S, Hou Z, Chen H. Evaluation of vulnerability of MAV/UAV collaborative combat network based on complex network. Chaos, Solitons & Fractals 2023;172: 113500. 





[29] Tran HT, Domercant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems☆. Procedia Computer Science 2016;95:126-33. 





[30] Zuo MJ. System reliability and system resilience. Frontiers of Engineering Management 2021;8:615-9. 





[31] Bai G, Wang H, Zheng X, et al. Improved resilience measure for component recovery priority in power grids. Frontiers of Engineering Management 2021;8:545-56. https://doi.org/10.1007/s42524-021-0161-5. 





[32] Li H, Sun Q, Zhong Y, Huang Z, Zhang Y. A soft resource optimization method for improving the resilience of UAV swarms under continuous attack. Reliability Engineering & System Safety 2023;237:109368. 





[33] Sun Q, Li H, Wang Y, Zhang Y. Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems. Reliability Engineering & System Safety 2022;222:108426. 





[34] Phadke A, Medrano FA. Towards resilient UAV swarms—A breakdown of resiliency requirements in UAV swarms. Drones 2022;6:11. 





[35] Hu N, Tian Z, Sun Y, Yin L, Zhao B, Du X, Guizani N. Building agile and resilient UAV networks based on SDN and Blockchain. IEEE Network 2021;35:57-63. 





[36] Mou Z, Gao F, Liu J, Wu Q. Resilient UAV swarm communications with graph convolutional neural network. IEEE Journal on Selected Areas in Communications 2021;40:393-411. 





[37] Vachtsevanos GJ, Lee BD, Oh S, Balchanos M. Resilient design and operation of cyber physical systems with emphasis on unmanned autonomous systems. Journal of Intelligent & Robotic Systems 2018;91:59-83. 





[38] Tran HT. A complex networks approach to designing resilient system-of-systems. Georgia Institute of Technology; 2016. 





[39] Cheng C, Bai G, Zhang Y, Tao J. Resilience evaluation for UAV swarm performing joint reconnaissance mission. Chaos 2019;29(5):053132. 





[40] Srivastava A, Prakash J. Future FANET with application and enabling techniques: anatomicization and sustainability issues. Computer Science Review 2021;39: 100359. 





[41] Reynolds CW. Flocks, herds, and schools: a distributed behavioral model. Computer Graphics 1998;21(4):273-82. 





[42] Vicsek T, Czirók A, Ben-Jacob E, et al. Novel type of phase transition in a system of self-driven particles. Physical Review Letters 1995;75(6):1226-9. 





[43] Couzin ID, Krause J, Franks NR, et al. Effective leadership and decision-making in animal groups on the move. Nature 2005;433(7025):513-6. 





[44] Liu T, Bai G, Tao J, Zhang Y, Fang Y, Xu B. Modeling and evaluation method for resilience analysis of multi-state networks. Reliability Engineering & System Safety 2022;226:108663. 





[45] Dui H, Si S, Zuo MJ, Sun S. Semi-Markov process-based integrated importance measure for multi-state systems. IEEE Transactions on Reliability 2015;64:754-65. 





[46] Castanon LJ, Zuluaga JR, Naredo JL. Numerical Laplace inversion methods for electromagnetic transient simulations. In: IEEE 2016 North American Power Symposium (NAPS); 2016. p. 1-6. https://doi.org/10.1109/NAPS.2016.7747864. 





[47] Liu T, Bai G, Tao J, Zhang Y, Fang Y. Mission-oriented resilience evaluation method for complex system. Systems Engineering and Electronics 2021;43(4):1003-11. 





[48] Yang XS. Nature-inspired metaheuristic algorithms[M]. Beckington: Luniver press; 2010. 





[49] Dijkstra EW. A note on two problems in connexion with graphs. Numerische Mathematik 1959;1:269-71. 





[50] Wenxing L, Muqing W, Min Z, Peizhe L, Tianze L. Hop count limitation analysis in wireless multi-hop networks. International Journal of Distributed Sensor Networks 2017;13:1-13. 





[51] Ixia. ixChariot. [Online] available at: https://www_keysight.com/us/en/products/network-test/performance-monitoring/ixchariot.html. 





[52] Latal J, Wilcek Z, Kolar J, Vojtěch J, Šarlej F. Measurement of performance parameters of multimedia services on a hybrid access network xPON/xDSL. In: 2019 21st International Conference on Transparent Optical Networks (ICTON); 2019. p. 1-7. 





[53] Kyrbashov B, Baronak I, Kovacic M, Janata V. Evaluation and investigation of the delay in VoIP networks. Radioengineering 2011;20(2). 





[54] Barnes WJ. Feasibility of a cognitive extension to existing 802.11b wireless devices. The University of Oklahoma; 2009. 





[55] Liu T, Bai G, Tao J, et al. An improved bounding algorithm for approximating multistate network reliability based on state-space decomposition method. Reliability Engineering and System Safety 2021;210:07500. 

