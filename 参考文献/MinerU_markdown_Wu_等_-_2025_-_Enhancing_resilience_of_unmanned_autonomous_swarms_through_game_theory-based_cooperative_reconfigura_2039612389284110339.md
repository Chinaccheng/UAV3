# Enhancing resilience of unmanned autonomous swarms through game theory-based cooperative reconfiguration

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/b950a75343c3dba4b0a9a0f2706a2eabbff1c5407e6f7fca7edb9e7d4a9f913b.jpg)


Chengxing Wu a, Hongzhong Deng a,∗, Hongqian Wu a, Chengyi Tu b 

a College of Systems Engineering, National University of Defense Technology, Changsha 410073, China 

b School of Economics and Management, Zhejiang Sci-Tech University, Hangzhou 310000, China 

# A R T I C L E I N F O

Keywords: 

Unmanned autonomous swarm 

Resilience 

Cooperation strategy 

Reconfiguration 

Evolutionary game 

# A B S T R A C T

The resilience of unmanned autonomous swarms (UAS) is critical for their ability to adjust behaviors and maintain essential functions when errors and failures occur. While significant advancements have been made in enhancing UAS resilience, the potential to utilize their inherent self-organizing and self-restructuring capabilities for further improvement remains largely underexplored. In this study, we present a game theorybased reconfiguration framework for UAS, enabling dynamic adjustments to the swarm’s network structure through cooperative payoffs. Building on this framework, we propose a UAS resilience metric to quantify the swarm’s task performance under continuous disturbances, validated through a case study. Finally, our analysis of the optimal configurations for enhancing UAS resilience—considering payoff matrices, swarm composition, communication range, and network structure—provides actionable insights for UAS design. We find that an optimal agent configuration ratio exists that maximizes UAS resilience, with specific constraints established for this ratio. Additionally, while increasing the communication range improves resilience, the benefits diminish beyond a certain threshold. We also find that network topology significantly impacts UAS resilience, particularly in structures with short global paths, which exhibit greater resilience. 

# 1. Introduction

Unmanned autonomous swarms (UAS) are complex networkphysical systems characterized by the operation of homogeneous or heterogeneous agents through self-organizing and self-restructuring behavior strategies [1–3]. These agents interact and cooperate with each other to avoid task conflicts and resource competition, significantly enhancing overall task execution efficiency [4,5]. This collaborative advantage has been applied across various domains, including automated warehouse robotics coordination [6], autonomous vehicle management in intelligent transportation systems [7], and drone swarms conducting exploration missions in complex environments [8]. 

Resilience is a core capability in the design and operation of UAS, ensuring the system can maintain functionality during disruptions [9, 10]. UAS typically operate in dynamic and unpredictable environments, making them vulnerable to disturbances such as equipment failures, communication interruptions, and targeted attacks [11–13]. When an agent fails, its connections with other agents may be severed. However, due to the self-organizing and self-restructuring abilities of UAS, the remaining agents can quickly re-establish connections, allowing the system to recover performance and continue mission objectives [14– 

16]. In such scenarios, resilience enables UAS to recover from disturbances and maintain their expected performance, making it essential for enhancing their ability to withstand uncertain threats and recover from disruptive events. Therefore, employing resilience as a measure to evaluate UAS capabilities is vital to ensure their reliable operation. 

Since Holling introduced the concept of resilience [17], it has been widely applied across various fields, from ecosystems [18] and supply chain networks [19] to transportation systems [20] and power grids [21]. With the increasing prevalence of autonomous robots, vehicles, and drones, the resilience of UAS has garnered significant attention [22–24]. Early studies, such as those by Tran et al. [25], proposed resilience evaluation methods for drone swarms based on performance differences between current and previous stable states [26]. Saulnier et al. [9] developed a resilient flocking framework for mobile robot teams, enabling them to achieve a resilient consensus on movement direction. These pioneering works have provided foundational insights into evaluating UAS resilience. 

Further efforts have focused on enhancing UAS resilience. Wubben et al. [27] proposed a resilient and reconfigurable swarm management scheme to address challenges related to swarm layout reconfiguration and the management of swarm element loss. Feng et al. [28] 

investigated the resilience of drone swarm formations under random attacks, introducing a reconfiguration method to address stochastic disturbances. Some studies systematically analyzed the factors influencing UAS resilience. For example, Zhang et al. [24] examined the impact of different topologies and parameters on swarm resilience, revealing that attack intensity and topology significantly affect swarm performance. 

While these groundbreaking studies effectively considered the impact of system topology and failure mechanisms on UAS resilience, they often overlook the necessity of maintaining the minimum performance required to complete missions during disruptions, which is crucial for ensuring UAS achieve their designated tasks. To address this, some studies proposed mission-oriented resilience evaluation frameworks. For instance, Cheng et al. [29] developed a joint reconnaissance mission model for drone swarms using complex networks and agent-based models to evaluate resilience. Bai et al. [30] incorporated the impact of limited communication ranges into resilience evaluation, proposing a mission-oriented resilience evaluation model for UAS. However, these studies still lack clearly defined mission baselines. Later works, such as Sun et al. [31], proposed a multi-swarm cooperative reconfiguration model for resilient unmanned weapon systems, combining variable mission baselines and recovery time, and Li et al. [32] introduced a baseline resilience evaluation method for heterogeneous swarms, effectively characterizing swarm resilience through mission completion metrics. These studies have significantly advanced our understanding of UAS resilience. 

Despite these advances, most studies have not fully considered the UAS’s ability to dynamically adjust structure in response to disruptions. While recent efforts, such as Li et al.’s soft resource optimization model [33], have improved resilience through task reallocation, they overlook the need for dynamic system reconfiguration. Additionally, some researchers have attempted to enhance resilience by dynamically supplementing and replacing agents after disturbances. For instance, Zhang et al. [34] introduced a cross-domain cooperation resilience evaluation method in adversarial scenarios, and Kong et al. [35] analyzed the impact of resource supplementation on swarm resilience using multidimensional topological features. However, these approaches rely on additional resources or agents, which are often unavailable in many scenarios. Therefore, leveraging the self-organizing and selfrestructuring dynamic characteristics of UAS to enhance their resilience remains a challenging issue. 

To address these limitations, this study proposes an evolutionary game theory-based cooperative payoff mechanism, establishing a foundational framework for adaptive dynamic reconfiguration of UAS. Within this framework, agents interact with neighbors under conditions of bounded rationality and asymmetric information, achieving global responses through local information exchange. The proposed model not only enhances UAS resilience but also provides theoretical support and practical strategies for future swarm operations and performance improvement. The main contributions are as follows: 

(i) A framework for self-organizing cooperative reconfiguration in UAS is proposed, utilizing evolutionary game theory to allow agents to autonomously select partners with the highest cooperative payoff, thereby achieving evolutionary stability. 

(ii) We introduce a resilience metric for UAS that incorporates mission tasks, resilience losses, and continuous disturbances, providing a comprehensive evaluation of resilience. This metric also considers the impact of partner interactions on individual agent performance. 

(iii) To validate the effectiveness of the proposed UAS resilience metric, a case study is conducted and compared with various baseline methods. The results demonstrate the reliability and superiority of the proposed metric in evaluating UAS resilience. 

(iv) Through analytical calculations and numerical simulations, the effects of payoff matrices, communication range, swarm composition, and network structure on UAS resilience are investigated. 

The findings reveal optimal configurations for enhancing UAS resilience, providing valuable theoretical support for the design of resilient UAS swarms. 

The remainder of this paper is organized as follows. Section 2 introduces our evolutionary game-based cooperation framework for UAS. In Section 3, we propose a resilience metric for UAS. Section 4 presents a case study demonstrating the feasibility and effectiveness of the proposed resilience metric. Section 5 explores resilience enhancement strategies for UAS from the perspectives of agent composition, communication range, payoff distribution, and network structure. Finally, Section 6 discusses the conclusions and outlines potential future work. 

# 2. Description of game theory-based UAS

# 2.1. Network model of UAS

UAS consist of agents with various capabilities that interact and cooperate with each other to address complex real-world applications, such as drone swarms and robotic collectives. Due to their self-organizing and self-restructuring capabilities, UAS can dynamically adjust their structure and interactions in response to disturbances, enabling them to adapt to complex and ever-changing scenarios. Consequently, the structure of UAS is inherently dynamic. 

At any point in time, the UAS structure can be described by a network comprising a finite number of agents, each participating in pairwise interactions to form a connected graph. Throughout the execution of UAS tasks, this network structure evolves over time and can be represented by one of $L$ possible network configurations at each discrete time point. For a network $\beta \in \{ 1 , \ldots , L \}$ , let $A _ { i j } ^ { \beta }$ denote the communication link between agent ?? and agent $j$ . A link exists if two agents are within each other’s communication range and engage in cooperate. We assume that all networks are undirected, meaning that for all $i , j \in \{ 1 , \ldots , N \}$ and $\beta \in \{ 1 , \ldots , L \}$ , $A _ { i j } ^ { \beta } = A _ { j i } ^ { \beta }$ . 

# 2.2. Cooperative reconfiguration processes of UAS using evolutionary game theory

In UAS, agents can be categorized into different autonomous entities based on their functions, such as sensing, decision-making, commanding, and execution [36,37]. These agents dynamically adjust their interaction partners to maintain effective collaboration in response to environmental changes. Evolutionary game theory (EGT) provides a powerful framework for modeling such adaptive processes by focusing on the interplay between participants, their strategies, and the resulting payoffs. Below, we outline the theoretical foundation of EGT and its application to the cooperative reconfiguration process in UAS. 

# 2.2.1. Evolutionary game theory

EGT extends classical game theory by introducing dynamic processes in which strategies evolve over time in response to payoffs. In this framework, agents iteratively refine their strategies based on interaction outcomes, with payoffs serving as feedback mechanisms. Successful strategies are reinforced, while ineffective ones are weakened, enabling agents to progressively optimize their behavior. This inherent adaptability makes EGT particularly effective for multi-agent systems like UAS, where agents operate in decentralized environments, relying on local interactions and limited global information to collectively achieve system-wide objectives through iterative strategy updates. 

The implementation of EGT in UAS reconfiguration is motivated by three key factors: dynamic adaptability, distributed decision-making, and optimization strategy evolution. UAS often operate in dynamic environments where disturbances such as agent loss or communication interruptions occur. EGT enables agents to continuously adjust their strategies in response to these changes, ensuring sustained system performance. Moreover, EGT provides a decentralized decision-making 

framework, allowing agents to optimize behavior based on local payoffs without relying on centralized control. Finally, EGT strengthens successful strategies and eliminates inefficient ones, promoting dynamic optimization of system performance based on task requirements and environmental conditions. These features make EGT a flexible and robust solution to address the challenges of real-world UAS applications. 

# 2.2.2. Cooperative reconfiguration in UAS

The cooperative reconfiguration process in UAS can be modeled as an evolutionary game, where agents adopt either cooperative or non-cooperative strategies and select neighbors within their communication range for interactions. Cooperative strategies promote mutual benefit, while non-cooperative strategies reflect self-serving behaviors. The network structure represents these strategies, with edges denoting cooperative interactions and the absence of edges indicating non-cooperation. Mutual cooperation between agents yields benefits, whereas non-cooperation results in no gains. Agents then iteratively refine their strategies based on the payoffs from these interactions, akin to selecting interaction partners that maximize their payoffs. 

We consider a UAS system comprising two primary types of agents: sensor entities $( S )$ and decision-maker entities $( D )$ . This dual-agent framework reflects many real-world UAS applications, such as reconnaissance and strike systems [38], and air-ground cooperative systems where drones act as sensors to collect data for ground vehicles performing tasks [39]. The payoff structure for cooperative strategies is represented by the following matrix, where each element corresponds to the payoff received based on the interaction type: 

$$
\begin{array}{c c} & S \quad D \\ S & \left( \begin{array}{c c} a & b \\ c & d \end{array} \right). \end{array}
$$

where ?? represents the payoff when two sensor entities cooperate, $b$ is the payoff for a sensor entity cooperating with a decision-maker entity, $c$ is the payoff for a decision-maker entity cooperating with a sensor entity, and $d$ represents the payoff when two decision-maker entities cooperate. Effective task execution relies on seamless collaboration between these two types of agents. By adjusting the parameters of the payoff matrix, the interaction strategies of agents can be effectively controlled. 

# 2.2.3. Evolutionary dynamics and strategy updates

Building on this foundation, we introduce evolutionary dynamics to simulate how agents iteratively adjust their strategies and connections to maximize their payoffs. These evolutionary dynamics are modeled within a network structure, where agents are positioned at the vertices and edges represent potential cooperative interactions. Typically, agents select multiple interaction partners. At each time step, the total payoff for the ??th sensor entity and decision-maker entity are given by: 

$$
\pi_ {i} ^ {S} = \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(a x _ {S} + b x _ {D}\right), \tag {1}
$$

$$
\pi_ {i} ^ {D} = \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(c x _ {S} + d x _ {D}\right), \tag {2}
$$

where $\pi _ { i } ^ { S }$ and $\pi _ { i } ^ { D }$ denote the total payoffs for the ??th sensor and decision-maker entities, respectively. The adjacency matrix $A _ { i j } ^ { \beta }$ encodes the interaction structure among agents in network $\beta$ . The variables $x _ { S }$ and $x _ { D }$ are binary indicators that describe the type of neighbor $j$ : if $j$ is a sensor entity, $x _ { S } = 1$ and $x _ { D } = 0$ ; otherwise, $x _ { S } = 0$ and $x _ { D } = 1$ . These variables ensure that the payoffs received by agent ?? are determined by both the interaction structure (via $A _ { i j } ^ { \beta } )$ and the types of neighboring agents (via $x _ { S }$ and $x _ { D . }$ ). 

Agents periodically reassess their network connections and strategies. This process follows an update rule: at each time step, agents evaluate whether they have reached an Evolutionary Stable State (ESS). 

If an agent has not achieved ESS, it updates its strategy by adjusting its interaction partners. Subsequently, all neighboring agents re-evaluate their ESS status based on these updates. When all agents achieve ESS, the system structure stabilizes, representing an optimal configuration for cooperative reconfiguration. The definition of ESS is as follows: 

Definition 2.1 (Evolutionarily Stable State [40,41]). A strategy $u \in V$ used by an agent is evolutionarily stable if, for all $v \in V$ with $v \neq u$ , we have 

$$
E (u, u) > E (v, u)
$$

where $V$ is the set of strategies and $E ( v , u )$ is the payoff function when using strategy $v$ against strategy ??. 

Through this modeling approach, we provide a comprehensive framework for understanding and optimizing cooperative reconfiguration processes in UAS systems using EGT. 

# 2.3. Evolution steps and simulation example of game-based UAS

In this section, we summarize the evolutionary steps of cooperative reconfiguration in UAS based on the previous discussions and illustrate these steps with a simulation example. 

# 2.3.1. Evolution steps for UAS cooperative reconfiguration

The network structure of UAS evolves through an initial construction phase, followed by a repair phase in response to disturbances. The initial evolution of the UAS network structure can be summarized in the following steps: 

Step 1: Network initialization and modeling. Set the initial constraints, including the number and types of agents, their interaction payoff matrix, and the optimal number of communication links per agent. Based on these parameters, each agent selects initial interaction partners within its communication range, prioritizing proximity. This step forms the initial network structure. 

Step 2: ESS status evaluation. Each agent calculates its payoffs from interactions using Eqs. (1) and (2). Agents then evaluate whether their current strategy has reached an ESS by comparing their payoffs to those achievable through alternative strategies. Agents that have not achieved ESS identify potential new partners that could improve their payoffs. 

Step 3: Strategy update. Agents that are not at ESS adjust their interaction strategies based on local information. Each agent follows a distributed decision-making process using the update rule introduced in Section 2.2.3: The agent gathers payoff data from current neighbors and evaluates potential new partners within its communication range; then based on the collected data, the agent calculates the expected payoff for each potential interaction and selects the partner that maximizes its payoff, considering the constraints of the payoff matrix. The agent replaces its least productive partner with the newly selected partner. 

Step 4: Network reevaluation. After each strategy update, all neighboring agents reassess their ESS status using only local information. If an agent’s status changes (e.g., it no longer achieves ESS due to a neighbor’s update), it initiates its own strategy adjustment using the same local decision-making process. This distributed feedback mechanism enables cascading updates across the network, guiding the system toward a stable and optimal configuration. 

Step 5: Convergence to a stable structure. Steps 2 to 4 are repeated until all agents achieve ESS, resulting in a stable network structure that optimizes cooperation among agents. In this state, the UAS achieves an optimized network configuration, maximizing cooperation efficiency and enhancing overall system performance. 

Through the iterative process outlined in Steps 1 to 5, the UAS progressively refines its network structure and improves coordination among agents. This process enhances the system’s resilience by dynamically restructuring the network in response to disruptions or environmental changes. As a result, the UAS maintains effective operation 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/b80ad0d675b198d28d05694eec26a3050ac1d21bb6674861b7a0428aa7c59623.jpg)



(a) Step 1: network initialization and modeling


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/0c2fa4411571f300159ea232fafc3908ed9c79f0aeb43f0157e5d54b6fa8c639.jpg)



(b) Step 5: convergence to a stable structure


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/0272573f3f5c43a1e2607626b6bef547c504bd214a8a64098ac297bf207c4a2b.jpg)



(c) cooperative reconfiguration after disturbance



Fig. 1. Illustrative example of the evolution process of game-based cooperative reconfiguration in UAS.


and adapts to adverse conditions, ensuring reliable performance even in challenging environments. When disturbances occur, the UAS network follows Steps 2 to 5 to repair and restore its structure. 

# 2.3.2. Illustrative simulation for UAS cooperation

To illustrate the evolutionary steps, we present a simulation example showcasing cooperative reconfiguration in a UAS. The simulation consider a UAS comprising 12 agents, including 6 sensing entities $( S )$ and 6 decider entities $( D )$ . Each agent adopts a strategy of either cooperation or non-cooperation with agents within its communication range, aiming to maximize its payoff. Each agent can form cooperative relationships with up to three neighbors, while non-cooperation yields no payoff. The payoff structure for cooperation is defined by the following matrix: 

$$
\begin{array}{c c} & S \quad D \\ S & \left( \begin{array}{c c} 0 & 0. 5 \\ 0. 5 & 0. 1 \end{array} \right). \end{array}
$$

The simulation results are shown in Fig. 1. At time step 1, agents construct an initial network by connecting to their nearest partners, as shown in Fig. 1(a). In this network, edges represent cooperative relationships, while the absence of edges indicates non-cooperation. At subsequent time steps, agents calculate their payoffs using Eqs. (1) and (2) from Section 2.2.3 and evaluate whether to adjust their strategies. Agents replace low-payoff partners with higher-payoff ones within their communication range. For instance, an $S$ agent connected to another $S$ agent receives a payoff of 0. If a nearby $D$ agent is available, the $S$ agent switches partners to secure a payoff of 0.5. Over time, agents iteratively adjust their connections and strategies until achieving an ESS, where no agent can improve its payoff by unilaterally changing its strategy. Fig. 1(b) illustrates the optimized network configuration after convergence. In this state, all agents have adopted ESS. For instance, an $S$ agent may establish cooperative relationships with three $D$ agents to maximize its payoff. 

When disruptions occur, such as agents failure, the remaining agents adapt by recalculating their payoffs and revising their connections using the same payoff-driven strategy. This reconfiguration process ensures that the system maintains functionality. Fig. 1(c) shows the network after reconfiguration, demonstrating the system’s resilience and adaptability under dynamic conditions. 

This simulation highlights how agents, guided by EGT, dynamically adjust their strategies to achieve a resilient and optimized network structure. By embedding adaptive, payoff-driven strategies, the proposed approach enables agents to reach a stable state using only local information and distributed decision-making. Furthermore, the method demonstrates the UAS’s ability to effectively recover and reconfigure when faced with disruptions. 

# 3. Resilience evaluation of cooperative reconfiguration UAS

In this section, we propose a new framework for evaluating the resilience of UAS with cooperative reconfiguration capabilities. This 

framework integrates the system’s cooperative reconfiguration abilities with metrics such as resilience loss and task baseline to provide a comprehensive assessment of UAS performance in complex environments. The framework is designed to enhance our understanding of how UAS can effectively maintain mission objectives and adapt to disruptions through cooperative strategies. 

# 3.1. UAS performance model

To evaluate the resilience of a UAS, we develop a performance model that accounts for both the intrinsic capabilities of individual agents and the performance enhancements achieved through their interactions within the network. In a UAS with $N$ agents, the interaction structure at any given moment is represented by a bipartite matrix $A _ { i j } ^ { \beta }$ , which encodes the connections between agents in a specific network configuration $\beta$ . The performance of each agent ?? under a given network configuration $\beta$ is modeled as: 

$$
f _ {i} ^ {\beta} = s _ {i} + \pi_ {i} ^ {S} = s _ {i} + \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(a x _ {S} + b x _ {D}\right), \tag {3}
$$

$$
g _ {i} ^ {\beta} = d _ {i} + \pi_ {i} ^ {D} = d _ {i} + \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(c x _ {S} + d x _ {D}\right), \tag {4}
$$

where $f _ { i } ^ { \beta }$ and $g _ { i } ^ { \beta }$ denote the overall performance of the ??th sensor $( S )$ and decision-maker $( D )$ agents, respectively. $s _ { i }$ and $d _ { i }$ represent the inherent performance capabilities of the ??th agent within the $S$ and $D$ entities. The interaction-driven performance enhancements are captured by $\pi _ { i } ^ { S }$ and $\pi _ { i } ^ { D }$ , which quantify the total payoffs from cooperative interactions with neighbors $j$ under the network configuration $\beta$ . 

Eqs. (3) and (4) integrate the performance contributions of individual agents and the network structure, effectively modeling how interactions influence agent performance within the UAS. To assess the overall performance of the UAS, we propose the following system-level performance model: 

$$
Q (\beta) = \frac {N (S)}{N (\beta)} \sum_ {i = 1} ^ {N (S)} f _ {i} ^ {\beta} + \frac {N (D)}{N (\beta)} \sum_ {j = 1} ^ {N (D)} g _ {j} ^ {\beta} \tag {5}
$$

where $Q ( \beta )$ represents the overall capability of the system at the $\beta$ network structure, and $N ( S )$ and $N ( D )$ denote the numbers of $S$ and $D$ agents, respectively. Eq. (5) combines the inherent capabilities of individual agents with the enhancements gained from network interactions, providing a comprehensive assessment of how both individual performance and network dynamics contribute to the overall system effectiveness. 

# 3.2. Resilience metrics

# 3.2.1. Typical methods for resilience metrics

Resilience metrics are critical for analyzing the ability of UAS to maintain mission performance under disturbances. Various methods 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/97a57e1e0717d2ee4699db67b399b191c2aade3f619217d7903ccb0e8f0bcbd9.jpg)



Fig. 2. Schematic diagram of resilience under a single disturbance, as quantified by Bruneau et al. [42].


have been proposed to evaluate and enhance system resilience. A widely recognized approach is the ‘‘resilience triangle’’, introduced by Bruneau et al. [42], which measures resilience by examining performance loss and recovery over time. As depicted in Fig. 2, a disturbance occurs at time $t _ { 0 }$ , causing system performance to decline; subsequently, the system enters a recovery phase until full restoration at time $t _ { 1 }$ . The area of the triangle formed during this process quantifies the overall impact of post-event performance loss. Bruneau et al. quantified resilience loss during a single event using the integral of the performance loss function [42]: 

$$
R _ {1} = \int_ {t _ {0}} ^ {t _ {1}} (1 - Q (t)) d t \tag {6}
$$

where $Q ( t )$ represents the system’s performance status, $t _ { 0 }$ is the start of the performance decline, and $t _ { 1 }$ marks the recovery to normalcy. While this method was initially developed for seismic contexts, it has been widely applied to various systems under different disturbances. However, this approach does not account for the task baseline and the system’s ability to withstand continuous disturbances, limiting its suitability for evaluating UAS resilience. 

To address these limitations, T. Liu, G. Bai et al. [43,44] proposed a dynamic resilience model specifically tailored for cross-domain swarms, demonstrating notable advantages, considering both time and performance resilience. However, our study focuses solely on performance resilience. As shown in Fig. 3, consider the mission time from $t _ { 0 }$ to ??, where the system’s performance $Q ( t )$ changes continuously. ??baseline describes the minimum performance required for the current mission, and $Q _ { \mathrm { o p t } }$ represents the ideal (or expected) performance of the system. The performance resilience metric is defined as [43,44]: 

$$
R _ {2} = \frac {\int_ {t _ {0}} ^ {t} Q (t) [ Q (t) - Q _ {\text {b a s e l i n e}} \geq 0 ] d t}{\int_ {t _ {0}} ^ {t} Q _ {\text {o p t}} (t) d t} \tag {7}
$$

where $R _ { 2 }$ is the performance resilience measure for systems, and $[ Q ( t ) -$ $Q _ { \mathrm { b a s e l i n e } } ~ \geq ~ 0 ]$ is the Iverson bracket. Only when $Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \ \geq \ 0 ,$ , $[ Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \geq 0 ] = 1 _ { : }$ , otherwise $[ Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \geq 0 ] = 0$ . 

This metric, proposed by T. Liu, G. Bai et al. [43,44], considers performance variations across multiple stages and the system’s ability to absorb disruptions and complete tasks. While this method provides detailed insights into UAS performance, it overlooks ‘‘resilience loss’’, and may yield counterintuitive results. For instance, when comparing systems with identical performance curves but differing baseline requirements, the method tends to evaluate systems with higher baselines as more resilient. A detailed case analysis highlighting this issue is provided in Section 4.3. However, in practice, a system with higher baselines are less likely to sustain performance under disruptions due to stricter minimum requirements. This inconsistency highlights the need for a more comprehensive resilience metric that aligns with practical expectations and accounts for mission-specific baseline thresholds. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/814f886f825f481e8f877fb2ec20abcc506a2890a94edbec3bbe761df7790682.jpg)



Fig. 3. The typical resilience process of a UAS.


# 3.2.2. Resilience metric for UAS systems with cooperative reconfiguration

To address the limitations of existing metrics, we integrate the work of Bruneau et al. [42] and T. Liu, G. Bai et al. [43,44] to propose a novel resilience metric tailored for UAS with collaborative reconfiguration capability. The proposed metric is defines as: 

$$
R = \frac {t \int_ {t _ {0}} ^ {t} (N (t _ {0}) Q (t _ {0}) - N (t) Q (t)) [ Q (t) - Q _ {\text {b a s e l i n e}} \geq 0 ] d t}{\sqrt {Q _ {\text {b a s e l i n e}} + t ^ {2}} \int_ {t _ {0}} ^ {t} N (t _ {0}) Q (t _ {0}) d t} \tag {8}
$$

where $N ( t _ { 0 } )$ is the initial number of agents in the UAS, $N ( t )$ represents the number of agents remaining after the disturbance, $Q _ { \mathrm { b a s e l i n e } }$ denotes the minimum performance threshold necessary for task completion, and $Q ( t _ { 0 } )$ represents the optimal performance of the UAS at the initial time. The expression $[ Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \geq 0 ]$ ] equals 1 if $Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \geq 0$ , and 0 otherwise. 

This metric integrates three critical components to comprehensively evaluate UAS resilience: 

(1) Mission sustainability: Building on the work of T. Liu, G. Bai, et al. this component evaluates the system’s ability to maintain performance above the predefined task baseline, retaining the form $[ Q ( t ) - Q _ { \mathrm { b a s e l i n e } } \geq 0 ]$ to ensure mission success. 

(2) Performance contributions from agents: The term $\frac { \int _ { t _ { 0 } } ^ { t } N ( t _ { 0 } ) Q ( t _ { 0 } ) - N ( t ) Q ( t ) d t } { \int _ { t _ { 0 } } ^ { t } N ( t _ { 0 } ) Q ( t _ { 0 } ) d t }$ captures the impact of performance losses 0due to agent attrition under continuous disruptions and the recovery of system performance through cooperative reconfiguration. This provides a holistic view of resilience by integrating the effects of performance degradation and recovery. 

(3) Performance decline dynamics: This component evaluates the rate of performance decline from $t _ { 0 }$ to ??, highlighting the system’s adaptability to external disruptions. The decline rate is approximated as $\frac { t } { \sqrt { \left[ Q ( t _ { 0 } ) - Q _ { \mathrm { b a s e l i n e } } \right] ^ { 2 } + t ^ { 2 } } }$ , which is further simplified for practical applications to $\frac { t } { \sqrt { Q _ { \mathrm { b a s e l i n e } ^ { + t ^ { 2 } } } } }$ This approximation provides an intuitive representation of decline dynamics while preserving essential system characteristics. 

By integrating these elements, the proposed metric ensures a comprehensive and interpretable assessment of UAS resilience under continuous disruptions. 

Eq. (8) defines the foundational formula for UAS resilience measurement, where $R \in [ 0 , 1 )$ indicates the range of resilience. A higher ?? value signifies stronger resilience. This metric uniquely combines agent quantity, performance loss, baseline performance, and the impact of continuous disturbances, offering a more accurate and comprehensive evaluation of UAS resilience, particularly for systems with collaborative reconfiguration capabilities. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/3e0bbb845f1469fcdbbb1a966e949277364f3d74b8a76b1d6da5ac3bb5f8abbc.jpg)



Fig. 4. Network structure of the UAS system with 40 drones employed for resilience analysis in the case study.


# 4. Case analysis

In this section, we validate the feasibility and effectiveness of the proposed resilience metric for cooperative reconfiguration in UAS through a case study. The analysis demonstrates that the proposed resilience metrics accurately reflect the system’s resilience under various disturbances and provide a comparative assessment against existing resilience metrics. 

# 4.1. Case description

We constructed a representative drone swarm system based on mission scenarios and requirements. The system consists of two types of drones: sensor drones $( S )$ and decider drones $( D )$ . Sensor drones detect targets and relay relevant information to decider drones, which execute corresponding tasks through information exchange. 

In this study, each drone’s initial performance capability is set at 0.1 $( d _ { i } = s _ { i } = 0 . 1 )$ . The swarm system comprises 40 drones, with 20 serving as decider drones and 20 as sensor drones. The minimum performance requirement for the mission is set at 10 $( Q _ { \mathrm { b a s e l i n e } } = 1 0 )$ . The cooperative payoff matrix is defined as follows: 

$$
\begin{array}{c c} & S \quad D \\ S & \left( \begin{array}{c c} 0 & 0. 5 \\ 0. 5 & 0. 1 \end{array} \right). \end{array}
$$

Using these parameters, we randomly generated a network structure of 40 drones on a plane coordinate system of size $5 0 \times 5 0$ units. Drones are spaced at least 5 units apart, with a maximum of 3 communication links per drone within a communication range of 30 units. The resulting swarm network structure, generated using the evolutionary algorithm, is illustrated in Fig. 4. 

During the mission, the drone swarm faces two primary challenges: (1) Drones may experience random failures that disrupt their communication with other drones, and (2) these failures destabilize the swarm’s ESS, triggering self-organizing reconfiguration processes to restore effective information exchange and maintain mission performance. 

# 4.2. Resilience analysis

Based on the swarm system described in Section 4.1, we conducted a resilience analysis to evaluate the system’s ability to maintain performance under disturbances. The performance states of individual drones within the swarm were calculated using Eqs. (3) and (4), and the overall system performance was determined by aggregating these states using Eq. (5): 

$$
\begin{array}{l} Q (t _ {0}) = Q (\beta) = \frac {N (S)}{N (\beta)} \sum_ {i = 1} ^ {N (S)} f _ {i} ^ {\beta} + \frac {N (D)}{N (\beta)} \sum_ {j = 1} ^ {N (D)} g _ {j} ^ {\beta} \\ = \frac {N (S)}{N (\beta)} \sum_ {i = 1} ^ {N (S)} \left(s _ {i} + \pi_ {i} ^ {S}\right) + \frac {N (D)}{N (\beta)} \sum_ {j = 1} ^ {N (D)} \left(d _ {i} + \pi_ {i} ^ {D}\right) \\ = 2 9. 7 \tag {9} \\ \end{array}
$$

Next, we simulated random failures by removing drones during each disturbance event. Fig. 5 shows the performance variations of the swarm under these conditions. We conducted 100 simulation runs, with one run highlighted to illustrate a typical process. Initially, the system performs optimally, well above the minimum threshold required for mission success. However, as the number of active drones decreases, the system’s performance declines. The cooperative reconfiguration mechanism, based on the evolutionary game, enables the remaining drones to reorganize their communication structure. This adaptive adjustment enhances system performance and demonstrates resilience. The cycle of performance degradation and recovery continues until the system’s performance eventually falls below the mission threshold, resulting in a loss of resilience. In contrast, without cooperative reconfiguration, the system fails to recover, highlighting the significant advantage of cooperative reconfiguration in enhancing resilience. 

To further evaluate system resilience, we compared scenarios with and without cooperative reconfiguration, applying the proposed resilience measurement method. Using Eq. (8), we calculated resilience for each of the 100 simulation runs shown in Fig. 5. The results, presented in Fig. 6, indicate that the system with cooperative reconfiguration exhibits significantly higher resilience than the system without reconfiguration. This confirms that our resilience evaluation metrics accurately reflect that a higher resilience value ?? corresponds to enhanced system resilience. 

# 4.3. Comparison with other resilience metrics

To further validate the effectiveness and reliability of the proposed resilience metric for UAS, we conducted comparative experiments with other established resilience metrics, including those by T. Liu, G. Bai et al. [43,44], J. Liu, R. Xu et al. [45], and Li et al. [33]. These metrics were originally designed for different domains—T. Liu, G. Bai et al.’s metric for drone swarms and J. Liu, R. Xu et al.’s metric for combat systems—but share a common goal of evaluating system resilience under continuous disturbances while considering the performance baseline. This shared foundation makes them relevant benchmarks for assessing the applicability of resilience metrics to UAS. Additionally, we referred to the work of Li et al. [33], which proposed a resilience measurement method for unmanned aerial vehicle swarms under continuous attacks from the perspective of soft resource optimization. However, Li et al.’s metric does not incorporate the concept of a task performance baseline. In this study, the task baseline in Li et al.’s metric serves to determine the duration for which the system performance exceeds a predefined threshold $( Q _ { \mathrm { b a s e l i n e } } )$ , representing the task time. 

The primary objective of this comparison is to assess the applicability of these metrics for UAS resilience evaluation, highlighting their limitations and strengths in this context. By identifying these limitations, we aimed to underscore the necessity of developing tailored approaches for UAS resilience evaluation and to demonstrate the advantages of our proposed metric. Importantly, this comparison is not intended to discredit existing methods but rather to illustrate their adaptability to UAS scenarios. The insights gained from this analysis further support the reliability and applicability of our proposed metric, providing a strong foundation for subsequent resilience evaluation and analysis. 

Experiment Setup 1: Resilience under different task baseline performance levels. In this experiment, we evaluated the resilience of a drone swarm system performing tasks with two different baseline performances levels $( Q _ { \mathrm { b a s e l i n e } } = 6 $ and $Q _ { \mathrm { b a s e l i n e } } = 1 0 )$ . Generally, systems performing tasks with lower baseline performance requirements exhibit higher resilience, as maintaining necessary performance during disturbances is easier. 

Three disturbance intensities were defined by removing 4, 8, and 16 drones from the swarm at once. The results are shown in Table 1. It can be seen that T. Liu, G. Bai et al.’s metric [43,44] showed some limitations in capturing the expected relationship between resilience and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/18e9dd73aac3a52a67b08b75c75f7d5a7e8043e563f7f4cd40fc34bac6ecd08e.jpg)



(a) Disturbance is modeled by 4 drone removal


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/d82799f4f55bca8e914eb57983cd4319b3e8b50ae5a73ecece90e0abd09643af.jpg)



(b) Disturbance is modeled by 8 drone removal


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/a11d84c07cc3019a46a212cbea560a00197192dc9b101ccb70f110acc1f10c47.jpg)



(c) Disturbance is modeled by 16 drone removal



Fig. 5. Performance of the swarm system with and without cooperative reconfiguration under continuous disturbances.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/e98f2d86bd8f2a3e0cb888aa8244e8c0dc525208e659a350a49c368098cfe594.jpg)



(a) Disturbance is modeled by 4 drone removal


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/a080dacf65f06eff661cd59c63d0276a63a32972130d0d79a85fc2e2edce8aec.jpg)



(b) Disturbance is modeled by 8 drone removal


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/523d0d74b4b7c2efaa1358d1503a753a2dce271222a5dff214ac26b3281574fd.jpg)



(c) Disturbance is modeled by 16 drone removal



Fig. 6. Resilience of the swarm system with and without cooperative reconfiguration under continuous disturbances.



Table 1 Comparison of resilience metrics under different baseline performance levels $( Q _ { \mathrm { h a s e l i n e } } = 6$ and $Q _ { \mathrm { h a s e l i n e } } = 1 0 ) ^ { \mathrm { a } }$


<table><tr><td rowspan="2"></td><td colspan="3">T. Liu, G. Bai et al. [43,44]</td><td colspan="3">J. Liu, R. Xu et al. [45]</td><td colspan="3">Li et al. [33]</td><td colspan="3">Our method</td></tr><tr><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td></tr><tr><td>Qbaseline = 6</td><td>0.52</td><td>0.50</td><td>0.55</td><td>2.31</td><td>1.30</td><td>0.51</td><td>0.33</td><td>0.22</td><td>0.14</td><td>0.69</td><td>0.73</td><td>0.72</td></tr><tr><td>Qbaseline = 10</td><td>0.59</td><td>0.62</td><td>0.65</td><td>0.83</td><td>0.47</td><td>0.18</td><td>0.41</td><td>0.34</td><td>0.20</td><td>0.62</td><td>0.62</td><td>0.63</td></tr></table>


a Here, disturbance intensities correspond to the removal of 4, 8 and 16 drones from the swarm at once. 



Table 2 Comparison of resilience metrics for drone swarms of different sizes (50 vs. 60 drones)a.


<table><tr><td rowspan="2"></td><td colspan="3">T. Liu, G. Bai et al. [43,44]</td><td colspan="3">J. Liu, R. Xu et al. [45]</td><td colspan="3">Li et al. [33]</td><td colspan="3">Our method</td></tr><tr><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td><td>4</td><td>8</td><td>16</td></tr><tr><td>50 drones</td><td>0.59</td><td>0.62</td><td>0.65</td><td>0.83</td><td>0.47</td><td>0.18</td><td>0.41</td><td>0.34</td><td>0.20</td><td>0.62</td><td>0.62</td><td>0.63</td></tr><tr><td>60 drones</td><td>0.62</td><td>0.54</td><td>0.65</td><td>1.28</td><td>0.68</td><td>0.32</td><td>0.44</td><td>0.31</td><td>0.23</td><td>0.64</td><td>0.74</td><td>0.68</td></tr></table>


a Here, disturbance intensities correspond to the removal of 4, 8 and 16 drones from the swarm at once. 


$Q _ { \mathrm { b a s e l i n e } }$ under the tested scenarios. Their metric incorrectly showed that as $Q _ { \mathrm { b a s e l i n e } }$ increases, resilience also increases. Undesirable results are highlighted in bold. Similarly, the metric proposed by Li et al. [33] produced the same incorrect trends. In contrast, J. Liu, R. Xu et al. [45] and our proposed metric correctly reflected that systems with lower baseline performance requirements exhibit greater resilience. However, the resilience values from J. Liu, R. Xu et al. [45] originally designed for combat systems, demonstrated significant variations and sometimes exceeding the expected range of 0–1. These results underscore the limited applicability of their metric to UAS systems. Our proposed metric not only accurately reflected the expected trends but also provided consistent values within the expected range, confirming its suitability for UAS resilience evaluation under varying baseline performance requirements and disturbance intensities. 

Experiment Setup 2: Resilience of different swarm sizes. We compared resilience between two drone swarm systems: one with 50 drones (25 sensors and 25 deciders) and another with 60 drones (30 sensors 

and 30 deciders). Generally, larger swarms tend to display higher resilience due to the greater number of resources available to compensate for losses during disturbances. 

We again used three disturbance intensities by removing 4, 8, and 16 drones from each swarm system at once. The results are shown in Table 2. Similar to the results of Experiment Setup 1, the metrics proposed by T. Liu, G. Bai et al. [43,44] and Li et al. [33] failed to capture the expected relationship between swarm size and resilience. Their metric unexpectedly indicated a decrease in resilience as swarm size increased (undesirable relationships are in bold in Table 2). In contrast, both J. Liu, R. Xu et al. [45] and our proposed metric correctly reflected an increase in resilience with swarm size. However, the resilience measurements from J. Liu, R. Xu et al. [45] exhibited significant variability under different disturbances and often exceeded the expected range of 0–1, suggesting that this metric may not be fully suitable for drone swarms. 

The comparative analysis highlights the limitations of existing metrics in evaluating UAS resilience. Both T. Liu, G. Bai et al.’s [43,44] and 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/8d26cea1661e503ccf2c45d1f37793fd3b8e1b599b43b8fd1e61d00879b79562.jpg)



(a) Average performance across 10o simulations


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/61505d19479422a19c18e5fbdf8e185cdc62b38fd2a0c2b4903815e723e12ef6.jpg)



(b)Average resilience across 100 simulations



Fig. 7. Effects of different reconfiguration methods on UAS performance and resilience.


Li et al.’s [33] metrics do not reliably reflect the actual system behavior, while J. Liu, R. Xu et al.’s metric [45], though more consistent, exhibits anomalies when applied to UAS due to its initial design focus on combat systems. Our proposed resilience metric consistently reflects the expected behavior of drone swarms under varying conditions, validating its reliability and effectiveness in accurately evaluating UAS resilience, and confirming its advantages for UAS. 

# 4.4. Comparison of reconfiguration methods

This section compares the proposed reconfiguration method with other strategies to highlight its advantages. We simulated disturbances by removing four agents at each time step (other as described in Section 4.1). The characteristics of the four methods are as follows: 

• Random reconfiguration (RR): After disturbances, remaining agents randomly select interaction partners within their communication range to re-establish connections. 

• Nearest-neighbor reconfiguration (NR): After disturbances, remaining agents reconnect with their closest neighbors within communication range. 

• Preference-based reconfiguration (PR): After disturbances, remaining agents prioritize reconnections with partners offering higher payoffs, e.g., sensor (??) and decider $( D )$ agents interact first due to mutual high returns. 

• Proposed evolutionary game-based reconstruction (GR): Similar to PR, but agents iteratively adjust their interaction strategies based on local payoffs, enabling autonomous optimization of connection behaviors. 

Each reconfiguration strategy was tested across 100 simulation runs. The average performance and resilience results are shown in Fig. 7. In terms of performance (Fig. 7a), both GR and PR outperformed RR and NR, with GR demonstrating slightly better results. In terms of resilience (Fig. 7b), the results followed a similar trend. The wavy line represents the resilience values from 100 simulations, and the horizontal line represents the average resilience. Task times $t _ { 0 }$ to ?? were define as 4 to 20. Both GR and PR exhibited superior resilience compared to RR and NR, with GR achieving the highest resilience among the tested methods. 

The results demonstrate that both GR and PR methods enable agents in UAS to reconnect with the most beneficial interaction partners, leading to improved performance and resilience relative to RR and NR. However, the proposed GR method dynamically adjust the system and optimize strategy through EGT, contributing to more efficient and stable system performance. 

In conclusion, the proposed GR method exhibits exceptional recovery and adaptability, making it particularly suitable for resilient UAS design in dynamic and uncertain environments. By leveraging payoff-driven strategies and iterative optimization, GR ensures superior performance and resilience compared to alternative methods. 

# 5. Resilience enhancement strategies for UAS of cooperative reconfiguration

In this section, we explore the key factors influencing the resilience of cooperative reconfiguration UAS and propose strategies to enhance their resilience. These factors include agent composition, payoff matrix, communication range, and network structure. By analyzing these factors in detail, we aim to propose optimization strategies to improve the system’s resilience in complex environments. 

# 5.1. Agent composition analysis

We analyze the impact of varying agent compositions—sensor agents $S$ and decider agents $D$ —on system resilience. In a system with $N$ agents, $N _ { S }$ represents the number of sensor agents and $N _ { D }$ represents the number of decision-maker agents. The proportion of sensor agents is defined as $\begin{array} { l l l } { p } & { = } & { { \frac { N _ { S } } { N } } } \end{array}$ ???? . Assuming each agent has ?? $k$ neighbors, the expected payoffs for cooperative interactions between agents can be represented by the following matrix: 

$$
\begin{array}{c c} & S \quad D \\ S & \left( \begin{array}{c c} p k a & (1 - p) k b \\ p k c & (1 - p) k d \end{array} \right). \end{array}
$$

Thus, the total system payoff from cooperative interactions $\pi$ can be expressed as: 

$$
\pi = N k \left(p ^ {2} a + p (1 - p) (b + c) + (1 - p) ^ {2} d\right) \tag {10}
$$

Next, to maximize $\pi$ , we solve for $p$ by differentiating Eq. (10). The optimal proportion $p$ is given by: 

$$
p = \frac {2 d - b - c}{2 (a - b - c + d)} \tag {11}
$$

This value maximizes the system’s performance and resilience, provided that $a - b - c + d < 0$ . 

To validate this analytical result, we conducted simulations with UAS systems consisting of 40, 50, and 60 agents. The proportion $p$ was varied by adjusting the number of sensor agents. Each configuration was simulated 100 times using parameters $a = 0$ , $b = 0 . 5$ , $c = 0 . 5$ , and $d = 0 . 1$ . According to Eq. (11), the optimal proportion $p$ for maximizing system resilience is 0.44. As shown in Fig. 8(a–c), system resilience increases with $p ,$ , peaking at $\begin{array} { r l r } { p } & { { } = } & { 0 . 4 4 } \end{array}$ , before gradually declining. This trend was consistent across all tested UAS sizes, validating the predictions of Eq. (11). Notably, resilience sharply drops to zero as $p$ approaches 1. 

To further evaluate the robustness of the analytical results, we examined the effects of different communication ranges among agents (Fig. 8(d–f)) and varying disturbance intensities (Fig. 8(g–i)) in the UAS with 60 agents. These results mirrored the trends observed in Fig. 8(a–c), demonstrating consistent behavior across different conditions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/dbed9cff59789fe3223e137a244bbf249a6634c61fd067f302d5b87b3853a51f.jpg)



(a) UAS with 40 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/b9718688ae185e8c19232d714a276619569f134b6d93b562057792e49f65d24d.jpg)



(b) UAS with 50 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/4fd7d918910ef9d2cc3daba083be0380f160c26e07cfd7c40250912e489392e9.jpg)



(c) UAS with 60 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/7d64b537b95db2298742f7612b81aeb746fde001bba7bcd26a023131755b4db8.jpg)



(d) Agent's communication range is 10


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/15958e33f4494770cf927e312cd8bb3799705895c0c63096ee2f933bbdf8e4e9.jpg)



(e) Agent's communication range is 20


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/764f0c55fc0c23be071c77c98b539366f5c4cd40f7439160a95e881e11ea7083.jpg)



(f) Agent's communication range is 30


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/27f656948ae6ac18ba1f21d2f9d46a770dd0b02594ba73bac15714397e140d92.jpg)



(g) Disturbance from removing 4 drones


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/fdc24e080d7bb8283d17e19ea7d5c3ecc1abdad407a78a106aa307a6794b107f.jpg)



(h) Disturbance from removing 8 drones


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/84d8d7cf7614bb6c552baf6777babc6f8b0c6115056109bc107c43fc73613cd3.jpg)



(i) Disturbance from removing 16 drones



Fig. 8. Impact of the sensor agent proportion $p$ on the resilience of UAS, with the payoff matrix parameters $a = 0$ , $b = 0 . 5$ , $c = 0 . 5$ , $d = 0 . 1$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/c9a31e9425b12ee0527934b48e1b380ce124a55e1beffdbe1ce2cfb97e597409.jpg)



(a) UAS with $\mathsf { a } { = } \dot { 0 }$ $\scriptstyle \mathtt { b - c = 0 . 5 }$ ,d=0.1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/2645740a07bb67cc4c6145f5dcfbf61611b799160fd6096a7748bb4426f023d3.jpg)



(b) UAS with a=0,b=0.7, $\scriptstyle \mathtt { c } = 0 . 3$ ,d=0.1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/6d0adfc491c10850fa154a8b3bd2cc6576e77d66aec5cb5f8579089c748716f2.jpg)



(c) UAS with a=0, b=0.2, $\mathsf { c } { = } 1$ ,d=0.1



Fig. 9. Effect of the sensor agent proportion $p$ on UAS resilience under different payoff parameters.


Additionally, we conducted sensitivity analyses with different parameter settings for ??, ??, ??, and $d$ , as shown in Fig. 9. Specifically, we tested three scenarios: (i) $a = 0$ , $b = 0 . 5$ , $c = 0 . 5$ , $d = 0 . 1$ ; (ii) $a = 0$ , $b = 0 . 7$ , $c =$ 0.3, $d = 0 . 1$ ; and (iii) $a = 0$ , $b = 0 . 2$ , $c = 1$ , $d = 0 . 1$ . The corresponding optimal $p$ values were calculated as 0.44, 0.44, and 0.45, respectively. In all cases, the simulation results aligned closely with the theoretical predictions of Eq. (11), underscoring the robustness of the optimal $p$ across diverse parameter configurations. Overall, the analytical results were consistently validated by the simulation findings, demonstrating that the optimal sensor agent proportion $\left( p \right)$ reliably enhances UAS resilience under various operational scenarios. 

# 5.2. Impact of the payoff matrix

We further analyzed the influence of the parameters in the payoff matrix on UAS payoff $\pi$ and its resilience. Assuming the system consists of $N$ agents, with half being sensor agents $( S )$ and the other half being decider agents $( D )$ , and each agent has $k$ neighbors of any type. Then, we can derive $\textit { a } = \textit { d }$ from Eq. (11). Under this condition, the total system payoff $\pi$ is expressed as: 

$$
\pi = N \cdot k \cdot \left[ \frac {1}{2} \cdot a + \frac {1}{4} \cdot (b + c) \right], \tag {12}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/53f7a8d5197b6994a623602507af5c9800a52c4f12906cfda9deab3ed0078f92.jpg)



(a) cross-type cooperation: b, ${ \mathfrak { c } } > { \mathfrak { a } }$ ,d


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/aa8f92da926b59852d3c2aba0324775673b7a8ee12802a4626eff8f841c863eb.jpg)



(b) same-type cooperation: a > b


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/f5627c37f8a83e0dcb7d4d2e357423768ba108eeb6cbadced26525948208b772.jpg)



(c) same-type cooperation: a> c



Fig. 10. Effect of payoff matrix parameters on UAS cooperation patterns.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/28b89af19e09cd5ab5202f571b59feef2e02e2debe08bca4c109570a5d4d1915.jpg)



(a) UAS with 40 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/52434c19d28c4463fbbe47882ac93911b9a012111d1a7a8b238e441883f14104.jpg)



(b) UAS with 50 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/35a949087dc2950e1db7c9901555a5f78cf8ece98cb555cea640ca74761949a5.jpg)



(c) UAS with 60 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/8a95a2220d7b419efc0a0757ab6a4e210049f598712262e96ab39ecd80d0e433.jpg)



(d) UAS with 40 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/61aa7b3ef1c172bda412562b2c70a13889791e080b21c2672a15a09e72119932.jpg)



(e) UAS with 50 agents


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/db8d6da8b36ba348a2ca32e23bed4eb0c7fe3cf75fafdf20604050d4ac12a18f.jpg)



(f) UAS with 60 agents



Fig. 11. The impact of the communication range (??) on the resilience of UAS.


where ?? represents the payoffs for cooperation among similar types of agents, and $b$ and ?? represent the payoffs for cooperation between different types of agents. 

Since $\pi$ is a linear function of ??, ??, and ??, increasing these parameters directly enhances the total system payoff and improves the system’s resilience. However, the relative magnitudes of these parameters determine the cooperation patterns within the system, as illustrated in Fig. 10. We formalized the network structure of a 30 agent UAS system with 15 ?? agents and 15 ?? agents. When cross-type payoffs $( b , c )$ exceed same-type payoffs $( a , d )$ , as shown in Fig. 10(a), cooperation predominantly occurs between agents of different types, fostering interagent collaboration. Conversely, if same-type cooperation payoffs (??) surpass cross-type payoffs (?? or $c ]$ , agents tend to cooperate within their own type, as depicted in Fig. 10(b) $\left( a > b \right)$ and (c) $\left( a > c \right)$ . Therefore, maintaining $b , c > a , d$ is crucial to encouraging balanced and effective collaboration between $S$ and $D$ agents. 

# 5.3. Communication range analysis

We then analyzed the impact of agent communication range on UAS resilience by modeling systems with varying communication ranges and measuring the resulting resilience. Specifically, we considered a $5 0 \times 5 0$ coordinate plane with swarms consisting of 40, 50, and 60 agents, evenly divided between sensor and decider agents. The communication range was varied between 5 and 50 units, and 100 simulations were 

run for each range. Random failures were simulated by removing 8 agents from the system during each disturbance event. The simulation results are shown in Fig. 11(a–c). We observed that resilience increases with communication range. Initially, small increases in range lead to rapid improvements in resilience. However, as the range grows, the rate of improvement diminishes, indicating diminishing returns. This trend was consistent across all tested swarm sizes. 

However, increasing the communication range can also introduce stochastic disturbances, such as higher power consumption, communication delays, and interference. To account for these factors, we modeled such disturbances using Gaussian noise. The noise intensity was assumed to increase exponentially with the communication distance between agents. Consequently, the performance functions of agents in Eqs. (3) and (4) were updated to include this noise: 

$$
f _ {i} ^ {\beta} = s _ {i} + \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(a x _ {S} + b x _ {D}\right) - \sigma e ^ {\gamma d _ {i j}}, \tag {13}
$$

$$
g _ {i} ^ {\beta} = d _ {i} + \sum_ {j = 1} ^ {N (\beta)} A _ {i j} ^ {\beta} \left(c x _ {S} + d x _ {D}\right) - \sigma e ^ {\gamma d _ {i j}}, \tag {14}
$$

where $\sigma$ represents additive, independent Gaussian noise, ?? is the exponential growth coefficient, and $d _ { i j }$ is the communication distance between agents. The results, shown in Fig. 11(d–f), used $\gamma = 0 . 1$ and Gaussian noise with a mean of 0 and a standard deviation of 0.01. These 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/da11e1f1e71827fdd048e29833b470a28617fcf7b16330b7c1b650b88db28a01.jpg)



(a) Lattice network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/d9af73b951a4965ab02e71cfc7beacbd79e2b317d8f476fa91c126d9485e3fe6.jpg)



(b)ER network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/d000f1bb33bcee8de8c6b7090f14006a6b2d677c2ee04f674490dcd7f4ce75e3.jpg)



(c)WS network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/2dde9b71-ba76-47ec-a3ce-ab2cbebda63a/77e14203c0b60b475173e66fe5804ced16793d558e9b8ee0585e71887076ec52.jpg)



(d) BA network



Fig. 12. Impact of network structures on the resilience of UAS.


results indicate that while resilience is slightly reduced compared to Fig. 11(a–c), the overall impact remains stable. 

Thus, increasing the communication range of agents can enhance system resilience, but further increases beyond certain ranges will not significantly boost resilience, even when accounting for random interference. 

# 5.4. Network structure analysis

In previous sections, we analyzed UAS configurations under the assumption that each agent was connected to at most three other agents. While this simplification overlooks the possibility that agents within the network may have differing numbers of connections, leaving it unclear how different network structures affect resilience. To address this, we explored how various UAS network topologies impact system resilience and identified strategies to enhance resilience through structural design. 

We assumed that each agent could have a different number of links and tested four distinct network topologies: lattice network [46], ER (Erdős–Rényi) network [47], WS (Watts–Strogatz) network [48], and BA (Barabási–Albert) network [49]. To assess the effect of system size, we used configurations with 40, 50, and 60 agents, running 100 simulations for each configuration. The average degree of the network ranged from 3 to 5. Random failures were modeled by removing 8 agents during each disturbance event. 

The resilience distributions of these network structures are shown in Fig. 12. Among all tested topologies, the BA network exhibited the lowest resilience, while the WS network demonstrated the highest resilience, with lattice and ER networks positioned between these extremes. These results highlight the critical role of network topology in determining the overall resilience of UAS. The BA network’s reliance on a few highly interconnected hubs means that the failure of these hubs can significantly compromise overall connectivity. This inherent vulnerability to targeted or random hub failures reduces the system’s resilience compared to other topologies with more uniform connection distributions. Conversely, the WS network, with its balance of local clustering and short global paths, facilitates the rapid reconstruction of broader network connections, enabling the system to better withstand disruptions. Consequently, the WS network emerges as a particularly robust structure for enhancing system resilience. 

# 6. Conclusion and future work

The improvement of resilience in UAS is a complex and important task. This paper explores the effects of cooperative reconfiguration based on evolutionary game theory on UAS performance and resilience, providing valuable insights into how cooperation among agents enhanced resilience. First, we established a cooperative reconfiguration 

framework that allows UAS agents to autonomously adjust their network structure based on cooperative payoffs after disturbances. Second, we developed a resilience metric that considers continuous disturbances, mission tasks, and performance baselines, and validated its effectiveness through case studies and comparative experiments. Finally, we analyzed the optimal configurations for improving UAS resilience, focusing on agent composition, payoff matrices, communication range, and network structure. 

Our study focuses on a UAS composed of two primary types of agents: sensor entities $( S )$ and decider entities $( D )$ . The main conclusions are as follows: (1) there exists an optimal ratio of $S$ agents, denoted as $p$ , that maximizes both performance and resilience of UAS, and we derived a precise criterion for $p ;$ (2) effective collaboration between $S$ and $D$ agents is achieved only when the payoff matrix satisfies the condition $b , c \ > \ a , d$ ; (3) increasing the communication range of agents can enhance system resilience, but further increases beyond a certain range do not lead to significant improvements, even under random disturbances; and (4) network topology also significantly impacts UAS resilience, particularly in structures with local clusters and short global paths that facilitate rapid reconfiguration and enhance the system’s ability to withstand disturbances. 

Future research could explore extending the proposed method to systems with three or more agent types, broadening its applicability to more complex real-world scenarios. However, such extensions present significant challenges, including increased complexity in multi-agent interactions, collaborative processes, and payoff structures, which complicate model construction and analysis. Addressing these challenges may require advanced modeling techniques, such as tensor-based representations for high-order interactions [50] and dynamic evolutionary games [51], to capture complex agent behaviors. These approaches would support the adaptation of the proposed method to multi-agent systems and facilitate its application in diverse and operationally complex environments. 

In summary, our work provides valuable insights into the resilience of unmanned systems through cooperative reconfiguration. The area of agent reconfiguration is broad, and the evolutionary game theory-based mechanism we propose would benefit from further validation in realworld contexts to evaluate its effectiveness under various operational conditions and enable comparisons with other cooperative strategies. Recently, Chen et al. [23] introduced a resilience metric for unmanned system-of-systems, highlighting the need for cooperative reconfiguration strategies to enhance resilience. We also plan to build upon this work to further optimize cooperative reconfiguration strategies, thereby strengthening resilience. 

# CRediT authorship contribution statement

Chengxing Wu: Writing – review & editing, Writing – original draft, Validation, Methodology, Investigation, Formal analysis, Conceptualization. Hongzhong Deng: Writing – review & editing, Writing – 

original draft, Resources, Methodology, Funding acquisition, Formal analysis, Conceptualization. Hongqian Wu: Writing – original draft, Validation, Methodology, Conceptualization. Chengyi Tu: Writing – review & editing, Resources, Funding acquisition, Conceptualization. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgments

This work was supported by the National Natural Science Foundation of China (NSFC) [grant number 71690233, and 71771214]. 

# Data availability

Data will be made available on request. 

# References



[1] Zhang T, Chai L, Wang S, Jin J, Liu X, Song A, Lan Y. Improving autonomous behavior strategy learning in an unmanned swarm system through knowledge enhancement. IEEE Trans Reliab 2022;71(2):763–74. 





[2] Chen J, Sun J, Wang G. From unmanned systems to autonomous intelligent systems. Eng. 2022;12:16–9. 





[3] Couzin ID, Krause J, Franks NR, Levin SA. Effective leadership and decision-making in animal groups on the move. Nature 2005;433(7025):513–6. 





[4] Nguyen ND, Nguyen T, Nahavandi S. Multi-agent behavioral control system using deep reinforcement learning. Neurocomputing 2019;359:58–68. 





[5] Lohan P, Mishra D. Utility-aware optimal resource allocation protocol for UAVassisted small cells with heterogeneous coverage demands. IEEE Trans Wirel Commun 2019;19(2):1221–36. 





[6] Chung S-J, Paranjape AA, Dames P, Shen S, Kumar V. A survey on aerial swarm robotics. IEEE Trans Robot 2018;34(4):837–55. 





[7] Singireddy SRR, Daim TU. Technology roadmap: Drone delivery–amazon prime air. Infrastruct Technol Management: Contrib from Energy, Heal Transp Sect 2018;387–412. 





[8] Saffre F, Hildmann H, Karvonen H, Lind T. Monitoring and cordoning wildfires with an autonomous swarm of unmanned aerial vehicles. Drones 2022;6(10):301. 





[9] Saulnier K, Saldana D, Prorok A, Pappas GJ, Kumar V. Resilient flocking for mobile robot teams. IEEE Robot Autom Lett 2017:2(2);1039-46. 





[10] Zhou X, Huang Y, Bai G, Xu B, Tao J. The resilience evaluation of unmanned autonomous swarm with informed agents under partial failure. Reliab Eng Syst Saf 2024;244:109920. 





[11] Wang B, Ng PH, Elhadidi BMNAK, Ang HS, Moon SK. Failure analysis and finite element simulation for structural systems in an unmanned aerial vehicle. In: 2019 16th international conference on ubiquitous robots. UR, IEEE; 2019, p. 636–40. 





[12] Mozaffari M, Saad W, Bennis M, Nam Y-H, Debbah M. A tutorial on UAVs for wireless networks: Applications, challenges, and open problems. IEEE Commun Surv & Tutorials 2019;21(3):2334–60. 





[13] Xu B, Bai G, Fang Y, Tao J, et al. Failure analysis of unmanned autonomous swarm considering cascading effects. J Syst Eng Electron 2022;33(3):759–70. 





[14] Duan H, Huo M, Fan Y. From animal collective behaviors to swarm robotic cooperation. Natl Sci Rev 2023;10(5):nwad040. 





[15] Innocente MS, Grasso P. Swarms of autonomous drones self-organised to fight the spread of wildfires. In: RSFF 2018 robust solutions for fire fighting: GEOSAFE workshop on robust solutions for fire fighting. CEUR; 2018, p. 30–9. 





[16] Campion M, Ranganathan P, Faruque S. UAV swarm communication and control architectures: a review. J Unmanned Veh Syst 2018;7(2):93–106. 





[17] Holling CS, et al. Resilience and stability of ecological systems. Annu Rev Ecol Syst 1973;4:1–23. 





[18] Huang H, Tu C, D’Odorico P. Ecosystem complexity enhances the resilience of plant-pollinator systems. One Earth 2021;4(9):1286–96. 





[19] Shishodia A, Sharma R, Rajesh R, Munim ZH. Supply chain resilience: A review, conceptual framework and future research. Int J Logist Manag 2023;34(4):879–908. 





[20] Zhou Y, Wang J, Yang H. Resilience of transportation systems: concepts and comprehensive review. IEEE Trans Intell Transp Syst 2019;20(12):4262–76. 





[21] Smith O, Cattell O, Farcot E, O’Dea RD, Hopcraft KI. The effect of renewable energy incorporation on power grid stability and resilience. Sci Adv 2022;8(9):eabj6734. 





[22] Vachtsevanos G, Lee B, Oh S, Balchanos M. Resilient design and operation of cyber physical systems with emphasis on unmanned autonomous systems. J Intell Robot Syst 2018;91:59–83. 





[23] Chen Z, Yin S, Li L, Cui W, Hong D. Resilience metric and dynamic assessment of unmanned system-of-systems considering cooperative reconfiguration strategies. IEEE Trans Reliab 2024. 





[24] Zhang P, Wu T, Cao R, Li Z, Xu J. UAV swarm resilience assessment considering load balancing. Front Phys 2022;10:821321. 





[25] Tran HT, Domerçant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Procedia Comput Sci 2016;95:126–33. 





[26] Tran HT, Balchanos M, Domerçant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng Syst Saf 2017;158:73–84. 





[27] Wubben J, Fabra F, Calafate CT, Cano J-C, Manzoni P. A novel resilient and reconfigurable swarm management scheme. Comput Netw 2021;194:108119. 





[28] Qiang F, Xingshuo H, Bo S, Yi R, Zili W, Dezhen Y, Yaolong H, Ronggen F. Resilience optimization for multi-UAV formation reconfiguration via enhanced pigeon-inspired optimization. Chin J Aeronaut 2022;35(1):110–23. 





[29] Cheng C, Bai G, Zhang Y-A, Tao J. Resilience evaluation for UAV swarm performing joint reconnaissance mission. Chaos: An Interdiscip J Nonlinear Sci 2019;29(5). 





[30] Bai G, Li Y, Fang Y, Zhang Y-A, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020;193:106602. 





[31] Sun Q, Li H, Wang Y, Zhang Y. Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems. Reliab Eng Syst Saf 2022;222:108426. 





[32] Li H, Sun Q, Wang M, Liu C, Xie Y, Zhang Y. A baseline-resilience assessment method for UAV swarms under heterogeneous communication networks. IEEE Syst J 2022;16(4):6107–18. 





[33] Li H, Sun Q, Zhong Y, Huang Z, Zhang Y. A soft resource optimization method for improving the resilience of uav swarms under continuous attack. Reliab Eng Syst Saf 2023;237:109368. 





[34] Zhang C, Liu T, Bai G, Tao J, Zhu W. A dynamic resilience evaluation method for cross-domain swarms in confrontation. Reliab Eng Syst Saf 2024;244:109904. 





[35] Kong L, Wang L, Cao Z, Wang X. Resilience evaluation of UAV swarm considering resource supplementation. Reliab Eng Syst Saf 2024;241:109673. 





[36] Tan Y, Zhang X, Yang K. Research on networked description and modeling methods of armament system-of-systems. J Syst Manag 2012;21(6):781–6. 





[37] Li J, Zhao D, Jiang J, Yang K, Chen Y. Capability oriented equipment contribution analysis in temporal combat networks. IEEE Trans Syst Man, Cybern.: Syst 2018;51(2):696–704. 





[38] Chen B, Pang G, Xiang Z, Gao X, Chen Y, Chen S. Modeling dual-layer interdependent command and control networks for integrated reconnaissance-strike and OODA-loop capabilities. IEEE Trans Netw Sci Eng 2024;11(6):5744–59. 





[39] Zhou Y, Cheng N, Lu N, Shen XS. Multi-UAV-aided networks: Aerialground cooperative vehicular networking architecture. IEEE Veh Technol Mag 2015;10(4):36–44. 





[40] Neill DB. Evolutionary stability for large populations. J Theoret Biol 2004;227(3):397–401. 





[41] Smith JM. The theory of games and the evolution of animal conflicts. J Theoret Biol 1974;47(1):209–21. 





[42] Bruneau M, Chang SE, Eguchi RT, Lee GC, O’Rourke TD, Reinhorn AM, Shinozuka M, Tierney K, Wallace WA, Von Winterfeldt D. A framework to quantitatively assess and enhance the seismic resilience of communities. Earthq Spectra 2003;19(4):733–52. 





[43] liu T, Bai G, tao J, Zhang Y, Fang Y. Mission-oriented resilience evaluation method for complex system.. Syst Eng Electron 2021;43(4). 





[44] Liu T, Bai G, Tao J, Zhang Y-A, Fang Y. A multistate network approach for resilience analysis of uav swarm considering information exchange capacity. Reliab Eng Syst Saf 2024;241:109606. 





[45] Liu J, Xu R, Li J, Yang K, Lou Z. Enhancing the resilience of combat system-ofsystems under continuous attacks: Novel index and reinforcement learning-based protection optimization. Expert Syst Appl 2024;251:123912. 





[46] Ohtsuki H, Hauert C, Lieberman E, Nowak MA. A simple rule for the evolution of cooperation on graphs and social networks. Nature 2006;441(7092):502–5. 





[47] Erdos P, Rényi A, et al. On the evolution of random graphs. Publ Math Inst Hung Acad Sci 1960;5(1):17–60. 





[48] Watts DJ, Strogatz SH. Collective dynamics of ‘small-world’networks. Nature 1998;393(6684):440–2. 





[49] Barabási A-L, Albert R. Emergence of scaling in random networks. Sci. 1999;286(5439):509–12. 





[50] Civilini A, Sadekar O, Battiston F, Gómez-Gardeñes J, Latora V. Explosive cooperation in social dilemmas on higher-order networks. Phys Rev Lett 2024;132(16):167401. 





[51] Su Q, McAvoy A, Plotkin JB. Strategy evolution on dynamic networks. Nat Comput Sci 2023;3(9):763–76. 

