# Optimisation in research ENEL445

*Converted from PDF: Optimisation in research ENEL445.pdf*

---

## Page 1

Optimisation in my research
Jeremy Watson

![Page 1](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_001.png)

---

## Page 2

Overview
• My research has used optimisation in a number of ways:
• Distributed optimisation and control algorithms for power systems (main 
focus today)
• Linear Matrix Inequalities (LMIs) for control synthesis*
• Optimal power-flow in unbalanced low-voltage distribution networks*
(*slides at the end if anyone is interested)

![Page 2](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_002.png)

---

## Page 3

Distributed optimisation / control 
• Main idea: 
• each agent / device / system controls its own variables (typically state 
variables of that system which are also design variables of an optimisation 
problem) 
• by low band-width, distributed communication with other local agents, these 
variables are updated until the global optimisation problem is solved.
• this can allow large-scale optimisation problems to be solved automatically by 
simple controllers at each device as opposed to solving the problem centrally 
at high computational cost and broadcasting the solution to each device. 
• already used (wide range of applications) in industry, although not especially 
common. 
• potential applications (mostly in the future) include coordination of UAVs, 
self-driving vehicle platoons, smart grid, etc.

![Page 3](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_003.png)

---

## Page 4

Distributed optimization / control
• Research areas:
• Improving convergence rates and properties (e.g. ADMM is one of the best 
recent algorithms)
• Coping with enforced dynamics in each agent. Agents typically have their own 
application-specific dynamics which may not be easy to control.
• Cyber-security – what happens if one or more devices are adversely 
controlled or deliberating send false data?
• Coping with time delays and/or noise in communication
• Stochastic networks – i.e. random communication failures, etc. – what can the 
distributed 
• Hybrid approaches using some form of reinforcement learning as well.

![Page 4](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_004.png)

---

## Page 5

Application to power systems
• replace optimal power-flow and frequency control with distributed 
optimisation & control
• each generator has a controller that guides its power setpoints to the 
(true) OPF setpoint, based on communication with neighbours.
• not really needed in the power system of today, but potential for 
implementation in future grids / microgrids

![Page 5](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_005.png)

---

## Page 6

• Consider a separable cost function for a network of agents
• Constraint: at steady-state, each agent must have the same value of 
the state variable (this is called a consensus problem). Typically this is 
something like a market price or (scaled) power output, etc.
Intro to distributed optimisation / control
i = agent i
xi = state of agent i
V = set of agents
Fi(xi) = cost function of agent i
Communication network matrix

![Page 6](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_006.png)

---

## Page 7

Intro to distributed optimisation / control
• KKT conditions for optimality
Results also exist for cost functions which 
are not strictly convex, but not in all cases 
and not with the same simplicity
Guaranteed stability & optimality!!

![Page 7](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_007.png)

---

## Page 8

Primal-dual secondary frequency control with delays 
(IEEE Trans. Automatic Control 2024)
Results (IEEE 39 system) with 20ms communication delays
Traditional controller
Our proposed controller
Results (IEEE 39 system) with noisy measurements (SNR = 20dB)
Our proposed controller
Traditional controller
Idea: transform the communicated variables to 
allow noise resistance + delay robustness
Transformations

![Page 8](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_008.png)

---

## Page 9

Distributed Averaging
Proportional-Integral
Controller
Distributed secondary control for hybrid AC/DC grids
(IEEE Trans. Control Systems 2021)
Case study
Traditional controller
Our proposed controller
Optimisation formulation
Idea: implement a similar form of distributed optimisation
 on hybrid AC/DC power grids
 
System dynamics
Control + Optimisation 
theory used to prove 
stability and optimality

![Page 9](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_009.png)

---

## Page 10

Linear Matrix Inequalities
• State-of-the-art linear control techniques are usually based on Linear 
Matrix Inequalities (LMIs), where the control gains are the solution to 
a linear optimisation problem. Examples:
• LQR (Riccati equations are LMIs)
• Model predictive control
• H-infinity, H2 control
• Passivity-based control
• Stability analysis
• Further reading (if interested): https://web.stanford.edu/~boyd/lmibook/lmibook.pdf

![Page 10](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_010.png)

---

## Page 11

Data-driven control 
(Trickett, PMAPS 2024)
Scalable microgrid control 
(IEEE Trans. Smart Grid 2021)
Formulation
System
Performance
Formulation
System
Performance
Inverse optimal and passivity-based control 
(Hallinan, IEEE CDC 2023)
Formulation
Performance
System

![Page 11](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_011.png)

---

## Page 12

Unbalanced optimal power-flow
• Back in 2017, optimal power-flow for unbalanced networks was 
mostly unexplored. 
• Published in IEEE Trans. Sustainable Energy.
22% reduction in energy losses
Results
Less computational expense
Formulation
Convexified
constraints
Small approximation error
Case study

![Page 12](../course.material/figs/Optimisation%20in%20research%20ENEL445/page_012.png)

---

