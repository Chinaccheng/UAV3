# Resilience evaluation of UAV swarm considering resource supplementation

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/c7e65e511c07fc69e11f84c7dd0b11116428ec54127334affdab35a278ca1db9.jpg)


Linghao Kong, Lizhi Wang, Zhongzheng Cao, Xiaohong Wang 

# ARTICLEINFO

Keywords: 

Resilience evaluation 

Swarm 

UAV 

Resource supplementation 

Complex network 

# ABSTRACT

In open-resource environments, unmanned aerial vehicle (UAV) swarms typically dynamically supplement and replace UAVs in the event of mission loss. During this process, there is a high degree of uncertainty and volatility regarding mission reliability. Solving the problem of resilience evaluation of the multidimensional characteristics of UAV swarms under resource supplementation is important to ensure the highly reliable operation of UAV swarms. In this study, we examined the impact of resource supplementation on the resilience of UAV swarms with respect to the resilience characteristics associated with the multidimensional topological features of the swarm. The mathematical concept of resilience and the specific characteristics of the UAV swarm were analyzed. By combining the two, a three-layer metric framework for UAV swarm resilience evaluation was proposed. On this basis, by considering the impact of resource supplementation, a resilience evaluation method was established using the theories of complex networks, flow networks, and multi-agent system simulation. Finally, a comparative and orthogonal-experiment case study was conducted with a UAV swarm confrontation scenario. The important factors and optimal benefits of the resilient recovery were analyzed based on the quantity, speed, and threshold of resource supplementation to guide the use of UAV swarms. 

# 1. Introduction

Due to high spatiotemporal complexity and multiple mission loads, unmanned aerial vehicle (UAV) swarm systems are widely used in defense deployments, environmental security, and urban logistics [1], with extensive research in autonomous control [2], communication links [3], intelligent collaboration [4,5], and mission assignment [6]. Today, UAV swarm systems are gradually being used in open scenarios to continuously improve their ability to interact with the environment [7-9]. However, UAV swarm systems, as whole mission systems, face more threat factors from the scenario and have a higher probability of being compromised by risks [10,11]. Therefore, resilience assessment under resource supplementation is an urgent problem for UAV swarms currently. 

To address this issue, a large number of studies have described the ability of swarm systems to resist damage and reconfiguration through the concept of resilience. Resilience generally refers to the ability of a system to withstand, respond to, and recover from disruptions. Since the concept of resilience was introduced by Holling for ecosystems, many researchers have followed his approach to conducting extensive research [12]. Resilience system analysis is widely used in systems such as transportation network systems [13], ecological network systems [14], road network systems [15,16], and pipeline network systems [17]. Woods summarized system resilience into four concepts: rebound, 

robustness, graceful extensibility, and sustained adaptability [18]. Phadke comprehensively considered the resilience of a UAV swarm. Overall, the disruption of one component in a UAV swarm can lead to unpredictable cascading failures. A resilience evaluation should consider all components [19], such as communication in the UAV swarm network [20] and network control [21]. Vachtsevanos designed the resilience of a UAV swarm from a risk management perspective. A resilient UAV swarm system should have the function of monitoring itself and its surrounding environment [22]. Therefore, the resilience of a UAV swarm is the ability to resist and absorb negative effects, reconfigure to recover, and meet mission expectations as much as possible under the impact of UAV failure, communication connectivity disruption, and degraded mission performance. 

In the context of networked applications, the research approach to swarm system resilience mainly considers the resilience of the network structure to factors such as random and deliberate attacks [23-25] and the network failure mechanism considering cascade failure [26]. Based on the application of this idea to the resilience of a UAV swarm, Sun et al. studied the resilience of an unmanned weapon system-of-systems under different attack intensities while considering the recovery of multiple topological reconfigurations of the system and analyzing the case of mission-oriented resilience metrics [27]. Bai et al. developed a communication-constrained UAV swarm model that considered the resilience of swarm communication capabilities under deliberate 

attacks. The resilience was improved using the reconnection of links [28]. Currently, research on the resilience of UAV swarms is focused on closed scenarios where resilience recovery comes from self-reconfiguration. In practical applications, UAV swarms are often used in open dynamic environments where performance changes are closely related to the loss and supplementation of UAVs. Because of the dynamics and flexibility in the use of UAV swarms, the supplementation of resources and system recovery in open environments are important concerns that should be addressed [29]. 

Various studies have developed different performance resilience metrics, and the analysis of the system requirements and reasonable metrics of resilience is the basis of resilience research. Dorblitz et al. studied the resilience of a transportation network under catastrophic events and developed a network model. The maximum clique was used as a performance metric [30]. Other metrics include the average shortest path length [31] and network throughput [32]. Poulin et al. summarized resilience performance metrics as the availability, productivity, and quality based on the study of the critical infrastructure [33]. The above metrics form a broad definition of the abstract objectives. Due to the complexity and emergence characteristics of UAV swarm systems, the proposed metrics need to reflect the system characteristics and mission requirements. 

In the study of resilience metric construction for UAV swarms, Cheng et al. studied UAV reconnaissance mission capability resilience, proposed resilience performance metrics targeting reconnaissance missions, and explored the impact of the topology and collaboration strategies on the resilience recovery based on complex network theory [34]. There have also been related studies on the mission capability [27], communication capability [28], and other metrics. Most studies performed resilience evaluations for a specific component of the UAV swarm. Based on the resilience concept requirements, the combination of a UAV swarm with resilience concepts and multi-component analysis should be considered. In addition, most of the resilience evaluation methods are based on resilience curve analysis, which only measures the integral performance of the resilience curve and lacks the analysis of the resilience process. Poulin analyzed the resilience curve in terms of many aspects of the parameters. It was proposed that the integration, size, and rate properties of the curve should be focused on and applied in specific models [33,34]. Therefore, it is necessary to conduct further research to improve the resilience evaluation methods and metrics for UAV swarm systems with high complexity, multiperformance synthesis, multidimensional topological feature correlation, and dynamic changes. 

The dynamic characterization of UAV swarm systems with resource supplementation and the resilience evaluation of multidimensional topological feature association is an important issue. In this study, the problem of system performance resilience evaluation with a UAV swarm system as the research object was examined. The system hierarchical characteristics were analyzed, a multi-level resilience metric and evaluation framework was constructed. A resilience evaluation method for UAV swarm systems with resource supplementation was proposed based on this framework. An example study of the resilience of a UAV swarm system was carried out in an open scenario, where external UAVs were added during the mission. By comparing the resilience recoveries in multiple scenarios, the resilience performance improvements for different conditions were determined to optimize the overall performance of the swarm. The main contributions of this study are summarized as follows. 

(i) A framework of resilience evaluation metrics for UAV swarms with resource supplementation was proposed. The mapping from the general mathematical concept of resilience to the physical object of a UAV swarm was realized. The resilience performance was analyzed on three levels based on UAV swarm multiperspective resilience evaluation needs. 

(ii) An evaluation method for UAV swarm systems with resource supplementation was proposed, and a swarm evaluation model 

was established. The flow concept was integrated into the network to better describe the dynamic changes in the system during the mission. 

(iii) An example study on the resilience of a UAV swarm system in an open scenario was carried out. The resilience characteristics were compared in terms of the quantity, speed, and threshold of resource supplementation, and orthogonal analysis was performed. The optimal conditions and marginal utility of the resilience recovery were studied to promote reliable UAV swarm operations. 

The rest of this study is organized as follows. In Section 2, the UAV swarm performance metrics are presented, and evaluation metrics are studied based on the swarm characteristics. Section 3 presents the process and method for resilience evaluation for UAV swarm systems. Section 4 compares and analyzes the results based on simulation experiments for validation. Finally, Section 5 provides the conclusions and future work. 

# 2. Performance metrics for resilience evaluation of unmanned aerial vehicle (UAV) swarm system

Performance metrics for resilience evaluation are the basis for evaluating the system resilience. This section proposes resilience metrics for UAV swarm systems based on dynamic characteristics and swarm emergence performances. In Sections 2.1, 2.2, and 2.3, performance metrics for resilience evaluation are constructed in three dimensions: the structural topology, flow connectivity, and mission effectiveness, respectively. 

When constructing resilience performance metrics for a UAV swarm, the following features are noted. 

- The system allows for swarm emergence, which not only expresses the role of individual UAVs in the swarm but also reflects the interactions and combination of capabilities from point to point. 

- When considering resource supplementation, the system performance changes have a larger scaling space and more complex changes than those with an autonomous reconfiguration. 

- The system is mission oriented. The swarm's own performance is the basis, and the mission capability cannot be ignored. 

Three dimensions are considered in the study of critical infrastructure resilience: the availability, productivity, and quality of service [33], which summarize the performance requirements for resilient system operation. Studies of satellite communication networks and complex equipment systems have similar decompositions of the resilience in these three dimensions [35,36]. 

The performance evaluation of a UAV swarm generally focuses on three aspects: the autonomous cooperative capability, system robustness, and mission effectiveness. Based on this, this study established swarm performance metrics from the following three perspectives. 

- In the process of an actual mission, the UAV swarm structure is dynamic and changeable. The mode, composition, and distance of the swarm always affect the efficiency of the system mission execution, and the topology-related performance always affects the integrity and availability of the swarm. 

- The output of the UAV swarm is mainly the mission effect and the communication messaging, such as resources that can be called and work that can be executed. It reflects the connectivity and availability of the system. 

- UAV swarm mission effectiveness is the ultimate purpose of a swarm application. In an open environment, the study of the performance in terms of the swarm availability and mission effectiveness under different conditions of resource supplementation can better guide the UAV swarm during use. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/c823e741e51766bdaa776582be5070f76c0631c1d405be131f39364f7c9950cb.jpg)



Fig. 1. Unmanned aerial vehicle (UAV) swarm system structure correspondence.


The above three dimensions can cover the UAV swarm performance, highlighting the swarm's emergence and autonomous characteristics. The resilience performance is specified for the UAV swarm system in terms of the structural topology performance, flow connectivity performance, and mission effectiveness. The specific metrics are described below. 

# 2.1. Structural topology performance

The structural topology performance incorporates the formation relationship and spatial structure of the UAV swarm into the resilience metric. The UAV swarm system is first modeled based on the structural topology aspect, and the network is the main model for describing the swarm at present [37]. Based on the study of Wang et al. on the modeling of a UAV swarm system, the multilayer complex network is divided into a communication layer, structure layer, and mission layer, which correspond to the communication data chain, vehicle, and mission load of UAV swarm system [38,39], respectively, and the mapping relationships are shown in Fig. 1. 

The complex network model of the UAV swarm is constructed based on the specific structural functions of the swarm, and its mathematical expression is $G = (V,E,X)$ , where $V = (V_{a},V_{b},V_{c})$ is the set of network nodes, $E = (E_{a},E_{b},E_{c},E^{\prime})$ is the set of edges, and $X = (X_{a},X_{c})$ is the set of node attributes. The model consists of three network layers, namely the communication layer $G_{a}$ , structure layer $G_{b}$ , and mission layer $G_{c}$ . The nodes and connected edges in the three layers of the network have different meanings. The communication layer $G_{a} = (V_{a},E_{a},X_{a})$ , where $V_{a}$ represents the UAV communication nodes, $E_{a}$ represents the UAV communication connection relationship, and $X_{a}$ represents the communication attribute capability of each node. The structure layer $G_{b} = (V_{b},E_{b})$ , where $V_{b}$ represents the UAV entity, $E_{b}$ represents the UAV formation relationship. The mission layer $G_{c} = (V_{c},E_{c},X_{c})$ , where $V_{c}$ represents the UAV mission payload, $E_{c}$ represents the UAV mission delivery relationship, and $X_{c}$ represents the mission attribute capability of each node. $E$ represents the set of inter-layer edges of the three-layer network. The connections between the layers represent the interdependence of the layers to form a whole, e.g., the mission layer and communication layer nodes are influenced by the structural layer nodes. 

For the structural topology performance measure of the network, the number of nodes, node average degree, average clustering coefficient, and global efficiency of the complex network topology metrics are selected as the structural topology resilience measures considering the degree of integrity of the basic properties of the network: 

$$
K = \frac {1}{N} \sum_ {i = 1} ^ {N} k _ {1}, \tag {1}
$$

$$
C = \frac {1}{N} \sum_ {i = 1} ^ {N} C _ {i}, \tag {2}
$$

$$
L = \frac {2}{N (N - 1)} \sum_ {i > j} d _ {i j}, \tag {3}
$$

$$
G E = \frac {1}{L}, \tag {4}
$$

$$
Q _ {1} = f \left(K ^ {*}, C ^ {*}, G E ^ {*}, n\right). \tag {5}
$$

Finally, referring to the normalization approach in the literature [40], the ratio of each metric to the maximum value is used as a normalized metric assuming a maximum value for each metric in the initial state. The weighted sum of the three metrics is used to represent the structural topology performance metrics of the network: 

$$
Q _ {1} = n * \left(a K ^ {*} + b C ^ {*} + c G E ^ {*}\right) (a, b, c \geq 0, a + b + c = 1). \tag {6}
$$

# 2.2. Flow connectivity performance

The flow connectivity performance incorporates the potential and availability of resources into the resilience metric. The communication information and mission capabilities are represented using flow properties. In a dynamic environment, the UAV swarm state changes in real time and interacts closely with the outside world, accompanied by the loss and replenishment of swarm components. A flow network $G = (V, E, C)$ is used to describe this dynamic interaction. 

The flow network has been studied in an unmanned swarm information exchange network and transportation network with algorithmic improvements [16,41]. The capacity of each edge $e_i (1 \leq i \leq n)$ in a random flow network can be some number from 0 to $c_i$ , which takes into account the dynamics of the network and better describes the real situation of the network. A detailed description of the flow network theory can be found in a previous publication [42]. 

In this study, flow was added to reflect the interactions between nodes in the UAV swarm network. The flow passes between nodes through connected edges under capacity constraints, describing the relationships between information transfer, mission assignment, and cooperation within the group. This is characteristic of the communication layer and mission layer in the complex network of a UAV swarm. 

The communication layer flow network $G_{a}^{\prime} = (V_{a},E_{a},C_{a})$ is established, where $V_{a}$ and $E_{a}$ are the sets of communication layer nodes and connected edges, respectively, and $C_{a}$ is the set of connected edge capacities, which represents the communication capacity limit between two nodes. The establishment of a communication layer flow network is based on the formation structure of the swarm, and generally, there are behavior-based methods, leader-follower methods, and autonomous control methods [40]. 

A mission layer flow network $G_{c}^{\prime} = (V_{c},E_{c},C_{c})$ is established, where $V_{c}$ and $E_{c}$ are the set of mission layer nodes and connected edges, respectively, and $C_c$ is the set of connected edge capacities, representing the mission capability flow limit between two nodes. The establishment of a mission layer flow network is based on the understanding and description of the system's mission process, which is summarized as an OODA (Observe, Orient, Decide, Act) loop by the US Air Force Colonel John Boyd, the basic idea of which can be found in previous publications [43,44]. The OODA loop allows for a broad overview of the mission process, breaking it down to form a chain of missions moving forward. With reference to this loop, the swarm mission execution process is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/b4f5a205d9361665116aa88685f695ad1caf31879194a15b093ef2c8a3bd9ec6.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/6b3171c0633ef867dd8bb2ff565735fdfe52025657dac5ba081adff951f6d262.jpg)



Fig. 2. Mission chain composition process.


summarized as "sensing" $\rightarrow$ "decision" $\rightarrow$ "execution," and the UAVs in the swarm are divided into three categories that perform the corresponding mission: 

- Sensor UAVs (S): UAV entities that scout, detect, and acquire information from the environment. 

- Decider UAVs (D): UAV entities that make judgments, commands, and controls. 

- Influencer UAVs (I): UAV entities that receive commands to directly execute specific missions. 

The three types of UAVs form a mission chain in a sequential manner to output mission capabilities to the target. At the same time, there are collaborative connections and mission interactions between nodes of the same type, such as information sharing between sensor nodes and mission redistribution between decider nodes. Therefore, because there is a mission serial relationship between sensor nodes and decider nodes, in the mission layer flow network, the flow directions include $S \rightarrow D$ , $D \rightarrow I$ , $S \rightarrow S$ , and $D \rightarrow D$ . Under this capability circulation relationship, based on the actual mission flow consideration, the mission chain can be represented as three kinds of meta-paths [27]: 

- $\mathrm{S} \rightarrow  \mathrm{D} \rightarrow  \mathrm{I}$ : The most basic mission chain. The sensor nodes receive information and pass it to the decideer nodes, and the decideer nodes judge the situation and command the influencer nodes to carry out the corresponding mission. 

- $\mathrm{S} \rightarrow  \mathrm{S} \rightarrow  \mathrm{D} \rightarrow  \mathrm{I}$ : Due to the information differences in different regions, the sensor nodes communicate to achieve information interoperability. 

- $\mathrm{S} \rightarrow  \mathrm{D} \rightarrow  \mathrm{D} \rightarrow  \mathrm{I}$ : Due to the non-uniform distribution of the connections between the decider nodes and the influencer nodes, the decider nodes communicate to regulate the mission assignment results. 

The actual mission chain is derived based on meta-paths, through which nodes form flow relations. 

The node capacity values in the complex networks are transformed. During the mission, the quality of communication is influenced and limited by the communication capacity of the nodes. The communication attribute capacity of a node within the communication layer is its ability to deliver information to the next node, and this value is used as the capacity of this forward edge. If a sensor UAV passes information to a decider UAV, the communication capacity of the sensor UAV is used as the communication capacity of the chain. Similarly, within the mission layer, $c_{c(i\rightarrow)} = x_{ci}$ , and the mission capacity of the node is used as the mission flow capacity of the node to the next connected edge of the 

node. The solutions of $C_a$ and $C_c$ are obtained, transforming the complex network model into a flow network model. 

Various types of UAVs continuously drive the mission through information sharing and situational awareness, with communication information and mission capabilities continuously flowing between nodes. Using this feature as an analogy for the flow model in a flow network, the flows start at the source and are transmitted within the capacity constraints of each edge to reach the sink. The size of the flow reflects the flow capacity of the network, with the maximum flow through the network as the flow capacity metric. Based on of the flow network, the flow connectivity is reflected in the communication flow capacity and mission flow capacity, and this performance is defined as, 

$$
Q _ {2} = Q _ {2 1} + n Q _ {2 2} (m, n \geq 0, m + n = 1), \tag {7}
$$

where $Q_{21}$ denotes the mission flow capacity, $Q_{22}$ denotes the communication flow capacity, and the weights $m$ and $n$ are based on the importance of the mission and communication, respectively. 

For the mission flow capability, on a unidirectional execution mission chain, the flows can reflect the mission execution and circulation with the chain start point as the source point and the chain end point as the sink. Based on this, the sensor node is taken as the source point, the influencer node as the sink point, and the maximum flow of the mission layer network as a reflection of the mission flow capability, i.e., 

$$
Q _ {2 1} = f _ {\text {c m a x}}. \tag {8}
$$

For communication flow capabilities, there is not only a forward flow of information based on a unidirectional execution mission chain but also a constant feedback of information. For example, the influencer nodes always feedback their mission execution to the decider nodes to update the group autonomous mission situation. Therefore, the communication circulation capacity consists of two parts, the maximum flow with the sensor nodes as the source and the influencer nodes as the sink, and the maximum flow with the influencer nodes as the source and the sensor nodes as the sink, denoted as, 

$$
Q _ {2 2} = k f _ {b \max } + l f _ {b \max } ^ {\prime} (k, l \geq 0, k + l = 1). \tag {9}
$$

The weights $k$ and $l$ are based on the importance of the communication information in the different directions. 

# 2.3. Mission effectiveness

The mission effectiveness evaluates the UAV swarm in terms of the quality of service. It also reflects the effectiveness of the mission cooperation and resource utilization of the UAV swarm through the mission chain. In an open environment, the mission effectiveness provides a visual representation of the impact of the loss and supplementation of nodes on the mission. Mission effectiveness requires not only consideration of the system characteristics and network emergence features but also statistical analysis of the mission execution process. The metrics are generally chosen as statistical metrics, such as the mission reliability as a mission effectiveness performance metric, 

$$
R (t) = P \left(C _ {s} > C _ {m}\right) \tag {10}
$$

where $C_s$ refers to the number of mission chains at the current moment, and $C_m$ is the mission baseline set based on the mission, corresponding to the number of mission chains. The formulation of the resilience baseline can be found in the literature [28,46]. The mission chain is calculated considering the mission capability output of the meta-paths as weights. $C_s$ is the weighted sum of the total number of meta-paths. Fig. 2 shows the composition process of the mission chains. The probability that the number of mission chains is greater than the baseline is taken as the mission effectiveness after conducting multiple missions. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/4bf5e5ae8ebd0f577e6f7201219ef374abe8e0c6d2f8dd0aaf3f1844ab289184.jpg)



Fig. 3. Resilience evaluation process.



Algorithm 1 Mission layer flow network modeling algorithm.


<table><tr><td colspan="2">Input: number of sensor UAVs m, number of decideur UAVs n, number of influencer UAVs p, the set of mission types for nodes type, The set of nodes in formation
Output: mission layer of graph form Gc</td></tr><tr><td colspan="2">1: initialize Gc //Initialize mission layer network graph to an empty graph, add m nodes to the graph</td></tr><tr><td colspan="2">2:N←m+n+p // Calculate the total number of nodes</td></tr><tr><td colspan="2">2: for i ∈N=[1,2,...N] do</td></tr><tr><td colspan="2">3: for j ∈N=[i,i+1,...N] do</td></tr><tr><td colspan="2">4: If the mission types of both UAV i and UAV j are decideur or sensor</td></tr><tr><td colspan="2">5: add a directed edge of nodes i and j to Gc</td></tr><tr><td colspan="2">6: elif UAV i is a sensor and UAV j is a decideur, and i and j are in the same formation</td></tr><tr><td colspan="2">7: add edge of nodes i and j to Gc</td></tr><tr><td colspan="2">8: elif UAV i is a decideur and UAV j is a influencer, and i and j are in the same formation</td></tr><tr><td colspan="2">9: add edge of nodes i and j to Gc</td></tr><tr><td colspan="2">10: end for</td></tr><tr><td colspan="2">11: end for</td></tr><tr><td colspan="2">12:return Gc</td></tr></table>


Algorithm 2 The algorithm for network reconnection after node changes.


<table><tr><td>Input: communication layer of graph form Ga, Structure layer of graph form Gb, mission layer of graph form Gc, the set of currently existing nodes 3nodelist
Output: communication layer of graph form Ga, Structure layer of graph form Gb, mission layer of graph form Gc // Output the updated three-layer network</td></tr><tr><td>1: for ni ∈ nodelist = [n1, n2, ...np] do // Iterate over all nodes in the current nodelist</td></tr><tr><td>2: if the graph Ga has no node ni // A new node is detected</td></tr><tr><td>3: add node ni to the graph Ga, Gb, Gc and connect node ni in close proximity</td></tr><tr><td>4: end for</td></tr><tr><td>5: for ai ∈ the set of nodes of Ga = [a1, a2, ...aq] do // Iterate over the nodes in the current network</td></tr><tr><td>6: delete node ai in the graph Ga, Gb, Gc</td></tr><tr><td>7: end for</td></tr><tr><td>8: return Ga, Gb, Gc</td></tr></table>

# 3. UAV swarm system resilience evaluation method

In this section, the resilience evaluation process of the UAV swarm system with resource supplementation is proposed, and the overall technical route is described, which is applicable to the performance resilience evaluation of different mission scenarios of the UAV swarm. The evaluation process is as follows: 

- The initial conditions of the UAV swarm are set according to the corresponding initial conditions of the mission, and the mission objectives and swarm size are clarified. Based on the initial scenario data, the swarm is initialized with a complex network model. Section 3.1 introduces the construction and calculation of the UAV swarm network. 

- The swarm behavior is deduced using a multi-agent system simulation to derive the whole mission process in order to obtain simulation data, and the mission deduction method for the multi-agent simulation is described in Section 3.2. 

- The network performance metrics of the UAV swarm during the simulation are calculated. The changes in the network model at different moments of the mission process are analyzed. 

- The structural topology resilience, flow connectivity resilience, and mission effectiveness resilience are calculated based on the network model, and finally, the system performance resilience is analyzed by plotting the resilience curve. In Section 3.3, the resilience curve is analyzed, and the resilience metrics are obtained. 

The overall process is shown in Fig. 3. 

# 3.1. Complex network modeling and solution

# 3.1.1. Modeling complex network

The complex network modeling has been briefly described in Sections 2.1 and 2.2. The connection of the network model is based on the UAV swarm formation and structure, and the structure layer network is built mainly by forming sub-clusters within the formation and connecting UAVs in close proximity. The construction of the communication layer flow network is dependent on the swarm structure and mission requirements. The specific establishment process can be found in previous publications [38,40]. The establishment of the mission layer network with node supplementation and consumption is described in detail below. The establishment of the mission layer flow network is based on the OODA model in Section 2.2, where the nodes form a flow network through three meta-paths, with the following process: 

1) Let the number of nodes of the sensor, decide, and influencer be $m$ , $n$ , and $p$ , respectively, and the number of formations be $k$ . Based on the path assignments $S \to D \to I$ , $S \to S \to D \to I$ , and $S \to D \to D \to I$ , the connections are made within sensor and decide nodes, and thus, there are a total of $m!$ and $n!$ connections, respectively. 

2) Based on mission meta-paths for intra-formation connectivity, there exist $m * n * p / k^2$ connectivity types, forming a complex network structure. 

3) Based on the complex network structure established in 2), the direction of the flow network edges is specified as mission forward, with the smaller numbered node pointing to the larger numbered node between similar nodes. The capacity of a node is used as the capacity of its forward edge. The pseudo-code is shown in Algorithm 1. 

The network changes mainly through the supplementation and removal of nodes, and in the three-layer network model, the layers are coupled to each other. When the UAV is damaged, the topology layer nodes fail, and the communication and mission layer nodes are also affected by their failure. At the same time, the change in the network causes the reconnection of network connected edges, whose connections are based on mission and scenario considerations. The reconfiguration principles mainly include reconfiguration within its communication range, searching for the corresponding node based on distance, and reconstituting the communication chain and the mission chain, with the number of connections not exceeding the maximum threshold value. The pseudo-code for reconnecting the network after a node change is shown in Algorithm 2. 


Algorithm 3



Maximum flow calculation algorithm.


<table><tr><td colspan="2">Input: number of UAVs n, Adjacency matrix for UAV networks g, set of forward edges of nodes pre, source node s, sink node t
Output: maxflow</td></tr><tr><td colspan="2">1:while 1 do</td></tr><tr><td colspan="2">2: flow←0</td></tr><tr><td colspan="2">3: for i ∈n=[1,2,...n] do //find the augmenting path</td></tr><tr><td colspan="2">4: if UAV i is a sensor and has a complete mission chain[i, j, k] // Complete means that the edge capacity of the chain is not zero</td></tr><tr><td colspan="2">5: pre[k] ←j //Forward edge assignment</td></tr><tr><td colspan="2">6: pre[j] ←i</td></tr><tr><td colspan="2">7: flow←min(g[s][i], g[i][j], g[j][k], g[k][t]) //Find the flow of this chain</td></tr><tr><td colspan="2">8: if flow != 0 //If flow = 0, the augmenting path is not found, the algorithm ends</td></tr><tr><td colspan="2">9: y←t //The current reverse edge is y</td></tr><tr><td colspan="2">10: while y! = s do //Create a reverse path</td></tr><tr><td colspan="2">11: g[y][pre[y]] += flow //update capacity</td></tr><tr><td colspan="2">12: g[pre[y]][y] -= flow</td></tr><tr><td colspan="2">13: maxflow+=flow //update the maximum flow</td></tr><tr><td colspan="2">14: y=pre[y]</td></tr><tr><td colspan="2">15: end while</td></tr><tr><td colspan="2">16: end for</td></tr><tr><td colspan="2">17: end while</td></tr><tr><td colspan="2">18: return maxflow</td></tr></table>

# 3.1.2. Resilience metric calculation

Three resilience performance metrics are presented in Sections 2.1, 2.2, and 2.3, where structural topology resilience is calculated using 

mainly complex network parameters, the mission effectiveness is calculated based on mission statistics values, and this section provides details on the calculation of the flow connectivity resilience. For the calculation of the network maximum flow, the Edmonds-Karp algorithm is used to search for the maximum flow in the network based on the following calculation process. 

1) The network flow is made to be 0. Two additional points, a super source and a super sink, are added to the network as the only source and sink of the flow network, and they are connected to sensor nodes and influencer nodes, respectively. Based on the current method of constructing the communication network and mission network, the network connection relationships are stored in respective matrices. 

2) An augmenting path is found with the BFS (breadth-first search) algorithm, the previous point at each point is recorded, the minimum capacity of the edges of that path is calculated as the flow of that path, and that flow value is added to the network flow. 

3) The path is traced in reverse, the capacity of each edge is subtracted from the flow value of that path, and the reverse edge is created to update the entire network. 

4) Steps 2) and 3) are repeated for the updated network until an augmenting path from the source to the sink cannot be found, at which point the network flow is the maximum flow. 

As an example, the pseudo-code for the mission layer network 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/9471594cb98bc4da8c3cd31a8312ad1d8d20aa9c1293e2bdd97891d341b4d92a.jpg)



Fig. 4. UAV swarm simulation flowchart.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/aafed4cfaead7e65a3b856d16cbf1afe03a4508c4735c3c6a0492f1989a5829a.jpg)



Fig. 5. State machine diagram for each type of UAV.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/dfafa03b86a631137010d36ad05597ed364be1b683dc06a68f74cd7b72e33798.jpg)



Fig. 6. Schematic diagram of the resilience curve.



Table 1 Experimental scenario parameters.


<table><tr><td>UAV swarm size</td><td>S: D: I</td><td>Number of formations</td><td>Target number</td></tr><tr><td>144</td><td>3: 1: 5</td><td>16</td><td>80</td></tr><tr><td>Scene size</td><td>Sensor UAV speed</td><td>Decider UAV speed</td><td>Influencer UAV speed</td></tr><tr><td>300 patches*140 patches</td><td>0.4 patch/tick</td><td>0.1 patch/tick</td><td>0.5 patch/tick</td></tr></table>

maximum flow calculation is shown in Algorithm 3. 

# 3.2. Multi-agent system simulation

A multi-agent system is a complex system formed by multiple agents 

interacting in an environment. System complexity can be reduced and control can be improved through multi-agent system analysis, and multi-agent models have been used to model swarms [28,41]. 

Netlogo is a Java-based multi-agent programming language and modeling environment that was developed by Uri Wilensky in 1999 to simulate complex phenomena [47]. It contains three main parts: "Interface" (for operating buttons, sliders, and screen output "worlds"), "Information" (for writing program documentation), and "Code" (for writing the underlying logic of the program). The agents in Netlogo follow serial execution logic. By writing down the behavior of each agent, a multi-agent system (MAS) that evolves over time can be modeled. The microscopic behaviors of agents interact to give rise to the macroscopic features of a complex system. Therefore, the mission process of the UAV swarm can be well described using Netlogo and the multi-agent simulation can react to the supplementation of nodes. Dynamic swarm mission results are obtained by statically describing the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/9fd6fb91cda59655ad479291497f5a953e72cf468e1beb612bc348216b893e24.jpg)



Fig. 7. Simulation scenario diagram.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/9b789a42588f8f0f539b19c0e9e225ecf4cbbf74781fbef10a1fef912bb07958.jpg)



Fig. 8. Diagram of a multilayer complex network of UAV swarm.



Table 2 Values of each level of factor A.


<table><tr><td>A</td><td>A1</td><td>A2</td><td>A3</td><td>A4</td></tr><tr><td>Quantity</td><td>12.5%</td><td>25%</td><td>37.5%</td><td>50%</td></tr></table>


Table 3 Values of each level of factor B.


<table><tr><td>B</td><td>B1</td><td>B2</td><td>B3</td><td>B4</td></tr><tr><td>Speed/v</td><td>1</td><td>2</td><td>4</td><td>8</td></tr></table>


Table 4 Values of each level of factor C.


<table><tr><td>C</td><td>C1</td><td>C2</td><td>C3</td><td>C4</td></tr><tr><td>Threshold</td><td>20%</td><td>30%</td><td>40%</td><td>50%</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/c20ff6062b012eb7dac69c19f91d788e285dbcf4272e9308f534e4859af9cea3.jpg)



Fig. 9. Orthogonal experimental design scheme.


individual behaviors of the sensor, decide, and influencer nodes of the UAV swarm in a time series loop. The generic UAV swarm mission process is divided into three phases. 

a) Mission initial phase: The swarm agent and the target are generated, the swarm interacts with communication and mission connection based on meta-paths, and the formation marches towards the target. 

b) Resistance phase: The agent executes the mission and generates the mission loss, e.g., an agent fails due to a mission, its formation becomes vacant, and the rest of the formation sends a formation connection request, searches for controllable agents, considers the control number and capacity constraints, and reconfigures the connection. 

c) Recovery phase: In this scenario, when the UAV swarm is damaged to a certain extent, resource nodes are brought in from outside for recovery, and the resource nodes are connected in the formation with the nodes in the scenario and continue the mission until the target is fully reached. The flowchart of the multi-agent simulation of the UAV swarm system with resource supplementation is shown in Fig. 4. 

The three types of UAV state machine diagrams are shown in Fig. 5. 

# 3.3. Curve analysis

The quantitative evaluation of the resilience is currently the main tool for resilience analysis [45]. The resilience curves of the system are plotted based on the variation of the performance function, and the classical resilience curves are shown in Fig. 6 (normalized). The key time points illustrated in the figure are defined as follows, 

- $t_e$ : time when the disruption event starts 

- $t_d$ : time when performance is at its lowest 

- $t_r$ : time when the performance recovery starts 

- $t_s$ : time when the performance reaches a steady state 

- $t_f$ : time when the mission ends 

Detailed definitions of the parameters can be found in a previous publication [33]. Based on the resilience curve parameters, the UAV swarm mission requirements and the setting of resilience targets [34,48, 49] are considered from the following perspectives. 

The resilience process is divided into two phases: the resistance phase and the recovery phase. In each phase, three factors were analyzed in terms of the magnitude, rate, and integration [46]. Each factor is calculated as follows, 

$$
R _ {1 d} = Q \left(t _ {d}\right), \tag {11}
$$

$$
R _ {2 d} = \Delta^ {1 - \frac {t _ {d} - t e}{\eta}}, \tag {12}
$$

$$
\begin{array}{l} \int_ {t _ {d}} ^ {t _ {d}} Q (t) d t \\ R _ {3 d} = \frac {t _ {e}}{\left(t _ {d} - t _ {e}\right)}, \end{array} \tag {13}
$$

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/3286244f289810d7b826d7ce41ae4f3d9dd1259a345aef7aff7d94e3501efbdc.jpg)



(a) $Q_{1}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/a3208886859bcee123942a9c1fa8ac5c6b10142630e2d1b9502501781e739d39.jpg)



(b) $Q_{2}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/e20fa8fe194093dc5c10ee3d829ffbc6a6e75e90183b968915e7f5e07816ad87.jpg)



(c) $Q_{3}$



Fig. 10. Performance variation curves for different supplementation quantities.


$$
R _ {1 r} = Q \left(t _ {f}\right), \tag {14}
$$

$$
R _ {2 r} = \Delta^ {\frac {t _ {2} - t _ {d}}{t f}}, \tag {15}
$$

$$
R _ {3 r} = \frac {\int^ {t _ {f}} Q (t) d t}{\left(t _ {f} - t _ {d}\right)}. \tag {16}
$$

The residual performance $R_{1d}$ is the minimum performance value of the system after a disruptive event. It reflects the ability of the UAV swarm system to maintain the overall performance after being subjected to a disruptive event. 

The failure rate $R_{2d}$ is based on the length of time it takes for the system to fail to a certain threshold value. The longer the time is, the better its ability to resist failure becomes. $\Delta$ is the degradation factor, which reflects how quickly the system fails. 

The cumulative performance of the resistance phase $R_{3d}$ reflects the effectiveness of the system in resisting damage. During recovery, the recovery performance $R_{1r}$ reflects the extent to which the system performs reconfiguration. The recovery rate $R_{2r}$ reflects how quickly the system recovers under the reconfiguration strategy. The cumulative performance of the recovery phase $R_{3r}$ reflects the effectiveness of the performance of the system during the reconfiguration process. 

The UAV swarm system has many uncertainties in the vehicle attribute settings, topology, collaboration strategies, formation size, and reconfiguration methods. Through the decomposition and comparison of different parameters, the details of the change in the performance of the resilience process can be analyzed, and the six indicators of resilience are weighted and summed to form an overall resilience metric, reflecting the overall state of the resilience process: 

$$
R = R _ {1 d} R _ {2 d} R _ {3 d} + R _ {1 r} R _ {2 r} R _ {3 r}. \tag {17}
$$

# 4. Simulation studies and discussion

The feasibility of the proposed method was verified by experiments, and the characteristics of the UAV swarm system under mission scenarios were analyzed, as discussed in this section. Through the comparison of different scenarios, the marginal utilities and optimal conditions for resilient recovery were determined, and the advantages and disadvantages of the various scenarios were analyzed, while suggestions are provided for the use and design of UAV swarm systems in practical applications. 

# 4.1. Experiment description

This section is based on a simulation example of the Netlogo multiagent system. The following is a brief introduction to the background of the example and the running process. The mission context of this scenario is a UAV swarm confrontation. The UAVs were divided into three categories based on the mission type: sensor, decider, and influencer. Each node had a fixed initial capability, and the mission was to attack a total of 80 targets. At the beginning of the mission, the sensor UAV conducted wide-range reconnaissance, and the reconnaissance radius was positively correlated with its own mission capacity value. After the sensor UAV cruises and reconnoiters the target, it provides information to the decider UAV. After receiving the information, the decider UAV assigns the attack mission to the corresponding influencer UAV swarm. The influencer UAV executes the corresponding attack mission through information interactions. The specific scenario parameters are shown in Table 1. 

The main changes in the UAV swarm during the mission were as follows. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/e87c419de1d2d2d25375df6d1907b730bbabef07926f549c85568f7714ab6b74.jpg)



Fig. 11. Boxplots of resilience factors for performance metric $Q_{2}$ with different supplementation quantities.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/7edb352ad5480adc596d999bf6ca1331b45fe13e09e6aff42a33fbbb2d98282d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/b50f4337f6385130720b9cd13e5b2d812ac7c885de19b461b9d90b0763104efd.jpg)



Fig. 12. Boxplots of resilience values of $Q_{1}$ and $Q_{2}$ for different supplementation quantities.


- The UAV swarm was subject to attacks from the target, resulting in the destruction of the UAV, the failure of the corresponding nodes, and the disconnection of the structural, communication, and mission layers. 

- After the communication network received damage, the UAV swarm reconnected the communication chain through self-organization to maintain information interaction. 

- When the overall number of UAVs in the swarm decreased to a certain threshold, external resources were added to respond with the current UAV swarm to achieve adaptive network adjustment and recovery. 

Finally, the termination condition was set as the target number being cleared to zero. The basic process of the scenario is depicted as shown in Fig. 7. The UAV swarm network model was constructed to form a three-layer network, as shown in Fig. 8. 

The following experimental protocol was established. 

1) Comparative analysis of the quantity of resource supplementation 

Six sets of experimental scenarios with different resource supplementation quantities were set, with a formation of nine UAVs, with the proportions of perception: decision: execution $= 3:1:5$ . The number of UAVs added was $0\%$ , $12.5\%$ , $25\%$ , $37.5\%$ , $50\%$ , or $62.5\%$ of the initial size. The supplementation speed was $\nu = 0.01875$ groups/ticks, and the supplementation threshold was set to less than $70\%$ of the total number of UAVs in the swarm, keeping the supplementation time the same. 

1) Comparative analysis of the speed of resource supplementation 

The accession rate was taken to be v, 2v, 4v, or 8v, where $\nu = 0.01875$ groups/ticks. The supplementation threshold was set to less than $70\%$ of the total number of the swarm, and the number of accessions was 54. Multiple experiments were conducted. 

1) Comparative analysis of the threshold of resource supplementation 

The supplementation threshold was defined as the number of lost UAVs reaching a certain percentage to start the supplementation. The threshold was set to $20\%$ , $30\%$ , $40\%$ or $50\%$ , with a total supplementation number of 54 and a supplementation speed of v. 

1) Orthogonal experiment 

In order to analyze the degrees of influence of the three factors, the supplementation quantity, supplementation speed, and supplementation threshold, on the resilience of the UAV swarm, and to seek the resource supplementation under the optimal conditions of resilience, orthogonal experiments were designed with three factors and four levels for the test program. The factors A, B, and C refer to the supplementation quantity, supplementation speed, and supplementation threshold, respectively, and the levels of each factor are shown in Tables 2, 3, and 4, respectively. 

This orthogonal experimental design scheme is shown in Fig. 9, and the variance analysis method was used to clarify the degrees of influence 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/377a096664fdec8fb04876746bb48d50d90ddf9207365312ac1101248b2a2228.jpg)



(a) $Q_{1}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/f0b71527447cc35fdc75159d282d9740bc129844c6a3ab63baaac1f49b843d99.jpg)



(b) $Q_{2}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/8066835564a90e961a55e0aa53653f9054ae37436b19835682d14c818df9ad40.jpg)



(c) $Q_{3}$



Fig. 13. Performance variation curves for different supplementation speeds.


of different factors on the resilience. The above experiments were performed with 50 replications per group. When calculating the mission effectiveness, the baseline was taken to be $60\%$ of the initial mission effectiveness. 

# 4.2. Results and discussions

# 4.2.1. Comparative analysis of quantity of resource supplementation

Based on the results of 50 experiments, three figures showing the performance changes over time were generated. For the structural topology performance metric $Q_{1}$ , as shown in Fig. 10(a), the overall trend 

was flat. Resource supplementation made its performance rebound significantly. As the quantity of supplementation increased, the resilience characteristics of its recovery became more and more evident. 

For the flow connectivity performance metric $Q_{2}$ , as shown in Fig. 10 (b), the recoveries under different supplementation quantities had significant differences, and the performance gradually decreased to close to 0 without adding UAVs. The recovery reached a higher level as the supplementation quantity increased. The decomposition of the curve parameters was performed for this characteristic curve, and boxplots of the six curve parameters under different conditions were created, as shown in Fig. 11. It is found that the recovery performance $R_{1r}$ tended to increase significantly with the increase in the amount of incorporation, while the recovery rate $R_{2r}$ decreased. This was because more nodes were added to increase the subsequent self-reconstruction time at the same recovery time. 

For the mission effectiveness metric $Q_{3}$ , as shown in Fig. 10(c), it can be seen that for this mission baseline, the performances with supplementation quantities of $0\%$ , $12.5\%$ , $25\%$ , and $37.5\%$ under multiple experiments were too low in terms of the reliability for the UAV swarm in the late mission, and the mission risk was high. The mission reliability at the supplementation quantities of $50\%$ and $62.5\%$ could consistently perform at a better level of 0.8 or more after recovery. At a supplementation quantity of $62.5\%$ , the subsequent confrontation process had no effect on the mission reliability, and the reliability remained at 1, which is consistent with Lanchester's square law and allows for a greater operational advantage when the number of UAVs is too large [50]. Therefore, in this mission scenario, the quantity to be added should be $50\%$ or more in order to maintain a better mission reliability. 

In order to analyze the regularity of the different factor changes of $Q_{2}$ and compare the effects of the change in the supplementation quantity conditions on the overall resilience value for multiple experiments, boxplots of the resilience values of $Q_{1}$ and $Q_{2}$ ( $Q_{3}$ was the experimental statistical value) under different conditions were generated, as shown in Fig. 12. 

It can be seen that the resilience value of structural topology performance increased with the quantity of supplementation, with diminishing marginal utility occurring after the quantity of supplementation reached $37.5\%$ . The flow connectivity performance increased with the quantity of supplementation and its resilience increased, but diminishing marginal utility appeared after the quantity of supplementation reached $50\%$ , and the benefit of a $62.5\%$ scale of supplementation on the growth of the resilience was low. 

# 4.2.2. Comparative analysis of speed of resource supplementation

Figures of the three performance changes with time were generated, as shown in Fig. 13. For the structural topology performance $Q_{1}$ , the variation showed an overall decreasing trend. The increase in the resource speed resulted in a slight increase in the performance improvement. The performance was insensitive overall to changes in the loss and supplementation. 

For the flow connectivity performance metric $Q_{2}$ , as shown in Fig. 13 (b), the recovery rate varied significantly at different accession speeds, and the group with a high supplementation speed could maintain a good status for a longer period of time. The size of its recovery performance also varied, and the high supplementation speed could maintain a high performance level for a short time, but as the mission proceeded, several curves basically reached the same level. The boxplots of the six influence factors under different conditions are shown in Fig. 14. The recovery performance $R_{1r}$ and recovery rate $R_{2r}$ had a significant increasing trends with the increase in the supplementation speed. 

For the mission effectiveness $Q_{3}$ , as shown in Fig. 13(c), it can be seen that for this mission baseline, the reliability recovery was not ideal at speed v. It could maintain a high mission reliability in the recovery process at supplementation speeds of 2v, 4v, and 8v. In the case of a certain number of resource supplementations, it was useful to increase the supplementation speed in order to maintain a better mission 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/9ddf70a72f22d1d96a3f6a4850db496583e598ce2bd2e5b68edd3a3cd03e2eb2.jpg)



Fig. 14. Boxplot of resilience factors for performance metric $Q_{2}$ with different supplementation speeds.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/7d1f599c140d9c66823e3c13a4da612e5ff107da1052460888f3ce26f05be494.jpg)



Fig. 15. Boxplots of resilience values of $Q_{1}$ and $Q_{2}$ for different supplement speeds.


reliability, and in this mission scenario, a 2v supplementation speed could be adopted. 

Based on the curve analysis, the specific effect of the supplementation speed on the performance resilience value was analyzed, and boxplots for different $Q_{1}$ and $Q_{2}$ performance resilience values were generated, as shown in Fig. 15. 

It can be seen that the $Q_{1}$ resilience increased with the supplementation speed. The trend slowed after the supplementation speed reached 2v, and diminishing marginal utility appeared. The diminishing marginal effect of the $Q_{2}$ resilience appeared after the supplementation speed of 4v. 

# 4.2.3. Comparative analysis of threshold of resource supplementation

The comparative curves of the three performances metrics at different supplementation thresholds were plotted, as shown in Fig. 16. For the structural topology performance metric $Q_{1}$ , as shown in Fig. 16 (a), the overall trend was flat. The performance recovered slightly as the supplementation threshold increased. For the flow connectivity performance metric $Q_{2}$ , as shown in Fig. 16(b), the lower the supplementation threshold was, the earlier its recovery occurred. Boxplots of the six parameters under different conditions were generated, as shown in Fig. 17. 

It can be found that the difference in the results was mainly in the resistance phase, where the resistance performance metrics $R_{1d}$ and $R_{3d}$ tended to decrease significantly with the increase in the supplementation threshold, and the failure rate $R_{2d}$ increased with the increase in the threshold. The lower the threshold was, the better the overall performance of its resistance phase became. 

For the mission performance $Q_{3}$ , as shown in Fig. 16(c), it can be seen that for this mission baseline, a threshold value of 0.2 could maintain a high reliability during the recovery phase, and the improvement of the performance between 0.2 and 0.3 was smaller. The threshold values of 0.4 and 0.5 still had a higher mission risk during the recovery process, so a low threshold value of 0.2 could be taken to ensure that the mission was completed in this mission scenario. Similarly, boxplots are shown in Fig. 18 for different values of the $Q_{1}$ and $Q_{2}$ performance resilience factors. 

It can be seen that the resilience of $Q_{1}$ varied with the supplementation threshold without a clear pattern. The resilience of $Q_{2}$ rose significantly with the decrease in the threshold and had no diminishing marginal benefit. Generally, these three experiments analyzed the optimal conditions and marginal utilities of the resilience recovery. For the structural topology performance, the supplementation quantity had a more pronounced impact, while the speed and threshold of the supplementation had little effect on it. For the flow connectivity performance, the resilience appeared to have significantly diminishing marginal utility as the conditions varied. At the current scenario scale, the benefits were not high when the supplementation conditions were too optimal. The best benefits were achieved when the supplementation quantity was at $50\%$ of the initial scale and when the supplementation speed was at 4v. Changes in the supplementation threshold did not show diminishing marginal benefits. For the mission effectiveness, the performance varied significantly for the different conditions, and the mission reliability metrics could all reach the ideal values when the supplementation conditions were superior. A high reliability could be 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/ee0a8214740074fa2b9dacacb7ecad4541dc81ae8f480c32f4a936b54cf4d7d3.jpg)



(a) $Q_{1}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/88bbede07fe746ff165790db75d2ff5ae1846b5ef178a1b6fcec4adc0f2df7e7.jpg)



(b) $Q_{2}$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/aeaefdfd2451ac733707e480e018a9f461a6b7a5182eca4ded4a6290ab0a617c.jpg)



(c) $Q_{3}$



Fig. 16. Performance variation curves for different supplementation thresholds.


maintained at a supplementation quantity of $50\%$ or more, and a large quantity had a significant advantage for the improvement of the mission reliability. The mission reliability was good at a supplementation speed of 2v, and the mission reliability was higher at a supplementation threshold of 0.2 times the initial quantity. 

# 4.2.4. Orthogonal experiment

The orthogonal experiment factors were $R_{Q_1}$ , $R_{Q_2}$ , and $R_{Q_3}$ , the resilience values corresponding to the performance factors $Q_1$ , $Q_2$ , and $Q_3$ , respectively. Each group of experimental values was the average of 

50 experiments. The degrees of influence of the different factors on the three resilience factors were analyzed using the variance analysis method. Tables 6, 7, and 8 show the analysis results for $R_{Q_1}, R_{Q_2}$ , and $R_{Q_3}$ , respectively. $R$ represents the extreme difference in the table, which was calculated as follows: 

$$
R = \max  \left(\bar {k _ {1}}, \bar {k _ {2}}, \bar {k _ {3}}, \bar {k _ {4}}\right) - \min  \left(\bar {k _ {1}}, \bar {k _ {2}}, \bar {k _ {3}}, \bar {k _ {4}}\right). \tag {18}
$$

Table 6 shows that the influence factors affecting the structural topology performance resilience were in the order of $A > B > C$ , meaning that the quantity of resources added was the most important factor affecting the resilience, and the optimal condition of the resilience was A4B3C1. Combined with the conclusions of experimental schemes 1, 2, and 3, the degrees of influence of the resource supplementation quantity, supplementation speed, and supplementation threshold on the performance resilience were smaller, and the resilience was mainly influenced by its own structure and strategy. 

From Table 7, we can see that the influences of the factors affecting the resilience of the flow connectivity performance factor $Q_{2}$ were in the order of $C > A > B$ , which means that the resource supplementation threshold was the most important factor affecting the resilience, and the optimal condition for resilience was A4B3C1. For the flow connectivity performance, to ensure good resilience, we need to control the supplementation threshold (supplementation timing) well, and the earlier the supplementation occurs, the better the resilience can be maintained. The more UAVs were added, the higher the recovery performance factor $R_{1r}$ was, and the higher the resilience became. The supplementation speed was optimal under condition B3, and a further increase in speed did not improve the resilience, while its effect on the resilience was not significant. 

It can be seen from Table 8 that the influences of the factors affecting the mission performance resilience were in the order of $\mathrm{C} > \mathrm{A} > \mathrm{B}$ , which means that the resource supplementation threshold was the most important factor affecting its resilience. The quantity and speed of supplementation had much less influence on the resilience than the supplementation threshold, and the optimal condition of the resilience was A4B4C1. The results for the mission performance were similar to those for the flow connectivity performance, and when combined with the data from Table 5, it was determined that the impact of the resource supplementation threshold on the mission performance resilience was critical. Supplementing too late could lead to an unrecoverable mission performance, which could be devastating to mission execution. It can also be seen from Fig. 16(c) that the mission performance decreased to 0 when the supplementation threshold was high and the mission baseline could not be reached. Furthermore, the larger the supplementation quantity and the faster the supplementation speed were, the more beneficial it was for the mission performance resilience. 

# 5. Conclusion

In this study, we evaluated the resilience of a UAV swarm system with resource supplementation and proposed multi-perspective resilience evaluation metrics. Complex network and flow network models were established based on the dynamic characteristics, each metric was defined concretely, the system resilience was evaluated by combining multi-agent technology with complex networks, and finally, application level verification and analysis were conducted through simulation experiments. The main conclusions were as follows: (1) Based on the current research on the system performance resilience, the resilience evaluation metrics of the UAV swarm system were based on three aspects: structure topology, flow connectivity, and mission effectiveness. This metric framework considers the multi-component, multi-level resilience of UAV swarms and meets the needs of UAV swarm resilience evaluation under resource supplementation. (2) A UAV swarm system resilience evaluation method was proposed to realize the behavioral logic deduction and real-time quantitative performance evaluation of 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/436d17b0c10e0061f93c49d914e0db0d5b448dff39b38b39f9912393935bd630.jpg)



Fig. 17. Boxplot of resilience factors for performance metric $Q_{2}$ with different supplementation thresholds.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/6a9329e0-2421-4cba-b579-a22262bcfd14/4e7bfe45f1ec69289cda99a73e172121a470ce85e0c68b8ac2d19d151785abd8.jpg)



Fig. 18. Boxplots of resilience values of $Q_{1}$ and $Q_{2}$ for different supplement thresholds.



Table 5 Values of each level of factor C.


<table><tr><td></td><td>A</td><td>B</td><td>C</td><td>\( R_{Q_1} \)</td><td>\( R_{Q_2} \)</td><td>\( R_{Q_3} \)</td></tr><tr><td>1</td><td>A1</td><td>B1</td><td>C1</td><td>1.029473</td><td>1.095227</td><td>1.165498</td></tr><tr><td>2</td><td>A1</td><td>B2</td><td>C2</td><td>0.940657</td><td>0.822623</td><td>0.614116</td></tr><tr><td>3</td><td>A1</td><td>B3</td><td>C3</td><td>1.203700</td><td>0.926232</td><td>0</td></tr><tr><td>4</td><td>A1</td><td>B4</td><td>C4</td><td>1.001369</td><td>0.731744</td><td>0</td></tr><tr><td>5</td><td>A2</td><td>B1</td><td>C2</td><td>1.016504</td><td>0.911035</td><td>0.719884</td></tr><tr><td>6</td><td>A2</td><td>B2</td><td>C1</td><td>1.182052</td><td>1.154751</td><td>1.421587</td></tr><tr><td>7</td><td>A2</td><td>B3</td><td>C4</td><td>1.108294</td><td>0.849914</td><td>0.004925</td></tr><tr><td>8</td><td>A2</td><td>B4</td><td>C3</td><td>1.217955</td><td>0.987295</td><td>0.213597</td></tr><tr><td>9</td><td>A3</td><td>B1</td><td>C3</td><td>1.151810</td><td>0.909537</td><td>0.023894</td></tr><tr><td>10</td><td>A3</td><td>B2</td><td>C4</td><td>1.127557</td><td>0.882751</td><td>0.048533</td></tr><tr><td>11</td><td>A3</td><td>B3</td><td>C1</td><td>1.418611</td><td>1.333343</td><td>1.318967</td></tr><tr><td>12</td><td>A3</td><td>B4</td><td>C2</td><td>1.252523</td><td>1.197225</td><td>0.988151</td></tr><tr><td>13</td><td>A4</td><td>B1</td><td>C4</td><td>1.204941</td><td>0.916728</td><td>0</td></tr><tr><td>14</td><td>A4</td><td>B2</td><td>C3</td><td>1.347736</td><td>1.228903</td><td>0.364812</td></tr><tr><td>15</td><td>A4</td><td>B3</td><td>C2</td><td>1.406525</td><td>1.236022</td><td>1.065431</td></tr><tr><td>16</td><td>A4</td><td>B4</td><td>C1</td><td>1.465009</td><td>1.297776</td><td>1.462587</td></tr></table>

the UAV swarm system with resource supplementation through the method of multi-agent and complex network model data interaction. (3) For the specific application scenarios of a UAV swarm, a study of the resource supplementation with different schemes was conducted. The results showed that the enhancement of the supplementation level would have diminishing marginal utility, and the best scheme can be selected based on the actual scale and mission scenario considering the cost and benefit. The related results can be used as a reference for 


Table 6 Range analysis of performance factor $Q_{1}$


<table><tr><td></td><td>A</td><td>B</td><td>C</td></tr><tr><td>k1</td><td>1.043800</td><td>1.100682</td><td>1.273786</td></tr><tr><td>k2</td><td>1.131201</td><td>1.149501</td><td>1.154052</td></tr><tr><td>k3</td><td>1.237625</td><td>1.284283</td><td>1.230300</td></tr><tr><td>k4</td><td>1.356053</td><td>1.234214</td><td>1.110540</td></tr><tr><td>R</td><td>0.312253</td><td>0.013605</td><td>0.011272</td></tr></table>


Table 7 Range analysis of performance factor $Q_{2}$


<table><tr><td></td><td>A</td><td>B</td><td>C</td></tr><tr><td>\(\overline{k_1}\)</td><td>0.893957</td><td>0.958131</td><td>1.220274</td></tr><tr><td>\(\overline{k_2}\)</td><td>0.975749</td><td>1.022257</td><td>1.041726</td></tr><tr><td>\(\overline{k_3}\)</td><td>1.080714</td><td>1.086378</td><td>1.012992</td></tr><tr><td>\(\overline{k_4}\)</td><td>1.169857</td><td>1.053510</td><td>0.845284</td></tr><tr><td>R</td><td>0.275901</td><td>0.128246</td><td>0.374990</td></tr></table>

decision making in the research, design, and utilization of UAV swarms. UAV swarm resilience is a widespread area of research, and this paper presented a methodological study and simulation experiments on the resilience of UAV swarms in resource supplementation scenarios. Continuing research in this direction requires consideration of many factors. (1) Not much consideration has been given to the specific 


Table 8 Range analysis of performance factor $Q_{3}$


<table><tr><td></td><td>A</td><td>B</td><td>C</td></tr><tr><td>k1</td><td>0.444903</td><td>0.477319</td><td>1.342160</td></tr><tr><td>k2</td><td>0.589998</td><td>0.612262</td><td>0.846896</td></tr><tr><td>k3</td><td>0.594886</td><td>0.597331</td><td>0.150576</td></tr><tr><td>k4</td><td>0.7232075</td><td>0.666084</td><td>0.013365</td></tr><tr><td>R</td><td>0.278304</td><td>0.188765</td><td>1.328795</td></tr></table>

approach and scheduling method for resource supplementation. In the future, the problem of resource allocation and resilience enhancement of UAV swarms will be the focus of research. (2) The strategy for resource supplementation in this study does not consider the mission objective case, such as the development of a mission baseline. In the future, the mission objective will be considered as a factor to evaluate UAV swarm resilience more comprehensively. (3) This study aimed to provide a framework of metrics and methods for evaluating the resilience of UAV swarms under resource supplementation, and experimental analysis was conducted under different conditions of resource supplementation. In-depth studies will be conducted on the solution methods for specific metrics. 

# Funding

This research was funded by the Science and Technology Innovation 2030-Key Project of "New Generation Artificial Intelligence" [grant number 2020AAA0108201] and the National Natural Science Foundation of China [grant number 62176015]. 

# CRediT authorship contribution statement

Linghao Kong: Methodology, Validation, Writing - original draft. Lizhi Wang: Writing - review & editing, Writing - original draft, Resources, Methodology, Funding acquisition. Zhongzheng Cao: Software. Xiaohong Wang: Resources, Methodology. 

# Declaration of Competing Interest

No potential conflict of interest was reported by the authors. 

# Data availability

Data will be made available on request. 

# References



[1] Zhou Y, Rao B, Wang W. UAV swarm intelligence: recent advances and future trends. IEEE Access 2020;8:183856-78. 





[2] Xia K, Son H. Adaptive fixed-time control of autonomous VTOL UAVs for ship landing operations. J Franklin Inst 2020;357(10):6175-96. 





[3] Wang C, Cui Y, Deng D, et al. Trajectory optimization and power allocation scheme based on DRL in energy efficient UAV-aided communication networks. Chinese J Electron 2022;31(3):397-407. 





[4] Xu Bei, Bai Guanghan, Liu Tao, Fang Yining, Zhang Yun-an, Tao Junyong. An improved swarm model with informed agents to prevent swarm-splitting. Chaos Solitons Fractal 2023;169:113296. 





[5] Wang X, Xu Y, Chen C, et al. Machine learning empowered spectrum sharing in intelligent unmanned swarm communication systems: challenges, requirements and solutions. IEEE Access 2020;8:89839-49. 





[6] Giles K, Giammarco K. A mission-based architecture for swarm unmanned systems. Syst Eng 2019;22(3):271-81. 





[7] Guo H, Zhou X, Wang Y, et al. Achieve load balancing in multi-UAV edge computing IoT networks: a dynamic entry and exit mechanism. IEEE Internet Things J 2022;9(19):18725-36. 





[8] Zeng J, Yang X, Yang L, et al. Modeling for UAV resource scheduling under mission synchronization. J. Syst. Eng. Electron. 2010;21(5):821-6. 





[9] Azoulay R, Reches S. UAV flocks forming for crowded flight environments. In: ICAART; 2019. p. 154-63. 





[10] Novak F, Walter V, Petracek P, et al. Fast collective evasion in self-localized swarms of unmanned aerial vehicles. Bioinspir Biomim 2021;16(6):066025. 





[11] Wang X, Xu Y, Chen C, et al. Machine learning empowered spectrum sharing in intelligent unmanned swarm communicate on systems: challenges, requirements and solutions. IEEE Access 2020;8:89839-49. 





[12] Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Syst 1973; 4(1):1-23. 





[13] Barahimi AH, Eydi A, Aghaie A. Multi-modal urban transit network design considering reliability: multi-objective bi-level optimization. Reliab Eng Syst Saf 2021;216:107922. 





[14] Wang T, Li H, Huang Y. The complex ecological network's resilience of the Wuhan metropolitan area. Ecol Indic 2021;130:108101. 





[15] Zhang Z, Ji T, Wei HH. Dynamic emergency inspection routing and restoration scheduling to enhance the post-earthquake resilience of a highway-bridge network. Reliab Eng Syst Saf, 2022;220:108282. 





[16] Liu Tao, Bai Guanghan, Tao Junyong, et al. Modeling and evaluation method for resilience analysis of multi-state networks. Reliab Eng Syst Saf 2022;226(4):18663. 2022. 





[17] Golara A, Esmaeily A. Quantification and enhancement of the resilience of infrastructure networks. J Pipeline Syst Eng Pract 2017;8(1):04016013. 





[18] Woods DD. Four concepts for resilience and the implications for the future of resilience engineering. Reliab Eng Syst Saf 2015;141:5-9. 





[19] Phadke A, Medrano FA. Towards resilient UAV swarms—a breakdown of resiliency requirements in UAV swarms. Drones, 2022;6(11):340. 





[20] Mou Z, Gao F, Liu J, et al. Resilient UAV swarm communications with graph convolutional neural network. IEEE J Sel Areas Commun 2021;40(1):393-411. 





[21] Hu N, Tian Z, Sun Y, et al. Building agile and resilient UAV networks based on SDN and blockchain. IEEE Netw 2021;35(1):57-63. 





[22] Vachtsevanos G, Lee B, Oh S, et al. Resilient design and operation of cyber physical systems with emphasis on unmanned autonomous systems. J Intell Robot Syst 2018;91:59-83. 





[23] Albert R, Jeong H, Barabasi AL. Error and attack tolerance of complex networks. Nature 2000;406(6794):378-82. 





[24] Crucitti P, Latora V, Marchiori M, et al. Efficiency of scale-free networks: error and attack tolerance. Physica A 2003;320:622-42. 





[25] Hui Y, Zun L, Yongjun L. Using local improved structural holes method to identify key nodes in complex networks. In: 2013 Fifth International Conference on Measuring Technology and Mechatronics Automation. IEEE; 2013. p. 1292-5. 





[26] Buldyrev SV, Parshani R, Paul G, et al. Catastrophic cascade of failures in interdependent networks. Nature 2010;464(7291):1025-8. 





[27] Sun Q, Li H, Wang Y, et al. Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems. Reliab Eng Syst Saf 2022;222: 108426. 





[28] Bai G, Li Y, Fang Y, et al. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020;193: 106602. 





[29] Ordoukhanian E, Madni AM. Model-based approach to engineering resilience in multi-UAV systems. Systems 2019;7(1):11. 





[30] Dorbritz R. Assessing the resilience of transportation systems in case of large-scale disastrous events. In: Environmental Engineering. Proceedings of the International Conference on Environmental Engineering (ICCEE). 8; 2011. p. 1070. May. 





[31] Mao Q, Li N. Assessment of the impact of interdependencies on the resilience of networked critical infrastructure systems. Natural Hazard 2018;93(1):315-37. 





[32] Casalicchio E, Metrics Galli E. for quantifying interdependencies. In: Proceedings of the Critical infrastructure protection II; 2008. p. 215-27. 





[33] Poulin Craig, Kane Michael B. Infrastructure resilience curves: performance measures and summary metrics. Reliab Eng Syst Saf 2021;216:107926. 





[34] Cheng C, Bai G, Zhang YA, et al. Resilience evaluation for UAV swarm performing joint reconnaissance mission. Chaos: Interdiscip J Nonlinear Sci 2019;29(5): 053132. 





[35] Geng Sunyue, Liu Sifeng, Fang Zhigeng. Resilient communication model for satellite networks using clustering technique. Reliab Eng Syst Saf 2021;215: 107850. 





[36] Wang N, Yuen KF. Resilience assessment of waterway transportation systems: combining system performance and recovery cost. Reliab Eng Syst Saf 2022;226:108673. 





[37] Strogatz SH. Exploring complex networks. Nature 2001;410(6825):268-76. 





[38] Lizhi WANG, et al. Unmanned aerial vehicle swarm mission reliability modeling and evaluation method oriented to systematic and networked mission. Chin J Aeronaut 2021;34(2):466-78. 





[39] Xiaohong WANG, et al. Robustness evaluation method for unmanned aerial vehicle swarms based on complex network theory. Chin J Aeronaut 2020;33(1):352-64. 





[40] Wang Tao, Li Hongbo, Huang Yue. The complex ecological network's resilience of the Wuhan metropolitan area. Ecol Indic 2021;130:108101. 





[41] Xu B, Liu T, Bai G, et al. A multistate network approach for reliability evaluation of unmanned swarms by considering information exchange capacity. Reliab Eng Syst Saf 2022;219:108221. 





[42] Ford LR, Fulkerson DR. Maximal flow through a network. Can J Math 1956;8:399-404. 





[43] Boyd J. A discourse on winning and losing. Maxwell air force base[r].al. USA: Air University Library Document No. M-U43947(Briefing slides); 1987. 





[44] Tan YJ, Zhang XK, Yang KW. Research on networked description and modeling methods of armament system-of-systems. J Syst Manag 2012;21(6):781-6. 





[45] Cheng C, Bai G, Zhang YA, et al. Improved integrated metric for quantitative assessment of resilience. Adv Mech Eng 2020;12(2):1687814020906065. 





[46] Li H, Sun Q, Wang M, et al. A baseline-resilience assessment method for UAV swarms under heterogeneous communication networks. IEEE Syst J 2022. 





[47] Tissue S, Wilensky U. Netlogo: a simple environment for modeling complexity. In: International conference on complex systems. 21; 2004. p. 16-21. 





[48] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35-53. 





[49] Tran HT, Balchanos M, Domercant JC, et al. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng Syst Saf 2017;158: 73-84. 





[50] Semenenko O, Mashkin O, Onofriichuk P, et al. Features of application of the Lanchester-type mathematical models in stochastic formulation when assessing the realities of air-land battle. INCAS Bull 2021;13:209-15. 

