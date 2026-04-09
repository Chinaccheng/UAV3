# Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/e43755d3a822107ab6382c5b870dcea0c98478e6f2e097a1ea52b395030ff155.jpg)


Qin Sun, Hongxu Li, Yuzhi Wang, Yingchao Zhang* 

School of Systems Science and Engineering, Sun Yat-sen University, Guangzhou 510006, PR China 

# ARTICLE INFO

Keywords: 

Resilience enhancement 

Unmanned weapon system-of-systems 

Cooperative reconfiguration 

Heterogeneous network 

Multi-swarm 

# ABSTRACT

Unmanned weapon system-of-systems (UWSoS) is a large-scale system composed of many types of unmanned weapon systems. With the soaring number of interconnected systems in UWSoS, UWSoS's complexity and interference uncertainty increase dramatically, resulting in preventive and protective strategies that are not all-inclusive. It is essential to research resilient UWSoS, which can recover the performance through the reconfiguration technique in the post-disruptive. We studied the reconfiguration model for UWSoS from the perspective of resilience enhancement. A multi-swarm-based cooperative reconfiguration model was proposed to maximize the resilience of UWSoS. First, an extended mission-oriented resilience metric is presented to effectively describe the resilience of the UWSoS, considering the variable mission baseline and restoration time. Subsequently, a cooperative factor-based resilience optimization model is established using the available existing entities in one swarm to replace the disrupted entities in another swarm. Finally, the feasibility, effectiveness, and superiority of the proposed model are illustrated through extensive experiments. This work could provide valuable insights for operational guidance and decision support for the design of resilient UWSoSs. 

# 1. Introduction

Unmanned weapon system-of-systems (UWSoS) is a new type of weapon system-of-systems [1-3] developed on unmanned intelligent technology and the concept of unmanned confrontation [4,5]. UwSoS is mainly composed of various functional unmanned weapon systems to achieve a high level of operational effectiveness through system cooperation, such as forming a series of synergy kill chains [6]. Unmanned weapon systems refer to typical intelligent unmanned platforms, such as unmanned aerial vehicles, unmanned ground vehicles, and unmanned surface vehicles, which have the characteristics of low cost, single function, and agile deployment. However, UWSoS operates in an adversarial environment, which is susceptible to interference [7], including being attacked, losing communication within the members, or malfunctioning owing to harsh situations [8]. Thus, it is of significant military value to study the reliable operation of UWSoS in an interference environment. 

Setting up redundancy and protection plans is a conventional method of reliability design. Li et al. [9] investigated a mixed active and cold standby component redundancy strategy to improve system reliability. Levitin et al. [10] studied optimal preventive replacement scheduling to maximize mission success probability. Li et al. [11] proposed a capability-oriented weapon contribution analysis framework to 

analyze a vital entity that needs to be protected in attack scenarios. However, these traditional strategies face significant challenges. Because the causes of interference are gradually becoming unpredictable and inevitable in the UwSoS operation [12], it is strenuous to set accurate prevention and protection strategies before the disruption. Hence, research emphasis has shifted from prevention or protection to withstand disruptions and recover swiftly in recent years [13- 15]. Resilience provides a novel perspective for UwSoS operations, combined with resisting uncertain interference and bouncing back from disruptive events. 

Resilience describes the capability of a system or system-of-systems to withstand, adapt, and recover from disruption [16,17]. In 1973, Holling proposed the definition of resilience in research on ecosystems [18]. Subsequently, studies on resilience metrics and resilience enhancement are underway in many domains, such as sociology [19, 20], infrastructure engineering [21,22], and military systems [12,23], and have become research hotspots in the past few years. 

The resilience metric is the cornerstone for resilience enhancement, which influences the choice of enhancement strategies [24-26]. According to the time correlation, resilience metrics can be divided into quotient and integral resilience models [27]. The quotient resilience model depicts the ratio of recovered performance to lost performance, 

and the integral resilience model describes the entire attack recovery process [28], such as the resilience triangle [29]. In the context of an unmanned weapon system-of-systems, Tran et al. [30] proposed an integral quantitative evaluation method based on the factors of system performance, recovery, absorption, volatility, and recovery time. Analyzing the role of mission in the confrontation, a modified resilience metric based on Tran's research was proposed by Bai [31], defaulting the final restored performance as the target mission. However, these methods do not consider explicit mission baselines. Liu et al. [32] defined a clear mission baseline for a mission-oriented system and proposed a resilience metric including time and performance resilience; however, they only considered the performance to reach the expected value. Therefore, the above methods cannot be directly applied to UwSoS because performances beyond or below the mission baseline have different implications for UwSoS and are important for resilience assessment. 

According to the results of the resilience metric, many researchers have developed various reconfiguration techniques for resilience enhancement [33-35]. Some available strategies are used for reconfiguration by utilizing the existing resources. Feng et al. [36] changed multiple unmanned aerial vehicle formations under random attacks to optimize system resilience. Tran et al. [37] enhanced the resilience of the command and control system-of-systems by randomly reconnecting the remaining nodes. However, the above methods, which have the characteristic of performing reconfiguration actions in the same network, always have a gap between the restored performance and the initial level [32,36]. Moreover, if a vital node is disrupted in the network, the effect of resilience enhancement by changing the formation or reconnecting links is insignificant for UwSoS. Conversely, some strategies are to reconfigure through cooperation with the outside. Pan et al. [28] and Zhang et al. [38] presented repair strategies for damaged systems based on resilience component importance analysis. Almoghathawi et al. [39] proposed a resilience-driven mixed-integer programming recovery model with limited maintenance resources. However, these methods are limited to scenarios in which the number of disrupted entities is small, and the entity can be repaired. Conversely, during UwSoS operation, the number of disrupted nodes is uncertain, and there is little time to repair the disrupted nodes. Sun et al. [40] proposed a synergy strategy based on the nodes of the maximum-minimum degree to overcome irreparability. However, the solution of this method is not globally optimal, and the application is limited to a homogeneous communication network because the collaboration target and synergy rules differ from UwSoS. Hence, it is necessary to establish a suitable reconfiguration model for UwSoS to enhance resilience. 

Because of these matters, we study the resilience enhancement problem for the UwSoS, focusing on establishing a cooperative reconfiguration model to increase recovery capability. In this study, an extended mission-oriented resilience metric is first presented, and then a multi-swarm-based cooperative reconfiguration model to maximize the resilience of UwSoS is proposed. The main contributions of this study are summarized as follows. 

(i) A mission-oriented UwSoS resilience metric is proposed to comprehensively consider the performance above and below the mission baseline, the changeable mission baseline, and the restoration time. This resilience metric can effectively describe the resilience of the UwSoS and provide resilience optimization targets for the reconfiguration model. 

(ii) A multi-swarm-based cooperative reconfiguration model was established to enhance the resilience of UwSoS. The model cannot only overcome the irreparability of entities during UwSoS operation but also recover the performance and narrow the gap to the desired level. Thus, it is more suitable for heterogeneous UwSoSs. 

(iii) The proposed method can assist decision-makers to evaluate the resilience of UwSoS and determine how much improvement can be achieved under various attack modes and attack intensities, thereby facilitating the reliable operation of the UwSoS. 

The remainder of this paper is organized as follows. In Section 2, brief definitions, network models, performance measurements, and resilience of UwSoS are introduced. The proposed mission-oriented resilience metric and multi-swarm-based cooperative reconfiguration model are presented in Section 3. Illustrative experiments were conducted to verify the proposed model in Section 4. Finally, concluding remarks and future work are presented in Section 5. 

# 2. Background

In this section, we review the background required to establish the multi-swarm cooperative reconfiguration model. Specifically, relevant definitions are briefly introduced. 

# 2.1. Heterogeneous network model of UWSoS

Definition 2.1 (Heterogeneous Network[41,42]). Given a directed graph $\mathcal{G} = (V,E,\varphi ,\psi)$ , which consists of a set of nodes $V$ and a set of edges $E$ . The graph has a node type mapping function $\varphi :V\to \mathcal{A}$ , in which each node $v\in V$ belongs to a particular node type $\varphi (v)\in \mathcal{A}$ and a link type mapping function $\psi :E\rightarrow \mathcal{R}$ , where each link $e\in E$ belongs to a particular relation $\psi (e)\in \mathcal{R}$ . If the graph has node-type $|\mathcal{A}| > 1$ or edge-type $|\mathcal{R}| > 1$ , the network is considered a heterogeneous network. 

Definition 2.2 (Meta-path[42,43]). A meta-path $\mathcal{P}$ is a path based on the network schema $\mathcal{T} = (\mathcal{A},\mathcal{R})$ , which represents a series of links between type $A_{1}$ and $A_{l + 1}$ : $A_{1}\xrightarrow{R_{1}}\ldots\xrightarrow{R_{l}}A_{l + 1}$ , where node types $A_{1},A_{2},\ldots,A_{l + 1}\in\mathcal{A}$ , and link types $R_{1},R_{2},\ldots,R_{l}\in\mathcal{R}$ . A path $p=\left(a_{1}a_{2}\ldots a_{l + 1}\right)$ follows the meta-path $\mathcal{P}$ , if each node $a_{i}$ has $\varphi(a_{i})=A_{i}$ and each link $e_{i}=\left\langle a_{i}a_{i+1}\right\rangle$ has $\psi(e_{i})=R_{i}$ in $\mathcal{P}$ , and $i=1,2,\ldots,l$ , called path instance of $\mathcal{P}$ , $p\in\mathcal{P}$ . 

The UWSoS is a combination of unmanned weapon systems with various capabilities, such as intelligence, command, control, and firing capacity. Referring to Cares' information-age combat model (IACM) [44] and Tan's operation loop [45], the entities of UWSoS are divided into four categories. 

- Sensor entities $(S)$ : entities that perform functions of early intelligence, reconnaissance, and surveillance. 

- Decider entities $(D)$ : entities that perform command and control functions. 

- Influencer entities $(I)$ : entities that perform striking and electromagnetic interference functions. 

- Target entities $(T)$ : entities of enemy sensors, deciders, and influencers on the battlefield. 

According to modern combat cycle theory, combat operation is a cyclic process that includes observation, orientation, decision-making, and action [11]. The enemy can be detected by the sensor entities $(T \to S)$ . Thus, information from the sensor entities is transmitted to the decider entities $(S \to D)$ for data fusion and analysis. Decider entities make operational decisions for influencer entities $(D \to I)$ . Correspondingly, the influencer entities obey the orders of the decider entities and execute strikes on the target entity $(I \to T)$ . Thus, a basic meta-operation loop is formed as $T \to S \to D \to I \to T$ , representing a meta-path of the observation, orientation, decision-making, and action processes. In addition, there are three other types of edges, $S \to S$ , $D \to S$ , and $D \to D$ , which can be added to the basic meta-operation loop for expansion, and their semantic information is elaborated in Ref. [46]. Fig. 1 shows four types of meta-operation loops. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/de02d03ac3a16ca7cf84489018005d51329b77961f437c1c48e5cf6e40c6e9e7.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/714da855f5446c1c490fcbda2ffb1fad15d52ccc80f09f54a14194fae6a4bbf8.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/b61ca074ee1c7e93b5176e10049bdd1f0c200c7be3a0f5c166a7afa55b09fb20.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/6f909de4220daf9f7b821555720612dbc32b466777c234b65a4a2c64e328b8dd.jpg)



(d)



Fig. 1. Schematic of different types of meta-operation loop. (a) Basic meta-operation loop: $T \rightarrow S \rightarrow D \rightarrow I \rightarrow T$ . (b) Generalized meta-operation loop: $T \rightarrow S \rightarrow D \rightarrow I \rightarrow T$ . (c) Generalized meta-operation loop: $T \rightarrow S \rightarrow D \rightarrow I \rightarrow T$ . (d) Generalized meta-operation loop: $T \rightarrow S \rightarrow D \rightarrow S \rightarrow D \rightarrow I \rightarrow T$ .


Based on the above, a UWSoS can be modeled as a heterogeneous network $\mathcal{G} = (V,E,\varphi ,\psi)$ , in which each entity is abstracted as a node and each information flow between two entities is abstracted as a link. $V = V^{S}\cup V^{D}\cup V^{I}\cup V^{T}$ denotes the set of four types of nodes, node type set $\mathcal{A} = \{S,D,I,T\}$ . $E = E^{S\to S}\cup E^{S\to D}\cup E^{D\to D}\cup E^{D\to S}\cup E^{D\to I}\cup$ $E^{I\to T}\cup E^{T\to S}$ denotes the set of seven types of edges and edge type set $\mathcal{R} = \{S\to D,S\to S,D\to S,D\to I,D\to D,I\to T,T\to S\}$ . Each node $v\in V$ has $\varphi (v)\in \mathcal{A}$ , and each link $e\in E$ has $\psi (e)\in \mathcal{R}$ . Unmanned entities usually perform missions in swarm patterns; thus, UWSoS can also be expressed as $\mathcal{G} = \{G_i\}$ , where $G_{i}$ represents the unmanned weapon swarm $i$ . 

# 2.2. The performance measure of UWSoS

The operation loop is the path instance of the meta-operation loop, which describes the operational process of an unmanned weapon system-of-systems. Therefore, the number of operation loops is a comprehensive indicator to measure the performance of the UwSoS. More operation loops indicate more available methods for the destruction of target entities [28,45]. Furthermore, the capability of each entity and the length of the operation loop are considered in Ref. [47]. This shows that the higher the capability of the entity, the higher the capability of the operation loop, the shorter the length of the chain, and the reliability of the system. However, the computational complexity may increase as the number of nodes in the network increases, and it will be more difficult to search all operation loops in a limited time. In addition, the types of meta-operation loops can be tailored depending on the actual environment because not all types are used frequently in confrontations. We adopted the method proposed by Li [47] to measure the performance of the UwSoS and limit the meta-operation loops to the four types shown in Fig. 1. The capability of an operation loop, $U(p_{j})$ , was measured using Eq. (1). 

$$
U \left(p _ {j}\right) = \frac {1}{\left| p _ {j} \right|} \times C A _ {T} (t e) \times \sum_ {v _ {j} \in P S} C A _ {S} \left(v _ {j}\right) \times \sum_ {v _ {j} \in P D} C A _ {D} \left(v _ {j}\right) \times \sum_ {v _ {j} \in P I} C A _ {I} \left(v _ {j}\right) \tag {1}
$$

where $p_j$ represents an operation loop containing a target entity $te$ , a sensor entity set $PS$ , a decider entity set $PD$ , and an influencer entity set $PI$ . $CA_T$ denotes the anti-reconnaissance capability of the target entity, $CA_S$ , $CA_D$ , and $CA_I$ denotes the sensor, decider, and influencer capabilities of the unmanned weapon systems, respectively. $\left|p_j\right|$ represents the length of the operation loop $p_j$ . The performance indicator of UwSoS $f(\mathcal{G})$ was measured using Eq. (2). 

$$
f (\mathcal {G}) = \sum_ {i \in V ^ {T}} \sum_ {p _ {j} \in P _ {\mathcal {G}}} w _ {i} \times U (p _ {j}) \tag {2}
$$

where $P_{\mathcal{G}} = \{p_j\}$ is the set of operation loops, and $w_{i}$ is the weight of the target entity $i \in V^{T}$ . 

# 2.3. The resilience process of UWSoS

This study examines the resilience paradigm based on Nan's attack-recovery process [48]. Fig. 2 shows the performance of the UWSoS 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/5bddcd4fd6be6c2d2bf176dbe21a70fbc87830bf98b9c043ab2037134adfcf5a.jpg)



Fig. 2. Illustration of the performance of UwSoS during an integral operation process under an attack [30,37,48].


during an integral operation process under an attack. The first is the original state, from time $t_0$ to $t_a$ , which describes the performance of UWSoS during normal operation. Time $t_a$ is an attacking point, meaning the enemy starts attacking. The second is a disruptive state. During the period $[t_a, t_m)$ , attacks occur randomly, and the performance decreases accordingly. The third state is the recovery state from $t_m$ to $t_s$ . UWSoS starts the recovery process at the minimum point $t_m$ , and the performance increases with the execution of the reconfiguration strategy. During this period, the performance transcends the mission baseline at $t_r$ , meaning the UWSoS is restored to the mission requirement and $t_r$ is the restoration time. The mission baseline in the UWSoS is the basic requirement to complete the mission in the confrontation. When the performance is larger than the mission baseline, the UWSoS can complete the mission by 100%. Otherwise, the UWSoS will run in a degraded operation state and only complete part of the mission. The part above the mission baseline is regarded as a redundant performance for the UWSoS. The fourth state describes the phenomenon in which the performance of UWSoS reaches a new steady state. In this study, the proposed cooperative reconfiguration model mainly works in the time from $t_m$ to $t_f$ , and it aims to increase the shadow area in Fig. 2. Meanwhile, the number of operation loops is used as the performance indicator of the UWSoS, that is, $y = f(G)$ . 

# 3. Multi-swarm-based cooperative reconfiguration model

In this section, a mission-oriented UwSoS resilience metric is first extended. Subsequently, a multi-swarm cooperative reconfiguration model is proposed to maximize the resilience of the UwSoS under the attack-recovery process. 

# 3.1. Resilience metrics of UWSoS

The selection of an appropriate resilience metric for UwSoS is essential for the reconfiguration model, as it provides evaluation criteria for the optimization objective. Inspired by Tran [30] and Bai's [31] proposed integral resilience evaluation method, we believe that the mission baseline of UwSoS is not equal to the initial performance [30] or the restored performance [31]. In addition, the mission baseline would vary with the requirement and is usually smaller than the initial value, which is simplified as a specified ratio of initial performance in this study. The part above the mission baseline is also important for resilience evaluation. When the performance reaches the mission baseline, it should exceed the mission baseline as much as possible because it has a better tolerance. Further, the restoration time should be equal to the time of the restoration point, not the time of the steady point; as soon as the performance reaches the mission baseline, it means that the UwSoS can accomplish the mission. Thus, the improved mission-oriented resilience metric $\mathcal{R}_{CF}$ is shown in Eq. (3). 

$$
\mathcal {R} _ {C F} = \frac {\sum_ {t = t _ {0}} ^ {t _ {f}} \min  \left(y _ {t} , y _ {b}\right)}{y _ {b} \cdot \left(t _ {f} - t _ {0} + 1\right)} \cdot \frac {y _ {r}}{y _ {b}} \cdot \left[ \frac {y _ {m}}{y _ {0}} + 1 - \eta^ {\left(\frac {y _ {r} - y _ {m}}{y _ {b}}\right)} + \varsigma \right], \tag {3}
$$

where $0 \leq \mathcal{R}_{CF} < \infty$ . $y_0 \in [0, \infty)$ is the initial performance value, $y_b \in [0, y_0]$ is the mission baseline value, $y_m \in [0, y_0]$ is the minimum performance after attack, $y_t \in [0, \infty)$ is the performance value of UwSoS at time $t$ , $y_r \in [0, \infty)$ is the mean restoration value during $[t_r, t_f]$ , and $\eta \in [0, 1]$ is the restoration time factor. $\varsigma \in [0, \infty)$ is the completion factor used to reflect the dynamic behavior of the UwSoS restored redundant performance. The factors $y_r$ , $\eta$ , and $\varsigma$ are expressed as 

$$
y _ {r} = \left\{ \begin{array}{c c} \frac {\sum_ {t = t _ {r}} ^ {t _ {f}} y _ {t}}{\left(t _ {f} - t _ {r} + 1\right)}, & t _ {m} <   t _ {r} \leq t _ {f} \\ y _ {s}, & t _ {r} > t _ {f} \end{array} , \right. \tag {4}
$$

$$
\eta = \left\{ \begin{array}{c c} \frac {t _ {r} - t _ {0}}{t _ {f} - t _ {0}}, & t _ {m} <   t _ {r} \leq t _ {f} \\ 1, & t _ {r} > t _ {f} \end{array} , \right. \tag {5}
$$

$$
\varsigma = C _ {m} \cdot \frac {y _ {r}}{y _ {b}} \cdot \mathbb {I} (M = = 1), \tag {6}
$$

where $y_{s}$ is the new steady performance value and $t_r > t_f$ means the performance is not restored to the mission baseline during $(t_m, t_f]$ . $\mathbb{I}$ is the mission indicator function, when the mission baseline is reached, $M == 1$ , the value $\mathbb{I} = 1$ otherwise, it equals 0. $C_M$ is a hyperparameter, and $C_M > 0$ , reflecting the importance of the completion factor $(\varsigma)$ in UwSoS resilience. When $C_M = 0$ , the mission completion factor is not considered, it is described as $\mathcal{R}_{NCF}$ , as shown in Eq. (7). 

$$
\mathcal {R} _ {N C F} = \frac {\sum_ {t = t _ {0}} ^ {t _ {f}} \min  \left(y _ {t} , y _ {b}\right)}{y _ {b} \cdot \left(t _ {f} - t _ {0} + 1\right)} \cdot \frac {y _ {r}}{y _ {b}} \cdot \left[ \frac {y _ {m}}{y _ {0}} + 1 - \eta^ {\left(\frac {y _ {r} - y _ {m}}{y _ {b}}\right)} \right]. \tag {7}
$$

where $0 \leq \mathcal{R}_{NCF} < \infty$ . 

# 3.2. Mathematical model

# 3.2.1. Assumptions

There are several assumptions for the proposed method, which are stated as follows: 

- Interference events are mainly assumed to be attacked by opponents, and each disrupted entity of the UWSoS is subjected to complete disruption. Simultaneously, the links connected to the disrupted entity are disconnected. 

- Each disrupted entity in each swarm of the UWSoS can be replaced by the same type of existing entity in other swarms. If both connecting entities exist, the previously damaged links can be reconnected. 

- Each entity of the UWSoS executes the cooperation or replacement action only once in the entire process. 

- Only one cooperation action is implemented per time step, and it is completed within one step. 

- Cooperation action only occurs in different swarms, and synergy in the same network is not considered here. 

# 3.2.2. Cooperative factor-based resilience objective

Considering the large number and low cost of entities in UwSoS, it is not cost-effective to repair entities after an attack. The proposed method takes advantage of the agile deployment of entities for reconfiguration through the cooperation of entities in different swarms and uses a slight loss in the performance of the cooperative swarm to obtain a large increment in the performance of the replaced swarm. Consequently, the overall performance was restored, and the resilience of the UwSoS was enhanced. 

Assume that there is a set of available recovery periods $\mathbb{T} = \{t_m,\dots ,t_f\}$ and a set of unmanned weapon swarms $K$ in the UwSoS. Using the network model, there is a node set $V^{k}$ and a link set $E^k$ for each network $k\in K$ . Each network $k$ has a set of disrupted nodes $V^{\prime k}$ and a set of existing nodes $V^{k}\backslash V^{\prime k}$ after an attack. As shown in Fig. 3, four main steps were executed using the multi-swarm cooperative reconfiguration method. Step 1: select an existing node $i\in V^k\backslash V^k$ in one network, called a cooperative node $(\gamma)$ , and its network $k$ is called a cooperative network. Step 2: select a disrupted node $j\in V^{\prime k^{\prime}}$ in another network, called the replaced node $(\delta)$ , and its network $k^{\prime}$ is called the replaced network. Step 3: establish a cooperative pair $\left(\gamma_t^k,\delta_t^{k'}\right)$ , indicating the cooperative node to take over the replaced node at time $t$ . Step 4: optimize a series of cooperative pairs during the time $[t_m,t_f]$ and reconfigure the UwSoS topology to obtain maximum resilience. In the operation process, each existing system in the UwSoS sends status information to the control center through the communication link per time. Thus, the decision-makers have complete information of the confrontation environment and send back reconfiguration order, which is obtained using the proposed method, to each existing system through the control center at each time step. 

Hence, the objective function of the cooperative factor-based resilient UWSoS can be mathematically represented by Eq. (8). 

$$
\max  C _ {1} \cdot \sum_ {k \in K} \mu^ {k} \cdot \mathcal {R} _ {C F} ^ {k} + C _ {2} \cdot \Delta^ {\mathbb {I} (M _ {U W, S o S} = = 1)} \tag {8}
$$

where $\mu^k$ is the weight of swarm $k\in K$ in UwSoS such that $\sum_{k\in K}\mu^{k} = 1$ . $\mathcal{R}_{CF}^{k}$ is the completion factor-based resilience of the swarm $k$ . $M_{UWSoS}$ is the mission completion indicator of UwSoS. When all the swarms' performances are larger than their mission baseline, the value of $\mathbb{I} = 1$ otherwise, $\mathbb{I} = 0$ . $C_1$ and $C_2$ are hyperparameters that reflect the importance between the resilience value and redundant performance and $C_1 + C_2 = 1$ . $\Delta$ is a cooperation factor that represents the degree of redundancy performance of all networks through cooperation. The larger the value, the better the overall redundant performance restored. It is expressed as: 

$$
\Delta = \left(\prod_ {k \in K} \frac {y _ {r} ^ {k}}{y _ {b} ^ {k}}\right), \tag {9}
$$

where $y_r^k$ and $y_b^k$ are the mean of the restoration performance value and mission baseline value for swarm $k$ , respectively. 

# 3.2.3. Cooperative reconfiguration constrains

Several sets of constraints are considered in the proposed optimization model: (i) reconfiguration constraints, (ii) performance constraints, and (iii) decision variable constraints. All sets of constraints are explained and formulated in the following paragraph. 

(i) Reconfiguration constraints are indicated by constraints (10)-(15). $\alpha_{it}^{k}$ and $\beta_{jt}^{k}$ are decision variables representing whether the existing node $i \in V^{k} \backslash V^{\prime k}$ and disrupted node $j \in V^{\prime k}$ in the network $k \in K$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/61f26e5bf82a7ec5c0c55d79333d96d6e5498457726e0441189798661b5dfa19.jpg)



Fig. 3. Illustration of the multi-swarm cooperative reconfiguration process.


are selected at time $t$ , respectively. Constraints (10)-(12) ensure that each network can perform cooperation or replacement action no more than once at a time. Constraint (13) ensures that if an existing node is selected in network $k$ , a disrupted node should be selected in another network $k'$ simultaneously. Constraint (14) ensures that all existing nodes in each network may perform cooperation actions only once in the entire cycle. Thus, do all disrupted nodes for replacement actions in constraint (15). 

$$
\sum_ {i \in V ^ {k} \backslash V ^ {\prime k}} \alpha_ {i t} ^ {k} + \sum_ {j \in V ^ {\prime k}} \beta_ {j t} ^ {k} \leq 1, \forall k \in K, t \in \mathbb {T} \tag {10}
$$

$$
\sum_ {k \in K} \sum_ {i \in V ^ {k} \backslash V ^ {\prime k}} \alpha_ {i t} ^ {k} \leq 1, \forall t \in \mathbb {T} \tag {11}
$$

$$
\sum_ {k \in K} \sum_ {j \in V ^ {\prime} k} \beta_ {j t} ^ {k} \leq 1, \forall t \in \mathbb {T} \tag {12}
$$

$$
\sum_ {k \in K} \sum_ {i \in V ^ {k} \backslash V ^ {\prime k}} \alpha_ {i t} ^ {k} - \sum_ {k ^ {\prime} \in K} \sum_ {j \in V ^ {\prime} \backslash k ^ {\prime}} \beta_ {j t} ^ {k ^ {\prime}} = 0, \forall t \in \mathbb {T}, k \neq k ^ {\prime} \tag {13}
$$

$$
\sum_ {t \in \mathbb {T}} \alpha_ {i t} ^ {k} \leq 1, \forall i \in V ^ {k} \backslash V ^ {\prime k}, k \in K \tag {14}
$$

$$
\sum_ {t \in \mathbb {T}} \beta_ {j t} ^ {k} \leq 1, \forall j \in V ^ {\prime k}, k \in K \tag {15}
$$

(ii) Performance constraints are represented by constraints (16)-(18). Constraints (16) and (17) indicate that the cooperative node $\gamma_t^k$ and replaced node $\delta_t^{k'}$ are obtained using decision variables. Constraint (18) indicates that only the cooperative node and replaced node of the same type can perform cooperative action, and $\varphi$ is the node type mapping function. 

$$
\gamma_ {t} ^ {k} = \left\{i \mid \alpha_ {i t} ^ {k} = 1, k \in K, i \in V ^ {k} \backslash V ^ {\prime k} \right\}, \forall t \in \mathbb {T} \tag {16}
$$

$$
\delta_ {t} ^ {k ^ {\prime}} = \left\{j \mid \beta_ {j t} ^ {k ^ {\prime}} = 1, k ^ {\prime} \in K, j \in V ^ {\prime k ^ {\prime}} \right\}, \forall t \in \mathbb {T} \tag {17}
$$

$$
\varphi \left(\gamma_ {t} ^ {k}\right) = \varphi \left(\delta_ {t} ^ {k ^ {\prime}}\right) \in \mathcal {A}, k \neq k ^ {\prime} \in K \tag {18}
$$

(iii) Decision variable constraints are represented by constraints (19) and (20). It denotes the binary decision variables for the existing node $i \in V^k \backslash V'^k$ and disrupted node $j \in V'^k$ in the network $k \in K$ at time $t \in \mathbb{T}$ . 

$$
\alpha_ {i t} ^ {k} \in \{0, 1 \}, \forall i \in V ^ {k} \backslash V ^ {\prime k}, k \in K, t \in \mathbb {T} \tag {19}
$$

$$
\beta_ {j t} ^ {k} \in \{0, 1 \}, \forall j \in V ^ {\prime k}, k \in K, t \in \mathbb {T} \tag {20}
$$

# 4. Illustrative experiments

In this section, numerical experiments are presented to illustrate the feasibility, effectiveness, and superiority of the proposed method. The effectiveness of the proposed resilience metric is described in Section 4.2. In Section 4.3, the feasibility of the proposed method is verified through the cooperative reconfiguration process, and the effectiveness of the proposed method is demonstrated through various attack scenario experiments. Subsequently, the superiority of the proposed method is exhibited using the algorithm comparison experiments in Section 4.4. Finally, the parameter analysis is described in Section 4.5. 

# 4.1. Experiment description

# 4.1.1. Generation method of the UWSoS

The UwSoS is open, and its scale varies with the systems added, removed, and modified. In addition, it usually performs missions in a multi-swarm pattern. Our proposed method is illustrated with fictional UwSoS generated by the proximal topology generator, and its process is executed in two stages: (i) generating an individual unmanned weapon swarm, and (ii) combining the swarms as a system-of-systems. 

For the first phase of the generation process, a weapon system-of-systems topology generator proposed by Li [49] was adopted. Each swarm was initially seeded with fewer systems. At each time step, a new random entity was added to the swarm from the final system set and connected to the existing entities based on the connection probability and information flow type. In contrast to Li's method [49], a maximum node degree constraint was added to limit the number of connections per node such that the connection capacity threshold should not be exceeded. For the second phase of the combining process, a system-of-systems is obtained by assembling the generated swarms according to the mission. 

# 4.1.2. Data preparation

The UWSoS is constructed by combining these swarms based on the mission. The general properties of the three swarms are listed in Table 1. Each swarm has a different structure because of its purpose: Swarm 1 mainly focuses on reconnaissance missions, composed of 20 sensor, 10 decider, 15 influencer, and 5 target entities. Swarm 2 needs to make more decisions when performing its mission. Thus, it is composed of 20 sensor, 15 decider, 10 influencer, and 5 target entities. Swarm 3 required more attack missions. Thus, it consists of 15 sensor, 10 decider, 20 influencer, and 5 target entities. There are seven types of edges in each swarm, and their statistical information is presented 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/6295b4228ffbb52e9e576d7fc29346902a0b192ff4fa332c648043a6490a35c4.jpg)



(a) Swarm 1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/df985a293e01f354bee1e2445bbe7fc918143426fe8e0e8e872c8b1bd89dfc7b.jpg)



(b) Swarm 2


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/a0721f23013501547bbe94dc658f39c8e973e2ce10f492489d564e1f32bf8358.jpg)



(c) Swarm 3



Fig. 4. A constructed UwSoS with three swarms. The UwSoS is constructed with sensor (purple), decider (orange), influencer (green), and target entities (red).



Table 1 General properties of swarms.


<table><tr><td>Name</td><td>Network topology</td><td>V</td><td>E</td><td>VS</td><td>VD</td><td>VI</td><td>VT</td><td>\(\overline{\text{deg}}\)</td></tr><tr><td>G1</td><td>Swarm 1</td><td>50</td><td>200</td><td>20</td><td>10</td><td>15</td><td>5</td><td>4</td></tr><tr><td>G2</td><td>Swarm 2</td><td>50</td><td>209</td><td>20</td><td>15</td><td>10</td><td>5</td><td>4.18</td></tr><tr><td>G3</td><td>Swarm 3</td><td>50</td><td>204</td><td>15</td><td>10</td><td>20</td><td>5</td><td>4.08</td></tr></table>

in Table 2. It is assumed that the capabilities of each entity are set to be unified. Further, the synergy only utilizes the existing UwSoS, and the cooperative action is assumed to be completed within the per time step. Hence, the cost of finance, time, and ease, are set as constants and satisfy the reconfiguration cost constraints. Fig. 4 shows the topological UwSoS constructed from the dataset. Nodes in the topology represent UwSoS entities, and the edges represent the information flow between entities. 

To access the proposed multi-swarm cooperative reconfiguration model, an optimal cooperative reconfiguration strategy, composed of a series of cooperative pairs, is obtained using a genetic algorithm in Python 3.7. The simulation period was set to 30 time steps, which included three periods: stable original operation period $(t = 0\sim 4s)$ , under attack period $(t = 5\sim 14s)$ , and cooperative reconfiguration period $(t = 15\sim 29s)$ . 

# 4.2. Mission-oriented resilience measure for UWSoS

In this section, five resilience metrics were analyzed to verify that the proposed metrics are more suitable to describe the mission-oriented UwSoS. Two identical networks, $G_1'$ and $G_1''$ , which have the same topology as Swarm 1, were used to perform various missions in this experiment. Four typical cases of different mission completion were obtained by adjusting the coefficient $\varepsilon$ . The detailed parameters are listed in Table 3. 

In the random node-attacking mode in which nodes are randomly attacked from a swarm, nodes 2, 29, 36, and 41 in $G_1'$ , nodes 17, 20, 44, 24, and 36 in $G_1''$ are destroyed sequentially. Thus, two cooperative strategies, namely Strategy 1 and Strategy 2, are obtained through the proposed method to restore the performance. The two strategies differ in that the performance curve of $G_1'$ in Strategy 1 slightly declines after $t = 24$ s. Fig. 5 shows the performance and mission baseline curves of $G_1'$ and $G_1''$ in four cases. Figs. 5(a)-(d) represent the trajectories of Strategy 1, which have the same performance and different mission baselines. Fig. 5(a) shows that $G_1'$ and $G_1''$ cannot be restored to the baseline. Fig. 5(b) shows that $G_1'$ restores to the baseline, but $G_1''$ fails. In Fig. 5(c), the results of $G_1'$ and $G_1''$ are reversed. Fig. 5(d) shows that $G_1'$ and $G_1''$ both restore to the baseline. Thus, do Strategy 2 in Fig. 5(e)-(h). 

As shown in Fig. 5(a), Strategy 1 was executed. At $t = 0 \sim 4$ s, $G_1'$ and $G_1''$ have the same performance value of 18.657 because of 

the same topology. Attacks occur randomly from $t = 5$ s to $14$ s, and performance starts to decline. Because the importance and number of disrupted nodes differ, the performances of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ drop to 12.3 and 7.63, respectively. Thus, the reconfiguration strategy is implemented from $t = 15$ s, and their performances are gradually restored (the detailed cooperative reconfiguration process is described in Subsection 4.3). The performance of $G_{1}^{\prime}$ fluctuated slightly during the recovery process and eventually stabilized at 15.083. The performance of $G_{1}^{\prime \prime}$ first decreased and then increased, eventually stabilizing at 14.483. The performance of Strategy 2 is similar to that of Strategy 1; however, the slight difference is that from $t = 24$ s, the performance of $G_{1}^{\prime}$ decreases slightly in Strategy 1. In Fig. 6, three resilience evaluation methods proposed by Tran [30,37], Bai [31], Liu [32], and the two metrics proposed in this study are used to measure the resilience of these cases. The weights of time and performance resilience of Liu's method are both set to 0.5 because they are equally important to UWSoS. 

According to Fig. 6(a), the resilience of case 1-4 calculated using Tran's method is the same, that is, $\mathcal{R}_{\text{Tran}} = 73.8298E - 2$ . Bai's method yielded similar results, that is, $\mathcal{R}_{\text{Bai}} = 81.1580E - 2$ . These values do not change with the mission baseline; however, the resilience calculated using the other three methods varies with the mission baseline and $\mathcal{R}_{\text{case4}} > \mathcal{R}_{\text{case2}} > \mathcal{R}_{\text{case3}} > \mathcal{R}_{\text{case1}}$ . As shown in Fig. 5, in Case 4, the performances of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ are both restored to the mission baseline; thus, the resilience is the highest. In Cases 2 and 3, only one network recovers to the mission baseline, and their restoration points are at $t = 16$ s and $t = 20$ s, respectively. Moreover, the total loss area of Case 2 was smaller than that of Case 3. Thus, the resilience of Case 2 was better than that of Case 3. In Case 1, the resilience is the lowest because $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ do not recover to their mission baseline. Hence, $\mathcal{R}_{\text{Liu}}$ , $\mathcal{R}_{\text{NCF}}$ , and $\mathcal{R}_{\text{CF}}$ can sensitively reflect the changeable mission baseline. When these methods are further compared in Case 1, the resilience of $G_{1}^{\prime}$ is smaller than that of $G_{1}^{\prime \prime}$ when using $\mathcal{R}_{\text{Liu}}$ . However, the proposed methods $\mathcal{R}_{\text{NCF}}$ and $\mathcal{R}_{\text{CF}}$ have opposite results. This is similar to Strategy 2, as shown in Fig. 6(b). According to the performances in Case 1 in Fig. 5, the performance of $G_{1}^{\prime}$ decreases less and recovers faster. In this case, the resilience of $G_{1}^{\prime}$ should be greater than that of $G_{1}^{\prime \prime}$ . As earlier mentioned, $\mathcal{R}_{\text{NCF}}$ and $\mathcal{R}_{\text{CF}}$ can effectively reflect these characteristics, which are more in line with the actual situation. 

Further, we compared the two proposed evaluation methods $\mathcal{R}_{NCF}$ and $\mathcal{R}_{CF}$ , as shown in Fig. 7. In Case 2 and 4, the resilience of $G_{1}^{\prime}$ calculated using $\mathcal{R}_{NCF}$ is equal irrespective of the strategy used (Strategy 1 or 2), as shown in Fig. 7(a). The redundant performance in Strategy 2 is better than that of Strategy 1, as shown in Fig. 5(b), (f), (d), (h), and it is difficult to distinguish $\mathcal{R}_{NCF}$ from this phenomenon. As shown in the enlarged view, the resilience calculated using $\mathcal{R}_{CF}$ in Strategies 1 and 2 are $46.8656E - 2$ and $46.8822E - 2$ , respectively, which are more sensitive to reflect their redundant performance. Fig. 7(b) shows that the resilience of $G_{1}^{\prime \prime}$ calculated using $\mathcal{R}_{CF}$ or $\mathcal{R}_{NCF}$ are 


Table 2 Statistical information of edges of swarms.


<table><tr><td>Name</td><td>Network topology</td><td>S → S</td><td>S → D</td><td>D → D</td><td>D → S</td><td>D → I</td><td>I → T</td><td>T → S</td></tr><tr><td>G1</td><td>Swarm 1</td><td>40</td><td>43</td><td>6</td><td>12</td><td>23</td><td>22</td><td>23</td></tr><tr><td>G2</td><td>Swarm 2</td><td>31</td><td>48</td><td>21</td><td>17</td><td>30</td><td>16</td><td>29</td></tr><tr><td>G3</td><td>Swarm 3</td><td>33</td><td>33</td><td>9</td><td>3</td><td>31</td><td>26</td><td>19</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/84f886302f7cd7f0a7e00b42f3484502d8ecd466ba6222e9c94c7622d4fb7101.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/e43124f9e4d6ed553a5798b4b2ee208780590da1b08d25db496272a877f98a0f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/abec511aa9b600733a6b1db28c1bb0b0c42f1be233a7433454697e7656ddf474.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/2d4d3de8fb090a7e442d1513597055c1e8b9ce2082e4df00264a4661250d614f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/4a94caa0a07de39e2cbd3a83f2120c91785a3416d031d127c70644f018df2db6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/e070dd342eb2df403f43cc66eb68aba37733123bc147c376ab8d127ce22cfe70.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/5ca44259fe8305543e06949e31487ae6bc452a0013145061f412ea56c5e0fdde.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/d35a2e0a907d9eed743ba8f809adead504b00650eb97801c6971098cc55f72a9.jpg)



The performance of $G_{1}^{\prime}$ The performance of $G_{1}^{\prime \prime}$ The mission baseline of $G_{1}^{\prime}$ - The mission baseline of $G_{1}^{\prime \prime}$



Fig. 5. The performance and mission baseline curves of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ in the random node-attacking mode. The performance curve of $G_{1}^{\prime}$ in Strategy 1 shows a slight decrease after $t = 24$ s.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/1abb1f5b2c1e087bb4e3c238ed08f2bab4e6bbb86bca2bf4e8499e59919c99b6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/5f4e606259409a182b5c9fc206ebf329f92e48906a07f303f78073cc5f0f0db4.jpg)



Fig. 6. The resilience of four cases in two strategies. The total resilience is the sum of the resilience of $G_{1}^{\prime}$ (blue) and $G_{1}^{\prime \prime}$ (orange).



Table 3 Mission baseline scaling coefficient $(\varepsilon)$ of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$


<table><tr><td></td><td>Case 1</td><td>Case 2</td><td>Case 3</td><td>Case 4</td></tr><tr><td>Coefficient (ε) of G&#x27;1</td><td>1</td><td>0.8</td><td>0.9</td><td>0.8</td></tr><tr><td>Coefficient (ε) of G&#x27;&#x27;1</td><td>1</td><td>0.8</td><td>0.7</td><td>0.7</td></tr><tr><td>Mission completion</td><td>None</td><td>G&#x27;1</td><td>G&#x27;&#x27;1</td><td>Both</td></tr></table>

the same in Strategies 1 and 2 since they have the same performance trajectory. If the performance is restored to the mission baseline, the resilience calculated using $\mathcal{R}_{CF}$ is higher than that calculated using $\mathcal{R}_{NCF}$ because of the mission completion factor in $\mathcal{R}_{CF}$ . In summary, the proposed metric $\mathcal{R}_{CF}$ can more effectively reflect the resilience of mission-oriented UWSoS, which is more in line with the actual confrontation environment. 

# 4.3. Cooperative reconfiguration method analysis for UWSoS

A detailed cooperative reconfiguration method is analyzed in this section. First, a cooperative reconfiguration process was introduced to demonstrate the feasibility of the proposed method. Subsequently, several disruptive scenarios, including 10 attack modes and 7 attack intensities, were simulated to verify the effectiveness of the proposed method. 

# 4.3.1. Analysis of cooperative reconfiguration process

In this scenario, two networks, $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ , participate in the mission, and the coefficients $(\varepsilon)$ were set to 0.8, that is, the initial performance was 18.657, and the mission baseline was 14.93. A cooperative reconfiguration strategy obtained using the proposed method was used, as shown in Table 4, and the performance trajectory corresponds to 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/dd846b672898d8d3518202b411ab70f8f477b1be2d038912c8b1133403a60214.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/70ec3b612a4ce166717a6383f82a9ab4770b1859dc5b3e0d361d0d469bd78245.jpg)



Fig. 7. Comparison of the resilience of $\mathcal{R}_{NCF}$ and $\mathcal{R}_{CF}$ . $\mathcal{R}_{NCF}$ in Strategy 1 has a blue color, $\mathcal{R}_{CF}$ in Strategy 1 has an orange color, $\mathcal{R}_{NCF}$ in Strategy 2 has a green color, and $\mathcal{R}_{CF}$ in Strategy 2 has a red color.



Table 4 A cooperative reconfiguration strategy of UwSoS.


<table><tr><td>t</td><td>Enable</td><td>Cooperative pair</td><td>f(G1′)</td><td>f(G1′′)</td><td>t</td><td>Enable</td><td>Cooperative pair</td><td>f(G1′)</td><td>f(G1′′)</td></tr><tr><td>14</td><td>No</td><td>-</td><td>12.30</td><td>7.63</td><td>20</td><td>Yes</td><td>(27G1′, 20G1′′)</td><td>15.32</td><td>14.43</td></tr><tr><td>15</td><td>Yes</td><td>(27G1′′, 29G1′)</td><td>14.91</td><td>7.23</td><td>21</td><td>Yes</td><td>(42G1′, 36G1′′)</td><td>15.32</td><td>14.48</td></tr><tr><td>16</td><td>Yes</td><td>(13G1′′, 2G1′)</td><td>16.16</td><td>7.23</td><td>22</td><td>Yes</td><td>(41G1′, 41G1′)</td><td>15.32</td><td>14.48</td></tr><tr><td>17</td><td>Yes</td><td>(23G1′, 24G1′′)</td><td>15.09</td><td>9.25</td><td>23</td><td>No</td><td>-</td><td>15.32</td><td>14.48</td></tr><tr><td>18</td><td>Yes</td><td>(31G1′, 44G1′′)</td><td>15.09</td><td>12.87</td><td>24</td><td>Yes</td><td>(9G1′, 17G1′′)</td><td>15.08</td><td>14.48</td></tr><tr><td>19</td><td>Yes</td><td>(31G1′′, 36G1′)</td><td>15.72</td><td>12.87</td><td>...</td><td>...</td><td>...</td><td>...</td><td>...</td></tr></table>

Fig. 5(b). During the entire period, the reconfiguration process starts at $t = 15$ s and ends at $t = 29$ s. After $t = 25$ s, no action was activated, and their performances are the same as $t = 24$ s; thus, it is no longer redundantly displayed in Table 4. 

At $t = 14$ s, the performances of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ both fall behind the mission baseline, and the synergy action was enabled the next second. At $t = 15$ s, the cooperative pair is $(27^{G_{1}^{\prime \prime}}, 29^{G_{1}^{\prime}})$ , meaning node 27 in $G_{1}^{\prime \prime}$ is selected to replace the disrupted node 29 in $G_{1}^{\prime}$ . Therefore, $f(G_{1}^{\prime})$ increased to 14.91, and $G_{1}^{\prime \prime}$ reduced to 7.23. None reached the mission baseline, and cooperation continued. At $t = 16$ s, $f(G_{1}^{\prime})$ increased to 16.16, and $G_{1}^{\prime}$ met the mission requirements. $G_{1}^{\prime \prime}$ remained at 7.23, indicating that the removal of node 13 in $G_{1}^{\prime \prime}$ will not influence its performance in this scenario. Meanwhile, $f(G_{1}^{\prime})$ is larger than the mission baseline of 1.25, and $G_{1}^{\prime \prime}$ is less than the mission baseline of 7.68. Hence, at $t = 17$ s, the cooperative pair $(23^{G_{1}^{\prime}}, 24^{G_{1}^{\prime \prime}})$ is used to slightly reduce the performance of $G_{1}^{\prime}$ and improve the performance of $G_{1}^{\prime \prime}$ . Thus, owing to the back-and-forth cooperation between $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ , the performances are eventually restored to 15.08 and 14.48 until $t = 24$ s. Although $G_{1}^{\prime \prime}$ does not reach the mission baseline in the end, its performance is significantly improved by 6.85, only 0.43 lower than the mission baseline. The results show that the proposed method can generate a feasible cooperative reconfiguration strategy to restore performance. 

4.3.2. Analysis of cooperative reconfiguration method in different attack modes 

The proposed method was applied in ten attack modes to illustrate its effectiveness. Four basic node-attacking strategies are designed: a mixed node type attack strategy (MA), a sensor node attack strategy (SA), a decider node attack strategy (DA), and an influencer node attack strategy (IA). They show that the mixed, sensor, decider, and influencer nodes are attacked in descending order of node degree, respectively. In the case of the attacked network and intensity, the above strategies are combined in pairs to obtain ten attack modes, as shown in Table 5. The coefficients $(\varepsilon)$ of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ are set to 0.8 and 0.7, that is, the mission baseline values are 14.93 and 13.06, respectively. 


Table 5 Description of 10 attack modes. Using varied numbers of disrupted nodes to indicate different attack intensities.


<table><tr><td rowspan="2">No.</td><td rowspan="2">Mode</td><td colspan="2">Attacked nodes</td></tr><tr><td>G&#x27;1</td><td>G&#x27;&#x27;1</td></tr><tr><td>1</td><td>MA-MA</td><td>44, 38, 29, 27</td><td>44, 38, 29, 27, 26, 25, 14, 11</td></tr><tr><td>2</td><td>SA-SA</td><td>18, 14, 12, 11</td><td>18, 14, 12, 11, 10, 5, 8, 2</td></tr><tr><td>3</td><td>DA-DA</td><td>29, 27, 26, 25</td><td>29, 27, 26, 25, 24, 22, 21, 20</td></tr><tr><td>4</td><td>IA-IA</td><td>44, 38, 39, 37</td><td>44, 38, 39, 37, 35, 43, 36, 41</td></tr><tr><td>5</td><td>SA-DA</td><td>18, 14, 12, 11</td><td>29, 27, 26, 25, 24, 22, 21, 20</td></tr><tr><td>6</td><td>SA-IA</td><td>18, 14, 12, 11</td><td>44, 38, 39, 37, 35, 43, 36, 41</td></tr><tr><td>7</td><td>DA-IA</td><td>29, 27, 26, 25</td><td>44, 38, 39, 37, 35, 43, 36, 41</td></tr><tr><td>8</td><td>DA-SA</td><td>29, 27, 26, 25</td><td>18, 14, 12, 11, 10, 5, 8, 2</td></tr><tr><td>9</td><td>IA-SA</td><td>44, 38, 39, 37</td><td>18, 14, 12, 11, 10, 5, 8, 2</td></tr><tr><td>10</td><td>IA-DA</td><td>44, 38, 39, 37</td><td>29, 27, 26, 25, 24, 22, 21, 20</td></tr></table>

As observed in Fig. 8, the proposed method can restore the performance in these modes; however, the restoration increment varies with the attack mode. In the IA-IA mode, the reconfiguration effect was the best. The performances of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ were restored to the original level at $t = 25$ s and $t = 24$ s, respectively. In the five attack modes of MA-MA, IA-IA, SA-IA, DA-IA, and IA-SA, both $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ can recover to their mission baselines, which means having the capability to complete the mission. In the other five modes, the lightly damaged network $G_{1}^{\prime}$ is preferentially restored to the mission baseline and then recovers another network. Eventually, the severely damaged network, $G_{1}^{\prime \prime}$ , fails to reach the mission baseline. At this moment, additional methods are needed to restore performance, such as the addition of new nodes to $G_{1}^{\prime \prime}$ . The performance of $G_{1}^{\prime}$ increases the fastest in the MA-MA mode, reaching the mission baseline at $t = 15$ s. Similarly, $G_{1}^{\prime \prime}$ in the SA-IA mode reached its restoration point at $t = 17$ s. In the DA-DA and DA-SA modes, the performance of $G_{1}^{\prime}$ has the slightest decrease, and in the DA-DA, SA-DA, and IA-DA modes, the performance of $G_{1}^{\prime \prime}$ had the most significant decrease, dropping to 0.87. The above phenomenon shows that in the DA-based attack modes if the decider node is lightly attacked, the network can better recover because of the existing redundant nodes; however, if the number of decider 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/08f04c54cd865b41b5e9be0e308d026d42db0ec87ac97a7721d492f76dc47e53.jpg)



Fig. 8. The performance and mission baseline curves of $G_{1}^{\prime}$ and $G_{1}^{\prime \prime}$ in 10 attack modes. Four nodes are disrupted in $G_{1}^{\prime}$ (blue), eight nodes are disrupted in $G_{1}^{\prime \prime}$ (yellow).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/ef48b8a5fc5f68c92340b61475a9f3cb97f6be3cd7f50358bd4c4b25354f0537.jpg)



Fig. 9. The resilience of UWSoS in 10 attack modes. The resilience of UWSoS is the sum of the resilience of $G_1'$ (blue) and $G_1''$ (orange).


nodes is massively attacked, the network is almost paralyzed, and its performance is difficult to recover. It also reveals that decide nodes play an important role in the network, and it is necessary to protect the decide nodes during the operation of UWSoS. In the DA-DA, SA-DA, and IA-DA modes, the performance of $G_{1}^{\prime}$ reduced to increase the performance of $G_{1}^{\prime \prime}$ at the final moment to gain the overall resilience enhancement. 

The resilience of the UwSoS in ten attack modes was measured, as shown in Fig. 9. UwSoS had the highest resilience in the DA-IA mode, but the worst in the DA-DA mode. The highest resilience of $G_{1}^{\prime}$ appeared in the DA-SA mode. In the SA-IA mode, the resilience of $G_{1}^{\prime}$ was the lowest; the resilience of $G_{1}^{\prime \prime}$ was the highest, and the resilience of each network was relatively balanced. $G_{1}^{\prime \prime}$ had the lowest resilience in the SA-DA mode. In each attack mode, the resilience of $G_{1}^{\prime}$ was significantly higher than that of $G_{1}^{\prime \prime}$ . Because $G_{1}^{\prime}$ is attacked lightly, the performance degradation is lower than that of $G_{1}^{\prime \prime}$ . Meanwhile, the method is usually preferred to recover $G_{1}^{\prime}$ ; thus, $G_{1}^{\prime}$ is restored faster than $G_{1}^{\prime \prime}$ . In addition, the performance of $G_{1}^{\prime \prime}$ reduced significantly after a severe attack. It requires a long time to recover, and sometimes it cannot even return to the mission baseline. 

Overall, the proposed method can effectively restore the performance of UwSoS in different attack modes, and the lightly damaged network is first restored. In the DA-IA mode, the performance was best restored, and its resilience was the highest. In DA-DA, SA-DA, and IA-DA modes, only the lightly damaged network can be restored, and if 

the severely damaged network is required to have higher performance, additional decide nodes need to be added. 

# 4.3.3. Analysis of cooperative reconfiguration method in different attack intensities

In this section, in the maximum or minimum node degree-based node-attacking strategy, seven levels of attack intensities are considered to verify the proposed method. Seven attack intensities were designed as follows: (i) The intensity factors $(r_{atk})$ were set as 0.1, 0.2, ..., 0.7. (ii) The number of disrupted nodes for each type was obtained, rounded up the result of the intensity factor $(r_{atk})\times$ the initial number of each type of node. (iii) At most two nodes are attacked per time for each type. The maximum or minimum node degree-based node-attacking strategies denote that the nodes are attacked in descending or ascending order of node degree. $G_{1}$ , $G_{2}$ , and $G_{3}$ are used in this experiment, and the coefficients $(\varepsilon)$ are all set to 0.8, as shown in Table 6. 

Fig. 10 shows the performance trajectories of UwSoS, $G_{1}$ , $G_{2}$ and $G_{3}$ for seven intensities; the proposed method also effectively restores the performance, and the recovery effects are related to the intensity level. As shown in Fig. 10(a), at intensities of 0.1 and 0.2, the performances are restored to the mission baseline. However, at the other intensities, the performances of UwSoS did not recover to the mission baseline; however, when compared with their lowest performance, they increased by $2.60\%$ , $7.46\%$ , $17.88\%$ , $24.57\%$ and $25.99\%$ , respectively. For the maximum node degree-based node-attacking strategy in Fig. 10(e), at 0.1 intensity, the performance of UwSoS is restored to the mission baseline. At the other six intensities, the performances slowly increased by $39.91\%$ , $20.51\%$ , $12.27\%$ , $0.93\%$ , $0.16\%$ , and $0.13\%$ , respectively, from their lowest values. Particularly at intensities of 0.6 and 0.7, UwSoS is almost paralyzed and difficult to recover. Because a high-intensity attack yields many disrupted nodes, it is difficult to form operation loops on the remaining nodes, even if reconfiguration is executed. Hence, new nodes are required to join these attack scenarios. Fig. 10(b)-(d) and (f)-(h) show that at low-intensity attacks, each network can simultaneously restore its performance to the mission baseline. For example, at the 0.1 attack intensity curve (blue) in Fig. 10(f)-(h), the performances of $G_{1}$ , $G_{2}$ and $G_{3}$ are lower than their mission baselines of $54.15\%$ , $48.03\%$ and $20.14\%$ , respectively, after an attacked. Through configuration, they finally recovered $85.70\%$ , $85.2\%$ , and $90.02\%$ of their original performances, respectively, all above the mission baseline. In high-intensity attacks, the lightly damaged network is first recovered, such as $G_{2}$ in the minimum node degree-based strategy and $G_{3}$ in the maximum node degree-based strategy. These characteristics are more significant from the perspective of resilience, as shown in Fig. 11. 


Table 6



Parameters of attacking intensities modes.


<table><tr><td>No.</td><td>Name</td><td>Network topology</td><td>Coefficient (ε)</td><td>Initial performance value</td><td>Mission baseline value</td></tr><tr><td>1</td><td>G1</td><td>Swarm 1</td><td>0.8</td><td>18.657</td><td>14.93</td></tr><tr><td>2</td><td>G2</td><td>Swarm 2</td><td>0.8</td><td>31.25</td><td>25.00</td></tr><tr><td>3</td><td>G3</td><td>Swarm 3</td><td>0.8</td><td>11.75</td><td>9.40</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/2a1afa38c4b078ca7e259bc96b66ef136d321a7947f3daae00dad1b1568af6d6.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/9ff6fc09c716682d56fa5a4b7fe73bd5848a00c783d06d1a48642e1a8508a07f.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/437f11fdefad4270442cbb26437033a044289aed2ce03e2d1b6f18957ffa8729.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/36cc3194cb9c9eeb60a4d06a35cb1aba6ce744a1c3b687c84c3a8cc0eaf3c7b1.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/43fce1b601aac035d6d12ce4617a1f2c8f73f2cb4285b6b4500f01a780b93f5b.jpg)



(e)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/751d8e11dd41cc708cbffdb9b5e4154b53c3de4a6a4c1bed770295437f2f253f.jpg)



(f)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/16492c57bd0b426f5fe782ae4bb04dc378554e10c8ab702cb0a6235f6ac5a574.jpg)



(g)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/b496f18dff69eee3483750772778857268a22f2d2d8eed450b3852cd9057081f.jpg)



0.1 intensity 0.2 intensity 0.3 intensity 0.4 intensity 0.5 intensity 0.6 intensity 0.7 intensity Mission baseline



Fig. 10. The performance and mission baseline curves of UwSoS in 7 attack intensities. The top four figures are in minimum node degree-based node-attacking strategy, and the bottom four figures are in maximum degree-based node-attacking strategy.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/15b24ad92020113cae1f9e1be780979b996103641062db7e765ef7abbf7cd104.jpg)



(a) Minimum node degree node-attacking strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/e90d91e0e0b6ac2e4705ff06c52d3ac2513ddb0d7b1cca8ef41628fe2e148cff.jpg)



(b) Maximum node degree node-attacking strategy



Fig. 11. The resilience of UWSoS in 7 attack intensities. The resilience of UWSoS is the sum of the resilience of $G_{1}$ (blue), $G_{2}$ (orange), and $G_{3}$ (green).


As the attack intensity increases, the resilience gradually decreases. The values decreased faster in Fig. 11(b) than in Fig. 11(a). The higher the degree of a node, the more important it is in the network, and if it is attacked, its performance will significantly decrease. At the same attack intensity, the resilience in the minimum node degree-based strategy is better than that of the maximum node degree-based strategy, which drops to 0 at 0.7 and 0.5, respectively. As shown in Fig. 11(a), the resilience of $G_{1}$ decreased the fastest, and $G_{2}$ decreased the slowest. Initially, the resilience of each network was relatively high; however, as the attack intensity increased, only $G_{2}$ had little resilience. Similar results were obtained for $G_{3}$ , as shown in Fig. 11(b). 

In summary, the proposed method can restore the performance of UwSoS at different attack intensities. The UwSoS has a better restored performance and stronger resilience in low-intensity attacks. Further, if the attack intensity is 0.1 or 0.2 in the minimum node degree-based strategy, UwSoS can recover to the mission baseline. This is similar to 

a 0.1 intensity of the maximum node degree-based strategy. For other intensity levels, if the UwSoS needs to properly recover and reach high resilience, additional nodes are required to join. 

# 4.4. Algorithms comparison

This section compares the proposed method with other reconfiguration algorithms to demonstrate the superiority of the proposed method. This experiment is simulated at a 0.1 intensity in the maximum node degree-based node-attacking strategy. The five algorithms are briefly described as follows: 

- Self-resistance (SR). UWSoS does not perform any action after an attack and relies only on its resistance capability to withstand disturbances. There was no recovery capability in this method. 

- Random node reconnection (RN) [37]. A disrupted node was randomly selected for each network per time step. Subsequently, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/590a7f95f6b4167cb2f5ff5a2fe95ca1c4a9f041de92dbc7abadce9a3a196d5a.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/c6d2da818fa7a1d750dc64cde07466e311cb1631ea2baf8991c4134fab97707e.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/adc65eeed9ba03fc85e5cb970bd60fadae0f88588709465372c689e2bf538488.jpg)



(c)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/a91fa4c42f631fdb5fb8ef1c04c1212c56ac907443f4eafa73d784b162e73d5f.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/b9ed8caf29a59e2f4f162117ade33d538d6127d8288b7de59131f192a0e749df.jpg)



Fig. 12. The performance and mission baseline curves of UwSoS in comparison algorithms.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/74167a6c35787438a8d90f82720ea400cebe219f1a20449e18fd0a0dfd5ab949.jpg)



Fig. 13. The resilience of UwSoS in comparison algorithms. The resilience of UwSoS is the sum of the resilience of $G_{1}$ (blue), $G_{2}$ (orange), and $G_{3}$ (green).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/0c9d9d6b9159651e6f9065521827865f45f49d92feb6ba147c55b01342e6273f.jpg)



Fig. 14. The resilience values of 5 comparison algorithms in each network.


the nodes previously linked to the selected node randomly reconnect to the existing nodes in the same network. In addition, the reconnection links conform to the meta-path types and maximum degree constraints. 

- Maximum degree node reconnection (MDN). It is similar to the RN; however, the disrupted and reconnected nodes are chosen based on the maximum node degree preference. 

- The proposed method with no completion factor (NCF). Adopt the proposed cooperative reconfiguration method; however, the optimal objective is Eq. (7). 

- The proposed method with completion factor (CF). It is similar to NCF; however, the optimal objective is changed to Eq. (3). 

Fig. 12 shows the performance trajectories of UwSoS, $G_{1}$ , $G_{2}$ , and $G_{3}$ in the five reconfiguration algorithms. As shown in Fig. 12(a), the reconfiguration algorithms NCF and CF are superior to the others, and they are the only two algorithms that can restore the performance of UwSoS to the mission baseline. Further, the proposed CF method is better than the NCF, and the SR algorithm is the worst. As regards resilience, the results are similar, as shown in Fig. 13. The values were 0.583@SR, 0.853@RN, 1.292@MDN, 1.807@NCF, and 1.811@CF. When adopting the proposed CF method, the UwSoS was more resilient than the others. 

Further, the performance curves for each network were compared, as shown in Fig. 12(b)-(d). Only the NCF and CF methods can restore the performance of each network to the mission baseline. Meanwhile, MDN can also drive the performance to reach the mission baseline in $G_{3}$ , and it restores faster than others; however, the effect of the MDN method is significantly influenced by the network structure. For example, in $G_{3}$ , the disrupted influencer nodes have more redundancy, and it is easier to form operation loops by reconnecting the maximum 

degree nodes; however, it performs poorly in different structures of $G_{1}$ and $G_{2}$ . Furthermore, this phenomenon indicates that the performance of reconfiguration in the same network is easily influenced by the network structure. However, the proposed method can overcome this deficiency and better perform in different network structures, which can clearly be seen from the perspective of resilience values in Fig. 14. The resilience of the proposed CF method is relatively balanced in each network and performs best in $G_{1}$ and $G_{2}$ , and third in $G_{3}$ . 

In summary, the proposed method has better recovery increments for each network and better adaptability for various network structures. Further, the CF method is more suitable to design a resilient UwSoS than others. 

# 4.5. Parameter analysis

In this section, we evaluated the influence of hyperparameters $C_1$ and $C_2$ in the optimization model on the results. This experiment is simulated at a 0.1 intensity in the maximum node degree-based node-attacking strategy. The parameter sensitivities of $C_1$ and $C_2$ are shown in Fig. 15. The restoration ratio equals the ratio of the restoration performance to the mission baseline, which is $y_r^k / y_b^k$ . The restoration ratio of UWSoS is the sum of the restoration ratios of $G_1$ , $G_2$ , and $G_3$ . 

Fig. 15 shows that the resilience value and restoration ratio vary with changes in hyperparameters. As the hyperparameter $C_1$ decreases, the resilience value decreases; however, the restoration ratio increases. Until $C_1$ dropped below 0.5, the restoration ratio was relatively stable. This indicates that adjusting the proportion of $C_1$ and $C_2$ could influence the performance of the total resilience and restoration ratio in the optimization model. We could set it according to the focus of attention and the actual battlefield situation. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/87acb667-9043-46e3-8250-2258c1ab4efe/60625fbb76a8c9f8ddbfe48991a43548c1ff6ccdb2be7d9324732f744da6234f.jpg)



Fig. 15. Parameter sensitivity analysis of $C_1$ and $C_2$ .


# 5. Conclusions

UWSoS, a novel type of modern weapon system-of-systems, is becoming increasingly intelligent and complex, potentially making it highly vulnerable. Therefore, designing a resilient UwSoS is a challenging task for architects. In this study, we have studied the reconfiguration model for UwSoS to enhance resilience, that is, to maximize the resilience in the attack-recovery process. The main conclusions are summarized as follows: (i) The proposed multi-swarm-based cooperative reconfiguration model can effectively restore the performance of UwSoS in different attack modes and attack intensities to enhance resilience. Meanwhile, the experiments indicate that the method has better adaptability than the others. (ii) The presented extended mission-oriented resilience metrics $\mathcal{R}_{CF}$ can more effectively reflect the resilience of mission-oriented UwSoS, which can capture the changeable mission baseline, restoration time, and mission completion. (iii) The proposed cooperative factor-based resilience optimization objective can further describe the redundant performance, and it is verified through experiments that it is affected by the hyperparameters $C_1$ and $C_2$ . 

In the future, we will further focus on the geographic distance, time cost, and energy cost of the cooperative reconfiguration model. In addition, it would be extended to allow the assignment of more than one available entity to simultaneously replace the critical disrupted entities to restore the performance at an earlier time. Finally, heuristics or artificial intelligence methods can be applied to solve the model in a short computational time. 

# CRediT authorship contribution statement

Qin Sun: Conceptualization, Methodology, Software, Writing - original draft, Visualization. Hongxu Li: Validation, Writing - review & editing. Yuzhi Wang: Visualization. Yingchao Zhang: Supervision, Funding acquisition. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgments

This research was supported by the Ph.D. Intelligent Innovation Foundation Project, PR China (No. 201-CXCY-A01-08-19-01), the Science and Technology on Information System Engineering Laboratory, PR China (No. 05202007). 

# References



[1] Uday P, Chandrahasa R, Marais K. System importance measures: definitions and application to system-of-systems analysis. Reliab Eng Syst Saf 2019;191:106582. 





[2] Li R, He M, He H, Wang Z, Yang C. A branch and price algorithm for the robust WSoS scheduling problem. J Syst Eng Electron 2021;32(3):658-67. 





[3] Sun Y, Fang Z. Research on projection gray target model based on FANP-QFD for weapon system of systems capability evaluation. IEEE Syst J 2021;15(3):4126-36. 





[4] Clark B, Patt D, Schramm H. Mosaic warfare: exploiting artificial intelligence and autonomous systems to implement decision-centric operations. Techreport, Washington D.C.: Center for Strategic and Budgetary Assessments; 2020. 





[5] Zhang T, Song A, Lan Y. Adaptive structure modeling and prediction for swarm unmanned system. Sci Sin Inform 2020;50(3):347-62. 





[6] Wang W, Li X, Yang S, Huang M, Wang T, Duan T. A design method of dynamic adaption mechanism for intelligent multi-unmanned-cluster combat system-of-systems. Syst Eng - Theory Pract 2021;41(5):1096-106. 





[7] Zhu X, Zhu X, Yan R, Peng R. Optimal routing, aborting and hitting strategies of UAVs executing hitting the targets considering the defense range of targets. Reliab Eng Syst Saf 2021;215:107811. 





[8] Madni AM, Sievers M, Erwin D. Formal and probabilistic modeling in design of resilient systems and system-of-systems. In: AIAA scitech 2019 forum. San Diego, California: AIAA SciTech Forum; 2019, p. 0223. 





[9] Li X, Li Y, Huang H. Redundancy allocation problem of phased-mission system with non-exponential components and mixed redundancy strategy. Reliab Eng Syst Saf 2020;199:106903. 





[10] Levitin G, Xing L, Xiang Y. Optimizing preventive replacement schedule in standby systems with time consuming task transfers. Reliab Eng Syst Saf 2021;205:107227. 





[11] Li J, Zhao D, Jiang J, Yang K, Chen Y. Capability oriented equipment contribution analysis in temporal combat networks. IEEE Trans Syst, Man, Cybern: Syst 2021;51(2):696-704. 





[12] Ordoukhanian E, Madni AM. Model-based approach to engineering resilience in multi-UAV systems. Systems 2019;7(11):1-19. 





[13] Iannacone L, Sharma N, Tabandeh A, Gardoni P. Modeling time-varying reliability and resilience of deteriorating infrastructure. Reliab Eng Syst Saf 2022;217:108074. 





[14] Poulin C, Kane MB. Infrastructure resilience curves: performance measures and summary metrics. Reliab Eng Syst Saf 2021;216:107926. 





[15] Liu W, Song Z. Review of studies on the resilience of urban critical infrastructure networks. Reliab Eng Syst Saf 2020;193:106617. 





[16] Barker K, Lambert JH, Zobel CW, Tapia AH, Ramirez-Marquez JE, Albert L, et al. Defining resilience analytics for interdependent cyber-physical-social networks. Sustain Resil Infrastruct 2017;2(2):59-67. 





[17] Almoghathawi Y, González AD, Barker K. Exploring recovery strategies for optimal interdependent infrastructure network resilience. Netw Spat Econ 2021;22(1):229-60. 





[18] Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Syst 1973;4(1):1-23. 





[19] Varajao J, Fernandes G, Amaral A, Gonçalves AM. Team resilience model: an empirical examination of information systems projects. Reliab Eng Syst Saf 2021;206:107303. 





[20] Sweya LN, Wilkinson S, Kassenga G. A social resilience measurement tool for Tanzania's water supply systems. Int J Disaster Risk Reduct 2021;65:102558. 





[21] Eldosouky A, Saad W, Mandayam N. Resilient critical infrastructure: bayesian network analysis and contract based optimization. Reliab Eng Syst Saf 2021;205:107243. 





[22] Liu X, Fang Y, Zio E. A hierarchical resilience enhancement framework for interdependent critical infrastructures. Reliab Eng Syst Saf 2021;215:107868. 





[23] Chen Z, Zhao T, Jiao J, Chu J. Performance-threshold-based resilience analysis of system of systems by considering dynamic reconfiguration. Proc Inst Mech Eng B 2020;00:1-11. http://dx.doi.org/10.1177/0954405420937528. 





[24] Mottahedi A, Sereshki F, Ataei M, Qarahaslanlou AN, Barabadi A. Resilience estimation of critical infrastructure systems: application of expert judgment. Reliab Eng Syst Saf 2021;215:107849. 





[25] Kammouha O, Gardoni P, Cimellaro GP. Probabilistic framework to evaluate the resilience of engineering systems using bayesian and dynamic bayesian networks. Reliab Eng Syst Saf 2020;198:106813. 





[26] Han L, Zhao X, Chen Z, Gong H, Hou B. Assessing resilience of urban lifeline networks to intentional attacks. Reliab Eng Syst Saf 2021;207:107346. 





[27] Dessavre DG, Ramirez-Marquez JE, Barker K. Multidimensional approach to complex system resilience analysis. Reliab Eng Syst Saf 2016;149:34-43. 





[28] Pan X, Wang H, Yang Y, Zhang G. Resilience based importance measure analysis for SoS. J Syst Eng Electron 2019;30(5):920-30. 





[29] Bruneau M, Chang SE, Eguchi RT, Lee GC, O'Rourke TD, Reinhorn AM, et al. A framework to quantitatively assess and enhance the seismic resilience of communities. Earthq Spectra 2003;19(4):733-52. 





[30] Tran HT, Balchanos M, Domercant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng Syst Saf 2017;158:73-84. 





[31] Bai G, Li Y, Fang Y, Zhang Y, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020;193:106602. 





[32] Liu T, Bai G, Tao J, Zhang Y, Fang Y. A mission-oriented resilience evaluation method for complex system. Syst Eng Electron 2021;43(4):1003-11. 





[33] Wu J, Wang P. Risk-averse optimization for resilience enhancement of complex engineering systems under uncertainties. Reliab Eng Syst Saf 2021;215:107836. 





[34] Wubben J, Fabra F, Calafate CT, Cano J-C, Manzoni P. A novel resilient and reconfigurable swarm management scheme. Comput Netw 2021;194:108119. 





[35] Shi Q, Li F, Olama M, Dong J, Xue Y, Starke M, et al. Network reconfiguration and distributed energy resource scheduling for improved distribution system resilience. Electr Power Energy Syst 2021;124:106355. 





[36] Feng Q, Hai X, Sun B, ren Y, Wang Z, Yang D, et al. Resilience optimization for multi-UAV formation reconfiguration via enhanced pigeon-inspired optimization. Chin J Aeronaut 2021. http://dx.doi.org/10.1016/j.cja.2020.10.029. 





[37] Tran HT, Domercant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Procedia Comput Sci 2016;95:126-33. 





[38] Zhang C, Chen R, Wang S, Dui H, Zhang Y. Resilience efficiency importance measure for the selection of a component maintenance strategy to improve system performance recovery. Reliab Eng Syst Saf 2022;217:108070. 





[39] Almoghathawi Y, Barker K, Albert LA. Resilience-driven restoration model for interdependent infrastructure networks. Reliab Eng Syst Saf 2019;185:12-23. 





[40] Sun Q, Li H, Wang Y, Zhou L, Zhang Y. Resilient UAV swarm modeling and solving based on multi-domain collaborative method. Acta Aeronaut Astronaut Sin 2021;25340, URL https://kns.cnki.net/kcms/detail/11.1929.V.20210619.0051.016.html. 





[41] Sun YZ, Han JW. Mining heterogeneous information networks: a structural analysis approach. ACM SIGKDD Explor Newsl 2013;14(2):20-8. 





[42] Chen W, Li J, Jiang J. Heterogeneous combat network link prediction based on representation learning. IEEE Syst J 2021;15(3):4069-77. 





[43] Sun YZ, Han JW, Yan XF, Yu PS, Wu TY. PathSim: meta path-based Top-K similarity search in heterogeneous information networks. Proc Vldb Endow 2011;4(11):992-1003. 





[44] Cares JR. An information age combat model. Tech. rep., USA: United States Office of the Secretary of Defense; 2004. 





[45] Tan Y, Zhang X, Yang K. Research on networked description and modeling methods of armament system-of-systems. J Syst Manag 2012;21(6):781-6. 





[46] Zhao D, Tan Y, Li J, Dou Y, Li L, Liu J. Research on structural robustness of weapon system-of-systems based on heterogeneous network. Syst Eng - Theory Pract 2019;39(12):3197-207. 





[47] Li J, Jiang J, Yang K, Chen Y. Research on functional robustness of heterogeneous combat networks. IEEE Syst J 2019;13(2):1487-95. 





[48] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35-53. 





[49] Li J, Tan Y, Yang K, Zhang X, Ge B. Structural robustness of combat networks of weapon system-of-systems based on the operation loop. Internat J Systems Sci 2017;48(3):659-74. 

