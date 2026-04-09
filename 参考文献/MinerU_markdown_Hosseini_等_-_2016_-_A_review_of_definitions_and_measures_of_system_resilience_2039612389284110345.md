# A review of definitions and measures of system resilience

Seyedmohsen Hosseini a , Kash Barker a,n , Jose E. Ramirez-Marquez b,c 

a School of Industrial and Systems Engineering, University of Oklahoma, United States 

b School of Systems and Enterprises, Stevens Institute of Technology, United States 

c Tec de Monterrey, School of Science and Engineering, Zapopan Guadalajara, Mexico 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/be9d1ce67de8ebe0a009112f2eaa2c075f0b4710ca40a9a7390a1f159fc92a5e.jpg)



CrossMark


# a r t i c l e i n f o

Article history: 

Received 11 January 2015 

Received in revised form 

7 July 2015 

Accepted 7 August 2015 

Available online 28 August 2015 

Keywords: 

Resilience 

Engineering systems 

# a b s t r a c t

Modeling and evaluating the resilience of systems, potentially complex and large-scale in nature, has recently raised significant interest among both practitioners and researchers. This recent interest has resulted in several definitions of the concept of resilience and several approaches to measuring this concept, across several application domains. As such, this paper presents a review of recent research articles related to defining and quantifying resilience in various disciplines, with a focus on engineering systems. We provide a classification scheme to the approaches in the literature, focusing on qualitative and quantitative approaches and their subcategories. Addressed in this review are: an extensive coverage of the literature, an exploration of current gaps and challenges, and several directions for future research. 

$\circledcirc$ 2015 Elsevier Ltd. All rights reserved. 

# 1. Introduction

Historically, the primary questions asked during a risk assessment study are: (i) what can go wrong?, (ii) what is the likelihood of such a disruptive scenario?, and (iii) what are the consequences of such a scenario? [1]. Risk management strategies have traditionally focused on reducing the likelihood of disruptive events and reducing the potential consequences of the event, as well as some synthesis of both. As such, risk management strategies often emphasized mitigation options in the form of prevention and protection: designing systems to avoid or absorb undesired events from occurring. The main objective of protection strategy is to detect the adversary early and defer the adversary long enough for an appropriate respond. While a protection strategy is critical to prevent undesired events or consequences, however recent events suggested that not all undesired events can be prevent. Hurricane Sandy, which devastated NY/NJ in 2012, is among the more recent examples of a disruptive event that adversely impacted multiple networked systems (e.g., months after the storm, power had not been restored to all communities in the NY/NJ area [2], one million cubic yards of debris impeded transportation networks [3]). Plenty of other disruptions have highlighted the resilience, or lack thereof, of networked systems: the August 2003 US blackout that caused transportation and economic network disruptions [4], Hurricane Isabel devastated the transportation system of the 

Hampton Roads, VA, region in 2003 and overwhelmed emergency response [5], the 2011 9.0 magnitude earthquake and tsunami that struck Japan, causing over 15,000 confirmed deaths and disrupting global supply chain networks [6]. It is because of these recent large-scale events that the Department of Homeland Security, among others, has placed emphasis on resilience through preparedness, response, and recovery [7,8]. 

The term resilience has increasingly been seen in the research literature [9] and popular science literature [10] due to its role in reducing the risks associated with the inevitable disruption of systems. This paper presents a comprehensive review of resilience in various disciplines, published from 2000 to April 2015. In this paper, we primarily focus on the quantitative perspective of modeling resilience, distinguishing our work from existing excellent review papers [11,12]. 

The word resilience has been originally originated from the Latin word “resiliere,” which means to “bounce back.” The common use of resilience word implies the ability of an entity or system to return to normal condition after the occurrence of an event that disrupts its state. Such a broad definition applies to such diverse fields as ecology, materials science, psychology, economics, and engineering. A graphical depiction of the initial impact and subsequent recovery of a six recent U.S. recessions is shown in Fig. 1 [13]. For example, figure shows that for the 1980s recession, there was a disruption that affected a change roughly equal to $- 1 . 2 \%$ and that the recovery lasted roughly six months. 

Several definitions of resilience have been offered. Many are similar, though many overlap with a number of already existing concepts such as robustness, fault-tolerance, flexibility, survivability, and agility, among others. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/a5d966921afb76af47d2ba0a0b6d4a1bd90cea443610e9a1c8dfc935e5b2fb93.jpg)



Fig. 1. Payroll change in recent recessions [13].


Some general definitions of resilience that span multiple disciplines have been offered. For example, Allenby and Fink [53] defined resilience as the “capability of a system to maintain its functions and structure in the face of internal and external change and to degrade gracefully when it must.” Pregenzer [54] defined resilience as the “measure of a system's ability to absorb continuous and unpredictable change and still maintain its vital functions.” Haimes [55] defined the resilience as the “ability of system to withstand a major disruption within acceptable degradation parameters and to recover with a suitable time and reasonable costs and risks.” Disaster resilience is characterized by Infrastructure Security Partnership [56] as the capability to prevent or protect against significant multi-hazard threats and incidents, including terrorist attacks, and to recover and reconstitute critical services with minimum devastation to public safety and health. Vugrin et al. [57] defined system resilience as: “Given the occurrence of a particular disruptive event (or set of events), the resilience of a system to that event (or events) is that system's ability to reduce efficiently both the magnitude and duration of deviation from targeted system performance levels.” Two elements of this definition are noted: system impact, the negative impact that a disruption imposes to a system and measured by the difference between targeted and disrupted performance level of system, and total recovery efforts, the amount of resources expended to recover the disrupted system. 

The concept of resilience has also been approached from particular disciplinary perspectives and across application domains, including psychology, ecology, and enterprises, among others. A variety of definitions for the notion of resilience have been proposed. We identify four domains of resilience: organizational, social, economic, engineering. Note that this classification may vary depending on researcher's perspective. We provide a variety of definitions of resilience according to the four aforementioned groups. 

# 1.1. Organizational domain

The concept of organizational resilience has emerged to address the need for enterprises to respond to a rapidly changing business environments. The resilience of an organization is defined by Sheffi [19] as the inherent ability to keep or recover a steady state, thereby allowing it to continue normal operations after a disruptive event or in the presence of continuous stress. Vogus and Sutcliffe [20] defined organizational resilience as “the ability of an organization to absorb strain and improve functioning 

despite the presence of adversity.” Sheffi [21] defined resilience for companies as “the company's ability to, and speed at which they can, return to their normal performance level (e.g., inventory, capacity, service rate) following by disruptive event.” McDonald [22] defined resilience in the context of organizations as “the properties of being able to adapt to the requirements of the environment and being able to manage the environments variability.” Patterson et al. [23] highlighted that collaborative crosschecking can greatly enhance the resilience of organizations. Collaborative cross-checking is an enhanced resilience strategy in which at least two groups or individuals with different viewpoints investigate the others' activations to evaluate accuracy or validity. By implementing collaborative cross-checking, erroneous actions can be detected quickly enough to mitigate adverse consequences. More definitions of resilience in the context of organizational, enterprises and can be found in [24–27]. 

# 1.2. Social domain

The social domain looks at the resilience capacities of individuals, groups, community, and environment. Adger [28] defined social resilience as “ability of groups or communities to cope with external stresses and disturbances as a result of social, political, and environmental change.” The Community and Regional Resilience Institute [29] defined the resilience as the capability to predict risk, restrict adverse consequences, and return rapidly through survival, adaptability, and growth in the face of turbulent changes. Keck and Sakdapolrak [30] defined social resilience as comprised of three dimensions: coping capacities, adaptive capacities, and transformative capacities. The term of community resilience is described by Cohen et al. [31] as ability of community to function properly during disruptions or crises. Pfefferbaum et al. [32] defined community resilience as “the ability of community members to take meaningful, deliberate, collective action to remedy the effect of a problem, including the ability to interpret the environment, intervene, and move on”. The concept of resilience has been well studied in subdomains of the social domain such as ecology [33–35], psychology [36–38], sociology [39–42]. 

# 1.3. Economic domain

Rose and Liao [43] described economic resilience as the “inherent ability and adaptive response that enables firms and regions to avoid maximum potential losses.” Static economic resilience is referred by Rose [44] as the capability of an entity or system to continue its functionality like producing when faces with a severe shock, while dynamic economic is defined as the speed at which a system recovers from a severe shock to achieve a steady state. A more specific definition of economic resilience is presented by Martin [45] as “the capacity to reconfigure, that is adapt, its structure (firms, industries, technologies, institutions) so as to maintain an acceptable growth path in output, employment and wealth over time.” 

# 1.4. Engineering domain

The concept of resilience in the engineering domain is relatively new in comparison to other domains. The engineering domain includes technical systems designed by engineers that interact with humans and technology, such as electric power networks. Note that Youn et al. [14] defined engineering resilience as the sum of the passive survival rate (reliability) and proactive survival rate (restoration) of a system. Another definition of engineering resilience is presented by Hollnagel et al. [15] as the intrinsic ability of a system to adjust its functionality in the presence of a disturbance and unpredicted changes. Hollnagel and Prologue [16] pointed out that, for resilience engineering, 

understanding the normal functioning of a technical system is important as well as understanding how it fails. The American Society of Mechanical Engineers (ASME) [17] defined resilience as the ability of a system to sustain external and internal disruptions without discontinuity of performing the system's function or, if the function is disconnected, to fully recover the function rapidly. Dinh et al. [18] identified six factors that enhance the resilience engineering of industrial processes, including minimization of failure, limitation of effects, administrative controls/procedures, flexibility, controllability, and early detection. 

Infrastructure systems such as water distribution systems, nuclear plants, transportation systems, and locks and dams, among others, can be considered as subdomain of the engineering domain as their construction and restoration require engineering knowledge. National Infrastructure Advisory Council (NIAC) [52] defined the resilience of infrastructure systems as their ability to predict, absorb, adapt, and/or quickly recover from a disruptive event such as natural disasters. Infrastructures are also considered as subdomain of social domain in which the lack of their resilience can lead to adverse impacts on communities. According to Percoco [46], infrastructure systems can greatly improve the economic efficiency of a country. Due to the crucial role of infrastructures on society and economy, research work has recently focused on infrastructure resilience [47–50]. Ouyang and Wang [51] assessed the resilience of interdependent electric power and natural gas infrastructure systems under multiple hazards, noting how interdependent network performance could be measured in physical engineering terms or in terms of societal impact. 

# 1.5. Analysis of resilience definitions

The review of resilience definitions indicates that there is no unique insight about how to define the resilience, however several similarities can be observed across these resilience definitions. The main highlights of resilience definitions reviewed above are summarized as follows: 

Some definitions does not specify mechanisms to achieve resilience; however many of them focus on the capability of system to “absorb” and “adapt” to disruptive events, and “recovery” is considered as the critical part of resilience. 

 For engineered systems, such as nuclear power systems, reliability is often considered to be an important feature to measure an ability to stave off disruption. 

 Some definitions, such as Sheffi [19] and ASME [17], emphasize that returning to steady state performance level is needed for resilience, while other definitions do not impose that the system (e.g., infrastructure, enterprise, community) return to pre-disaster state. 

 The definition offered by Haimes [55] suggests a multidimensionality to the quantification of resilience, that particular states of a system are inherently more resilient than others. Further, Haimes stresses that the resilience of a system is threat-dependent. 

 Some definitions such as Allenby and Fink [53], Pregenzer [54], and Adger [28] defined resilience in terms of preparedness (pre-disaster) activities, while the role of recovery (post-disaster) activities are discarded. Definitions presented by organizations such as National Infrastructure Advisory Council (NIAC) [52] emphasized on the role of both preparedness and recovery activities to achieve resilience. 

The rest of paper includes the following structure. Section 2 our approach to reviewing the literature, and Section 3 provides a classification methodologies that are used to measure and assess the resilience in various disciplines. Section 4 summarizes 

important lessons obtained the literature, and Section 5 discusses the existing gaps and restrictions on assessing resilience. Finally, we provide concluding remarks in Section 6. 

# 2. Literature review methodology

In this section, we discuss framework we used to identify resiliencerelated literature. We also report, to the extent that we can, the distribution of literature by domains, years of publication, and journals. 

To present a breadth coverage of literature review of resilience study, we developed a framework of five steps: (i) online database searching and information clustering, (ii) citation and sample refinement, (iii) abstract review refinement, (iv) full-text review refinement, and (v) final sort. The Web of Science database, one of the most comprehensive multidisciplinary content search platforms for academic researchers [58], was searched to identify the papers. 

Using keywords to conduct the search, we selected those papers only relevant to modeling and measuring resilience in engineering fields, including engineering design, supply chain, infrastructure systems, and physical networks, and non-engineering fields, including enterprises/organizations, social networks, and economics. Journal papers were filtered with such keywords as resilience modeling, resilience quantification, resilience metrics, design resilience, disaster resilience, and engineering resilience. This approach was applied to the papers published from 2000 to April 2015, though we focus primarily on recent papers. 

# 2.1. Distribution by domain

CiteSpace [59], a well-known visualization tool, was used to visualize and analyze trends in the resilience literature. As shown in Fig. 2, the application of resilience in each discipline is represented by a cluster. The largest cluster is dedicated to the Psychology domain, followed by the Environmental, Social, & Ecology domain. The size of cluster of a discipline is relates to the number of papers published in that discipline. Meanwhile, a lesser proportion of resilience-related research exists in the engineering domain, suggesting that greater strides in defining and quantifying resilience have historically been made in nonengineering contexts. As such, opportunities exist in impacting resilience in the engineering domain (e.g., engineering design). 

# 2.2. Distribution by journal

Several different journals from different disciplines that published work related to resilience quantification approaches were included in this literature review. Table 1 lists 14 journals that contributed more than one article examined in this literature review. Among these, Reliability Engineering and Systems Safety is the most significant source of articles related to the resilience research, with Risk Analysis, International Journal of Production Research, and Procedia Computer Science following. The application of resilience in organizations, enterprises, business management, and logistics engineering are mostly published in International Journal of Production Research. Mathematical modeling perspectives on resilience have been mostly published in Computers and Operations Research, Transportation Research-Part B, and Transportation Research-Part E. 

# 2.3. Distribution by year of publication

The distribution of resilience-related archival journal articles by year from 2000 to April 2015 is represented in Fig. 3, using Web of Science [60]. The recent government and policy emphasis on resilience is also seen in academic research, according to the increasing appearance of resilience-related research. 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/2f04a0cb62de4d3ede8b093e567a2ef58f4c2167d01bd097f53e1b9158f4be91.jpg)



Fig. 2. A snapshot of clusters based on category, created by CiteSpace.



Table 1 Top journal sources of resilience research, as appropriate for this review.


<table><tr><td>No.</td><td>Journal title</td><td>No. of papers</td></tr><tr><td>1</td><td>Reliability Engineering and Systems Safety</td><td>10</td></tr><tr><td>2</td><td>Risk Analysis</td><td>5</td></tr><tr><td>3</td><td>International Journal of Production Research</td><td>4</td></tr><tr><td>4</td><td>Procedia Computer Science</td><td>3</td></tr><tr><td>5</td><td>Computers &amp; Operations Research</td><td>3</td></tr><tr><td>6</td><td>Safety Science</td><td>3</td></tr><tr><td>7</td><td>Transportation Research-Part B</td><td>2</td></tr><tr><td>8</td><td>Transportation Research-Part E</td><td>2</td></tr><tr><td>9</td><td>Bioscience</td><td>2</td></tr><tr><td>10</td><td>European Management Journal</td><td>2</td></tr><tr><td>11</td><td>Earthquake Spectra</td><td>2</td></tr><tr><td>12</td><td>Computers and Industrial Engineering</td><td>2</td></tr><tr><td>13</td><td>Process Safety Progress</td><td>2</td></tr><tr><td>14</td><td>Structural Safety</td><td>2</td></tr><tr><td>15</td><td>IEEE Systems Journal</td><td>2</td></tr><tr><td>16</td><td>International Journal of Critical Infrastructures</td><td>2</td></tr><tr><td>17</td><td>Journal of Loss Prevention in the Process Industries</td><td>2</td></tr><tr><td>18</td><td>Process Safety and Environmental Protection</td><td>2</td></tr><tr><td>19</td><td>Transportation Research-Part A</td><td>2</td></tr><tr><td>20</td><td>Expert Systems with Applications</td><td>2</td></tr><tr><td>21</td><td>Electrical Power and Energy Systems</td><td>2</td></tr><tr><td>22</td><td>Global Environmental Change</td><td>2</td></tr></table>

# 2.4. Classification of resilience assessment approaches

In general, the resilience evaluation procedure can be separated into two major categories: qualitative and quantitative. The qualitative category which includes methods that tend to assess the resilience of system without numerical descriptors, contains two sub-categories: 

(i) conceptual frameworks that offer best practices, and (ii) semiquantitative indices that offer expert assessments of different qualitative aspects of resilience. The quantitative methods include two subcategories: (i) general resilience approaches that offer domain-agnostic measures to quantify resilience across applications, and (ii) structuralbased modeling approaches that model domain-specific representations of the components of resilience. Note that the focus of this paper is on quantitative approaches, given our interest in engineering systems. The classification scheme of resilience assessment approaches is visually represented in Fig. 4. Readers interested in qualitative contributions to resilience research can refer to Refs. [61,62]. We summarize the classification of reviewed papers, along with their corresponding methods, in Table 2. 

# 3. Qualitative assessment approaches

This section highlights the qualitative resilience assessment approaches categorized as conceptual frameworks and semiquantitative indices. 

# 3.1. Conceptual frameworks

Work that we classified as conceptual frameworks constitute the majority of the qualitative approaches for assessing the system resilience. Alliance [63] proposed a generic framework for evaluating the resilience of social–ecological systems, composed of seven steps: (i) defining and understanding the system under study, (ii) identifying the appropriate scale to evaluate resilience, (iii) identifying the system drivers and external and internal 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/6b0de6682e9380faafd1e98468159b5b1a0bbcce9859e3baded5c74c17ea0c56.jpg)



Fig. 3. Distribution of papers by year of publication, as of April 2015.


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/c2488d15a51670c565887799c65f6cf98b3cbf5651a4cba494dc810aa8de19de.jpg)



Fig. 4. Classification scheme of resilience assessment methodologies.


disturbance, (iv) identifying the key players in the system, including people and governance, (v) developing conceptual models for identifying necessary recovery activities, (vi) implementing the results of step v to inform policymaker, and (vii) incorporating the findings of the previous step. Speranza et al. [64] developed a notional framework for analyzing resilience of livelihoods, or the “resources that people have and the strategies they adopt to make a living.” The framework provides a few attributes of three dimension of resilience: buffer capacity (the amount of change that a system can undergo), self-organization (the emergence of society through inherent social structure), and capacity for learning (an ability to adapt). In a homeland security context, Kahan et al. [65] proposed a broad conceptual framework for system resilience using eight guiding principles: (i) threat and hazard assessment, (ii) robustness, (iii) consequence mitigation, (iv) adaptability, (v) risk-informed planning, (vi) risk-informed investment, (vii) harmonization of purposes, and (viii) comprehensive of scope. Labaka et al. [66] proposed a holistic resilience framework that has been defined in close collaboration with general management. Their proposed framework consists of two resilience types: internal resilience and external resilience with resilience policies and resilience sub-policies. Several qualitative resilience studies have addressed critical infrastructure applications. Sterbenz et al. [67] presented a framework for resilience and survivability of communication networks and also a survey that includes the resilience disciplines. The results of their study indicate that six factors of defend, detect, diagnose, remediate, refine, and recover contribute to designing resilient networks that can be extended to other domains. This framework provides only a conceptual insight and does not quantify system resilience. In similar work, Vlacheas et al. [68] identified properties of resilience in the scope of telecommunication networks. They found that reliability, safety, 

availability, confidentiality, integrity, maintainability, and performance, along with their interactions, are most influential properties of networks resilience. Bruyelle et al. [69] suggested some technological solutions and behavior management to improve the resilience of mass transportation systems in the case of bomb attacks. Patterson et al. [70] proposed three key factors for achieving resilience in medication delivery: (i) advanced information visualization techniques, (ii) scenario-based design and evaluation of treatments, and (iii) teamwork during the elicitation of requirements. 

Vugrin et al. [71] introduced resilience as a function of absorptive capacity, adaptive capacity, and restorative capacity. Absorptive capacity is the degree to which a system is able to absorb shocks posed from a disruption, adaptive capacity is the degree to which a system is able to adapt itself temporarily to new disrupted conditions, and restorative capacities is the degree to which a system is able to restore itself if adaptive capacity is not effective. Note that adaptive and restorative capacities refer to recovery activities. This definition of resilience capacity accounts for both preparedness and recovery. A feature of their research that is distinct from others is about introducing resilience cost index (RCI), which is composed of two elements: loss costs posed by disruptive events, and recovery costs. Shirali et al. [72] distilled the main barriers for achieving resilience in a chemical plant, indicating that the main barriers to achieving resilience are: (i) a shortage of experience about resilience engineering, (ii) intangibility of resilience engineering level, (iii) choosing production over safety, (iv) lack of reporting system, (v) religious beliefs, and (vi) out-of-date procedures and manual, poor feedback loop, and economic problems. Shirali et al. [73] found seven indicators of resilience from safety culture perspective which includes: schedule delays, safety committees, meeting effectiveness, safety 


Table 2 Classification of the literature in modeling and planning for resilience.


<table><tr><td rowspan="3">Reference</td><td colspan="2">Qualitative</td><td colspan="5">Quantitative</td><td rowspan="3">Area studied in reference</td></tr><tr><td rowspan="2">Conceptual framework</td><td rowspan="2">Semi-quantitative</td><td colspan="2">Generic resilience metrics</td><td colspan="3">Structural-based modeling</td></tr><tr><td>Deterministic</td><td>Probabilistic</td><td>Optimization</td><td>Simulation</td><td>Fuzzy</td></tr><tr><td>Alliance [63]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Society-Ecology</td></tr><tr><td>Speranza et al. [64]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Society-Ecology</td></tr><tr><td>Kahan et al. [65]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>No specific area</td></tr><tr><td>Labaka et al. [66]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Nuclear plant</td></tr><tr><td>Sterbenz et al. [67]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Communication network</td></tr><tr><td>Vlacheas et al. [68]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Telecommunication network</td></tr><tr><td>Bruyelle et al. [69]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Community</td></tr><tr><td>Patterson et al. [70]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Healthcare</td></tr><tr><td>Vugrin et al. [71]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>No specific area</td></tr><tr><td>Shirali et al. [72]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Process industry</td></tr><tr><td>Shirali et al. [73]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Plant manufacturing</td></tr><tr><td>Ainuddin and Routary [74]</td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td></td><td>Community</td></tr><tr><td>Cutter et al. [81]</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>Community</td></tr><tr><td>Pettit et al. [82]</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>Supply chain</td></tr><tr><td>Shirali et al. [83]</td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td></td><td>Process industry</td></tr><tr><td>Bruneau et al. [84]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Community</td></tr><tr><td>Zobel [88]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Nospecificarea</td></tr><tr><td>Zobel and Khansa [89]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Nospecificarea</td></tr><tr><td>Rose [44]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Economic</td></tr><tr><td>Cox et al. [90]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Transportation</td></tr><tr><td>Henry and Ramirez-Marquez [91]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Transportation</td></tr><tr><td>Wang et al. [96]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Enterpriseandbusiness</td></tr><tr><td>Omer et al. [97]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Urbaninfrastructure</td></tr><tr><td>Chen and Miller-Hooks [98]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Transportation</td></tr><tr><td>Janic [99]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Airtransportnetwork</td></tr><tr><td>Orwin and Wardle [100]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Soilbiology</td></tr><tr><td>Enjalbert et al. [101]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Transportation</td></tr><tr><td>Ouedraogo et al. [102]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Human-machinesystems</td></tr><tr><td>Francis and Bekera [103]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Urbaninfrastructure</td></tr><tr><td>Cimellaro et al. [104]</td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td></td><td>Healthcare</td></tr><tr><td>Cheng and Shinozuka [105]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Community</td></tr><tr><td>Ouyang et al. [106]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Urbaninfrastructure</td></tr><tr><td>Youn et al. [14]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Engineering design</td></tr><tr><td>Ayyub [107]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Nospecificarea</td></tr><tr><td>Hashimoto et al. [108]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Waterresourcesystem</td></tr><tr><td>Franchin and Cavalieri [109]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Urbaninfrastructure</td></tr><tr><td>Pant et al. [93]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Transportation</td></tr><tr><td>Attoh-Okine et al. [110]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Urbaninfrastructure</td></tr><tr><td>Barker et al. [92]</td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td></td><td>Networks</td></tr><tr><td>Faturechi et al. [111]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Airportpavementnetwork</td></tr><tr><td>Faturechi and Miller-Hooks [112]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Transportation</td></tr><tr><td>Azadeh et al. [113]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Petrochemical plant</td></tr><tr><td>Jin et al. [114]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Metro networks</td></tr><tr><td>Baroud et al. [94]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Waterway network</td></tr><tr><td>Cardoso et al. [115]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Closed-loop supply chain</td></tr><tr><td>Khaled et al. [116]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Transportation</td></tr><tr><td>Vugrin et al. [117]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Transportation</td></tr><tr><td>Ash and Newth [118]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Computer networks</td></tr><tr><td>Alderson et al. [125]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Infrastructures</td></tr><tr><td>Sahebjamnia et al. [87]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Resource allocation</td></tr><tr><td>Li and Zhao [126]</td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td></td><td>Supply chain</td></tr><tr><td>Albores and Shaw [127]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Resource allocation</td></tr><tr><td>Carvalho et al. [128]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Transportation</td></tr><tr><td>Virginia et al. [129]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Supply chain</td></tr><tr><td>Jain and Bunya [130]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Water storage reservoir</td></tr><tr><td>Adjetey-Bahun et al. [131]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Transportation</td></tr><tr><td>Sterbenz et al. [132]</td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td></td><td>Internet networks</td></tr><tr><td>Aleksic et al. [133]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td>Organization</td></tr><tr><td>Azadeh et al. [134]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td>Petrochemical plant</td></tr><tr><td>Muller et al. [135]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td>Urban infrastructure</td></tr><tr><td>Tadic et al. [136]</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✓</td><td>Organization</td></tr></table>

education, worker's involvement, competence, safety training. The authors also found that resilience measurements is dependent on four managerial factors including centralization or decentralization control systems, management of change, risk management 

and accident analysis, management commitment to safety and resilience. 

Ainuddin and Routary [74] proposed a community resilience framework for an earthquake prone area in Baluchistan of 

Pakistan, constructed from a household survey that was conducted among 200 residences. The proposed framework comprises the following: (i) identifying hazard/disaster characteristics, (ii) determining individual/community vulnerability, (iii) risk reception and awareness preparedness, and (iv) finally improving social (educational, health coverage), economic (housing capital, employment), and physical (shelter, housing age) resources. 

Other conceptual framework for analyzing resilience, as well as some guiding principles and characteristics of resilient systems, can be found in [75–80]. 

# 3.2. Semi-quantitative Indices

The semi-quantitative index approach is usually constructed with a set of questions designed to assess different resiliencebased system characteristics (e.g., redundancy, resourcefulness) on a Likert (0–10) or percentage scale (0–100). Assessments of the characteristics from expert opinion are aggregated in some way to produce an index of resilience. For example, Cutter et al. [81] first identified 36 resilience variables of communities to natural disasters, including redundancy, resourcefulness, and robustness. Each variable was then scored between 0 and 100 according to the data observation from a government source. These 36 variables were grouped into five sub-indices, including economic, infrastructure, social, community capital, and institutional. The score for each subindex was calculated using an unweighted average of each variable, and the total score was calculated by taking unweighted average of all sub-index scores. Pettit et al. [82] distilled the two key drivers of resilience in an industrial supply chain: (i) level of the supply chain's vulnerability, and (ii) capability of the supply chain to withstand and recover from disruption. The authors measured vulnerability and capability of supply chains by providing a set of 152 questions divided into six sections of vulnerability and 15 sections of capability. The importance of each factor was weighted by policymakers, and finally the responses to the questions were calculated using the weighted sum approach. Shirali et al. [83] used a semi-quantitative approach to assess resilience engineering in a process industry, introducing six critical process industry resilience indicators: (i) top management, (ii) commitment, (iii) learning culture, (iv) awareness, (v) preparedness, and (vi) flexibility. Data related to these six indicators were collected from 11 units of a process industry using a survey, and the data were analyzed and scored using principal component analysis. 

# 4. Quantitative assessment approaches

This section describes several quantitative resilience assessment approaches that serve as the focus of this review. 

# 4.1. General measures

General resilience measures provide a quantitative means to assess resilience by measuring performance of system, regardless of the structure of system. These measures are comparable across different system contexts with similar underlying logic. As we have defined them, generic resilience metrics determine resilience by comparing the performance of system before and after disruption without concentrating on system-specific characteristics (though modeling performance may require understanding underlying system behavior). We broadly characterize these general measures as deterministic and stochastic, each of which have been used to describe static and dynamic system behavior. 

Deterministic vs. probabilistic: a deterministic performance-based approach does not incorporate uncertainty (e.g., probability of 

disruption) into the metric, while a probabilistic performance-based approach captures the stochasticity associated with system behavior. 

 Dynamic vs. static: a dynamic performance-based approach accounts for time-dependent behavior, while a static performance-based approach is free of time dependent measures of resilience. 

# 4.1.1. Deterministic approaches

Bruneau et al. [84] defined four dimensions of resilience in the well-known resilience triangle model in civil infrastructure: (i) robustness, the strength of system, or its ability to prevent damage propagation through the system in the presence of disruptive event, (ii) rapidity, the speed or rate at which a system could return to its original state or at least an acceptable level of functionality after the occurrence of disruption, (iii) resourcefulness, the level of capability in applying material (i.e., information, technological, physical) and human resources (i.e., labor) to respond to a disruptive event, and (iv) redundancy, the extent to which carries by a system to minimize the likelihood and impact of disruption. 

Bruneau et al. [84] then proposed a deterministic static metric for measuring the resilience loss of a community to an earthquake with Eq. (1). The time at which the disruption occurs is $t _ { 0 }$ , and the time at which the community returns to its normal pre-disruption state is $t _ { 1 }$ . The quality of the community infrastructure at time t, which could represent several different kinds of performance measures, is denoted with Q tð Þ. 

$$
R L = \int_ {t _ {0}} ^ {t _ {1}} [ 1 0 0 - Q (t) ] d t \tag {1}
$$

In this approach, the quality of degraded infrastructure is compared to the as-planned infrastructure quality (100) during the recovery period. RL can be illustrated as the shaded area in Fig. 5. Larger RL values indicate lower resilience while smaller RL imply higher resilience. The privilege of this method is its general applicability. Although this approach is utilized for the context of earthquake; however it can be extended to many systems as quality is a general concept. As such, its general applicability is an important advantage of the resilience triangle metric. The proposed metric by Bruneau et al. [84] assumes that the quality of community infrastructure is at $1 0 0 \%$ before earthquake, perhaps an unrealistic assumption. Some issues with the resilience triangle [85] include that the area associated with RL could be a difficult measure for decision makers to comprehend even when given as a percentage and that the disruptive event has an assumed instantaneous impact and the recovery efforts begin immediately. 

The resilience triangle paradigm has been applied in several contexts [86,87], as well as by Zobel [88], whose proposed metric is specified by “calculating the percentage of the total possible loss over some suitably long time interval $T ^ { \ast \ast \ast }$ as shown in Eq. (2). Parameters include, $X \in [ 0 , 1 ]$ as the percentage of functionality lost after a disruption, $T \in [ 0 , T ^ { * } ]$ as the time required for full recovery, and $T ^ { * }$ as a suitably long time interval over which lost functionality is determined. Zobel, who recognized that the same level of resilience found from the resilience triangle could be found from different combinations of $X$ and T, provided a visualization of the tradeoffs between lost functionality and recovery time for the same level of “resilience.” 

$$
R (X, T) = \frac {T ^ {*} - X T / 2}{T ^ {*}} = 1 - \frac {X T}{2 T ^ {*}} \tag {2}
$$

From Fig. 6, it can be seen that the total possible loss can be calculated as triangular area XT=2 for a single disruptive event. Zobel and Khansa [89] then extended the metric in Eq. (2) to measure the onset of and partial recovery from multiple, sequential disruptive events. An advantage of this proposed metric is its simplicity, though its linear recovery may not be realistic for some 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/b43f434a378fdbb27c6869cb429ded4511cb242c71be6feadad5dd078fa290fd.jpg)



Fig. 5. Resilience loss measurement from the resilience triangle (adapted from [84]).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/17318420f230ebbed48a785b25d00bdab1a3007233e843583c209543e9d1eeb8.jpg)



Fig. 6. A reinterpretation of the resilience triangle (adapted from [88]).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/752e819b15bc13dcc8b2cbe8bfc79e37e3bb8ce6124b416b174ab70a30ddb3a2.jpg)



Fig. 7. Static economic resilience quantification ([44]).


![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/de236514f8a7082be691cb22a1d27e8a672a9186ceb7d6db97734477388792c0.jpg)



Fig. 8. Dynamic economic resilience (Rose [44]).


systems and events. Further, the conceptual illustration of resilience represented in Fig. 6 suggests that the degradation of performance after a disruptive event is immediate, which may be true for some systems, though some systems may see a more gradual decrease over time (e.g., a manufacturing plant that maintains inventory as preparedness mechanism). This is also true for the conceptual illustration of resilience presented in Fig. 5 by Bruneau et al. [84]. 

Rose [44] defined economic resilience as “the ability of an entity or system to maintain system functionally when a disruption occurs.” This metric measures the ratio of the avoided drop in system output and the maximum possible drop in system output, 

![image](https://cdn-mineru.openxlab.org.cn/result/2026-04-02/fe9f9a47-9898-46dc-96da-d61654123377/daaad88151e15b8eba303e5c02b8c5ea8dcbae4bac0e47d6d4ddb29ef9f13755.jpg)



Fig. 9. System performance and state transition to describe resilience (adapted from Henry and Ramirez-Marquez [91]).


as shown in Fig. 7. The proposed metric, provided in Eq. (3), is classified as a deterministic static model where $\% \Delta D Y$ is the difference in non-disrupted and expected disrupted system performance and $\% \Delta D Y ^ { \mathrm { m a x } }$ is the difference in non-disrupted and worst case disrupted system performance. It may be difficult to estimate the expected degraded performance level, especially for unknown disruptions, because depth, width, and intensity of unknown disruptions might not be precisely estimable. Cox et al. [90] used a similar metric to calculate the resilience of London's transportation system, where the worst case disruption referred to the maximum reduction in passenger journeys for the attacked transportation modes. 

$$
R = \frac {\% \Delta Y ^ {\max} - \% \Delta Y}{\% \Delta D Y ^ {\max}} \tag{3}
$$

Rose [44] also considered the time-dependent aspects of recovery in the definition of dynamic resilience. Dynamic resilience can be obtained by hastening repair and reconstructing capital stock, such that investment becomes an important input in the dynamic resilience formula in Eq. (4). The measure, DR, is a function of $S O _ { H R }$ , the output of the system under hastened recovery, and $S O _ { W R }$ , the system's output without hastened recovery, where $t _ { i }$ is the ith time step during recovery and $N$ is the number of time steps considered. DR is depicted graphically in Fig. 8. 

$$
D R = \sum_ {i = 1} ^ {N} S O _ {H R} \left(t _ {i}\right) - S O _ {W R} \left(t _ {i}\right) \tag {4}
$$

Although the computation of dynamic resilience proposed by Rose [44] is relatively simple, it does not quantify the resilience value within a range of 0 and 1. In contrast to the dynamic resilience proposed by Rose [44], an economic resilience measure proposed by the same author is bounded between 0 and 1, which provides a convenient understanding of system resilience, especially for intermediate resilience values (0.2–0.8). 

Henry and Ramirez-Marquez [91] developed a time-dependent resilience metric that quantifies resilience as ratio of recovery to loss. Given that the performance of the system at a point in time is measured with performance function $\varphi ( t )$ , three system states that are important in quantifying resilience are represented in Fig. 9: (i) the stable original state which represents normal functionally of a system before disruption occurs, starts from time $t _ { 0 }$ and ends by time $t _ { e }$ , (ii) the disrupted state, which is brought about by a disruptive event $( e ^ { j } )$ at time $t _ { \mathrm { e } }$ whose effects set in until time $t _ { d }$ , describes the performance of the system from time $t _ { d }$ to $t _ { s }$ , (iii) the stable recovered state which refers to the new steady state performance level once the recovery action initiated at time $t _ { s }$ is over. Important dimensions of resilience that are depicted in Fig. 9 include reliability, or the ability of the system to maintain typical operation prior to a disruption, vulnerability, or the ability of the system to stave off initial impacts after event $e ^ { j }$ , and recoverability, or the ability of the system to recover in a timely manner from $e ^ { j }$ . The time-dependent measure of 

resilience is defined in Eq. (5), noting that resilient behavior is a function of $e ^ { j }$ . Notation $\textstyle \mathbf { \mathcal { A } } ( t | e ^ { j } )$ was adopted by Whitson and Ramirez-Marquez [81], as R is commonly reserved for reliability. 

$$
\mathbf {R} _ {\varphi} (t | e ^ {j}) = \frac {\varphi (t | e ^ {j}) - \varphi (t _ {d} | e ^ {j})}{\varphi (t _ {0}) - \varphi (t _ {d} | e ^ {j})} \tag {5}
$$

As explained above, the numerator of this metric implies recovery up to time t, while the denominator refers to the total loss due to disruption $e ^ { j }$ . The authors also calculated the total cost of recovered system followed by disruption as sum of implementing cost for resilience action and loss cost incurred due to system's non-operability due to disruption. Several subsequent developments in the context of resilience measurement and planning [92– 95] are based on the system state transition represented in Fig. 9 and the metric in Eq. (5) by Henry and Ramirez-Marquez [91]. 

Wang et al. [96] proposed a metric to measure the resilience of enterprise information systems, defined in Eq. (6), where m is the number of operations in the enterprise information system, $d _ { i }$ is the demand time for the recovery of operation $i ( i = 1 , 2 , . . . , m )$ , $c _ { i }$ is the completion time of operation i, and $z _ { i }$ is the weight given to the importance of operation i. 

$$
R = \max  \sum_ {i = 1} ^ {m} z _ {i} \frac {d _ {i}}{c _ {i}} \tag {6}
$$

This resilience measure can take on values greater than 1 when all operations can be recovered within demand time, and a larger value of this metric implies a more resilient system. The major limitation of this metric is that the number of recovery actions and number of operations are assumed to be known, while in reality systems are dealing with unknown situations. 

Omer et al. [97] proposed a resilience metric for infrastructure networks, calculated as the ratio of the closeness centrality of the network before and after disruption respectively. The closeness centrality is determined based on the accessibility of a node to the rest of the network. This resilience metric gives a value between 0 and 1, where the larger value is more desirable. 

Chen and Miller-Hooks [98] introduced an indicator for measuring resilience in transportation networks. The resilience indicator, represented in Eq. (7), quantifies the post-disruption expected fraction of demand that, for a given network, can be satisfied within pre-determined recovery budgets. Parameter $d _ { w }$ quantifies the maximum demand that can be satisfied for origin– destination (O–D) pair w following a disruption, and $D _ { w }$ is demand that can be satisfied for O–D pair w prior to the disruption. A limitation of this formulation includes its lack of specificity of the contribution of pre-disaster and post-disaster recovery activities, specifically in accounting for recovery time. 

$$
\text {R e s i l i e n c e} = E \left(\sum_ {w \in W} d _ {w} / \sum_ {w \in W} D _ {w}\right) = \frac {1}{\sum_ {w \in W} D _ {w}} E \left(\sum_ {w \in W} d _ {w}\right) \tag {7}
$$

Janic [99] used the proposed indicator by Chen and Miller-Hooks [98] for assessing airport resilience, defined as a ratio between the on-time flights and the total number of planned flights. 

Orwin and Wardle [100] introduced a measurement metric by linking resilience with instantaneous and maximum disturbance as shown in Eq. (8). $E _ { m a x }$ refers the maximum intensity of absorbable force without perturbing the system's function, and $E _ { j }$ refers to the magnitude of the disturbance's effect on safety at time $T _ { j }$ . The instantaneous resilience at time $T _ { j }$ can take on values between 0 and 1, where the value 1 indicates the maximum system resilience. The maximum resilience can be obtained when the disturbance's impact is fully recovered $\left( E _ { j } = 0 \right)$ . A disadvantage of this metric is that it does not consider time to recover and, much like the resilience triangle, could return the same resilience 

value for two systems with different recovery times. 

$$
\text {R e s i l i e n c e} = \left(\frac {2 \times | E _ {\max } |}{| E _ {\max } | + | E _ {j} |}\right) - 1 \tag {8}
$$

Enjalbert et al. [101] introduced local and global resilience assessment metrics, found in Eqs. (9) and (10), respectively, to model the resilience of public transportation systems from a safety management perspective. Function S t is a safety indicator of the system, measured as the “sum of effect of factors which can affect the system safety” [101]. Local resilience measures instantaneous resilience based on the safety indicator, and global resilience is obtained by integrating of local resilience over time, between when the disturbance effect commences (represented by $t _ { b }$ ) and end time of disturbance effect (represented by $t _ { e }$ ). Ouedraogo et al. [102] expands the application of these local and global resilience metrics to air transportation systems. 

$$
\text {L o c a l} = \frac {d S (t)}{d t} \tag {9}
$$

$$
\text {g l o b a l} = \int_ {t _ {b}} ^ {t _ {e}} \text {l o c a l} = \int_ {t _ {b}} ^ {t _ {e}} \frac {d S (t)}{d t} \tag {10}
$$

Francis and Bekera [103] proposed a dynamic resilience metric. $\rho _ { i }$ for event i, shown in Eq. (11). $S _ { p }$ refers to the speed of recovery, $F _ { o }$ is the performance of level of the system at its original state, $F _ { r }$ is the performance level at a new stable level after recovery efforts, and $F _ { d }$ is the performance level immediately following the disruption. Speed of recovery in Eq. (12) assumes exponential growth, with $t _ { \delta }$ representing slack time or the maximum amount of time post-disaster that is acceptable before recovery ensues, $t _ { r }$ representing the time to final recovery or time to reach a new equilibrium state, $t _ { r } ^ { * }$ representing the time to complete the initial recovery actions, and a representing the parameter controlling the “decay” in resilience until the new equilibrium is met. This metric describes the absorptive capacity in terms of the proportion of original steady-state functionality maintained after the new steadystate functionality, $F _ { r } / F _ { o }$ . It is notable that this metric is not constrained on [0, 1], thereby making extreme values difficult to comprehend, and further the exponential growth function governing the improvement in resilience may not always represent system behavior. The relationship between absorptive capacity and adaptive capacity is a bit unclear. The authors suggest ratio $F _ { d } / F _ { o }$ represents the capability of system to absorb shocks without recovery action, and $F _ { r } / F _ { o }$ represents adaptive capacity which relates to those post-disaster activities taken after the disruption. Adaptive capacity might be more effectively formulated to reflect the ability of the system to recover the lost performance level not initially absorbed by absorptive capacity. That is, for the adaptive capacity ratio, the recovered performance level $F _ { r }$ could be compared with the difference between the initial performance level $F _ { o }$ and the performance level after disruption $F _ { d } , F _ { r } / ( F _ { 0 } - F _ { d } )$ . 

$$
\rho_ {i} = S _ {p} \frac {F _ {r}}{F _ {o}} \frac {F _ {d}}{F _ {o}} \tag {11}
$$

$$
S _ {p} = \left\{ \begin{array}{l l} \left(t _ {\delta} / t _ {r} ^ {*}\right) \exp \left[ - a \left(t _ {r} - t _ {r} ^ {*}\right) \right] & \text {f o r} t _ {r} \geq t _ {r} ^ {*} \\ \left(t _ {\delta} / t _ {r} ^ {*}\right) & \text {o t h e r w i s e} \end{array} \right. \tag {12}
$$

Cimellaro et al. [104] expressed resilience in terms of quality of service, as shown in Eq. (13), where $\alpha$ is a weighting factor representing the importance of pre- and post-disruption service qualities, $Q _ { 1 } ( t )$ and $Q _ { 2 } ( t )$ are the quality service of the system before and after the disruption, respectively, and $T _ { L C }$ is the control time of the system. The authors applied this metric to measure healthcare resilience, using waiting time that a patient spends in the queue for treatment as an index of service quality. The resilience value obtained in Eq. (13) is highly dependent upon the value of the 

weighting factor. Therefore, different resilience values can be attained due to differences in decision maker preferences. Although the authors introduced four properties of resilience including rapidity, robustness, redundancy, and resourcefulness, these properties were not explicitly included in the resilience metric. 

$$
R = \alpha \int_ {T _ {L C}} \frac {Q _ {1} (t)}{T _ {L C}} d t + (1 - \alpha) \int_ {T _ {L C}} \frac {Q _ {2} (t)}{T _ {L C}} d t \tag {13}
$$

# 4.1.2. Probabilistic approaches

Chang and Shinozuka [105] introduced a probabilistic approach for assessing resilience, measured with two elements: (i) loss of performance and (ii) length of recovery. Resilience is defined as the probability of the initial system performance loss after a disruption being less than the maximum acceptable performance loss and the time to full recovery being less than the maximum acceptable disruption time. This measure is represented in Eq. (14), where A represents the set of performance standards for maximum acceptable loss of system performance, $r ^ { * }$ , and maximum acceptable recovery time, $t ^ { * }$ , for a disruption of magnitude i. 

$$
R = P (A \mid i) = P \left(r _ {0} <   r ^ {*} \text {a n d} t _ {1} <   t ^ {*}\right) \tag {14}
$$

A series of disruption simulations were performed, and the probabilities in Eq. (14) were generated from the proportion of simulation runs not meeting the standards defined by A. Although Chang and Shinozuka [105] applied this approach to measure the resilience of infrastructure and communities following an earthquake, it can be generally applied to any other systems and disruptions. The distinguishing feature of the proposed metric is its acknowledgment of uncertainty in quantification of resilience. However, the proposed metric does not consider an extra penalty when both performance loss and length of recovery exceed their maximum acceptable values. 

Ouyang et al. [106] developed a stochastic time-dependent metric for measuring “annual resilience” under multi-hazard events, shown in Eq. (15). Their primary metric measures the mean ratio of the area between the actual performance curve, $P ( t )$ , and the time axis to the area between the target performance curve, $T P ( t )$ , and the time axis over a length of time T (considered to be a year by the authors). AR is a stochastic metric as $P ( t )$ is modeled as a stochastic process, and $T P ( t )$ can be represented as a stochastic process or some dethazards can be included with the $\textstyle \sum _ { n = 1 } ^ { N ( T ) } A I A _ { n } ( t _ { n } )$ ction. Multipleterm, where n occur during T, $t _ { n }$ is a random variable describing the time at which the nth event occurs, and $A I A _ { n } ( t _ { n } )$ is the area between $P ( t )$ and TP t for the nth event. The authors considered different types of disruptions, making the approach more applicable for real world applications. Further, uncertainty is incorporated by modeling target performance curve as stochastic process. 

$$
A R = E \left[ \frac {\int_ {0} ^ {T} P (t) d t}{\int_ {0} ^ {T} T P (t) d t} \right] = E \left[ \frac {\int_ {0} ^ {T} T P (t) d t - \sum_ {n = 1} ^ {N (T)} A I A _ {n} \left(t _ {n}\right)}{\int_ {0} ^ {T} T P (t) d t} \right] \tag {15}
$$

Youn et al. [14] considered both mitigation and contingency strategies to define their resilience metric. The metric, provided in Eq. (16), is defined as the sum of the passive survival rate (reliability) and proactive survival rate (restoration) following a disruption. 

$$
\Psi (\text {r e s i l i e n c e}) = R (\text {r e l i a b i l i t y}) + \rho (\text {r e s t o r a t i o n}) \tag {16}
$$

In Eq. (16), restoration is defined to be the degree of reliability recovery and is calculated as the joint probability of a system failure event, $E _ { s f }$ , a correct diagnosis event, $E _ { c d }$ , a correct prognosis event, $E _ { c p }$ , and a successful recovery action event, $E _ { m r }$ [14]. The 

formulation for restoration is provided in Eq. (17). 

$$
\rho = P \left(E _ {m r} \mid E _ {c p} E _ {c d} E _ {s f}\right) \times P \left(E _ {c p} \mid E _ {c d} E _ {s f}\right) \times P \left(E _ {c d} \mid E _ {s f}\right) \times P \left(E _ {s f}\right) \tag {17}
$$

In contrast to the most of studies reviewed in this paper (e.g., [91,96]), the metric in Eq. (16) accounts for reliability, or a preventive means to stave off the occurrence of a disruption as a component in quantifying resilience, while most other resilience assessment metrics are primarily a function of the level of initial impact and duration of recovery. It is noteworthy to point out that this metric is bounded on [0,1]. $\boldsymbol { \Psi }$ takes on the value 0 when the restoration activity does not occur or otherwise fails, and takes on the value 1, its upper bound, when the system is completely restored. The advantage of resilience formula given in Eq. (16) is the consideration of both pre-disaster and post-disaster activities. As shown in Eq. (17), restoration is not time-dependent, therefore does not consider the length of restoration. Due to its inclusion of reliability, such a metric is perhaps more suitable for measuring the resilience of engineering systems because reliability can more effectively be calculated for engineering systems through failure testing studies. The calculation of conditional probability may be difficult, especially when a disruption occurs for the first time. Any errors in estimating the conditional probability by expert knowledge can result in a mischaracterization of restoration, and consequently, resilience. 

Ayyub [107] defined a stochastic resilience metric in terms that also considered the effects of aging on the system. The system's performance is defined as the difference between the system's strength and system's load. Robustness and resourcefulness are considered as two dimensions of resilience in this metric. The metric is shown in Eq. (18), where $T _ { i }$ is the time to incident, $T _ { f }$ is the time to failure, $T _ { r }$ is the time to recovery, $\Delta T _ { f } = T _ { f } - T _ { i }$ is the duration of failure, and $\Delta T _ { r } = T _ { r } - T _ { f }$ is the duration of recovery. 

$$
R _ {e} = \frac {T _ {i} + F \Delta T _ {f} + R \Delta T _ {r}}{T _ {i} + \Delta T _ {f} + \Delta T _ {r}} \tag {18}
$$

The failure profile, F, in Eq. (18) is a measure of robustness and redundancy, calculated using Eq. (19). Ayyub offers several trajectories of $f$ for brittle, ductile, and graceful failures. Similarly, the recovery profile, R, measures recoverability with Eq. (20), with several example trajectories of $r$ depending on the convexity (e.g., “as good as old”) or concavity (e.g., “as good as new”) recovery. The plot of system performance in [107] is similar to that of Fig. 9, but offers (i) explicit vulnerability and recoverability trajectories with specific meanings and (ii) specifically incorporates the effects of aging in its graphical representation. 

$$
F = \frac {\int_ {t _ {i}} ^ {t _ {f}} f d t}{\int_ {t _ {i}} ^ {t _ {f}} Q d t} \tag {19}
$$

$$
R = \frac {\int_ {t _ {f}} ^ {t _ {r}} r d t}{\int_ {t _ {f}} ^ {t _ {r}} Q d t} \tag {20}
$$

Note that the time to failure $T _ { f }$ is characterized by its probability density function which is the negative of the derivative of reliability function. This metric by Ayyub [107] is among the most comprehensive resilience measures, prescribing both mitigation (reliability) and contingency (recovery duration) strategies. Ayuub [107] modeled the ratio of robustness to redundancy and the ratio of resourcefulness to rapidity by introducing failure profile $F$ and recovery profile R, respectively. 

Hashimoto et al. [108] defined the resilience of a system as conditional probability of a satisfactory (i.e., non-failure) state in time period $t + 1$ given an unsatisfactory state in time period t, shown in Eq. (21).S t is the state of the system at time t, and NF and $F$ represent non-failure and failure states, respectively. 

$$
R = P \{S (t + 1) \in N F \mid S (t) \in F \} \tag {21}
$$

Franchin and Cavalieri [109] introduced a probabilistic metric for assessing infrastructure resilience in the presence of earthquake. Their definition of resilience is based on the efficiency of the spatial distribution of an infrastructure network. The efficiency of two nodes in an infrastructure network is defined as being inversely proportional to their shortest distance. The resilience metric is provided in Eq. (22), where $P _ { D }$ is the fraction of displaced population, $E _ { 0 }$ is the efficiency of the city network before the earthquake, $P _ { r }$ is the measure of progress of recovery, and $E ( P _ { r } )$ is the recovery curve of the fraction of the displaced population. In their study, the efficiency of a city road network is measured in terms of population density. 

$$
R = \frac {1}{P _ {D} E _ {0}} \int_ {0} ^ {P _ {D}} E \left(P _ {r}\right) d P _ {r} \tag {22}
$$

The metric in Eq. (22) is probabilistic due to the stochastic nature of $P _ { D }$ . This resilience metric is restricted between 0 and 1, since normalization is performed with $P _ { D }$ and $E _ { 0 }$ . Although the authors used this metric for assessing resilience of road city network, it is applicable to the other infrastructures such as electric power and water supply networks, assuming a suitable function for efficiency exists. An time-dependent extension could model $P _ { D }$ using a dynamic simulation model. 

Pant et al. [93] introduced three stochastic resilience metrics to implement the resilience formulation in Eq. (5). Time to Total System Restoration measures the total time spent from the point of time when recovery activities commence to the time that all recovery activities are finalized. From recovery point of view, this metric refers to the man-hours require to repair the disrupted component individually. In their work a set of recovery activities are defined based on order of importance, assuming that the recovery order and probability distributions for the components recoveries are known. The second resilience measure, Time to Full System Service Resilience, measures the total time spent from the point of time when recovery starts to the time that system service is fully restored. Finally, Time to $\alpha \times 1 0 0 \%$ -Resilience: it measures the total time spent from the point of time when recovery commences until the time that $\alpha \times 1 0 0 \%$ of system functionality (e.g., capacity, inventory) is restored. 

Attoh-Okine et al. [110] quantified the value of system resilience using belief functions or Dampster–Shafer theory, a generalization of the Bayesian theory of subjective probability that uses imprecise probabilities. The discrete belief functions was used to calculate the resilience of system which is beneficial for the systems with high degree of interdependencies like those connecting infrastructure systems. 

Barker et al. [92] proposed two stochastic resilience-based component importance measures (CIMs) for identifying the primary contributors to network resilience, also based on the resilience formulation in Eq. (5). The modeling of these two metrics is devoted to vulnerability and recoverability in a network following a disruption. The first CIM metric, analogous to the risk reduction worth importance measure in the reliability engineering field, quantifies the proportion of restoration time attributed to each network component. The second resilience-based CIM, similar to the reliability achievement worth importance measure, quantifies how network resilience is improved if a specific network component is invulnerable. The authors then concluded that the network resilience can be obtained in the form of two ways: vulnerability reduction strategy or accelerating the speed of recovery activities through evaluating CIM metrics. 

# 4.2. Structural-based models

The structural-based approaches examine how the structure of a system impacts its resilience. System behavior must be observed and characteristics of a system must be modeled or simulated. We 

characterize structural-based models into three kinds of approaches: optimization models, simulation models, and fuzzy logic models. 

# 4.2.1. Optimization models

Faturechi et al. [111] proposed a mathematical model for evaluating and optimizing airport resilience, aiming to maximize the resilience of an airport's runway and taxiway network. The main strategy used in their mathematical model is the quick restoration of post-event take-off and landing capacities to the level of capacities before disruption by taking into account time, physical, operational, space, resource, and budget restrictions. Two types of decision variables, including pre-event and post-event decisions, were considered. The main feature of their work is that preparedness and recovery activities are taken into account in the stochastic integer model. 

Faturechi and Miller-Hooks [112] introduced a multi-objective, three-stage stochastic mathematical model to quantify and optimize travel time resilience in road networks. The three stages of decision process include: (i) pre-event mitigation, (ii) preparedness, and (iii) post-event response. The resilience of the road network is defined as network's ability to withstand and adapt to a disruption, with travel time used to assess resilience. The objective function of their model seeks to maximize the expectation of road network resilience over all possible disruption scenarios and minimize the total travel time simultaneously. 

Azadeh et al. [113] investigated the concept of resilience engineering in a petrochemical plant using data envelopment analysis (DEA), a linear programming method for measuring the efficiency of multiple decision-making units (DMUs) when production process consists of multiple input and outputs. The authors first introduced 10 indicators of resilience of a petrochemical plant including management commitment, reporting, learning, awareness, preparedness, flexibility, self-organization, teamwork, redundancy, and fault-tolerance. In their petrochemical plant study, 11 departments such as chemical operation, information technology, maintenance, and polymer operation are considered and denoted as DMUs. Finally, DEA is utilized to measure the efficiency of the petrochemical plant's departments based on 10 introduced indicators. 

Jin et al. [114] developed a two-stage stochastic programming model for analyzing the resilience of a metropolitan public transportation network. The authors defined the resilience of the network as the fraction of travel demand that can be satisfied by the disrupted network after occurrence of disruptive event. The proposed mathematical model generates alternative paths under disruptive conditions. 

Baroud et al. [94] quantified vulnerability and recoverability of waterway network using the two stochastic resilience-based component importance measures (CIM) introduced by Barker et al. [92]. The links of waterway network were ranked with respect to their importance calculated by two CIM indicators. The waterway links were prioritized using a multicriteria comparison technique to generate a stochastic order. The authors did not take into account the impact of cascading of a disruptive event through the waterway network. 

Cardoso et al. [115] proposed a mixed integer linear model to design both forward and closed-loop supply chains. The proposed model takes into account two situations: (i) when the disruption occurs with certainty, and (ii) when there is a probability associated with the occurrence of disruption. Six indicators are considered into the model for designing a resilience network including flow and node complexity, node and density criticality, customer service level and investment. 

Khaled et al. [116] proposed a mathematical model and solution approach for evaluating critical railroad infrastructures to maximize rail network resilience. Identifying critical components can enable 

stakeholders to prioritize protection initiatives or add necessary redundancy to maximize rail network resilience during a disruptive event. In this paper, the criticality of an infrastructure element is evaluated based on the increased delay incurred when that element is disrupted. The mathematical model considers individual component (links and nodes) disruptions separately to determine the impact, where considering multiple component disruptions simultaneously might be more meaningful as a disruptive event may realistically impact multiple adjacent components. 

Vugrin et al. [117] proposed a multi-objective optimization model for transportation network recovery, where resilience is defined by the optimal recovery of disrupted links. The model consists of two levels: (i) a lower-level problem that involves solving for network flows, and (ii) an upper-level problem that identifies the optimal recovery sequences and modes. The proposed model embedded only recovery actions, including the level of recovery for a disrupted link, but not preparedness actions. 

Ash and Newth [118] attempted to optimize complex largescale networks for resilience against cascading failures. Cascading failures are very common in power transmission, communication, and transportation networks. Cascading failures usually triggers by failing a node of network due to overloading and its effect nonlinearly propagate through network that eventually may results in network shutdown. Many efforts have been put to study the behavior of cascading failure in complex interdependent networks like [119–124]. Ash and Newth [118] first modeled cascading failures and then developed failure resilient networks based the notion of network topology indices including common neighbors, modularity, and assortativeness. 

Alderson et al. [125] proposed a mixed integer non-linear programming (MINLP) to quantify the operational resilience of critical infrastructures. Resilience is defined in terms of defense strategies with little attention given to the important recovery dimension of resilience found in most works. Their proposed model aims to find out the best defense strategy in the case of attacks such that the total cost of the defense strategy is minimized. The concentration of MINLP model is on preparedness actions, but not on recovery. 

Sahebjamnia et al. [87] proposed a multi-objective mixed integer linear programming (MOMILP) to find efficient resource allocation patterns among candidate business continuity and disaster recovery plans while considering features of organizational resilience. The objective of proposed model is to minimize the total loss of operating level of key products, as well as to minimize the total recovery time of key products. 

With respect to supply chains, Li and Zhao [126] developed a model for assessing supply chain resilience with a series relationship among the supply chain components along with self-adaptive and self-recovery abilities. 

# 4.2.2. Simulation models

Albores and Shaw [127] proposed a discrete event simulation model to evaluate the preparedness of a fire and rescue service department in the presence of terrorist attacks. The authors considered preparedness as key driving factor of pre-event disruption resilience. Two simulation models were: (i) the first model mimics the mass decontamination of a population following a terrorist attack, while (ii) the second model deals with the harmonization of resource allocation across regions. 

Carvalho et al. [128] applied discrete event simulation to assess the resilience of a supply chain. Two strategies of flexibility and redundancy are taken into account as elements of resilience in their simulation model. Redundancy is modeled by keeping additional inventory to successfully withstand disruptions, and flexibility is modeled by restricting the extent of the disrupted transportation 

system. Six different scenarios are investigated with the simulation model. There are several limitations for this research study. First, the results found in this research may not be universally applicable across different sectors, as a redundancy strategy may not be a costefficient solution in comparison to a flexibility strategy due to high inventory holding costs, or vice versa. 

Virginia et al. [129] proposed a dynamic simulation approach for simulating supply chain resilience. The authors considered readiness (preparedness), responsiveness, and recovery as key elements of resilience. The Integral of Time Absolute Error (ITAE), used commonly in the control engineering field, is employed as measure of resilience. The simulation model attempts to capture the minimum value of ITAE which is corresponding to the best response and recovery with lowest deviation from the target level following by disruption. 

Jain and Bhunya [130] used Monte Carlo Simulation to study the resilience of a water storage reservoir, calculated using conditional probability introduced by Hashimoto et al. [108]. The behavior of a reservoir's resilience is investigated under diverse adversary scenarios. 

With respect to critical infrastructure networks, Adjetey-Bahun et al. [131] used a time-dependent simulation model to measure the resilience indicators of a railway transportation system. A set of disruptive events are modeled through simulation model with consequences of increase of travel time and reduction of train capacity. Sterbenz et al. [132] proposed an approach based on integrating analytical simulation, topology generation, and experimental emulation to improve the resilience and survivability of Internet networks. The resilience of the Internet network is defined as the ability of the network to provide a desired service level when it is challenged by large-scale disasters or intense failures. 

# 4.2.3. Fuzzy logic models

Aleksic et al. [133] proposed a fuzzy model for assessing organizational resilience. Fuzzy linguistic variables were used to express the relative importance of the organizational resilience factors. 

Azadeh et al. [134] assessed the factors of engineering resilience through a fuzzy cognitive map (FCM). The authors used a FCM to describe the causal reasoning between nine factors of engineering resilience: teamwork, awareness, preparedness, learning culture, reporting, flexibility, redundancy, management commitment, and fault tolerance. A FCM can be represented by a fuzzy graph structure and obtained as a result of neural network and fuzzy logic approaches. 

Muller et al. [135] presented a fuzzy architecture for assessing the resilience of critical infrastructure. Redundancy and adaptability were considered to be the primary components of infrastructure resilience. The redundancy and adaptability inputs of the fuzzy architecture, and the resilience output, are expressed using linguistic variables. 

Tadic et al. [136] integrated fuzzy forms of the Analytic Hierarchy Process (AHP) and the multicriteria discrete comparison technique TOPSIS for evaluating and ranking organizational resilience based on qualitative assessments. The approach was used to rank several resilience factors including (i) planning strategies, (ii) capability and capacity of internal resources, (iii) internal situation monitoring and reporting, (iv) human factors, (v) quality, (vi) external situation monitoring and reporting, (vii) capability and capacity of external resources, (viii) design factors, (ix) detection potential, and (x) emergency response. 

# 5. Research directions

Based on the literature review presented in this paper, as well as recent reports and calls for proposals by US funding agencies, 

we identify a few on-going and upcoming research directions that are of interest to the resilience community. 

# 5.1. Planning for resilience

We offer a review of a number of measures for quantifying resilience in this paper. But their usefulness is limited unless they can guide planning for resilience. 

Highlighted throughout this review, resilience generally focuses on the ability of a process or system to withstand a disruptive event and to recover from it. Both of these components of resilience (e.g., referred to as robustness and rapidity by Bruneau et al. [84], referred to as the complement of vulnerability and as recoverability [91]) are the result of planning and resource allocation. Understanding the tradeoffs among resources available and the resilience achieved through investments in vulnerability reduction and recoverability enhancement enables planning for resilience. Optimization models can be used to model the vulnerability and recoverability of disrupted systems. With respect to network vulnerability, the network interdiction literature provides a formulation for optimal allocation of resources toward network disruption [144]. The recovery problem can be viewed and modeled in similar to project scheduling problem, with the primary difference being that the completion of a subset of repair tasks has value because the performance of infrastructure network can be partially restored [137]. The integration of interdiction approaches and subsequent recovery scheduling approaches may provide a means to optimally allocate resources to building resilience with the tradeoff between vulnerability reduction and recoverability enhancement in mind. 

# 5.2. Resilient interdependent processes and systems

Recognizing the interdependence among infrastructure systems is vital for planning for their operation [138]. There exist highly coupled relationships among transportation, electric power, and telecommunication systems, among other infrastructures. And the resilience of one system can impact the resilience of others. More work is needed from translating a wealth of interdependent infrastructure models [139] to the study of their interdependent resilience [e.g., 140]. 

# 5.3. Standards for resilient systems

The National Institute of Standards and Technology (NIST) is a federal agency charged with developing and applying measurements and standards for industry practice. NIST has recently promoted the identification of existing standards and guidelines that can be implemented to enhance resilience in the built environment, as well as develop new standards and guidelines to fill remaining gaps. Emphasis is given to performance goals for buildings and infrastructure networks and systems under disruptions, including their recovery [141]. 

# 5.4. Community resilience and the built environment

An ultimate measure of the performance of infrastructure networks and other systems is how they enable and enhance daily life. And when such networks and systems are disrupted, how does their resilience impact the resilience of the community that relies on them? The relationship between communities and the built environment is a budding area of research with momentum provided by NIST [142], which is linking the standards for the built environment to their ultimate benefit to the community. Measuring community resilience can come from several perspectives, including human movement, community connectivity, and economic productivity [143]. 

# 6. Concluding remarks

Over the past decade, the significance of the concept of resilience has been well recognized among researchers and practitioners. Effort has been devoted to measure the resilience of engineering systems, but challenges still exist. The objective of this paper is to provide a taxonomy and review of approaches to quantify system resilience. We first classified four domains for definitions of resilience: organizational, social, economic, and engineering. Across these domains, the traditional definitions of resilience concentrate on the inherent ability of systems to absorb of the effects of a disruption to their performance, referring to preparedness activities, and more recent definitions also account for the recovery of their performance. 

We classify the quantification of resilience into two broad classes: qualitative and quantitative approaches. Qualitative assessment approaches include conceptual frameworks and semi-quantitative methods. Conceptual frameworks provide insights about the notion of resilience but do not provide a quantitative value. Semi-quantitative generally involve the aggregation of expert opinion along multiple dimensions into an index. The quantitative assessment category is characterized as either general resilience measures or structural models. General resilience measures generally assess resilience by comparing the performance of a system before and after disruption. Some measures are static in nature [84], while others offer a timedependent perspective on system performance [91]. A recent trend in resilience measures has been accounting for aleatoric and epistemic uncertainty with stochastic approaches. Structural based approaches emphasize the structure or characteristics of a particular system to derive a measure of its resilience. Work reviewed in this paper is summarized in Table 2. 

The term “resilience” is increasingly used in research journals, government documents, and the media, but work still remains on making resilience assessment usable. Methods for resilience planning are still a relatively unexplored area, including tangible resource allocation models, tradeoffs among the dimensions of resilience, the relationship between community resilience and the resilience of the built environment, and data-driven standards ensuring resilience. 

# References



[1] Kaplan S, Garrick J. On the quantitative definition of Risk. Risk Anal 1981;1:11–27. 





[2] Manual J. The long road to recovery: environmental health impacts of hurricane sandy. Environ Health Perspect 2013;121:A152–9. 





[3] Lipton E. Cost of storm-debris removal in city is at least twice the US average. The New York Times; 2013. 





[4] Minkel JR. The 2003 northeast blackout-five years later. Sci Am 2008, http:// www.scientificamerican.com/article/2003-blackout-five-years-later/. 





[5] Smith CM, Graffeo CS. Regional Impact of Hurricane Isabel on Emergency Departments in Coastal Southeastern Virginia. Acad Emerg Med 2005;12 (12):1201–5. 





[6] MacKenzie CA, Santos JR, Barker K. Measuring international production losses from a disruption: case study of the japanese earthquake and tsunami. Int J Prod Econ 2012;138(2):293–302. 





[7] Department of Homeland Security. National Infrastructure protection plan. Washington, DC: Office of the Secretary of Homeland Security; 2013. 





[8] Department of Homeland Security. Quadrennial homeland security review (QHSR). Washington, DC: Office of the Secretary of Homeland Security; 2014. 





[9] Park J, Seager TP, Rao PSC, Convertino M, Linkov I. Integrating risk and resilience approaches to catastrophe management in engineering systems. Risk Anal 2013;33:3. 





[10] Zolli A, Healy AM. Resilience: why things bounce back. New York City, NY: Simon & Schuster; 2013. 





[11] Bhamra R, Dani S, Burnard K. Resilience: the concept, a literature review and future directions. Int J Prod Res 2011;49(15):5375–93. 





[12] Martin-Breen P, Anderies JM. Resilience: a literature review. Brighton: Institute of Development Studies (IDS); 2011. 





[13] Rampell C. Comparing recessions and recoveries: job changes. The New York Times; 2012. 





[14] Youn BD, Hu C, Wang P. Resilience-driven system design of complex engineered systems. J Mech Des 2011;133:10. 





[15] Hollnagel E, Woods DD, Leveson N. Resilience engineering: concepts and precepts. Aldershot, UK: Ashgate; 2006. 





[16] Hollnagel E. Prologue: the scope of resilience engineering. In: Hollnagel E, Paries J, Woods DD, Wreathall J, editors. Resilience engineering in practice: a guidebook. USA: Ashgate Publishing Company; 2010. 





[17] American Society of Mechanical Engineers (ASME). Innovative Technological Institute (ITI). Washington, D.C.: ASME ITI, LLC; 2009. 





[18] Dinh LTT, Pasman H, Gao X, Sam Mannan M. Resilience engineering of industrial processes: principles and contributing factors. J Loss Prev Process Ind 2012;25:233–41. 





[19] Sheffi Y. The resilience enterprise: overcoming vulnerability for competitive enterprise. Cambridge, MA: MIT Press; 2005. 





[20] T.J. Vogus and K.M. Sutcliffe, Organizational resilience: toward a theory and research agenda. In: Proceedings of the IEEE international conference on systems, man and cybernetics; 2007. p. 3418–422. 





[21] Sheffi Y. Resilience reduces risk. Logist Q 2006;12:1. 





[22] McDonald N. Organisational resilience and industrial risk. In: Hollnagel E, Woods DD, Leverson N, editors. Resilience engineering: concepts and precepts. USA: Ashgate Publishing Company; 2010. p. 155–79. 





[23] Patterson ES, Woods DD, Cook RI, Render ML. Collaborative cross-checking to enhance resilience. Cogn Technol Works 2007;9(3):155–62. 





[24] Alblas AA, Jayaram JSR. Design resilience in the fuzzy front end (FFE) context: an empirical examination. Int J Prod Res 2014:1–19. http://dx.doi.org/ 10.1080/00207543.2014.899718. 





[25] Burnard K, Bhamra R. Orginasational resilience: development of a conceptual framework for organisational response. Int J Prod Res 2011;49(18):5581–99. 





[26] Gilly J-P, Kechidi M, Talbot D. Resilience of organisations and territories: the role of pivot firms. Eur Manag J 2014;32(4):596–602. 





[27] Riolli L, Savicki V. Information system organizational resilience. Omega 2003;31(3):227–33. 





[28] Adger WN. Social ecological resilience: are they related? Prog Hum Geogr 2000;24(3):347–64. 





[29] Community and regional resilience institute (CARRI) Research report 8. Economic resilience to disasters; 2009. 





[30] Keck M, Sakdapolrak P. What is social resilience? Lessons learned and ways forward Erdkunde 2013;67(1):5–19. 





[31] O. Cohen, D. Leykin, M. Lahad, A. Goldberg and L. Aharonson-Daniel, The conjoint community resiliency assessment measure as a baseline for profiling and predicting. 





[32] Pfefferbaum B, Reissman D, Pfefferbaum R, Klomp R, Gurwitch R. Building resilience to mass trauma events. In: Doll L, Bonzo S, Nercy J, Sleet D, editors. Resilience engineering: concepts and precepts. New York: Kluwer Academic Publishers; 2005. 





[33] Carpenter S, Walker B, Anderies JM, Abel N. From metaphor to measurement: resilience of what to what? Ecosystems 2001;4:765–81. 





[34] Webb CT. What is the role of ecology in understanding ecosystem resilience? BioScience 2007;57(6):470–1. 





[35] Kerkhoff AJ, Enquist BJ. The implications of scaling approaches for understanding resilience and reorganization in ecosystems. BioScience 2007;57 (6):489–99. 





[36] Luthar SS, Cicchetti D, Becker B. The construct of resilience: a critical evaluation and guidelines for future work. Child Dev 2000;71(3):543–62. 





[37] Bonanno GA, Moskowitz JT, Papa A, Folkman S. Resilience to loss in bereaved parents, and bereaved gay men. J Personal Soc Psychol 2005;88(5):827–43. 





[38] Bonanno GA, Galea S. What predicts psychological resilience after disaster? The role of demographics, resources, and life stress J Consult Clin Psychol 2007;75(5):671–82. 





[39] Yu Y, Peng L, Chen L, Long L, He W, Li M, et al. Resilience and social support posttraumatic growth of women with infertility: the mediating role of positive coping. Psychiatry Res 2014;28(2):401–5. 





[40] Cacioppo JT, Reis HT, Zautra AJ. Social resilience: the value of social fitness with an application to the military. Am Psychol 2011;66(1):43–51. 





[41] White RK, Edwards WC, Farrar A, Plodinec MJ. A practical practical approach to building resilience in America's communities. American Behavioral Scientist 2014;59(2):200–19. 





[42] Kofinas G. Resilience of human-rangifer systems: frames off resilience help to inform studies of human dimensions of change and regional sustainability. IHDP Update 2003;2:6–7. 





[43] Rose A, Liao SY. Modeling regional economic resilience to disasters: a computable general equilibrium analysis of water service disruptions. J Reg Sci 2005;45(1):75–112. 





[44] Rose A. Economic resilience to natural and man-made disasters: multidisciplinary origins and contextual dimensions. Environ Hazard 2007;7 (4):383–98. 





[45] Martin RL. Regional economic resilience, hysteresis and recessionary shocks. J Econ Geogr 2012;12:1–32. 





[46] Percoco M. Infrastructure and economic efficiency in Italian regions. Netw Spat Econ 2004;4:361–78. 





[47] Shafieezadeh A, Ivery Burden L. Scenario-based resilience assessment framework for critical infrastructure systems: case study for seismic resilience of seaports. Reliab Eng Syst Saf 2014;132:207–19. 





[48] Shepherd DiPietro G, Scott Matthews H, Hendrickson CT. Estimating economic and resilience consequences of potential navigation infrastructure failures: a case study of the Monogahela River. Transp Res A 2014;69:142–64. 





[49] Vugrin ED, Camphouse RC. Infrastructure resilience assessment through control design. Int J Crit Infrastruct 2011;7(3):243–60. 





[50] MacKenzie CA, Barker K. Empirical data and regression analysis for estimation of infrastructure resilience with applications to electric power outages. J Infrastruct Syst 2013;19(1):25–35. 





[51] Ouyang M, Wang Z. Resilience assessment of interdependent infrastructure systems: with a focus on joint restoration modeling and analysis. Reliab Eng Syst Saf 2015;141:74–82. 





[52] National infrastructure advisory council (NIAC), critical infrastructure resilience: final report and recommendations;2009. 





[53] Allenby B, Fink J. Social and ecological resilience: toward inherently secure and resilient societies. Science 2000;24(3):347–64. 





[54] Pregenzer A. Systems resilience: a new analytical framework for nuclear nonproliferation. Albuquerque, NM: Sandia National Laboratories; 2011. 





[55] Haimes YY. On the definition of resilience in systems. Risk Anal 2009;29 (4):498–501. 





[56] The infrastructure Security Partnership (TISP). Regional disaster resilience: a guide for developing on action plan. Reston, VA: American Society of Civil Engineers; 2006 The infrastructure Security Partnership. 





[57] Vugrin ED, Warren DE, Ehlen MA, Camphouse RC. A framework for assessing the resilience of infrastructure and economic systems. In: Gopalakrishnan K, Peeta S, editors. sustainable infrastructure systems: simulation, modeling, and intelligent engineering. Berlin: Springer-Verlag, Inc.; 2010. 





[58] 〈http://thomsonreuters.com/thomson-reuters-web-of-science/〉. 





[59] Chen C, CiteSpace II. Detecting and visualizing emerging trends and transient patterns in scientific literature. J Am Soc Inf Sci Technol 2006;57(3):359–77. 





[60] www.webofscience.com. 





[61] Ungar M. Qualitative contributions to resilience research. Qual Soc Work 2015;2(1):85–102. 





[62] Sarre S, Redlich C, Tinker A, Salder E, Bhalla A, McKevitt C. A systematic review of qualitative studies on adjusting after stroke: lessons for the study of resilience. Disabil Rehab 2014;36(9):716–26. 





[63] Resilience alliance. assessing resilience in social-ecological systems: a practitioners workbook, 1 2007a. 





[64] Speranza CI, Wiesmann U, Rist S. An indicator framework for assessing resilience in the context of social-ecological dynamics. Glob Environ Change 2014;28:109–19. 





[65] Kahan JH, Allen AC, George JK. An operational framework for resilience. J Homel Secur Emerg Manag 2009;6(1):1–48. 





[66] Labaka L, Hernantes J, Sarriegi JM. Resilience framework for critical infrastructures: an empirical study in a nuclear plant. Reliability Engineering and System Safety 2015 in Press. 





[67] J.P.G. Sterbenz, E.K. Cetinkaya, M.A. Hameed, A. Jabbar and J.P. Rohrer, Modeling and analysis of network resilience. In: Proceedings of the IEEE COMSNETS, Bangalore, India; 2011. 





[68] Vlacheas P, Stavroulaki V, Demestichas P, Cadzow S, Ikonomou D, Gorniak S. Towards end-to-end network resilience. Int J Crit Infrastruct Prot 2013;6(3– 4):159–78. 





[69] Bruyelle J-L, O’Neill C, EI-M E, Hamelin F, Sartori N, Khoudour L. Improving the resilience of metro vehicle and passengers for an effective emergency response to terrorist attacks. Saf Sci 2014;62:37–45. 





[70] Patterson ES, Woods DD, Roth EM, Cook RI, Robert L, Wears RL, et al. Three key levers for achieving resilience in medication delivery with information technology. J Patient Saf 2006;2(1):33–8. 





[71] Vugrin ED, Warren DE, Ehlen MA. Framework for infrastructure and Economic systems: quantitative and qualitative resilience analysis of petrochemical supply chains to a hurricane. Process Saf Prog 2011;30(3):280–90. 





[72] Shirali GHA, Motamedzade M, Mohammadfam I, Ebrahimipour V, Moghimbeigi A. Challenges in building resilience engineering (RE) and adaptive capacity: a field study in a chemical plant. Process Saf Environ Prot 2012;90:83–90. 





[73] Shirali GHA, Mohammadfam I, Motamedzade M, Ebrahimipour V. Moghimbeigi. Assessing resilience engineering based on safety culture and managerial factors. Process Safy Prog 2012;30(1):17–8. 





[74] Ainuddin S, Routray JK. Community resilience framework for an earthquake prone area in Baluchistan. Int J Disaster Risk Reduct 2012;2:25–36. 





[75] Madni AM, Jackson S. Towards a conceptual framework for resilience engineering. IEEE Syst J 2009;3(2):181–91. 





[76] Wright C, Kiparoglou V, Williams M, Hilton A. A framework for resilience thinking. Procedia Comput Sci 2012;8:45–52. 





[77] Limnios EAM, Mazzarol T, Ghadouani A, Schilizzi GM. The resilience architecture framework: for organizational archetypes. Eur Manag J 2014;32:104–16. 





[78] Eakin HC, Wehbe MB. Linking local vulnerability to system sustainability in a resilience framework: two cases from Latin America. Clim Change 2009;93:355–77. 





[79] Thomas S, Keegan C, Barry S, Layte R, Jowett M, Normand C. A framework for assessing health system resilience in an economic crisis: Ireland as a test case. BMC Health Serv Res 2013;13(450):1–8. 





[80] Abreu Saurin T, Cesar Carim G. A framework for identifying and analyzing sources of resilience and brittleness: a case study of two air taxi carriers. Int J Ind Ergon 2012;42:312–24. 





[81] Cutter SL, Berry M, Burton C, Evans E, Tate E, Webb JA. place based model for understanding community resilience to natural disasters. Glob Environ Change 2008;18(4):598–606. 





[82] Pettit TJ, Fiksel J, Croxton KL. Ensuring supply chain resilience: development of a conceptual framework. J Bus Logist 2010;31(1):1–21. 





[83] Shirali GA, Mohammadfam I, Ebrahimpour V. A new method for quantitative assessment of resilience engineering by PCA and NT approach: a case study in a process industry. Reliab Eng Syst Saf 2013;119:88–94. 





[84] Bruneau M, Chang SE, Eguchi RT, Lee GC, O’Rourke TD, Reinhorn AM, et al. A framework to quantitatively assess and enhance the science the seismic resilience of communities. Earthq Spectra 2003;19(4):733–52. 





[85] Nicholson CD, Barker K, Ramirez-Marquez JE. Vulnerability analysis for resilience-based network preparedness. Reliab Eng Syst Saf 2015;145:62–73. 





[86] Adams TM, Bekkem KR, Toledo-Duran EJ. Freight Resilience Measures. J Transp Eng 2012;138(11):1403–9. 





[87] Sahebjamnia N, Torabi SA, Mansouri SA. Integrated business continuity and disaster recovery planning: towards organizational resilience. Eur J Oper Res 2015;242(1):261–73. 





[88] Zobel CW. Representing perceived tradeoffs in defining disaster resilience. Decis Support Syst 2011;50(2):394–403. 





[89] Zobel CW, Khansa L. Characterizing multi-event disaster resilience. Comput Oper Res 2014;42:83–94. 





[90] Cox A, Prager F, Rose A. Transportation security and the role of resilience: a foundation for operational metrics. Transp Policy 2011;18(2):307–17. 





[91] Henry D, Ramirez-Marquez JE. Generic metrics and quantitative approaches for system resilience as a function of time. Reliab Eng Syst Saf 2012;99:114–22. 





[92] Barker K, Ramirez-Marquez JE, Rocco CM. Resilience-based network component importance measure. Reliab Eng Syst Saf 2013;117:89–97. 





[93] Pant R, Barker K, Ramirez-Marquez JE, Rocco CM. Stochastic measures of resilience and their application to container terminals. Comput Ind Eng 2014;70:183–94. 





[94] Baroud H, Ramirez-Marquez JE, Rocco CM. Importance measures for inland waterway network resilience. Transp Res E 2014;62:55–67. 





[95] Baroud H, Ramirez-Marquez JE, Barker K, Rocco CM. Measuring and planning for stochastic network resilience: application to waterway commodity flows. Risk Anal 2014;34(7):1317–35. 





[96] Wang JW, Gao F, Ip WH. Measurement of resilience and its application to enterprise information systems. Enterp Inf Syst 2010;4(2):215–23. 





[97] Omer M, Mostashari A, Lindemann U. Resilience analysis of soft infrastructure systems. Procedia Comput Sci 2014;28:565–74. 





[98] Chen L, Miller-Hooks E. Resilience: an indicator of recovery capability in intermodal freight transport. Transp Sci 2012;46(1):109–23. 





[99] Janic M. Modeling the resilience, friability and costs of an air transport network affected by a large-scale disruptive event. Transp Res A 2015;71:1–16. 





[100] Owin KH, Wardle DA. New indices for quantifying the resistance and resilience of soil biota to exogenous disturbances. Soil Biol Biochem 2004;26:1907–12. 





[101] Enjalbert S, Vanderhaegen F, Pichon M, Abel Ouedraogo K, Millot P. Assessment of transportation system resilience. In: Cacciabue C, Hjälmdahl M, Luedtke A, Riccioli C, editors. human modeling in assisted transportation. Springer-Verlag Italia Srl; 2011. p. 335–41. 





[102] Ouedraogo AK, Enjalbert S, Vanderhaegen F. How to learn from the resilience human-machine system? Eng Appl Artif Intell 2013;26(1):24–34. 





[103] Francis R, Bekera B. A metric and frameworks for resilience analysis of engineered and infrastructure systems. Reliab Eng Syst Saf 2014;12:90–103. 





[104] Cimellaro GP, Reinhorn AM, Bruneau M. Seismic resilience of a hospital system. Struct Infrastruct Eng 2010;6(1–2):127–44. 





[105] Chang SE, Shinozuka M. Measuring improvements in the disaster resilience of communities. Earthq Spectra 2004;20(3):739–55. 





[106] Ouyang M, Duenas-Osorio L, Min X. A three-stage resilience analysis framework for urban infrastructure systems. Struct Saf 2012;36–37:23–31. 





[107] Ayyub BM. Systems resilience for multihazard environments: definition, metrics, and valuation for decision making. Risk Anal 2014;34(2):340–55. 





[108] Hashimoto T. Reliability, resiliency, and vulnerability criteria for water resource system performance evaluation. Water Resour Res 1982;18 (1):14–20. 





[109] Franchin P, Cavalieri F. Probabilistic assessment of civil infrastructure resilience to earthquakes. Computer-Aided Civil and Infrastructure Engineering 2015;30(7):583–600. 





[110] Attoh-Okine NO, Cooper AT, Mensah SA. Formulation of resilience index of urban infrastructures using belief functions. IEEE Syst J 2009;3:2. 





[111] Faturechi R, Levenberg E, Miller-Hooks E. Evaluating and optimizing resilience of airport pavement networks. Comput Oper Res 2014;43:335–48. 





[112] Faturechi R, Miller-Hooks E. Travel time resilience of roadway networks under disaster. Transp Res B 2014;70:47–64. 





[113] Azadeh A, Salehi V, Ashjari B, Saberi M. Performance evaluation of integrated resilience engineering factors by data envelopment analysis: the case of a petrochemical plant. Process Saf Environ Prot 2014;92:231–41. 





[114] Jin JG, Tang LC, Sun L, Lee D-H. Enhancing metro network resilience via localized integration with bus services. Transp Res E 2014;63:17–30. 





[115] Cardoso SR, Barbosa-Povoas APFD, Relvas S, Novais AQ. Resilience assessment of supply chains under different types of disruption. Comput Aided Chem Eng 2014;34:759–64. 





[116] Khaled AA, Jin M, Clarke DB, Hoque MA. Train design and routing optimization for evaluating criticality of freight railroad infrastructures. Transp Res B 2015;71:71–84. 





[117] Vugrin ED, Turnquist MA, Brown NJK. Optimal recovery sequencing for enhanced resilience service restoration in transportation networks. Int J Crit Infrastruct 2014. 





[118] Ash J, Newth D. Optimizing complex networks for resilience against cascading failure. Phys: Stat Mech Appl 2007;380:673–83. 





[119] Hernandez-Fajardo I, Duenas_Osorio L. Probabilistic study of failures in complex interdependent lifeline systems. Reliab Eng Syst Saf 2013;111:260–72. 





[120] Cupac V, Lizier JT, Prokopenko M. Comparing dynamics of cascading failures between network-centric and power flow models. Electr. Power Energy Syst 2013;49:369–79. 





[121] Koc Y, Warnier M, Kooij RE, Brazier FMT. An entropy-based metric to quantify the robustness of power grids against cascading failures. Saf Sci 2013;59:126–34. 





[122] Su Z, Li L, Peng H, Kurths J, Xiao J, Yang Y. Robustness of interrelated traffic networks to cascading failures. Scientific Reports 2014;4:1–7. Article number: 5413. 





[123] Wang J, Jiang C, Qian J. Robustness of internet under targeted attack: a cascading failure perspective. J Netw Comput Appl 2014;40:97–104. 





[124] Ouyang M, Duenas-Osorio L. Multi-dimensional hurricane resilience assessment of electrical power systems. Struct Saf 2014;48:15–24. 





[125] Alderson DL, Brown GG, Carlyle WM. Assessing and improving operational resilience of critical infrastructures and other systems. Tutor Oper Res 2014:180–215. 





[126] Li Y, Zhao L. Analyzing deformation of supply chain resilient system based on cell resilience model. In: Li K, Fei M, Jia L, Irwin GW, editors. life system modeling and intelligent computing. Berlin Heidelberg: Springer-Verlag; 2010. p. 26–35. 





[127] Albores P, Shaw D. Government preparedness: using simulation to prepare for a terrorist attack. Comput Oper Res 2008;35:1924–43. 





[128] Carvalho H, Barroso AP, Machado VH, Azevedo A, Cruz-Machado V. Supply chain redesign for resilience using simulation. Comput Ind Eng 2012;62:329–41. 





[129] Virginia LM, Spiegler M, Naim MM, Wikner J. A control engineering approach to the assessment of supply chain resilience. Int J Prod Res 2012;50 (21):6162–87. 





[130] Jain SK, Bhunya PK. Reliability, resilience and vulnerability of a multipurpose storage reservoir. Hydrol Sci J 2010;53(2):434–47. 





[131] K. Adjetey-Bahun, B. Birregah, E. Chatelet, J.-L. Planchet, A simulation-based approach to quantifying resilience indicators in a mass transportation system. In: Proceedings of the 11th international ISCRAM conference, University Park, Pennsylvania; 2014. 





[132] Sterbenz JPG, Hutchison D, Cetinkaya EK, Jabbar A, Rohrer JP, Scholler M, et al. Resilience and survivability in communication networks: strategies, principles, and survey of disciplines. Comput Netw 2010;54:1245–65. 





[133] Aleksic A, Stefanovic M, Arsovski S, Tadic D. An assessment of organizational resilience potential in SMEs of the process industry, a fuzzy approach. J Loss Prev Process Ind 2013;26(6):1238–45. 





[134] Azadeh A, Salehi V, Arvan M, Dolatkhah M. Assessment of resilience engineering factors in high-risk environments by fuzzy cognitive maps: a petrochemical plant. Saf Sci 2014;68:99–107. 





[135] Muller G. Fuzzy architecture assessment for critical infrastructure resilience. Procedia Comput Sci 2012;12:367–72. 





[136] Tadic D, Aleksic A, Stefanovic M, Arsovski S. Evaluation and ranking of organizational resilience factors by using a two-step fuzzy AHP and fuzzy TOPSIS. Math Probl Eng 2014:1–13. 





[137] Nurre SG, Cavdaroglu B, Mitchell JE, Sharkey TC, Wallace WA. Restoring infrastructure systems: An integrated network design and scheduling (INDS) problem. Eur J Oper Res. 2012;223:794–806. 





[138] Rinaldi SM, Peerenboom JP, Kelly TK. Identifying, understanding and analyzing critical infrastructure interdependencies. IEEE Control Syst Mag 2001;25 (6):11–25. 





[139] Holden R, Val DV, Burkhard R, Nodwell S. A network flow model for interdependent infrastructures at the local scale. Saf Sci 2013;53(1):51–60. 





[140] Ouyang M, Hong L, Mao Z-J, Yu M-H, Qi F. A methodological approach to analyze vulnerability of infrastructures. Simul Model Pract Theory 2009;17 (5):817–28. 





[141] 〈http://www.nist.gov/el/building_materials/resilience/guide.cfm〉. 





[142] Kelly C, Ferrara A, Wilson GA, Ripullone F, Nole A, Harmer N, et al. Community resilience and land degradation in forest and shrubland socioecological systems: evidence from Gorgoglione, Basilicata, Italy. Land Use Policy 2015;46:11–20. 





[143] Pant R, Barker K, Zobel CW. Static and dynamic metrics of economic resilience for interdependent infrastructure and industry sectors. Reliab Eng Syst Saf 2014:92–102. 





[144] Lunday BJ, Sherali HD. Network interdiction to minimize the maximum probability of evasion with synergy between applied resources. Ann Oper Res 2012;196(1):411–42. 

