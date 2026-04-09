# A framework for the quantitative assessment of performance-based system resilience

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/43b62f3645eb0d418e3cb8fb2caf2ab718724b800410ce510342e589234898f5.jpg)


sm 

Huy T. Tran⁎ , Michael Balchanos, Jean Charles Domerçant, Dimitri N. Mavris 

Aerospace Systems Design Laboratory, Georgia Institute of Technology, 275 Ferst Dr., Atlanta, GA, USA 

# A R T I C L E I N F O

Keywords: 

System resilience 

Resilience metrics 

Adaptive networks 

# A B S T R A C T

Increasing system complexity and threat uncertainty require the consideration of resilience in the design and analysis of engineered systems. While the resilience engineering community has begun to converge on a definition and set of characteristics for resilience, methods for quantifying the concept are still limited in their applicability to system designers. This paper proposes a framework for assessing resilience that focuses on the ability of a system to absorb disruptions, recover from them, and adapt over time. The framework extends current approaches by explicitly considering temporal aspects of system responses to disruptions, volatility in system performance data, and the possibility of multiple disruption events. Notional system performance data is generated using the logistic function, providing an experimental platform for a parametric comparison of the proposed resilience metric with an integration-based metric. An information exchange network model is used to demonstrate the applicability of the framework towards system design tradeoff studies using stochastic simulations. The presented framework is domain-agnostic and flexible, such that it can be applied to a variety of systems and adjusted to focus on specific aspects of resilience. 

# 1. Introduction

The concept of resilience has expanded the focus of engineering complex systems beyond traditional discussions of robustness, reliability, and risk management. Since being introduced by Holling [1], resilience has placed greater emphasis on a system's adaptability and recoverability, in addition to its ability to absorb disruptions. This transition is readily observed across government and industry, and is beginning to alter the way in which we approach systems engineering. The need for resilience is especially strong for increasingly interconnected and complex systems, such as those under the purview of the military [2], national infrastructures [3], and economic systems [4]. 

Traditional systems engineering attempts “to anticipate and resist disruptions through classical reliability methods, such as redundancy at the component level and use of preventative maintenance at the system level” [5]. In comparison, resilience shifts the focus towards sustaining and recovering critical system functions in the presence of potential threats or failures, often through adaptation. There has been much discussion regarding the meaning of resilience and appropriate metrics for quantifying it. Quantifying resilience is particularly motivated by the need to support design and decision making, enabling “system resilience to be considered as an attribute of a system's delivery 

system” [6]. 

This paper presents a framework for making quantitative assessments of system resilience using performance data. Current approaches for assessing resilience consider many of the foundational aspects of resilience, such as absorption, restoration, and adaptation. This paper seeks to extend those approaches by capturing additional features of complex system environments and behaviors, such as repeated disruptions and volatility in delivered system performance. These features are often observable characteristics of many complex systems and the environments in which they operate. 

The remainder of this paper is organized as follows. Section 2 provides further background regarding definitions of resilience and metrics for quantifying it. Section 3 describes the proposed framework for assessing resilience. Section 4 describes a method for parametrically comparing potential resilience metrics using the logistic function, and implements the method to compare the developed resilience metric with a commonly used one from the literature. Section 5 describes the application of the framework to an information exchange network model. Section 6 summarizes contributions of this paper and opportunities for further advancing the field of resilience engineering. 

# 2. Background

An interdisciplinary discussion has developed concerning how designers can incorporate resilience into the engineering of complex systems and system of systems (SoS). Using Holling's definition [1] as a starting point, numerous publications attempt to shed more light on the ideal behavior of a resilient system. The safety engineering community has driven this effort [7], with contributions from specific domains such as critical infrastructures [8,9], communication networks [10], logistic and transportation networks [11,12], and organizational resilience [13]. Despite differences between systems of interest within these communities, the majority of the formulated definitions follow Holling's lead, defining resilience as a system property describing its capacity to adapt to, recover from, and absorb potential disruptions. 

This section gives a brief overview of prominent resilience definitions and identifies important properties of a resilient system. Following this overview, relevant frameworks and metrics for assessing resilience are discussed to establish a foundation for the proposed framework. The reader is referred to existing reviews of resilience engineering for a more thorough discussion of the field [6,14–16]. 

# 2.1. Defining resilience

Much of the early work in resilience engineering has focused on identifying definitions for resilience and common properties of resilient systems. These definitions appear within various scientific fields and are often tailored to specific applications of interest (e.g. see the review by Ref. [17]). However, each definition captures certain aspects of resilience, collectively building our understanding of the concept and improving our ability to address resilience in the system design process. 

The Department of Defense suggests that an architecture is resilient if it can provide functions necessary for mission success with high probability, in spite of hostile action or adverse conditions. The architecture should also maintain short periods of reduced capability across a wide range of scenarios, conditions, and threats [18]. In nonmilitary applications, emphasis is often given towards dynamic system recoverability; i.e. the ability of a system or organization to react to and recover from disturbances at an early stage, with minimal effect on its dynamic stability [19]. Francis and Bekera review resilience definitions from several other disciplinary perspectives [6]. 

To further develop the concept of resilience, many researchers focus on identifying design heuristics or unique properties commonly seen in resilient systems [20,21]. Vugrin et al. break down system resilience into three capacities: the absorptive, restorative, and adaptive capacities of a system [22]. The absorptive capacity is the degree to which a system “can automatically absorb the impacts of system perturbations and minimize consequences with little effort.” The restorative capacity focuses on exogenous system repair. The adaptive capacity focuses on endogenous mechanisms to respond to disturbances, e.g. through selforganization and learning mechanisms. The National Academy of Sciences provides a similar breakdown, adding preparation and planning as an additional capacity [23]. Linkov et al. and Fox-Lent et al. present these capacities in the form of a resilience matrix, mapping various system domains to each capacity [24,25]. 

There has also been discussion in the literature regarding the overlap between resilience and other system attributes, such as robustness, vulnerability, and reliability. Robustness is commonly defined as insensitivity to defined perturbations [16,26,27]. Uday and Marais add that robustness aims to minimize performance loss immediately following a disturbance; in comparison, resilience allows for some performance loss in the hope of recovering that performance over time [15]. Vulnerability focuses on susceptibility to known disturbances [26]. Reliability characterizes “the ability of a system and its components to perform required functions under stated conditions for a specified period of time” [15]. Reliability engineering 

aims to minimize failure probabilities, for example through mean time between failures analysis [20]. 

Resilience builds upon these concepts by focusing on the ability to mitigate the impacts of unexpected disturbances. The complexity and interdependencies of modern systems and SoS make it improbable to identify and prevent all possible disturbances. Therefore, focusing on known and expected threats (e.g. through robust design, vulnerability assessment, and reliability engineering) leaves a system dangerously susceptible to unanticipated ones. As such, resilience engineering aims to design systems capable of not just preventing or absorbing a disturbance, but also recovering from disturbances over time [15,20,26]. Resilience is also primarily a structural property of a system in that it is strongly derived from the organization or topology of the system. Robustness is similarly structural, vulnerability less so, and reliability instead focused on functional component design. 

Woods argues that only focusing on recovery (or rebound) is insufficient for resilience engineering [16]. Resilience should also thoroughly consider adaptation, including graceful extensibility (i.e. the ability to stretch finite resources to handle disturbances near operational bounds) and sustained adaptability (i.e. the ability to adapt throughout a system's life cycle). Investigations of complex systems and principles of their evolution support this need to fully consider adaptation, as well as tradeoffs between resilience and efficiency [27,28]. As a system adapts to address one threat, it often unintentionally exposes itself to others, creating a spiral-like evolution of adaptation and resilience [29]. Finite resources and a need for efficiency may push such a system towards a state of brittleness, rather than resilience. 

Considering discussions of resilience from a variety of communities, we assume the resilience definition given by the National Academy of Sciences for this framework: 

Resilience is the ability to prepare and plan for, absorb, recover from, and more successfully adapt to adverse events [23]. 

# 2.2. Quantifying resilience

Definitions of resilience allow system designers to identify desired system properties and make qualitative assessments of resilience. However, methods and metrics for quantitatively assessing resilience are also required to enable rigorous and traceable comparisons between potential system designs [23]. Several quantitative assessment methods have been proposed in the literature [30–36]. This discussion focuses on those from Vugrin et al. [22], Henry et al. [37], and Francis and Bekera [6], since their approaches effectively capture most aspects of resilience as previously described. 

The resilience assessment framework from Vugrin et al. [22] uses an integration-based calculation of resilience, focusing on time-averaged effects of a threat on system performance. The authors also propose an integration-based quantification of required recovery effort (used as a proxy for the cost of resilience). The framework includes a qualitative component, mapping the ability of a system to provide three resilience capacities (i.e. absorptive, restorative, and adaptive) to desired functions or services. Their proposed metrics capture the overall system response well by quantifying cumulative system performance and cost over time, relative to a specified disruption event. 

Henry et al. also present a framework with a performance-based metric for resilience [37]. Their metric converts time-dependent performance data to a time-dependent resilience figure-of-merit, $R ( t )$ . This metric describes the ratio of current system performance to lost performance at a given time t. The authors also consider recovery time and resilience costs through a system decomposition into components. 

Francis and Bekera propose a framework that calculates a single resilience value from performance data for a system facing a disruption event, thus simplifying design comparisons and decision-making 

processes [6]. Their metric includes a recovery time factor to capture temporal aspects of resilience, and normalized post-disruption and stable recovered performance levels to represent system absorptive and restorative capacities. The authors also account for uncertainty in event occurrences through consideration of event probabilities. Hence, their method can be described as a resilience-based risk assessment. 

These resilience assessment frameworks account for many desired aspects of resilience, including the impact of disruptions on system performance, recovery costs, and recovery time. However, these frameworks, and others in the literature, can be extended by providing more explicit consideration of certain system features and environmental characteristics that play a role in determining the resilience of a system. This paper develops a resilience assessment framework that contributes to the literature by addressing the following: 

• Multiple disruptions over time – Many systems will face multiple disruptions over time, requiring analysis of how they respond to those events over their entire life-cycle. 

• Volatility in system performance data – Real and simulated system behaviors often will not resemble idealized performance time data, as presented in many notional resilience diagrams (e.g. see Fig. 2). 

• A repeatable process for quantifying resilience that can be automated – Many existing frameworks provide limited guidance for how to determine certain values used in resilience calculations, limiting their applicability to large simulation-based design studies. 

Experiments for characterization of resilience metric behaviors – Standardized methods should be developed to enable cross-discipline comparisons of potential resilience metrics and identify behaviors of those metrics as system response dynamics are altered. 

# 3. A quantitative resilience assessment framework

This section introduces a framework for assessing the resilience of a system, or systems, of interest. We give particular attention to the development of a set of resilience factors and two resilience metrics, R and $R _ { t o t a l } ,$ used to measure the resilience of a system subjected to one or more disruptions. The framework is composed of five steps, illustrated in Fig. 1: identification of systems of interest, potential disruptions, and potential recovery actions, followed by measurement of system performance and calculation of system resilience. This framework enables quantitative comparisons of potential system designs, with respect to their resilience to a set of disruptions. For example, this framework could be used to assess the resilience of various communication networks, where multiple recovery actions are being considered. 

With regards to the overall system design process, this framework focuses on resilience assessment. That is, the framework does not explicitly suggest methods for improving resilience; we assume that system designs and their potential recovery or adaptation mechanisms have already been identified. However, the framework can be used to identify system weaknesses and suggest areas of improvement, through comparison of individual resilience factors (each of which quantifies a particular aspect of system resilience). 

The framework can be combined with various methods for design space exploration (e.g. Design of Experiments), subject matter experts, and tradespace analysis (e.g. sensitivity analysis) to identify and explore potential system designs and improvements. Decision theory (e.g. multi-criteria decision making) could then be used to compare system designs such that multiple design objectives, including resilience, are accounted for. The combination of these methods would formulate a thorough process for conceptual system design, using this assessment framework as a basis for performing quantified resilience assessments. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/5499515e6437bb95d6f6fa702749a6d505645f4f6574e9f2abac1e9394862850.jpg)



Fig. 1. Overview of the resilience assessment framework.


# 3.1. System description

The framework begins with a definition of the systems being considered and their desired capabilities. These systems may be currently existing ones with suspected vulnerabilities, future systems being considered in a design study, or any other systems requiring a resilience assessment. These systems can range from complicated systems (e.g. an airplane) to complex, heterogeneous SoS (e.g. a ballistic missile defense system). The framework uses system performance data to calculate a set of resilience factors and metrics and is therefore independent of system complexity or heterogeneity, as long as the user is able to obtain measurements of system performance over time. Though we assume that the framework can be applied to a wide range of system scales and complexities, we do not assume that resilience itself is a scalable property; the scalability of resilience is an open research area. 

System capabilities are defined as specific functions that a system is desired to be able to provide or perform. System performance is defined as a time-varying measure of how well a system is achieving a desired capability at a given time t. For example, a communications network may be designed to provide certain data transfer rates (i.e. a throughput rate of $c$ data packets per second). A desired capability of this network is then the ability to transfer data packets. However, while a network may be capable of transferring $c$ data packets per second, at any given time instant t, the actual observed throughput rate of the network (i.e. its performance) is some value $y ( t )$ that may differ from C. 

# 3.2. Potential disruptions analysis

When assessing the resilience of a system, an analyst must consider what the system is resilient to, since “the resilience of a system can be measured only in terms of the specific threat (input)… different attacks would generate different consequence (output) trajectories for the same resilient system” [26]. Therefore, the framework requires identification of potential threats, or disruptions, to be considered. 

Consider a structure designed for use in areas known for strong tornado activity. Since this structure was designed in anticipation of destructive wind speeds, it will likely be resilient to storms with high wind speeds. However, this same structure may not be as resilient to flooding, since it was not designed with such disruptions in mind. Stating that a system is simply resilient does not provide enough information regarding the expected performance of the system. A more complete statement would include what the system is resilient to: high wind speeds in this example. 

# 3.3. Recovery action analysis

The framework also requires identification of potential recovery actions. These recovery actions enable a system to respond to disruptions and recover lost capabilities. Some recovery actions may even improve system capabilities relative to normal operating conditions, providing a level of anti-fragility to the system [38]. Example recovery actions include repairing damaged systems and adapting or reconfiguring existing system structures. 

# 3.4. System performance measurement

This framework uses system performance data to calculate resilience. Since temporal aspects of a system's response to disruptions play a large role in resilience [26], we use measurements of system performance over time. These measurements are assumed to be equally spaced in time, such that they can be represented as time series data. This assumption enables the use of time series methods for analyzing a system's performance response. Though we use performance data to calculate resilience, we do not assess resilience as a direct measure of functional performance. Instead, we focus on resilience as a structural property of a system, characterizing its ability to maintain or improve desired functional performance levels over time. 

Two approaches for obtaining performance data are using recorded data from actual system operations and modeling and simulation. If possible, real system data should be used, provided that the data is complete and has been accumulated over periods of time in which the system faced disruptions of interest. However, such data is often highly corrupted or simply not available, particularly for large, complex systems for which resilience assessments are often desired. Additionally, resilience assessments may be needed for system design tradeoff studies. Systems of interest in such studies typically do not exist, limiting the availability of performance data. 

We suggest the use of modeling and simulation to produce system performance data, in the absence of actual observed data. This approach enables analysis of small and large systems, with consideration of multiple system designs, disruption types, and recovery actions. Simulation studies can also capture stochasticity in system operations, for example through the use of simulation replications or Monte Carlo simulation. Many systems operate in environments characterized by random or uncertain behaviors, which can strongly affect the impact of disruptions on a system and the ability of the system to respond to those disruptions. 

Focusing on a single capability (and subsequently a single measure of system performance) assumes that behaviors to be characterized are adequately represented by that capability. This assumption may be challenged by SoS with multiple stakeholders and objectives. For example, the ballistic missile defense system (BMDS) includes communication, radar, and weapon systems, among many others. Many of these systems are independently operated with differing immediate objectives. Analyzing the BMDS within this framework requires one to identify a single capability representative of the overall objective of the SoS, e.g. the probability of intercepting an enemy missile. Identifying a single SoS capability may be more difficult in other cases, such as the national infrastructure SoS, which includes many critical infrastructure sectors or domains. Multiple resilience analyses can be performed if 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/3021ed5b0304995a73a1a6b2f9b9bec5b1ec449849ef04c384f6d3ff3b8cce77.jpg)



Fig. 2. Notional plot of system performance data. The inset figure shows an example of volatile (solid line) and smoothed (dashed line) performance data.


available performance data is comparable among various domains. Multi-criteria decision making can also be used to handle multiple domain concerns. 

Fig. 2 shows a notional example of system performance data, where $y ( t )$ represents the performance of a system at time t. Important times and performance values in this notional example are defined as follows: 

• $t _ { 0 } ~ =$ start time of the period of interest 

• $t _ { D } =$ time of the disruption event 

• $t _ { R } =$ time when the recovery action is implemented 

• $t _ { S S } =$ time when recovered performance has reached steady-state 

• $t _ { f i n a l } =$ end time of the period of interest 

• $y _ { D } =$ desired performance (i.e. normal operating performance level) 

• $y _ { R } =$ recovered performance 

• $y _ { m i n } =$ minimum performance 

The notional data in Fig. 2 shows clear trends and smooth transitions in system performance. However, actual measured or simulated data is often volatile or noisy, due to the stochastic nature of many real or simulated processes (see the inset of Fig. 2). Since we are primarily concerned with general trends in the data, we use smoothed performance data for the calculation of resilience metrics. We smooth the data using a Savitzky-Golay (S-G) filter [39]. S-G filters maintain the shape of narrow peaks in data, at the expense of removing less noise than other moving average filters [40,41]. Since system degradation and recovery may produce large, narrow peaks in performance data, S-G filters are used for smoothing performance data. 

For the remaining discussion of the assessment framework, $y _ { r a w } ( t )$ represents raw performance data and $y ( t )$ represents the raw data smoothed using an S-G filter. The smoothed data is used for all resilience metric calculations. The raw data is only used for calculation of the volatility factor. 

# 3.5. System resilience calculation

We define a resilience metric, $R$ , to quantify a system's resilience to one disruption event. Providing a single metric for resilience enables quantitative comparisons between system designs and simplifies tradeoff studies that may involve a large design space and multiple decision criteria. For example, measuring resilience with a single metric simplifies the process of identifying the Pareto frontier of resilience and cost for a given design space. Using a time-dependent measure of resilience, such as that proposed by Henry et al. [37], requires further 

analysis to characterize that tradeoff. 

We develop $R$ by identifying important characteristics of a resilient system, based on our assumed definition of resilience. These characteristics are quantified by a set of resilience factors, which are used to calculate the system resilience, $R$ , as 

$$
R = \left\{ \begin{array}{l l} \sigma \rho [ \delta + \zeta + 1 - \tau^ {(\rho - \delta)} ] & \text {i f} \rho - \delta \geq 0 \\ \sigma \rho (\delta + \zeta) & \text {o t h e r w i s e}, \end{array} \right. \tag {1}
$$

where $0 \leq R \leq \infty$ , and has a reference value of two for a normal operating scenario (i.e. a scenario with no loss of desired performance over time). A normal operating scenario could be one in which no disruption occurs or the disruption is so insignificant that it has no observable effect on the system's performance. A scenario with $R > 2$ would typically be one where the system's performance increases over the initial or desired level following a recovery action. The upper limit for this metric is shown as infinite because the metric is bounded by the theoretical limit of the performance data. For example, the recovery factor $\rho$ (discussed in Section 3.5.2) is proportional to the final recovered performance level of the system within the time period considered; there is no clear bound on this value. 

This metric is based on the integration of performance data, defined as the total performance factor, σ, similar to other resilience metrics in the literature [22,32,42]. However, we modify this integration-based approach by incorporating a set of additional resilience factors to explicitly account for various aspects of resilience. The recovery factor, $\rho$ , accounts for the end state of the system (i.e. its recovered performance). The absorption factor, δ, accounts for the ability of the system to absorb the effects of a disruption. The volatility factor, ζ, accounts for the volatility of performance data, representing the ability of the system to smoothly transition from one state to another. The normalized recovery time factor, τ, accounts for temporal aspects of the system response through calculation of the time required to reach steady-state following a disruption. The influence of $\tau$ decreases as the amount of performance recovered (i.e. $\rho - \delta )$ decreases. The conditional statement in Eq. (1) ensures that systems are only rewarded for quickly reaching steady-state (i.e. having low values of τ) if their recovered performance is better than their minimum performance. Note that only one R value is calculated for a specified time period (i.e. $R$ is a function of a time period $t _ { 0 }$ to $t _ { f i n a l } ,$ rather than directly being a function of time t). The following sections describe the calculation of each resilience factor (refer to Fig. 2 for descriptions of performance data variables used in calculations). 

# 3.5.1. Total performance factor

The total performance factor, $\sigma$ , accounts for the total performance maintained by a system throughout the time period of interest. This factor is calculated as 

$$
\sigma = \frac {\sum_ {t = t _ {0}} ^ {t _ {\text {f i n a l}}} y (t)}{y _ {D} \left(t _ {\text {f i n a l}} - t _ {0}\right)}, \tag {2}
$$

where $0 \leq \sigma \leq \infty$ , and has a value of one in a normal operating scenario. This metric is based on the integration of performance data with respect to time. Since this data is obtained at discrete time steps, $\sigma$ is calculated as a summation of the performance data. We normalize this summation by the desired integration value. 

Measuring resilience with performance integration alone rewards systems able to provide high levels of performance at any point of time during a scenario. However, it does not account for when that performance is provided. Consider two systems, A and B. System A may show significant performance degradation immediately following a disruption, but quickly recover nearly all of that performance over time once a recovery action is implemented (see Fig. 3). In comparison, system B may show very little initial performance degradation following a disruption, but slowly lose performance over time. Despite differences in the dynamic responses of these two systems, there is 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/cab98834e6a041f01c87cfa407a991cfe85f51049ebfb131e7992e392ce33df4.jpg)



Fig. 3. Notional comparison of performance data for two systems with different responses to a disruption. System A shows a large initial degradation in performance following the disruption, but is able to quickly recover most of the lost performance. System $B$ shows a slow, gradual decline in performance following the disruption, but is not able to recover any lost performance over time. These performance data show different responses to a disruption but have notionally similar integration values.


the possibility for integration of their performance data to have similar values, suggesting similar integration-based resilience. Therefore, additional resilience factors are considered to more distinctly quantify system resilience. 

# 3.5.2. Absorption, recovery, and recovery time factors

The ability of a system to absorb the impacts of a disruption and recover lost capabilities in a timely manner is critical to its resilience [6,22]. The absorption factor, δ, captures how well a system is able to absorb a disruption and reduce its impact on system performance. This factor is calculated as 

$$
\delta = \frac {y _ {\text {m i n}}}{y _ {D}}, \tag {3}
$$

where $0 \leq \delta \leq \infty$ , and has a value of one in a normal operating scenario. The minimum of the performance data is used for $y _ { m i n }$ . This factor can be greater than one if the system begins with a performance level higher than desired and is not strongly affected by the disruption (e.g. a system with volatile performance data or one that initially operates at a higher than expected performance level). 

This factor does not explicitly account for or differentiate between preventative and resistive measures used to mitigate threat impacts. Instead, such measures are implicitly accounted for by characterizing observed impacts on system performance. For example, if a system can implement preventative measures to anticipate threats and adjust itself before they occur, these actions will likely result in no or small change in performance, thus giving $\delta \approx 1$ (the nominal value). Likewise, a system able to resist threats such that no impact is seen on system performance will give $\delta = 1$ . 

The recovery factor, $\rho$ , captures how well a system is able to recover lost capabilities. This factor is calculated as 

$$
\rho = \frac {y _ {R}}{y _ {D}}, \tag {4}
$$

where $0 \leq \rho \leq \infty$ , and has a value of one in a normal operating scenario. Determining the recovered performance level, $y _ { R }$ , is a simple task when analyzing a small number of cases with clearly defined recovery values, such as those seen in Figs. 2 and 3. One can perform a visual inspection of the data, or if automated calculation is desired, select the final performance level as the recovered value. However, for automated analysis of data sets where the system does not recover to a clearly defined value (e.g. those from stochastic simulation studies), determining $y _ { R }$ is a non-trivial task. To account for these situations, we define $y _ { R }$ to be the steady-state performance of the system following a disruption event and possible implementation of a recovery action. Using steady-state performance provides a more accurate representa-

tion of what level the system has recovered to than, for instance, using the final observed system performance. 

We use the Marginal Standard Error Rules (MSER) method to determine when steady-state has been reached and what the steadystate performance is. MSER is a heuristic approach for handling the initialization bias problem in time series data [43–46]. This method estimates the length of the simulation warm-up period, $d ^ { * }$ , allowing an analyst to use a truncated subset of data (i.e. $y ( t )$ where $t > d ^ { * }$ ) to calculate the steady-state mean of a time series. Calculating the mean using the truncated time series attempts to remove any bias that may have been introduced to the data by initializing a simulation in a condition different from the expected steady-state condition. This method is often applied to output data generated by simulations of stochastic processes. 

The MSER method estimates the steady-state observation number, $d ^ { * }$ , using the MSER statistic, as 

$$
d ^ {*} = \underset {d \geq 0} {\arg \min } \quad \text {M S E R} (n, d) \tag {5}
$$

$$
\operatorname {M S E R} (\mathrm {n}, \mathrm {d}) = \frac {1}{(n - d) ^ {2}} \sum_ {t = d + 1} ^ {n} [ y (t) - \bar {y} (n, d) ] ^ {2}, \tag {6}
$$

where $n$ is the total number of observations in the time series and ${ \overline { { y } } } \left( n , d \right)$ is the mean of the truncated time series (i.e. the mean of the portion of the time series where $t > d$ ). White and Robinson [45] provide a description of the intuition behind this method for estimating simulation warm-up time. 

Using the MSER method, the steady-state recovery time of a system, $t _ { s s }$ , is defined as the time associated with the $d ^ { * } + 1$ observation in performance data. For example, for performance data beginning at time $t ~ = ~ 1 { \ : } s$ and incremented in one second time steps (i.e. $t = 1 , 2 , . . . )$ , if $d ^ { * } = 1 0$ then $t _ { s s } = 1 1 s$ . The steady-state performance of the system, $y _ { R }$ , is defined as the truncated mean following steadystate, 

$$
y _ {R} = \frac {1}{n - d ^ {*}} \sum_ {t = t _ {s s}} ^ {t _ {\text {f i n a l}}} y (t). \tag {7}
$$

Two modifications are implemented to apply the MSER method to performance data. A MSERrequired value determines whether or not steady-state is reached, where steady-state is only reached if $\mathrm { M S E R } ( n , d ^ { * } ) > \mathrm { M S E R } _ { \mathrm { r e q u i r e d } }$ . This threshold is necessary because typical implementations of MSER assume that steady-state is reached within the first half of a data set. If steady-state is not reached within the given time period, $y _ { R }$ is defined as the mean performance from the last $1 0 \%$ of performance data points (e.g. the mean of the final 10 data points for a dataset of 100 observations). A MSERthreshold defines the minimum MSER required to assume steady-state has been reached (i.e. steadystate is reached once $\mathbf { M S E R } ( n , d ) \leq \mathbf { M S E R } _ { \mathrm { t h r e s h o l d } } )$ . This threshold is implemented to account for cases where performance values decrease so slowly over time that the algorithm estimates steady-state at the end of the data set, even though very little change is seen in performance values past the first observation where the threshold is reached. Results shown in this paper use $\mathrm { \mathbf { M S E R } _ { \mathrm { r e q u i r e d } } } = 0 . 1$ and $\mathrm { M S E R } _ { \mathrm { t h r e s h o l d } } = 0 . 0 0 0 1$ . 

Steady-state recovery time is used to define the recovery time factor, τ, which captures the speed with which a system recovers to steady-state. This factor accounts for the ability of a system to not only respond to a disruption and recover lost capabilities, but to do so in a timely manner. The recovery time factor is calculated as the time until steady-state recovery is reached, relative to the total time period considered, 

$$
\tau = \frac {d ^ {*}}{n}, \tag {8}
$$

where $0 \leq \tau \leq 1$ , and has a value of zero in a normal operating scenario. 

The recovery time factor explicitly accounts for feedback dynamics related to system recovery (e.g. immediate versus slow recovery), but 

does not do so for similar dynamics related to initial performance degradation (e.g. sudden disruption versus slow drifts). Instead, the dynamics of performance degradation are implicitly accounted for by the total performance factor and the resulting ability of the system to recover from the degradation. The framework assumes that necessary time scales are considered in the collection of performance data to capture such feedback dynamics. 

# 3.5.3. Volatility factor

The ability of a system to provide smooth transitions from degraded to recovered states is accounted for with the volatility factor, ζ. A system with highly volatile performance data, such as that in the inset of Fig. 2, sees large and sudden drops in performance over time. We define this type of system to be less resilient than a system that produces similar, but smoother performance data. Signal-to-noise ratio $\mathrm { ( S N R _ { d B } ) }$ is used to quantify volatility in performance data, and is calculated as 

$$
\mathrm {S N R} _ {\mathrm {d B}} = 1 0 \log_ {1 0} \frac {P _ {s}}{P _ {n}} \tag {9}
$$

$$
P _ {s} = \sum_ {t = t _ {0}} ^ {t _ {\text {f i n a l}}} S (t) ^ {2} \tag {10}
$$

$$
P _ {n} = \sum_ {t = t _ {0}} ^ {t _ {\text {f i n a l}}} N (t) ^ {2}, \tag {11}
$$

where $P _ { s }$ is the signal power, $P _ { n }$ is the noise power, $S ( t )$ is the true signal, and $N ( t )$ is signal noise. The true signal is approximated with smoothed performance data, such that $S ( t ) = y ( t )$ . Signal noise is approximated as the difference between the raw data, $y _ { r a w } ( t )$ , and smoothed data using 

$$
N (t) = y _ {\text {r a w}} (t) - y (t) \tag {12}
$$

Fig. 4 shows an example comparison of raw and smoothed performance data, with the approximated performance noise. 

$\mathrm { S N R } _ { \mathrm { d B } }$ is converted to the volatility factor using a logistic function transformation as follows, 

$$
\zeta = \frac {1}{1 + \exp \left[ - 0 . 2 5 \left(\mathrm {S N R} _ {\mathrm {d B}} - 1 5\right) \right]}, \tag {13}
$$

where $0 \leq \zeta \leq 1$ , and has a value of one in a normal operating scenario. The function steepness (set to $- 0 . 2 5 )$ ) and offset (set to 15) are set to 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/1ccf008dc098ef39280c9ecc3941142bf1328aa76c5d8bc64e17d53e3d1cb769.jpg)



Fig. 4. Example of (top) raw and smoothed performance data, with (bottom) corresponding approximations for performance noise. The raw data is smoothed using an S-G filter with polynomial order 3 and frame size 11.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/7bb9281d7841cb225a0a91074640e39abb9a581dfc85f715ce765bf0529b5456.jpg)



Fig. 5. Notional example of performance data for a system subjected to multiple disruptions, with a recovery action implemented after each disruption. The scenario is split into three epochs for calculation of $R _ { 1 }$ R R 2 3, , , and $R _ { t o t a l }$ .


ensure that performance data with no observable volatility provides a volatility factor of one, with a gradual decline in $\zeta$ as volatility is increased. 

Accounting for volatility in this manner requires systems being compared to have similar performance measurement noise. Systems with differing levels of measurement or inherent process noise may have their resilience values undesirably affected by the volatility factor. For example, noise due to sensor measurements or model randomness needs to be comparable between systems, to prevent penalizing one system more than another due to measurement noise, rather than response volatility. We also assume that volatility in performance data is undesirable; in cases where volatility is purposely designed into the system, this factor should be removed from resilience calculations. 

# 3.5.4. Total resilience metric, $\mathbf { R } _ { \mathbf { t o t a l } }$

We also consider scenarios with multiple disruptions over time (see Fig. 5). Since the resilience metric, $R _ { : }$ , is defined for a scenario with a single disruption, multiple disruption scenarios are split into $N _ { e p o c h s }$ epochs, where each epoch is defined to contain a single disruption and the subsequent recovery action. System resilience for the ith epoch, $R _ { i } ,$ is calculated using Eq. (1). System total resilience, $R _ { t o t a l } ,$ is then calculated for the entire scenario using an exponentially weighted mean of $R _ { i }$ from each epoch, as 

$$
R _ {\text {t o t a l}} = \sum_ {i = 1} ^ {N _ {\text {e p o c h s}}} w _ {i} R _ {i}, \tag {14}
$$

where $0 \leq R _ { t o t a l } \leq \infty$ . The weights, $w _ { i } ,$ are defined as normalized coefficients of an exponentially weighted moving average filter, 

$$
w _ {i} = \frac {\alpha (1 - \alpha) ^ {N _ {\text {e p o c h s}} - i}}{\sum_ {j = 1} ^ {N _ {\text {e p o c h s}}} \alpha w _ {j}} = \frac {(1 - \alpha) ^ {N _ {\text {e p o c h s}} - i}}{\sum_ {j = 1} ^ {N _ {\text {e p o c h s}}} w _ {j}}, \tag {15}
$$

with smoothing factor $^ { a }$ and $0 \leq \alpha \leq 1$ . Higher values of $^ { a }$ increase the weight given to later values of $R _ { i }$ (i.e. $R _ { i }$ values associated with epochs that occur towards the end of a scenario are more heavily weighted than those occurring earlier in the scenario). 

A weighted mean is used to give preference to systems that improve their resilience over time, capturing the ability of a system to adapt to disruptions. System adaptation is separated from other resilience factors because it can improve (or potentially worsen) the other factors. This epoch-based calculation results in $R _ { t o t a l }$ being focused on longterm system performance and adaptation, while $R$ focuses on shortterm responses to a single disruption. If these time-scales become mixed (e.g. a system is subjected to a second threat before it has fully recovered from the first), there may be confounding in $R$ values calculated from later epochs. 

Analyzing multiple disruptions as separate epochs allows one to evaluate the evolution of a system over time and its ability to extend its resources and continually adapt. For example, as a system approaches the bounds within which it can handle disturbances, it may continue to exhaust constrained resources, which may in turn increase recovery 

time. This effect would be captured by decreasing $\tau$ and $R$ values in subsequent epochs. These high-level effects could be complemented with detailed analysis of cost and resource constraints, in addition to critical slowing down and tipping points to provide further insights into the graceful extensibility and sustained adaptability of a system [47,48]. 

This metric does not require that each threat faced by the system over time is the same. Though a system may more readily learn from and adapt to past threats if they are similar, it is also possible for a system to learn from different threats over time and adapt to certain aspects of each threat. 

# 4. Experimental resilience metric comparison

Since the presented framework strongly depends on the resilience metric, $R$ , we provide a comparison between $R$ and an integration metric, I, calculated as 

$$
I = \sum_ {t = t _ {0}} ^ {t _ {\text {f i n a l}}} y (t). \tag {16}
$$

We compare to integration because it provides a single value for resilience and is often used in the literature for quantifying resilience [22,32,30,42]. These comparisons focus on the ability of both metrics to capture expected trends and desired aspects of resilience for notional data, with respect to the assumed definition of resilience. 

We use a logistic function to create notional performance data, because these “S”-curves capture the general shape of systems undergoing performance degradation and recovery. We create performance data representative of a system facing a single disruption with no recovery action using 

$$
y (t) = A _ {1} + \frac {K _ {1} - A _ {1}}{1 + \exp \left[ B _ {1} \left(t - x _ {1}\right) \right]} + N \left(0, \sigma_ {1}\right), \tag {17}
$$

where $K _ { 1 }$ determines the initial performance level (i.e. the upper asymptotic limit of the function), $A _ { 1 }$ determines the minimum performance (i.e. the lower asymptotic limit), $B _ { 1 }$ determines the inflection steepness, and $x _ { 1 }$ determines the location of the inflection point on the t-axis. Volatility is modeled as Gaussian white noise, added to the data by drawing from a normal distribution with mean of zero and standard deviation $\sigma _ { 1 }$ . Fig. 6a shows the resulting function shape with the inflection steepness varied and white noise added to the inset figure. 

We also consider systems facing a single disruption with a recovery action. We add a recovery action to this notional data by using 

$$
y (t) = A _ {2} + \frac {K _ {2} - A _ {2}}{1 + \exp \left[ B _ {2} \left(t - x _ {2}\right) \right]} + N (0, \sigma_ {2}) \tag {18}
$$

for the recovery portion of the data, where a negative value is used for $B _ { 2 }$ to create an increasing function. Eq. (17) is still used for the degradation portion of the data, with $A _ { 1 }$ adjusted to ensure a smooth transition between the recovery and degradation portions of the data. Fig. 6b shows an example of data with a recovery action added. We focus on a single disruption event for this comparison because there is limited consideration of multiple disruptions among existing resilience metrics. 

Eqs. (17) and (18) are used to generate notional performance data for controlled comparisons between R and the integration metric, I. Logistic function parameters are parametrically varied to compare the behavior of these two resilience metrics as the shape of performance data is altered. These comparisons provide a sense of how well each metric is able to capture desired resilience trends of different potential performance data. We focus on results for cases with a recovery action, where parameters of the recovery logistic function $( K _ { 2 } , x _ { 2 } , B _ { 2 } , \sigma _ { 2 } )$ are varied. Similar results are seen for cases without a recovery action, when corresponding parameters of the degradation function are varied. 

Fig. 7 shows a comparison of $R$ and $I$ for cases where the recovered 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/e72d8da1f6f5484e92db77741f15991cc655cf9fe7f8ffbd28f00ee65146f06c.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/23befbd27884e4bda94758520f7124e9a3fb02b51a62f524cde1a0a77d0ff380.jpg)



(b)



Fig. 6. Notional performance data for (a) systems with no recovery action and (b) systems with a recovery action. Data in (a) is generated using Eq. (17), with the inflection steepness, $B _ { 1 }$ , varied $( A _ { \mathrm { l } } = 2 0$ , $K _ { \mathrm { l } } = 5 0$ , $x _ { 1 } = 2 5$ , $\sigma _ { \mathrm { { l } } } = 0 ,$ ). The inset figure shows how Gaussian white noise $( \sigma _ { 1 } = 1 0 )$ ) is used to model performance volatility, where the dashed line shows the corresponding data with no volatility (i.e. $\sigma _ { 1 } = 0$ ). Data in (b) is generated using Eq. (17) for $0 \leq t < 5 0$ and Eq. (18) for $5 0 \leq t \leq 1 0 0$ , and has the recovery steepness, $B _ { 2 }$ , varied $( K _ { 1 } = 5 0$ , $x _ { \mathrm { 1 } } = 2 5$ , $B _ { 1 } = 0 . 5$ , $\sigma _ { \mathrm { { l } } } = 0$ , $A _ { 2 } = 2 0$ , $K _ { 2 } = 4 0$ , $x _ { 2 } = 7 0$ , $\sigma _ { 2 } = 0$ ).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/bb2ac61989bc476576b7a5d078226122f40532c261ba6c523b32a0fba98c62a7.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/c21e7fa14e4f2d77d7c2ef5a30f98ca802e34a59ac772aaf01ef0bfa092ff038.jpg)



(b)



Fig. 7. Resilience R (a) and integration resilience $I$ (b) for cases with a recovery action. These cases correspond to those shown in Fig. 6b, with $K _ { 2 }$ and $x _ { 2 }$ varied and $B _ { 2 } = 0 . 5$ .


performance, $K _ { 2 } ,$ , and the location of the recovery inflection point, $x _ { 2 }$ , are varied. Both metrics capture expected resilience trends, as $R$ and $I$ increase as $K _ { 2 }$ is increased and $x _ { 2 }$ decreased. Increasing $K _ { 2 }$ should improve resilience because systems that recover to a higher performance level are more resilient, assuming that all other factors are held constant. Decreasing $x _ { 2 }$ should improve resilience because systems that recover faster are more resilient. 

Fig. 8 shows that $R$ and I have different trends when the recovery steepness, $B _ { 2 }$ , and volatility, $\sigma _ { 2 }$ , are varied. Considering cases with no volatility added (i.e. $\sigma _ { 2 } = 0 \mathrm { \ i }$ ), we see that resilience measured by R increases as $B _ { 2 }$ decreases. However, the opposite trend is seen when resilience is measured with I. This difference in trends is primarily due to the recovery factor, $\rho _ { 2 }$ , used in the calculation of R. This recovery factor rewards systems that are able to recover to a higher performance level, such as those with lower $B _ { 2 }$ values in these cases. The recovery time factor, τ, also rewards cases with low $B _ { 2 }$ values because of their fast recovery times. In comparison, the integration calculation of $I$ only considers the total performance maintained throughout the entire process. Therefore, $I$ rewards cases with higher $B _ { 2 }$ values due to their 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/5112c9976924e7d16b315d2b691d41830aafa7ef63adfdd84aee82f783ffbeda.jpg)



Fig. 8. Resilience R (a) and integration resilience I (b) for cases with a recovery action. These cases correspond to those shown in Fig. 6b, with $B _ { 2 }$ and $\sigma _ { 2 }$ varied.


ability to provide performance in the middle of the time period considered, despite lower recovered performance levels. Given these differences, R better captures resilience as defined for this paper, since it focuses on the ability to recover lost capabilities. Integration results also show less variability in resilience values, providing lower resolution in resilience comparisons. 

This preference of R over I depends on the definition of resilience used and domain being studied. There may be situations where the ability to absorb a disruption is more important than the ability to recover from it. Should an analyst wish to focus on particular aspects of resilience, weights can be added to the resilience factors to adjust $R$ as desired. For example, infrastructure dependency analysts may with to focus on the absorption factor in an effort to improve survivability, while disaster response analysts may wish to focus on the recovery factor. 

Fig. 8 also shows that $R$ and $I$ have different trends when volatility in performance data is varied through $\sigma _ { 2 }$ . Increasing $\sigma _ { 2 }$ decreases resilience measured by $R$ , due to the volatility factor, $\zeta .$ . This factor penalizes systems with highly volatile performance data, such as those 

represented by cases with high values of $\sigma _ { 2 }$ . In comparison, resilience measured by $I$ is minimally affected by changes to $\sigma _ { 2 }$ . These results demonstrate the ability of $R$ to account for performance volatility, a factor not considered by integration. 

# 5. Application problem: information exchange in a networked system

We demonstrate use of the proposed resilience assessment framework on a model of information exchange in a networked system. Many networked systems use connectivity among constituent members to enable information exchange critical to the overall performance of the system. Examples of such systems include technological networks such as the Internet [49] and the World-Wide Web [50], organizational networks or business firms [51], and social networks [52]. However, the networked nature of these systems can also introduce vulnerabilities, especially when there is a dependence on connectivity. System analysts must consider the question of what happens when nodes or links fail, and in the event that system performance is greatly comprised, identify methods to improve system resilience. We use the proposed framework to assess the resilience of networked systems, specifically considering the implementation of network adaptation through link rewiring as a response to repeated node removals. 

The application of our framework begins with a description of the system of interest. We focus on systems that can be represented as networks, where nodes are individual members within a system (e.g. people within an organization) and links are potential paths of information flow. We use a model based on the one proposed by Dodds, Watts, and Sabel for organizational networks [51] to simulate information exchange in a network. The goal of the networked system is to successfully enable information sharing between nodes, over an extended period of time. Information exchange is modeled by messages passed between source and target nodes, along existing paths in the network. These messages can represent information needed for the completion of a task, data being transferred from one location to another, or any other form of information that may be contained in a message. This model is not validated by empirical data; it is meant to investigate fundamental behaviors of networked systems and provide high-level insights regarding ways to improve network resilience. There are limitations to such abstraction of networked systems [53,54], requiring additional consideration of higher fidelity and domainspecific models to provide actionable recommendations to decision makers. 

Each node in the network creates a new message with probability $\mu$ at every time step in the simulation. The node creating the message is designated as the source node. The target node of the message (i.e. the node the message is intended for) is randomly selected from the set of nodes in the network. The message creation rate, $\mu$ , can be used to define the load of the network, where low values of $\mu$ correspond to low information flow scenarios, while high values of $\mu$ correspond to high information flow scenarios. 

Once created, messages are forwarded along the shortest path in the network to their target node (see Fig. 9). Messages are passed from one node to a neighboring node in a single time step. Each node is assumed to have complete knowledge of the current network topology, allowing nodes to determine the shortest path from themselves to another node in the network. Nodes are assumed to have unlimited queuing capacity, with links assumed to have unlimited bandwidth; i.e. message queuing and network congestion are not considered. 

To fully define the systems of interest, we need to determine initial network topologies. We use scale-free networks due to their appearance in many real complex systems [49,50,55,56], created by the Barabási-Albert (BA) preferential attachment model [57]. The BA model begins with a small number, $m _ { 0 } ,$ , of initially connected nodes (we define these nodes to be fully connected). The network grows by adding one node to the network at each step, where each added node 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/a21d46e1bb8ee2a044c81408087d116dc185999c0487815dbcdc399f8d248442.jpg)



Fig. 9. Example of message passing in a scale-free network. The source node, target node, and shortest path are highlighted red. This network was created using the BA model, with $N = 1 0 0$ nodes, $m _ { 0 } = 5$ , and $m = 2$ . Nodes sizes are scaled by degree, showing several highly connected network hubs that characterize scale-free networks. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.).


links with m existing nodes in the network. Preferential attachment refers to the definition of how nodes choose their neighbors. The probability, $P ( k _ { j } )$ , that a node with degree $k _ { j }$ is linked with is proportional to the degree of that node, such that 

$$
P \left(k _ {j}\right) = \frac {k _ {j}}{\sum_ {i} k _ {i}}. \tag {19}
$$

We define potential network disruptions as node removal events, where nodes are removed uniformly at random (e.g. random node failures) or in a targeted manner (e.g. intentional network attacks). Targeted node removal is based on node degree, where the most connected nodes (i.e. the nodes with the most links) are removed each time. Node degrees are recalculated following any changes to the network topology. Repeated disruptions within a simulation run are all from the same threat type. 

Recovery actions considered in this study are based on network adaptation, where nodes affected by a disruption rewire any links disconnected by the disruption (see Fig. 10). Two adaptation strategies are considered: random rewiring and preferential attachment. With random rewiring, nodes randomly decide who to rewire disconnected links to. With preferential attachment, nodes give preference to highly connected nodes using Eq. (19). These simple disruption and recovery actions provide a stark contrast in random versus directed actions, enabling a study of differences in network behaviors between these two extremes. These high-level insights can be used in a spiral design process to focus higher-fidelity studies on certain areas of the network design space. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/e60a1b185d805befbf87dd22d0d0c4d6242a4cfb8fdc8cc66e10ce1d4e52264c.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/07208670b4f4d071e0fbeeb3b27645e1e7d04dc9015f1528006bd65eb233ecff.jpg)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/0ad2904579b1880a2fc6cdb78320a1f2fb4f845af5460a8a713434112579784c.jpg)



(c）


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/b98b6e18fce45d4146feb2432e796294c137d9a4cfbe07df6679f121debd5302.jpg)



(d)



Fig. 10. Network adaptation based on preferential attachment, following targeted attacks using node degree (node sizes scaled by degree). The initial network is shown in (a) with the first targeted node highlighted. The adapted network is shown in (b) with rewiring nodes and their rewired links highlighted. The second targeted node is shown in (c), with the second adapted network shown in (d).



Table 1 Scenario descriptions.


<table><tr><td></td><td>Disruption type</td><td>Recovery action</td></tr><tr><td>Scenario 1</td><td>Random</td><td>None</td></tr><tr><td>Scenario 2</td><td>Random</td><td>Random</td></tr><tr><td>Scenario 3</td><td>Random</td><td>Preferential</td></tr><tr><td>Scenario 4</td><td>Degree-based</td><td>None</td></tr><tr><td>Scenario 5</td><td>Degree-based</td><td>Random</td></tr><tr><td>Scenario 6</td><td>Degree-based</td><td>Preferential</td></tr></table>

System performance, $y ( t )$ , is measured as the total number of messages received in a network at each time step in a simulation. This data is then used to calculate system resilience with Eqs. (1) and (14). Calculating resilience from simulated network performance aims to extend existing characterizations of network resilience based on topological properties. The proposed resilience framework, as applied to this problem of information exchange in networked systems, is summarized in the following steps (resilience calculations are discussed in the remainder of this section): 

1. System Description: information exchange in scale-free networks. 

2. Potential Disruptions Analysis: random and degree-based node removals. 

3. Recovery Action Analysis: none, random rewiring, or preferential attachment-based adaptation. 

4. System Performance Measurement: total number of messages received at a given time t. 

Six scenarios are considered in this analysis, described in Table 1. Initial network topologies are all scale-free, with networks being subjected to node removals every 200 time steps in the simulation. For scenarios with adaptation, rewiring occurs 100 time steps after node removals. Due to the stochastic nature of the simulation, 100 repetitions are run for each scenario. Stochasticity in the simulation comes from randomness in message generation, the BA algorithm, node removals, and link rewiring. Statistical analysis of the output simulation data is used to characterize the resulting uncertainty in system performance. 

Fig. 11 shows mean performance data for each scenario considered (i.e. performance data averaged over all 100 replications for each scenario). Disruption type shows a large impact on the ability of a network to maintain its performance over time, with degree-based removals causing much larger degradations in performance than random removals. This trend agrees with complex network studies of 

scale-free network robustness utilizing a statistical physics-based approach [58–61], but differs slightly from those implementing a constrained optimization approach [53]. Our result likely differs from the latter due to our abstraction of domain-specific network properties (e.g. routing and constrained topology evolution). Results also show that adding random or preferential adaptation enables networks to recover all lost performance due to node removals. 

Though performance plots enable general comparisons of system resilience, analysis of $R$ and $R _ { t o t a l }$ are used for more quantitative analysis. Fig. 12 shows the mean resilience, R, for each epoch in simulated performance data. R results match general trends seen in performance data, in that degree-based removals have a larger impact on network resilience than random ones, with adaptation enabling networks to achieve resilience values near two (i.e. nearly achieving normal operating scenario $R$ values). 

Fig. 13 shows a box plot of total resilience, $R _ { t o t a l } ,$ calculated for each replication of every considered scenario. Being able to represent multi-disruption system resilience with a single value, $R _ { t o t a l } ,$ enables direct comparisons between systems of interest, as well as statistical analysis that is difficult to replicate with performance plots or time or epoch-based resilience metrics (e.g. R or the metric proposed by [37]). These results show that networks without any adaptation have large variation in $R _ { t o t a l }$ to random node removals. In comparison, all other scenarios show much less variance in $R _ { t o t a l } ,$ suggesting more predictability in system performance. The benefit of building adaptation into networks facing degree-based attacks is also clearly shown, where there is a large gap in the resilience systems are able to achieve with and without adaptation. For these threats, random adaptation shows slightly higher median and quartile $R _ { t o t a l }$ values than preferential adaptation, due to preferential adaptation creating network hubs that can be targeted by subsequent removals. This difference in adaptation methods is difficult to see in mean performance and $R$ plots. The benefit of adaptation is significantly less pronounced for scenarios with random threats; in fact, these scenarios show a notable overlap in the range of $R _ { t o t a l }$ values for systems with and without adaptation. Roughly $2 5 \%$ of systems with no adaptation had similar $R _ { t o t a l }$ to those with adaptation (when facing random threats). Random and preferential adaptation provide similar levels of resilience for these threats. 

# 6. Conclusions

This paper presents a framework for quantitative assessments of system resilience. The proposed framework contributes to the resilience engineering literature by accounting for multiple disruption 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/f588828f87e7392296923c0bcee95248df07317cb2d967229236f0f37403200d.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/59dd4de44e5bae3b50405dbedad903d1bb683ecb33174abe9dff49933970a193.jpg)



Fig. 11. Mean performance data for networks subjected to (a) random (R) and (b) degree-based (D) attacks. Two adaptation strategies are considered, random (Rand.) and preferential attachment (Pref.), in addition to no recovery action (None). Initial network topologies are created using the BA model, with $N = 1 0 0$ nodes, $m _ { 0 } = 5 ,$ , and $m = 2$ . Vertical dashed lines indicate node removal events, where five nodes are simultaneously removed at each event. Adaptation occurs 100 time steps after removal events.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/d33444283d5fcca95d315580a937b6dfb0d67d60b71c780f4f9ad60b58ef6d8a.jpg)



(a)


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/cad5840c9d84947aa44c7008faaa795abedc13883e4a39cd7a1c005b20db72e0.jpg)



(b)



Fig. 12. Mean epoch-based resilience results calculated from performance data. Resilience is calculated for each epoch in a scenario, such that $R$ at time $t = 1 0 0$ corresponds to the resilience of a network in the epoch specified by $1 0 0 \leq t < 2 0 0$ .


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/e99a2099-e0ce-481d-b75d-a6af394d7f84/024ebf3c66a3c7242f1a3cc906f64c2cd147a6f2ccb7f1c119e3791154486c7e.jpg)



Recovery Action



Fig. 13. Total resilience, $R _ { t o t a l } $ calculated for all 100 replications of the considered scenarios. Red lines indicate median data values, blue boxes indicate $2 5 \%$ and $7 5 \%$ quantiles, box end points (i.e. whiskers) indicate minimum and maximum values not considered outliers, and red “plus” signs indicate outliers. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.).


events, explicitly considering volatility in performance data, and providing a method for experimental comparisons of potential resilience metrics. Resilience assessments begin with a description of systems of interest and their desired capabilities, as well as the identification of potential disruptions and recovery actions. Measurements of system performance over time are then used to calculate a set of resilience factors culminating in a resilience metric, R, and a total resilience metric, $R _ { t o t a l } .$ . An S-G filter and the MSER method are used to simplify and support metric calculations, and an exponential weighting function used to collapse resilience calculations to a single value for scenarios with multiple disruption events. 

This framework is particularly useful within large simulation design studies. For example, the information exchange network application problem compares system designs with two potential recovery actions, as well as those with no recovery action, subjected to two potential threats. Resilience measured by $R$ shows general trends in system performance, based on the ability of a system to maintain and recover desired capabilities. Statistical analysis of $R _ { t o t a l }$ enables direct comparisons of system designs, with consideration of stochasticity in simulated performance and system adaptation over time. Results show that benefits of network adaptation with regards to system resilience strongly depend on the type of threat faced. On average, adding 

adaptation improves system resilience; however, the resilience gained by incorporating adaptation is reduced for random node removals compared to targeted ones. These insights can be used within an overall design process to guide future investment decisions and research agendas. For example, combined with cost-benefit analysis, a network designer can use these assessments to identify if investing in link rewiring is a worthwhile task for their system, given knowledge of specific threat likelihoods. For scenarios where targeted disruptions are anticipated, a designer can design for whichever link rewiring scheme is cheapest, since the benefits of random and preferential rewiring are similar (with respect to resilience and the abstract model used). 

Limitations of this framework include the lack of cost considerations, threat probabilities and uncertainty propagation, and detailed consideration of adaptive capacity constraints and brittleness. Future extensions will aim to address these limitations, for example through integration with risk-based methods (e.g. see [62]) and critical slowing down analysis. Future efforts should also quantitatively compare the proposed metrics with other resilience metrics from the literature, as well as metrics for other system attributes (e.g. robustness, survivability, and risk). These assessments should be performed within the context of the life-cycle of a system, which may help to provide designers with an understanding of the potential impact of such assessments on system life-cycle performance and cost. 

# References



[1] Holling CS. Resilience and stability of ecological systems. Annu Rev Ecol Syst 1973;4:1–23. 





[2] Neches R, Madni AM. Towards affordably adaptable and effective systems. Syst Eng 2013;16(2):224–34. http://dx.doi.org/10.1002/sys. 





[3] National Infrastructure Advisory Council (NIAC). Critical infrastructure resilience final report and recommendations, Tech. Rep., NIAC (2009). 





[4] Simmie J, Martin R. The economic resilience of regions towards an evolutionary approach. Camb J Reg Econ Soc 2010;3(1):27–43. http://dx.doi.org/10.1093/ cjres/rsp029. 





[5] Uday P, Marais K. Exploiting stand-in redundancy to improve resilience in a system-of-systems (SoS). Procedia Comput Sci 2013;16:532–41. http://dx.doi.org/ 10.1016/j.procs.2013.01.056. 





[6] Francis R, Bekera B. A metric and frameworks for resilience analysis of engineered and infrastructure systems. Reliab Eng Syst Saf 2014;121:90–103. http:// dx.doi.org/10.1016/j.ress.2013.07.004. 





[7] Woods D. Engineering organizational resilience to enhance safety: a progress report on the emerging field of resilience engineering. In: Proceedings Hum. Factors Ergon. Soc. Annu. Meet., Vol. 50; 2006. p. 2237–41. http://dx.doi.org/10.1177/ 154193120605001910. 





[8] Turnquist M, Vugrin E. Design for resilience in infrastructure distribution networks. Environ Syst Decis 2013;33(1):104–20. http://dx.doi.org/10.1007/s10669- 012-9428-z. 





[9] Alderson DL, Brown GG, Carlyle WM. Operational models of infrastructure resilience. Risk Anal 2015;35(4):562–86. http://dx.doi.org/10.1111/risa.12333. 





[10] Sterbenz JPG, Çetinkaya EK, Hameed Ma, Jabbar A, Qian S, Rohrer JP. Evaluation of network resilience, survivability, and disruption tolerance analysis, topology 





generation, simulation, and experimentation. Telecommun Syst 2013;52(2):705–36. http://dx.doi.org/10.1007/s11235-011-9573-6. 





[11] Ip WH, Wang D. Resilience and friability of transportation networks evaluation, analysis and optimization. IEEE Syst J 2011;5(2):189–98. http://dx.doi.org/ 10.1109/JSYST.2010.2096670. 





[12] Zhao K, Kumar A, Harrison TP, Yen J. Analyzing the resilience of complex supply network topologies against random and targeted disruptions. IEEE Syst J 2011;5(1):28–39. 





[13] Mendonca D, Wallace WA. Factors underlying organizational resilience: the case of electric power restoration in New York City after 11 September 2001. Reliab Eng Syst Saf 2015;141:83–91. http://dx.doi.org/10.1016/j.ress.2015.03.017. 





[14] Righi AW, Saurin TA, Wachs P. A systematic literature review of resilience engineering research areas and a research agenda proposal. Reliab Eng Syst Saf 2015;141:142–52. http://dx.doi.org/10.1016/j.ress.2015.03.007. 





[15] Uday P, Marais K. Designing resilient systems-of-systems: a survey of metrics, methods, and challenges. Syst Eng 2015;18(5):491–510. http://dx.doi.org/ 10.1002/sys. 





[16] Woods DD. Four concepts for resilience and the implications for the future of resilience engineering. Reliab Eng Syst Saf 2015;141:5–9. http://dx.doi.org/ 10.1016/j.ress.2015.03.018. 





[17] Bhamra R, Dani S, Burnard K. Resilience: the concept, a literature review and future directions. Int J Prod Res 2011;49(18):5375–93. http://dx.doi.org/ 10.1080/00207543.2011.563826. 





[18] D. of Defense, Fact sheet: Resilience of Space Capabilities, Tech. Rep. 





[19] Hollnagel E, Woods DD, Leveson N. Resilience engineering: concepts and precepts. Aldershot, UK: Ashgate; 2006. 





[20] Madni AM, Jackson S. Towards a conceptual framework for resilience engineering. IEEE Syst J 2009;3(2):181–91. http://dx.doi.org/10.1109/JSYST.2009.2017397. 





[21] Jackson S, Ferris TLJ. Resilience principles for engineered systems. Syst Eng 2013;16(2):152–64. http://dx.doi.org/10.1002/sys.21228. 





[22] Vugrin ED, Warren DE, Ehlen MA, Camphouse RC. A framework for assessing the resilience of infrastructure and economic systems. In: Gopalakrishnan K, Peeta S, editors. Sustainable and resilient critical infrastructure systems. Berlin Heidelberg: Springer; 2010. p. 77–116. http://dx.doi.org/10.1007/978-3-642-11405-2_3. 





[23] T. N. A. of sciences, Disaster resilience: a national imperative, The National Academies Press, Washington, DC, 2012. http://dx.doi.org/10.17226/13457. 





[24] Linkov I, Eisenberg DA, Bates ME, Chang D, Convertino M, Allen JH, et al. Measurable resilience for actionable policy. Environ Sci Technol 2013;47:10108–10. 





[25] Fox-Lent C, Bates ME, Linkov I. A matrix approach to community resilience assessment: an illustrative case at rockaway peninsula. Environ Syst Decis 2015;35(2):209–18. http://dx.doi.org/10.1007/s10669-015-9555-4. 





[26] Haimes YY. On the definition of resilience in systems. Risk Anal 2009;29(4):498–501. http://dx.doi.org/10.1111/j.1539-6924.2009.01216.x. 





[27] Alderson DL, Doyle JC. Contrasting views of complexity and their implications for network-centric infrastructures. IEEE Trans Syst Man, Cyber – Part A Syst Hum 2010;40(4):839–52. http://dx.doi.org/10.1109/TSMCA.2010.2048027. 





[28] Patterson MD, Wears RL. Resilience and precarious success. Reliab Eng Syst Saf 2015;141:45–53. http://dx.doi.org/10.1016/j.ress.2015.03.014. 





[29] Woods DD, Branlat M. Basic patterns in how adaptive systems fail. In: H. E, P. J, W. DD, W. J (Eds.), Resilience engineering in practice: a guidebook, Ashgate, Farnham, UK, 2011. p. 127–44. 





[30] Attoh-Okine NO, Cooper AT, Mensah Sa. Formulation of resilience index of urban infrastructure using belief functions. IEEE Syst J 2009;3(2):147–53. http:// dx.doi.org/10.1109/JSYST.2009.2019148. 





[31] Omer M, Nilchiani R, Mostashari A. Measuring the resilience of the trans-oceanic telecommunication cable system. IEEE Syst J 2009;3(3):295–303. http:// dx.doi.org/10.1109/JSYST.2009.2022570. 





[32] Reed DA, Kapur KC, Christie RD. Methodology for assessing the resilience of networked infrastructure. IEEE Syst J 2009;3(2):174–80. http://dx.doi.org/ 10.1109/JSYST.2009.2017396. 





[33] Whitson JC, Ramirez-Marquez JE. Resiliency as a component importance measure in network reliability. Reliab Eng Syst Saf 2009;94(10):1685–93. http:// dx.doi.org/10.1016/j.ress.2009.05.001. 





[34] Greco R, Di Nardo A, Santonastaso G. Resilience and entropy as indices of robustness of water distribution networks. J Hydroinform. 2012;14(3):761–71. http://dx.doi.org/10.2166/hydro.2012.037. 





[35] Filippini R, Silva A. A modeling framework for the resilience analysis of networked 





systems-of-systems based on functional dependencies. Reliab Eng Syst Saf 2014;125:82–91. http://dx.doi.org/10.1016/j.ress.2013.09.010. 





[36] Uday P. System importance measures: a new approach to resilient systems-ofsystems. Ph.d., Purdue University; 2015. 





[37] Henry D, Emmanuel Ramirez-Marquez J. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99:114–22. http://dx.doi.org/10.1016/j.ress.2011.09.002. 





[38] Taleb NN, Douady R. Mathematical definition, mapping, and detection of (anti) fragility. Quant Financ 2013;13(11):1677–89. http://dx.doi.org/10.1080/ 14697688.2013.800219. 





[39] Schafer RW. What is a savitzky-golay filter?. IEEE Signal Process Mag 2011;28(4):111–7. http://dx.doi.org/10.1109/MSP.2011.941097. 





[40] Jönsson P, Eklundh L. TIMESAT - a program for analyzing time-series of satellite sensor data. Comput Geosci 2004;30(8):833–45. http://dx.doi.org/10.1016/j.cageo.2004.05.006. 





[41] Orfanidis SJ. Introduction to signal processing. Prentice Hall, Inc.; 2009, ISBN: 0- 13-209172-0 http://www.ece.rutgers.edu/~orfanidi/intro2sp/. 





[42] O'Rourke TD. Critical infrastructure, interdependencies, and resilience. Bridg Link Eng Soc 2007;37(1):22–9. http://dx.doi.org/10.1109/TIGA.1967.4180765. 





[43] White KP. An effective truncation heuristic for bias reduction in simulation output. Simulation 1997;69(6):323–34. http://dx.doi.org/10.1177/ 003754979706900601. 





[44] White KP, Spratt SC. A comparison of five steady-state truncation heuristics for simulation. In: Proceedings 2000 winter simul. conference, 2000 p. 755–60. 





[45] White KP, Robinson S. The problem of the initial transient (again), or why MSER works. J Simul 2010;4:268–72. http://dx.doi.org/10.1057/jos.2010.19. 





[46] Law AM. Simulation modeling and analysis, 5th ed.. New York, NY, USA: McGraw-Hill Education; 2015. 





[47] Scheffer M, Carpenter SR, Lenton TM, Bascompte J, Brock W, Dakos V, et al. Anticipating critical transitions. Sci (80-. ) 2012;338(6105):344–8. http:// dx.doi.org/10.1126/science.1225244. 





[48] Dai L, Korolev KS, Gore J. Slower recovery in space before collapse of connected populations. Nature 2013;496(7445):355–8. http://dx.doi.org/10.1038/nature12071. 





[49] Faloutsos M, Faloutsos P, Faloutsos C. On power-law relationships of the internet topology. In: ACM SIGCOMM comput. Commun. Rev., ACM, 1999. p. 251–62. 





[50] Albert R, Jeong H, Barabasi A-L. Diameter of the world-wide web. Nature 1999;401:130–1. 





[51] Dodds PS, Watts DJ, Sabel CF. Information exchange and the robustness of organizational networks. Proc Natl Acad Sci U S A 2003;100(21):12516–21. http:// dx.doi.org/10.1073/pnas.1534702100. 





[52] Haythornthwaite C. Social network analysis: an approach and technique for the study of information exchange. Libr Inf Sci Res 1996;18:323–42. http:// dx.doi.org/10.1016/S0740-8188(96)90003-1. 





[53] Doyle JC, Alderson DL, Li L, Low S, Roughan M, Shalunov S, et al. The “robust yet fragile” nature of the Internet. Proc Natl Acad Sci U S A 2005;102(41):14497–502. http://dx.doi.org/10.1073/pnas.0501426102. 





[54] Alderson DL. Catching the network science bug: insight and opportunity for the operations researcher. Oper Res 2008;56(5):1047–65. http://dx.doi.org/10.1287/ opre.1080.0606. 





[55] Albert R, Barabási A-L. Statistical mechanics of complex networks. Rev Mod Phys 2002;74(1):47–97. http://dx.doi.org/10.1103/RevModPhys.74.47. 





[56] Newman MEJ. The structure and function of complex networks. Soc Ind Appl Math 2003;45(2):167–256. http://dx.doi.org/10.1137/S003614450342480. 





[57] Barabási A-l, Albert R. Emergence of scaling in random networks. Sci (80-.) 1999;286(5439):509–12. http://dx.doi.org/10.1126/science.286.5439.509. 





[58] Albert R, Jeong H, Barabasi A-L. Error and attack tolerance of complex networks. Nature 2000;406(6794):378–82. http://dx.doi.org/10.1038/35019019. 





[59] Cohen R, Erez K, Ben-Avraham D, Havlin S. Resilience of the internet to random breakdowns. Phys Rev Lett 2000;85(21):4626–8. 





[60] Cohen R, Erez K, Ben-Avraham D, Havlin S. Breakdown of the internet under intentional attack. Phys Rev Lett 2001;86(16):3682–5. http://dx.doi.org/10.1103/ PhysRevLett.86.3682. 





[61] Holme P, Kim BJ, Yoon CN, Han SK. Attack vulnerability of complex networks. Phys Rev E Stat Nonlin Soft Matter Phys 2002;65(5 Pt 2):056109. 





[62] Filippini R, Zio E. Integrated resilience and risk analysis framework for critical infrastructures. In: ESREL 2013, Amsterdam; 2013. 

