# A soft resource optimization method for improving the resilience of UAV swarms under continuous attack

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/bcc6af0dca32b9ca06fc04382c5913d44f4381c004773002d6415c8b5a411336.jpg)


Hongxu Li, Qin Sun, Yuanfu Zhong, Zhiwen Huang, Yingchao Zhang 

School of Systems Science and Engineering, Sun Yat-sen University, Guangzhou 510006, PR China 

# ARTICLE INFO

Keywords: 

Resilience 

Soft resource optimization 

Unmanned aerial vehicle swarms 

Continuous attack 

# ABSTRACT

Resilience is a comprehensive metric that measures the ability of an unmanned aerial vehicle (UAV) swarm to resist and recover after being attacked. Improving resilience is critical when UAV swarms still need to perform their intended mission after being attacked. Although studies have shown that adding UAVs or changing communication links can improve the resilience of UAV swarms, these enhancement methods cannot be the first choice due to the limitations of physical resources and mission benefits. In addition, these studies focus more on the single attack but ignore the continuous attack. Therefore, a method for improving the resilience of UAV swarms under continuous attack is proposed in this paper from the perspective of soft resource optimization. Firstly, a resilience measurement method considering cost and benefit is proposed. Unlike previous studies, the resilience measurement method given in this paper is from the perspective of missions rather than the structure of swarms. Secondly, a soft resource optimization model to improve the resilience of UAV swarms under continuous attack is constructed, and the solution algorithm of the model is given. Finally, the feasibility and superiority of the model and algorithm are verified by simulation experiments. 

# 1. Introduction

Unmanned aerial vehicles (UAVs), also known as flying robots, have been widely used in military reconnaissance, agricultural irrigation, disaster rescue, and other fields by taking advantage of their low cost, flexible action, and solid environmental adaptability [1]. However, the mission capabilities exhibited by single UAVs when performing large-scale missions are limited. Therefore, the UAV swarms have gradually become the focus of scholars. Through powerful resource sharing and team collaboration capabilities, UAV swarms can more easily handle complex and large-scale missions [2]. 

In fact, after the continuous research of scholars, the UAV swarm has gradually moved from science fiction to reality, and its development has begun to take shape. A recent exciting paper titled Swarm of micro-flying robots in the wild confirms this view. This paper enables swarms of UAVs to fly in groups in highly cluttered and even unknown environments [3]. Soria also wrote in the review article, "An optimal planning algorithm enables swarms of flying robots to explore novel environments autonomously and safely"[4]. Regarding the technical research on other UAV swarms, Jiang et al. have conducted detailed metrological statistics, which is enough to see that the UAV swarms have apparent advantages and are developing rapidly [5]. However, these studies also have a problem that cannot ignore: the assumed external environment is peaceful. It is undeniable that the missions 

performed by UAV swarms are not all peaceful ones. On the contrary, UAV swarms are better at performing some tedious and dangerous missions, which leads to the fact that UAV swarms are often in harsh environments during the mission [6]. 

As we all know, there are a lot of external disturbances in harsh environments, which can be natural or artificial. For example, in a complex battlefield environment, a UAV swarm may face electromagnetic interference and severe weather interference simultaneously, resulting in the interruption of communication, loss of function, and even damage to the UAV swarm [7-9]. Due to these external disturbances, the ability of UAV swarms to perform missions is seriously affected, thereby reducing battlefield benefits. In previous studies, scholars have proposed different schemes to improve the overall anti-jamming capability of complex systems, among which the research on robustness [10-12], reliability [13-16], and vulnerability [17,18] is very representative. The purpose of these properties is to make complex systems such as UAV swarms more robust in harsh environments, thereby reducing the loss in mission revenue due to external interference. However, the problems with these performances are also pronounced, and the focus is only on exploring the ability of the swarm system to resist and absorb disturbance. It is worth noting that the value of the UAV swarm is to complete the specified mission and obtain the maximum mission benefit. But blindly exploring the stress resistance of UAV swarms does not 

allow it to bring more mission benefits. Compared with properties such as robustness and fragility, resilience, as a relatively novel performance representing overall capability, has attracted the attention of scholars. From a comprehensive and systematic perspective, resilience discusses resistance and recovery, allowing UAV swarms to gain more mission benefits. 

The famous ecologist Holling first noticed the concept of resilience in a 1973 paper called Resilience and Stability of Ecological Systems[19]. Early resilience research focused on natural resilience, and around 1980, resilience began to be widely used in various fields, such as psychology [20], sociology [21], and engineering [22]. Research on the resilience of swarm systems has recently become a hotspot [23-28]. For ease of study, these swarm systems are described as complex networks in which the elements and the connections between elements in the swarm system represent topologically as nodes and lines, respectively. Scholars have attempted to characterize the resilience of swarm systems by exploring the properties of complex networks [29-33]. As a particular swarm system, the resilience of the UAV swarm usually characterizes in the way mentioned above. 

The resilience research of UAV swarms carry out mainly from two aspects: resilience assessment and resilience improvement. On the one hand, Cheng et al. [34] explored the resilience evaluation method of UAV swarms when performing joint reconnaissance missions and gave a resilience evaluation framework. Bai et al. [35] explored the evaluation method of resilience based on the UAV swarm considering the communication distance. Sun et al. [36] proposed a complex network-based baseline resilience assessment method for UAV swarms based on [34,35]. Zhang et al. [9] also presented a resiliency evaluation framework for UAV swarms from the perspective of information traffic load balancing. Considering the heterogeneity of UAV swarms, Li et al. [37] presented a baseline resilience assessment method based on heterogeneous communication networks. On the other hand, Saulnier et al. [38] proposed a dynamic connection management method for communication networks to ensure that the UAV swarms achieve resilience consensus in the direction of movement. Ramachandran et al. [39,40] used the method of communicating with other UAVs to automatically reconfigure communication resources to improve the resilience of UAV swarms. Mou et al. [6] used a graph convolutional neural network to quickly reconstruct the communication connectivity to improve the resilience of UAV swarms. Sun et al. [41] adopted a collaborative strategy between UAV swarms to achieve a multi-cluster resilient, steady state. 

The above studies show that adding UAVs or changing communication links can improve the resilience of UAV swarms. However, in a harsh environment, these lifting methods are challenging to achieve due to the limitations of physical resources and mission benefits. In other words, using these lifting methods is the last resort. In fact, without changing the physical resources, it is also an excellent way to improve the mission benefits of the UAV swarm by changing the mission plan of the existing material resources. We prefer to call it soft resource optimization. The advantage of the soft resource optimization method is that there is no need to replace or change the existing physical resources, which optimizes the resource cost and the time cost required for mission handover. For example, two UAVs with a strike capability of 5 perform three strike missions, respectively. If one of the UAVs is damaged by a strike during the second mission, the other UAVs can take over the remaining two missions of the struck UAVs instead of sending a new one. The soft resource optimization method improves the overall benefit of the mission by rationally utilizing the redundant mission execution capability of the UAV swarm. Although the soft resource optimization method does not show a leap-forward improvement in mission benefits compared with the violent process of changing physical resources, it is a required transitional and emergency improvement method. In other words, water afar quenches, not fire. 

Based on the above, this paper proposes a method for improving the resilience of UAV swarms under centralized control architecture from the perspective of soft resource optimization. The expected contributions of this study are as follows: 

- This paper proposes a new resilience measure from the perspective of UAV cost and mission benefit. Compared with measuring UAV swarm resilience from a structural point of view, the method proposed in this paper is more practical. From a valuable point of view, the mission of the UAV swarm is to maximize the benefits of the mission rather than just considering whether its defense capabilities are enhanced. 

- A soft resource optimization model for improving the resilience of UAV swarms under continuous attack is constructed, and the soft resource optimization model is given. The advantage of the soft resource optimization model is that it saves the resource cost and time cost caused by the replacement or change of physical resources. 

- The feasibility and superiority of the model and algorithm are verified by simulation experiments. The experimental results show that the model solution algorithm can improve the resilience of the UAV swarm under centralized control architecture. 

The remainder of this paper is organized as follows. Some background will be introduced in Section 2. A soft resource optimization model and solution algorithm to improve the resilience of UAV swarms under centralized control architecture will be constructed in Section 3. Simulation experiments to verify the feasibility and superiority of the models and algorithms will be given in Section 4. Some conclusions will be presented in Section 5. 

# 2. Background

Some basic concepts about UAV swarms and resilience will be reviewed in this section, which will be aided in understanding the problem description. 

# 2.1. Control architecture of UAV swarms

The control architecture of the UAV swarms determines the transmission path of command information and status information. The current mainstream control architectures of UAV swarms are centralized and distributed control architectures. In practical applications, a centralized control architecture is more popular. The main reason is that the centralized control architecture has strong controllability and stability for the UAV swarms [42]. The centralized control architecture of the UAV swarms is mainly composed of UAV swarms, a control base station, and a communication link. The control base station transmits the instruction information to the UAV swarms through the communication link. On the contrary, the UAV swarms feedback the status information to the control base station through the communication link, as shown in Fig. 1. 

UAV swarms can more effectively complete large-scale missions by their group characteristics, but their complex internal structures and communication relationships are challenging to characterize. In recent years, complex networks have been frequently used to describe the structure and communication relationships of UAV swarms [13,14,30, 35,43,44]. In this process, the complexity of the topology process is reduced, and an excellent topology effect is achieved. According to the centralized control architecture of the UAV swarms, the topology of the UAV swarms can be obtained using a complex network approach, as shown in Definition 2.1. 

Definition 2.1. Let $G = (U, L)$ be an undirected graph, where $U = \{u_1, u_2, \ldots, u_n\}$ denotes a UAV swarm, $L = \{l_1, l_2, \ldots, l_n\}$ denotes a set of communication links between the UAV and the control base station, and the communication link between each $u_i$ and the control base station corresponds to $l_i$ , $i = 1, 2, \ldots, n$ . 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/3a50652d1fe1766f2b0a9031f8c2e816129f069535825342baed20f1d66b5a29.jpg)



(a) Schematic diagram of centralized control architecture of UAV swarms


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/cd0282ce0f8152528412fd124c967a90c99220f19e7ede54d0526c597947b5f0.jpg)



(b) Structure diagram of centralized control architecture of UAV swarms



Fig. 1. Centralized control architecture of the UAV swarms.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/1875e2950eb9a48dcb764baf3dcbf6c3ada7171c3f387e012d5f8e2ad3b9cd1c.jpg)



Fig. 2. Resilience process of UAV swarms.


# 2.2. Resilience process of UAV swarms

The UAV swarms resilience process division is crucial for exploring resilience measurement. Various UAV swarms resilience processes have been studied by scholars, and the general division model is shown in Fig. 2. 

The resilience process of UAV swarms is mainly divided into four periods, including the initial period, resistance period, recovery period, and stabilization period. The initial period is the dynamic stabilization stage of the performance of the UAV swarms before being attacked, and the performance value at this time is at a high level in the entire resilience process. The resistance period refers to the period from the attack on the UAV swarm to the performance minimum. After the UAV swarm is attacked, the dynamic stability of performance will be broken, and the performance will drop rapidly until it drops to a minimum value. The recovery period is mainly the period from the minimum performance to the dynamic stability of performance recovery. The performance of the UAV swarms can be quickly recovered through different improvement methods. Still, due to the damage to the physical system, the performance cannot be restored to the initial state. The stable period mainly refers to the recovery of the performance of the UAV swarms to a dynamic stable state. 

# 3. Methodology

After reviewing some representative works, the resilience metric of UAV swarms under centralized control architecture, the soft resource optimization model for improving the resilience of UAV swarms under centralized control architecture, and the solving algorithm of the model will be described in detail in this section. 

# 3.1. Resilience metric of UAV swarms

The resilience metric of UAV swarms is a meaningful work that describes the system state of UAV swarms in the face of extremist attacks in a quantitative way comprehensively and systematically. The description of this state can be developed from the perspective of the structure of the UAV swarms, and it can also be designed from the perspective of the cost or benefit of the UAV swarms. But the latter is more conducive to discussing resource utilization, which is another perspective on the performance of UAV swarms. Therefore, this subsection will explain the resilience metric from the cost and benefit of UAV swarms performing missions. 

# 3.1.1. Performance metric

Let $U = \{u_{1}, u_{2}, \dots, u_{n}\}$ be characterized as a UAV swarm, and $T = \{T_{1}, T_{2}, \dots, T_{m}\}$ denote the set of missions to be performed by the UAV swarm. $|U| = n$ and $|T| = m$ are the number of UAVs and missions, respectively. The command and control structure of the UAV swarm is a centralized control structure, and all UAVs are subject to the unified deployment of the control base station. The combat instructions are transmitted from the control base station to the UAV terminal through the communication network, and the status information of the UAV is also transmitted to the control base station through the combat network. There is no mutual communication between UAVs. The graph topology satisfies Definition 2.1. The UAV swarms perform missions in a two-dimensional Euclidean space $\mathbb{R}^2$ , at any time $t$ , the position of the $u_{i}$ is $(x_{i}^{U}(t), y_{i}^{U}(t))$ , $i = 1, 2, \dots, n$ . In addition, given the area where the UAV swarms perform missions, and the area where the missions are performed contains a limited number of missions to be performed, and the horizontal position of the missions is $(x_{j}^{T}, y_{j}^{T})$ , $j = 1, 2, \dots, m$ . The UAV swarm has an initial mission execution sequence $\Delta = \langle \Delta_{1}, \Delta_{2}, \dots, \Delta_{n} \rangle$ , where $\Delta_{i} = \left\langle M_{1}^{i}, M_{2}^{i}, \dots, M_{z}^{i} \right\rangle$ , $i = 1, 2, \dots, n$ , and $z$ is the number of missions in $\Delta_{i}$ . Then the completion time $\Phi_{i}, i = 1, 2, \dots, n$ of the mission performed by the UAV can be given, as shown in Eq. (1). 

$$
\left\{ \begin{array}{c} \Phi_ {i} \left(M _ {1} ^ {i}\right) = \frac {\operatorname {d i s t} \left(\Gamma_ {i} , M _ {1} ^ {i}\right)}{v _ {i}} + T _ {e} \left(M _ {1} ^ {i}\right) \\ \Phi_ {i} \left(M _ {k} ^ {i}\right) = \Phi_ {i} \left(M _ {k - 1} ^ {i}\right) + \frac {\operatorname {d i s t} \left(M _ {k - 1} ^ {i} , M _ {k} ^ {i}\right)}{v _ {i}} + T _ {e} \left(M _ {k} ^ {i}\right), k = 2, 3, \dots , z \\ \Phi_ {i} \left(M _ {e} ^ {i}\right) = \Phi_ {i} \left(M _ {z} ^ {i}\right) + \frac {\operatorname {d i s t} \left(M _ {z} ^ {i} , \Gamma_ {i}\right)}{v _ {i}} \end{array} \right. \tag {1}
$$

where $T_{e}(M)$ represents the time required to perform mission $M$ , and $\Gamma_{i}$ is the initial position coordinates of the UAV. The meaning of $M_{e}^{i}$ is that the UAV returns to the initial position after completing the missions in the order in the mission sequence. $dist(\cdot)$ represents the calculation of Euclidean distance 

Let $\mathbf{H}(t) \in \{0,1\}^{n \times m}$ denote the decision variable matrix at planned time $t \in [0, t_{end}]$ , as shown in Eq. (2). 

$$
\mathbf {H} (t) = \left[ \mathbf {h} _ {1} (t), \mathbf {h} _ {2} (t), \dots , \mathbf {h} _ {n} (t) \right] ^ {\mathrm {T}}, \tag {2}
$$

where $\mathbf{h}_i(t) = \left[h_i^{(1)}(t),h_i^{(2)}(t),\dots,h_i^{(m)}(t)\right]\in \{0,1\} ^m$ and 

$$
\left\{ \begin{array}{l l} h _ {i} ^ {(j)} (t) = 0 & i f t \neq \Phi_ {i} \left(M _ {j} ^ {i}\right) \\ h _ {i} ^ {(j)} (t) = 1 & i f t = \Phi_ {i} \left(M _ {j} ^ {i}\right) \end{array} . \right. \tag {3}
$$

The profit of the UAV swarm through carrying out the mission is mainly affected by cost and revenue. These two elements are described in detail below. 

# 1. Revenue of UAV swarm

The income of the UAV swarm mainly refers to the behavior of obtaining the value attached to the mission by executing the mission. Every mission to be accomplished has value. Depending on the attributes of the mission, the value will vary. The revenue $P(t) \in \mathbb{R}_{+}$ from the mission performed by the UAV swarm at time $t$ is shown in Eq. (4). Note that in this paper, we define $\| A\| _1$ as the sum of the absolute values of all the elements of matrix $A$ . 

$$
P (t) = \left\| \mathbf {R} (t) \mathbf {H} (t) \mathbf {V a l} ^ {\mathrm {T}} \right\| _ {1}, \tag {4}
$$

where $\mathbf{Val} \in \mathbb{R}_+^{1 \times m}$ represents the mission value vector, and $\mathbf{R}(t) = \mathrm{diag}\left(r_1(t), r_2(t), \ldots, r_n(t)\right) \in \{0, 1\}^{n \times n}$ is a diagonal matrix, representing the state vector of the UAV swarm at time $t$ . The state of the UAV is mainly divided into a normal working state and a stop state. The normal working state includes the flight stage after the UAV takes off and the mission completion stage. The stop state mainly includes the stage when the UAV stops working due to its own or external force. Therefore, suppose $Q$ is the set of UAV numbers that can continue to complete the mission, then $U \backslash Q$ denotes the set of UAV numbers that are attacked, and we have 

$$
r _ {i} (t) = \left\{ \begin{array}{l l} 1 & i f \quad \left\{i \notin U \backslash Q \mid U \backslash Q \neq \emptyset \right\} \quad o r \quad U \backslash Q = \emptyset \\ 0 & i f \quad \left\{i \in U \backslash Q \mid U \backslash Q \neq \emptyset \right\} \end{array} . \right. \tag {5}
$$

# 2. Cost of UAV swarm

The cost of the UAV swarm is mainly divided into two parts: damage cost and en-route loss. First, when the UAV swarm is attacked, some UAVs are damaged and cannot continue to perform the scheduled mission. At this time, the cost of these damaged UAVs is called the damage cost $D(t) \in \mathbb{R}_{+}$ of the UAV swarm, as shown in Eq. (6). 

$$
D (t) = \mathbf {1} ^ {\mathrm {T}} \left(\mathbf {I} _ {n} - \mathbf {R} (t)\right) \mathbf {C} \mathbf {o} ^ {\mathrm {T}}, \tag {6}
$$

where $\mathbf{C}\mathbf{o}\in \mathbb{R}_{+}^{1\times n}$ represents the cost vector of the UAV swarm. 

En-route loss $E(t) \in \mathbb{R}_+$ of UAV swarm refers to the total loss of UAV during the mission, such as energy loss, as shown in Eq. (7). 

$$
E (t) = \sigma \cdot \triangle t \cdot \left(\mathbf {I} ^ {\mathrm {T}} \mathbf {R} (t) \mathbf {V} ^ {\mathrm {T}}\right), \tag {7}
$$

where $\sigma \in [0,1]$ represents the comprehensive adjustment coefficient of the route loss, and $\mathbf{V} \in \mathbb{R}_{+}^{1\times n}$ represents the speed vector of the UAV swarm. $\triangle t$ is the time interval. In addition, the dynamic characteristics of the UAV are not considered in this paper. Only the kinematic characteristics are considered. 

Based on the cost and revenue of the UAV swarm, we can further calculate the profit $B$ obtained by the UAV swarm performing missions, as shown in Eq. (8). 

$$
B = \int_ {t = 0} ^ {t _ {\text {e n d}}} (P (t) - D (t) - E (t)) d t. \tag {8}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/092328f6cb0afd4ef66e01b3df647ec3643166a74d602652c2940705ae18a155.jpg)



Fig. 3. Continuous resilience within the mission cycle of the UAV swarm.


In particular, when the UAV swarm is not under any attack and keeps executing the mission according to the established mission plan, the expected revenue $\bar{B}$ of the UAV swarm is shown in Eq. (9). 

$$
\bar {B} = \int_ {t = 0} ^ {t _ {\text {e n d}}} (\bar {P} (t) - \bar {E} (t)) d t, \tag {9}
$$

where $\bar{P}(t) = \left\|\mathbf{H}(t)\mathbf{V}\mathbf{a}^{\mathrm{T}}\right\|_1$ and $\bar{E}(t) = \sigma \cdot \Delta t \cdot (\mathbf{1}^{\mathrm{T}}\mathbf{I}_n\mathbf{V}^{\mathrm{T}})$ represent the expected revenue and expected en-route loss cost of the UAV swarm performing the mission at time $t$ , respectively. 

According to Eq. (8) and Eq. (9), the performance $P(\tilde{t}) \in [0,1]$ of the UAV swarm at time $\tilde{t}$ is shown in Eq. (10). 

$$
\begin{array}{l} P (\tilde {t}) = 1 - \frac {\bar {B} - B (\tilde {t})}{\bar {B}} \\ = 1 - \frac {\int_ {t = 0} ^ {t _ {e n d}} \left(\bar {P} (t) - \bar {E} (t)\right) d t - \int_ {t = 0} ^ {t _ {e n d}} \left(P _ {\bar {t}} (t) - D _ {\bar {t}} (t) - E _ {\bar {t}} (t)\right) d t}{\int_ {t = 0} ^ {t _ {e n d}} \left(\bar {P} (t) - \bar {E} (t)\right) d t}, \tag {10} \\ \end{array}
$$

where $\tilde{t} \in [0, \tilde{t}_{end}]$ represents the actual time, and when the last UAV completes the mission sequence, $\tilde{t} = \tilde{t}_{end}$ . In addition, when $\bar{B} = B(\tilde{t})$ , $P(\tilde{t}) = 1$ , which means that the profit obtained by the UAV swarm during mission execution reaches the expected profit, which is the maximum profit that the UAV swarm can bring, and the UAV swarm performance is also the maximum value one at this time. Because if the initial mission plan does not change, the UAV swarm does not need to modify the initial mission plan, so it is expected that the profit obtained by the mission plan is the maximum profit. If the UAV is struck, the profit decreases, and when the profit is 0, that is, $B(\tilde{t}) = 0$ , the performance $P(\tilde{t})$ of the UAV swarm is also 0. 

# 3.1.2. Resilience assessment

As is known to all, a UAV swarm is not only attacked once in the process of carrying out the mission, but the attack is often presented with multiple segments of untimed attack, and the intensity of the attack is also different. Then, a resilience process cannot sufficiently characterize the performance change of a UAV swarm in the whole mission execution cycle, so this paper presents the continuous resilience process of a UAV swarm, as shown in Fig. 3. 

It can be seen from Fig. 3 that the UAV swarm is hit multiple times during the execution of the mission, not the only one. After the attack, the UAV swarm will recover its performance through some recovery methods. As a result, a continuous resilience process consisting of multiple resilience processes is formed, as shown by the solid line in 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/0e149d7ab1586696919166062dd357bb69a6091cb64f1153e062de356bafdcb9.jpg)



Fig. 4. The explanation of the research idea.


Fig. 3. The dotted line shows its performance when the UAV swarm is only attacked, and no recovery measures are taken. The performance corresponding to these two cases differs in the final steady-state stage. 

The resilience measurement of the UAV swarm during the mission sequence should consider both the locality and wholeness of the continuous resilience process. First, from a local point of view, the resistance $\theta_{p}$ of the UAV swarm to each attack should be considered. This phase mainly measures the performance degradation in $[\tilde{t}_{attack}^{p},\tilde{t}_{\min}^{p}]$ time intervals, and the measurement formula is shown in Eq. (11). 

$$
\theta_ {p} = \frac {P \left(\tilde {t} _ {\text {a t t a c k}} ^ {p}\right) - P \left(\tilde {t} _ {\min } ^ {p}\right)}{P \left(\tilde {t} _ {\text {a t t a c k}} ^ {p}\right)}, \tag {11}
$$

where $P(\tilde{\tau}_{attack}^p)$ and $P(\tilde{\tau}_{\min}^p)$ represent the initial and minimum performance values at the $p$ th attack time, respectively. 

More locally, the recovery $\mu_{p}$ of UAV swarms after implementing recovery strategies should also be considered, as recovery is a core capability of resilience. The strength and weaknesses of recovery ability are mainly reflected in the performance improvement measurement in $\left[\tilde{t}_{\min}^{p},\tilde{t}_{\text {recover }}^{p}\right]$ time intervals, and the measurement formula is shown in Eq. (12). 

$$
\mu_ {p} = \frac {P \left(\tilde {t} _ {\text {a t t a c k}} ^ {p}\right) - P \left(\tilde {t} _ {\text {r e c o v e r}} ^ {p}\right)}{P \left(\tilde {t} _ {\text {a t t a c k}} ^ {p}\right)}, \tag {12}
$$

where $P\left(\tilde{t}_{\text{recover}}^p\right)$ represents the recovery performance value at the $p$ th attack time. 

From the integrity perspective, the UAV swarm should consider the performance change of the whole mission cycle, that is, the measurement of the overall performance between $[0,\bar{t}_{end}]$ , as shown in Eq. (13). 

$$
\zeta = \frac {\int_ {\tilde {t} = 0} ^ {\tilde {t} _ {e n d}} P (\tilde {t}) d \tilde {t}}{P _ {0} \cdot \tilde {t} _ {e n d}}. \tag {13}
$$

Then, according to Eq. (11), Eq. (12), and Eq. (13), we can give the resilience measurement $R \in [0, 1]$ of the UAV swarm, as shown in Eq. (14). 

$$
R = \zeta \cdot \frac {1}{s} \sum_ {p = 1} ^ {s} \left(1 - \theta_ {p}\right) \left(1 - \mu_ {p}\right), \tag {14}
$$

where $s = \left|\left\{\left(\tilde{t}, P(\tilde{t})\right) \mid P'(\tilde{t}) = 0, P''(\tilde{t}) < 0\right\}\right| \leqslant N_{att}$ , $N_{att}$ is the number of times the UAV swarm is attacked. In particular, when the recovery process is not in effect, $P(\tilde{t}_{\min}^p) = P(\tilde{t}_{\text{recover}}^p)$ . 

# 3.2. Soft resource optimization model

The soft resource optimization model (SROM) is explored in detail in this section. Firstly, the research questions and research ideas are analyzed. Secondly, the assumptions of modeling are given. Then the objective function of the model is constructed. Finally, the constraints of the model are proposed. 

# 3.2.1. Research idea

The main problem studied in this paper is using the soft resource optimization method to improve the recovery of the UAV swarm after being attacked during the mission without changing the structure of the UAV swarm, including adding UAVs or changing the UAV communication link. The explanation of the research idea is shown in Fig. 4. 

The process of solving the research problem in this paper can be seen in Fig. 4. First of all, the location of the UAV swarm and the established mission is known, as are the initial mission sequence of the UAV swarm and the centralized command and control mode. Among them, an optimization algorithm can solve the initial mission sequence. Since this is not the problem to be explored in this paper, the initial mission sequence has been fixed. Over time, UAV swarms have come under attack during their missions. The figure shows that the attacked UAV still has some remaining planned missions to complete. The uncompleted mission information will be transmitted to the UAV swarms control base station along with the remaining UAV information. We have a picture of the transmission of data. When the information is passed through a computing device embedded with the SROM algorithm, the device gives the optimal solution from a finite number of solutions and packets the information back to the UAV swarm. In 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/416436fc16375278427b00536b26c7c94b4498e811d93e2ec4d37776e58ae546.jpg)



(a) UAV 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/f80cb1c7330d4eef65caae81dce273ebb654f3888664feb775842aaf4926469c.jpg)



(b) UAV 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/b4bd47e3b44ee725a14b889acc63ee2ae7dd09fe21e34e3a03ba1103ca0ccd41.jpg)



(c) UAV 3


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/6ec63142bf6579f7646a3ce8c1d858ebe0e7e326bd14ab746357255a1e01b716.jpg)



(d) UAV 4


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/83993e2cde1511ac6a191128d084146a441bb6101babb25bbe5c0e342d01b6d1.jpg)



(e) UAV 5



Fig. 5. The cumulative gain of each of the five UAVs.


this case, the UAV swarm will readjust the mission plan to achieve the purpose of performance recovery and ultimately improve the resilience of the UAV swarm. 

# 3.2.2.Assumptions

According to the research problems and research ideas, this paper makes assumptions about the model from preparation conditions, attack conditions, and recovery conditions. 

# Assumption 1 (Preparation Condition).

According to the different focus of this paper, some specific general assumptions are needed before the UAV swarm performs the mission. 

1. The initial mission sequence of the UAV swarm is known. 

This assumption was covered in detail when we discussed Fig. 4. This paper is independent of the initial mission sequence and focuses on the performance improvement of UAV swarm after damage. Therefore, even if different algorithms are used to calculate different initial mission sequences, it does not affect the conclusion of this paper. 

2. The initial speed of each UAV is determined, and it is assumed that it always travels at a constant speed. The ability to execute missions is defined and expendable. 

This assumption is made for the convenience of calculation. In practice, the speed of the UAV will not be uniform, but the change in speed is not considered in this paper. In addition, the mission capability of UAVs is also assumed to be expendable. The mission execution capability will be consumed after a mission is executed. 

3. The details of executing a mission are ignored, and only mission value, location, and execution time are considered. 

The details of the mission to be performed by the UAV fleet are not considered, including the nature of the mission and so on. Consider only three factors: mission value, location, and execution time. This assumption mainly eliminates the interference factors with low relevance to the research problem in this paper. 

Assumption 2 (Attack Condition). 

In this paper, we assume that the UAV swarm is attacked during the mission, and its attack is destructive to a single UAV. The specific performance is as follows: 

1. After the UAV is attacked, its communication link with the control base station is interrupted. 

This assumption ensures that the control base station can confirm the status of the UAV immediately after being attacked. An emergency recovery strategy is adopted to prevent the model from lagging in time. 

2. After the UAV is attacked, it can no longer continue to perform missions. 

In this paper, all UAV's functions are considered paralyzed when attacked, and partial function paralysis will not be considered. 

3. UAV swarms under continuous attack 

In this paper, the UAV swarm is under continuous attack. Continuous attack means that the UAV swarm is attacked at least once during the execution of the task, that is, the attack time and target are random, not targeted at a specific time and target. 

# Assumption 3 (Recovery Condition).

In this paper, the recovery method we take is a soft resource optimization method, which achieves the purpose of performance recovery by redistributing the redundant mission execution capability of the UAV swarm. We have the following assumptions: 

1. The UAV swarms should still have redundant mission execution capabilities after being attacked. 

This assumption guarantees the environment in which the optimization model can be used. The SROM can be used only when the UAV swarm is attacked and still has redundant mission execution capability. 

2. The unfinished mission sequence of the attacked UAV will be transmitted back to the control base station, waiting for reassignment. 

This assumption defines the data flow direction, and the remaining mission sequence will be transferred to the UAV swarm control base station for unified deployment. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/2857bc0907aa8099392caad663119a9423378196ae09d847fea113cd14e7f780.jpg)



(a) The overall cumulative gain


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/f71228da06639ec2f2af83bb8ec2412cf718bf7a7d463d9f7f5b5914dfc69be2.jpg)



(b) The normalized overall gain



Fig. 6. The overall cumulative gain and the normalized overall gain of the UAV swarm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/b6cffc63cb2f264364b52ce5b29e308c91502b247d2152d39733c04e467cfc1c.jpg)



Fig. 7. The performance of the UAV swarm.


3. The UAVs should not exceed their mission execution capabilities when taking over missions, and a mission can only be taken over by one UAV. 

This is the assumption of mission capability. All measures taken in this paper should meet the assumption of mission capability. Any behavior exceeding mission capability is regarded as invalid action. 

# 3.2.3. Objective function and constraints

According to the research ideas, the objective function and constraints of SROM are given in this section. First, the core goal of SROM is to minimize the profit loss of the attack on the UAV swarm as much as possible so that the UAV swarm can maximize the completion of the established mission. Therefore, in this subsection, the objective function of the SROM is the maximization of the resilience value of the UAV swarm, as shown in Eq. (15). 

$$
\max  R = \max  \zeta \cdot \frac {1}{s} \sum_ {p = 1} ^ {s} \left(1 - \theta_ {p}\right) \left(1 - \mu_ {p}\right) \tag {15}
$$

Eq. (15) not only maximizes the overall performance ratio but also minimizes the performance loss of the UAV swarm under each strike, which fully reflects the core objective of SROM. 

According to the assumptions, the constraints of SROM can be divided into three aspects: capacity constraints, allocation constraints, and decision variable constraints. 

# 1. Capacity constraints

In the assumption condition, the UAVs in the UAV swarm all have mission execution capability and belong to the consumptive capability. The setting of each UAV's initial mission execution capability is limited, and the following inequalities need to be satisfied. 

$$
\left(\int_ {t = 0} ^ {t _ {e n d}} \mathbf {H} _ {q} (t) d t\right) \mathbf {1} \leqslant \mathbf {C} ^ {\mathrm {T}}, \forall q \in [ 0, \tilde {t} _ {e n d} ], \tag {16}
$$

where $\mathbf{C} \in \mathbb{R}_{+}^{1 \times n}$ represents the initial mission execution capability vector of the UAV swarm. In addition, this paper stipulates that when two matrices $\mathbf{A}$ and $\mathbf{B}$ of the same dimension compare sizes, if all the elements in matrix $\mathbf{A}$ are less than or equal to the elements in the same position in matrix $\mathbf{B}$ , we will call $\mathbf{A} \leqslant \mathbf{B}$ . 

UAV swarms also need to accommodate only one UAV for each mission. It is not allowed to share a mission with more than one UAV. The constraint needs to satisfy Eq. (17). 

$$
\left(\int_ {t = 0} ^ {t _ {\text {e n d}}} \mathbf {H} _ {q} ^ {\mathrm {T}} (t) d t\right) \mathbf {1} = \mathbf {1}. \tag {17}
$$

# 2. Allocation constraints

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/ce17d8e6078f2f629a6b62e3c1bfeff298230083bd61283f224eee3f8457c46f.jpg)



(a) Mission plan at 14.72s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/6198a2aa027d8bff2a5d6063d497587805bcbfa20a704e10edbc1cc4055ca2b4.jpg)



(b) Mission plan at 15.72s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/90d018fa626175ca7bd035304b8a8c03ff11c866e31adbb61db8fe83b734d20b.jpg)



(c) Mission plan at 16.72s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/cfd1aa60389005c256a4c532221bacccb6d0d97b5909bf3b26c20173ec929a5e.jpg)



(d) Mission plan at 23.25s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/18ad2404e60bbea35e80d9338f78d8020fb05962a6c755862a583aa7e674e182.jpg)



(e) Mission plan at 24.25s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/08e8c452d681a766a45c461f4215100a75777fe76c1ff2b8f1366fa402a9e6d9.jpg)



(f) Mission plan at 25.25s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/b332179ab196e3b25d59580ad3e4b18dc16daf7e112bdc4923233832383536ec.jpg)



(g) Mission plan at 32.37s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/746e87ce93dbe8f5f2a1fd5edb3b597e86e5fbf8ef41381f690641e8bf7f59d8.jpg)



(h) Mission plan at 33.37s


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/222fc4ad6eab1155322af3eae1237679313448a7cc621a6440ea49bc8816b324.jpg)



(i) Mission plan at 34.37s



Fig. 8. The mission progress graph of the UAV swarm.


In the process of executing SROM, UAVs not only need to meet the capability constraints but also need to meet the basic allocation constraints. First, UAV swarms will reduce the number of missions carried out after a strike. Of course, the constant number of missions is a special case where the strike did not affect the UAV swarm. The constraint needs to satisfy the following inequality. 

$$
\int_ {t = 0} ^ {t _ {\text {e n d}}} \left(R _ {q} (t) \mid i \in U \backslash Q\right) \mathbf {H} _ {q} (t) d t \leqslant \int_ {t = 0} ^ {t _ {\text {e n d}}} \mathbf {H} _ {q} (t) d t, \forall q \in [ 0, \tilde {t} _ {\text {e n d}} ]. \tag {18}
$$

In addition, in a continuous resilience process, each strike of the UAV swarm will reduce the number of missions before the strike, and the equal sign also represents the case that the UAV swarm is not affected by the strike. 

$$
\int_ {t = 0} ^ {t _ {\text {e n d}}} \left(R _ {q} (t) \mid q = \tilde {t} _ {\min } ^ {p}\right) \mathbf {H} _ {q} (t) d t \leqslant \int_ {t = 0} ^ {t _ {\text {e n d}}} \left(R _ {q} (t) \mid q = \tilde {t} _ {\text {a t t a c k}} ^ {p}\right) \mathbf {H} _ {q} (t) d t. \tag {19}
$$

The above two constraints limit the state rationality when the UAV swarm is attacked, and the state rationality when recovery measures are taken will be discussed below. After the UAV swarm takes recovery measures, the number of missions with performance recovery should 

be between the highest and lowest values before and after the strike. When the number of missions is fully restored to the initial state, the equal constraint in the following equation is satisfied. 

$$
\left\| \int_ {t = 0} ^ {t _ {\text {e n d}}} \left(\mathbf {H} _ {q} (t) \mid q \in \left[ \tilde {t} _ {\text {r e c o v e r}} ^ {p}, \tilde {t} _ {\text {a t t a c k}} ^ {p + 1} \right]\right) d t \right\| _ {1} \leqslant \left\| \int_ {t = 0} ^ {t _ {\text {e n d}}} \mathbf {H} _ {\tilde {t} _ {\text {a t t a c k}} ^ {p}} (t) d t \right\| _ {1}. \tag {20}
$$

On the contrary, when the mission is not recovered, the equality constraint in the following equation is satisfied. 

$$
\left\| \int_ {t = 0} ^ {t _ {\text {e n d}}} \left(\mathbf {H} _ {q} (t) \mid q \in \left[ \tilde {t} _ {\text {r e c o v e r}} ^ {p}, \tilde {t} _ {\text {a t t a c k}} ^ {p + 1} \right]\right) d t \right\| _ {1} \geqslant \left\| \int_ {t = 0} ^ {t _ {\text {e n d}}} \mathbf {H} _ {\tilde {t} _ {\min } ^ {p}} (t) d t \right\| _ {1}. \tag {21}
$$

# 3. Decision variable constraints

The decision variable constraints of the UAV swarm mainly represent the binary decision matrix corresponding to each planned time $t$ under the actual time $q$ . 

$$
\mathbf {H} _ {q} (t) \in \{0, 1 \} ^ {n \times m}, \forall q \in [ 0, \tilde {t} _ {\text {e n d}} ], t \in \left[ 0, t _ {\text {e n d}} \right]. \tag {22}
$$

# 3.3. Solving algorithm

For SROM, a solution algorithm is proposed in this paper. It can be seen from the model that the core problem solved in this paper is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/0f902880a80652e85c103a5977efdb2c3f15516c423c49ca1d5b18cb75b30cdd.jpg)



(a) UAV 1 is attacked


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/dc0613128054bba9dc2bcae16d5378e78a040a0b19b94b49684d0d399321eeca.jpg)



(b) UAV 2 is attacked


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/44b2d7d8ede68048f3ee6539d7f45b1764ed391b44d6de5640b52019580b828b.jpg)



(c) UAV 3 is attacked


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/87eb72a5002ecab561d3fc8754b51998400bf04a9e0d2a27fc9e6a04d0dd034f.jpg)



(d) UAV 4 is attacked


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/a7f2e12d4d3be5857253385d0bea25453cebb24ab0f18af5f38341bba695c0c7.jpg)



(e) UAV 5 is attacked



Fig. 9. The effect of attack time sensitivity on the UAV swarm resilience.


to reasonably redistribute the remaining outstanding missions of the attacked UAVs to maximize the objective function, i.e., resilience. This is a combinatorial optimization problem, where different combinations of insertion missions will lead to changes in the overall performance of the UAV swarm. Therefore, the following algorithm is designed in this paper to find the optimal solution for the objective function. 

It can be seen from Fig. 4 that the input of the model mainly includes the information on the UAVs that have not been attacked in the UAV swarm and the information on the uncompleted missions of the attacked UAVs. The UAV information $RU = \langle Num, Pos, Spe, Cap \rangle$ that has not been attacked mainly includes the number, position, speed, and remaining mission capability of the UAV at $\tilde{i}_{attack}^p$ . The information $RM = \langle Num, Pos, Val, Exe \rangle$ of the uncompleted mission of the attacked UAV mainly includes the number, position, value, and execution time of the mission at $\tilde{i}_{attack}^p$ . After collecting and processing $RU$ and $RM$ , together with the mission list of the UAV swarm at $\tilde{i}_{attack}^p$ , they are used as the input of SROM. The output of this algorithm is a new mission list, as shown in Algorithm 1. 

# 4. Simulation analysis

Two experiments will be given in this section to verify the feasibility and superiority of the SROM proposed in this paper. The experimental environment used in this paper is a PC with Intel(R) Core(TM) i7-9750H processor and 32G RAM. In addition, the compilation platform we use is MATLAB R2021b, and all algorithms are compiled on this platform. 

Experiment 1: In this paper, we use the UAV and mission data of [45] and consider the experimental scenario of 5 UAVs to complete 20 missions. The specific parameters of the UAVs are shown in Table 1, and $\sigma = 1$ . 

The specific parameters of the mission are shown in Table 2. 

First, to verify the feasibility of the method proposed in this paper, the numbers of the UAVs are attacked are set as 2, 3, and 5, and the 


Table 1



Some parameters of UAV.


<table><tr><td>UAV</td><td>Initial position</td><td>Cost</td><td>Speed</td><td>Mission capability</td></tr><tr><td>1</td><td>(60, 70)</td><td>45</td><td>5</td><td>6</td></tr><tr><td>2</td><td>(41, 71)</td><td>45</td><td>5</td><td>6</td></tr><tr><td>3</td><td>(61, 32)</td><td>45</td><td>5</td><td>6</td></tr><tr><td>4</td><td>(43, 23)</td><td>45</td><td>5</td><td>6</td></tr><tr><td>5</td><td>(51, 40)</td><td>45</td><td>5</td><td>6</td></tr></table>


Table 2



Some parameters of mission.


<table><tr><td>Mission</td><td>Location</td><td>Value</td><td>Time spent</td><td>Mission</td><td>Location</td><td>Value</td><td>Time spent</td></tr><tr><td>1</td><td>(67, 23)</td><td>120</td><td>1</td><td>11</td><td>(80, 98)</td><td>150</td><td>1</td></tr><tr><td>2</td><td>(65, 70)</td><td>130</td><td>2</td><td>12</td><td>(94, 89)</td><td>150</td><td>2</td></tr><tr><td>3</td><td>(25, 55)</td><td>125</td><td>1</td><td>13</td><td>(32, 65)</td><td>140</td><td>1</td></tr><tr><td>4</td><td>(8, 32)</td><td>140</td><td>2</td><td>14</td><td>(85, 68)</td><td>130</td><td>2</td></tr><tr><td>5</td><td>(30, 26)</td><td>150</td><td>1</td><td>15</td><td>(70, 34)</td><td>123</td><td>1</td></tr><tr><td>6</td><td>(40, 44)</td><td>130</td><td>2</td><td>16</td><td>(43, 52)</td><td>145</td><td>2</td></tr><tr><td>7</td><td>(42, 90)</td><td>125</td><td>1</td><td>17</td><td>(25, 86)</td><td>120</td><td>1</td></tr><tr><td>8</td><td>(19, 40)</td><td>140</td><td>2</td><td>18</td><td>(78, 43)</td><td>130</td><td>2</td></tr><tr><td>9</td><td>(60, 34)</td><td>125</td><td>1</td><td>19</td><td>(36, 32)</td><td>140</td><td>1</td></tr><tr><td>10</td><td>(66, 55)</td><td>130</td><td>2</td><td>20</td><td>(95, 13)</td><td>150</td><td>2</td></tr></table>

attack times are 14.72, 23.25, and 32.37, respectively, according to the parameters of the UAVs and mission mentioned above. In addition, the computing time interval of the computing facility is $\Delta t = 1$ . 

Fig. 5 shows the cumulative gain of each of the five UAVs, where the horizontal coordinate represents the planned time $t$ and the vertical coordinate means the actual time $\tilde{t}$ . As $t$ increases, the cumulative gain increases gradually due to the UAVs' incremental gain after completing the mission according to the planned schedule. However, as $\tilde{t}$ increases, the planned cumulative gain changes, containing both rising and falling cumulative gains, as some of the UAVs in the UAV swarm are attacked or perform succession missions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/03f16093fe7a6c4f1544210f6c6237d486634138cbc69cb39552ebfb43007e3c.jpg)



(a) Attack in 7 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/8aa8e329ad9875b075e921b58ac2c64dae91132366abdd1c623b4104cecbd869.jpg)



(b) Attack in 10 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/1e8b9bac408062a19d245bf230d13f0375787f82f823fbb4dcc84d05bda95d5d.jpg)



(c) Attack in 13 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/1a261de4c06b56f6d5345798da5d913c7310793c8cd6075f93058bd0dcb34d90.jpg)



(d) Attack in 16 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/f14aa16b40bb64d2f8f861dd0abb43d3f63cfdf091dac31de5b88d5a00c883d1.jpg)



(e) Attack in 19 seconds



Fig. 10. The effect of different attack combinations on the UAV swarm resilience.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/5153d79223376e29fc5dc4c2e275470cdedf4fe1943c457666e5f4e73624ba12.jpg)



(a) Attack in 7 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/502e12d1c44571e5de60402b0e902a432480c8fa465a1b96d674ace5cfa59ed7.jpg)



(b) Attack in 10 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/30414388d3c950b3241483f62c31110119056b94d4b54ab52b02d351d67c4b34.jpg)



(c) Attack in 13 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/e468844b88d48dd3d8c15cd5399b34c5cd0d77eea2206a1e58a4bb6cfcf6c07a.jpg)



(d) Attack in 16 seconds


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/d8a6ed5c97a461cd622acf0ad10f134f1a9805aeb82dc20ff6c33c1d117dd229.jpg)



(e) Attack in 19 seconds



Fig. 11. Resilience of UAV swarm under different recovery strategies.


Since the UAVs numbered 2, 3, and 5 were attacked in this experimental setup, respectively, the cumulative gain of the UAVs decreases 

with increasing $\tilde{t}$ after the attack moment as seen in subfigures (b), (c), and (e) in Fig. 5. However, after the use of SROM, the UAVs 

Algorithm 1: Solving Algorithm of SROM  
Input: The input mainly includes the RU, RM, and mission list $\int_{t=0}^{t_{end}} \mathbf{H}_{\tilde{t}_{attack}}^p(t) dt$ of the UAV swarm at $\tilde{t}_{attack}^p$ Output: The output mainly includes a new mission list $\int_{t=0}^{t_{end}} \mathbf{H}_{\tilde{t}_{recover}}^p(t) dt$ of the UAV swarm at $\tilde{t}_{recover}^p$ 1: Calculate the estimated return time $\tilde{t}_{min}^p \gets \tilde{t}_{attack}^p + \Delta t$ of the mission list optimization result.  
2: Calculate the numbered set $Q$ of undamaged UAVs in the UAV swarm at time $\tilde{t}_{attack}^p$ .  
3: Extracting the UAVs with the remaining capacity space constitutes the set $Q_c \in Q$ .  
4: Construct the remaining mission set $\{T_r^{remain}|r \in U \backslash Q\}_p$ of the attacked UAV, where $\mu!$ is the full number of permutations of elements in $\{T_r^{remain}|r \in U \backslash Q\}_p$ .  
5: Construct the results of all permutations into a matrix $\Phi$ , where the rows of $\Phi$ are the number of total permutations, and the columns of $\Phi$ are the number of elements in the set.  
6: count $\gets 0$ 7: while count < $\mu!$ do  
8: count $\gets$ count + 1  
9: for $g \gets 1$ to $g \leqslant \left|\{T_r^{remain}|r \in U \backslash Q\}_p\right|$ by $g++ do$ 10: for $h \gets 1$ to $h \leqslant \left|\{T_l^{remain}|l \in Q_c\}\right|$ by $h++ do$ 11: According to Eq. (8), calculate the income $B$ of $\Phi(count, g)$ and the remaining missions of the UAV is unattacked.  
12: Calculate the return $\bar{B}$ for the original permutation according to Eq. (9).  
13: Calculate the incremental return $\phi_k, k = 1, 2, \dots, \sum_{l \in Q_c} \left( \left| \{T_l^{remain}\} \right| + 1 \right)!$ for all rearranged combinations.  
14: Get the maximum value $\max_k \phi_k$ of the income increment.  
15: Refresh the UAV swarm mission list.  
16: end for  
17: end for  
18: Record the maximum income increment $\gamma_u, u = 1, 2, \dots, count$ of all rearrangement combinations under each count order.  
19: end while  
20: Calculate the maximum revenue increment $\max_k \gamma_u$ , and record the update mission list $\int_{t=0}^{t_{end}} \mathbf{H}_{\tilde{t}_{recover}}^p(t) dt$ of the UAV swarm at $\tilde{t}_{recover}^p$ . 

numbered 1 and 4 take over part of the mission, changing the initial mission schedule, and their cumulative gains increase with $\tilde{t}$ , as shown in subfigures (a) and (d) in Fig. 5. 

The overall cumulative gain of the UAV swarm is shown in Fig. 6 (a). In addition, the normalized overall gain of the UAVs in the UAV swarm is shown in Fig. 6 (b). 

From Fig. 6, it can be seen that the cumulative gain of the UAV swarm is divided into three phases as $\tilde{t}$ increases. In the initial phase, the UAV swarm is not under any attack, and its cumulative gain value is the highest, but after $14.72\mathrm{s}$ , the UAV numbered 2 is attacked. The cumulative gain of the UAV swarm suddenly drops, and the SROM is activated. The UAVs numbered 1 and 3 take over some of the missions and update their own original scheduled mission schedule. The mission handover point in subfigure (b) of Fig. 6 illustrates this process. The exact process occurs at 23.25 and $32.37\mathrm{s}$ , where the UAVs are attacked numbered 3 and 5 and have part of their missions finally taken over by UAV numbered 4. 

The performance of the UAV swarm can be calculated according to Eq. (10), as shown in Fig. 7, where its comparison curve is given, i.e., the change in performance of the UAV swarm without the SROM. For the sake of observation, the curves are smoothed in Fig. 7 using Gaussian smoothing, where the data window is 10. 

Two curves are shown in Fig. 7, which are the UAV swarm's performance variation curves with SROM; its opposite is the performance variation curve without SROM. From the figure, it is clear that the performance of the UAV swarm is greatly improved after using SROM 

compared to that without SROM. The performance difference between the two is shown in the built-in plot in Fig. 7, and the disparity continues to rise as $\tilde{t}$ increases. 

To more visually show the changes in the UAV swarm mission plan, the mission progress graph of the UAV swarm is given in Fig. 8. 

The horizontal axis is Fig. 8 represents the planned time $t$ , the vertical axis represents the five UAVs, and the entire subfigure represents the planned mission progress of the UAVs at the actual time $\tilde{t}$ . The start time of the mission and the execution time of the mission are marked below each mission, respectively. Sufigures (a)-(c) show the recovery process of the UAV swarm at the first attack at $14.72 \, \text{s}$ . The initially planned mission of the UAV swarm is shown in subfigure (a). At $14.72 \, \text{s}$ , UAV 2 is attacked, and its subsequent missions, 3 and 17, will not be able to continue, as shown in figure (b). The information about the hit is transmitted to the control base station through the communication link. The planned mission progress of the UAV swarm is recalculated within the control base station through the SROM. The new planned mission progress to the UAV swarm through the communication link after $1 \, \text{s}$ , shown in figure (c). It can be seen that UAV 1 and UAV 3 received mission 3 and mission 17, respectively, and updated the planned mission list. Subfigures (d)-(i) show the resilience process of the 2nd and 3rd attacks. More intuitively, Fig. 8 clearly shows the changes in the mission planning diagram of the UAV swarm before and after the attack and recovery. 

With Eq. (14), the resilience value of the UAV swarm can be calculated, and after calculation, the resilience value of the UAV swarm 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/a0dd5213fa79973928d8988e972e04142568fa2b8c818951b2ed05ee69cb11a9.jpg)



(a) The performance variation of the resilience process


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/ae9d7e83a52b28627d245d7470ffe2e3d27193328eab48692b70bb6b0c642884.jpg)



(b) The resilience value


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/d500efee0267350a936d303d5370a48813702f1ba603aec2c86a1558d6916a9f.jpg)



(c) The confidence interval


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/452d0bf0ca8dac4c4ef393203b04d1a77711f04f3d53782a28c68a5bdf9708e2.jpg)



(d) The mean curve



Fig. 12. 1000 Monte Carlo simulation results..


using SROM in this experiment is 0.8736. The resilience value of the UAV swarm without SROM is 0.6991. From the results, it is clear that SROM can significantly improve the performance of the struck UAV swarm and make it more resilient. 

To explore the effect of attack time sensitivity on the UAV swarm resilience more deeply, Fig. 9 shows the change in the resilience of the UAV swarm for five scenarios, which correspond to five UAVs being attacked individually. For example, subfigure (a) indicates that UAV 1 is attacked, and the other UAVs usually operate. The horizontal coordinate of each subfigure represents the number of strike simulations performed with $1\mathrm{s}$ as the time interval between the start of the first mission of the UAV and the end of the last mission. The vertical coordinate represents the resilience value of the UAV swarm. More intuitively, Fig. 9 shows the variation in the resilience of a single UAV in a UAV swarm when attacked at different times. 

Three conclusions can be drawn from Fig. 9. Firstly, as the strike time is shifted back, the number of missions that the UAV swarm cannot complete gradually decreases, and the resilience of the UAV swarm becomes higher. Secondly, the backward shift of the strike time causes the resilience values derived using SROM and not using SROM to be close to each other, which is because the number of missions that the UAV swarm cannot complete is reduced, and the performance space that needs to be recovered is compressed; in other words, the 

more missions remaining in the struck UAV, the more pronounced the SROM effect is, all other things being equal. Finally, the UAV swarm resilience values obtained using SROM are consistently higher than those obtained without SROM, which fully demonstrates the feasibility of the SROM. 

From another perspective, we fixed the attack time and deeply explored the effect of different attack combinations on the UAV swarm resilience, as shown in Fig. 10. Since, in this case, the five UAVs work together from 7 to $19\mathrm{~s}$ , Fig. 10 investigates the change of UAV swarm resilience with 3-second intervals and fixed strike moments of 7, 10, 13, 16, and $19\mathrm{~s}$ , respectively. The horizontal coordinate of each subfigure represents the number of simulations of different strike combinations, and the total number of simulations is $C_5^1 + C_5^2 + C_5^3 + C_5^4 = 30$ . The vertical coordinate represents the resilience value of the UAV swarm. More intuitively, Fig. 10 shows the variation in the resilience of a UAV swarm changes when exposed to different combinations of attacks. 

Three conclusions can also be drawn from Fig. 10. Firstly, with the increase in the number of UAVs attacked in the UAV swarm under the fixed strike time, the number of UAVs that can take over the mission becomes less, so the overall resilience shows a downward trend. Secondly, the increase in the number of UAVs attacked in the swarm also causes the resilience values obtained with and without SROM to be close to each other. Finally, the resilience value of the UAV swarm 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/03813ae84a1f7462549a7ee54cdd994ef6158dce8cd1cd77e41a89325324c1a1.jpg)



(a) Strengths of $20\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/98721edc319fccecced62956d2282e06a00d03f08b3c829848e0af20a6617093.jpg)



(b) Strengths of $40\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/175ab4a968132afb42fb924e1131799f1a4332b45af31df92c5184d146611c1f.jpg)



(c) Strengths of $60\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/159dbb20c085416a33008025bb5e80d4255daf64f41dad771e56433e3c020dab.jpg)



(d) Strengths of $80\%$



Fig. 13. The variation of resilience value of UAV swarm under four groups of different attack intensity..


obtained with SROM is consistently higher than that without SROM, similar to the conclusion in Fig. 9. 

Based on not using SROM, this experiment also compares two other methods; one is the random resource allocation model (RRAM), and the other is the benefit minimization resource allocation model (BMRAM), as shown in Fig. 11. Among them, the RRAM randomly selects an allocation scheme in the process of choosing allocation schemes and does not pursue the maximization of income. The BMRAM sets the minor benefit allocation scheme. The main reason for comparing this scheme is to prove that the soft resource allocation scheme is not randomly allocating missions. Improper soft resource allocation can result in resilience much lower than those without SROM. 

It can be seen from Fig. 11 that the UAV swarm using SROM has the highest resilience value and is stable so that the UAV swarm can guarantee the mission revenue; At the same time, the benefit minimization resource allocation model will lead to the lowest resilience value of the UAV swarm, and the random resource allocation model will lead to a significant and unstable change in resilience value. This indicates that the SROM model is the optimal choice when a UAV swarm is attacked. 

Experiment 2: To explore the UAV swarm's generalized resilience value, the Monte Carlo simulation method is adopted to estimate the confidence interval by Eq. (23) of the unknown population means 

through 1000 random experiments. 

$$
\bar {x} _ {\mathrm {C V}} = \mu_ {S A} \pm t _ {\mathrm {C V}} * \frac {s}{\sqrt {n}}, \tag {23}
$$

where $\mu_{SA}$ , $t_{\mathrm{CV}}$ , $s$ , and $n$ represent the sample average, the $t$ critical value, the sample standard deviation, and the sample size, respectively. This paper selects the $95\%$ receptive field interval, $t_{\mathrm{CV}}$ is 2.262 by looking up the table. In addition, $\sigma = 1$ . 

Firstly, a simulation example is used to explain the method of estimating confidence intervals. This example assumes that a UAV swarm composed of 5 UAVs will perform 20 established missions, and the initial positions of the UAVs and missions in each random experiment are randomly given. The UAV has a constant speed of 5 units per second and can perform up to 5 missions. Each UAV costs 45. The value of the mission is 100, and the execution time of the mission is set to random values of 1 s and 2 s. Two UAVs were attacked randomly in each random simulation experiment, and the experimental results are shown in Fig. 12. 

Subfigure (a) in Fig. 12 shows the performance variation of the resilience process of the UAV swarm in 1000 simulation experiments, and subfigure (b) calculates the resilience value of each simulation experiment according to Eq. (14). Furthermore, we set the sample size of each group as 10. Then, according to Eq. (23), the confidence 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/60f3911f374ec90dbcf321cdd0174b59b93c24997bb7ce1c175812161276c0f5.jpg)



(a) The first group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/64a21c5bf495079b05a60a7d0495775dcf8a16447615342641413e829c94798a.jpg)



(b) The second group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/0ec8900b62dcc0eeac4fcbdb5dd7833a6b8616b18cfd676723e28575da89f71e.jpg)



(c) The third group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/f798b139d139ab11f71651b55af84d2595db39477b8eb6f2cb2f87a72dd7d00b.jpg)



(d) The fourth group


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/6beeaf4e09da2b500a198bfaa937853ce8a5262d199e1e5314f210de1e49b5bd.jpg)



(e) The fifth group



Fig. 14. The influence of different strike intensities on UAV swarm resilience under a fixed scale.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/66f045f710db39dd22a0660e4cf97fab72f2a84431208ffdf76b773fa05c6aa5.jpg)



Fig. 15. The impact of the number of missions on UAV swarm resilience.


interval of the population mean of 100 groups of independently sampled samples at $95\%$ confidence level can be calculated, as shown in subfigures (c) and (d). The dashed line value in subfigure (d) is 0.664, which covers most of the confidence intervals obtained by 100 independent sampling groups and can be used as the reference value for the overall mean resilience value of the UAV swarm composed of 5 UAVs executing 20 established missions and 2 UAVs being attacked. 

Furthermore, we set up four groups of comparative experiments to verify the superiority of the SROM, as shown in Fig. 13. 

Fig. 13 shows the variation of resilience value of UAV swarm under four groups of different attack intensity. The abscissa represents The 

Times of $5^{*}100$ simulation groups, where 5 represents five groups of UAV swarms of different sizes and the number of missions executed, and 100 represents the results of 1000 simulation experiments divided into independent sampling samples with sample size n of 10. The ordinate represents the resilience value of the UAV swarm. The five groups of UAV swarms of different sizes and the number of missions performed in the four sub-figures are shown in Table 3. In addition, the four subgraphs have attack intensities of $20\%$ , $40\%$ , $60\%$ , and $80\%$ , respectively. It is worth mentioning that the attack intensity refers to the random attack on a certain number of UAVs in the UAV swarm. For example, $20\%$ attack intensity on a UAV swarm consisting of 10 UAVs means that two UAVs will stop working. 

The following conclusions can be drawn from Fig. 13. Firstly, with fixed attack intensity, its resilience gradually increases with the increase of UAV swarm size and mission number. This is because more UAVs and missions mean that the optimization space of SROM increases; that is, it can better compensate for the strike's impact. Secondly, the resilience with SROM is always higher than without SROM, which reflects the superiority of the proposed model. Finally, with the increase of UAV swarm size and the number of missions, 100 groups of independent sampling samples under the $95\%$ confidence level of the confidence interval of the population mean is stable, indicating that the UAV swarm scale and missions, the greater the number of the alternative scheme, the performance of UAV swarm, the higher the possibility of recovery, so the resilience of the estimated to be affected will be smaller. 

From another perspective, we also set up five groups of comparative experiments to verify the superiority of SROM, as shown in Fig. 14. 

Different from Fig. 13, Fig. 14 shows the influence of different strike intensities on UAV swarm resilience under a fixed scale. The abscissa represents the simulation times of $4^{*}100$ groups, where 4 represents the four groups of experiments with the attack intensity of $20\%$ , $40\%$ , $60\%$ , and $80\%$ , respectively. The remaining parameters are similar to 


Table 3 Some parameters of UAV swarm and missions.


<table><tr><td></td><td>The first group</td><td>The second group</td><td>The third group</td><td>The fourth group</td><td>The fifth group</td></tr><tr><td>Scale of UAV swarm</td><td>5</td><td>10</td><td>15</td><td>20</td><td>25</td></tr><tr><td>Number of missions</td><td>20</td><td>40</td><td>60</td><td>80</td><td>100</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/afd2ef034c307247942fa16c49887935af3616803c64daee213009be7ef7f86b.jpg)



(a) The mission value is 60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/85d2e8a1914a50038a63bfca07b09bd9fbcbcf2abb93b8006776959bd4c9d188.jpg)



(b) The mission value is 80


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/75d9c30b4e7d3a2989ee904807c3eee89e56d52bdcebf146da22afd5179b3863.jpg)



(c) The mission value is 100



Fig. 16. The impact of changes in mission value on UAV swarm resilience..


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/51c84be531f6f8978d1a2b19214c095d10b4e8711bada60467356ffeb8d7ecaf.jpg)



(a) The cost of the UAV is 60


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/ea4b3202922c4753a4db6cf44edd09cad94eabe1475f392fd9997346ebc8a1ea.jpg)



(b) The cost of the UAV is 80


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/35ae3a22-b22a-4a6c-980f-3c8429261c86/3ea411307899866a4cfb6862cdb57a726c8701afed0809f27f32978e8b2623d1.jpg)



(c) The cost of the UAV is 100



Fig. 17. The impact of changes in UAV cost on UAV swarm resilience.


Fig. 13. The following conclusions can be drawn from Fig. 14. Firstly, under a fixed scale, the resilience of the UAV swarm decreases rapidly with the increase in strike intensity. This is because the number of UAVs increases, the remaining uncompleted missions also increase, and the number of UAVs that can take over the missions reaches saturation, so the overall resilience of the UAV swarm decreases. Secondly, the resilience with SROM is always higher than without SROM, which also proves the superiority of the proposed model. 

The above experiments all adopt the assumption that the UAV swarm size and the number of missions grow proportionally at the same time. To explore the situation where the number of missions increases but the scale of the UAV swarm remains the same, we assume that the number of UAVs in the UAV swarm is 5, the mission execution capability is still 5, and other conditions remain the same. It is easy to know that the number of missions in the UAV swarm can vary between [5,24]. This ensures that each UAV can be assigned to at least one mission, and the redundancy value is left to ensure that the SROM can be used. The simulation results are shown in Fig. 15. 

In Fig. 15, the abscissa is the number of $19^{*}100$ simulation groups, 19 represents the number of 19 different missions, and 100 represents the results of 1000 simulation experiments divided into independent sampling samples with sample size n equal to 10. Fig. 15 is described as a scatter plot. The scatter is fitted by quadratic Polynomial polynomials using the cftool toolbox; the R-Square curve is 0.9831 for the data fitted with SROM and 0.9894 for the data fitted without SROM. This indicates that the fit is relatively good in explaining the variation of the data. 

Two conclusions can be drawn from Fig. 15. First, two data fitting curves downward trend after rising first; this is because, in the very beginning, mission quantity is less, the UAV is the original plan mission, in fact, the highest yield, but due to the attack, another mission of UAV to succeed may lead to cost increase, and cannot compensate for the loss in income, so the resilience is very low. And as the number of missions increases, the cost of taking over will decrease. However, when approaching the limit of UAV swarm capability, the solution space of SROM is compressed so that the resilience value will show a downward trend. Secondly, it can be found that the scatter and fitting curves using SROM are higher than those without SROM, which reflects the superiority of the method proposed in this paper. 

Finally, we thoroughly explore the impact of changes in UAV cost and mission value on UAV swarm resilience, as shown in Fig. 16 and Fig. 17. 

Fig. 16 mainly explores the impact of increasing UAV cost on UAV swarm resilience under the condition of fixed mission value. The abscissa is the number of $5^{*}100$ groups of simulations, where 5 represents five different UAV costs, which are 20, 40, 60, 80, and 100, respectively. Similarly, Fig. 17 mainly explores the influence of increasing mission value on UAV swarm resilience under the condition of fixed UAV cost. The abscissa is the number of $3^{*}100$ simulation groups, where 3 represents three different mission values, which are 60, 80, and 100, respectively. This is because the mission value is too low and the distance wear is too high, which leads to negative revenue. 

The following conclusions can be drawn from Fig. 16. First, when the mission value is fixed, the higher the cost of the UAV, the lower 

the resilience of the UAV swarm. This is because when other conditions are unchanged, the higher the cost of UAV, the greater the loss of the attack, so the revenue will be reduced, and the resilience will also be reduced. But if the UAV cost is fixed and the mission value is higher, the conclusion is reversed, as shown in Fig. 17. Secondly, Fig. 16 and Fig. 17 show that the scatter and fitting curves with SROM are higher than those without SROM, which is similar to Fig. 15, reflecting the superiority of the proposed method. 

# 5. Conclusions

The resilience improvement of UAV swarm is significant work. Structurally improving UAV swarm resilience is a fast recovery method, but resource constraints accompany it. When a UAV swarm is attacked, it is always a difficult mission to replenish or deploy new UAVs or change communication links. The SROM proposed in this paper solves this physical resource limitation and focuses on the mission benefits of the UAV swarm instead of simply making up for the defects in the UAV swarm structure. In addition, the UAVs have obtained the new mission plan through the algorithm proposed in this paper. Compared with other algorithms, the resilience value received by the algorithm proposed in this paper is always the highest. The simulation experiment verifies the feasibility and superiority of the proposed model. In future work, we will further discuss the soft resource optimization model of heterogeneous UAV swarms and explore the soft resource optimization model of UAV swarms under the distributed command and control structure. 

# CRediT authorship contribution statement

Hongxu Li: Writing - review & editing, Writing - original draft, Visualization, Validation, Methodology, Investigation, Conceptualization. Qin Sun: Writing - review & editing, Supervision, Methodology. Yuanfu Zhong: Writing - review & editing, Visualization, Validation, Supervision. Zhiwen Huang: Writing - review & editing, Supervision. Yingchao Zhang: Writing - review & editing, Supervision, Project administration, Funding acquisition. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Data availability

No data was used for the research described in the article. 

# Acknowledgments

This research was supported by the National Key Laboratory (No. XM2020XT1009, No. XM2021XT1025, XM2021XT1026, HT-WB-2021-0159), the Science and Technology on Information System Engineering Laboratory (No. pu52201059). 

# References



[1] Mason F, Capuzzo M, Magrin D, Chiariotti F, Zanella A, Zorzi M. Remote tracking of UAV swarms via 3D mobility models and LoRaWAN communications. IEEE Trans Wireless Commun 2022;21(5):2953-68. 





[2] Liu ZH, Wang XK, Shen LC, Zhao SL, Cong YR, Li J, et al. Mission-oriented miniature fixed-wing UAV swarms: a multilayered and distributed architecture. IEEE Trans Syst Man Cybern 2022;52(3):1588-602. 





[3] Zhou X, Wen XY, Wang ZP, Gao YM, Li HJ, Wang QH, et al. Swarm of microflying robots in the wild. Science Robotics 2022;7(66):eabm5954. 





[4] Soria E. Swarms of flying robots in unknown environments. Science Robotics 2022;7(66):eabq2215. 





[5] Jiang YY, Gao Y, Song WQ, Li Y, Quan Q. Bibliometric analysis of UAV swarms. J Syst Eng Electron 2022;33(2):406-25. 





[6] Mou ZY, Gao FF, Liu J, Wu QH. Resilient UAV swarm communications with graph convolutional neural network. IEEE J Sel Areas Commun 2022;40(1):393-411. 





[7] Lim GJ, Kim S, Cho J, Gong YB, Khodaei A. Multi-UAV pre-positioning and routing for power network damage assessment. IEEE Trans Smart Grid 2018;9(4):3643-51. 





[8] Ma MN, Tao W, Zhang X, Xu ZY, Li HM, Wang QJ. Electromagnetic interference analysis of permanent magnet linear synchronous launchers. IEEE Trans Plasma Sci 2020;48(5):1309-15. 





[9] Zhang PT, Wu T, Cao RH, Li Z, Xu JW. UAV swarm resilience assessment considering load balancing. Front Phys 2022;10:821321. 





[10] Pocock MJO, Evans DM, Memmott J. The robustness and restoration of a network of ecological networks. Science 2012;335(6071):973-7. 





[11] Cai Q, Alam S, Pratama M, Liu JM. Robustness evaluation of multipartite complex networks based on percolation theory. IEEE Trans Syst Man Cybern 2021;51(10):6244-57. 





[12] Wang S, Liu J, Jin YC. A computationally efficient evolutionary algorithm for multiobjective network robustness optimization. IEEE Trans Evol Comput 2021;25(3):419-32. 





[13] Dui HY, Zhang C, Bai GH, Chen LW. Mission reliability modeling of UAV swarm and its structure optimization based on importance measure. Reliab Eng Syst Saf 2021;215:107879. 





[14] Xu B, Liu T, Bai GH, Tao JY, Zhang YA, Fang YN. A multistate network approach for reliability evaluation of unmanned swarms by considering information exchange capacity. Reliab Eng Syst Saf 2022;219:108221. 





[15] Feng Q, Liu M, Dui HY, Ren Y, Sun B, Yang DZ, et al. Importance measure-based phased mission reliability and UAV number optimization for swarm. Reliab Eng Syst Saf 2022;223:108478. 





[16] Levitin G, Xing LD, Dai YS. Mission aborting and system rescue for multi-state systems with arbitrary structure. Reliab Eng Syst Saf 2022;219:108225. 





[17] Wen T, Deng Y. The vulnerability of communities in complex networks: an entropy approach. Reliab Eng Syst Saf 2020;196:106782. 





[18] Choeum D, Choi D. Vulnerability assessment of conservation voltage reduction to load redistribution attack in unbalanced active distribution networks. IEEE Trans Ind Inf 2021;17(1):473-83. 





[19] Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Syst 1973;4(1):1-23. 





[20] Ungar M, Theron L. Resilience and mental health: how multisystemic processes contribute to positive outcomes. Lancet Psychiatry 2020;7(5):441-8. 





[21] Ungar M, Ghazinour M, Richter J. Annual research review: what is resilience within the social ecology of human development? J Child Psychol Psychiatry 2013;54(4):348-66. 





[22] Liu R, Lei S, Peng C, Sun W, Hou Y. Data-based resilience enhancement strategies for electric-gas systems against sequential extreme weather events. IEEE Trans Smart Grid 2020;11(6):5383-95. 





[23] Dui HY, Zheng XQ, Wu SM. Resilience analysis of maritime transportation systems based on importance measures. Reliab Eng Syst Saf 2021;209:107461. 





[24] Wu YY, Chen SR. Resilience modeling and pre-hazard mitigation planning of transportation network to support post-earthquake emergency medical response. Reliab Eng Syst Saf 2023;230:108918. 





[25] Watson BC, Morris ZB, Weissburg M, Bras B. System of system design-for-resilience heuristics derived from forestry case study variants. Reliab Eng Syst Saf 2023;229:108807. 





[26] Xu S, Tu HC, Xia YX. Resilience enhancement of renewable cyber-physical power system against malware attacks. Reliab Eng Syst Saf 2023;229:108830. 





[27] Zhou ZS, Matsubara Y, Takada H. Resilience analysis and design for mobility-as-a-service based on enterprise architecture modeling. Reliab Eng Syst Saf 2023;229:108812. 





[28] Ialokhoin O, Pant R, Hall JW. A model and methodology for resilience assessment of interdependent rail networks - Case study of Great Britain's rail network. Reliab Eng Syst Saf 2023;229:108895. 





[29] Fan DM, Sun B, Dui HY, Zhong JL, Wang ZY, Ren Y, et al. A modified connectivity link addition strategy to improve the resilience of multiplex networks against attacks. Reliab Eng Syst Saf 2022;221:108294. 





[30] Sun Q, Li HX, Wang YZ, Zhang YC. Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems. Reliab Eng Syst Saf 2022;222:108426. 





[31] Liu T, Bai GH, Tao JY, Zhang YA, Fang YN, Xu B. Modeling and evaluation method for resilience analysis of multi-state networks. Reliab Eng Syst Saf 2022;226:108663. 





[32] Ma LJ, Zhang X, Li JQ, Lin QZ, Gong MG, Coello CAC, et al. Enhancing robustness and resilience of multiplex networks against node-community cascading failures. IEEE Trans Syst Man Cybern 2022;52(6):3808-21. 





[33] Yang BF, Zhang L, Zhang B, Xiang Y, An L, Wang WF. Complex equipment system resilience: composition, measurement and element analysis. Reliab Eng Syst Saf 2022;228:108783. 





[34] Cheng CC, Bai GH, Zhang YA, Tao JY. Resilience evaluation for UAV swarm performing joint reconnaissance mission. Chaos 2019;29(5):053132. 





[35] Bai G, Li Y, Fang Y, Zhang Y, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020;193:106602. 





[36] Sun Q, Li HX, Zhang YC, Xie YX, Liu CY. A baseline assessment method of UAV swarm resilience based on complex networks. In: 2021 IEEE 19th world symposium on applied machine intelligence and informatics. IEEE; 2021, p. 83-6. 





[37] Li HX, Sun Q, Wang MH, Liu CY, Xie YX, Zhang YC. A baseline-resilience assessment method for UAV swarms under heterogeneous communication networks. IEEE Syst J 2022;1-12. http://dx.doi.org/10.1109/JSYST.2022.3197324. 





[38] Saulnier K, Saldana D, Prorok A, Pappas GJ, Kumar V. Resilient flocking for mobile robot teams. IEEE Robot Autom Lett 2017;2(2):1039-46. 





[39] Ramachandran RK, Preiss JA, Sukhatme GS. Resilience by reconfiguration: exploiting heterogeneity in robot teams. In: 2019 IEEE/RSJ international conference on intelligent robots and systems. 2019, p. 6518-25. 





[40] Ramachandran RK, Pierpaoli P, Egerstedt M, SSukhatme GS. Resilient monitoring in heterogeneous multi-robot systems through network reconfiguration. IEEE Trans Robot 2022;38(1):126-38. 





[41] Sun Q, Li HX, Wang YZ, Zhou LP, Zhang YC. Resilient UAV swarm modeling and solving based on multi-domain collaborative method. Acta Aeronaut Astronaut Sinica 2022;43(5):325340 [in Chinese]. 





[42] Liang XL, Zhang JQ, Lv N. UAV swarms. Northwestern Polytechnical University Press; 2018, 





[43] Wang XH, Zhang Y, Wang LZ, Lu DW, Zeng GQ. Robustness evaluation method for unmanned aerial vehicle swarms based on complex network theory. Chin J Aeronaut 2020;33(1):352-64. 





[44] Wang LZ, Zhao XJ, Zhang Y, Wang XH, Ma TL, Gao X. Unmanned aerial vehicle swarm mission reliability modeling and evaluation method oriented to systematic and networked mission. Chin J Aeronaut 2021;34(2):466-78. 





[45] Zhang RP, Feng YX, Yang YK. Hybrid particle swarm algorithm for multi-UAV cooperative task allocation. Acta Aeronaut Astronaut Sinica 2021. http://dx.doi.org/10.7527/S1000-6893.2021.26011 [in Chinese]. 

