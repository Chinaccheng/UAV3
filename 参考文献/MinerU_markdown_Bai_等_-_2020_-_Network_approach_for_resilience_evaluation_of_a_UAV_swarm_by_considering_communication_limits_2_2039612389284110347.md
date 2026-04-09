# Network approach for resilience evaluation of a UAV swarm by considering communication limits

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/97c081aa20f8259b8be9e302acb6908bd44189f3cfac61f214ac403461cc791f.jpg)


Guanghan Bai, Yanjun Li, Yining Fang, Yun-An Zhang⁎ , Junyong Tao 

Laboratory of Science and Technology on Integrated Logistics Support, National University of Defense Technology, Changsha, P.R. China 

# A R T I C L E I N F O

Keywords: 

System resilience 

UAV swarm 

Dynamic distance 

Complex networks 

Information exchange 

# A B S T R A C T

An unmanned aerial vehicle (UAV) swarm is a group of numerous UAVs performing tasks in a self-organized and self-adaptive manner to achieve an overall mission objective. Currently, the model of a UAV swarm is based on complex networks, where each UAV is represented as a node and each link denotes information exchange between UAVs. However, existing studies do not consider the limited communication range of each UAV. In this study, an improved UAV swarm model is proposed by incorporating the effect of limited communication range into the existing model. A UAV swarm mitigates the effects of possible threats and disruptions via self-adaptation; hence, it is suitable to use resilience to evaluate its performance. An improved resilience metric is proposed based on the difference between the swarm's performance and its standard system performance. A case study is conducted in which a UAV swam is called to implement a surveillance mission. Results and comparisons with extant studies indicate that the proposed model and metric lead to a more realistic method to evaluate the resilience of a UAV swarm. The proposed model and metric can be used to support mission planning and the design of a UAV swarm. 

# 1. Introduction

The use of unmanned aerial vehicles (UAVs) leads to agility and lower cost, and also allows the implementation of dull, dirty, and dangerous missions without posing risks to humans. Recently, there has been increasing interest in the use of UAVs for civil and military applications. Examples include repeated missions for long durations, surveillance missions under threat, and surveillance missions in nuclear, biological, and chemical circumstances. 

One of the current trends for UAVs is the use of swarm, in which a group of numerous UAVs perform tasks in a self-organized and selfadaptive manner to achieve an overall mission objective. Self-organized implies that the UAV swarm spontaneously forms a completely decentralized order via local interactions. Self-adaptive implies that the UAV swarm exhibits the capability to accommodate possible changes in circumstances, threats, and disruptive events via local interactions spontaneously. Self-organization and self-adaptive require an agile and resilient information exchange (IE for short) network for the UAV swarm in terms of link connection, link communication, and link rewiring. Thus, in this study, the UAV swarm is represented as an IE network where nodes represent UAVs and links represent information exchanged between UAVs. 

Currently, the number of UAVs in a swarm exceed hundreds, and 

the number will continue to increase in the future. Despite the increasing complexity of the swarm, there is a paucity of studies on the performance evaluation of the aforementioned types of large-scale networks. A common performance measure is reliability, and this is used to evaluate the ability of a system to sustain normal operation. Specifically, several reliability measures for networks are developed and applied to evaluate the performance of networked systems, including connectivity measures for binary networks, and performance measures for multistate networks [23]. In the aforementioned reported measures, if the component and network are not repairable, then reliability represents the probability that the component or the network is in a certain state within a specified time. If the component and the network are repairable, then reliability represents the probability that the component or system is in a certain state when time approaches infinity. The probabilistic measures are based on the failure data of components and system in the history. Additionally, it is typically assumed that the network topology remains unchanged in network reliability analysis. Thus, the main approach for reducing the probability of failures is by using high reliability components and/or increasing system redundancy during the design stage. 

However, a UAV swarm is typically used to implement dirty and dangerous missions in a conflict environment. The difficulty is specifically observed in military missions, where unpredictable threats and 

inevitable disruptive events correspond to the main causes of failures of the swarm. Thus, it is difficult and worthless to collect historical failure data. To mitigate unforeseen threats and undesirable events, traditional methods (including the use of high reliability components and/or increasing system redundancy) is not cost-effective [2]. Conversely, the UAV swarm is designed to accommodate disruptive events and restore its performance in terms of system reconfigurations and/or reformations. For example, a UAV swarm implementing a surveillance mission over a specified battlefield can be exposed to an enemy's air defense system [3]. When a few UAVs are destroyed, which is unpredictable and inevitable, its links to other UAVs are lost. Subsequently, given the capability of self-organization and self-adaptive, the UAVs whose links are lost start to rewire to the rest of the active UAVs in a timely manner. Thus, the UAV swarm restores its performance and continues its mission objective. As shown in the aforementioned scenario, the UAV swarm can adapt to disruptive events, and restore its intended performance to complete its assigned mission. Resilience provides a new approach for the design and analysis of engineering systems, to enhance the ability of the aforementioned systems to withstand uncertain threats and bounce back from disruptive events. Thus, it is more appropriate to use resilience for performance evaluation of a UAV swarm. 

A general procedure for resilience evaluation of a system is given as follows. First, an appropriate network model is developed to describe a UAV swarm. Second, an appropriate resilience evaluation method is developed. We discuss the extant studies on the two steps as follows. 

# 1.1. Model for UAV swarm as a network

The models of a UAV swarm include three scenarios: the initial swarm topology model, swarm damage model, and swarm recovery model. Given the enormous scale of UAVs and heavy data transmission load [1], it is difficult for the UAV swarm to be fully connected. The complex networks approach is widely applied to model several realworld systems. Tran et al. [2] applied a complex networks approach to model the three scenarios of the UAV swarm. The initial network topology is generated using scale-free networks with preferential attachment [5,6]. The network damage is implemented via removing nodes in a targeted manner [3] where it is preferential to remove node (s) with the higher number of neighbors at each threat event. The network recovery is implemented via link rewiring in preferential manner [4] where it is preferential to rewire nodes with higher number of neighbors. 

However, complex network models used in extant studies [2–4] do not consider the effect of geographic distance among UAVs and dynamic changes of the distances. Currently, a UAV swarm is designed to use wireless communications for information sharing and interaction among UAVs [1]. Each UAV receives and sends information using multi-hop communication. Evidently, the connectivity and reliability of data transmission is affected by the distance between each pair of UAVs. Thus, it is not realistic to assume that two UAVs far from each other possess same communication quality as two UAVs close to each other. Additionally, the connection between each pair of UAVs is subject to dynamic changes. This is because the relative position of each pair of UAVs rapidly changes during the mission. It is important to incorporate the effect of distance and its dynamic changes into the model of the UAV swarm. 

Based on preferential attachment model [6], Barthelemy [7] considered the effect of distance between nodes in complex network models via incorporating the adjusting parameter and distance function. Barrat et al. [8] improved the model in [7] by considering the node with weight. Manna and Sen [9] proposed a different distance function and incorporated an adjusting factor to the preferential attachment function. In the reported studies, the preferential attachment of the node is affected by the distance of the candidate node in a decreasing trend. However, there are two limitations in the reported models that preclude them from being appropriate for a UAV swarm. 

First, it is likely that networks generated by the reported models [7–10] contain isolated clusters and nodes. Isolated clusters and nodes exist in a few real-world networks. However, it is not appropriate for the UAV swarm. The swarm is fully self-organized and self-adaptive; hence, its awareness and actions are based on local interactions among UAVs. Given that each individual UAV exhibits limited capability, the joint capability of the swarm significantly decreases if isolated clusters and/or nodes exist. We consider a UAV swarm in a surveillance mission as an example. If isolated clusters and/or nodes exist, then each isolated cluster or node only obtains limited information of the target field, and does not include any information on the location of other UAVs and their awareness about the target field. Thus, a few areas can be monitored by too many UAVs, while several blind areas can remain. Thus, the UAV swarm is unable to obtain complete situation awareness of the target field, and the mission fails. Therefore, it is necessary to improve the reported models via incorporating the effect of distance among nodes, and this is unlikely to generate isolated clusters and/or nodes. 

Second, reported models [7–10] do not consider dynamic changes in the distance between each pair of UAVs. The networks examined by [7–10] mainly correspond to static networks including transportation and mobility networks, Internet, and power grids. However, a UAV swarm is highly mobilized and the topology of a UAV swarm can experience rapid changes during a mission. Therefore, it is necessary to improve the reported models via incorporating the dynamic changes of relative position for each pair of UAVs during a mission operation. 

# 1.2. Resilience evaluation of a UAV swarm

Resilience and its evaluation methods have been developed and applied to several real-world complex systems including infrastructure facilities [11,12,22], ecological systems [13,14], and complex engineering systems [15,17]. A summary of resilience evaluation methods is given in [16]. 

More recently, Nan and Sansavini [12] proposed a method to assess the resilience of interdependent infrastructures, in which an integrated metric is proposed based on time scale and performance level. Each factor is consistent with the concept of the defined resilience capacities, and the resilience metric exhibits a range of $[ 0 , \infty )$ . Tran et al. [17,2] proposed a method for resilience evaluation, in which the system performance data before the disruptive events and after recovery events is considered. Additionally, it can be used to evaluate a system subject to multiple disruptions. However, extant studies do not consider the resilience evaluation of a UAV swarm. To the best of the authors’ knowledge, only Tran et al. [3] applied the proposed resilience evaluation method in [17] for resilience evaluation of a UAV swarm. 

The resilience metric in [3,17] mainly focused on the topology of a system. First, a resilience value for each disruptive–recovery event is obtained via a function that synthesizes several key performance factors of a UAV swarm with each factor obtained by using the ratio of the corresponding capabilities after recovery and that before disruption. Second, the total system resilience is calculated by taking a weighted average of the resilience values for each disruptive–recovery event. As shown in the aforementioned procedure, the reported resilience measure is obtained using the difference between the UAV swarm's current performance and UAV swarm's performance in the last steady state. This reflects the capability of the swarm's network topology to adapt to disruptive events and restores its intended performance. 

However, the resilience metric is potentially not appropriate for a UAV swarm where the goal involves completing the assigned mission. Effectively, a UAV swarm is mission-oriented, and this indicates that a standard system performance exists that is qualified to complete the assigned mission. The administrator or the commander wishes to understand the difference between the current performance of a UAV swarm after each disruption, and compare it to the standard system performance. They also want to determine the overall performance of a UAV swarm and compare it to the standard system performance during 

the mission. Subsequently, they can determine whether to start the mission, or to abort it and re-plan it via incorporating additional UAVs for a swarm to achieve the required resilience. This ultimately aids the UAV swarm in completing the assigned mission. The reported resilience only reflects the general capability of the swarm's network topology to recover from disruptive events. However, it is unable to aid the administrator or commander in terms of decision making as to whether the swarm can complete its assigned mission. Thus, the resilience for single disruptive–recovery event should reflect the difference between system performance after each single event and standard system performance. Therefore, it is necessary to develop a proper resilience metric for the UAV swarm, to evaluate its capability to complete the assigned mission. 

# 1.3. Organization of the study

As indicated in the aforementioned literature review, it is necessary to develop an improved model and resilience metric for a UAV swarm, which is more realistic (and useful) for decision support and for the optimal design of a UAV swarm during mission operations. In this study, based on the reported models of a UAV swarm using scale free networks, we proposed an improved UAV swarm model by incorporating the effect of dynamic distances among UAVs. Additionally, the reported resilience metric is further improved to reflect the difference between the swarm's performance after each single event and standard system performance. The remainder of the study is organized as follows. An improved UAV swarm model (which considers effects of dynamic distances among UAVs) is proposed in Section 2. Section 3 proposes a mission-oriented resilience metric based on the improved UAV swarm model. In Section 4, a case study is conducted based on a multi-agent simulation, and this is followed by comparisons and discussions. Section 5 concludes the study. 

# 2. Improved model for a UAV swarm

In this section, an improved model for a UAV swarm is proposed by incorporating the effect of dynamic distance among UAVs. There are two improvements in the model. First, based on existing equations that consider the effect of distance between nodes, an improved equation is proposed that incorporates the effect of communication limits among nodes, and avoids generating isolated clusters and/or nodes. Second, the mechanism dealing with dynamic changes of distance between UAVs is proposed and incorporated into the proposed model. In Section 2.1, we briefly introduce existing network models by considering the effect of distance between nodes and discuss their limitations. Section 2.2 details the development of the proposed model incorporating the effect of dynamic distance between nodes, and this is followed by experimental validations. The mechanism dealing with dynamic changes of distance between UAVs is provided in Section 2.4. 

# 2.1. Preliminaries

In Tran et al. [2–4], the initial network topology is generated using scale-free networks with a preferential attachment algorithm. For example, given that the number of fully connected nodes initially corresponds to $m _ { 0 } .$ , a new node, $j$ creates $m \left( m < = m _ { 0 } \right)$ links to the existing nodes where the probability of node $j$ to link existing node i is given as follows: 

$$
P _ {j \rightarrow i} = \frac {k _ {i}}{\sum_ {l = 1} ^ {N _ {t}} k _ {l}}, \tag {1}
$$

where $N _ { t }$ denotes the current number of nodes in the network, and $k _ { i }$ denotes the degree of freedom of node i. 

Similarly, the network recovery is implemented via link rewiring in preferential manner where the probability of node $j$ (that is connected 

with the lost node) to rewire remaining node i is the same as Eq. (1). 

Based on the preferential attachment model [6], Barthelemy [7], Barrat et al. [8], and Manna and Sen [9,10] proposed different distance functions and adjusting factors to the preferential attachment probability function based on the following equation: 

$$
P _ {j \rightarrow i} = \theta k _ {i} F \left(d _ {j \rightarrow i}\right), \tag {2}
$$

where θ denotes the adjusting factor, $k _ { i }$ denotes the degree of freedom of node i, F( · )denotes the distance function that represents the effect of geographic distance on the connectivity and reliability of data transmission among UAVs, and $d _ { j  i }$ denotes the distance between node j and i. 

Barthelemy [7] considered the effect of distance between nodes in the complex network models by incorporating adjusting the parameter and distance function based on the following equation. 

$$
P _ {j \rightarrow i} = \theta k _ {i} F \left(d _ {j \rightarrow i}\right) = \frac {1}{\sum_ {l} e ^ {- d _ {j \rightarrow l} / r _ {\mathrm {c}}}} k _ {i} e ^ {- d _ {j \rightarrow i} / r _ {\mathrm {c}}}, \tag {3}
$$

where $k _ { i }$ denotes the degree of freedom of node $i , d _ { j  l }$ denotes the distance between node $j$ and previous linked node $l , r _ { c }$ denotes the range of communication, and $d _ { j  i }$ denotes the distance between node $j$ and i. 

Barrat et al. [8] improved the model in [7] by considering the node with weight based on the following equation: 

$$
P _ {j \rightarrow i} = \theta s _ {i} ^ {w} F \left(d _ {j \rightarrow i}\right) = \frac {1}{\sum_ {l} s _ {l} ^ {w} e ^ {- d _ {j \rightarrow l} / r _ {c}}} s _ {i} ^ {w} e ^ {- d _ {j \rightarrow i} / r _ {c}}, \tag {4}
$$

where $s _ { i } ^ { w }$ denotes the weight of node $i , d _ { j  l }$ denotes the distance between node $j$ and previous linked node $l , r _ { c }$ denotes the range of communication, and $d _ { j  i }$ denotes the distance between node $j$ and i. 

Manna and Sen [9] proposed a different distance function and incorporated an adjusting factor to the preferential attachment probability function as follows: 

$$
P _ {j \rightarrow i} = \theta k _ {i} ^ {\beta_ {k}} F \left(d _ {j \rightarrow i}\right) = \theta k _ {i} ^ {\beta_ {k}} d _ {j \rightarrow i} ^ {\gamma}, \tag {5}
$$

where θ denotes the adjusting factor, $\beta _ { k }$ denotes the adjusting factor for degree of freedom, $\gamma$ denotes the adjusting factor for distance, $k _ { i }$ denotes the degree of freedom for node $i , \mathrm { a n d } d _ { j  i }$ $i ,$ denotes the distance between node $j$ and node i. The effect of the three adjusting factors are discussed in [10]. 

In the aforementioned studies, the preferential attachment probability of a node is affected by the distance of a candidate node in terms of function $F ( d _ { j  i } )$ . As shown in Fig. 1(a), based on Eqs. (2)–(4), F $( d _ { j  i } )$ drops quickly when distance increases due to its exponential form, and this can be hardly modified through adjusting factors. Additionally, as shown in Fig. 1(b), based on Eqs. (2) and (4), when the degree of freedom for a node corresponds to 0, its preferential attachment probability corresponds to 0. Thus, the networks generated by the reported models [7–10] are likely to contain isolated clusters and nodes. 

# 2.2. Improved model

A UAV swarm is fully self-organized and self-adaptive, and thus its awareness and actions are based on local interactions among UAVs. Given that each individual UAV exhibits limited capability, the joint capability of the swarm is significantly reduced if isolated clusters and/ or nodes exist. Thus, we propose a new model for the initial network topology generation for a UAV swarm, and this is unlikely to generate isolated clusters and/or nodes. 

Fig. 2 shows the initial network topology generation for a UAV swarm. Given that the number of fully connected nodes initially corresponds to $m _ { 0 }$ , a new node, $j$ creates $m \left( m < = m _ { 0 } \right)$ links to the existing nodes, where the probability of node $j$ to link existing node i is given as follows: 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/bb3b70273a392b4b0e911ce058afc3fcb637f33c1364ed786070a83077482f8e.jpg)



(a) Isolated cluster generation


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/5ce4f517d6bcd7b26012fffdd7fbc52e5cd5845c1c804b657765b7ffb7f3df60.jpg)



(b) Isolated node generation



Fig. 1. Generation of isolated clusters and nodes using reported models.


$$
P _ {j \rightarrow i} = \alpha \left(k _ {i} + \varepsilon\right) F \left(d _ {j \rightarrow i}\right) = \left\{\begin{array}{l}\frac {\left(k _ {i} + \varepsilon\right) F \left(d _ {j \rightarrow i}\right)}{\sum_ {l = 1} ^ {N _ {t}} F \left(d _ {j \rightarrow l}\right)\left(k _ {l} + \varepsilon\right)}, \sum_ {l = 1} ^ {N _ {t}} F \left(d _ {j \rightarrow l}\right) > 0\\0, \text {o t h e r w i s e}\end{array}, \right. \tag {6}
$$

where $N _ { t }$ denotes the current number of nodes in the network, ɛ denotes the adjusting factor, and $k _ { i }$ denotes the degree of freedom of node i. 

The function $F ( d _ { j  i } )$ is given as follows: 

$$
F \left(d _ {j \rightarrow i}\right) = \left\{\begin{array}{l}1, d _ {j \rightarrow i} <   \eta \mathrm {r} _ {c}\\\frac {\left(\mathrm {r} _ {c} - d _ {j \rightarrow i}\right)}{\left(1 - \eta\right) \mathrm {r} _ {c}}, \eta \mathrm {r} _ {c} \leq d _ {j \rightarrow i} <   \mathrm {r} _ {c},\\0, d _ {j \rightarrow i} \geq \mathrm {r} _ {c}\end{array}\right. \tag {7}
$$

where $r _ { c }$ denotes the range of communication, $d _ { j  i }$ denotes the distance between node $j$ and $i ,$ and $\eta$ denotes the distance influential factor. It should be noted that when $\begin{array} { r } { \sum _ { l = 1 } ^ { N _ { t } } F ( d _ { j  l } ) = 0 } \end{array}$ , the probability of node $j$ to link all existing nodes corresponds to 0, and this implies there are nodes inside the maximum communication range of node j. In this case, node j stays in active until newly added nodes or a few nodes appear within the communication range of node $j .$ . 

With respect to network recovery, the probability of node $j$ (whose linked node(s) are lost) to rewire the remaining node i is the same as Eq. (6). The function $F ( d _ { j  i } )$ is the same as Eq. (7). Table 1 summarizes 


Table 1 Comparisons between the proposed and existing equations.


<table><tr><td>Name</td><td colspan="2">Equation</td></tr><tr><td>Barthelemy [7]</td><td colspan="2">Pj→i = θkiF(dj→i) = 1/∑l e−dj→l/rckl e−dj→i/rc,</td></tr><tr><td>Barrat et al. [8]</td><td colspan="2">Pj→i = θsiwF(dj→i) = 1/∑l siw e−dj→l/rscsiw e−dj→i/rc,</td></tr><tr><td>Manna and Sen [9]</td><td colspan="2">Pj→i = θkiβkF(dj→i) = θkiβk dj→i,</td></tr><tr><td>Proposed equation</td><td colspan="2">Pj→i = α(ki + ε)F(dj→i) = (ki + ε)F(dj→i)/∑l=1NtF(dj→l)(kl + ε), ∑l=1NtF(dj→l) &gt; 0</td></tr><tr><td></td><td>0,</td><td>otherwise</td></tr><tr><td></td><td>1,</td><td>dj→i &lt; ηrc</td></tr><tr><td></td><td>F(dj→i) = {rc - dj→i}/(1 - ηrc},</td><td>ηrc ≤ dj→i &lt; rc</td></tr><tr><td></td><td>0,</td><td>dj→i ≥ rc</td></tr></table>

the proposed and existing equations. 

We illustrate the proposed model by comparing it with the other reported models using the following experiments. The network topologies of UAV swarm are generated using four models, namely 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/5f038f564a22ae689da4ca9f90a889aaf3535ec690614dda932dbfb4fb1530c0.jpg)



Fig. 2. Initial network topology generation for a UAV swarm.



Table 2 Parameters for the experiment.


<table><tr><td>Parameter</td><td>Meaning</td><td>Value</td></tr><tr><td>N</td><td>Size of the network</td><td>100</td></tr><tr><td>m0</td><td>Number of nodes in the initial network</td><td>2</td></tr><tr><td>m</td><td>Number of newly added links</td><td>1</td></tr><tr><td>rc</td><td>Range of Communication</td><td>100</td></tr><tr><td>βk</td><td>Adjusting factor for degree of freedom</td><td>0.8</td></tr><tr><td>γ</td><td>Adjusting factor for distance</td><td>-5</td></tr><tr><td>ε</td><td>Adjusting factor</td><td>0.1</td></tr><tr><td>η</td><td>Distance influential factor</td><td>0.8</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/0ea7d5876524462ab291e69627fc32c394e0f0260f3b1c69dfce03dbc4a14c7c.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/a8af10b36c39238d06d99398e58a5e2982bb061faa93badaea467b068af327c0.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/122dc0b71ae9d8aa9ee5ed1992fa77cd2476a09328ff18faad9cded4c1ed679d.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/ad2b1e8859e895f5721c1fdbf9b297da92187356a57c70e507465de4f67e409f.jpg)



(@)



Fig. 3. Networks generated using (a) [7], (b) [8], (c) [9], and (d) the proposed model.


Barthelemy [7], Barrat et al. [8], Manna and Sen [9,10], and the proposed model. The parameters are given in Table 2. The positions of nodes in each generated network are identical. The experiments are coded in $C + +$ and plotted in OpenCV [21]. 

The results are shown in Fig. 3. As shown in the figure, the networks generated using models in Barthelemy [7], Barrat et al. [8], and Manna and Sen [9] contain isolated clusters and nodes. Conversely, the network generated using the proposed model does not contain any isolated clusters and nodes. 

# 2.3. Dynamic changes of relative distance

The reported models introduced in Section 2.1 do not consider the dynamic changes for each pair of UAVs. A UAV swarm is highly mobilized, and thus the relative position of each pair of UAVs varies across time. Hence, the topology of a UAV swarm can experience rapid changes during the mission. A mechanism dealing with dynamic changes is developed for a UAV swarm as shown in Fig. 4. As shown in the figure, the corresponding link is removed when the distance between two UAVs exceeds the range of communication, $r _ { c }$ . The host node (which the removed link belongs to) rewires the link based on Equations (6) – (7). It should be noted that when $\begin{array} { r } { \sum _ { l = 1 } ^ { N _ { t } } F ( d _ { j  l } ) = 0 } \end{array}$ , the probability of node $j$ to link all existing nodes corresponds to 0. In this case, node $j$ stays in active until other nodes move within its range of communication. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/c6d72ff10847660bb5618b6b3ae450dc345782829bb0da020e525a8c626a8bd7.jpg)



Fig. 4. Mechanism to deal with dynamic changes for a UAV swarm.


# 3. Mission-oriented resilience metric for a UAV swarm

In this section, a mission-oriented resilience metric for UAV swarm is developed based on the reported resilience metric. Generally, resilience evaluation method includes the system performance measure selection and resilience metric construction. In Section 3.1, we discussed system performance measure selection. The reported resilience metric in [3,17] and its limitation are discussed in Section 3.2. Section 3.3 discusses the improved resilience metric. 

# 3.1. System performance measure

It is recalled that a UAV swarm performs tasks in a self-organized and self-adaptive manner via information sharing and interaction. Thus, we focus on the capability of information exchange as system performance for the UAV swarm. In the study, we use the same system performance measure as detailed in Tran et al. [2,17], and this denotes the total information received in the UAV swarm. 

Each UAV periodically generates information and sends the same to its target UAV via the shortest path. The probability of information generated for each UAV at time t is given as follows [2]: 

$$
\mu_ {t} = \frac {\mu_ {0} N}{N _ {t}}, \tag {8}
$$

where $\mu _ { 0 }$ denotes the initial information generation probability, N denotes the total number of UAVs, and $N _ { t }$ denotes the current number of UAVs. Tran [2] defined the total number of information received in an IE network of a UAV swarm at time t as the system performance. This is because the length of the shortest path for each information reduces the real-time performance of information exchange for UAV swarm. The total number of information received in the IE network is given as follows [2]: 

$$
\bar {y} (t) = \sum_ {i = 1} ^ {N _ {t}} \sum_ {j = 1} ^ {R _ {i} (t)} \Delta^ {d _ {j} ^ {i}}, \tag {9}
$$

where $R i ( t )$ denotes the number of information received for node i, dji 

denotes the length of the shortest path obtained via shortest path algorithm (such as Dijkstra's algorithm [19] for the $j _ { t h }$ message received by node i), $N _ { t }$ denotes the current number of UAVs, and $\Delta$ denotes the time-sensitive factor. The range of $\Delta$ corresponds to $0 < \Delta \leq 1$ and is given based on the requirement of the mission. $\Delta = 1$ when the realtime performance is ignored. This is because the information generation for each UAV is a random variable. Tran [2] used multiple simulations to obtain average raw values of $y ( t )$ . Savitzky–Golay (S–G) filter [18] is further applied to calculate the smoothed values of $y ( t )$ . 

# 3.2. Reported resilience metric

Given the system performance measure, the next step involves developing a proper resilience metric. Tran et al. [3] proposed a method to evaluate system resilience subject to multiple disruptions and is used for resilience evaluation of a UAV swarm. There are mainly two steps in the reported method. First, the resilience for each disruption–recovery event is calculated via Equation [3] as follows: 

$$
S _ {i} = \left\{ \begin{array}{l l} \sigma \rho [ \delta + \varsigma + 1 - \tau^ {\rho - \delta} ], & \text {i f} \rho \geq \delta \\ \delta \rho (\delta + \varsigma), & \text {o t h e r w i s e} \end{array} , \right. \tag {10}
$$

where $\sigma , \delta , \boldsymbol { \rho } , \tau ,$ and $\varsigma$ denote the performance factor, absorption factor, recovery factor, recovery time factor, and volatility factor, respectively. The factors are calculated using the ratio of the corresponding capabilities before disruption and that after the recovery as follows [3]. 

As shown in Fig. 5, we assume that $y _ { D } , y _ { \mathrm { m i n } } ,$ , and $y _ { R }$ denote $y ( t )$ before the disruption, before the recovery, and after the recovery, respectively. 

Given the period of a single event $[ t _ { 0 } , t _ { f i n a l } ]$ , let $t _ { t h } , t _ { \operatorname* { m i n } } ,$ and $t _ { s s }$ denote the time when the disruption occurs, system is stable after disruption, and recovery begins, respectively. Thus, we obtain the following expressions: 

$\begin{array} { r } { y _ { D } = \frac { \sum _ { t _ { 0 } } ^ { t _ { t h } } y ( t ) } { t _ { t h } - t _ { 0 } } , ~ y _ { \operatorname* { m i n } } = \frac { \sum _ { t _ { \operatorname* { m i n } } } ^ { t _ { S s } } y ( t ) } { t _ { s s } - t _ { \operatorname* { m i n } } } , ~ y _ { R } = \frac { \sum _ { t _ { S s } } ^ { t _ { t h a l } } y ( t ) } { t _ { f i n a l } - t _ { s s } } , ~ \sigma = \frac { \sum _ { t _ { 0 } } ^ { t _ { f i n a l } } y ( t ) } { y _ { D } ( t _ { f i n a l } - t _ { 0 } ) } , } \end{array}$ − t tth 0 , $\begin{array} { r } { \delta = \frac { y _ { \mathrm { m i n } } } { y _ { D } } } \end{array}$ , $\begin{array} { r } { \tau = \frac { t _ { s s } - t _ { 0 } } { t _ { f i n a l } - t _ { 0 } } \mathrm { . } } \end{array}$ , ρ = $\begin{array} { r } { \rho = { \frac { y _ { R } } { y _ { D } } } . } \end{array}$ y D , and $\zeta = \frac { 1 } { 1 + \exp [ - 0 . 2 5 ( S N R _ { d B } - 1 5 ) ] }$ . The calculation of signal-to-noise $( S N R _ { d B } )$ is given in [18]. 

Second, given the resilience for each disruption–recovery event, the total system resilience is expressed as follows [3]: 

$$
S _ {\text {t o t a l}} = \sum_ {i = 1} ^ {N _ {\text {t h r e a t}}} \frac {w _ {S} ^ {i}}{\sum_ {j = 1} ^ {N _ {t}} w _ {S} ^ {j}} S _ {i}, \tag {11}
$$

where $w _ { R } { } ^ { i } = ( 1 - \beta ) ^ { N _ { t } - i }$ denotes the weight of the $i _ { t h }$ event, $\beta$ denotes 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/2e4fad45a01ddad9034e903ed1da5af2b6213a8ea3cc1b46dac0286a5e8ec2f8.jpg)



Fig. 5. Illustration of yD, ymin, yR, t0,tfinal, tth, tmin, and $t _ { s s } .$


the weight factor, $N _ { t h r e a t }$ denotes the number of disruption–recovery event, and $N _ { t }$ denotes the current number of UAVs. 

# 3.3. The improved resilience metric

However, the factors in Eq. (10) are calculated based on the ratio of the corresponding capabilities before disruption and that of after the recovery event, and this is potentially not appropriate for a UAV swarm. The ultimate goal for a UAV swarm involves completing the assigned mission. There exists a standard system performance that is qualified for completing the assigned mission. Thus, each disruption–recovery event's resilience should reflect the difference between the system performance after each event and standard system performance. Therefore, based on the resilience metric in [3], we propose a new resilience measure as follows. 

First, a resilience value for each disruptive–recovery event is obtained by a function synthesizing several key performance factors of the UAV swarm wherein each factor is obtained using the difference between the system performance after each event and standard system performance. We modify the equations to obtain factor $\overline { { y _ { D } } }$ as follows: 

$$
\bar {y _ {D}} = \mu_ {t} N _ {t} = \left(\mu_ {0} \frac {N}{N _ {t}}\right) N _ {t} = \mu_ {0} N, \tag {12}
$$

where $\mu _ { 0 }$ denotes the initial information generation probability, and $N$ denotes the total number of UAVs. Based on Eq. (12), $\overline { { y _ { D } } }$ corresponds to the expected value of $y ( t )$ when $N _ { t } \geq \mu _ { 0 } N ,$ , which denotes the standard system performance. Based on $\overline { { y _ { D } } }$ , the absorption factor is defined as follows: 

$$
\bar {\rho} = \frac {y _ {R}}{\bar {y} _ {D}}. \tag {13}
$$

With respect to the recovery time factor, it is more appropriate to begin with the time when disruption occurs. Thus, the recovery time factor is defined as follows: 

$$
\bar {\tau} = \frac {t _ {\mathrm {s s}} - t _ {\mathrm {m i n}}}{t _ {\text {f i n a l}} - t _ {\mathrm {m i n}}}, \tag {14}
$$

where the difference from $\tau$ is that $t _ { 0 }$ is replaced by $t _ { \mathrm { m i n } }$ . Based on the above equations, the performance factor is defined as follows: 

$$
\bar {\sigma} = \frac {\sum_ {t _ {\operatorname* {m i n}}} ^ {t _ {\text {f i n a l}}} y (t)}{\overline {{y _ {D}}} \left(t _ {\text {f i n a l}} - t _ {\min }\right)}, \tag {15}
$$

Given the newly defined factors, the resilience for each disruption–recovery event is calculated in a manner similar to Eq. (10) as follows: 

$$
\bar {S} _ {i} = \left\{ \begin{array}{l} \bar {\sigma} \bar {\rho} [ \delta + \varsigma + 1 - (\bar {\tau}) ^ {(\bar {\rho} - \delta)} ], \text {i f} \bar {\rho} \geq \delta \\ \delta \bar {\rho} (\delta + \varsigma), \text {o t h e r w i s e} \end{array} , \right. \tag {16}
$$

Second, the total resilience is calculated using the same equation as (11). Table 3 summarizes the proposed resilience measure and existing one. 

As shown in the aforementioned procedure, the proposed resilience measure captures the difference between the swarm's current performance and its standard system performance, and this reflects the capability of the swarm to adapt to disruptive events and restore its intended performance, and also reflects the capability of the swarm to complete its assigned mission. 

# 4. Case study

In this section, a case study is conducted based on a multi-agent simulation, in which a UAV swam is called to implement a surveillance mission over a controlled area. We compare the proposed model and resilience metric with that proposed by Tran et al. [2,17]. In Section 4.1, we introduce the background of the mission and the 


Table 3 Comparisons between the proposed resilience measure and existing measure.


<table><tr><td>Difference</td><td>Proposed resilience measure</td><td>Reported resilience measure [3]</td></tr><tr><td>different</td><td>\(\overline{S}_{i}=\{\overline{\sigma}\overline{\rho}\left[\delta+\varsigma+1-(\overline{\tau})^{(\overline{\rho}-\delta)}\right], \quad \text{if}\overline{\rho} \geq \delta\) \(\delta\overline{\rho}(\delta+\varsigma), \quad \text{otherwise}\)</td><td>\(S=\begin{cases}\sigma\rho[\delta+\varsigma+1-\tau^{\rho-\delta}] &amp; \text{if}\rho \geq \delta \\ \delta\rho(\delta+\varsigma) &amp; \text{otherwise}\end{cases}\)</td></tr><tr><td>different</td><td>\(\overline{y_{D}}=\mu_{t}N_{t}=(\mu_{0}\frac{N}{N_{t}})N_{t}=\mu_{0}N\)</td><td>\(y_{D}=\frac{\sum_{t_{0}}^{t_{th}}y(t)}{t_{th}-t_{0}}\)</td></tr><tr><td>same</td><td>\(y_{\min }=\frac{\sum_{t_{\min }}^{t_{SS}}y(t)}{t_{SS}-t_{\min }}\)</td><td>\(y_{\min }=\frac{\sum_{t_{\min }}^{t_{SS}}y(t)}{t_{SS}-t_{\min }}\)</td></tr><tr><td>same</td><td>\(y_{R}=\frac{\sum_{t_{SS}}^{t_{final}}y(t)}{t_{final}-t_{SS}}\)</td><td>\(y_{R}=\frac{\sum_{t_{SS}}^{t_{final}}y(t)}{t_{final}-t_{SS}}\)</td></tr><tr><td>different</td><td>\(\overline{\sigma}=\frac{\sum_{t_{\min }}^{t_{final}}y(t)}{y_{D}(t_{final}-t_{\min })}\)</td><td>\(\sigma=\frac{\sum_{t_{0}}^{t_{final}}y(t)}{y_{D}(t_{final}-t_{0})}\)</td></tr><tr><td>same</td><td>\(\delta=y_{\min }/y_{D}\)</td><td>\(\delta=y_{\min }/y_{D}\)</td></tr><tr><td>different</td><td>\(\overline{\tau}=\frac{t_{SS}-t_{\min }}{t_{final}-t_{\min }}\)</td><td>\(\tau=\frac{t_{SS}-t_{0}}{t_{final}-t_{0}}\)</td></tr><tr><td>different</td><td>\(\overline{\rho}=\frac{y_{R}}{y_{D}}\)</td><td>\(\rho=y_{R}/y_{D}\)</td></tr><tr><td>same</td><td>\(\varsigma=\frac{1}{1+\exp[-0.25(SNR_{dB}-15)]}\)</td><td>\(\varsigma=\frac{1}{1+\exp[-0.25(SNR_{dB}-15)]}\)</td></tr><tr><td>different</td><td>\(\overline{S_{total}}=\sum_{l=1}^{N_{\text{threat}}}\frac{w_{S}^{l}}{\sum_{j=1}^{N_{T}}w_{S}^{j}}\overline{S_{l}}\)</td><td>\(S_{total}=\sum_{i=1}^{N_{\text{threat}}}\frac{w_{S}^{i}}{\sum_{j=1}^{N_{T}}w_{S}^{j}}S_{i}\)</td></tr></table>

experiment settings. Section 4.2 details the simulation results, comparisons, and discussions. 

# 4.1. Mission background and experiment settings

The mission background is similar to that in [4]. A UAV swam is called to implement a surveillance mission over a specified battlefield as shown in Fig. 6. An Arsenal Plane releases $N$ identical UAVs in a safety zone. The UAVs form the initial network topology using Eqs. (6) and (7) and move towards the battle filed. The aim of the UAV swarm involves covering the whole battlefield to minimize the blind area. The capability of information exchange (i.e., the total information received at each time step) is used as the system performance of the UAV swarm. Other background is given as follows: 

There are $N$ identical UAVs in the swarm with the mission to maintain awareness of the battlefield. Each UAV moves in a snakelike search pattern within the battlefield. Each UAV receives and sends information about the locations of detected opponents and other UAVs via multi-hop wireless communication. The UAVs are evenly distributed in the battlefield to maintain the awareness of the battlefield. When a UAV senses other UAVs within its detection range, it turns around and moves in the opposite direction. 

• There are M identical ground opponents with defense capability. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/79fd7e2aef30a4fb0925b1cdbfd2c8b80a5ec08436d6d7244a6d0d70829962df.jpg)



Fig. 6. Surveillance mission over a specified battlefield.


The attack occurs with a time step of $T _ { t h r e a t } .$ Each attack removes UAVs in a targeted manner where node(s) with the higher number of neighbors are removed at each threat event. The number of removed UAVs corresponds to $m _ { d }$ . Whenever a tie occurs, it is broken arbitrarily. After $t _ { a d a p t } ,$ the UAV swarm starts to rewire. The network recovery is implemented via link rewiring using Eqs. (7) and (8). 

• The battlefield corresponds to a rectangular grid with size $S = 5 0 0 \times 6 0 0$ . The unit of grid is a patch. The UAV moves with a speed of $\nu _ { u a \nu }$ patch/s, and the speed for ground opponent corresponds to $\nu _ { e }$ patch/s. 

• For comparison purposes, the communication ranges for UAV, $r _ { c }$ are set as ∞, 100/patches, 150/patches, 200/patches, 250/patches. The case for $r _ { c } = \infty$ denotes the case in Tran et al. [2,3]. It should be noted that different UAV communication ranges generate different network topologies of the swarm. Thus, different UAV communication ranges represent different network topologies of the swarm. 

The agent-based model for the UAV swarm and the background settings are developed in Anylogic [20]. The simulation terminates after the first 10 disruption–recovery events. The number of replications for simulation corresponds to $N _ { s }$ . The length of shortest path, $d _ { j { : } } ^ { i }$ , is obtained via Dijkstra's algorithm [19]. The parameter setting for the mission and UAV is given in Table 4. 

# 4.2. Results and discussions

First, we obtain the total number of information received, $y ( t )$ , for each run via Eq. (11). Subsequently, we obtain the average raw values of y(t) and apply S–G filter to obtain the smoothed values of $y ( t )$ . The results under different UAV communication ranges, $r _ { c } ,$ are shown in 


Table 4 Parameters for the experiment.


<table><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td>N</td><td>50</td><td>md</td><td>2</td></tr><tr><td>M</td><td>20</td><td>η</td><td>0.8</td></tr><tr><td>Threat</td><td>200</td><td>μ0</td><td>0.5</td></tr><tr><td>tadapt</td><td>100</td><td>Ns</td><td>100</td></tr><tr><td>νuav</td><td>1</td><td>[θ0, tfinal]</td><td>[0, 2300]</td></tr><tr><td>νe</td><td>0.3</td><td>Nthreat</td><td>10</td></tr><tr><td>m0</td><td>2</td><td>β</td><td>0.2</td></tr><tr><td>m</td><td>1</td><td>Δ</td><td>0.9</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/bdb347160f1dd8f253fa5903415beb0541afeac1f1b0da54c63bc7ca14276d06.jpg)



Fig. 7. y(t) under different UAV communication ranges.


Fig. 7. As shown in the figure, $y ( t )$ increases with $r _ { c }$ for each time point. The capability of information exchange $y ( t )$ indicates the performance of the UAV swarm, and this increases with the UAV communication capability. When $r _ { c } = \infty$ , the case denotes the model used in Tran et al. [2–4], andy(t) stays around the standard performance, i.e., $\mu _ { 0 } N = 2 5$ . The results shown in Fig. 7 validate that the proposed UAV swarm model can be used to capture the effect of dynamic distance among UAVs for the system performance of the UAV swarm. 

It should be noted that y(t) for the first disruption–recovery event relatively exceeds the rest of events. This is because the UAVs are not evenly distributed within the battlefield. Herey(t) remains stable for the rest of the eight disruption–recovery events under each communication range. Additionally, y(t) remains stable under each communication range. This is explained as follows. Based on Eq. (8), $\mu _ { t }$ increases when $N _ { t }$ decreases. Thus, the performance of the UAV swarm is not affected for the first several disruptions. This shows the advantage of the swarm in which the system withstands certain external threats and disruptions. 

Second, given y(t), we adopt the resilience metric in Tran et al. [3], which corresponds to Eq. (10) to obtain the resilience for each disruption–recovery event under different UAV communication ranges, $r _ { c }$ . As shown in Fig. 8, an evident difference does not exist among the resilience values under different UAV communication ranges, $r _ { c }$ . Thus, resilience metric does not reflect the trend that the performance of the UAV swarm (which denotes the capability of information exchange) increases with the communication capability of the UAV, as shown in Fig. 7. This is because the reported resilience metric in Tran et al. [3] is 

calculated based on the ratio of the corresponding capabilities after recovery and that before disruption, respectively. Thus, the resilience is a relative value without reference to the standard system performance. Additionally, given each UAV communication range, $r _ { c } ,$ the resilience metric is not stable, even after the first two disruption–recovery events. 

Third, we apply the proposed resilience metric (which corresponds to Eq. (16)) to obtain the resilience for each disruption–recovery event under different UAV communication ranges, $r _ { c }$ . The result is shown in Fig. 9. As shown in Fig. 9, an evident difference exists among the resilience values under different UAV communication ranges, $r _ { c }$ . Thus, the proposed resilience metric reflects the trend that the performance of the UAV swarm (which denotes the capability of information exchange) increases with the communication capability of the UAV as shown in Fig. 7. This is because the proposed resilience metric reflects the difference between the system performance after each event and standard system performance. Thus, the resilience increases with communication range $r _ { c }$ because the system performance increases with communication range, $r _ { c }$ . Additionally, with the exception of the case corresponding to $r _ { c } = \infty$ , the resilience is higher in the first disruption–recovery event and remains stable for the rest of the nine disruption–recovery events under each communication range. 

Finally, we obtain the total system resilience using Eq. (11) given the resilience value of each disruption–recovery event as calculated by Eqs. (10) and (16). The results are shown in Fig. 10. As shown in the figure, an evident increasing trend exists for the resilience values obtained by the proposed resilience metric under different UAV 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/6a8f4f423056bc4d3fc4aa237ab464300593843cad28065fcf620c7d3fe52a95.jpg)



Fig. 8. Resilience based on Tran et al. [3] for each event.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/e8c5835bd940d70613de8f90bbeffacd649c631b023b295ffa0e941b4bdffc35.jpg)



Fig. 9. Resilience based on the proposed method for each event.


communication ranges, $r _ { c }$ . The result is in agreement with the fact that a UAV swarm with better communication capability exhibits better system resilience, and this enhances the capability of the UAV swarm to complete the assigned surveillance mission over a specified battlefield. Conversely, there is no such trend using Eq. (13) in Tran et al. [3]. 

The proposed model and metric can be used to support the mission planning and design of a UAV swarm. For example, based on the aforementioned results, the administrator or the commander determines the number of UAVs for the swarm to achieve the required resilience, and this ultimately helps the UAV swarm in completing the assigned mission. Additionally, during the UAV swarm design phase, a tradeoff can be made between the communication capability and corresponding cost under the requirement of desired resilience. 

# 5. Conclusions

Given the limitation of its wireless communication capacity, the connectivity and reliability of data transmission for UAVs is affected by the distance between each pair of UAVs. Additionally, the UAVs are portable and physical distances among UAVs are subject to dynamic changes during the mission. Thus, based on the reported models of a UAV swarm, we proposed an improved UAV swarm model via incorporating the effect of distance and its dynamic change among UAVs. The network generated by using the proposed model is unlikely to contain isolated clusters and nodes. A mechanism dealing with dynamic 

changes is also incorporated. Unpredictable threats and inevitable disruptive events correspond to the main causes of failures. Hence, a UAV swarm is designed to accommodate disruptive events and restore its performance. Thus, given the improved network model for a UAV swarm, an improved resilience metric reflecting the difference between the swarm's performance after each event and its standard system performance is proposed. 

Results from the case study reveal that the performance of a UAV swarm remains stable for the first several disruptions. This indicates the advantage of the swarm in which the system withstands certain external threats and disruptions. When compared with traditional network reliability measures, the proposed resilience measure captures the main advantage of UAV swarm (which adapts to disruptive events) and restores its intended performance to complete its assigned mission in terms of system reconfigurations and/or reformations. Additionally, the resilience values obtained by the proposed resilience metric exhibit an increasing trend under different UAV communication ranges, $r _ { c }$ . The result suggests that a UAV swarm with better communication capability exhibits better system resilience. This enhances the capability of a UAV swarm to complete the assigned surveillance mission over a specified battlefield. When compared with the reported resilience measures for a UAV swarm, the proposed resilience measure reflects the trend that the performance of a UAV swarm (which denotes the capability of information exchange) increases with the UAV communication capability. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/84d0eac2-8471-4346-93e7-0b1561f86a62/418e72ff1ede9039b90cf8cf51628bccdce80025d3ffc1c931e6c339f76a43d6.jpg)



Fig. 10. Resilience based on proposed method for each event.


In the study, we focus on the failure of UAVs caused by external threats and disruptions such as malicious attacks by opponents. We did not consider the failure of nodes (UAVs) due to its own malfunction, i.e., we acquiesce that each UAV's reliability corresponds to 1. However, UAVs can also fail due to their own malfunctions in a conflict environment. We plan to incorporate the reliability of nodes in a future study. Additionally, a UAV swarm is highly mobilized, and the topology of a UAV swarm can experience rapid changes during a mission. Thus, UAV speed can also affect frequencies of the topology changes for a UAV swarm. We plan to examine the effect of different UAV speeds on the resilience of a UAV swarm in a future study. 

# Acknowledgment

The study was supported by the National Natural Science Foundation of China (Grant #71701207 and 51705526) and National key Laboratory of Science and Technology on Reliability and Environmental Engineering. 

# References



[1] Li Y, St-Hilaire M, Kunz T. Improving routing in networks of UAVs via scoped flooding and mobility prediction. IEEE; 2013. Wireless Days. 





[2] Tran HT. A complex networks approach to designing resilient system-of-systems[D]. Georgia Institute of Technology; 2016. 





[3] Tran HT, Domerçant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Procedia Comput Sci 2016;95:126–33. 





[4] Tran HT, Domerçant JC, Mavris DN. Evaluating the agility of adaptive command and control networks from a cyber complex adaptive systems perspective. J Defense Model Simul 2015;12(4). 





[5] Barabasi AL, Albert R. Emergence of scaling in random networks. Science 1999;286(5439):509. 





[6] Barabasi AL, Albert R, Jeong H. Mean-field theory for scale-free random networks. Phys A Stat Mech Appl 1999;272(1-2):173–87. 





[7] Barthelemy M. Crossover from scale-free to spatial networks. Europhys Lett 2002;63(6):915. 





[8] Barrat A, Barthelemy M, Vespignani A. The effects of spatial constraints on the evolution of weighted complex networks. J Stat Mech Theory Exp 2005;2005(05):799–803. 





[9] Manna SS, Sen P. A-059: modulated scale-free network in euclidean space. Phys Rev E Stat Nonlinear Soft Matter Phys 2002;66(2):066114. 





[10] Sen P, Banerjee K, Biswas T. Phase transitions in a network with a range-dependent connection probability. Phys Rev E 2002;66(3):037102. 





[11] Labaka $\mathrm { L } ,$ Hernantes J, Sarriegi JM. Resilience framework for critical infrastructures: an empirical study in a nuclear plant. Reliab Eng Syst Saf 2015;141:92–105. 





[12] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35–53. 





[13] Biggs R, Schlüter M, Biggs D, Bohensky EL, Burnsilver S, Cundill G, et al. Toward principles for enhancing the resilience of ecosystem services. Soc Sci Electron Publ 2012;37:421–48. 





[14] Hipsey MR, Hamilton DP, Hanson PC, Carey CC, Coletti JZ, Read JS. Predicting the resilience and recovery of aquatic systems: a framework for model evolution within environmental observatories. Water Resour Res 2015;51(9):7023–43. 





[15] Henry D, Ramirez-Marquez JE. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99:114–22. 





[16] Hosseini S, Barker K, Ramirez-Marquez JE. A review of definitions and measures of system resilience. Reliab Eng Syst Saf 2016;145:47–61. 





[17] Tran HT, Balchanos M, Domerçant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng & System Safety 2017;158:73–84. 





[18] Schafer RW. What is a savitzky-golay filter? IEEE Signal Process Mag 2011;28(4):111–7. 





[19] Dijkstra EW. A note on two problems in connexion with graphs. Numerische Mathematik 1959;1(1):269–71. 





[20] Borshchev A. Multi‐method modelling: AnyLogic. Discr-Event Simul Syst Dyn Manag Decis Mak 2014. 





[21] Bradski G., Kaehler A. Learning openCV, 1st Edition. O’Reilly Media, Inc. 2008. 





[22] Ouyang M, Zhenghua W. Resilience assessment of interdependent infrastructure systems: With a focus on joint restoration modeling and analysis. Reliab Eng Syst Saf 2015;141:74–82. 





[23] Ball MO, Colbourn CJ, Provan JS. Network reliability. Handbook Oper Res Manag Sci 1995;7:673–762. 

