# The resilience evaluation of unmanned autonomous swarm with informed agents under partial failure

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a72143a51bc127c77d156706d3d96dfb5a93c31b732f739d378dc00874b68b0d.jpg)


Xinxin Zhou a, Yun Huang a, Guanghan Bai a,\*, Bei Xu b, Junyong Tao a 

$^{a}$ Laboratory of Science and Technology on Integrated Logistics Support, College of Intelligent Science, National University of Defense Technology, Changsha 410073, China 

<sup>b</sup> The School of General Aviation, Nanchang Hang Kong University, Nanchang 330063, China 

# ARTICLEINFO

# Keywords:

Unmanned autonomous swarm 

Self-recovery 

Partial failure 

Resilience metric 

Couzin-leader model 

# ABSTRACT

The resilience analysis of unmanned autonomous swarms under various disturbances provides valuable insights for the design of unmanned swarms and mission planning. Current studies usually focus on the complete failure of the individual in the swarm where the individual and/or its connections are removed and/or rewired. In this paper, we study the issue of swarm resilience with some agents suffering partial failure. Three motion models and their corresponding resilience processes are proposed respectively given three partial failure modes. Furthermore, an improved resilience evaluation metric considering the absolute time scale and minimum mission performance requirement is proposed. The collective behavior and resilience process under different partial failures and strategies are studied through simulations. The results reveal the swarm resilience decreases as the swarm size increases, and the swarm resilience is sensitive to degree and location failure strategy. 

# 1. Introduction

Many multi-agent models have been developed by physicists, biologists, and engineers to depict collective behaviors of natural swarms such as bees, bird flocks, schools of fish, etc. [1-4]. They have shown that emergent phenomena can be produced through local interactions between agents with limited intelligence. For instance, unmanned swarm with informed individuals is an important class of unmanned swarm. Couzin et.al [3] first proposed such model to show that coordinating with nearby neighbors is sufficient to result in the group's movement in a certain direction. In this model, informed individuals serve as the central authority and are in charge of guiding the group. This model is currently the subject of a surge that has many potential applications in engineering, such as unknown forest environment exploration [5], moving target seeking [6], omnidirectional patrolling [7] and etc. 

With many different unmanned autonomous swarms developed, it is crucial to study the associated failure problems caused by internal failures and/or failures by external disruptions [8-15]. Internal failures of individuals in unmanned autonomous swarms are caused by failures of internal component and subsystems, such as propulsion and power, control systems, etc. [16-17], while external disruptions are caused by malicious attacks and/or severe environment. The attack on unmanned autonomous swarms can be divided into two types, namely hard killing 

and soft killing [18-22]. Hard killing refers to the use of physical weapons, such as missiles, laser, nets, projectile, etc. Soft killing, which neutralizes threat using non-lethal methods, usually takes jamming or signal hijacking to damage the swarm. Soft-kill attacks contain high-power microwave attacks, electromagnetic attacks, etc. 

Given different failure modes and analysis, reported studies have been carried on the swarm reliability [23-27], robustness [28], survivability [29]. However, these performance criteria mainly focused on the anti-interference ability. Because the unmanned autonomous swarm is a self-organization system which has a certain self-recovery ability to deal with its own failure, interference and disruptions, resilience is more suitable to describe the capabilities of the swarm. The resilience is the ability to absorb, recover from, and more successfully adapt to failures or disruptions. The concept of resilience has broadened the focus of complex engineering systems beyond traditional discussions of robustness, reliability, and risk management. Since being introduced by Holling [30] in ecological system, resilience has placed greater emphasis on a system's adaptability and recoverability, in addition to its ability to absorb disruptions. This transition is readily observed across government and industry, and is beginning to alter the way in which we approach systems engineering [31]. The need for conducting resilience analysis become important for increasingly interconnected and complex systems, such as those under the purview of the military [32], national infrastructures [33-34], and traffic networks [35-36], gas [37-38], and 

# Notation List

$\Delta t$ : the time step. 

$d_{i}(t)$ : the desired direction of individual $i$ 

$\alpha$ : the repulsive distance. 

$\beta$ : the attraction distance. 

$c_{i}(t)$ : the position vector of individual $i$ 

$\nu_{i}(t)$ : the velocity vector of individual $i$ 

$\omega$ : the social interaction weight. 

g : the preferred direction of the informed individual. 

$\gamma$ ： field of perception. 

$\theta$ : the maximum turn angle in $\Delta t$ 

$\tau$ : the adjustment factor. 

$\rho$ : the recovery factor. 

$\zeta$ : thevolatilityfactor. 

$\sigma$ : the total performance factor. 

$\delta$ : the absorption factor. 

$\mu$ : the absolute time sensitivity factor. 

$B$ : the reference time. 

$\Delta$ : the time importance factor. 

unmanned swarms [10-15]. When evaluating the resilience of a system, an analyst should consider what the system is resilient to, since "the resilience of a system can be measured only in terms of the specific threat (input), and different attacks would generate different consequences trajectories for the same system [39]". Because the fault accommodation and recovery of the swarm emerge as a whole through the 

local interaction mechanism between individuals under disturbance. Therefore, we may know the fault of the individual, how individual's failure propagates within the swarm and how the swarm recovers from the disturbance are still unclear. 

Previous studies usually focus on the complete failure of individuals in swarm, and directly remove the individual [11-15]. For individuals in a swarm, complete failure of an individual means the all the functions of individual is completely lost and can't be perceived by other individuals during interaction. However, many real systems are more complex by 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/2fffb2b3cd968577d060eced3734ebf56c7d278b4ebf1a43128ed3cd12ebeb1a.jpg)



Fig. 2. The $\nu_{\text{group}}$ change process of resilience process in Fig. 1.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/b1a303da9d42f4fbd2742e213c9dcf8cce43149fff0d98fc30688672fa2ce1a8.jpg)



(a) Adjustment stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/bf5e914e23ff6156046a14e6821a5f6bcb8578f726ba051392f395f7ef26089d.jpg)



(b) Stabilization stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/8c8f5f8e1e011e0e7b616f8ee0db641d8d783d711ad5feeec2e95182046ded44.jpg)



(c) Disturbance occurs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/407335bccd64e79ee7d1e20002bc7d6e4343f4670912364d20408fdc6cb61d73.jpg)



(d) Propagation of disturbance


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/7250bb0ae9822ed9eda106ad7d309634dc117930d85b5bd23244ce66c00f1f4b.jpg)



(e) Recovery


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/1fcfd2a37137635faf8513cd0364658b39b47bcd0266ff79eeda4c012ae2dbc6.jpg)


(f) Stable stage 

Attrack 

Repulse 

Leader 

Follower 

Failure 


Fig. 1. Resilience process with some individuals being immobile under partial failure.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f8717c817e3006ec985ada043ca5ab02e7ff61af96c63494726a10df6684a0d0.jpg)



(a) Adjustment stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/ad97f50df5cb2a602dc12b8a5ade2e2c6d598732c03b381da8846e3c4938db61.jpg)



(b) Stabilization stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/080c35a7ad8a057ad82c3d12c54e68cdea2aa67e8270cb57786fc846676d4875.jpg)



(c) Disturbance occurs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f7db12b959e41733a07442cbc0be629ac4d42667b35a980a2ed5e1a62b142e78.jpg)



(d) Propagation of disturbance


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/e6a8e755b4110562ea7a77750335d41bdb692576574d221356cb86f0cde0af33.jpg)



(e) Recovery


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/619e5a923641d3059ab8dd609953ab891efbdf1d5d24861d8154b631fec68e14.jpg)



(f) Stabilization stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f4e8e0eadd0916306b39571b5b760db00866da5f5dad857e06c03d6d1b74224d.jpg)



Fig. 3. Resilience process with random motion of some individuals under partial failure.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/db986326c4f7e3cba94f7208a4ae4fa8e0ff3c953583e00684291578e16a828a.jpg)



Fig. 4. The $\nu_{\mathrm{group}}$ change process of resilience process in Fig. 3.


nature, there exist states apart from complete failure and perfect functioning [40-42]. Tuteja deals with three models for a unit under the assumption that each unit attains three modes - normal (N), partial failure (P) and complete failure (F) [43]. Jenny stated that a partial failure mode is defined as a mode in which a component has suffered catastrophic failure but the system still retains some fraction of its original capacity to do work. The fraction of capacity lost depends on the function and location of the failed component [44]. Won stated that the partial failure of an equipment unit generally implies a partial loss of its functions [45]. In general, partial failure refers to a reduction in system/component functionality or partial loss of functionality. In this 

paper, we mainly focus on the swarm resilience of individuals in unmanned swarms encountering partial failures. Partial failure of an individual refers to the case that some subsystems in the individual lose the function while other subsystems are still working normally. Both hard killing and soft killing all may lead to partial failure of individuals in the swarm. Xu studies the resilience of UAS with partial failure where the motion subsystem is malfunctioning. The number of anchored individuals is adopted as performance indicator to evaluate resilience [10]. However, individuals affected by the faulty individuals are not stationary. In addition, because the individual is moving constantly, it is difficult to distinguish whether it is anchored or not, and the definition of the "anchor state" had not been defined clearly. Thus, it is unreasonable to describe these individuals affected by individuals with crash fault as "failed individuals". 

Regarding the quantitative analysis of resilience, many resilience metrics and evaluation methods can be found in reported studies. The first quantitative resilience evaluation method was proposed by Bruneau et.al, which measures the degradation in the quality of community infrastructure [46]. The concept of resilience loss, also known as "a resilience triangle" was proposed later, which has been widely accepted as a fundamental guide for resilience evaluation [47-48]. However, the resilience triangle method is not able to show the dynamic behaviors. Henry and Ramirez-Marquez use three system states to respect system's state, which are stable original state, disrupted state and stable recovered state [49]. The advantage of this metric is that both disruption and recovery phases are considered. However, Henry and Ramirez-Marquez's metric is not as intuitive as the resilience metric expressed by one numerical value. Recently, several general resilience metrics have been proposed. Nan and Sansavini proposed an integrated metric for evaluating the resilience of independent infrastructures [50]. Their metric considered robustness, rapidity in disruptive phase, performance loss in disruptive phase, etc. Tran et. al proposed a resilience metric, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f04d3d70487000e6b570ec1598794d3bb37b66c93654a4bdc83a742ec9ec5d34.jpg)



(a) Adjustment stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/cd4675d13533ef3d1646e34e5e4b5f0e777012f722229cd3e6a7febaa524289b.jpg)



(b) Stabilization stage


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/98f6b8493e1db70b1ccb0f6e70b31422fdaf3a1708606811d8def6f855631c96.jpg)



(c) Disturbance occurs


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/23bdfc84aecbf8d5238de8f78d878f7358173af0e4ead80e9763789682c21d5e.jpg)



(d) Propagation of disturbance Attract Rep


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/b51cf4cbc55b82159f4b0e3a04cba748f84c92cb31f8db66b41efebfc91c0f2c.jpg)



(e) Recovery


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a2b699fddf499cc3ed48421124e0ed48ebad0993e485b766ad4a71004c0a3d5f.jpg)



(f) Stable stage



Fig. 5. Resilience process with some individuals moving in the opposite direction of the swarm under partial failure.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3cffae7873c96b092095cefe25e85343bcd41b84ceee4072cf838880c43fc95d.jpg)



Fig. 6. The $\nu_{\mathrm{group}}$ change process of resilience process in Fig. 5.


which constructs the recovery factor, total performance factor, absorption factor, volatility factor, and recovery time factor to obtain a comprehensive resilience indicator [51]. On this basis, Cheng propose an improved resilience metric considering absolute time, which is constructed in the form of a summation of two capacities, namely absorptive and restorative capacities [52]. A weight coefficient is assigned to each capacity to enhance the flexibility according to various system requirements of stakeholders. The metric also considers the impact of absolute time scale. Liu proposes a resilience metric that considers the minimum performance level of the mission, which thought only performance above the minimum performance can be considered as the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/481abd74f458d752326dd2f6e2d39576670651fd30b231aa55837702870dcdef.jpg)



Fig. 7. An example of resilience process for the improved resilience metric.


effective performance [53]. 

However, the above resilience metrics contain some shortcomings when they are applied to analyze the resilience of unmanned swarm. Tran and Nan' resilience metric is based on a relative time scale, which is not appropriate to evaluate swarm's resilience correctly on different time scales. In addition, when the performance drops suddenly and recover to a certain level, Nan's metric is close to 0, which is inappropriate for swarm. Cheng's metric is based on an absolute time scale, and the resilience process of the system is a comprehensive process of survivability and recovery. However, the mathematic form of Cheng's metric overemphasizes recovery process, which may obtain incorrect resilience when the combined effect of system degradation and recovery is the same [52]. Liu propose a new resilience metric considering the mission's requirement for minimum the performance [53]. However, when a swarm performance curve is a gradual decline form, and unable to recover any lost performance over time, Liu's method is unable to recognize such situation, and may mistakenly perceive this situation as 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/6d3ec1526f50c29a8d62fc2cb155b51d46403794b41bea06f61198e14b35e741.jpg)



Fig. 8. Performance curves at different time scales.



Table 1 Resilience calculation of Tran's method.


<table><tr><td>Case number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Resilience value</td><td>0.4149</td><td>0.5329</td><td>0.6629</td><td>0.8051</td><td>0.9595</td><td>1.1264</td></tr><tr><td>Case number</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Resilience value</td><td>0.4158</td><td>0.5360</td><td>0.6691</td><td>0.8153</td><td>0.9750</td><td>1.1483</td></tr></table>

having good resilience. Thus, it is necessary to develop an improved resilience metric which is more appropriate for such dynamic unmanned swarm and overcome the limitations of the reported metrics. 

In this paper, we concentrate on the emergent behavior of the swarm, and study the resilience of the swarm under partial failure. The major contributions of this article are summarized as follows. (1) We developed three motion models of the individual respectively given three typical partial failure modes in the swarm and give their corresponding resilience processes. (2) We propose an improved resilience metric that overcomes the drawbacks of existing resilience metrics for analyzing unmanned swarm. (3) The collective behavior and resilience process of unmanned swarms under different partial failures and strategies are investigated through simulations. The rest of this article is organized as follows. In Section 2, we introduce the classic Couzin-leader model as our swarm model, and adopt the average velocity as the swarm performance. Motion models under different partial failures and corresponding resilience processes are developed in Section 3. Section 4 gives an improved resilience metric and conduct comparisons with reported metrics. The collective behavior and resilience process of unmanned swarms under different partial failures and strategies are investigated through simulations in Section 5. 


Table 2 Resilience calculation of Liu's method.


<table><tr><td>Case number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Resilience value</td><td>0.5799</td><td>0.6099</td><td>0.6399</td><td>0.6699</td><td>0.6999</td><td>0.7299</td></tr><tr><td>Case number</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Resilience value</td><td>0.5799</td><td>0.6099</td><td>0.6399</td><td>0.6699</td><td>0.6999</td><td>0.7299</td></tr></table>


Table 3 Resilience calculation of Cheng's method.


<table><tr><td>Case number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Resilience value</td><td>0.165214</td><td>0.1898355</td><td>0.21857354</td><td>0.2510539</td><td>0.286988</td><td>0.3264705</td></tr><tr><td>Case number</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Resilience value</td><td>0.1633609</td><td>0.1812938</td><td>0.20233784</td><td>0.22591892</td><td>0.2521878</td><td>0.281050</td></tr></table>


Table 4 Resilience calculation of the improved method with $B = 20$ $\Delta = 0.8$


<table><tr><td>Case number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Resilience value</td><td>0.2221</td><td>0.2799</td><td>0.3447</td><td>0.4159</td><td>0.4929</td><td>0.5761</td></tr><tr><td>Case number</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Resilience value</td><td>0.1401</td><td>0.1770</td><td>0.2187</td><td>0.2645</td><td>0.3145</td><td>0.3688</td></tr></table>

# 2. Unmanned swarm model

We use Couzin-leader model as our swarm movement model [3], the Couzin-leader model is extended from the Couzin model [2]. The Couzin-leader model is a classic distributed swarm model under multi-agent framework, which can achieve a coordinated group movement with the leadership of some informed agents. The main feature of Couzin-leader model is that a few individuals in the swarm have the pertinent information, and information can be transferred within groups without communicating with each other explicitly. Swarm members are not aware of which individuals are informed individuals. The advantage of this model is that it can avoid a large amount of communication between individuals. When the swarm performs missions under weak communication environment where various disturbances take places, such as electromagnetic interference, weather effect, etc., and the 


Table 5 Resilience calculation of the improved method with $B = 30$ $\Delta = 0.6$


<table><tr><td>Case number</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>Resilience value</td><td>0.1598</td><td>0.1995</td><td>0.2444</td><td>0.2938</td><td>0.3472</td><td>0.4048</td></tr><tr><td>Case number</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td></tr><tr><td>Resilience value</td><td>0.0791</td><td>0.0988</td><td>0.1215</td><td>0.1463</td><td>0.1734</td><td>0.2028</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/381b329e7bd98f1dc7342fa66fa0f71089daef7e548e956d1230f983eddf72c6.jpg)



Fig. 9. Performance curve considering mission performance requirement.



Table 6 The resilience calculation results.


<table><tr><td></td><td>RTran</td><td>RLiu</td><td>RCheng</td><td>RImproved</td><td></td></tr><tr><td>System A</td><td>0.55979</td><td>0.625</td><td>0.055777</td><td>0.36798</td><td>0.25548</td></tr><tr><td>System B</td><td>0.69522</td><td>0.60</td><td>0.052071</td><td>0.22929</td><td>0.18277</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/2675e286edcc0961788ee662989e3c64f8a56a8d20f5717ce838b1c94519c947.jpg)



Fig. 10. Performance curve considering minimum performance requirement.


unmanned swarm usually selects a few unmanned platforms to receive mission target information, unmanned swarm based on swarm models with leaders like Couzin-leader model to solve this problem is efficient [57]. 

Consider a swarm of $N$ individuals moving about in a two-dimensional plane with constant speed $\nu$ , the initial direction of all individuals is generated arbitrarily. The time step is $\Delta t$ . Every individual has a position vector $c_{i}(t)$ and a direction vector $\nu_{i}(t)$ , which attempts to maintain a minimum distance $\alpha$ i.e., repulsion distance between itself $i$ and other individual $j$ at all times by turning away from neighbors within that range. 

$$
d _ {i} (t + \Delta t) = - \sum_ {j \neq i} \frac {c _ {j} (t) - c _ {i} (t)}{\left| c _ {j} (t) - c _ {i} (t) \right|} \tag {1}
$$

where $d_{i}$ represents the desired direction of travel individual $i$ . This simulates individuals acting to maintain to avoid collisions. And avoidance is the highest priority. 

If neighbors of individual $i$ are not detected in collision avoidance region, but have distance with $i$ greater than $\alpha$ and less than $\beta$ , then the 


Table 7 The resilience calculation results.


<table><tr><td></td><td>RTran</td><td>RLiu</td><td>RCcheng</td><td>RImproved</td><td></td></tr><tr><td>System A</td><td>0.522649</td><td>0.71</td><td>0.478457</td><td>0.381365</td><td>0.25548</td></tr><tr><td>System B</td><td>0.252698</td><td>0.71</td><td>0.104099</td><td>0</td><td>0</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/8c510432d5bce61effbfd9d1093cc00a0ff98da4edafe625762c8ab7dedbcbd3.jpg)



Fig. 11. Performance curves for different concavo-convexities.



Table 8 The resilience calculation results.


<table><tr><td></td><td>RTran</td><td>RLiu</td><td>RCcheng</td><td>RImproved</td></tr><tr><td>Case 1</td><td>1.429727</td><td>0.875</td><td>0.4314</td><td>1.3124</td></tr><tr><td>Case 2</td><td>1.429727</td><td>0.875</td><td>0.4554101</td><td>1.3124</td></tr><tr><td>Case 3</td><td>1.429727</td><td>0.875</td><td>0.479</td><td>1.3124</td></tr></table>

individual $i$ will tend to become attracted and aligned with neighbors within a local interaction range $\beta -\alpha$ 

$$
d _ {i} (t + \Delta t) = \sum_ {j \neq i} \frac {c _ {j} (t) - c _ {i} (t)}{\left| c _ {j} (t) - c _ {i} (t) \right|} + \sum_ {j = i} \frac {v _ {j} (t)}{\left| v _ {j} (t) \right|} \tag {2}
$$

$d_{i}(t + \Delta t)$ is converted to the unit vector $\widehat{d}_i(t + \Delta t) = \frac{d_i(t + \Delta t)}{|d_i(t + \Delta t)|}$ . 

At the same time, a proportion $Lp$ of the individuals are given the information about a preferred direction (denoted by a unit vector $g$ ), which are referred as leaders in this paper. All other individuals have no particular preferred direction. Individuals are not aware of which individuals are informed. Informed individuals balance the informed direction and their social interactions with a weighting term $\omega$ . $\widehat{d}_i(t + \Delta t)$ is replaced by $d_i^{\prime}(t + \Delta t)$ , which is given as follows. 

$$
\dot {d} _ {i} (t + \Delta t) = \frac {\widehat {d} _ {i} (t + \Delta t) + \omega g}{| \widehat {d} _ {i} (t + \Delta t) + \omega g |} \tag {3}
$$

If $\omega = 0$ , vector $g$ has no influence, and individuals have no desire to move in any specific direction. As $\omega = 1$ , individuals balance the preference to move in direction $g$ and to maintain their social interactions with their group members. As $\omega$ exceeds 1, individuals are heavily influenced by their preferred direction $g$ . Every individual has a field of perception, denoted as $\gamma$ . The field of perception takes direction of movement as the center line, $\frac{\gamma}{2}$ left and $\frac{\gamma}{2}$ right. An individual can only detect individuals in the field of perception. Every individual has a max turning rate $\theta$ . Individuals can turn through an angle of, at most of, $\theta \Delta t$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/412a18ba9629a2028bed834b534b892435a6abd41a6b5e125ba35a2b7525ca98.jpg)



Fig. 12. Area division in unmanned swarms.



Table 9 Simulation parameters.


<table><tr><td>Parameter</td><td>Symbol</td><td>Value</td></tr><tr><td>Speed(/m/s)</td><td>ν</td><td>10</td></tr><tr><td>Zone of interaction / m</td><td>α</td><td>100</td></tr><tr><td>Zone of repulsion / m</td><td>β</td><td>10</td></tr><tr><td>The max turning angle</td><td>θ</td><td>2</td></tr><tr><td>Time step / s</td><td>Δt</td><td>0.2</td></tr><tr><td>Number of individuals</td><td>N</td><td>10,50,100,200</td></tr><tr><td>Failure proportion</td><td>P</td><td>0-1</td></tr><tr><td>Social interaction weight of informed individuals</td><td>ω</td><td>0.5</td></tr><tr><td>Leader proportion</td><td>Lp</td><td>0.3</td></tr></table>

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/52790e52fc82e14ca89de8656282d0f158ec897f1be5c521f04417793637e247.jpg)



(a) The velocity evolution process of $p = 10\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/2a225d11559d2880c952d18aa9394b4195a5eb8eda243cf4c1b5a7fff3bb5b03.jpg)



(b) The velocity evolution process of $p = 20\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/daca0e4e7a18ae769a319800f0c106a5a03574d59e18f7f989322b9625e50679.jpg)



(c) The velocity evolution process of $p = 30\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a16bcfe46debe28ff9f977bb38564388ee840e9320d9bf43d999fdf3843e02d4.jpg)



(d) The velocity evolution process of $p = 50\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/c20ebd7fdd97efc0f9535ae1afbf9c0b93a41664522dfbcef758b10bbc277e11.jpg)



(e) The velocity evolution process of $p = 60\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/dc588a175c2a898b2b56e1921c1b29421178ee44ce0466e7365b3be1da3d0368.jpg)



(f) The velocity evolution process of $p = 70\%$



Fig. 13. The velocity evolution process of the swarm under different partial failure proportions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/c77b8f78aeb59277ea6ae82687a34bd8df0832775773b3900c805d78e3be1075.jpg)



Fig. 14. The resilience with different failure proportions.


in every step. If the angle between $\nu_{i}(t)$ and $\vec{d}_i(t + \Delta t)$ is less than $\theta \Delta t$ , the individual $i$ can get their desired direction $\vec{d}_i(t + \Delta t)$ , otherwise they turn $\theta \Delta t$ towards it. 

The main feature of Couzin-leader is that group can move in the direction of informed individuals, therefore we adopt the average velocity of the swarm towards the informed individuals to describe the performance of the group, which is defined as follows. 

$$
v _ {\text {g r o u p}} (t) = \frac {1}{N} \sum_ {1} ^ {N} v _ {i} (t) g \tag {4}
$$

where $\nu_{i}(t)$ is the vector velocity of individual $i$ i.e., $d_{i}(t + \Delta t), g$ is the vector velocity of the informed individuals, $\nu_{\text{group}}(t)$ reflects the navigation accuracy of the swarm. 

# 3. Motion models of individual under partial failure and swarm resilience process

Swarm may encounter a variety of countermeasures in adversarial environments. Countermeasures can be grouped as physically destroying the individual, interfering the individual, etc. These countermeasures and internal failure may cause partial failure of individuals in the swarm. The movement states of individuals in swarms may show different forms under partial failure modes. In this section, we develop three motion models under three partial failure modes, i.e., immovability, random movement, and move in opposite direction. 

# 3.1. Immovability

# 3.1.1. Motion model of immovability

When a single individual or few individuals experience motor subsystem failure or control system failure, the form of movement of the individual may appear immobile. While other subsystems continue to function normally, they can still perceive other individuals, and vice versa. Thus, they are unable to move but still connect and affect other individuals. The fault-free individuals may be influenced by those individuals with partial failure, which may prevent the swarm from moving [10]. Assume all individuals in swarm are well-working at the beginning. The failure process of this behavior is as follows. 

(1) Before time $t_k$ , individual $i$ behaves normally and updates its state include position and velocity direction according to motion model in Section 2. 

(2) At time $t_k$ , individual $i$ encounters partial failure and can only change its velocity direction, but can't change its position for all $t \geq t_k$ , i.e., $c_i(t) = c_i(t_k)$ for all $t \geq t_k$ , other individuals still behave normally according to the motion model in Section 2. 

(3) The surrounding individuals within the interaction range are affected. This effect is propagated in the swarm, thereby influencing the behavior of the whole swarm. 

# 3.1.2. Resilience process under immobility of some individuals

Fig. 1 depicts the resilience process of the swarm through snapshots where some individuals in the swarm are immobile. Among these individuals, blue individuals represent leaders, red individuals represent followers, and black individuals represent individuals with partial failures. Green lines indicate attractive interactions between individuals, and pillow lines represent repulsive interactions between individuals. Fig. 1. (a) shows the self-adjustment process of the unmanned swarm from the initial state to the stable state. Fig. 1. (b) shows the stable state of the swarm, where the swarm exhibits a movement trend which is almost similar to the leaders' movement direction. Fig. 1. (c) shows the status of the swarm after some individuals are immobile under partial failure. These immobile individuals interact with normal individuals and affect normal individuals. For these individuals that are still normal, on the one hand, they are attracted by failure individuals, on the other hand, they are also attracted by other normal individuals including normal leaders. And the direction where normal individuals are attracted by failure individuals may be opposite to the direction of swarm, thus, the velocity of normal individuals will be reduced. Fig. 1. (c-e) show the process of the swarm being affected by the failure individuals. It can be seen that during the early stage of the failure, a large number of individuals are influenced, as the swarm progresses, the number of affected individuals gradually decreases, exhibiting a self 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a003b89daef5e0f1add7e55d51970f4aa9206bfbd897c38ec0c1154e23065f67.jpg)



(a) Individuals are trapped of $p = 30\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/37a0941a4fd921c81119ea53e82b927e7e3b88b7dde9291a6ac25c886d903cda.jpg)



(b) Individuals are trapped of $p = 50\%$



Fig. 15. Individuals being trapped by partial failure individuals with $30\%$ and $50\%$ failure of the swarm.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/7ab110623686e780655af5093478d2a5efa6565866e09d1fa094cd2ca6f11520.jpg)



(a)The velocity evolution process of $p = 10\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a0e64c64882eb0438cadb7e7287b09f99a9c140291d81606c9036450c40fe8ef.jpg)



(b) The velocity evolution process of $p = 20\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/6a35c0685d986e3e0eee93d49037f5aafc091498128d4b67be56f5ef81bc334d.jpg)



(c) The velocity evolution process of $p = 30\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/bc86cfc071a74fc495a2270295173ba625322284bfebba0675844864dd8dca6a.jpg)



(d) The velocity evolution process of $p = 50\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/d0b7f78da0861a5c343d36c38d762b27196c0b5ae82714599bbe54902a0d45f5.jpg)



(e) The velocity evolution process of $p = 60\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/9b76fed6450936863ea18b3479ce56df7b36a696a1d48b0d0baec6d7e339dc2e.jpg)



(f) The velocity evolution process of $p = 70\%$ with different swarm sizes 20,50,100,200



Fig. 16. The velocity evolution process with different swarm sizes and different failure proportions.


recovery capacity. Fig. 1. (e) is the state of the swarm after recovery. It can be seen that there are no green lines between normal individuals between failure individuals, i.e., normal individuals no longer interact with failure individuals, the swarm returns to a state of coordinated movement in leader's direction of movement. Fig. 2 show the evolution process of the $\nu_{\mathrm{group}}$ . The blue line represents raw data. The red line represents smoothed data by Savizky-Golay (S-G) filter [54]. It can be seen that the $\nu_{\mathrm{group}}$ experiences an obvious decline and recovery process. It also can be seen that the recovery process of swarm is not stable and demonstrates some volatility, the reason is that the swarm is a nonlinear 

system, and its performance fluctuates. 

# 3.2. Random motion

# 3.2.1. Motion model of random motion of the individual

When a single individual or a small group of individuals are disturbed by electromagnetic interference or radio-frequency interference which may lead to sensing system failure and control system failure, thereby resulting in an uncontrolled random motion. Individuals in the swarm move randomly, and they can't perceive other individuals 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/65f064b7869d886b0361fd33f015923bdb988d747069e05ad882a26d42640e99.jpg)



Fig. 17. Resilience with different swarm sizes and failure proportion.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3b23ef055e04e7b993396fa39f71b5c1fc52425839d5613dda717904bc4430f6.jpg)



Fig. 18. Resilience under degree failure strategy.


normally and can't behave correctly in response to information input, however, other individuals can still perceive these failure individuals normally under the circumstances. Assume all individuals are moving normally at the beginning. The failure process of this behavior are as follows. 

(1) Before $t_k$ , individual $i$ behaves normally and updates its state include position and velocity direction according to the motion model in section 2. 

(2) At time $t_k$ , individual $i$ encounters partial failure and moves randomly for all $t \geq t_k$ , i.e., $c_i(t) = c_i(t_k) + d(i)*\Delta t$ for all $t \geq t_k$ . $d(i)$ is a random generated direction, $d(i) = 2\pi * X, X \sim U(0,1), X$ follows a uniform distribution on the interval [0,1]. It should be noted that the new velocity direction still satisfies the turning rate constrains. Other fault-free individuals still update their velocity direction and position according to the motion model in section 2. 

(3) The failure individuals can't sense other individuals, but other individuals can still sense the failure individuals, the surrounding individuals within the interaction range are affected. This effect is propagated in the swarm, thereby influencing the behavior of the whole swarm. 

# 3.2.2. Resilience process under random motion of some individuals

Fig. 3 depicts the resilience process of the swarm through snapshots, illustrating the resilience process where certain individuals move randomly. Fig. 3. (a) shows the self-adjustment process of the unmanned swarm from the initial state to the stable state. Fig. 3. (b) shows the stable state of the swarm. Fig. 3. (c) and (e) shows the recovery process. Due to the interaction mechanism, the random movement of the failure individuals affect the normal individuals. Fig. 3. (f) shows the state of the swarm after recovery where the swarm restore a stable state. The change process of the $\nu_{\text{group}}$ in Fig. 3 is shown in Fig. 4. It can be seen that the $\nu_{\text{group}}$ of the unmanned swarm experiences a recovery process after being disturbed. 

# 3.3. Movement in the opposite direction of the swarm

# 3.3.1. Motion model of movement in the opposite direction of the individual

When some individuals in the swarm encounter hacker attacks and are hijacked, the movement of the individual may also move in the opposite direction of the swarm, thus affecting the movement of the unmanned swarm. Assume all individuals are moving normally at the beginning. The failure process of this behavior are as follows. 

(1) Before $t_k$ , individual $i$ behaves normally and updates its state include position and velocity direction according to the motion model in section 2. 

(2) At time $t_k$ , individual $i$ encounters partial failure and moves in the opposite direction of the swarm for all $t \geq t_k$ , i.e., $c_i(t) = c_i(t_k) - g * \Delta t$ , for all $t \geq t_k$ . $g$ is the preferred direction of informed individuals. Other fault-free individuals still update their velocity direction and position according to the motion model in section 2. 

(3) The surrounding individuals within the interaction range are affected. This effect is propagated in the swarm, thereby influencing the behavior of the whole swarm. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/b66fa1be49d6f247fe354870b4fcd7a641793150874726b716bbb98c524169c1.jpg)



(a)The state of normal movement


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/97fabb61d743c3b00e787c02f9a3d4f6c0378b43932eb1b15fe1f8f5200c3b3f.jpg)



(b) Failure by degree


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/ce2eebc9b5c85d5580bb999b99087b8b46570fb35a5d4cf38711db9dcd2adb92.jpg)



(c) The state after failure



Fig. 19. Swarm behavior under degree failure strategy with swarm size $N = 100$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3218454fef598b26870918811ea4a32f4197e1c4fb28eca0bad4f81e89afad3d.jpg)



(a) Front failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a2ce12c61904a5344873d8f97038433008d56f97fc072ed5aa0498f3ae30c2a6.jpg)



(b) End failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/be72e169671edb7e24b832113a81a1fec4f784ce0d7f96bedd68b869113a2c46.jpg)



(c) Right/Left failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/285a98e571399261310920809a8955b2b5d347ab5d713a76932ca839fc49f631.jpg)



(d) Center failure strategy



Fig. 20. Resilience under location failure strategy.


# 3.3.2. Resilience process with some individuals moving in the opposite direction of the swarm

Fig. 5 depicts the progression of the swarm through snapshots, illustrating the situation where some individuals experience being held hostage, etc., and they show movement in the opposite direction of the swarm. Fig. 5. (a) shows the self-adjustment process of the unmanned swarm from the initial state to the stable state. Fig. 5. (b) shows the stable state of the swarm. Fig. 5. (c) and 5. (e) show the recovery process after some individuals moving in the opposite direction of the swarm. Due to the interaction mechanism, failure individuals affect the normal individuals. Fig. 5. (f) is the state of the swarm after recovery, where the swarm restore a stable state. The evolution process of the $\nu_{\text{group}}$ of resilience process in Fig. 5 is shown in Fig. 6. It also can be seen that the unmanned swarm has undergone a recovery process after being disturbed. 

# 4. An improved resilience metric

In this section, we propose an improved resilience metric by considering the absolute time scale and minimum mission performance requirement on the basis of Tran's metric. Resilience process time is an important factor reflecting the swarm resilience, the shorter the recovery time is, and the better resilience of the system, and the absolute resilience process time is a key indicator reflection of system resilience. We build an absolute time sensitivity factor on the basis of the absolute resilience process time. In addition, in some scenarios, the performance of the swarm needs to be above a certain level to complete mission. For example, in fast target tracking and surveillance scenarios, high speed is important when UAV swarms need to track fast-moving targets or provide real-time surveillance. In this section, according to inadequacies of existing resilience metrics, we present an improved evaluation metric that takes into account the absolute time scale and minimum mission 

performance requirement. Then, we demonstrate the advantage of the improved resilience metric through four numerical examples. 

# 4.1. The improved resilience metric

Time is an important factor for a resilience metric, the system's recovery time after being disturbed is an embodiment of the system's self-organization and self-reconfiguration ability. Tran's metric is based on a relative time scale, however, many systems with well-defined mission characteristics are influenced by absolute time scale [52]. In addition, a system may also not need to operate at its full capacity to fulfill the mission for some missions [53]. By taking into account the above considerations, we propose an improved resilience metric that incorporates the absolute time and the minimum mission requirement on the basis of Tran's metric. 

We add a new parameter $y_{m}$ shown in Fig. 7, which represents the minimum mission performance requirement. The Eq. of improved metric is as follows. 

$$
R _ {\text {i m p r o v e d}} = \left\{ \begin{array}{c} \rho^ {\tau} \sigma [ \delta + \zeta ] \mu \text {i f} \rho - \delta \geq 0 \\ 0 \text {i f} \rho - \delta <   0 \end{array} \right. \tag {5}
$$

Where $\tau$ is used to adjust the preference of decision making and/or administrator. When $\tau = 0$ , the improved metric focused on evaluating from the perspective of mission requirements. When $\tau = 1$ , the improved metric focused on evaluating from the system itself. $\rho$ is the recovery factor, $\zeta$ is the volatility factor, which are same as $\rho$ and $\zeta$ in Tran's method 

The total performance factor considering the minimum mission performance requirements is $= \frac{\int_{t_0}^{t_{final}} y(t) [y(t) - y_m] dt}{\int_t^{t_{final}} y_d dt}$ . If the performance $y(t)$ is greater than $y_m$ , $y(t)$ is effective, otherwise $y(t)$ is useless. $[P]$ is the Iverson bracket. When $P$ is true, $[P] = 1$ , otherwise $[P] = 0$ . The 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/195ea64e6569fb61a35a9d3d46b8aacb2a506d5d57c2f79ccb87d77ad7c461d5.jpg)



(a) The velocity evolution process of $p = 10\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a590c9fa6d7d34b2c139393b8cf30ddaeb973b712f56f2328a545511e43ae7b6.jpg)



(b) The velocity evolution process of $p = 20\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/4b6040b54e9178439ab1acbb8f12a48c95dc4ad32692a5601f90c7acd7be7d13.jpg)



(c) The velocity evolution process of $p = 30\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/9c4f87f7480d6dba7bfbe54ac651021ed2e8c791c45ab7095501b1eaae8ebd72.jpg)



(d) The velocity evolution process of $p = 50\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/1e9928ffb83aea61167256a8552f714efe703cd44d211d3fd858e05e97d2307a.jpg)



(e) The velocity evolution process of $p = 60\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/5195c74aae82fbdaa80a505204ca24c29993fb5d0ad9c990e203ee5ba5139ef7.jpg)



(f) The velocity evolution process of $p = 70\%$



Fig. 21. The velocity evolution process of the swarm under different failure proportions.


improved $\sigma$ describe the ratio of the total effective cumulative performance to the total expected performance. $\delta$ is the absorption factor, and $\delta = \frac{y_{\min}[y_{\min} - y_m]}{y_D}$ . This factor also considers that if $y_{\min}$ meet the minimum mission requirement. If the $y_{\min} > y_m$ , $\delta = \frac{y_{\min}}{y_D}$ , otherwise $\delta = \frac{y_{\min} + 0}{y_D} = 0$ . This factor describes that how well a system is able to absorb a disruption. The bigger the $\delta$ is, the system ability drops less, the bigger the resilience is. 

$\mu$ is the absolute time sensitivity factor, and $\mu = \Delta^{\frac{[SS - D]}{B}}$ . Time importance factor $\Delta$ is used to measure the importance of time, 0 

$< \Delta \leq 1$ , the greater $\Delta$ is, the more critical the time is. When $\Delta = 1$ , time importance factor doesn't influence the system resilience, because $\mu$ is always 1 under such circumstances. $\Delta$ and $\mu$ are directly proportional. Reference time $B$ provides an absolute time reference for the system. For different systems and different scenarios, the absolute reference time $B$ can be different, for example, $B$ for infrastructure systems, may be measured in certain hours or days, $B$ for ecosystems may be measured in certain months or years, and the value of $B$ for unmanned swarm may be measured in some minutes or hours [52]. $t_{SS} - t_{D}$ is the total time it takes for the system to return to a steady state from the disturbance, the 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/9049de43ce1288d48149b41dbb79ba92728b5f7422e5e3ac90bbbf930056f2f5.jpg)



Fig. 22. Resilience with different failure proportions.


smaller the $t_{SS} - t_D$ is, the more resilient the system is. $t_{SS} - t_D$ is inversely proportional to $\mu$ . 

# 4.2. Comparative analysis

In this section, we validate the proposed resilience metric by comparing with existing metrics under 4 typical resilience process. 

# 4.2.1. Performance curves at different time scales

This case consists of 12 performance curves for an unmanned autonomous swarm with different total mission time which represents the average velocity of the swarm in a certain direction in Fig. 8, case 1 - case 6 and case 7 - case 12 have the same trend and total mission time respectively, however, the total time in case 1 - case 6 is half of case 7 - case 12. This case focuses on evaluating the resilience of the system itself [52]. 

The performance data of the system during the disturbance phase is generated by Eq. (6) [51]. 

$$
y = A _ {1} + \frac {K _ {1} - A _ {1}}{1 + \exp [ B _ {1} (t - x _ {1}) ]} \tag {6}
$$

$K_{1}, A_{1}, B_{1}$ and $x_{1}$ represent the desired performance, minimum performance, slope of deformation, deformation position parameters respectively during the disturbance phase. 

The performance data of the system during the recovery phase is generated by Eq. (7) [51]. 

$$
y = A _ {2} + \frac {K _ {2} - A _ {2}}{1 + \exp [ - B _ {2} (t - x _ {2}) ]} \tag {7}
$$

$K_{2}, A_{2}, B_{2}$ and $x_{2}$ represent the recovered performance, minimum performance, slope of deformation, deformation position parameters respectively during the recovery phase. 

The parameters for case1 - case6 are set as $t = 100$ , $K_{1} = 50$ , $A_{1} = 20$ , $B_{1} = 0.5$ , $x_{1} = 25$ , $A_{2} = 20$ , $B_{1} = -0.5$ , $x_{2} = 70$ . $K_{2}$ is set as [25, 30, 35, 40, 45, 50] respectively. The parameters for case 7 - case 12 are set as $t = 200$ , $K_{1} = 50$ , $A_{1} = 20$ , $B_{1} = 0.5$ , $x_{1} = 50$ , $A_{2} = 20$ , $B_{1} = -0.5$ , $x_{2} = 70$ , $K_{2}$ is set as [25, 30, 35, 40, 45, 50] respectively. It can be seen that the time of case 1 - case 6 is half of case 7 - case 12, and other parameters are all the same. It can be naturally seen that the resilience of case 1 - case 6 is higher than case 7 - case 12 under the same recovery level. 

# (1) Resilience calculation of Tran's method

From Table 1, we can see that the difference in resilience under same 

recovery level is not much, even resilience is greater with large time scale, which is clearly not in line with common sense. Tran's metric can't distinguish resilience in different time scales. 

# (2) Resilience calculation of Liu's method

Liu's resilience metric consists of two parts, time resilience and performance resilience. Performance resilience can describe resilience than time resilience because it has taken time into account. And we use performance resilience to describe resilience. The results are shown as Table 2. 

Compare case 1 with case 7, case 2 with case 8, ..., case 6 with case 12, it can be seen that Liu's method can't distinguish resilience at different time scales. 

# (3) Resilience of Cheng's method

Cheng's metric contains two parts, survivability and recoverability, and we set the survivability coefficient as 0.5 and recoverability coefficient as 0.5 in this case. It can be seen that the resilience of case 1 - case 6 is greater than that of case 7 - case 12 at the same recovery level respectively from Table 3, which indicates that Cheng's metric can distinguish resilience under different time scales. 

# (4) Resilience calculation of the improved method

Our main concern is evaluating the system's own resilience, thus we set $y_{m} = 0$ , $B = 20$ , $\Delta = 0.8$ and $B = 30$ , $\Delta = 0.6$ respectively to illustrate the credibility of the proposed metric. 

From the Tables 4 and 5, It can be seen that the resilience increases as the recovery level increases with the same time scale. It also can be seen that the resilience decreases as $t_{SS} - t_D$ increases with the same time level. In addition, it can be seen that the reference time $B$ and the time importance factor $\Delta$ don't influence the relative value with the same resilience process. 

# 4.2.2. Mission-Oriented resilience evaluation

A curve of an unmanned swarm performing reconnaissance missions is shown in Fig. 9, and the lowest capability requirement is $70\%$ of its normal reconnaissance capability. Assume that the swarm is disrupted at the $5^{\text{th}}$ hour, and the reconnaissance ability drops to $20\%$ . System A restores to $75\%$ of desired reconnaissance capability within 5 hours, and system B speed 8 hours to bring the system back $100\%$ . However, during the 20-hour mission, system B meets the minimum performance requirement for 15 hours, while System A only meets it for 12 hours. In general, the resilience of strategy 1 is better. This case focuses on evaluating the resilience of the mission requirements. 

And the parameters for the first column of $R_{improved}$ are that $\Delta = 0.8$ , $B = 5$ , the parameters for the second column of $R_{improved}$ are $\Delta = 0.6$ , $B = 7$ . It can be seen that Tran's metric can't correctly evaluate resilience when considering the mission requirement from Table 6. 

# 4.2.3. Resilience evaluation considering minimum performance

The parameter settings of this case in Fig. 10 are that the total time is $t_{final} = 100$ , desired performance $y_{D} = 50$ , minimum performance requirement $y_{m} = 10$ . For system A, system is disturbed at $t = 30$ , and the system performance drops to the lowest point at $t = 50$ , $y_{min} = 20$ . When $t = 80$ , system restores a stable state, $y_{D} = 30$ . For system B, system is also disturbed at $t = 30$ , system performance keeps dropping down until $y = \frac{160}{9}$ at $t = 80$ . And during the mission period, the total residual performance proportion of system A and system B to the total desired performance are the same. However, after the disturbance, the performance of system B has been degraded to a plateau and there is no recovery process, thus the resilience of system A is better. 

The parameters for the first column of $R_{improved}$ are that $\Delta = 0.8$ , $B =$ 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/a049a93c2163005a15932a7bd25484599e7a43fd3c19ab0c53b56c4bbdd312e0.jpg)



(a) The velocity evolution process of $p = 10\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3cc085de152fe5aea7c1ab55fd16e5d8ac908fa0e59bd6d8ff962146b6b7c2f6.jpg)



(b) The velocity evolution process of $p = 20\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/856f5f7291b7406d3d1587504a0b60e0f06decedd44f372670c4aa502c8e2aec.jpg)



(c) The velocity evolution process of $p = 30\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/9a4f16acc1b8beaad842b7df82222b31af21436e55751f767d6a030c7ea1835b.jpg)



(d) The velocity evolution process of $p = 50\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/d63d60aa0f445ca4718e0544834bbed649ae70c43160e87e564f9c433032918c.jpg)



(e)The velocity evolution process of $p = 60\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/2cf49ffc589a0a0f1279a29a5aa54db9313bdf47a148bc8976da929add7ca50c.jpg)



(f) The velocity evolution process of $p = 70\%$ with different swarm sizes 20,50,100,200



Fig. 23. The velocity evolution process with different swarm sizes and different failure proportions.


40, the second column of $R_{improved}$ are $\Delta = 0.5$ , $B = 60$ . It can be seen that Liu's metric can't distinguish from different recovery levels when the system's performance is the same from Table 7. 

# 4.2.4. Resilience evaluation with performance curves for different concavoconvexities

Consider 3 cases shown in Fig. 11 [52], the initial performance level of three cases $y_{o}$ , the performance level after recovery of three cases $y_{R}$ , the time of disturbance occurrence $t_{D}$ of three cases, the time of recovery occurrence $t_{R}$ and the time of reaching the steady-state level $t_{SS}$ of three cases are all the same. The difference lies in the dynamic process during the disruption and recovery phases. 

It can be seen that the resilience of $R_{\text{Tran}}$ , $R_{\text{Liu}}$ and $R_{\text{improved}}$ are all the same, however, $R_{\text{case1}} < R_{\text{case2}} < R_{\text{case3}}$ of $R_{\text{Cheng}}$ from Table. 8, parameters of three cases are the same, the comprehensive resilience effects of three cases are the same, thus resilience should be the same in all three cases. However, the result of the resilience calculation is case 1 < case 2 < case 3 of $R_{\text{Cheng}}$ , which is unreasonable. 

In general, the improved resilience evaluation method takes into account the absolute time scale and the minimum performance requirement, and can evaluate system from mission and system itself. Compared with Tran's method, Liu's method and Cheng's metric, the improved metric makes up for shortcomings that Tran's method can't distinguish the resilience under different time scales, Liu's method can't 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f5973f546c4c2e22867e636b5c23d00339d491296917e8edaa444368bf77b835.jpg)



Fig. 24. Resilience with different failure proportions and swarm sizes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/acb475ccc2324f91278d578ee139ffae34d72ef8cf8f77c53523830e0f532f0a.jpg)



Fig. 25. Resilience value under degree failure strategy.


distinguish the resilience when the performance all meets the minimum performance requirement, and Cheng's metric calculate resilience incorrectly when the combined effects of the resilience process are the same. 

# 5. Simulation and discussions

In this section, we propose a location failure strategy and construct three failure strategies on the basis of the random failure strategy and the degree failure strategy. And we study the swarm resilience law under different motion models with partial failures, different swarm sizes and failure strategies. 

# 5.1. Failure strategy

To simulate the failure power and strategy of the failed individuals in the swarm, we give three failure strategies, namely one random failure strategy and two deliberate failure strategies, i.e., degree failure strategy and location failure strategies. Let $P$ denote the percentage of the failed individuals, the number of failed individuals is denoted as $N * P$ . 

# 5.1.1. Random failure strategy

Under random failure strategy, the initially failed individuals are 

randomly chosen with the proportion $P$ , ignoring the network topology and any other properties. Random failure can mimic the failures due to platform defects, external environments factors, third party attacks without knowing any information, etc. 

# 5.1.2. Temporal degree failure strategy

The temporal degree failure is a type of malicious failure strategy. The degree reflects the influence of an individual. We order the individuals according to their temporal degree from large to small and then select the top $N * P$ individuals as failure individuals. The individual's degree is the number of its neighbors who can perceive this individual, which is a temporal variable and varies as dynamical swarm network evolves. 

# 5.1.3. Failure by location of the swarm

An unmanned swarm always moves in a certain formation, and an individual's influence in different spatial position is different. There are few studies that concentrate on the impacts of failure in different locations on swarm from the perspective of resilience. We divide the spatial position of the group into five areas: front, end, center, left, right, where the front is the area where the swarm faces movement direction, and so on to study resilience. Fig. 12 shows the regional division of the swarm. 

We set a virtual target point $Of(x_{Of}, y_{Of})$ in the velocity direction of the whole swarm to help divide the space area, $Of$ is in the extend line of the swarm velocity direction. $Oc(x_{Oc}, y_{Oc})$ is the geometric center of the swarm, and $x_{Oc} = \frac{1}{N} \sum_{i=1}^{N} x_i, y_{Oc} = \frac{1}{N} \sum_{i=1}^{N} y_i$ . The slope of the line $OcOf$ is the velocity direction of the whole swarm, i.e., $\nu_{\text{group}}(t)$ . 

# (1) The front failure strategy

Calculate the distance $d_{if}$ between individual $i$ and virtual target point $\nu_{Of}$ . And individuals at the front of the swarm have more influence [55]. 

$$
d _ {i f} = \sqrt {\left(x _ {i} - x _ {O f}\right) ^ {2} + \left(y _ {i} - x _ {O f}\right) ^ {2}} \tag {8}
$$

Sort individuals according to $d_{if}$ from large to small, then choose $N * p$ individuals with smallest distance and set them as failures. 

# (1) The end failure strategy

Sort individuals according to $d_{if}$ from large to small, then choose $N * p$ individuals with largest distance and set them as failures. 

# (2) The left failure strategy

First, determine the if the individual is on the left side of the swarm, if yes, calculate the distance between individual and line $OcOf$ , choose $N * p$ individuals with the largest distance, and set them as failure individuals. 

The Eq. of line $OcOf$ is: 

$$
v _ {\text {g r o u p}} (t) x + y _ {O c} - v _ {\text {g r o u p}} (t) x _ {O c} - y = 0 \tag {9}
$$

If $\nu_{\text{group}}(t)x + y_o - \nu_{\text{group}}(t)x_o - y < 0$ , then the individual $i$ is located in the left swarm. 

The distance between individual $i$ and line $OcOf$ is: 

$$
d _ {i o o f} = \frac {\left| v _ {g r o u p} (t) x + y _ {O c} - a x _ {O c} - y \right|}{\sqrt {v _ {g r o u p} (t) ^ {2} + 1}} \tag {10}
$$

Then sort individuals which are located in the left swarm according to $d_{ioof}$ , and choose $N * p$ individuals with the largest distance and set them as failures. 

# (3) The right failure strategy

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/1cdcb4e1bebc95c8fa18955097af23e62b06074e19cb97d855b37738e0a75524.jpg)



(a) Front attack strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/f97293e7a51c62aa1d10ddc4c88bb62be36883e03f7e7c14f57b6139b3081466.jpg)



(b) End attack strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/744f730c1a2eb86745108f01742ddb137d55a9b35a10747c4dacb156905c73c2.jpg)



(c) Right/Left attack strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/054ed9a690fc046c37f2a2b6310a6ede3ce5a100bdb8ab386f5af1ba009557e4.jpg)



(d) Center attack strategy



Fig. 26. Resilience value with location failure strategy.


If $\nu_{\text{group}}(t)x + y_{\text{Oc}} - \nu_{\text{group}}(t)x_{\text{Oc}} - y > 0$ , the individual $i$ is located in the right swarm. Calculate the distance $d_{\text{ioof}}$ between individual $i$ and line $OcOf$ . Then sort individuals which are located in the right swarm according to distance from large to small, and choose $N * p$ individuals with the largest distance and set them as failures. 

# (4) The center failure strategy

Calculate the distance $d_{i0}$ between individual $i$ and swarm center $Oc(x_{Oc},y_{Oc})$ . 

$$
d _ {i 0} = \sqrt {\left(x _ {i} - x _ {O c}\right) ^ {2} + \left(y _ {i} - y _ {O c}\right) ^ {2}} \tag {11}
$$

Sort individuals according to the distance, then choose $N * p$ individuals with the largest distance set them as failure individuals. 

# 5.2. Parameter setting

Consider a swarm with $N$ individuals moving about in a two-dimensional plane at random directions. They start in a random initial direction, where each individual can detect at least one other. Individuals are subject to random influences, e.g., sensory/movement error, the movement is affected by a random circular wrapped Gaussian distribution centered on 0, with a standard deviation of 0.01 for all individuals. Simulation parameters are shown in Table 9. Because the position of all individuals is randomly generated and all leaders are randomly selected, the position of the failed individuals is also random, to reduce the effect of randomness, we use the average value of 100 simulations as the resilience in each scenario. We use Anylogic for our 

swarm simulation, which is a multimethod simulation modeling tool and supports agent-based, discrete event and system dynamics simulation method and is suitable for swarm simulation [56]. 

# 5.3. Resilience evaluation of individuals immobile failure

# 5.3.1. The resilience evaluation with different partial failed percentage

Fig. 13 shows the performance evolution process of the swarm under different failure proportions. We use smoothed data to analyze the swarm. It can be seen that when some individuals suffer failure, the velocity decreases rapidly to a minimum value. Then the average velocity of the swarm is slowly recovering, and finally reaches a stable state. It also can be seen that the recovery process of swarm is not stable and demonstrates some volatility. From Fig. 13 we can find that as the proportion of unmanned swarm failures increases, the average velocity of the swarm after recovery decreases, and the time that takes to return to a stable state increases. 

It can be seen that resilience $R$ decreases as the percentage of failed individuals increases, and the trend in resilience is consistent with common sense from Fig. 14. We also find that some normal individuals will keep shaking near the failure individuals in some scenarios, which can't escape from the failure individuals. We take the simulation snapshots of the swarm in Fig. 15 to illustrate this phenomenon. We can see that when the subgroup of the swarm containing leaders has left, there are still a proportion of individuals near the failure individuals, and we also can see that swarm with a high proportion of failures has more individuals anchored by failure individuals. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/1df791f4622ed71e2859357f5f328191495655333a44796198f9c7998a04c691.jpg)



(a) The velocity evolution process of $p = 10\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/413a9ff9be25fff93925938d985c4380e7f3c3e699e8b83fed47c30dfec7ab97.jpg)



(b) The velocity evolution process of $p = 20\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/7131dca6b75dce0212bec5360e73bffcc8ef0d99f0a45100d0adb92012c0cc4a.jpg)



(c) The velocity evolution process of $p = 30\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3a88b8691c07cf7664cf860a40e551f7b0961f3d77e83658d102f5412bf65fc7.jpg)



(d) The velocity evolution process of $p = 50\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/4caee90f6c030b628d0b0456dc46eb3cf05765b7f431c51e2fa99cd920924c12.jpg)



(e) The velocity evolution process of $p = 60\%$


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/78e9ce80e466567cfa0510fef2c891005b376e2f41cd985c0cc5cba0b01ecd76.jpg)



(f) The velocity evolution process of $p = 70\%$



Fig. 27. The velocity evolution process of the swarm under different failure proportions.


# 5.3.2. The resilience evaluation with different swarm sizes

In this section, we study resilience with different swarm sizes, i.e., $N = 10,50,100,200$ . Fig. 16 shows a typical velocity evolution process of swarm with the different failure proportion and swarm sizes. It can be seen that the swarm size can affect the recovery time, the lowest performance level and the performance level after recovery. When $p \leq 30\%$ , swarms with 20, 50, 100, 200 individuals all experienced an obvious recovery process, the recovery time increases as the swarm size increases, and the performance after recovery decreases as the swarm size increases. 

We explore the how the resilience of unmanned swarms varies with different swarm sizes and with different proportions of failures. Fig. 17 show the resilience $R$ calculated by Eq. (5), it can be seen that resilience decreases as the swarm size increases. 

# 5.3.3. The resilience evaluation with different failure strategy

Degree failure strategy. Fig. 18 show the resilience under degree failure strategy, it can be seen that when swarm size $N < 100$ , the resilience decreases as the failure proportion increases, which shows a clear downward trend, however when the swarm size is large, resilience is at a very low level. The reason is that when the swarm size is small, more individuals can be accommodated within the perception range of the individual. And the location difference of the faulty individuals under random and degree failure strategy is small. However, when the swarm size is large, the shape of the swarm presents an elongated bounding box during motion. Individuals with high degree usually occupies the middle of the swarm, when these individuals fail, the swarm has a high probability to split, many individuals may be anchored by failed individuals, resulting in a low performance level of recovery. Fig. 19 shows a typical 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/4a64cc9de16b4de65b30790a243870c95b333f534ccfc27319c029f28bae74cd.jpg)



Fig. 28. Resilience of the swarm under different failure proportions.


process of this situation. 

Location failure strategy. Fig. 20 shows the resilience R calculated by Eq. (5) based on the simulation data with location failure strategy, and the failure proportion on abscissa of coordinate in Fig. 20 is not for the entire swarm, but only refers to the swarm that meets the location requirement. It can be seen that resilience with front failure strategy and center failure strategy have low resilience and a faster decline rate. It can be seen from Fig. 20(a) that when $N = 20$ , the resilience under front failure strategy declines rapidly as the failure proportion increases, when $N = 100$ , $200$ , $P \geq 0.2$ , swarm resilience is at a very low level. The reason is that many leaders occupy the front of the swarm, and more leaders fail as the failure proportion increases, more leaders fail, resulting in low resilience. From Fig. 20(d) we can see that when the swarm size $N = 100$ , 200 and $P \geq 0.2$ , swarm resilience is at a very low level. It shows when the swarm size is large, the failure of a small number of individuals can influence the swarm greatly under the center failure strategy. From the Fig. 20(b) and the Fig. 20(c), it can be seen that the swarm resilience shows a linear decreasing trend under end failure strategy and right/left failure strategy. 

# 5.4. Resilience evaluation of individuals moving randomly under partial failure

# 5.4.1. The resilience evaluation with different percentage failed individuals

Fig. 21 shows a typical process of performance evolution curve when some individuals moving randomly under partial failure. It can be seen that as the failure proportion increases, the longer the recovery time takes, the lower the recovery level is. It can be seen that the resilience of the swarm becomes smaller as the failure proportion increases from Fig. 22. 

# 5.4.2. The resilience evaluation with different swarm sizes

Fig. 23 shows a process example of performance evolution curve with different swarm sizes when some individuals move randomly under partial failure. It can be seen that the swarm resilience decreases as the swarm size grows from Fig. 24. 

# 5.4.3. The resilience evaluation with different failure strategies

Degree failure strategy. From Fig. 25, it can be seen that when the swarm size is 20 or 50, the swarm resilience still follows the pattern of decreasing with an increase in the failure proportion. However, when the swarm size is 100, 200, a small failure proportion of swarm can lead to low resilience of the swarm, and the swarm resilience remains at a low 

level under different failure proportions. 

Location failure strategy. Fig. 26 shows the resilience under different location failure strategies when some individuals moving randomly in the swarm, the swarm resilience decreases rapidly under the front and center failure strategies, and the swarm resilience decreases gently under right/left and end failure strategy. From Fig. 26(a), it can be seen that when the swarm size is 100 and 200 and failure proportion is larger than 0.2, the resilience is at a low level. The reason is that shape of swarm with leaders presents an elongated bounding box during motion, leaders usually occupy the front of the swarm. The failure in the front of an unmanned swarm means many leaders fail. In this case, it is difficult for leaders to navigate the swarm. From Fig. 26(d), it can be seen that when swarm size is 100 and 200, the resilience is at a low level under center failure strategy, the reason is similar to the swarm suffering immobile failure. 

# 5.5. Resilience evaluation of individuals moving in the opposite direction of the swarm under partial failure

# 5.5.1. The resilience evaluation with different percentage failed individuals

Fig. 27 shows a typical process of performance evolution curve when some individuals move in the opposite direction of the informed direction under different failure proportions. It is evident that the recovery level of the swarm decreases with the increase of the failure proportion. However, the time taken from perturbation to steady state level does not change significantly. And the worst-case scenario is that the overall swarm velocity is less than 0, the swarm exhibits movement in a direction opposite to the desired direction of the swarm. Fig. 28 shows the R calculated by Eq. (5) based on the simulation data, showing that the resilience of the swarm also becomes smaller as the failure proportion increases. 

# 5.5.2. The resilience evaluation with different swarm sizes

Fig. 29 shows a process example of performance evolution curves with different swarm sizes when some individuals move in the opposite direction of the informed direction. Fig. 30 shows the resilience calculated by Eq. (5). It can be seen that from the swarm resilience decreases as the swarm size grows. 

# 5.5.3. The resilience evaluation with different failure strategy

Degree failure strategy. Fig. 31 show the resilience calculated by Eq. (5), it can be seen that the swarm resilience decreases as the swarm size grows. And when the swarm size is 100,200, a low failure proportion of individuals can make the swarm resilience at a lower level. The reason is that when the swarm size is large, the shape of the swarm presents an elongated bounding box during motion, individuals with high degrees occupy the middle position of the swarm, the movement of individuals in the opposite direction of the swarm which are in the center of the swarm will greatly affect the recovery of individuals in the rear of the swarm. 

Location failure strategy. Fig. 32 illustrates the resilience under different location failure strategies, it can be seen that under the front failure strategy, the resilience of unmanned swarms decreases rapidly from Fig. 32(a). The reason behind this phenomenon is that leaders always occupy the front of the swarm, and when the individuals in the swarm move in the opposite direction, the overall movement of the swarm is greatly affected. Simultaneously, it can be seen that the swarm resilience declines slowly as the failure proportion increases under end failure strategy, and the swarm resilience is the greatest at a specific failure proportion, the reason is that these failed individuals quickly leave the swarm, causing the swarm to split, the swarm is affected for a short time, and a high resilience is achieved comprehensively. When the swarm size 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/31d68438c91ed677a9b01bc3fce5b0065a7c5f5008f25534ecd651786540a35d.jpg)



(a) The velocity evolution process of $p = 10\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/8e962fb420021140eb4f559223958f1b855a38550af9c0221e70edac73584842.jpg)



(b) The velocity evolution process of $p = 20\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/ebbee9b772eccd58e92e9524560204d98a5a01e0e6bf19d558d8eca7e09d5741.jpg)



(c) The velocity evolution process of $p = 30\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/6000e80c69cf49b6d2253878afdc52400e4282945c97a095c5720206f77f5d20.jpg)



(d) The velocity evolution process of $p = 50\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/6972de332ed92e9d89965f76a9472dd9cf94518840d12695cab020fcc9167623.jpg)



(e) The velocity evolution process of $p = 60\%$ with different swarm sizes 20,50,100,200


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/521d222a3e264c80effaddf3d7f61d44867cacfcd15b20937047f8d7d0991d9d.jpg)



(f) The velocity evolution process of $p = 70\%$ with different swarm sizes 20,50,100,200



Fig. 29. The velocity evolution process with different swarm sizes and different failure proportions.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/3ce40726a0b886307f2997996c2c9447a54cb7e5cdd44d086866996fb6ee05a5.jpg)



Fig. 30. Resilience with different failure proportions and swarm sizes.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/d92e945d3815ce96337aa8aaa04aa9e36e10f79021d5848978d51028a28872cc.jpg)



Fig. 31. Resilience under degree failure strategy.


is large, the failure of a small number of individuals can make the swarm resilience at a low level under the center failure strategy. The reason is similar to degree failure strategy. 

# 6. Conclusion

Resilience is an important characteristic of unmanned swarms and is attracting more and more attention. We investigate the swarm's self-organization and self-recovery ability of swarm considering partial failure of individuals in swarm in this paper. First, we use the classic model Couzin-Leader model to establish the unmanned swarm model, and we adopt the average velocity in the desired direction as the swarm performance. Then we analyze the behavior rules of the individual under partial failure, and three motion models and resilience processes are developed. After that, considering absolute time scale and minimum performance requirement of the mission, we propose an improved resilience metric for swarm resilience evaluation, and we demonstrate the superiority of the proposed metric through 4 comparative experiments. On the basis of the random failure strategy and the degree failure strategy, we also propose a location failure strategy and construct three failure strategy in total. Finally, we analyze the collective behavior and resilience process of unmanned swarms under different failure proportions, different swarm sizes, and different failure strategies through simulation. 

According to the above simulation and discussions, we can obtain some general findings as follows. (1) The resilience of the swarm decreases as the failure proportion increases. There exists an anchoring phenomenon, where some normal individuals are trapped by faulty individuals. This is mainly caused by the interaction mechanism, where some normal individuals are mainly affected by the faulty individuals. (2) The resilience of swarm decreases as the size of the swarm increases. It is difficult for individuals to influence other individuals in the interaction range when the scale of the swarm is large. In addition, the shape of the swarm shows a rectangular shape when swarm size is large, and influence of leaders becomes smaller as leaders are usually in the front of the swarm. (3) Among different failure strategies, degree based strategy, center based strategy and the front based strategy have more impact on the resilience of the swarm. The central based strategy and degree based strategy will hinder the interaction between the front and rear parts of the swarm, resulting in the fragmentation of the swarm easily. Because leaders are always in the front of the swarm, the failure in front of the swarm will greatly influence the performance and resilience of the swarm. (4) Compared to individual with immobile failure, swarm with individuals moving random and moving in the opposite direction under partial failure has lower resilience. 

This study provides a new way of analyzing unmanned swarms, including the resistance, adaptation, and recovery capabilities of unmanned swarms under partial failures of some individuals. It can help discover flaws in the design of unmanned swarm interaction mechanisms. For practical unmanned swarm, we can perform simulation experiments or real experiments and conduct the resilience analysis. The capability of unmanned swarm to complete tasks under disturbance conditions can be evaluated which is used for optimal design and mission planning. In modern combat environment, the unmanned autonomous swarms are not only required to keep stable operations, but also withstand uncertain threats and recover from disruptive events. Resilience is an extension of reliability, which enhances the ability of aforementioned systems to resist disruptions and bounce back from damages. It provides powerful decision-making assistance and support for unmanned systems and other combat support systems in future joint operations. 

Recently, Xu proposed an improved swarm model with informed individuals to prevent swarm-splitting with a dual-adaptive feedback mechanism [57]. We also plan to study and further improve the model to reduce the sensibility to the swarm size, degree failure strategy and location failure strategy. In addition, minimal paths set can describe the communication redundancy in the swarm [58]. We plan to apply the minimal path sets as performance indicator of the swarm for resilience analysis. 

# Author statement

Xinxin Zhou conceived and designed the methodology and model; Yun Huang coded the algorithms; Guanghan Bai and Junyong Tao proposed the idea of this paper; Bei Xu designed the experiments and analyzed the data. All authors have contributed to the editing and proofreading of this paper. 

# CRediT authorship contribution statement

Xinxin Zhou: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing - original draft, Writing - review & editing. Yun Huang: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing - original draft, Writing - review & editing. Guanghan Bai: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/24a489a4707be1af49f55a91c680181b46f11829ccc08209bb16fdd9626be229.jpg)



(a) Front failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/5f92b8c16001d22cdbdb82962035eb552083b05a947cd3c2d035434f41e64256.jpg)



(b) End failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/66f24641eae175595b8d09feb22f8a3d1623113fa8c92ddd97a52489ac27b885.jpg)



(c) Right/Left failure strategy


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/96560354-cf9a-4b63-8395-d33ce6118bcb/fb877da678efab272facbc331c58ce081fde1d5cc1ce9f6cbb465d9c9c690208.jpg)



(d) Center failure strategy



Fig. 32. Resilience under location failure strategy.


Validation, Visualization, Writing - original draft, Writing - review & editing. Bei Xu: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing - original draft, Writing - review & editing. Junyong Tao: Conceptualization, Data curation, Formal analysis, Funding acquisition, Investigation, Methodology, Project administration, Resources, Software, Supervision, Validation, Visualization, Writing - original draft, Writing - review & editing. 

# Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper. 

# Data availability

Data will be made available on request. 

# Acknowledgment

This work was supported in part by the Natural Science Foundation of China under Grant 72271242 and in part by the Hunan Provincial Natural Science Foundation of China for Excellent Young Scholars under Grant 2022JJ20046. 

# References



[1] Reynolds CW. Flocks, herds, and schools: a distributed behavioral model. Seminal graphics. New York, NY, USA: ACM; 1998. p. 273-82. https://doi.org/10.1145/280811.281008. 





[2] Couzin ID, Krause J, James R, Ruxton GD, Franks NR. Collective memory and spatial sorting in animal groups. J Theor Biol 2002;218:1-11. https://doi.org/10.1006/jtbi.2002.3065. 





[3] Couzin ID, Krause J, Franks NR, Levin SA. Effective leadership and decision-making in animal groups on the move. Nature 2005;433:513-6. https://doi.org/10.1038/nature03236. 





[4] Olfati-Saber R. Flocking for multi-agent dynamic systems: Algorithms and theory. IEEE Trans Autom Control 2006;51:401-20. 





[5] Liao F, Wang J, Teo R, Hu Y, Lai S, Cui J, et al. Vision-based autonomous flocking of UAVs in unknown forest environment. In: Proceedings of the 12th IEEE International Conference on Control and Automation (ICCA). IEEE; 2016. p. 892-7. 





[6] Zhu S, Wang D, Low CB. Cooperative control of multiple UAVs for moving source seeking. J Intell Robot Sysms 2014;74:333-46. 





[7] Kasugai K, Miyagawa I, Murakami K. Leader-follower formation control of multiple unmanned aerial vehicles for omnidirectional patrolling. Int Worksh Adv Image Technol (IWAIT) 2019 2019;11049:477-82. SPIE. 





[8] Hu B, Seiler P. Pivotal decomposition for reliability analysis of fault tolerant control systems on unmanned aerial vehicles. Reliab Eng Syst Saf 2015;140: 130-41. https://doi.org/10.1016/j.ress.2015.04.005. 





[9] Wang X, Ning R, Zhao X, Wu C. Reliability assessments for two types of balanced systems with multi-state protective devices. Reliab Eng Syst Saf 2023;229:108852. https://doi.org/10.1016/j.ress.2022.108852. 





[10] Xu B, Bai G, Zhang Y, Fang Y, Tao J. Failure analysis of unmanned autonomous swarm considering cascading effects. J Syst Eng Electron 2022;33:759-70. https://doi.org/10.23919/JSEE.2022.000069. 





[11] Bai G, Li Y, Fang Y, Zhang Y-A, Tao J. Network approach for resilience evaluation of a UAV swarm by considering communication limits. Reliab Eng Syst Saf 2020; 193:106602. https://doi.org/10.1016/j.ress.2019.106602. 





[12] Cheng C, Bai G, Zhang Y-A, Tao J. Resilience evaluation for UAV swarm performing joint reconnaissance mission 2019:15. 





[13] Sun Q, Li H, Wang Y, Zhang Y. Multi-swarm-based cooperative reconfiguration model for resilient unmanned weapon system-of-systems. Reliab Eng Syst Saf 2022; 222:108426. https://doi.org/10.1016/j.ress.2022.108426. 





[14] Li H, Sun Q, Zhong Y, Huang Z, Zhang Y. A soft resource optimization method for improving the resilience of UAV swarms under continuous attack. Reliab Eng Syst Saf 2023;237:109368. https://doi.org/10.1016/j.ress.2023.109368. 





[15] Li H, Sun Q, Wang M, Liu C, Xie Y, Zhang Y. A baseline-resilience assessment method for UAV swarms under heterogeneous communication networks. IEEE Syst J 2022;16:6107-18. https://doi.org/10.1109/JSYST.2022.3197324. 





[16] Gomes PME. Failure analysis methods in unmanned aerial vehicle (UAV) applications 2007. 





[17] Revill MB. UAV swarm behavior modeling for early exposure of failure modes. Monterey United States: Naval Postgraduate School; 2016. 





[18] Sud A. UAVs and counter UAVs technologies in the world and the indigenous capability. CLAWS J 2020;13:65-84. 





[19] Choi J, Seo M, Shin H-S, Oh H. Adversarial swarm defence using multiple fixed-wing unmanned aerial vehicles. IEEE Trans Aerosp Electron Syst 2022;58:5204-19. https://doi.org/10.1109/TAES.2022.3169127. 





[20] Luo R, He G, Bu X, Shi J. Cooperative guidance law for the mother-cabin of the anti-UAV cluster mother-son missile. Appl Sci 2023;13:5397. https://doi.org/10.3390/app13095397. 





[21] Sharma A. Counter-Unmanned Aircraft Systems (C-UAS) n.d. 2012. 





[22] He D, Yang G, Li H, Chan S, Cheng Y, Guizani N. An effective countermeasure against UAV swarm attack. IEEE Net 2020;35:380-5. 





[23] Dui H, Zhang C, Bai G, Chen L. Mission reliability modeling of UAV swarm and its structure optimization based on importance measure. Reliab Eng Syst Saf 2021; 215:107879. https://doi.org/10.1016/j.ress.2021.107879. 





[24] Feng Q, Liu M, Dui H, Ren Y, Sun B, Yang D, et al. Importance measure-based phased mission reliability and UAV number optimization for swarm. Reliab Eng Syst Saf 2022;223:108478. https://doi.org/10.1016/j.ress.2022.108478. 





[25] Xu B, Liu T, Bai G, Tao J, Zhang Y, Fang Y. A multistate network approach for reliability evaluation of unmanned swarms by considering information exchange capacity. Reliab Eng Syst Saf 2022;219:108221. https://doi.org/10.1016/j.ress.2021.108221. 





[26] Wu C, Zhao X, Wang S, Song Y. Reliability analysis of consecutive-k-out-of-r-from-n subsystems: f balanced systems with load sharing. Reliab Eng Syst Saf 2022;228: 108776. https://doi.org/10.1016/j.ress.2022.108776 





[27] Guikema SD. A comparison of reliability estimation methods for binary systems. Reliab Eng Syst Saf 2005;87:365-76. https://doi.org/10.1016/j.ress.2004.06.007. 





[28] Wang X, Zhang Y, Wang L, Lu D, Zeng G. Robustness evaluation method for unmanned aerial vehicle swarms based on complex network theory. Chinese J Aeronaut 2020;33:352-64. https://doi.org/10.1016/j.cja.2019.04.025. 





[29] Biediger D, Mahadev A, Becker AT. Investigating the survivability of drone swarms with flocking and swarming flight patterns using virtual reality. In: Proceedings of the IEEE 15th International Conference on Automation Science and Engineering (CASE). IEEE; 2019. p. 1718-23. https://doi.org/10.1109/COASE.2019.8843173. 





[30] Holling CS. Resilience and Stability of Ecological Systems. Annu.Rev Ecol Syst. 1973;4:1-23. https://doi.org/10.1146/annurev.es.04.110173.000245. 





[31] Tran HT, Domercant JC, Mavris DN. A network-based cost comparison of resilient and robust system-of-systems. Proc Comput Sci. 2016;95:126-33. https://doi.org/10.1016/j.procs.2016.09.302. 





[32] Chen Z, Hong D, Cui W, Xue W, Wang Y, Zhong J. Resilience evaluation and optimal design for weapon system of systems with dynamic reconfiguration. Reliab Eng Syst Saf 2023;237:109409. https://doi.org/10.1016/j.ress.2023.109409. 





[33] Izaddoost A, Naderpajouh N, Heravi G. Modelling principal-agent dilemma for management of resilience in interdependent infrastructure systems. Reliab Eng Syst Saf 2023;238:109424. https://doi.org/10.1016/j.ress.2023.109424. 





[34] Trucco P, Petrenj B. Characterisation of resilience metrics in full-scale applications to interdependent infrastructure systems. Reliab Eng Syst Saf 2023;235:109200. https://doi.org/10.1016/j.ress.2023.109200. 





[35] Arango E, Nogal M, Yang M, Sousa HS, Stewart MG, Matos JC. Dynamic thresholds for the resilience assessment of road traffic networks to wildfires. Reliab Eng Syst Saf 2023;238:109407. https://doi.org/10.1016/j.ress.2023.109407. 





[36] Wu Y, Hou G, Chen S. Post-earthquake resilience assessment and long-term restoration prioritization of transportation network. Reliab Eng Syst Saf 2021;211: 107612. https://doi.org/10.1016/j.ress.2021.107612. 





[37] Jiang Q, Cai B, Zhang Y, Xie M, Liu C. Resilience assessment methodology of natural gas network system under random leakage. Reliab Eng Syst Saf 2023;234:109134. https://doi.org/10.1016/j.ress.2023.109134. 





[38] Hasanzad F, Rastegar H. Application of optimal hardening for improving resilience of integrated power and natural gas system in case of earthquake. Reliab Eng Syst Saf 2022;223:108476. https://doi.org/10.1016/j.ress.2022.108476. 





[39] Haimes YY. On the definition of resilience in systems. Risk Anal 2009;29(4): 498-501. https://doi.org/10.1111/j.1539-6924.2009.01216.x. 





[40] Ni T, Modarres M. Using dynamic master logic diagram for component partial failure analysis n.d. 





[41] Yeh W-C. Novel binary-addition tree algorithm (BAT) for binary-state network reliability problem. Reliab Eng Syst Saf 2021;208:107448. https://doi.org/10.1016/j.ress.2021.107448. 





[42] Yeh W-C. Building Reliable Budget-Based Binary-State Networks. Reliab Eng Syst Saf 2023:109567. https://doi.org/10.1016/j.ress.2023.109567.443. 





[43] Tuteja RK, Arora RT, Taneja G. Analysis of a two-unit system with partial failures and three types of repairs. Reliab Eng Syst Saf 1991;33:199-214. https://doi.org/10.1016/0951-8320(91)90059-G. 





[44] Jenny JA. The effect of partial failure modes on reliability analysis. IEEE Trans Reliab 1969;18:175-80. 





[45] Won JK, Modarres M. Improved bayesian method for diagnosing equipment partial failures in process plants. Comput Chem Eng 1998;22:1483-502. https://doi.org/10.1016/S0098-1354(97)00276-7. 





[46] Bruneau M, Chang SE, Eguchi RT, Lee GC, O'Rourke TD, Reinhorn AM, et al. A framework to quantitatively assess and enhance the seismic resilience of communities. Earthquake Spectra 2003;19:733-52. https://doi.org/10.1193/1.1623497. 





[47] Sahebjamnia N, Torabi SA, Mansouri SA. Integrated business continuity and disaster recovery planning: Towards organizational resilience. Euro J Operat Res. 2015;242:261-73. https://doi.org/10.1016/j.ejor.2014.09.055. 





[48] Zobel CW, Khansa L. Characterizing multi-event disaster resilience. Comp Oper Res 2014;42:83-94. 





[49] Henry D, Emmanuel Ramirez-Marquez J. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99: 114-22. https://doi.org/10.1016/j.ress.2011.09.002. 





[50] Nan C, Sansavini G. A quantitative method for assessing resilience of interdependent infrastructures. Reliab Eng Syst Saf 2017;157:35-53. https://doi.org/10.1016/j.ress.2016.08.013. 





[51] Tran HT, Balchanos M, Domercant JC, Mavris DN. A framework for the quantitative assessment of performance-based system resilience. Reliab Eng Syst Saf 2017;158:73-84. https://doi.org/10.1016/j.ress.2016.10.014. 





[52] Cheng C, Bai G, Zhang Y-A, Tao J. Improved integrated metric for quantitative assessment of resilience. Adv Mech Eng. 2020;12:168781402090606. https://doi.org/10.1177/1687814020906065. 





[53] Liu T, Bai G, Tao J, Zhang Y-A, Fang Y, Xu B. Modeling and evaluation method for resilience analysis analysis of multi-state networks. Reliab Eng Syst Saf 2022;226:108663. https://doi.org/10.1016/j.ress.2022.108663. 





[54] Schafer RW. What is a savitzky-golay filter? IEEE Signal Process Mag 2011;28(4): 111-7. https://doi.org/10.1109/MSP.2011.941097. 





[55] Strandbirk-Peshkin A, Papageorgiou D, Crofoot MC, Farine DR. Inferring influence and leadership in moving animal groups. Phil Trans R Soc B 2018;373:20170006. https://doi.org/10.1098/rstb.2017.0006. 





[56] Weimer CW, Miller JO, Hill RR. Agent-based modeling: An introduction and primer. In: Proceedings of the Winter Simulation Conference (WSC). IEEE; 2016. p. 65-79. https://doi.org/10.1109/WSC.2016.7822080. 





[57] Xu B, Bai G, Liu T, Fang Y, Zhang Y, Tao J. An improved swarm model with informed agents to prevent swarm-splitting. Chaos Soliton Fract. 2023;169: 113296. https://doi.org/10.1016/j.chaos.2023.113296. 





[58] Zhou X, Bai G, Tao J, Xu B. An improved method to search all minimal paths in networks. IEEE Trans Rel. 2023;1-12. https://doi.org/10.1109/TR.2023.3234055. 

