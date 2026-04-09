# Disintegrating the information exchange network of UAV swarm based on relative resilience

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/75725a3726482e13ccb9cb72dc5f4e5008f82af96ec513b150072413bd74ec23.jpg)


Yawen Zhu ${ \mathrm { a } } _ { \oplus }$ , Guanghan Bai ${ \mathfrak { a } } , ^ { * } \oplus$ , Zhan Xu b , Louzhaohan Wang c , Bei Xu 

a College of Intelligence Science and Technology, National Key Laboratory of Equipment State Sensing and Smart Support, National University of Defense Technology, Changsha 410073, China 

b Department of Scientific Research, National University of Defense Technology, Changsha 410073, China 

c Institute of Remote Sensing Satellite, China Academy of Space Technology, Beijing 100094, China 

d School of General Aviation, Nanchang HangKong University, Nanchang 330000, China 

# A R T I C L E I N F O

Keywords: 

UAV swarm 

Information exchange network 

Disintegration 

Relative resilience 

# A B S T R A C T

An unmanned aerial vehicle (UAV) swarm composed of autonomous UAVs coordinate through information exchange (IE) network in a self-organized manner to achieve collective objectives. The inherent hyper-dynamic, self-adaptive and self-recovery capabilities of IE network pose significant challenges to develop effective disintegration strategies. Most of conventional network disintegration methods designed for static networks, are inappropriate for IE network, whose post-damage reconfiguration aligns with its resilience. By considering both historical information and future trends, this study proposed a new disintegrating method for the IE network of UAV swarm based on relative resilience, which quantifies networks’ instantaneous recovery capacity at specific moments. The relative resilience combines temporal efficiency and rate of change, enabling real-time resilience analysis without requiring complete resilience process data. Simulation studies demonstrate that the proposed method outperforms other methods in different networks, achieving a $4 0 \%$ improvement in disruption effectiveness compared to the baseline method and maintaining a lower recovery level throughout the disintegrating process. This indicates that the method can achieve more sustained and balanced network disintegration, with higher cost-effectiveness and adaptability to dynamic changes. This work exhibits advantages in the persistence and balance of disintegration outcomes and provides a more suitable framework for dynamic network disintegration. 

# 1. Introduction

An unmanned aerial vehicle (UAV) swarm is a group of numerous UAVs performing tasks in a self-organized and self-`adaptive manner to achieve an overall mission objective [1]. Unmanned swarms can adapt to changing tasks by reorganizing its cooperative distributed networks. This enables the swarm to maintain relative stability in dynamic environments while ensuring task completion [2]. Focusing on counter-terrorism and security applications, disintegrating adversarial swarm networks becomes critical for defense and security purposes. In addition, the highly dynamic, self-organizing, and self-recovering characteristics make UAV swarms resilient to disruptions, particularly in terms of disintegration [3]. 

For UAV swarms, an efficient and resilient information exchange (IE) network among swarm is essential to accomplish missions [1]. IE 

network constitutes the core foundation for swarm autonomous coordination, making its disruption the critical pathway to swarm disintegration. In swarm scenarios, effective disintegration is primarily achieved through disrupting the underlying communication network that enables coordination and collaboration among swarm entities. Due to the high mobility of UAVs, the relative distances between nodes within the IE network are constantly changing, leading to real-time variations in network topology [4]. Consequently, the essence of swarm disintegration entails disintegrating a dynamic and evolving network topology with self-recovering capabilities. 

Network disintegration [5] refers to the disruption of network topology, the weakening of network functionality, and the interference with network behavior through the removal of certain nodes or edges [6]. By identifying the minimal set of nodes that can cause the fastest disintegration of the network, the search for the optimal disintegration 

strategy, also known as the optimal percolation problem [7,8], is conducted. This is a combinatorial optimization problem, for which a small-scale networks, such optimization problems can be challenging [9]. Early efforts focused on finding the minimal set of nodes to disrupt the network by evaluating a series of topological centralities of the nodes. Traditional methods of disintegration networks often rely on metrics such as ND (Network Dismantling) [10], SC (Subgraph Centrality) [11], GND (Generalized Network Dismantling) [12], CI (Collective Influence) [13] and so on. The approach based on centrality for network dismantling is applied and can be categorized according to different types of centrality, including degree centrality [14,15], recalculating degree centrality [16], K-core centrality [17], betweenness centrality [18] and etc. 

These reported methods have shown good performance in static networks. However, they are less desirable to handle the dynamic networks [8]. Because the disintegration problem of static network is NP-hard [5], and the dynamical changes of nodes and topology during the dismantling process further increase the difficulty because of the changes in the set of solutions. With the advancement of dynamic network research, scholars have begun to focus on methods for disintegrating dynamic networks. For instance, various methodologies have been developed, including Machine learning dismantling [19,20], Cost-Effective network disintegration [21–23], Disintegration based on cascading [24,25], Dismantling based on community topology [26], Disintegration based on Kernel density estimation [27], Disintegration based on percolation theory [28,29] and Disintegration based on Heuristic algorithms [30,31] among others. The related studies of network disintegration are shown in Table 1. 

However, the disintegration of swarm IE networks poses significant challenges because these IE networks demonstrate self-recovery through reconfiguration post-disruption [39]. For instance, disintegration strategies based on centrality metrics [40] may degrade the network, yet its structural integrity and operational functionality restore in subsequent phases due to dynamic reconfiguration and autonomous recovery capabilities [41]. When addressing such adaptive networks [42], disintegration approaches focusing on instantaneous topological snapshot suffer diminished efficacy. They fail to account for the self-adaptive nature inherent in evolving network architectures [43] . It is necessary to develop a different disintegration methodology rooted in the fundamental characteristics of swarm IE networks, which are characterized by hyper-dynamic evolution, self-adaptive coordination, and self-recovery mechanisms [44]. This reconfigurability manifests in the recovery process following performance changes, which aligns with the concept of resilience [45,46]. It had been introduced to characterize the system’s ability to resist, absorb, recover and adapt from disturbances [47]. As the reverse of network disintegration [26], highlighting resilience during the disintegration process is critical for understanding the robustness and adaptability of complex systems [48]. The related resilience models are shown in Table 2. 

Based on the concept of resilience proposed by Holling, resilience models have evolved. The resilience triangle model [49] uses the area of 


Table 1 Comparisons of the disintegration methods.


<table><tr><td>Reference</td><td>Based Theory</td><td>Object</td></tr><tr><td>[12,14]</td><td>Betweenness centrality</td><td>Unweighted graphs</td></tr><tr><td>[17]</td><td>K-shell decomposition</td><td>Internet</td></tr><tr><td>[27]</td><td>Kernel density estimation</td><td>Synthetic &amp; real-world networks</td></tr><tr><td>[10,32]</td><td>Network dismantling</td><td>Random graphs</td></tr><tr><td>[31]</td><td>Nondominated sorting genetic algorithm</td><td>Multilayer networks</td></tr><tr><td>[33]</td><td>Collective influence</td><td>Hierarchical networks</td></tr><tr><td>[6,34,35]</td><td>Tabu search</td><td>Undirected graph and spatial networks</td></tr><tr><td>[36]</td><td>Global search algorithms</td><td>ER WS BA</td></tr><tr><td>[37]</td><td>Deep reinforcement learning</td><td>BA</td></tr><tr><td>[38]</td><td>Link-Based</td><td>Spatial Network</td></tr></table>


Table 2 Comparisons of the resilience models.


<table><tr><td>Reference</td><td>Proposed</td><td>Year</td><td>Specialty</td></tr><tr><td>[47]</td><td>Holling</td><td>1973</td><td>Definition of resilience</td></tr><tr><td>[49]</td><td>Bruneau et al.</td><td>2003</td><td>Classical resilience triangle</td></tr><tr><td>[50]</td><td>Zobel</td><td>2011</td><td>Predictive resilience triangle model</td></tr><tr><td>[51]</td><td>Herry et al.</td><td>2012</td><td>Five stages of resilience process</td></tr><tr><td>[52]</td><td>Nan et al.</td><td>2017</td><td>Five parameters for resilience process</td></tr><tr><td>[53]</td><td>Tran et al.</td><td>2017</td><td>Five factors for calculating resilience</td></tr><tr><td>[54]</td><td>Zeng et al.</td><td>2021</td><td>Based on Markov reward process</td></tr><tr><td>[55]</td><td>Liu et al.</td><td>2021</td><td>Task-time resilience</td></tr><tr><td>[56]</td><td>Wang et al.</td><td>2024</td><td>Resilience based on community structure</td></tr><tr><td>[57]</td><td>Zhang et al.</td><td>2024</td><td>Dynamic resilience</td></tr><tr><td>[58]</td><td>Dui et al.</td><td>2024</td><td>Multi-phased resilience</td></tr></table>

a triangle formed by the decline in performance over time to represent system resilience. Zoble’s resilience model [59] focuses on the velocity of system performance degradation and can be applied to scenarios involving continuous interference events. Henrry’s resilience model [51] emphasizes the five-stages process of resilience. Nan’s resilience model [52] introduces five parameters and integrates them into a comprehensive formula to describe the resilience process. Similarly, Tran’s resilience model [53] incorporates five factors, namely recovery capacity, overall performance factor, absorption capacity, fluctuation factor, and time factor. In practical applications, Mission-oriented resilience [55] focuses on system performance within a mission-specific context and its temporal resilience. Dynamic resilience models [57] emphasize the real-time resilience of systems operating in dynamic environments. Many existing models based on time integration, require access to the entire resilience process, including disturbance onset, recovery trajectory, and final state. This is impractical in adversarial or rapidly changing environments where data may be incomplete or unavailable [60]. In addition, during the disintegration process, the dynamic nature of network changes leads to significant data fluctuations and incompleteness [61]. Therefore, a new resilience model is need to describe the instantaneous relative resilience capacity of networks given historical and predictive information from the disintegration process [62]. 

This study focuses on the reconfiguration and recovery during the disintegration process of UAV swarm’s IE network. A relative resilience model is proposed to characterize the network’s relative resilience level during disintegration. By incorporating both historical information and future trends, a disintegration method based on the proposed relative resilience is developed. The main contributions of this study are as follows. 

a) Relative resilience metric: The proposed metric quantifies the network’s instantaneous resilience capacity relative to a reference time, combining temporal efficiency and rate of change. This realtime metric is adaptable to diverse scenarios and provides a novel perspective for resilience assessment in dynamic systems. 

b) Resilience-based disintegration strategy: The proposed strategy incorporates historical information to identify critical nodes and reduce redundant attacks, while trend prediction enables proactive targeting of future topological changes. Simulation results demonstrate its effectiveness in suppressing adaptive reconfiguration and improving cost-effectiveness compared to traditional methods. 

The rest of this paper is as follows. Section 2 focuses on modeling swarm dynamic communication network. Section 3 defines relative resilience and proposes a comprehensive relative resilience model for analysis and validation. Section 4 incorporates historical and predictive information to develop a disintegration model based on relative resilience. Lastly, Section 5 verifies the proposed model through simulation case studies. 

# 2. Model of swarm information exchange network

UAV swarms rely on IE networks for swarm control. A rational information interaction model is crucial for ensuring the normal movement of individuals within the swarm and the accurate execution of missions. During mission execution, UAVs are in motion, resulting in dynamic changes in the distances between individual swarm members. Consequently, the IE network may exhibit characteristics of a dynamic scale-free network under certain conditions [63,64], such as preferential attachment during dynamic interactions. And Li et al. [65] experimentally verified the applicability of the scale-free network modeling method on swarms. 

Dynamic networks are used to describe networks whose topology changes over time, with changes in topology manifested as the addition or removal of nodes or edge. Focusing on the horizontal plane where most swarm interactions occur during certain missions, we use twodimensional coordinates to simplify for modeling. The positions of individual nodes change over time according to motion models, the position of a node at time t can be represented as $F ( X ( t ) , Y ( t ) )$ , which are given as follows: 

$$
\frac {d X (t)}{d t} = f _ {x} \left(x _ {0}, v _ {0}, a, t\right), \tag {1}
$$

$$
\frac {d Y (t)}{d t} = f _ {y} \left(y _ {0}, v _ {0}, a, t\right), \tag {2}
$$

where $X ( t )$ and $Y ( t )$ denote the coordinate values of the node at time t; x0 and $y _ { 0 }$ denote the initial coordinates of the node; $\nu _ { 0 }$ denotes the initial velocity of the node; a denotes the acceleration of the node; $f _ { x }$ (⋅) denotes the velocity component function in the $x -$ direction; and $f _ { y }$ (⋅) denotes the velocity component function in the y-direction. Because the network nodes change with time, the distance between nodes also change, resulting in a dynamic network topology. The differential equation of the network state can be obtained as: 

$$
\frac {d W (t)}{d t} = g \left(F (X (t), Y (t)), P (t), C (t), t\right), \tag {3}
$$

where $\ b { F } ( \ b { X } ( t ) , \ b { Y } ( t ) ) \epsilon \mathbb { R } ^ { n }$ represents node location, where $\mathbb { R } ^ { n }$ denotes an ndimensional vector space; $P ( \mathbf { t } ) \epsilon \mathbb { R } ^ { d }$ is characteristic parameters of network node function, where $\mathbb { R } ^ { d }$ denotes an $d$ -dimensional vector space; $C ( \mathrm t )$ is the network connection rules; $g ( \cdot )$ denotes the instantaneous change function controlling the dynamics of the network; $W ( t ) \epsilon \mathbb { R } ^ { n * d }$ represents the states of the network with n nodes, each composed of dynamic systems, at time $t \epsilon [ 0 , \infty ]$ , and these states are governed by connection rules $C ( t ) . \ \mathbb { R } ^ { n * d }$ denotes the $n * d$ -dimensional vector space, where $d$ denotes the feature dimension of 

Due to the positions of the nodes varying over time, the network becomes dynamic. At a given moment, the connection rules $C ( \mathbf { t } )$ of the network nodes follow the dynamic generation algorithm for IE network topology, which considers geographic distance. At the initial moment, $m _ { 0 }$ initial nodes are given, with all initial nodes fully connected. Each time a new node is added, the new node a establishes m connections with existing nodes. The probability of a new node $a$ connecting to an existing node b is given by Eq. (4) [65]. 

$$
P _ {a \rightarrow b} = \alpha \left(k _ {b} + \varepsilon\right) F \left(d _ {a \rightarrow b}\right) = \frac {\left(k _ {b} + \varepsilon\right) F \left(d _ {a \rightarrow b}\right)}{\sum_ {l = 1} ^ {N (t)} F \left(d _ {a \rightarrow l}\right)\left(k _ {l} + \varepsilon\right)}, \tag {4}
$$

where $P _ { a  b }$ denotes the connection probability between the new node $a$ and the existing node b; α( .) denotes the distance influence factor; $k _ { b }$ represents the degree of the i-th node; $\varepsilon$ is a positive offset factor; and $N ( t )$ is the number of nodes in the network at time t; $F ( d _ { a  b } )$ denotes the connection probability function between the new node a and the existing node b; $F ( d _ { a  l } )$ denotes the connection probability function between the existing node a and the existing node $l ; k _ { l }$ denotes the degree of 

freedom of the l-th node. If $\begin{array} { r } { \sum _ { l = 1 } ^ { N ( t ) } F ( d _ { a  l } ) = 0 } \end{array}$ , the probability of all existing nodes being connected is zero, meaning the new node a cannot establish a connection with any existing node. In this case, node $a$ will remain active and attempt to connect again when new nodes are added. The analytical expression for the function $F ( d _ { a  b } )$ is given by Eq. (5) [65]. 

$$
F (d) = \left\{ \begin{array}{c c} 1 & d <   \alpha r _ {c} \\ \frac {\left(r _ {c} - d\right)}{\left(1 - \alpha\right) r _ {c}} & \alpha r _ {c} \leq d <   r _ {c}, \\ 0 & d \geq r _ {c} \end{array} \right. \tag {5}
$$

where $F ( d )$ represents the node connection probability; $r _ { c }$ is the node communication range radius; $d$ is the distance between nodes; and $\alpha$ is the distance influence factor. This process is repeated until the number of nodes reaches the network’s specified scale N. When a swarm fails or occurs external attack, it manifests as the removal of nodes and the disappearance of connections in IE network. The network possesses certain self-adaptive and self-recovery capabilities, enabling it to reestablish connections based on node positions and communication connection rules. The reconfiguration process of the IE network is shown in Fig. 1. 

When attempting to disintegrate dynamic network, it is found that the removal of nodes and node movements can lead to changes in network topology. The IE network can recover certain communication functions through reconfiguration, demonstrating resilience capacity. This resilience capability is also changing. The network topology after disintegration and reconstruction are illustrated in Fig. 2. 

# 3. Relative resilience model

Due to the inherent reconfiguration mechanisms of the dynamic network, reconstruction is activated. The network exhibits resilience, which is characterized by its ability to maintain functionality under disruptions [66]. Therefore, this section focuses on analyzing the relative resilience framework. 

# 3.1. Definition of relative resilience

Resilience is defined as the ability of a system to resist, absorb, adapt, and recover to its original state after being disturbed [47]. It centers on the entire resilience process, as shown in Fig. 3. Resilience is quantified and analyzed based on this process, characterizing the system’s recovery capability. Given that resilience is an inherent system attribute that can be measured at any moment, the concept of relative resilience is introduced. This concept captures the system’s capacity to resist, absorb, adapt to, and recover from disruptions at a specific moment in time, which represents the recovery level of the current state compared to a reference moment. 

Relative resilience captures the system’s relative to reference time, current, real-time resilience, focusing on the present moment rather than the entire process. Unlike traditional resilience assessments, relative resilience isolates the system’s resilience capability at a specific instant. It is in depends of its state in prior or subsequent moments. The simplified expression of relative resilience is as follows: 

$$
R _ {t _ {n}} ^ {\prime} = \frac {B}{A} = \frac {C p (t _ {n}) - C p (t _ {s})}{C p _ {\text {i n i}} - C p (t _ {s})}, \tag {6}
$$

where $C p _ { i n i }$ is the initial capacity of network, $C p ( t _ { s } )$ is the network capability at reference time $t _ { s }$ , $C p ( t _ { n } )$ is network capability at time $t _ { n }$ . The essence of relative resilience lies in its ability to reflect the system’s state before and after disturbances through its current performance value, reference performance value. The value of the simplified relative resilience is the ratio of two lines segments A and B, which is shown in Fig. 4. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/dc768f97dc989ccb41bc16057e379f90ec9ef043936fe4c0e8e3a730d533219e.jpg)



Fig. 1. Dynamic communication network reconfiguration algorithm flow.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/0b602d5650caa2712699d7cdfaf6a73dca31f3acf69fd3f69f1eb1f6b8cf0198.jpg)



(a) Initial Network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/dbe65bb934081e9abde954e7ecee178bcdf526db21b829cddca244f2f8b96d29.jpg)



(b) Disintegrated Network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/637a4e50fbab4d91db11763a1e4024e4349616d3b28491cba3ac906450bfab24.jpg)



(c) Reconfiguration Network



Fig. 2. The network before and after the reconfiguration.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/d30009d5e4bd7667618033ef886ca396ec40e4164a2ccba100c36598338c5601.jpg)



Fig. 3. The process of resilience.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/74dc1392b3169c9da7b596a6aae40d90b8c32627b474e3febf8754b41fc4e2d7.jpg)



Fig. 4. Simplified relative resilience.


Relative resilience has different values and meanings in different resilience stages. Therefore, time reference parameter γ and performance reference parameter $\delta$ are introduced. Specifically, γ captures the temporal relationship between the current time $t _ { n }$ , and the reference time $t _ { s }$ , allowing the resilience process to be divided into pre-disturbance 

and post-disturbance phases. δ reflects the performance change relative to the reference performance $C p ( t _ { s } )$ , enabling the identification of recovery or decline trends in system performance. The entire ductility process is divided into four regions, as shown in Fig. 5. 

Time reference parameter is 

$$
\gamma = \left\{ \begin{array}{l} 1, t _ {n} - t _ {s} > 0 \\ - 1, t _ {n} - t _ {s} <   0 \end{array} . \right. \tag {7}
$$

Performance reference parameter is 

$$
\delta = \left\{ \begin{array}{l} 1, C p \left(t _ {n}\right) - C p \left(t _ {s}\right) > 0 \\ - 1, C p \left(t _ {n}\right) - C p \left(t _ {s}\right) <   0 \end{array} . \right. \tag {8}
$$

In Fig. 5, different regions have different meanings of relative resilience, as follows: 

a) Region $\textcircled{1}$ (Positive values): The system is in the post-recovery phase. A larger value of relative resilience indicates better recovery at this moment. 

b) Region $\textcircled{2}$ (Positive values): The system is in the pre-decline phase. A larger value of relative resilience indicates smaller losses at that moment. 

c) Region $\textcircled{3}$ (Negative values): The system is in the pre-recovery phase. A larger negative value indicates higher relative resilience. 

d) Region $\textcircled{4}$ (Negative values): The system is in the post-decline phase. A larger negative value indicates higher relative resilience. 

The reference time $t _ { s }$ serves as a temporal baseline for comparative analysis of system performance across different time instances $t _ { n }$ . This temporal anchor helps systematic evaluation of resilience dynamics and quantitative assessment of system behavior relative to a predetermined operational state. The selection criteria for the reference time are contingent upon the specific application domain and the particular resilience phase under investigation. 

# 3.2. Comprehensive relative resilience

When considering the time scale and the rate of change at a specific moment, we introduced relative time parameter and rate parameter. The relative time, denoted as Δt, represents the difference between the relative resilience time and reference time. The rate parameter, denoted as $k$ , represents the slope of the curve at that point, describing the rate of change. The comprehensive relative resilience expression is given as follows: 

$$
R ^ {\prime} = \frac {B}{A} * \frac {1}{1 + e ^ {\eta t}} + \frac {1 - e ^ {- \xi k}}{2 (1 + e ^ {- \xi k})} = \frac {C p \left(t _ {n}\right) - C p \left(t _ {s}\right)}{C p _ {i n i} - C p \left(t _ {s}\right)} * \frac {1}{1 + e ^ {\eta t}} + \frac {1 - e ^ {- \xi k}}{2 \left(1 + e ^ {- \xi k}\right)}, \tag {9}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/09d4f14541dcb6670183c7c95c4380fb3de707f690b62d8746a42c45033b7470.jpg)



Fig. 5. Regions of relative resilience.


where $\textstyle { \frac { B } { A } }$ represents relative performance magnitude, $\frac { 1 } { 1 + e ^ { \eta t } }$ represents relative time, and 1− e− ξk $\frac { 1 - e ^ { - \xi k } } { 2 ( 1 + e ^ { - \xi k } ) }$ represents the rate of change. $C p ( t _ { n } )$ denotes the capacity at time $t _ { n } , C p ( t _ { s } )$ denotes the capacity at the reference time ts, $C p _ { i n i }$ denotes the capacity at the initial time. k denotes the rate parameter, $\pmb { k } = C p ^ { \prime } ( t _ { i } ) . \eta$ and $\xi$ denote scaling factors, and $\eta$ , $\xi \in \mathsf { \Gamma } ( 0 , 1 )$ . The scaling factors $\eta$ and $\xi$ can be adjusted through actual application scenarios and data to ensure that the model response is reasonable within the expected parameter range, consistent with actual conditions. 

Building upon Eqs. (6) and Eq. (9) incorporates additional factors such as relative time and rate of change to represents the comprehensive relative resilience, which makes it more applicable to complex and dynamic systems. The comprehensive relative resilience expression can be used to characterize the resilience capability of a system at a specific moment in terms of its resistance, absorption, adaptation, and recovery in the dimensions of performance, time, and rate of change. 

Henry et al. [51] analyze resilience as a time dependent function in the context of systems. They describe the metrics of network and system resilience, time for resilience and total cost of resilience. The model divides the resilience process into five phases and introduces a real-time resilience metric, which is as follows: 

$$
R (t | e ^ {j}) = \frac {\varphi (t | e ^ {j}) - \varphi (t _ {d} | e ^ {j})}{\varphi (t _ {0}) - \varphi (t _ {d} | e ^ {j})}, \tag {10}
$$

where $\varphi ( t | e ^ { j } )$ is the capacity of the system at t, $\varphi \big ( t _ { d } | e ^ { j } \big )$ is the lowest capacity of the system after disruption. $\varphi ( t _ { 0 } ) - \varphi \big ( t _ { d } \big | e ^ { j } \big )$ indicates the recovery degree of the system at t after recovery. $\varphi ( t | e ^ { j } ) - \varphi \big ( t _ { d } | e ^ { j } \big )$ indicates the degree of performance loss when the system is disturbed. This metric serves as a real-time resilience indicator that focuses on the recovery extent at a specific moment after the restoration process begins, disregarding intermediate performance evolution. Its validity has been verified in road network analyses. Given this foundation, the relative instantaneous resilience metric emphasizes a system’s resilience capability at an evaluation time relative to a reference time, without requiring complete resilience process data. 

Both Henry’s and the proposed resilience ignore intermediate resilience processes during disruptions and provide real-time resilience values. But, 

a) Henry’s resilience model examines performance values at three critical moments to characterize system resilience. In contrast, the relative resilience framework addresses scenarios with incomplete resilience data by focusing on performance values at three temporal nodes, namely initial time, reference time, and evaluation time. The relative resilience model allows the reference time to be freely chosen based on application scenarios. 

b) The Henry’s model requires predefined disturbance and recovery times, which may not be available in dynamic environments. The relative resilience model is designed to operate without complete resilience process data, making it more suitable for adversarial scenarios. 

c) The relative resilience model incorporates temporal efficiency and rate of change, providing a comprehensive view of the system’s dynamic characteristics. This multi-dimensional approach distinguishes it from Henry’s model, which primarily considers performance differences. 

The relative resilience represents an instantaneous resilience capacity relative to a specific reference time, which can be flexibly selected based on application contexts. When the reference time is set as the time of minimum resilience and the evaluation time corresponds to full recovery completion, this metric aligns precisely with the Henry resilience. 

Relative resilience lies in the ability to represent the system’s instantaneous resilience capacity relative to a reference time, even in the 

absence of a complete resilience process. It is expressed as the relative proportion of performance differences between the current and reference moments. It also incorporates the effects of time efficiency and the dynamics of change. In essence, relative resilience provides a snapshot of the system’s dynamic response, rather than a cumulative measure over time. The reference time can be defined according to specific requirements, allowing the calculated relative resilience to align with application needs. 

# 3.3. Relative resilience of dynamic communication network

For swarm dynamic IE networks, the inherent characteristics, dynamic edge reconfiguration and continuous structural evolution endow them with self-adaptive and self-recovery capabilities. Through simulation analysis, the network topology at each moment under dynamic motion is captured, and the number of connected components is quantified. The number of connected components is directly correlated with the network’s communication capability. A higher number of connected components indicates a more fragmented network, thereby reducing communication efficiency. Consequently, the number of connected components serves as a critical metric for assessing, providing valuable insights into its resilience and functionality. The communication capability of the network can be represented as follows: 

$$
C p ^ {C} = \frac {1}{L P}, \tag {11}
$$

where $L P$ means the number of connected components of the network. Based on it, the performance curve of the communication network can be obtained, as shown in Fig. 6. 

According to the relative resilience model, we consider relative time and perform normalization on Δt at the reference moment $t = 5$ . The relative resilience at various moments can be calculated, as shown in Fig. 7. 

It is observed that relative resilience fluctuates over time, due to node dynamics and network connection rules, which induce continuous structural changes. As a time-dependent network attribute, resilience evolves and is influenced by the choice of the reference moment. When t $= 5$ is selected as the reference moment, moment $t = 1 0$ exhibit high relative resilience values. This indicates that the network is in a more robust state during this moment compared to moment 5. 

This demonstrates that the network possesses self-adaptive and selfrecovery mechanisms. It is crucial to employ different strategies in combination with relative resilience for analysis and disintegrating. By targeting and reducing its performance resilience, the network’s recovery and adaptation capabilities can be degraded until it loses its selfrecovery capability, achieving complete disintegration beyond the threshold [66]. 

# 4. Disintegration model based on relative resilience

Network disintegration involves the strategic removal of specific nodes or edges to disrupt the topology, diminish functionality, or 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/b3047fe75835799ee9c83c2d0aa004db85c8206d2919ceeaf46f9a8b2bf34d7f.jpg)



Fig. 6. Performance curve of dynamic IE network.


interfere with behavior. Swarm UAVs exhibit a highly dynamic, variable, and adaptive nature, making their IE networks particularly challenging to disrupt. 

# 4.1. Algorithm for dynamic network based on closely connected group

In the IE network, the closely connected group refers to a node that shares more than $k _ { s }$ common neighbors with other nodes. $k _ { s }$ represents the minimum number of communication links between two nodes, also indicating that the two nodes have a significant number of common backup nodes. A node and other nodes with more than $k _ { s }$ common neighbors form a closely connected group. It is used as the dynamic network’s connection feature. As time progresses, the coordinates of network nodes change, leading to dynamic changes in the network topology. Consequently, the feature also undergoes dynamic changes. Due to the dynamic changes in the network topology, the network’s attribute, resilience, is also changing. The closely connected group is shown in Fig. 8. 

A dynamic swarm communication network disintegration algorithm is proposed based on “Disintegration algorithm based on closely connected group” [67]. This algorithm investigates the dynamic network’s weak bridge nodes, aiming to balance disintegration efficiency and cost. The algorithm process is shown in Fig. 9. According to this algorithm, weak nodes in the network can be identified. By targeting and removing nodes that act as topological bridges in communication, the network can be disintegrated. 

# 4.2. Disintegration model based on historical information and trend prediction

# 4.2.1. Historical information

The topology of IE network is evolving. It means that an attack at time t may have its impact diminished at the next moment, due to structural changes that repair the vulnerabilities caused by the attack. Although the network is in a state of continuous motion, its topology at each moment is fixed. The removal set can be determined based on the closely connected group at that specific moment. Since the network topology at each moment is related to the topology of previous moments, the removal set from earlier moments, along with targeted disintegration strategies, can serve as a reference for the current moment. The historical information in dynamic disintegration is shown as Fig. 10. 

By calculating the removal sets from historical moments, it can be used as a reference for formulating disintegration strategies at the attack moment. This historical information can optimize the proposed key node identification disintegration algorithm. Based on the above analysis, we propose a dynamic network disintegration method based on historical information, combining historical state information to determine the final removal set under dynamic conditions [68], which is as follows: 

$$
\frac {d S ^ {H} (t)}{d t} = S \left(A, \varphi , \delta_ {n} ^ {H}, \omega , t\right), \tag {12}
$$

where $S ^ { H } ( t )$ represents the disintegration removal set at time t based on historical information; $A ( t )$ represents the disintegration algorithm based on closely connected group; $\varphi$ indicates the network’s dynamic change frequency, reflecting the speed of network evolution over time; $\delta _ { n }$ represents the temporal step size of historical information, reflecting the span of historical data referenced, $\delta _ { n } ^ { H } = t _ { i - 1 } - t _ { i - n } ,$ , where $n$ indicates the size of the historical information span; $\omega$ represents the reference probability of historical information, reflecting the reliability of historical data. The function $S : S e t {  } S e t$ denotes a mapping from one set to another. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/534b42e88c5629ed6ac86b240621d1c7c759f8ce2b08116d634683d1f5a21419.jpg)



Fig. 7. Relative resilience of dynamic IE network.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/9255f27942e11d39580cd59379c583edeb184c6d1d3c245eb31420179f58b4e6.jpg)



(a)t=1


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/88cc3319121b01f6f3d67a71fa5901334ae4f5c26505d613f2c38105e5938dea.jpg)



(b)t=2



Fig. 8. Change of closely connected group.


$$
\omega_ {n} ^ {a} = \frac {\sum_ {t = t _ {i - n}} ^ {t = t _ {i - 1}} O _ {t} ^ {H} \left(v ^ {a}\right)}{\delta_ {n} ^ {H}}, \tag {13}
$$

$$
O _ {t _ {i - n}, t _ {i - 1}} ^ {H} \left(\nu^ {a}\right) = \left[ o _ {t _ {i - n}} ^ {H}, o _ {t _ {i - n + 1}} ^ {H}, o _ {t _ {i - n + 2}} ^ {H}, \dots , o _ {t _ {i - 1}} ^ {H} \right], \tag {14}
$$

$$
o _ {t _ {j}} ^ {H a} = \left\{ \begin{array}{c c} 1, & \text {a s r e m o v e d n o d e a t} t _ {j} \\ 0 & \text {e l s e} \end{array} , \right. \tag {15}
$$

where $o _ { t _ { j } } ^ { H a }$ denotes the label of the removed state of node $\nu ^ { a }$ at time $t _ { j } , t _ { j } \in$ $\left( t _ { i - n } , ~ t _ { i - 1 } \right)$ . 

$$
\operatorname {s e t} _ {n} ^ {a} = \left\{ \begin{array}{l l} 1, & \omega_ {n} ^ {a} \geq \omega_ {d} \\ 0 & \text {e l s e} \end{array} , \right. \tag {16}
$$

where $s e t _ { n } ^ { \mathrm { a } } = 1$ indicates that node $s e t _ { i j } ^ { \mathrm { a } } = 0$ is included in the removal set at that moment, and $s e t _ { i j } ^ { \mathrm { a } } = 0$ indicates that node a is not included in the removal set at that moment. For all nodes $\in V _ { i }$ , $\omega _ { i j } ^ { \mathrm { a } }$ represents the probability of node $\nu ^ { a }$ being part of the removal set during the time interval $[ t _ { i - n } , t _ { i - 1 } ]$ . A threshold $\omega _ { d }$ is applied to determine the final removal set. If a node’s removal probability exceeds $\omega _ { d }$ , it is considered to have a high probability of being removed in the historical information. The historical information-based disintegration removal set $S ^ { H } ( t _ { i } )$ at time $t _ { i }$ is 

$$
S ^ {H} \left(t _ {i}\right) = \left\{\nu^ {a}, \nu^ {b}, \nu^ {c}, \dots \dots \right\}, \tag {17}
$$

where $\nu ^ { i }$ is the node whose removal probability exceeds $\omega _ { d }$ 

The specific algorithm process is shown in the Appendix. 

# 4.2.2. Trend prediction in dynamic disintegration

The dynamic networks not only possess existing attributes but also exhibit a form of inertia. The structural changes follow certain trends, enabling anticipation of future network configurations. This predict-

ability allows for more informed and strategic interventions. Considering the potential future topologies of the network, an attack at time t may lead to changes in the network’s topology due to its inherent motion, enhancing or diminishing the disintegration effect. By analyzing the disintegration removal sets and effects of future moments, we can identify the optimal disintegration removal set at the current moment that maximizes future disintegration effectiveness. The trend prediction in dynamic disintegration is shown in Fig. 11. 

By calculating the removal sets and disintegration effects of subsequent moments, this information serves as predictive data for swarm disintegration. It provides a reference and supplement for the disintegration strategy at the attack moment. The disintegration method based on trend prediction as follows: 

$$
\frac {d S ^ {p} (t)}{d t} = S \left(A, \varphi , \delta_ {n} ^ {p}, \omega , t\right), \tag {18}
$$

where $S ^ { P } ( t )$ represents the disintegration removal set at time t based on predictive information; $A ( t )$ represents the disintegration algorithm based on closely connected group; $\varphi$ indicates the network’s dynamic change frequency, reflecting the speed of network evolution over time $\delta _ { n } ^ { P }$ represents the temporal step size of predictive information, reflecting the span of predictive data referenced, $\delta _ { n } = t _ { i + 1 } - t _ { i + n } , r$ n indicates the size of the predictive information span; $\omega$ represents the reference probability of predictive information, reflecting the reliability of predictive data. The function $S : S e t {  } S e t$ denotes a mapping from one set to another. 

$$
\omega_ {n} ^ {a} = \frac {\sum_ {t = t _ {i + 1}} ^ {t = t _ {i + n}} O _ {t} ^ {p} \left(v ^ {a}\right)}{\delta_ {n}}, \tag {19}
$$

$$
O _ {t _ {i + n}, t _ {i + 1}} ^ {P} \left(\nu^ {\alpha}\right) = \left[ o _ {t _ {i + 1}}, o _ {t _ {i + 2}}, o _ {t _ {i + 3}}, \dots , o _ {t _ {i + n}} \right], \tag {20}
$$

$$
o _ {t j} ^ {\mathrm {p a}} = \left\{ \begin{array}{c c} 1, & \text {a s r e m o v e d n o d e a t} t _ {j} \\ 0 & \text {e l s e} \end{array} , \right. \tag {21}
$$

where $o _ { t _ { j } } ^ { P a }$ denotes the label of the removed state of node $\nu ^ { a }$ at time $t _ { j }$ , $t _ { j } ~ \in ~ ( t _ { i + 1 } , ~ t _ { i + n } )$ . 

$$
\operatorname {s e t} _ {n} ^ {\mathrm {p a}} = \left\{ \begin{array}{l l} 1, & \omega_ {n} ^ {\mathrm {a}} \geq \omega_ {d} \\ 0 & \text {e l s e} \end{array} , \right. \tag {22}
$$

where $s e t _ { n } ^ { \mathrm { P a } } = 1$ indicates that node $\nu ^ { a }$ is included in the removal solution set at the current moment, $s e t _ { i j } ^ { \mathrm { a } } = 0$ indicates that node $\nu ^ { a }$ is not included in the removal solution set at that moment. Based on the predictive trend information, the removal set $S ^ { P } ( t _ { i } )$ at time $t _ { i }$ can be obtained as follows: 

$$
S ^ {p} \left(t _ {i}\right) = \left\{\nu^ {a}, \nu^ {b}, \nu^ {c}, \dots \dots \right\}, \tag {23}
$$

where $\nu ^ { i }$ represents the node whose removal probability exceeds $\omega _ { d }$ . The specific algorithm process is shown in the Appendix. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/e315a5b0a352bdd27467eb440e96aadd9c95e8c4875ecf478981ca79130a76af.jpg)



Fig. 9. Flow chart of dynamic network disintegrate algorithm [67].


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/732c4f934e6a7854c5b7ad143dc669f35d9e814dfbc08b09641e72e7b4ab7236.jpg)



Fig. 10. Historical information in dynamic disintegration.


# 4.3. Disintegration model based on relative resilience

When selecting nodes for removal during disintegration, one approach focuses on the occurrence probability of historical information, while the other considers the impact on subsequent communication performance. Neither approach addresses the resilience, which is crucial during network disintegration. As demonstrated in earlier studies of this paper, dynamic networks exhibit reconfiguration and reconstruction 

phenomena during motion and disintegration, leading to the recovery of network performance. Therefore, leveraging historical and predictive information, we propose a disintegration model based on relative resilience, which is shown in Fig. 12. 

The model is 

$$
\frac {d S ^ {R} (t)}{d t} = S \left(A, \varphi , \delta_ {n} ^ {R}, \overline {{R _ {\text {s e t} x} ^ {\prime}}}, t\right), \tag {24}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/f25c5f18ed26667ab726d762aa41b3f10f0140e4840fcffda7581b4ce889d0c9.jpg)



Fig. 11. Trend prediction in dynamic disintegration.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/02c7ed5be26e57f06cd9966deaa23417959ee646aba405bfbfc6d3e1784acc5b.jpg)



Fig. 12. Disintegration model based on relative resilience.


where $S ^ { P } ( t )$ represents the disintegration removal set at time t based on relative resilience; $A ( t )$ represents the disintegration algorithm based on closely connected group; $\varphi$ indicates the network’s dynamic change frequency, reflecting the speed of network evolution over time; $\delta _ { n } ^ { R }$ represents the temporal step size of predictive information, reflecting the span of predictive data referenced, $\delta _ { n } ^ { \mathrm { R } } = t _ { m a x } - t _ { m i n }$ . The function S : $S e t {  } S e t$ denotes a mapping from one set to another. $\overline { { R _ { s e t _ { x } } ^ { \prime } } }$ represents the average relative resilience after removing $n$ nodes from the $s e t _ { x }$ in the network. 

$$
R _ {i} ^ {\prime} \left(t _ {n}\right) = \frac {C p \left(t _ {n}\right) - C p \left(t _ {s}\right)}{C p _ {i n i} - C p \left(t _ {s}\right)} * \frac {1}{1 + e ^ {\eta t}} + \frac {1 - e ^ {- \xi k}}{2 \left(1 + e ^ {- \xi k}\right)}, \tag {25}
$$

which represents the network relative resilience at time $t$ after node $_ i$ is removed. 

$$
\overline {{R _ {s e t _ {x}} ^ {\prime}}} = \frac {\sum_ {t _ {\min }} ^ {t _ {\max }} R _ {s e t _ {x}} ^ {\prime} \left(t _ {i}\right)}{n} \tag {26}
$$

$\overline { { R _ { s e t _ { x } } ^ { \prime } } }$ denotes the average relative resilience after sequentially removing node sets $s e t _ { x }$ between $[ t _ { m i n } , t _ { m a x } ] . R _ { s e t _ { x } } ^ { ' } ( t _ { i } )$ denotes the relative resilience after removing node set $s e t _ { x }$ at $t _ { i }$ . When the average relative resilience of the network after node i is removed is lower than initial, the node is added to the removed node set. Finally, the average relative resilience of the network during the period after node set is removed is the lowest. 

$$
\overline {{R _ {\text {s e t} m} ^ {\prime}}} = \operatorname {M i n} \left\{\overline {{R _ {\text {s e t} 1} ^ {\prime}}}, \overline {{R _ {\text {s e t} 2} ^ {\prime}}}, \dots \dots \overline {{R _ {\text {s e t} x} ^ {\prime}}} \right\}, \tag {27}
$$

$\overline { { R _ { s e t _ { m } } ^ { \prime } } }$ represents the minimum mean of network relative resilience at time t after is removed. 

$$
s e t _ {m} = \arg \overline {{R ^ {\prime}}} _ {s e t _ {m}}.
$$

The removal set $S ^ { P } ( t _ { i } )$ based on the relative resilience at time $t _ { i }$ can be obtained as: 

$$
S ^ {R} \left(t _ {i}\right) = s e t _ {m}. \tag {28}
$$

The specific algorithm process is shown in the Appendix. 

Compared with other methods, this model is based on relative resilience, considering the network’s resilience throughout the disintegration process. It focuses not only on identifying key nodes within the network but also on evaluating the overall resilience of the network. It achieves a thorough and continuous decline in network performance, thereby accomplishing the goal of disintegration. 

# 5. Case study

This section aims to validate the aforementioned models through simulation analysis. The swarm consists of 50 UAVs tasked with reconnaissance missions in a specific area. The UAV swarm will adaptively adjust its configuration during operation. The capabilities and status of the UAVs are consistent. Each UAV corresponds to a node in swarm IE network. The communication range of the UAVs is limited and constrained by geographical distance. Communication only occurs within the communication range, forming the edges of the IE network. Based on the model established in Section 2 of this paper, a UAV swarm IE network model was developed to transmit relevant information and maintain communication, as shown in the Fig. 13. 

For dynamic swarm IE network A, the parameters are set as Table 3 [67]. 

In the network, nodes move along changing circular trajectories, with their velocity and direction varying at each time point. This type of motion is observed in vibration systems and dynamic equilibrium scenarios. The path of each node follows a circular trajectory with a radius that varies over time, determined by both time and frequency, and is controlled by sine and cosine functions with a frequency of $f$ . The timevarying radius is given as follows: 

$$
r (t) = 5 0 \left(1 - \cos \left(\frac {2 \pi t}{\frac {f}{1 0}}\right)\right), \tag {29}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/81725fef0d1a4d0a5f1987f463f5aeecba4b751824fd957d28f6af5b5172bf92.jpg)



(a) The UAV swarm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/906a657fa9dd54980ded98941f8b7058714c315b69c3968e910ae44e53d2781f.jpg)



(b) The swarm IE network.



Fig. 13. The Swarm and IE network of Case.



Table 3 Table of parameter.


<table><tr><td>Parameter</td><td>Meaning</td><td>Value</td></tr><tr><td>N</td><td>Network size</td><td>50</td></tr><tr><td>m0</td><td>Initial number of nodes</td><td>2</td></tr><tr><td>m</td><td>The number of edges of the newly added node</td><td>1</td></tr><tr><td>rc</td><td>Maximum communication distance between nodes</td><td>100</td></tr><tr><td>ε</td><td>Freedom index adjustment factor</td><td>1</td></tr><tr><td>η</td><td>Geographical distance index</td><td>1</td></tr></table>

where $r ( t )$ is the radius of the trajectory at time t, and $f$ is the frequency of change. The radius undergoes periodic changes with a period of $\frac { f } { 1 0 }$ frames. As time progresses, the radius varies between 0 and 50. The position of a node at time t is calculated as follows: 

$$
x _ {t} = x _ {0} + 5 * \cos (t * f), \tag {30}
$$

$$
y _ {t} = y _ {0} + 1 0 * \sin (t * f), \tag {31}
$$

where $\left( x _ { 0 } , \ y _ { 0 } \right)$ represents the initial coordinates. The terms cos(t ∗f) describe the offsets in the x and y directions, which vary with time. The network edge is connected according to the connection model of this paper. The performance and relative resilience of the dynamic network under different disintegration methods are analyzed. 

# 5.1. Analysis of original network

The network exhibits adaptive and self-recovery capabilities due to 

the dynamic movement of its nodes, dynamic reconfiguration of links, and the dynamic evolution of its topology. The network topology at various time points under network movement is obtained through simulation, and its connectivity is calculated, resulting in the performance curve, as shown in Fig. 14. (a). 

It can be observed that the network’s communication performance varies over time. The performance is relatively low during the time interval of 2 to 7, while it shows better performance at time points $t = 1 0$ and $t = 1 3 , 1 4 , 1 5$ . This variation might be attributed to the network’s self-adaptive characteristics adjusting. Additionally, significant fluctuations in performance are observed at certain time points, which could be related to the network’s inherent dynamic nature. Based on the relative resilience model, the time point $t = 5$ is selected as a reference moment, and the calculation of its relative resilience yields the results presented in the Fig. 14. (b). 

At time points with lower performance, the network’s relative resilience values are indeed smaller, or even are negative, indicating that the network’s resilience capability is low at those moments. Meanwhile, it is found that the network exhibits higher relative resilience values during the time interval of $t = 1 0 – 1 5$ , suggesting that the network’s resilience capability is better during this period. 

# 5.2. Disintegration method without information

Wang et al. [67] have demonstrated that the disintegration algorithm based on closed components swarms outperforms other disintegration strategies in static networks. We conducted simulation analyses using a degree-based disintegration strategy in this paper. At time $t = 5$ , 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/2a47aa0ee45b0cb17db84777f9a359d383ea202243e39d062e33a24fb25767a6.jpg)



(a) Capacity


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/ba5ac4c17f485c1f5b674d9d7171b4c859ec035581df7c530ad7171271933425.jpg)



(b) Relative resilience



Fig. 14. Original network.


the disintegration removal set obtained through the degree-based strategy for the swarm was $\{ 1 0 ~ 1 4 ~ 1 6 \}$ . The performance curve of the dynamic swarm, which is shown in Fig. 15. 

It reveals that the connectivity level of the swarm remained unchanged after the disintegration at $t = 5$ compared with original dynamic network. This phenomenon occurs because dynamic changes in swarm nodes and edges trigger structural reorganization, which offsets the impact of node removal through reconstruction and recovery. These results highlight the limitations of traditional static swarm disintegration methods in dynamic environments, such as degree-based strategies, where inherent adaptability diminishes the sustained effectiveness of targeted node removal. 

According to the dynamic network disintegration algorithm in Section 4.1 of this paper, the network is disintegrated at time $t = 5$ . It can be obtained that the sequence of nodes removed from the dynamic communication network at time $t = 5$ without information method is {13 34 47}. The change curve of network performance is shown in Fig. 16. (a). 

When a disintegrating attack is initiated at time $t = 5$ , the network performance decreases at subsequent time points $t = 6$ , 7, 8 and 9. However, the network demonstrates a certain recovery capability in the following time trend. According to the relative resilience model, it is calculated as Fig. 16. (b). 

The network’s ‘resilience capability’, as a network attribute, varies with time and is closely related to the selection of the reference moment. At time points $t = 7$ , 8, 9 and 10, the network exhibits high relative resilience values, indicating that the network is in a better recovery state during this period compared to $t = 5$ . This also suggests that the disintegration strategy without additional information has certain limitations. Therefore, it is essential to analyze the network based on relative resilience. By reducing its performance resilience, the network’s recovery and adaptive capabilities can be weakened until the network loses its self-recovery ability, achieving complete disintegration. 

# 5.3. Disintegration method with historical information and trend prediction

Based on the disintegration methods proposed in this paper, which consider historical information and trend prediction, we perform network disintegration at time $t = 5$ . Parameters are set as in Table 4. 

According to the model, the disintegrating removal solution sets considering historical information and prediction trend can be obtained as follows: 

$$
S ^ {H} = \{1 7 3 0 3 4 \}.
$$

$$
S ^ {p} = \{1 3 0 3 4 \}.
$$

The network performance curve is shown in Fig. 17 and Fig. 18. 

The three methods are compared and analyzed as Fig. 19. 

It can be observed that the disintegration method based on historical information leads to a significant decrease in network performance at 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/268d9138cd1fb454aa8b8943c25d3400b93f303c62ab61b5eb018c2530a93b74.jpg)



Fig. 15. Capacity of the disintegrated network through the degreebased strategy.


time points $t = 6 , 7 , 8 , 1 0$ , but the network shows a certain recovery trend in subsequent moments. On the other hand, the disintegration method based on predictive trends results in a noticeable decrease in network performance throughout the subsequent time intervals without any recovery trend, indicating the effectiveness of this method. 

Compared to the disintegration without information, both the disintegration methods based on historical information and predictive trends show improved disintegration effects. Compared to attacks based solely on the network topology at a specific moment, the disintegration strategies based on historical information and predictive trends can achieve more long-term impact. Such strategies result in more sustained disintegration effects. Consequently, these strategies demonstrate better performance in dynamic models, reducing disintegration costs and enhancing disintegration efficiency. Furthermore, the disintegration method based on predictive trends has a greater impact on the network in subsequent periods compared to the method based solely on historical information. 

# 5.4. Disintegration method based on relative resilience

According to the disintegration method based on relative resilience presented in Section 4.3. At $t = 5$ , the network is disintegrated. The remove solution set is 

$$
S ^ {R} = \{1 1 3 4 4 3 \}.
$$

The performance curve and relative resilience are shown in Fig. 20. 

When performing a disintegration attack based on relative resilience at time $t = 5$ , it is evident that compared to the scenario without any attack. There is a significant decrease in relative resilience across various time points. At time points $t = 7 , 8 , 9 , 1 0$ , both the performance values and relative resilience values show a marked decline. This indicates that the network’s recovery state during this period is relatively weaker compared to $t = 5$ . Furthermore, the performance consistently decreases at the disintegration moment and beyond, proving that the informed disintegration strategy is more effective and sustainable. 

# 5.5. Contrastive analysis

# 5.5.1. Different resilience models

When complete process information is available, it is possible to obtain the actual performance curve, capturing the entire resilience process. Under these considerations, we propose analyzing the dynamic information exchange network within the time interval of 1 to 10 moments, employing traditional resilience models for computation and analysis. The results reveal that, in the absence of external interference, the dynamic information interaction network exhibits a complete performance process curve, which is shown in Fig. 21. (a). 

According to Henry Resilience model [51] and Dynamic Resilience [57] model, we can get 

$$
R ^ {H e n r y} = \frac {0 . 5 - 0 . 3 3}{1 - 0 . 3 3} = 0. 2 5 3 7.
$$

$$
R ^ {\text {D y n a m i c}} = 0. 5 3 6 7.
$$

When disintegrate is based on relative resilience, its complete performance curve with full information is illustrated in Fig. 21. (b). Henry resilience value and Dynamic resilience value of the network under this disintegrate strategy are calculated as follows: 

$$
R _ {D R R} ^ {H e n r y} = \frac {0 . 3 3 - 0 . 2}{1 - 0 . 2} = 0. 1 6 2 5.
$$

$$
R _ {D R R} ^ {\text {D y n a m i c}} = 0. 4 1 8 4.
$$

When disintegrate is based on different resilience models, according to Henry resilience model, it is necessary to know the minimum performance value throughout the entire process. On this basis, at the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/6115f5f8c934527698e07103c745545939dc4734622f4266278690b3980f19ae.jpg)



(a) Capacity


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/9f10673934a873ae867bfa3369e88b7c2eceac6c5251127c4dd04bc0326e3ef7.jpg)



(b) Relative resilience



Fig. 16. Disintegrated network without information.



Table 4 Table of parameters.


<table><tr><td>Parameters</td><td>Value</td></tr><tr><td>Moment t</td><td>5</td></tr><tr><td>Temporal step size δ</td><td>4</td></tr><tr><td>Change frequency f</td><td>1</td></tr><tr><td>Reference probability ω</td><td>0.5</td></tr></table>

disintegrate moment $t = 5$ , the lower the performance value at this moment, the lower value of Henry resilience will be. Therefore, the disintegrate strategy based on Henry resilience model can be determined as follows: 

$$
S ^ {R _ {\text {H e n r y}}} = \{1 3 3 4 4 3 \}.
$$

Its complete performance curve with full information is illustrated in Fig. 21. (c). 

Henry resilience and Dynamic resilience of disintegrated network are 

$$
R _ {D H R} ^ {H e n r y} = \frac {0 . 3 3 - 0 . 2}{1 - 0 . 2} = 0. 1 6 2 5.
$$

$$
R _ {D H R} ^ {\text {D y n a m i c}} = 0. 4 2 3 5.
$$

Based on the dynamic resilience model, it is necessary to have complete information about the entire time period before the disintegration moment. On this basis, if the performance values are consistently low during that time period, the network’s resilience value will be lower. Therefore, the disintegration strategy based on dynamic resilience can be determined as follows: 

$$
S _ {D D R} ^ {R \text {D y n a m i c}} = \{3 0 3 4 4 3 \}.
$$

Its complete performance curve with full information is illustrated in Fig. 21. (d). 

Henry resilience and Dynamic resilience of disintegrated network are 

$$
R _ {M D} ^ {H e n r y} = \frac {0 . 3 3 - 0 . 2}{1 - 0 . 2} = 0. 1 6 2 5.
$$

$$
R _ {M D} ^ {\text {D y n a m i c}} = 0. 4 2 1 8.
$$

According to the calculation results, it is found that the Henry model focuses on the recovery level at a specific moment during the process. Dynamic resilience levels under different disintegration strategies exhibit similar characteristics. In comparison, relative resilience considers the performance at moments with known information prior to the disintegration moment. It indicates that disintegration strategies based on different resilience models can achieve the disintegration of information interaction networks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/5ce3cb12f375aec1114422d85cc1e19471210fa15f280c0c9218bbde5ee5286a.jpg)



Fig. 18. Capacity of the disintegrated network with trend prediction.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/a0824ca0808418e61a4e3110dd860a1cfdc6fbd66af8eed702a345b91ab96129.jpg)



Fig. 17. Capacity of the disintegrated network with historical information.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/e3bfdc50fe5cfdbfdc3070f4944b0cf787e233bde02f4a8135c755cd843fa043.jpg)



Fig. 19. Comparison of capacity $( C p _ { 1 }$ is the capacity of the disintegrated network without information, $C p _ { 2 }$ is the capacity of the disintegrated network with historical information, and $C p _ { 3 }$ is the capacity of the disintegrated network with trend prediction.).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/0f3e3dbe3c195b92f79f694cafece83110fe0a0dfae72365c2bc75cb3dde89b9.jpg)



(a) Capacity


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/3c14a077feda78923a7b472986b738802285ed00114b820fb8cd99115c2a0e63.jpg)



(b) Relative resilience



Fig. 20. Disintegrated network with relative resilience.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/3ef19c9a847d70fe6a0bec94de3b73dac4b6131031eb845a39000e2f356f5b43.jpg)



(a) Complete capacity curve of network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/ede896d32660c9540d0774e40d108803f77908f0c9cc96e0c4023572a2db624c.jpg)



(b) Disintegrated network with relative resilience


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/24cbfa3c1648ae3e8c1756dba4cf3181cc0eaa40de37acd0fff15353a9ee05fc.jpg)



(c) Disintegrated network with Henry resilience


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/1fbecc33fdce4df457ba961db26faf5c22680355546b2089d28ff3c5f25c2441.jpg)



(d) Disintegrated network with Dynamic resilience



Fig. 21. Complete capacity curve of networks.


When the resilience process is not available, meaning only partial steady-state performance values at specific moments are obtainable, as illustrated in Fig. 22. Only point values are obtainable. When $t = 6$ is the moment of lowest performance and $t = 1 0$ is the completion moment, the Henry resilience for the entire process can still be calculated. However, resilience values at other moments remain unavailable. Due to the lack of complete data, traditional time-integrated dynamic resilience cannot be computed. In this scenario, relative resilience enables the representation of network instantaneous resilience relative to a reference moment. 

# 5.5.2. Different indicators

5.5.2.1. Capacity. From the Fig. 23, it can be observed that compared to the dynamic communication network’s inherent performance curve, the performance of the network decreases under all four disintegration methods. The disintegration without additional information causes a significant decline in network performance at $t = 6 , 7 , 9$ , but the performance recovers to its original level in subsequent moments. 

When considering historical information for disintegration, the effect is improved compared to the no-information case, resulting in a performance decline. However, the network still exhibits a certain recovery trend afterward. In contrast, the disintegration method based on predictive trends shows advantages over the historical information approach by maintaining a sustained decline in performance during the subsequent time intervals. Furthermore, the disintegration method based on relative resilience demonstrates even more pronounced effects compared to the predictive trend method, achieving a continuous decline in network performance. 

5.5.2.2. Cost-effectiveness. During the disintegration process, it is essential to consider not only the effectiveness of disintegration but also the balance between disintegration effectiveness and cost. The costeffectiveness of removal is calculated for comparison, as shown below: 

$$
C = \frac {N _ {C}}{N _ {Y C}}, \tag {32}
$$

where $C$ represents the removal efficiency, $N _ { C }$ is the number of additional connected components resulting from a single simulation, and $N _ { Y C }$ is the number of vulnerable nodes removed in a single simulation. A higher C indicates that a significant disintegration effect can be achieved with low costs. 

The mean of cost-effectiveness of disintegration without information is 

$$
C _ {1} = 0. 0 8 3.
$$

The mean of cost-effectiveness of disintegration with historical information is 

$$
C _ {2} = 0. 1 2 5.
$$

The mean of cost-effectiveness of disintegration with trend prediction is 

$$
C _ {3} = 0. 2 2 9.
$$

The mean of cost-effectiveness of disintegration with relative resilience is 

$$
C _ {4} = 0. 2 9 2.
$$

It can be observed that the disintegration method based on relative resilience demonstrates a higher cost-effectiveness, indicating that this method achieves better disintegration results with lower costs. Disintegration based on relative resilience not only achieves continuous and thorough performance degradation but also balances the cost and effectiveness of disintegration. 

5.5.2.3. Relative resilience. From the Fig. 24, it can be observed that compared to the network’s inherent relative resilience capability, the network’s relative resilience capability decreases after implementing disintegration based on relative resilience, even reaching negative or zero values. 

This indicates that the disintegration method indeed impacts the resilience capability. The introduction of a relative time scale leads to changes in the magnitude of resilience values. Moments farther away from the reference time require longer periods for the same level of performance change, resulting in smaller calculated relative resilience values. It will be better to capture the nuanced changes by amplifying the time sensitivity. 

# 5.5.3. Different times

5.5.3.1. Reference time=6. When the reference time is set to $t = 6$ , the relative instantaneous resilience is compared across different failure strategies as follows. 

From the Fig. 25, it can be observed that when the reference time changes, the value of the network’s relative resilience also changes. Since the performance level at time $t = 6$ is lower than that at time $t = 5$ , the overall level of relative resilience has increased, indicating that the network’s resilience capacity is better relative to time $t = 6$ . 

1) The trend of relative resilience remains unchanged. The network exhibits a favorable recovery trend during the later time frame. 

2) For the network’s own relative resilience, the level remains high during time $t = 1 1 \mathrm { - } 1 5$ . 

3) Compared to the no-information strategy, the disintegration strategy based on relative resilience still shows a significant effect in reducing the network’s relative instantaneous resilience. 

5.5.3.2. Disintegration time ${ } = { } 1 0$ . Experiments were conducted at $T = 1 0$ and on different network configurations, yielding consistent results that validate the method’s effectiveness. The disintegration strategy without 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/10c15883d884a7b9f7581da62f0802f1229da423692ca9d3b3b8ab20b828d109.jpg)



Fig. 22. Complete information versus incomplete information.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/d51b43a9b8b0a78c9e5050c4747740196f2da4347a18694a5f0950e1c38be1b1.jpg)



Fig. 23. Comparation of capacity $\mathrm { C } p _ { 0 }$ is the capacity of the original network, $C p _ { 1 }$ is the capacity of the disintegrated network without information, $C p _ { 2 }$ is the capacity of the disintegrated network with historical information. $C p _ { 3 }$ is the capacity of the disintegrated network with trend prediction and $C p _ { 4 }$ is the capacity of the disintegrated network with relative resilience).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/787f7a21c988bc6a77e6b624e4af2651c9f2922fe22e2e9c0c0285ae7c9faaf0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/6bdd87d1e3b62c27da2a36caabb58c0d97c5dcbee3834b816f78e3d82587b0ab.jpg)



Fig. 24. Comparation of relative resilience of original and disintegrated networks.


information can be determined as follows: 

$$
S ^ {N o N} = \{2 1 3 1 7 \}.
$$

The disintegration strategy with historical information can be determined as follows: 

$$
S ^ {H i s} = \{1 1 3 4 3 3 \}.
$$

The disintegration strategy with trend prediction can be determined as follows: 

$$
S ^ {P r e} = \{1 4 3 4 \}.
$$

The disintegration strategy relative resilience can be determined as follows: 

$$
S ^ {R R} = \{4 1 4 3 1 1 \}.
$$

The performance and relative resilience of the network after disintegration under different disintegration strategies at the moment $T = 1 0$ changes as shown in Fig. 26, 

It can be seen that the disintegration method based on relative toughness is still able to deal a sustained blow to this dynamic adaptive network due to other methods. This also reaffirms the validity of the model proposed in this paper. 

# 5.5.4. Different networks

In order to further verify the applicability of the present model, we conducted experiments on different networks for an extended period of time. The disintegration is performed at the moment $T = 5$ and the relevant results as well as the analysis are as shown in Fig. 27. 

Among them, Network A simulates a swarm communication network with high volatility, and the related parameter settings are shown in 

Table 3. Network B simulates a dynamic network with minor periodic changes, and has a certain degree of volatility. Network C simulates a stable network with continuous and stable network performance. From Fig. 27, it can be seen that in different networks, the relative resiliencebased disintegration method can cause persistent degradation of network performance and outperforms other methods to realize effective and continuous disintegration of dynamic networks. 

# 5.5.5. Different disintegration methods

We apply different disintegration methods to network A at time $T = 5$ to validate effectiveness of the model this paper proposed. FINDER [37] is a reinforcement learning-based disintegration method that performs well in static networks by identifying critical node. According to FINDER, the disintegration strategy is 

$$
S ^ {F I N D E R} = \{1 0 1 4 1 6 \}.
$$

Percolation theory [33] is applied to network theory to describe the phenomenon of phase change in network connectivity with the removal of nodes or edges, and the threshold at which the network loses connectivity is called the percolation threshold. According to percolation theory, the disintegration strategy is 

$$
S ^ {P r e} = \{1 0 1 4 1 6 \}.
$$

According to disintegration model based on relative resilience, the disintegration strategy is 

$$
S ^ {R R} = \{1 1 3 4 4 3 \}.
$$

After disintegration at the moment $T = 5$ , the performance of the network changes as Fig. 28. 

According to the above analysis, for dynamic networks, percolation 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/d0961f5da41ca80967cb625d70b4929b689d59e8a38c7e729b7489e347d2587a.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/65d7a5fcf698e82f65797eb3bd7525514463aef978c015d319afb40d4beef0c8.jpg)



(a) Relative resilience of the original network when reference time $t _ { s } = 5$ vs $t _ { s } = 6$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/25b7bcacaa807be9d6e5a5bdadd48c289014872855c2a0d9a522e34553568528.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/27ed1728df4977c3f431135037ea758e03c4d6002ac940ae5a88f523505f6bbb.jpg)



(b) Relative resilience of the disintegrated network when reference time $t _ { s } = 5$ vs $t _ { s } = 6$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/4b88c211c75d867211e71c005ea0b5221a36f56c5994b3d4496d29ff63168a0f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/45b19fd212a82e40c46c2ac5319d1a86d1df6da82eb01e308f882c8e6a10c6eb.jpg)



(c) Relative resilience of the disintegrated network with $R ^ { \prime }$ when reference time ts = 5 vs ts = 6



Fig. 25. Comparation of relative resilience when reference time $t _ { s } = 5$ & $t _ { s } = 6$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/8a3efc727313da6943aa775c5f9b9677c896cddc481bc65813775b225ab54b5c.jpg)



(a) Capacity curve


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/7ca231d92ba7a74ce5ae9549fa3c29abeac10652603a60838141be1f20d5bd9b.jpg)



(b)Relative resilience of initial network


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/e6dda77c3005d3864e6eef1cbc2dde0adcfb88c49a096b44b21839fe43b18a8c.jpg)



(c) Relative resilience of disintegrated network with information


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/5915526a891d7e65b7e4626a6fc36df2510a2399683bd07cecd92d78cabe76d0.jpg)



(d) Relative resilience of disintegrated network with relative resilience



Fig. 26. Comparation of different disintegration methods when disintegration time $\mathbf { t } = 1 0$ .



(a) Network A


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/dd33119fb5739b065854f3eeb809a75a43604215926c2808dfdbbc13cfe96fa5.jpg)



(b) Network B


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/80f3667b60848de37d9211631609cd1f95141c356d84ceec4f819e8279453145.jpg)



(c) Network C


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/ab42e18134f61d7a70ea8815771f022642fd12dda5817d3a01dcbd7e9cc0f59e.jpg)



Fig. 27. Capacity curve of different networks with different disintegration method.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/88056851-ca86-432b-90cf-95773e84f4f1/dad5757a162a09736b2bdeae56d3d21229ed7671288bc79c7f26c78e3c8a9d59.jpg)



Fig. 28. Comparation of capacity with different disintegration methods.


disintegration method has some limitations for the object of this paper, the dynamic swarm IE network. Meanwhile, the percolation theory pays more attention to the threshold of network disintegration, while the method proposed in this paper pays more attention to the method of disintegration. Meanwhile, it is found that the existing reinforcement learning methods are weak for dynamic reconnectable swarm IE network. The blow caused is short-lived and can be replied by its own adaptive adjustment. In that case, the dynamic disintegration method based on relative toughness proposed in this paper has certain advantages. Meanwhile, in the process of analysis, it is found that the disintegration efficiency can be effectively improved by integrating the dynamic reconnection feature into the reinforcement learning modeling. 

In conclusion, the disintegration strategy based on relative resilience exerts a certain temporal influence on the network. It gains an advantage in the dynamic balance between the network’s inherent recovery capability and the damage caused by the attack. This suggests that incorporating relative resilience into the analysis is effective. By 

reducing its performance resilience, the network’s recovery and adaptive capabilities can be weakened until the network loses its selfrecovery ability, achieving complete disintegration. 

# 6. Conclusions

This study addresses the high dynamics and self-recovery characteristics of swarm dynamic IE networks by proposing a dynamic network disintegration model based on relative resilience. By defining relative resilience and constructing a comprehensive evaluation index, the study quantifies the network’s immediate recovery capability when subjected to attacks. Simulation results demonstrate that, compared to traditional static disintegration methods, the dynamic disintegration strategy based on relative resilience reduces network performance, enhances costeffectiveness, and suppresses the network’s adaptive reconfiguration. The strategy based on historical information reduces redundant attacks by excavating the criticality of nodes in time series, while the trend prediction strategy achieves proactive strikes by predicting future topological changes. Additionally, the relative resilience model reveals the coupling relationship between network performance and time sensitivity, providing a new perspective for real-time assessment of dynamic networks. 

The UAV swarm serves as a representative example of dynamic networks with self-recovery and adaptive characteristics. The methodology presented in this work can be generalized and applied to other network systems that exhibit similar properties, including high dynamics, autonomous reconfiguration capabilities, and self-recovery mechanisms. For example, in power systems, relative resilience can guide decisions on whether to activate backup power sources or adjust loads, enabling real-time monitoring of grid node relative resilience and rapid identification of vulnerable links. Future research will explore the broader applicability of this framework to diverse network types with adaptive behaviors. 

Future work will focus on expanding the applicability of the relative resilience-based disintegration method to other types of dynamic networks beyond UAV swarms. Next, we plan to incorporate reinforcement learning theory into our framework to develop intelligent disintegration strategies, potentially improving disintegration efficiency and reducing computational overhead. Furtherly, we will explore the integration of percolation theory to identify critical thresholds for dynamic network disintegration. 

# Author statement

Yawen Zhu conceived and designed the methodology and model; Guanghan Bai proposed the idea of this paper and designed the experiments; Zhan Xu supervised the model; Louzhaohan Wang coded the algorithms; Bei Xu analyzed the data. All authors have contributed to the editing and proofreading of this paper. 

# CRediT authorship contribution statement

Yawen Zhu: Writing – review & editing, Writing – original draft, Visualization, Validation, Methodology, Formal analysis, Conceptualization. Guanghan Bai: Visualization, Validation, Methodology, Funding acquisition, Formal analysis, Conceptualization. Zhan Xu: Visualization, Supervision, Resources, Project administration, Methodology. Louzhaohan Wang: Writing – original draft, Validation, Methodology, Data curation, Conceptualization. Bei Xu: Validation, Supervision, Methodology, Funding acquisition. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgments

This work was supported in part by the National Natural Science Foundation of China under Grant 72271242 and in part by the National Natural Science Foundation of China under Grant 72461026, the Province Department of Education Key Science and Technolog, China, under Grant GJJ220112. 

# Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.ress.2025.111745. 

# Data availability

Data will be made available on request. 

# References



[1] Liu T, Bai G, Tao J, Zhang Y-A, Fang Y. A multistate network approach for resilience analysis of UAV swarm considering information exchange capacity. Reliab Eng Syst Saf 2024;241:109606. https://doi.org/10.1016/j. ress.2023.109606. 





[2] Feng Q, Liu M, Dui H, Ren Y, Sun B, Yang D, et al. Importance measure-based phased mission reliability and UAV number optimization for swarm. Reliab Eng Syst Saf 2022;223:108478. https://doi.org/10.1016/j.ress.2022.108478. 





[3] Li H, Sun Q, Zhong Y, Huang Z, Zhang Y. A soft resource optimization method for improving the resilience of UAV swarms under continuous attack. Reliab Eng Syst Saf 2023;237:109368. https://doi.org/10.1016/j.ress.2023.109368. 





[4] Boccaletti S, Latora V, Moreno Y, Chavez M, Hwang d-U. Complex networks: structure and dynamics. Phys Rep 2006;424:175–308. https://doi.org/10.1016/j. physrep.2005.10.009. 





[5] Deng Y, Wang Z, Xiao Y, Shen X, Kurths J, Wu J. Spatial network disintegration based on spatial coverage. Reliab Eng Syst Saf 2025;253:110525. https://doi.org/ 10.1016/j.ress.2024.110525. 





[6] Qi M, Deng Y, Deng H, Wu J. Optimal disintegration strategy in multiplex networks. Chaos 2018;28. https://doi.org/10.1063/1.5078449. N.PAG-N.PAG. 





[7] Morone F, Makse HA. Influence maximization in complex networks through optimal percolation. Nature 2015;524:65–8. https://doi.org/10.1038/ nature14604. 





[8] Artime O, Grassia M, De Domenico M, Gleeson JP, Makse HA, Mangioni G, et al. Robustness and resilience of complex networks. Nat Rev Phys 2024;6:114–31. https://doi.org/10.1038/s42254-023-00676-y. 





[9] Lalou M, Tahraoui MA, Kheddouci H. The Critical node detection Problem in networks: a survey. Comput Sci Rev 2018;28:92–117. https://doi.org/10.1016/j. cosrev.2018.02.002. 





[10] Braunstein A, Dall’Asta L, Semerjian G, Zdeborov´a L. Network dismantling. Proc Natl Acad Sci 2016;113:12368–73. https://doi.org/10.1073/pnas.1605083113. 





[11] Estrada E, Rodríguez-Velazquez ´ JA. Subgraph centrality in complex networks. Phys Rev E 2005;71:056103. https://doi.org/10.1103/PhysRevE.71.056103. 





[12] Wandelt S, Lin W, Sun X, Zanin M. From random failures to targeted attacks in network dismantling. Reliab Eng Syst Saf 2022;218:108146. https://doi.org/ 10.1016/j.ress.2021.108146. 





[13] Morone F, Makse HA. Influence maximization in complex networks through optimal percolation. Nature 2015;524:65–8. https://doi.org/10.1038/ nature14604. 





[14] Albert R, Jeong H, Barab´asi A-L. Error and attack tolerance of complex networks. Nature 2000:406:378-82.https://doi.0rg/10.1038/35019019. 





[15] Deng Y, Wu J, Xiao Y, Li Y. Efficient disintegration strategies with cost constraint in complex networks: the crucial role of nodes near average degree. Chaos Woodbury N 2018;28:061101. https://doi.org/10.1063/1.5029984. 





[16] Holme P, Kim BJ, Yoon CN, Han SK. Attack vulnerability of complex networks. Phys Rev E 2002;65:056109. https://doi.org/10.1103/PhysRevE.65.056109. 





[17] Carmi S, Havlin S, Kirkpatrick S, Shavitt Y, Shir E. A model of internet topology using k-shell decomposition. Proc Natl Acad Sci 2007;104:11150–4. https://doi. org/10.1073/pnas.0701175104. 





[18] Freeman L. A set of measures of centrality based on betweenness. Sociometry 1977; 40:35–41. https://doi.org/10.2307/3033543. 





[19] Grassia M, De Domenico M, Mangioni G. Machine learning dismantling and earlywarning signals of disintegration in complex systems. Nat Commun 2021;12:5190. https://doi.org/10.1038/s41467-021-25485-8. 





[20] Jiang W, Li P, Fan T, Li T, Zhang C, Zhang T, et al. Scalable rapid framework for evaluating network worst robustness with machine learning. Reliab Eng Syst Saf 2024;252:110422. https://doi.org/10.1016/j.ress.2024.110422. 





[21] Wang Z, Deng Y, Holme P, Di Z, Lü L, Wu J. Cost-effective network disintegration through targeted enumeration. IEEE Trans Syst Man Cybern Syst 2024;54: 7657–69. https://doi.org/10.1109/TSMC.2024.3454780. 





[22] Shen X, Wang Z, Deng Y, Wu J. Spatial network disintegration with heterogeneous cost. Chaos Solitons Fractals 2024;187:115414. https://doi.org/10.1016/j. chaos.2024.115414. 





[23] Deng Y, Wu J, Xiao Y, Zhang M, Yu Y, Zhang Y. Optimal disintegration strategy with heterogeneous costs in complex networks. IEEE Trans Syst Man Cybern Syst 2020;50:2905–13. https://doi.org/10.1109/TSMC.2018.2832238. 





[24] Jia C-X, Liu R-R. Cascading dynamics in double-layer hypergraphs with higherorder inter-layer interdependencies. Reliab Eng Syst Saf 2025;257:110841. https:// doi.org/10.1016/j.ress.2025.110841. 





[25] Dui H, Zhai J, Fu X. Attack strategies and reliability analysis of Wireless Mesh Networks considering cascading failures. Reliab Eng Syst Saf 2025;257:110832. https://doi.org/10.1016/j.ress.2025.110832. 





[26] Musciotto F, Miccich`e S. Exploring the landscape of dismantling strategies based on the community structure of networks. Sci Rep 2023;13:14448. https://doi.org/ 10.1038/s41598-023-40867-2. 





[27] Wang Z, Su Z, Deng Y, Kurths J, Wu J. Spatial network disintegration based on kernel density estimation. Reliab Eng Syst Saf 2024;245:110005. https://doi.org/ 10.1016/j.ress.2024.110005. 





[28] Dong G, Luo Y, Liu Y, Wang F, Qin H, Vilela ALM. Percolation behaviors of a network of networks under intentional attack with limited information. Chaos Solitons Fractals 2022;159:112147. https://doi.org/10.1016/j. chaos.2022.112147. 





[29] Duan Y, Huang J, Deng H, Ni X. Robustness of hypergraph under attack with limited information based on percolation theory. Chaos Solitons Fractals 2024;188: 115518. https://doi.org/10.1016/j.chaos.2024.115518. 





[30] Zdeborov´a L, Zhang P, Zhou H-J. Fast and simple decycling and dismantling of networks. Sci Rep 2016;6:37954. https://doi.org/10.1038/srep37954. 





[31] Qi M, Chen P, Liang Y, Li X, Deng H, Duan X. Multi-objective disintegration of multilayer networks. Reliab Eng Syst Saf 2025;260:111042. https://doi.org/ 10.1016/j.ress.2025.111042. 





[32] Altarelli F, Braunstein A, Dall’Asta L, Zecchina R. Large deviations of cascade processes on graphs. Phys Rev E 2013;87:062115. https://doi.org/10.1103/ PhysRevE.87.062115. 





[33] Morone F, Makse HA. Influence maximization in complex networks through optimal percolation. Nature 2015;524:65–8. https://doi.org/10.1038/ nature14604. 





[34] Deng Y, Wu J, Qi M, Tan Y. Optimal disintegration strategy in spatial networks with disintegration circle model. Chaos Interdiscip J Nonlinear Sci 2019;29: 061102. https://doi.org/10.1063/1.5093201. 





[35] Deng Y, Wu J, Tan Y. Optimal attack strategy of complex networks based on tabu search. Phys Stat Mech Its Appl 2016;442:74–81. https://doi.org/10.1016/j. physa.2015.08.043. 





[36] Ventresca M. Global search algorithms using a combinatorial unranking-based problem representation for the critical node detection problem. Comput Oper Res 2012;39:2763–75. https://doi.org/10.1016/j.cor.2012.02.008. 





[37] Fan C, Zeng L, Sun Y, Liu Y-Y. Finding key players in complex networks through deep reinforcement learning. Nat Mach Intell 2020;2:317–24. https://doi.org/ 10.1038/s42256-020-0177-2. 





[38] Wang Z, Deng Y, Wang Z, Kurths J, Wu J. Efficient link-based spatial network Disintegration strategy. IEEE Trans Netw Sci Eng 2025;12:1096–111. https://doi. org/10.1109/TNSE.2024.3523952. 





[39] Saif M, Javad-Kalbasi M, Valaee S. Effectiveness of reconfigurable intelligent surfaces to enhance connectivity in UAV networks. IEEE Trans Wirel Commun 2024;23:18757–73. https://doi.org/10.1109/TWC.2024.3476422. 





[40] Ghanem M, Magnien C, Tarissan F. Centrality metrics in dynamic networks: a comparison study. IEEE Trans Netw Sci Eng 2019;6:940–51. https://doi.org/ 10.1109/TNSE.2018.2880344. 





[41] Liu X, Peng H, Gao J. Vulnerability and controllability of networks of networks. Chaos Solitons Fractals 2015;80:125–38. https://doi.org/10.1016/j. chaos.2015.08.009. 





[42] Duan Dongli, Lv Changchun, Si Shubin, Wang Zhen, Li Daqing, Gao Jianxi, et al. Universal behavior of cascading failures in interdependent networks: proceedings of the National Academy of Sciences of the United States of America. Proc Natl Acad Sci U S A 2019;116:22452–7. https://doi.org/10.1073/pnas.1904421116. 





[43] Hausken K, Welburn JW, Zhuang J. A review of game theory and risk and reliability analysis in infrastructures and networks. Reliab Eng Syst Saf 2025;261: 111123. https://doi.org/10.1016/j.ress.2025.111123. 





[44] Pan X, Guo Z. Dynamic resilience in complex networks. Chaos Solitons Fractals 2025;196:116369. https://doi.org/10.1016/j.chaos.2025.116369. 





[45] Zhou J, Coit DW, Felder FA, Wang D. Resiliency-based restoration optimization for dependent network systems against cascading failures. Reliab Eng Syst Saf 2021; 207:107383. https://doi.org/10.1016/j.ress.2020.107383. 





[46] Liu X, Li D, Ma M, Szymanski BK, Stanley HE, Gao J. Network resilience. Phys Rep 2022;971:1–108. https://doi.org/10.1016/j.physrep.2022.04.002. 





[47] Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Evol Syst 1973;4:1–23. https://doi.org/10.1146/annurev.es.04.110173.000245. 





[48] Duan D, Zhao X, Cai Z, Wang N. Resilience prediction and tipping point control of multilayer ecological networks based on dimensionality reduction method. Chaos Solitons Fractals 2025;191:115914. https://doi.org/10.1016/j. chaos.2024.115914. 





[49] Bruneau M, Chang SE, Eguchi RT, Lee GC, O’Rourke TD, Reinhorn AM, et al. A framework to quantitatively assess and enhance the seismic resilience of communities. Earthq Spectra 2003;19:733–52. https://doi.org/10.1193/ 1.1623497. 





[50] Zobel CW. Representing perceived tradeoffs in defining disaster resilience. Decis Support Syst 2011;50:394–403. https://doi.org/10.1016/j.dss.2010.10.001. 





[51] Henry D, Emmanuel Ramirez-Marquez J. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99: 114–22. https://doi.org/10.1016/j.ress.2011.09.002. 





[52] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35–53. https://doi. org/10.1016/j.ress.2016.08.013. 





[53] Tran HT, Balchanos M, Domerçant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng Syst Saf 2017;158:73–84. https://doi.org/10.1016/j.ress.2016.10.014. 





[54] Zeng Z, Fang Y-P, Zhai Q, Du S. A Markov reward process-based framework for resilience analysis of multistate energy systems under the threat of extreme events. Reliab Eng Syst Saf 2021;209:107443. https://doi.org/10.1016/j. ress.2021.107443. 





[55] Bai G, Fang Y;, Liu T, Tao J, Zhang Y-A. Mission-oriented resilience evaluation method for complex system. Syst Eng Ele 2021;43:1003–11. https://doi.org/ 10.12305/j.issn.1001-506X.2021.04.17. 





[56] Wang S, Wang J, Luan S, Song B. Deep sparse autoencoders-based community detection and resilience analysis of interdependent infrastructure networks. Chaos Solitons Fractals 2024;189:115720. https://doi.org/10.1016/j. chaos.2024.115720. 





[57] Zhang C, Liu T, Bai G, Tao J, Zhu W. A dynamic resilience evaluation method for cross-domain swarms in confrontation. Reliab Eng Syst Saf 2024;244:109904. https://doi.org/10.1016/j.ress.2023.109904. 





[58] Dui H, Zhu Y, Tao J. Multi-phased resilience methodology of urban sewage treatment network based on the phase and node recovery importance in IoT. Reliab Eng Syst Saf 2024;247:110130. https://doi.org/10.1016/j.ress.2024.110130. 





[59] Zobel CW. Representing perceived tradeoffs in defining disaster resilience. Decis Support Syst 2011;50:394–403. https://doi.org/10.1016/j.dss.2010.10.001. 





[60] Tan S-Y, Wu J, Lü L, Li M-J, Lu X. Efficient network disintegration under incomplete information: the comic effect of link prediction. Sci Rep 2016;6:22916. https://doi.org/10.1038/srep22916. 





[61] Zheng Z, Sangaiah AK, Wang T. Adaptive communication protocols in flying ad hoc network. IEEE Commun Mag 2018;56:136–42. https://doi.org/10.1109/ MCOM.2017.1700323. 





[62] Bakhtiari S, Najafi MR, Goda K, Peerhossaini H. A dynamic Bayesian network approach to characterize multi-hazard risks and resilience in interconnected critical infrastructures. Reliab Eng Syst Saf 2025;257:110815. https://doi.org/ 10.1016/j.ress.2025.110815. 





[63] Watts DJ, Strogatz SH. Collective dynamics of ‘small-world’ networks. Nature 1998;393:440–2. https://doi.org/10.1038/30918. 





[64] Albert R, Jeong H, Barabasi ´ A-L. Diameter of the world-wide web. Nature 1999; 401:130-1.https://doi.org/10.1038/43601 





[65] Bai G, Li Y, Fang Y, Zhang Y-A, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020; 193:106602. https://doi.org/10.1016/j.ress.2019.106602. 





[66] Mumby PJ, Hastings A, Edwards HJ. Thresholds and the resilience of Caribbean coral reefs. Nature 2007;450:98–101. https://doi.org/10.1038/nature06252. 





[67] Wang L, Huang Y, Dai H, Bai G, Tao J. A simple algorithm for disintegrating information exchange network of UAV swarm. In: 2023 9th Int. Symp. Syst. Secur. Saf. Reliab. ISSSR. IEEE; 2023. p. 414–9. https://doi.org/10.1109/ ISSSR58837.2023.00067. 





[68] Barzel B, Liu Y-Y, Barabasi ´ A-L. Constructing minimal models for complex system dynamics. Nat Commun 2015;6:7186. https://doi.org/10.1038/ncomms8186. 

