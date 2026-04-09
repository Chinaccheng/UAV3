# Toward the resilience of UAV swarms with percolation theory under attacks

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/cb9409049c0bfee82a94b099519e957a2d7fd120210761aa6e9635383f53de1e.jpg)


Tianzhen Hu a, Yan Zong a, Ningyun Lu a,b,∗, Bin Jiang a,b 

a College of Automation Engineering, Nanjing University of Aeronautics and Astronautics, Nanjing, 211106, China 

b State Key Laboratory of Mechanics and Control of Mechanical Structures, Nanjing University of Aeronautics and Astronautics, Nanjing, 211106, China 

# A R T I C L E I N F O

Keywords: 

Unmanned aerial vehicles 

Swarm 

Percolation 

Resilience 

# A B S T R A C T

Unmanned aerial swarms have been widely applied across various domains. The security of swarms against attacks has been of significance. However, there still exists a lack of quantitatively assessing the unmanned swarm resilience against attacks. Thus, this work adopts the percolation theory to mathematically analyse the resilience of the unmanned aerial swarms after random attacks. In addition to the typically used popularity in the preferential attachment, distance of neighbours is taken into account for modelling unmanned swarms, which is missing in the literature. This improved preferential attachment-based swarm model offers a more precise and realistic description of swarm behaviours. In addition, an attack model is proposed, which can be a description of dynamic attacks. Moreover, this study also utilizes the percolation theory to assess the resilience of swarms after the random attacks. Finally, the simulation results show that the resilience derived using percolation theory aligns with the improved swarm model. The proposed swarm model maintains $7 9 \%$ resilience when $2 0 \%$ of the UAVs are attacked under random attacks, and even $6 9 . 4 \%$ resilience when $2 0 \%$ of the UAVs are attacked under initial betweenness-based attacks. 

# 1. Introduction

Unmanned Aerial Vehicle (UAV) swarms are collections of multiple UAVs that collaborate in a self-organized and self-adaptive manner [1]. Recently, swarms have been widely utilized in many applications, including agriculture, search and rescue, and environmental monitoring [2], resulting in decreased time and resource utilization [3]. Nevertheless, the dynamic and complex environment poses challenges for resilient UAV swarms [4]. 

UAV swarms are susceptible to external factors, such as adversarial attacks. Among these, malware attacks, man-in-the-middle attacks, and Denial-of-Service (DoS) attacks have the most significant impact on UAV swarms [5,6]. When a swarm is attacked, communication among UAVs may be lost [7]. However, UAV swarms are highly dependent on communication among individual UAVs for synchronized operation [8]. This can lead the UAV swarm to suffer from safety hazards and finally lead to task failure. Therefore, it is crucial to ensure the resilience of UAV swarms in the face of external attacks. 

The large-scale swarms usually consist of a large number of UAVs. Thus, it is a challenge to establish an effective model to evaluate the stability of a swarm under the dynamic characteristics and various types of attacks. Some researches have tried to study the movement and resilience of UAV swarms. The work in [9] proposed a swarm model with a dual-adaptive feedback mechanism to prevent swarm-splitting and enhance the coordination and target-reaching ability. The work 

in [10] developed a confrontation model and proposed a resiliencebased strategy selection model that adjusts in real time to enhance the performance and success in mission-critical operations. Inspired by the fact that a UAV swarm is similar to the characteristics of complex systems, methods from the field of complex systems can be applied to analyse a UAV swarm. There has been extensive literature focused on the stabilities of complex systems [11]. In fact, UAV swarms can be mapped into complex network topology, where nodes represent UAVs, while edges denote the communication links between UAVs [12]. 

The resilience of UAV swarms refers to the ability of maintaining functionality and complete missions when several UAVs are attacked [13–15]. UAV swarms need to maintain function and complete missions when encountering various types of attacks. Thus, studying the resilience of UAV swarms has generated considerable research interest. 

# 1.1. Related work

The models for the UAV swarm can be divided into two categories: Barabási-Albert (BA) model and spatial model [16–19]. In the BA model, link probability between UAVs is modelled using the preferential attachment (PA) scheme. Specifically, adding a wireless communication link with probability between two UAVs is proportional to the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/489e859ebc92c12c62ea4a7480ed5aa104308b5e9150191232bbca9673013447.jpg)



OuAV waiting for connection


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/ec0c89a9d3bbd796be1b81bd92a6ada20fe9cf6a9811533774a11a72eb2a0e74.jpg)



UAV in swarm--- communication range — communication link


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/94f061f41bb64085e56d4781ae600b6010f6fb3e8647aa5115613e1f2f26085f.jpg)



newadded communication link



Fig. 1. Generation of UAV swarms with various attachment mechanisms. (a) Preferential attachment. (b) Spatial preferential attachment. (c) Proposed preferential attachment.


UAV degree. As the number of communication links among existing UAVs increases over time, the swarm degree distribution follows a power-law distribution. In Fig. 1(a), due to the high degree of $v _ { 1 }$ , a UAV $v _ { j }$ waiting for a connection is likely to be linked to $v _ { 1 }$ . This is unrealistic since the distance between $v _ { 1 }$ and $v _ { j }$ is greater than the communication range. 

Alternatively, the spatial model applies distance in studying link probability between UAVs [20]. To model effect of distance, two mainly distance functions are studied, namely the exponential and the power function [18,21,22]. For instance, the work of [23] proposed a model of the Internet topology driven by a spatial PA with power distance function. Subsequently, the work in [24] analysed a spatial growth model with exponential distance. The work in [25] discussed how Euclidean distance influences the scaling laws observed in socioeconomic and infrastructure variables in cities. The notable work in [26] developed a fully connected initial UAV swarm generation model for a UAV swarm, and this model is widely used [27]. However, both of these distance functions result in a same problem, that link probability is high even UAVs with high degree are far away from others. Thus, they fail to precisely reflect the real world. 

A UAV swarm is vulnerable to attacks. Typically, there are two types of attacks: communication attacks, which disrupt the communication among UAVs, and UAV attacks. UAV attacks aim to reduce the performance of UAVs through malicious code injection or physical damage, which is focused in this study. But existing attack models focus on static attack and only attack UAVs with degree [28–30]. 

Resilience assessment of UAV swarms has generated considerable recent research interest [31,32]. The pioneering work in [26] introduced a resilience evaluation metric by comparing current swarm performance with standard performance. The work in [33] developed a resilience evaluation method with the absolute time scale and mission requirement for informed agents. Specifically, they focused on partial failure. The work in [34] studied the impact of resource supplementation on the resilience of UAV swarms. It is worth noting that they modelling UAV swarms as a three-layer framework. However, these resilience assessment mainly focused on the global performance of UAV swarm, which are not able to describe specific dynamic of UAV swarm under attacks. Percolation theory is efficient for quantifying the resilience of UAV swarms in the face of attacks. It conducts a comprehensive study into the dynamics of how connectivity degrades when UAVs or links fail. The distinguished work of [35] provided a theoretical explanation for the invulnerability of various complex network topologies to random and intentional attacks. For networks with the same average degree, a wider degree distribution corresponds to a higher degree of resilience [36]. Unfortunately, there is still a lack of percolation studies on UAV swarms to quantitatively assess their resilience. 

# 1.2. Contribution and paper organization

Despite the maturity of complex networks, little attention has been paid to modelling UAV swarm topology. There are instances where full connectivity of a UAV swarm topology cannot be achieved. There is still a need for an efficient method to accurately model a UAV swarm and develop a mathematical dynamic analysis of its internal evolution when suffering attack. Furthermore, there is a lack of analysis from the perspective of complex networks. Moreover, the understanding of the impact of attacks on a complex network of UAV swarm is currently insufficient. To address this problem, this paper models UAV swarms and studies the resilience of UAV swarms under UAV attacks. The main contributions of this paper are summarized as follows. 

• Considering the distance among UAVs, a preferential attachmentbased swarm model is proposed. The model considers the coupling of degree and distance of neighbours, quantifying the ability of UAVs to add communication links to closer UAVs. 

• An attacked model is proposed to perform various attacks on the UAV swarm, in particular, it can describe dynamic attacks. In addition to the random attack, other four targeted attacks are performed. 

• The proposed swarm model is further analysed through a resilience assessment framework by the largest connected component and percolation theory. The proposed framework reveals the effects of random attacks on the resilience of the UAV swarm. 

This paper is organized as follows: Section 2 presents the problem to be addressed and UAV model. In Section 3, a UAV swarm is designed as a hybrid evolution model, and an attack model is proposed. Section 4 depict largest connected component and percolation theory for calculating the resilience of UAV swarm networks under UAV attacks in details. Section 5 verifies the correctness of the proposed theory by carrying out simulations on UAV swarm networks. Section 6 provides conclusions from our work and future directions for this research. 

# 2. Preliminaries and problem description

Definition 1 (UAV Degree ??). For UAV swarms, the degree $k$ of a UAV is defined as the total number of communication links both to and from the UAV. 

Definition 2 (Swarm Degree Distribution $\mathcal { P } ( k ) )$ ). The degree distribution of a swarm, denoted by $\mathcal { P } ( k ) _ { i }$ , is defined as the probability distribution for a UAV having a degree of $k$ . 

Definition 3 (Swarm Stage). The swarm stage refers to the remaining part of a swarm after several UAVs and their corresponding communication links have been removed due to attacks. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/244a9d4b79dcc48f9e5dbe6ac04fe7bb9034564d5923282acf81c6a1f982e50a.jpg)



Fig. 2. Schematic diagram of a UAV swarm suffering a UAV attack.


Typically, a UAV swarm can be modelled by a bi-directed graph $\mathcal { G } = ( \mathcal { V } , \ \mathcal { E } )$ , where $\mathcal { V } = \left\{ v _ { i } \ | \ i = 0 , 1 , 2 , \dots , N \right\}$ denotes the set of UAVs, and $\mathcal { E } ~ = ~ \left\{ e _ { i } ~ | ~ i = 1 , 2 , \ldots , M \right\}$ represents the set of communication links among UAVs. The swarm consists of a backbone UAV [37] (i.e., $v _ { 0 } \big .$ ) and other member UAVs, which are represented by $\overline { { \mathcal { V } } } ~ =$ $\left\{ v _ { i } \mid i = 1 , 2 , \ldots , N \right\}$ . The backbone UAV aims to maintain wireless communication between the UAV swarm and the ground station, whereas other member UAVs can only communicate with UAVs in the swarm. If the UAV $v _ { j }$ is within the communication range of the $i$ -th UAV $v _ { i }$ , there exists a link probability [i.e., $\textstyle \pi ( k _ { i } \mid j ) > 0 ]$ of establishing a communication link between $v _ { i }$ and $v _ { j }$ . Otherwise, $\pi ( k _ { i } \mid j )$ equals zero. This means that there is no wireless communication link between two UAVs, if they are out of communication range with each other. 

# 2.1. UAV swarm models

In the literature, several methods have been proposed to study the UAV link probability $\pi ( k _ { i } \mid j )$ , such as Barabási-Albert (BA) model and the spatial model [16,38]. However, as shown in Fig. 1a, the BA model assumes that a UAV can add links with other UAVs without considering distance. This is not true in the real world. Thus, based on the BA, several spatial models have been proposed to combine the distance ?? between two UAVs [20–22]. Fig. 1(b) describes the spatial model. These models typically apply PA with fitness factors $\eta$ and a distance function $F ( d )$ , and the link probability is given by 

$$
\varPi \left(k _ {i} \mid j\right) = \frac {\eta k _ {i} F (d)}{\sum_ {j} \eta k _ {j} F (d)} \tag {1}
$$

$\eta$ captures the ability of newly added UAV of establishing communication links. In other words, the degree of newly added UAVs is smaller, and the newly added UAVs possess a lower probability of establishing communication links. 

Two types of distance functions are commonly used: the power distance function $F ( d ) = d ^ { - \gamma }$ , where $\gamma > 0$ denotes the tuning parameter [39], and the exponential distance function $F ( d ) = e ^ { - d / r _ { c } }$ , where $r _ { c }$ represents the communication range [24]. For the power distance function $F ( d )$ , its value approaches zero as the distance between two UAVs $v _ { i }$ and $v _ { j }$ increases. Despite this, the UAV degree $k _ { i }$ remains high, resulting in a large link probability $\pi ( k _ { i } \mid j )$ for UAV $v _ { j }$ . The same issue also arises with the exponential distance function. Thus, the consideration of the distance influence factor in [24,39] fails to precisely reflect the real world. A more accurate model that accounts for the communication distance among UAVs is required. 

# 2.2. An attack model

A UAV swarm is vulnerable to attacks. This study mainly focuses on the random attack, which is a type of UAV attack. In Fig. 2, at the time instant ??, when one UAV in the swarm is attacked, the UAV (in red) and the corresponding communication links (in red dashed lines) are removed from the swarm. This causes the swarm to split into two parts. In the UAV attack models, the probability of ${ \mathcal { W } } _ { \alpha } ( k _ { i } )$ is typically 

used to describe the likelihood of a UAV being attacked. The attack probability for each UAV follows 

$$
\mathcal {W} _ {\alpha} \left(k _ {i}\right) = \frac {\left(k _ {i} + \tau\right) ^ {\alpha}}{\sum_ {i = 1} ^ {N} \left(k _ {i} + \tau\right) ^ {\alpha}} \tag {2}
$$

where $\alpha ~ \in ~ ( - \infty , + \infty )$ determines the probability of a UAV being attacked, $\tau$ is a constant value [28,40]. The work of [40] assumed that $\tau$ equals zero, and $k _ { i } \neq 0$ if $\alpha < 0$ . This means that a UAV with the degree $k _ { i }$ will be attacked. If the UAV’s degree is zero, there is no attack in this model. Note that the current static model cannot reflect the dynamic attack strategy, which means that the attacks are updated according to the (communication and UAV) states of the swarm. 

In addition to UAV degree, betweenness centrality is also a key factor in modelling UAV attack probability.1 Betweenness centrality measures the extent to which a certain UAV lies on the shortest communication links between other UAVs. In other words, it helps identify UAVs that play a bridging role in the swarm. However, no work considers both degree and betweenness centrality in the modelling of UAV attacks. 

# 2.3. Resilience assessment

In this work, the resilience assessment evaluates the capability of UAV swarms to remain connected during attacks [42]. Even though the resilience assessment of UAV swarms has been investigated, most studies (e.g., [26,43,44]) focus on studying the resilience from a global perspective. In other words, these studies may overlook the local details of interactions among UAVs, which can be addressed by using site percolation theory. In percolation theory, the Largest Connected Component (LCC) and the percolation threshold are used to assess resilience. The LCC of a UAV swarm is the largest subset of UAVs, ${ \mathcal { V } } _ { L }$ , in which there is a communication link between any two UAVs. The percolation threshold is the critical point at which a UAV swarm transits from being connected to disconnected. 

The work of [35] investigated the resilience of Scale-Free (SF) and Erdős-Rényi (ER) swarm topologies under random and targeted attacks.2 It finds that the percolation threshold in the SF topology is less than that of the ER swarm topology under targeted attacks. Recently, the works in [45,46] analysed the LCC emergence through the percolation process. However, these resilience assessments based on percolation theory may not be applicable to UAV swarms due to the lack of consideration of UAV degree, communication range, and the distance among UAVs. Therefore, a more realistic resilience assessment method (based on the percolation theory) is required for the UAV swarm. 

# 2.4. Problem description

Until now, the use of power or exponential distance functions in UAV swarm models cannot accurately describe swarm behaviour. Meanwhile, the current attack model lacks the consideration of betweenness centrality, and falls into the category of static attacks. However, the recent attack strategies are dynamic, which means that the attacks are updated according to the swarm states. Thus, the resilience assessments based on the current UAV and attack models fail to consider UAV degree, communication range, and distances among UAVs, leading to inaccuracies in resilience assessment. 

Through considering the communication range and distance between UAVs, a UAV swarm model is proposed. In addition, a dynamic attack model using degree and betweenness centrality is presented, which means that the attack strategy is updated according to the UAV 

swarm states. Based on the proposed UAV swarm and dynamic attack model, a novel resilience assessment method is introduced, which can offer accurate resilience assessment results using the percolation theory. 

Overall, the UAV model and attack model in the literature cannot realistically reflect the practices in the real world. We try to offer a solution of realistic modelling of UAV swarms and attacks. Besides, the research on how UAV swarms evolve after being attacked is still insufficient and lacks clarity. Thus, analysing the resilience of the UAV swarm is necessary when facing different types of attacks. 

# 3. Proposed UAV swarm models

# 3.1. UAV swarm model

Here, a UAV swarm model is proposed for generating the UAV swarm. An issue motivated by power distance and exponential distance function is identified. The issue is that the high degree of UAV $v _ { i }$ results in a large link probability for UAV $v _ { j }$ despite the distance function approaching zero as the distance between UAVs increases. To solve this issue, UAV degree and distance function are combined in this study, the link probability in the proposed swarm model is given as: 

$$
\pi \left(k _ {i} \mid j\right) = \beta \frac {k _ {i}}{\sum_ {n = 1} ^ {N _ {t}} k _ {n}} + (1 - \beta) \frac {F \left(d _ {j i}\right)}{\sum_ {n = 1} ^ {N _ {t}} F \left(d _ {j n}\right)} \tag {3}
$$

where $\beta \in ( 0 , \ 1 ]$ is an attachment parameter represents weights of degree and distance, it can adjust the importance of degree and distance. For $\beta = 1$ , the link probability of the proposed model reduced only depend on UAV degree. The proposed model is decided by UAV degree and distance function when $0 < \beta < 1$ . $k _ { i }$ is the degree of ??-th UAV. $N _ { t }$ is denoted as the number of UAVs in the current UAV swarm at time step ??. $d _ { j i }$ is the distance between UAV $v _ { i }$ and $v _ { j }$ and $F ( d _ { j i } )$ is a distance function. 

Inspired from the power and exponential distance function, the curve of the distance function $F ( d _ { j i } )$ is smoothed and decreased. It is natural to think of a smoothed S-shaped function, logistic function. But the logistic function is a increasing function. The distance function is supposed to be decreased and sensitive to communication range. To precisely reflect UAV swarms in the real world, therefore, the proposed distance function is given as: 

$$
F \left(d _ {j i}\right) = \frac {1}{1 + e ^ {\left(d _ {j i} - s \times r _ {c}\right) \times \sigma}} \tag {4}
$$

where $s$ is a constant, it is used to adjust the midpoint of $F ( d _ { j i } )$ . In this study, $s$ is set as 0.5 and the midpoint is half of the communication range. That is if ${ d } _ { j i } = \boldsymbol { s } \times \boldsymbol { r } _ { c }$ , $F ( d _ { j i } )$ equals to 0.5. $F ( d _ { j i } )$ decreases with the distance $d _ { j i }$ and $\sigma$ is a constant that controls the decreasing rate of $F ( d _ { j i } )$ . 

Given UAVs are distributed in a region. Initially, backbone UAV $v _ { 0 }$ establishes $m _ { 0 } - 1$ communication links to $m _ { 0 } - 1$ nearest UAV within the communication range of $v _ { 0 }$ . Hence, there are $m _ { 0 }$ UAVs in the initial UAV swarm. Moreover, the growth of the UAV swarm can be seen in Fig. 1(c). UAV $v _ { j }$ is waiting to connect UAVs in the swarm (i.e. green nodes). If some UAVs in the swarm within the communication range of $v _ { j } { \mathrm { : } }$ , establish $g$ communication links from $v _ { j }$ to $g$ UAVs in the swarm. The probability of establishing communication links is Eq. (3). The selection method of UAV $v _ { i }$ includes three steps based on the link probability. First, generate a random number $r ( r \in [ 0 , 1 ) )$ . Then, calculate the cumulative probability from the link probabilities. If the first cumulative probability is greater than $r$ , select the corresponding UAV $v _ { i }$ . The details of proposed model are described in Algorithm 1. 

Remark 1. The proposed UAV swarm is able to recover the swarm by reinitializing swarm according to Algorithm 1 after being attacked. 


Algorithm 1 Proposed UAV Swarm Generation Method


1: Input: $N$ distributed UAVs $\mathcal{V}$ , Communication range $r_c$ , distance $d_{ji}$ between $v_j$ and $v_i$ , initial number $m_0$ of UAVs in the swarm  
2: Output: UAV swarm $\mathcal{G}$ 3: Initialize an empty graph $\mathcal{G}$ , add backbone UAV $v_0$ into $\mathcal{G}$ .  
4: while $d_{j0} < r_c$ and the number of UAVs in the swarm $< m_0$ do  
5: Select a nearest UAV $v_j$ within $r_c$ of backbone UAV $v_0$ 6: Add $v_j$ into $\mathcal{G}$ 7: Establish a communication link between $v_0$ and $v_j$ 8: end while  
9: for $j = m_0$ to $N - m_0$ do  
10: Add $v_j$ into $\mathcal{G}$ and wait for connection  
11: for 1 to $g$ do  
12: Generate a random number num between [0,1)  
13: for UAV $v_i$ in $\mathcal{G}$ do  
14: if $d_{ji} < r_c$ then  
15: Calculate the link probability $\Pi(k_i \mid j)$ between UAV $v_i$ 16: and UAV $v_j$ according Eq. (3) and Eq. (4)  
17: Cumu = The sum of the link probability $\Pi(k_i \mid j)$ 18: if Cumu > num then  
19: Establish a communication link between $v_i$ and $v_j$ 20: end if  
21: end if  
22: end for  
23: end for  
24: end for  
25: Return $\mathcal{G}$ 

# 3.2. Proposed attack model

An integrated attack model is proposed for consideration of degree and betweenness centrality. The probability of a UAV being attacked is modelled using the following equation. 

$$
\mathcal {W} _ {\mu , l, \alpha} = \frac {\left(\mu \times b _ {i l} + (1 - \mu) \times k _ {i l} + \tau\right) ^ {\alpha}}{\sum_ {i = 0} ^ {n _ {l}} \left(\mu \times b _ {i l} + (1 - \mu) \times k _ {i l} + \tau\right) ^ {\alpha}} \tag {5}
$$

where $\mu$ takes a binary value 0 or 1. $\tau$ is a constant to avoid singularities for $k _ { i l } = 0$ , $b _ { i l } = 0$ and $\alpha \ : < 0$ . ?? represents the UAV swarm is at the ??-th $( l \ge 0 )$ ) swarm stage. If $l = 0$ , it refers to the initial not attacked UAV swarm, $n _ { 0 } = N$ . The ?? parameter characterizes the current UAV swarm after each round of attack. Thus, the proposed attack model can be dynamic attack. $b _ { i l }$ is the betweenness centrality of UAV $v _ { i } \in \mathcal V _ { l }$ , which measures the number of the shortest paths between all UAV pairs $( v , w )$ $( v , w \neq i )$ . $k _ { i l }$ is the degree of UAV $v _ { i }$ . When $\mu = 0$ , a UAV with degree $k _ { i l }$ will be attacked. Otherwise, a UAV with betweenness centrality $b _ { i l }$ will be attacked. The value of ?? $( \alpha \in ( - \infty , + \infty ) )$ ) determines the probability of a UAV being attacked and $n _ { l } = | \mathcal { V } _ { l } |$ is the number of UAVs at the ??-th swarm stage. 

Five types of attacks can be conducted by the proposed attack model, including random attack and four targeted attacks. When $\alpha =$ 0, each UAV is with the same likelihood of being attacked, representing random attacks, which is described in Section 5.3. The case $\alpha \ \to \ \infty$ refers to the targeted attack. Four targeted attacks are described in Section 5.4 including Initial Degree-based Attack (ID), Initial Betweenness-based Attack (IB), Recalculated Degree Attack (RD) and Recalculated Betweenness Centrality Attack (RB). 

# 4. Resilience assessment of UAV swarms

In this study, resilience assessment of UAV swarms under UAV attacks is analysed through percolation theory. Percolation theory describes geometric features of clustered UAV components in swarms when UAVs and links are attacked and removed [13]. In network 

science, one usually removes each node or link with probability $q$ to realize the percolation. For one thing, we try to solve the issue of resilience of the proposed swarm model against the topology variances, which is consistent with percolation theory. 

The resilience assessment focuses on the size of LCC in the swarm stage. LCC is the largest set of UAVs $S \subset V$ , which can be identified where there is a path from any UAV $u$ to any other UAV $v$ in $\mathcal { G }$ . If the LCC remains, the UAV swarm is considered to be functional. Given a UAV swarm $\mathcal { G } _ { i }$ , assume that $\mathcal { G }$ is under UAV attack and a fraction of UAVs are removed from $\mathcal { G }$ . Consider the LCC of $\mathcal { G }$ and define the resilience of $\mathcal { G }$ as 

$$
R = \frac {1}{N} \sum_ {i = 0} ^ {q _ {c}} \frac {N _ {L} (i)}{N} \tag {6}
$$

where $N _ { L } ( i )$ represents the number of UAVs in LCC after ?? UAVs have been attacked. $q$ is the ratio of attacking and removing UAVs. $q _ { c }$ is the percolation threshold, representing the critical ratio. $N$ is the number of UAVs in swarms. The range of $R$ lies between 0 and 1, large values represent higher resilience of the UAV swarm. 

Before attacked, the swarm degree distribution can be analysed by mean field approach [47]. For sufficiently long time, substitute Eqs. (3) and (4), the connectivity $k _ { i } ( t )$ of the $i$ -th UAV with distance $d$ evolves according to the following continuous time evolution equation: 

$$
\frac {\partial k _ {i}}{\partial t} = g \beta \frac {k _ {i} (t)}{\sum_ {n = 1} ^ {N _ {t}} k _ {n}} + g (1 - \beta) \frac {1 / \left(1 + e ^ {\left(d _ {j i} - s \times r _ {c}\right) \times \sigma}\right)}{\sum_ {n = 1} ^ {N _ {t}} 1 / \left(1 + e ^ {\left(d _ {j i} - s \times r _ {c}\right) \times \sigma}\right)} \tag {7}
$$

where the first and second terms describe the increment in $k _ { i }$ due to popularity and distance respectively. Note that $\begin{array} { r } { \sum _ { n } k _ { n } = 2 g t } \end{array}$ , with the factor of 2 coming from the undirected nature of the commuunication links. In order to analyse the scale-free characteristic of proposed network, the degree distribution is expected as: 

$$
P (k) \sim \frac {2}{\beta} \left(\frac {\beta k}{2}\right) ^ {- \gamma} \tag {8}
$$

where $\begin{array} { r } { \gamma = \frac { 2 } { \beta } + 1 } \end{array}$ 

??UAV attacks change the swarm degree distribution. Generating function is applied in studying the changes. The generating functions $G _ { 0 } ( x )$ of swarm degree distribution $P ( k )$ is: 

$$
G _ {0} (x) = \sum_ {k = 0} ^ {\infty} P (k) x ^ {k} \tag {9}
$$

and $G _ { 1 } ( x )$ of UAV swarms can be written as: 

$$
G _ {1} (x) = \sum_ {k = 1} ^ {\infty} \frac {k P (k)}{\langle k \rangle} x ^ {k - 1} \tag {10}
$$

where $\frac { k P ( k ) } { \langle k \rangle }$ denotes the probability that the UAV reached by following ⟨ ⟩an link has degree $k$ , $G _ { 1 } ( x )$ is the corresponding generating function. 

Assuming a link connects to the LCC with probability $R _ { L }$ . If UAV ?? connects LCC through a chosen link, it requires UAV ?? not be attacked and there is at least one link to LCC except the chosen link. Therefore, a self-consistent equation can be obtained: 

$$
R _ {L} = (1 - q) \left[ 1 - G _ {1} \left(1 - R _ {L}\right) \right] \tag {11}
$$

Hence, the probability that a randomly chosen UAV belongs to LCC, denoted as $S$ , is developed: 

$$
S = (1 - q) \left[ 1 - G _ {0} \left(1 - R _ {L}\right) \right] \tag {12}
$$

When $q  q _ { c }$ , $R _ { L }  0$ . Import Taylor series, Eq. (11) turns to : 

$$
1 = \left(1 - q _ {c}\right) \sum_ {k = 1} ^ {\infty} \frac {k P (k)}{\langle k \rangle} x ^ {k - 1} + o \left(R _ {L}\right) \tag {13}
$$

$q _ { c }$ can be obtained by simplified Eq. (13): 

$$
q _ {c} = 1 - \frac {1}{\zeta - 1} \tag {14}
$$


Table 1 Parameters for the simulations.


<table><tr><td>Parameter</td><td>Value</td><td>Description</td></tr><tr><td>L</td><td>103</td><td>Side length of square region</td></tr><tr><td>A</td><td>106</td><td>Region area</td></tr><tr><td>N</td><td>103</td><td>Number of UAVs</td></tr><tr><td>β</td><td>0.9</td><td>An attachment parameter represents weights of degree and distance</td></tr><tr><td>m0</td><td>4</td><td>Initial number of UAVs in the swarm</td></tr><tr><td>g</td><td>1</td><td>Number of communication links a new UAV makes with existing UAVs when it joins the swarm</td></tr><tr><td>s</td><td>0.5</td><td>A constant to adjust the midpoint of distance function F(dji)</td></tr><tr><td>rc</td><td>250 (m)</td><td>Communication range of UAVs</td></tr><tr><td>τ</td><td>1</td><td>A constant to avoid singularities for kil=0, bll=0 and α&lt;0 in Eq. (5)</td></tr><tr><td>σ</td><td>0.05</td><td>A constant to control the decreasing rate of distance function F(dji)</td></tr></table>

where $\begin{array} { r } { \zeta = \frac { \langle k ^ { 2 } \rangle } { \langle k \rangle } } \end{array}$ ⟨??⟩ , $\begin{array} { r } { \langle k \rangle = \sum _ { k = 1 } ^ { \infty } P ( k ) k , \langle k ^ { 2 } \rangle = \sum _ { k = 1 } ^ { \infty } P ( k ) k ^ { 2 } . } \end{array}$ ?? of scale-free network can be approximately by: 

$$
\zeta = \left| \frac {2 - \gamma}{3 - \gamma} \right| \times g, \gamma > 3 \tag {15}
$$

The percolation threshold $q _ { c }$ is combined to assess the resilience of UAV swarms. A higher $q _ { c }$ suggests that the UAV swarm can withstand a large amount of attacks before disconnection, signifying greater resilience. On the contrast, a lower $q _ { c }$ suggests lower resilience. On the whole, LCC and percolation threshold $q _ { c }$ are key indicators of the resilience of the UAV swarms. The resilience assessment of the proposed UAV swarm is described in Algorithm 2. 

# Algorithm 2 Resilience Assessment of The Proposed UAV Swarm

1: Input: UAV swarm $G$ 

2: Output: The resilience of ?? ?? and percolation threshold $q _ { c }$ 

3: for 1 to $N - 1$ do 

4: One UAV $v _ { a }$ is being attacked with probability Eq. (5) 

5: Remove the attacked UAV $v _ { a }$ and corresponding communication links 

6: Calculate $N _ { L }$ 

7: end for 

8: Solve Eq. (6) and Eq. (14) 

9: Return ??, and $q _ { c }$ 

# 5. Numerical simulations

# 5.1. Configurations

A UAV swarm has been efficiently employed in surveillance missions [48]. When performing surveillance missions, a UAV swarm hovers over an area and is exposed to attacks and threats [49]. Since the severe consequences of malicious attacks and threats, it is vital to evaluate a UAV swarm and ensure mission accomplishment. 

In this section, a case study is conducted to perform a surveillance mission. Numerous UAVs are distributed in a given square region. Each of these UAVs exchange information with UAVs within communication range through HELLO message. Next, these distributed UAVs establish communication links among UAVs until all UAVs are added into the UAV swarm. Therefore, a UAV swarm is established through communication among UAVs. Then, the established UAV swarm performs a surveillance mission in the square region. The simulations are performed using python 3.7.2 and networkx 2.6.3 on Ubuntu 18.04.6, with an intel i7-10700F processor, and 16 GB RAM. The parameters setting for the mission and UAV swarm are given in Table 1. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/9fa4fc68152efd803c44ebe68e1966b8e4d5fa5f4be72da9d6ff4089d9578b0a.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/e4b334b5f404744fb14ec365d6fed6e031ab105b73797939132ac34cd650ed35.jpg)



(b)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/7933c79251e116b3cceab89f00f2520f8fadae23a583e7976d89f03efc991feb.jpg)



（c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/f9415fb0bbb5c264c3a7b5835a3ddca843879a81495c831e10216e1be1c80ad8.jpg)



(d)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/61925ebb4db5fd8e3d6b5121da519257c98e64f95a3a4db69b87e7f859855bdf.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/9e2850a6abcb7a38ffc11c5587215ffb72b92749e28fa1af1fa09d6aae73e764.jpg)



(f)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/9e8ef058defd7959057e9799828edbccce78cbffc5c8f11173da50b6d2c1f271.jpg)



(g）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/9978de63bd7c9abbd6e9898a890a78f268a139b55d71a3b5fe7608b422684f1d.jpg)



Fig. 3. A UAV swarm of different models with varying communication ranges. (a) A UAV swarm of BA model, $r _ { c } = 2 5 0 ~ \mathrm { m }$ . (b) A UAV swarm of spatial model with power distance function, $r _ { c } = 2 5 0 ~ \mathrm { m }$ . (c) A UAV swarm of spatial model with exponential function, $r _ { c } = 2 5 0 ~ \mathrm { m }$ . (d) A UAV swarm of spatial model with exponential function, $r _ { c } = 8 0 0 ~ \mathrm { m }$ . (e) A UAV swarm of [26], $r _ { c } = 2 5 0 ~ \mathrm { m }$ . (f) A UAV swarm of [26], $r _ { c } = 8 0 0 ~ \mathrm { m }$ . (g) A UAV swarm of proposed model, $r _ { c } = 2 5 0 ~ \mathrm { m }$ . (h) A UAV swarm of proposed model, $r _ { c } = 8 0 0 ~ \mathrm { m }$ .


# 5.2. Simulation results

The resilience of the proposed UAV swarm is assessed under five attack types that are commonly encountered in performing surveillance missions. For convenience of visualization, Fig. 3 shows the comparison between the BA model, the spatial model with power distance function, the spatial model with exponential distance function, model in [26] and the proposed UAV swarm model with 100 UAVs. As can be seen in Fig. 3(a), almost all UAVs of the BA model connect UAVs out of communication range without communication range limitation. Fig. 3(b) shows that the spatial model with power distance function exists few links with UAVs out of communication range. It may be reasonable that both BA model and spatial model with power distance function do not consider communication range. Although the spatial model with exponential distance function considers communication range, part of UAVs connect UAVs beyond communication range in Fig. 3(c). Therefore, BA model, spatial model with power and exponential distance function are not realistic for modelling UAV swarm. 

In contrast, as depicted in Fig. 3(e), the UAV swarm implemented using the method described in [26] appears to be scattered. Comparing Fig. 3(e) and Fig. 3(g), it is evident that communication links of the proposed model is consistently more concentrated in the centre of the region. Besides, model in [26] did not initialize the UAV swarm quite well, because they neglect the distance between initial UAVs. Thus, it leads to first $m _ { 0 }$ UAVs connect to each other even beyond communication range (e.g. red line). 

Different $r _ { c }$ : When generating UAV swarm, a UAV would rather connect UAVs with closer neighbours. Besides, a UAV swarm of different models with varying communication range can be observed in Fig. 3. The spatial model with exponential distance function is similar when $r _ { c } = 2 5 0 ~ \mathrm { m }$ and $r _ { c } ~ = ~ 8 0 0 ~ \mathrm { m }$ . All of them are unrealistic. Both our proposed model and [26] perform well when $r _ { c } / L$ is small. As shown in Figs. 3(e) and 3(f), UAVs add communication links with closer neighbours when $r _ { c } / L = 2 5 0 / 1 0 0 0 = 0 . 2 5$ . But model in [26] fails to add communication links to closer neighbours when $r _ { c } / L$ increases. As shown in Figs. 3(f) and 3(h), $r _ { c } / L = 2 5 0 / 1 0 0 0 = 0 . 8 ,$ , which means that most UAVs are within the communication range. Fig. 3(f) shows that a UAV connect to UAVs far away in [26]. On the contrary, the proposed model connects to closer neighbours, as shown in Fig. 3(h). Since the impact of communication range $r _ { c }$ on the link probability $\textstyle \pi ( k _ { i } \mid j )$ 

can be easily adjusted based on $\beta$ in the proposed model. Furthermore, global efficiency and local efficiency should be employed as additional metrics to compare these two models. 

Efficiency: In this part, the global efficiency $E _ { \mathrm { g l o b a l } }$ and local efficiency $E _ { \mathrm { l o c a l } } ( i )$ are analysed. Global efficiency is often used to assess the overall effectiveness of a UAV swarm in terms of information flow and communication. It is calculated as the average of the inverse of the shortest path lengths between all pairs of UAVs in the swarm. Local efficiency is particularly relevant for studying communication patterns within specific regions. It is calculated as the average of the inverse of the shortest path lengths between neighbours of a UAV. 

The global efficiency and local efficiency of different UAV swarm models are reported in Table 2. The global efficiency of BA model is the largest among all the models. While it is not suitable for modelling UAV swarm due to its unrealistic. The global efficiency of spatial model with exponential and power distance function is good, but the local efficiency of both spatial models is zero. It means they lack the ability of resistance to attacks on a small scale. The global efficiency of the swarm using approach in [26] is slightly higher than that of the proposed model. But this observation suggests that a few long-distance connections between UAVs increase the global efficiency of [26]. It is consistent with the red line in Fig. 3(e), which shows two UAVs establishing a connection despite being beyond the communication range. On the other hand, the local efficiency of the proposed model is significantly higher than that of the UAV swarm using approach in [26]. This implies that the UAVs of the proposed model are tightly connected, so even if one UAV is attacked, its neighbours can still maintain communication. 

Distance function: As mentioned previously, various distance functions have been studied [24,26,50]. The distance function of $F ( d )$ in Eq. (4) is displayed in Fig. 4. $\sigma$ is set as 0.5 to control the decreasing rate of $F ( d _ { j i } )$ [51,52]. Apparently, when ?? exceeds communication range, $F ( d )$ of exponential [24] and power [50] distance function are close to 0. But the probability of connection is non-zero when UAV with high degree. This leads to controversial in reality, UAVs cannot receive information out of range. Distance function in [26] decreases, which is what we expect. But smoothed trends are preferred such as power and exponential, since in path loss models, signals attenuation is a smoothed decreasing curve [53]. The aim of our proposed distance function $F ( d )$ is establishing a probability when distance $d$ between 


Table 2 Efficiency of UAV swarms with different models.


<table><tr><td>Efficiency</td><td>Model in [26]</td><td>Proposed Model</td><td>BA Model</td><td>Spatial Model with exponential distance function</td><td>Spatial Model with power distance function</td></tr><tr><td>Global</td><td>0.2560 ± 0.0058</td><td>0.2223 ± 0.0092</td><td>0.4276 ± 0</td><td>0.2521 ± 0.0174</td><td>0.2081 ± 0.0081</td></tr><tr><td>Local</td><td>0.2182 ± 0.0440</td><td>0.2689 ± 0.0310</td><td>0.2017 ± 0</td><td>0</td><td>0</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/bc51af778c0edfffb3d6d462e6e76b719727d75e7256bd21530952c42c3f43d9.jpg)



Fig. 4. Various distance function.


UAVs smaller than communication range, $F ( d )$ decreases smoothly. Most importantly, when $d > r _ { c }$ , $F ( d )$ needs to close to 0. 

Degree distribution: As shown in Fig. 5, an unusual degree distribution in the proposed model, characterized by a majority of UAVs with degree two and a small number of UAVs with high degree. Here, $N = 1 0 0 0$ . It is interesting to note that there are even fewer UAVs with degree one compared to those with degree two. This is due to the neighbours of some UAVs may less than 2. This degree distribution is distinct from those seen in both the BA model and spatial models. The effect of $F ( d )$ preventing the model from scale-free power-law. Approximately, the distribution closely follows a power-law pattern, except for several UAVs with large degree. Higher $\beta$ responds to closer power-law. It is worth noting that the presence of clustering, a phenomenon absent in the spatial models, may be observed in the proposed model. This can be attributed to the higher likelihood of UAVs closer in space being connected to each other. Besides, the degree distribution of UAV swarm with $N \ = \ 2 0 0 0$ is analysed, and the results are similar to those for $N = 1 0 0 0$ . 

# 5.3. Resilience analysis in random attack

• Random Attack (RND): The proposed attack model responds to random attack when $\alpha ~ = ~ 0$ , $l ~ = ~ 0$ in Eq. (5). Thus, RND attack is the simplest attack strategy, $1 / N$ is the probability of each UAV in swarms being attacked. That is at ??-th time, hackers randomly choose one UAV to attack, then the attacked UAV and corresponding communication links are removed. 

Continuous random attacks are performed to UAV swarms to further evaluate the resilience of UAV swarms by the percolation theory. As shown in Fig. 6(b), after continuing RND attack and removing 26 of 100 UAVs, the UAV swarm breaks into pieces. Fig. 6(c) shows that after RND attack 87 UAVs, there remains a LCC of size 5. 

The proposed UAV swarm model is applied with different $\beta$ under continuous RND attacks. Eq. (6) is utilized to measure resilience of proposed swarm model. Resilience of different models is summarized in Table 3 under RND attacks. The resilience of BA model is outstanding 

under continuous RND attacks [35]. The proposed model with $\beta = 0 . 9$ is a slightly larger than that with $\beta ~ = ~ 0 . 1$ under RND attacks. The resilience of proposed model is quite similar between model in [26] under RND attacks. The resilience of two spatial models is poor, which may be the effect of their zero local efficiency in Table 2. 

# 5.4. Resilience analysis in targeted attack

Then it is also intuitive to ask for attack strategies that target the most relevant UAVs. These strategies are termed as target attacks and calculated by Eq. (5). 

• Initial Degree-based Attack (ID): The proposed attack model is ID attack when $\mu = 0$ , $l = 0$ , $\alpha  \infty$ . The attack model focuses on degree based attack if $\mu = 0$ . $l = 0$ means the attack is based on the degree of UAVs at the initial swarm stage. Thus, the UAV with the highest degree is attacked if $\alpha \to \infty$ . 

• Initial Betweenness-based Attack (IB): The proposed attack model is IB attack when $\mu = 1$ , $l = 0$ , $\alpha \to \infty$ . The attack model is betweenness centrality based attack if $\mu = 1$ . Furthermore, the UAV with the highest betweenness centrality of the initial swarm stage is attacked if $l = 0$ , $\alpha \to \infty$ . 

• Recalculated Degree Attack (RD): The proposed attack model is RD attack when $\mu = 0$ , $\alpha \to \infty$ . The UAV with highest degree is attacked at the ??-th swarm stage. The difference between ID is that RD depends on the degree of the current ??-th swarm stage not the initial swarm stage. 

• Recalculated Betweenness Centrality Attack (RB): The proposed attack model is RB attack when $\mu ~ = ~ 1$ , $\alpha \ \to \ \infty$ . The UAV with highest betweenness centrality is attacked at the ??-th swarm stage. The difference between IB is that RB depends on the betweenness centrality of the current $l$ -th swarm stage not the initial swarm stage. 

Besides, resilience of model in [26] is also be calculated for continuous targeted attacks. As summarized in Table 4, the resilience of the proposed model is greater than that of the model in [26] for ID, IB, RD and RB when $\beta$ is 0.9 and 0.1. BA model is more resilient than model in [26]. Similarly, the resilience of two spatial models is extremely poor under four targeted attacks, which may be a direct result of their zero local efficiency in Table 2. Overall, it is fair to compare the proposed model with model in [26] under RND and four targeted attacks. 

Furthermore, the proposed UAV swarm model is applied with different $\beta$ under five types of continuous attacks. Similarly, we use Eq. (6) to measure the resilience of the proposed swarm model. Ten iterations are applied to improve the consistency of the results. As detailed in Fig. 7, the value of $R$ is nearly unaffected by different $\beta$ under RND. Apparently, the proposed model is more resilience and can tolerant much more attack when facing RND. The proposed model is the least resilient when facing RB attack. Undering RND is far more resilient than undering RB attack. The order of resilience is $R N D > I B > I D > R D >$ ????. Additionally, the resilience of the proposed model decreases as $\beta$ increases under ID, IB, and RD attacks. It may be reasonable to suppose that the proposed model becomes more dependent on UAV degree and the degree distribution approaches to power-law with the increasing of $\beta$ . Moreover, it can be observed that only resilience under IB and RB fluctuates with the iterations. This seems to imply that betweenness centrality requires the use of approximation algorithms in large scale swarms. Thus, the resilience fluctuates under IB and RB attack for a 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/b128b9408caf338875654dd45087dcdb0e16905efe05be3a1a34316d93ce7c61.jpg)



Fig. 5. Degree distribution of the proposed model with different $\beta$ , $N = 1 0 0 0$ .



Table 3 Resilience of different models under RND attacks.


<table><tr><td>Attack</td><td>β = 0.9 in our model</td><td>β = 0.1 in our model</td><td>Model in [26]</td><td>BA Model</td><td>Spatial Model with exponential distance function</td><td>Spatial Model with power distance function</td></tr><tr><td>RND</td><td>0.4200</td><td>0.4092</td><td>0.4201</td><td>0.4524</td><td>0.1662</td><td>0.1356</td></tr></table>


Table 4 Resilience of different models under four targeted attacks.


<table><tr><td>Attack</td><td>β = 0.9 in our model</td><td>β = 0.1 in our model</td><td>Model in [26]</td><td>BA Model</td><td>Spatial Model with exponential distance function</td><td>Spatial Model with power distance function</td></tr><tr><td>ID</td><td>0.2050</td><td>0.2634</td><td>0.1349</td><td>0.2014</td><td>0.0053</td><td>0.0072</td></tr><tr><td>IB</td><td>0.2634</td><td>0.3431</td><td>0.1771</td><td>0.2381</td><td>0.0055</td><td>0.0074</td></tr><tr><td>RD</td><td>0.1748</td><td>0.2184</td><td>0.1206</td><td>0.1815</td><td>0.0048</td><td>0.0063</td></tr><tr><td>RB</td><td>0.1240</td><td>0.11271</td><td>0.1057</td><td>0.1637</td><td>0.0048</td><td>0.0064</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/c06586b7ee9eac562df942b472e1071643e1dff1b706d41bdffc41e5a2bf367f.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/7139562b5b2db2926ac9a838bbd8309b96eb6e592f6448f3a06d6a2581667cc7.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/c6fa15a3974309953f4d005978dda0ee0af51a6589574531195709d7e7efa622.jpg)



(c）



Fig. 6. A UAV swarm after continuing RND and randomly removing nodes.


given proposed UAV swarm model. The proposed model is resilient when $\beta$ is 0.9. 

Then, LCC of the proposed swarm model is investigated by 10 iterations with $\beta \ = \ 0 . 9$ . As shown in Fig. 8(e), $S$ is the size of LCC, $q$ represents ratio of removed UAVs. The proposed swarm model maintains $7 9 \%$ resilience when $2 0 \%$ of the UAVs are attacked under random attacks, and even $6 9 . 4 \%$ resilience when $2 0 \%$ of the UAVs are attacked under IB. As described in Fig. 8(a), at the beginning, LCC under IB sharply drop consistent with ID and RD, then slightly decrease under continuous UAV attacks. Therefore, the resilience under ID and RD are close. The resilience of the proposed model is the lowest under RB, but it is approximately comparable to that of ID and RD, with a value of $q _ { c }$ . Similarly, the fluctuations observed under IB and RB attack result from the approximation algorithms used for calculating betweenness centrality. 

Subsequently, percolation threshold $q _ { c }$ is utilized to assist analysis the resilience of the proposed model with different $\beta$ . Ten iterationss are employed, the results are shown in Fig. 9. The percolation threshold $q _ { c }$ is nearly 0.8 under RND close to $q _ { c }$ calculate by Eq. (14), 0.780. Due 

to the difficulty in obtaining analytical solutions, we employ numerical simulations to investigate the percolation threshold of the UAV swarm under ID, IB, RD and RB attack. The percolation threshold $q _ { c }$ under IB approximately equals to that under RND. This indicates that continuing to attack and remove even $8 0 \%$ UAVs can destroy the proposed UAV swarm model under IB. However, the difference between IB and RND increases as $\beta$ increases. The value of $q _ { c }$ is a around 0.6 under ID, except when $\beta = 0 . 3$ . It is higher than percolation threshold under IB. This suggests that for the initial attack type, the proposed model under IB is resilient than ID. Nevertheless, the percolation threshold $q _ { c }$ under RD is a little higher than that under RB, and they are the lowest. Thus, the proposed model is more resilient under RD than under RB. 

# 5.5. Discussion

Our results show that the proposed UAV model is resilient against RND, ID, IB, RD and RB attacks. Furthermore, the proposed UAV model could be applied to ensure the completion of missions. However, some limitations are worth noting. Although resilience analysis of UAV swarms based on percolation theory is efficient, the UAV agents are controlled by second-order dynamics. Future work should therefore include UAV six degrees of freedom (6-DOF) model to achieve better simulation outcomes. In addition, the performance of UAV swarms focuses on the number of LCC. More factors, such as recovery, energy and mission completion, should be considered when describing the performance of UAV swarms in the future. 

# 6. Conclusions

A model with degree and distance is proposed for a UAV swarm based on PA. Besides, an attack model is proposed for modelling dynamic attacks. To analyse the resilience of this proposed model, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/0fccef1df37cfb5893cb8ffe57111e5c71a882952e1fc438a45242f079e63df3.jpg)



Fig. 7. Resilience of the proposed model under RND, ID, IB, RD and RB attack, $m = 1 , N = 1 0 0 0$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/991fe869b1385e2a8996a7180f46fba2b5619b92b3287e65956ad6f42a6e7eaa.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/375829ae4ae3e949f3009a1605a28f18b92dc29dc11bed4eb0b35d40a99f3b58.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/762ec39262c3201230b1fbcdda4ae48ff65525a3af8bfef3fa7575da5d7a6aea.jpg)



（c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/6996f4bd5781c03c67a31c72456c44fb2acdeb41a2272b2c8a98170d3f51e38f.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/acfab905d5f21b81056cc07c81553d4515d47940dc977255e716016fe73526d6.jpg)



(e)



Fig. 8. LCC under different attacks. (a) RND (b) ID (c) IB (d) RD (e) RB, $m = 1 , N = 1 0 0 0$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/a8e6451a-e448-41bd-87e8-76155b7084da/9560569ab0ee7ce12aa526b126a18d4ea62f9d5781ec0706122626858a917867.jpg)



Fig. 9. Percolation threshold $q _ { c }$ for different $\beta$ under different attacks, $m = 1 , N = 1 0 0 0$ .


various attack scenarios, including RND, ID, IB, RD and RB, are performed. For resilience assessment, two vital measures are considered: LCC and percolation threshold. Therefore, based on percolation theory, a comprehensive framework is proposed for assessing the resilience of UAV swarms. The model is identified resilient against attacks. Our further studies can focus on enhancing resilience of UAV swarm by increasing the number of links per UAV in each step. 

# CRediT authorship contribution statement

Tianzhen Hu: Writing – original draft, Validation, Methodology, Investigation, Formal analysis, Conceptualization. Yan Zong: Writing – review & editing, Supervision. Ningyun Lu: Writing – review & editing, Supervision, Funding acquisition. Bin Jiang: Writing – review & editing, Funding acquisition. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Acknowledgements

This study was supported by the International Cooperation and Exchange of the National Natural Science Foundation of China (Grant No. 62020106003) and the National Natural Science Foundation of China (Grant No. 62273176 and No. 62303221). 

# Data availability

The authors do not have permission to share data. 

# References



[1] Feng Q, Liu M, Dui H, Ren Y, Sun B, Yang D, et al. Importance measure-based phased mission reliability and UAV number optimization for swarm. Reliab Eng Syst Saf 2022;223:108478. http://dx.doi.org/10.1016/j.ress.2022.108478. 





[2] Andrews J, Poole J, Chen W. Fast mission reliability prediction for unmanned aerial vehicles. Reliab Eng Syst Saf 2013;120:3–9. http://dx.doi.org/10.1016/j. ress.2013.03.002. 





[3] Phadke A, Medrano FA, Sekharan CN, Chu T. An analysis of trends in UAV swarm implementations in current research: Simulation versus hardware. Drone Syst Appl 2024;12:1–10. http://dx.doi.org/10.1139/dsa-2023-0099. 





[4] Folke C, Carpenter SR, Walker B, Scheffer M, Chapin T, Rockström J. Resilience thinking: Integrating resilience, adaptability and transformability. Ecol Soc 2010;15:20. http://dx.doi.org/10.5751/es-03610-150420. 





[5] Yaacoub JP, Noura H, Salman O, Chehab A. Security analysis of drones systems: Attacks, limitations, and recommendations. Internet Things 2020;11:100218. http://dx.doi.org/10.1016/j.iot.2020.100218. 





[6] Hunt K, Agarwal P, Zhuang J. On the adoption of new technology to enhance counterterrorism measures: An attacker-defender game with risk preferences. Reliab Eng Syst Saf 2022;218:108151. http://dx.doi.org/10.1016/j.ress.2021. 108151. 





[7] Fotouhi A, Qiang H, Ding M, Hassan M, Giordano LG, Garcia-Rodriguez A, et al. Survey on UAV cellular communications: Practical aspects, standardization advancements, regulation, and security challenges. IEEE Commun Surveys Tuts 2019;21(4):3417–42. http://dx.doi.org/10.1109/COMST.2019.2906228. 





[8] Lopez MA, Baddeley M, Lunardi WT, Pandey A, Giacalone JP. Towards secure wireless mesh networks for UAV swarm connectivity: Current threats, research, and opportunities. In: 2021 17th international conference on distributed computing in sensor systems. DCOSS, IEEE; 2021, p. 319–26. http://dx.doi.org/10. 1109/dcoss52077.2021.00059. 





[9] Xu B, Bai G, Liu T, Fang Y, an Zhang Y, Tao J. An improved swarm model with informed agents to prevent swarm-splitting. Chaos Solitons Fractals 2023;169:113296. http://dx.doi.org/10.1016/j.chaos.2023.113296. 





[10] Zhang C, Liu T, Bai G, Tao J, Zhu W. A dynamic resilience evaluation method for cross-domain swarms in confrontation， Reliab Eng Syst Saf 2024:244:109904. http://dx.doi.org/10.1016/j.ress.2023.109904. 





[11] Cai Q, Alam S, Liu J. On the robustness of complex systems with multipartitivity structures under node attacks. IEEE Trans Control Netw Syst 2020;7(1):106–17. http://dx.doi.org/10.1109/TCNS.2019.2919856. 





[12] Jiang B, Shen Q, Shi P. Neural-networked adaptive tracking control for switched nonlinear pure-feedback systems under arbitrary switching. Automatica 2015;61(C):119–25. http://dx.doi.org/10.1016/j.automatica.2015.08.001. 





[13] Li M, Liu RR, Lü L, Hu MB, Xu S, Zhang YC. Percolation on complex networks: Theory and application. Phys Rep 2021;907:1–68. http://dx.doi.org/10.1016/j. physrep.2020.12.003. 





[14] Wandelt S, Xu Y, Sun X. Measuring node importance in air transportation systems: On the quality of complex network estimations. Reliab Eng Syst Saf 2023;240:109596. http://dx.doi.org/10.1016/j.ress.2023.109596. 





[15] Wang S, Guo Z, Huang X, Zhang J. A three-stage model of quantifying and analyzing power network resilience based on network theory. Reliab Eng Syst Saf 2024;241:109681. http://dx.doi.org/10.1016/j.ress.2023.109681. 





[16] Barabasi AL, Albert R. Emergence of scaling in random networks. Science 1999;286(5439):509–12. http://dx.doi.org/10.1515/9781400841356.349. 





[17] Tran HT, Domerant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Procedia Comput Sci 2016;95:126–33. http://dx. doi.org/10.1016/j.procs.2016.09.302. 





[18] Soares DJB, Tsallis C, Mariz AM, Silva LRd. Preferential attachment growth model and nonextensive statistical mechanics. Europhys Lett 2005;70(1):70–6. http://dx.doi.org/10.1209/epl/i2004-10467-y. 





[19] Liang Y, Xia Y, Yang XH. Hybrid-radius spatial network model and its robustness analysis. Phys A 2022;591:126800. http://dx.doi.org/10.1016/j.physa.2021. 126800. 





[20] Barthélemy M. Spatial networks. Phys Rep 2011;499(1–3):1–101. http://dx.doi. org/10.1016/j.physrep.2010.11.002. 





[21] Cinardi N, Rapisarda A, Tsallis C. A generalised model for asymptotically-scalefree geographical networks. J Stat Mech Theory Exp 2020;2020(4):043404. http://dx.doi.org/10.1088/1742-5468/ab75e6. 





[22] Oliveira R, Brito S, da Silva LR, Tsallis C. Statistical mechanical approach of complex networks with weighted links. J Stat Mech Theory Exp 2022;2022(6):063402. http://dx.doi.org/10.1088/1742-5468/ac6f51. 





[23] Yook SH, Jeong H, Barabási AL. Modeling the Internet’s large-scale topology. Proc Natl Acad Sci 2002;99(21):13382–6. http://dx.doi.org/10.1073/pnas. 172501399. 





[24] Barthélemy M. Crossover from scale-free to spatial networks. Europhys Lett 2003;63(6):915. http://dx.doi.org/10.1209/epl/i2003-00600-6. 





[25] Ribeiro FL, Meirelles J, Ferreira FF, Neto CR. A model of urban scaling laws based on distance dependent interactions. R Soc Open Sci 2017;4(3):160926. http://dx.doi.org/10.1098/rsos.160926. 





[26] Bai G, Li Y, Fang Y, Zhang YA, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020;193:106602. http://dx.doi.org/10.1016/j.ress.2019.106602. 





[27] Motlagh NH, Kortoçi P, Su X, Lovén L, Hoel HK, Haugsvær SB, et al. Unmanned aerial vehicles for air pollution monitoring: A survey. IEEE Internet Things J 2023;10(24):21687–704. http://dx.doi.org/10.1109/JIOT.2023.3290508. 





[28] Dong G, Gao J, Du R, Tian L, Stanley HE, Havlin S. Robustness of network of networks under targeted attack. Phys Rev E 2013;87(5):052804. http://dx.doi. org/10.1103/PhysRevE.87.052804. 





[29] Freitas S, Yang D, Kumar S, Tong H, Chau DH. Evaluating graph vulnerability and robustness using tiger. In: Proceedings of the 30th ACM international conference on information & knowledge management. 2021, p. 4495–503. http: //dx.doi.org/10.1145/3459637.3482002. 





[30] Lu QL, Sun W, Dai J, Schmöcker JD, Antoniou C. Traffic resilience quantification based on macroscopic fundamental diagrams and analysis using topological attributes. Reliab Eng Syst Saf 2024;247:110095. http://dx.doi.org/10.1016/j. ress.2024.110095. 





[31] Liu T, Bai G, Tao J, Zhang YA, Fang Y. A multistate network approach for resilience analysis of UAV swarm considering information exchange capacity. Reliab Eng Syst Saf 2024;241:109606. http://dx.doi.org/10.1016/j.ress.2023. 109606. 





[32] Sun X, Hu Y, Qin Y, Zhang Y. Risk assessment of unmanned aerial vehicle accidents based on data-driven Bayesian networks. Reliab Eng Syst Saf 2024;248:110185. http://dx.doi.org/10.1016/j.ress.2024.110185. 





[33] Zhou X, Huang Y, Bai G, Xu B, Tao J. The resilience evaluation of unmanned autonomous swarm with informed agents under partial failure. Reliab Eng Syst Saf 2024;244:109920. http://dx.doi.org/10.1016/j.ress.2023.109920. 





[34] Kong L, Wang L, Cao Z, Wang X. Resilience evaluation of UAV swarm considering resource supplementation. Reliab Eng Syst Saf 2024;241:109673. http://dx.doi. org/10.1016/j.ress.2023.109673. 





[35] Albert R. Error and attack tolerance of complex networks. Nature 2000;406. http://dx.doi.org/10.1515/9781400841356.503. 





[36] Cohen R, Havlin S. Complex networks: Structure, robustness and function. Cambridge University Press; 2010, http://dx.doi.org/10.1017/cbo9780511780356. 





[37] Tsao KY, Girdler T, Vassilakis VG. A survey of cyber security threats and solutions for UAV communications and flying ad-hoc networks. Ad Hoc Netw 2022;133:102894. http://dx.doi.org/10.1016/j.adhoc.2022.102894. 





[38] Menczer F. Evolution of document networks. Proc Natl Acad Sci 2004;101(suppl_1):5261–5. http://dx.doi.org/10.1073/pnas.0307554100. 





[39] Manna SS, Sen P. Modulated scale-free network in Euclidean space. Phys Rev E 2002;66(6):066114. http://dx.doi.org/10.1103/physreve.66.066114. 





[40] Gallos LK, Cohen R, Argyrakis P, Bunde A, Havlin S. Stability and topology of scale-free networks under attack and defense strategies. Phys Rev Lett 2005;94:188701. http://dx.doi.org/10.1103/PhysRevLett.94.188701. 





[41] Brandes U. A faster algorithm for betweenness centrality. J Math Sociol 2001;25(2):163–77. http://dx.doi.org/10.1080/0022250X.2001.9990249. 





[42] Woods DD. Four concepts for resilience and the implications for the future of resilience engineering. Reliab Eng Syst Saf 2015;141:5–9. http://dx.doi.org/10. 1016/j.ress.2015.03.018. 





[43] Phadke A, Medrano FA. Towards resilient UAV swarms-A breakdown of resiliency requirements in UAV swarms. Drones 2022;6:340. http://dx.doi.org/10.3390/ drones6110340. 





[44] Sun Q, Li H, Zhang Y, Xie Y, Liu C. A baseline assessment method of UAV swarm resilience based on complex networks. In: 2021 IEEE 19th world symposium on applied machine intelligence and informatics. SAMI, IEEE; 2021, p. 000083–6. 





[45] Gotesdyner O, Gross B, Porath DVB, Havlin S. Percolation on spatial anisotropic networks. J Phys A 2022;55(25):254003. http://dx.doi.org/10.1088/1751-8121/ ac6914. 





[46] Amit G, Ben Porath D, Buldyrev SV, Bashan A. Percolation in fractal spatial networks with long-range interactions. Phys Rev Res 2023;5:023129. http://dx. doi.org/10.1103/PhysRevResearch.5.023129. 





[47] Barabási AL, Albert R, Jeong H. Mean-field theory for scale-free random networks. Phys A 1999;272(1–2):173–87. http://dx.doi.org/10.1016/s0378- 4371(99)00291-5. 





[48] Tang J, Duan H, Lao S. Swarm intelligence algorithms for multiple unmanned aerial vehicles collaboration: A comprehensive review. Artif Intell Rev 2023;56(5):4295–327. http://dx.doi.org/10.1007/s10462-022-10281-7. 





[49] Javaid S, Saeed N, Qadir Z, Fahim H, He B, Song H, et al. Communication and control in collaborative UAVs: Recent advances and future trends. IEEE Trans Intell Transp Syst 2023;24(6):5719–39. http://dx.doi.org/10.1109/tits. 2023.3248841. 





[50] Barrat A, Barthélemy M, Vespignani A. The effects of spatial constraints on the evolution of weighted complex networks. J Stat Mech Theory Exp 2005;2005(05):P05003. http://dx.doi.org/10.1088/1742-5468/2005/ 05/p05003. 





[51] Erciyes K. Complex networks: An algorithmic perspective. Boca Raton: CRC Press; 2014, http://dx.doi.org/10.13140/2.1.1608.1281. 





[52] Cohen R, Erez K, Daniel, Havlinl S. Resilience of the internet to random breakdowns. Phys Rev Lett 2006;85(21):4626–8. http://dx.doi.org/10.1515/ 9781400841356.507. 





[53] Isabona J, Oghu E, Omasheye O. Path loss and models: A survey and future perspective for wireless communication networks. Int J Adv Netw Appl 2023;15:5892–907. http://dx.doi.org/10.35444/IJANA.2023.15209. 

