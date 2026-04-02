# Applied Engineering Optimisation - Power Systems Optimisation for Learn v4-2

*Converted from PDF: Applied Engineering Optimisation - Power Systems Optimisation for Learn v4-2.pdf*

---

## Page 1

Applied Engineering 
Optimisation
ENEL445

![Page 1](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_001.png)

---

## Page 2

Power Systems Optimisation
• Term 2 of ENEL445: applications, nature-
inspired/evolutionary optimisation.
• This week, I’ll give a brief (and not too difficult) 
overview of optimization in power systems. We’ll 
look at what is used in industry + a brief discussion 
of future trends. 
• Even if you aren’t interested in power systems, treat this 
as an illustrative example.

![Page 2](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_002.png)

---

## Page 3

Q: How is optimization used in 
power systems?
• Economic dispatch / Optimal power flow (OPF)
• Power system state estimation
• Also: load forecasting, optimal / model-predictive 
control of power electronics, scheduling / energy 
management / demand response, etc. 
• The latter (energy management) is a highly important 
aspect and links to both forecasting and the optimal 
power flow problem.

![Page 3](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_003.png)

---

## Page 4

Economic dispatch
• Used in many power markets, e.g. European Power 
Exchange (EPEX) etc, NZ Electricity Market (until 
Nov 2022).
• Supply must meet demand, as cheaply as possible, 
subject to generator limits. 
• Does not consider any network flows, losses, or 
network constraints. (Although, penalty factors -
more on this later - may be used to approximate 
the effect of losses).

![Page 4](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_004.png)

---

## Page 5

Formulation
Classification:
Confidence

![Page 5](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_005.png)

---

## Page 6

Solving the economic dispatch 
problem
• In the linear case, “merit order” techniques can easily 
solve the economic dispatch problem, e.g.
• In the non-linear case? Use constrained optimisation 
techniques!

![Page 6](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_006.png)

---

## Page 7

Economic Dispatch Example
D
1
2
2
1
1
1
1
2
2
2
2
2
1
1
1
What is economic dispatch for a two generator 
system P
500 MW  and
(
)
1000 20
0.01
$/
(
)
400 15
0.03
$/
Using the Largrange multiplier method we know
(
)
20
0
G
G
G
G
G
G
G
G
G
G
P
P
C P
P
P
hr
C
P
P
P
hr
dC P
dP

=
+
=
=
+
+
=
+
+
−
=
+
1
2
2
2
2
1
2
.02
0
(
)
15
0.06
0
500
0
G
G
G
G
G
G
P
dC
P
P
dP
P
P



−
=
−
=
+
−
=
−
−
=

![Page 7](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_007.png)

---

## Page 8

Economic Dispatch Example, cont’d

![Page 8](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_008.png)

---

## Page 9

Inclusion of Transmission Losses
• The losses on the transmission system are a function 
of the generation dispatch.  In general, using 
generators closer to the load results in lower losses
• This impact on losses should be included when 
doing the economic dispatch
• Losses can be included by slightly rewriting the 
Lagrangian:
G
1
1
L(
, )
(
)
(
(
)
)   
m
m
i
Gi
D
L
G
Gi
i
i
C P
P
P P
P


=
=
=
+
+
−


P

![Page 9](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_009.png)

---

## Page 10

Impact of Transmission Losses
G
1
1
G
This small change then impacts the necessary
conditions for an optimal economic dispatch
L(
, )
(
)
(
(
)
)   
The necessary conditions for a minimum are now
L(
, )
(
)
m
m
i
Gi
D
L
G
Gi
i
i
i
Gi
Gi
C P
P
P P
P
dC P
P
d



=
=
=
+
+
−

=



P
P
1
(
)
(1
)
0  
(
)
0
L
G
Gi
Gi
m
D
L
G
Gi
i
P P
P
P
P
P P
P

=

−
−
=

+
−
=


![Page 10](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_010.png)

---

## Page 11

Impact of Transmission Losses
th
i
i
Solving each equation for  we get
(
)
(
)
(1
0  
(
)
1
(
)
1
Define the penalty factor L  for the i  generator
1
L
(
)
1
i
Gi
L
G
Gi
Gi
i
Gi
Gi
L
G
Gi
L
G
Gi
dC P
P P
dP
P
dC P
dP
P P
P
P P
P




−
−
=

= 


−





= 


−






![Page 11](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_011.png)

---

## Page 12

Impact of Transmission Losses
1
1
1
2
2
2
i
Gi
The condition for optimal dispatch with losses is then
(
)
(
)
(
)
1
Since L
 if increasing P  increases
(
)
1
(
)
the losses then 
0
1.0
This makes generator
G
G
m
m
Gm
L
G
Gi
L
G
i
Gi
L IC P
L IC
P
L IC
P
P P
P
P P
L
P

=
=
=
= 


−







→


i
 i appear to be more expensive
(i.e., it is penalized).  Likewise L
1.0 makes a generator
appear less expensive.  


![Page 12](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_012.png)

---

## Page 13

Calculation of Penalty Factors
i
Gi
Unfortunately, the analytic calculation of L  is 
somewhat involved.  The problem is a small change
in the generation at P  impacts the flows and hence
the losses throughout the entire system.  However,
Gi
 
using a power flow you can approximate this function 
by making a small change to P  and then seeing how
the losses change:  
(
)
(
)
1
(
)
1
L
G
L
G
i
L
G
Gi
Gi
Gi
P P
P P
L
P P
P
P
P







−


![Page 13](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_013.png)

---

## Page 14

Two Bus Penalty Factor Example

![Page 14](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_014.png)

---

## Page 15

Variants
• The two main alternatives are: uniform pricing (e.g. 
NZ) or pay-as-bid (UK). 
• Uniform pricing (sometimes called pay-as-cleared): 
every generator whose bid is accepted is paid the 
marginal price (market price in previous slide).
• Pay-as-bid: every generator whose bid is accepted is 
paid the price of their bid.
• Can you think of advantages / disadvantages of 
either?

![Page 15](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_015.png)

---

## Page 16

Optimal power flow
• Given a power system, i.e. a network of generators, 
power lines, transformers, buses (nodes), and loads 
…
• Objective: meet demands at minimum cost
• Cost: generation costs 
• Constraints: Power flows follow the laws of physics, 
limits on equipment etc.

![Page 16](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_016.png)

---

## Page 17

Optimal power flow
• If there are no system constraints, the solution is 
the same as Economic Dispatch. 
• Recall (if you did ENEL382) the power flow 
equations. Let’s formulate the optimal power flow 
problem:

![Page 17](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_017.png)

---

## Page 18

*[Page appears blank or contains only images]*

![Page 18](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_018.png)

---

## Page 19

25,000 buses
32,230 branches
4,834 generators
Q: how long to solve?

![Page 19](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_019.png)

---

## Page 20

Optimal power-flow
• Due to the complexity of the non-linear problem 
we have posed, most commercial packages and 
power system operators use a simplified version 
called (mis-named) DC optimal power flow. 
• In the cases where the full AC OPF is solved, by far 
the best algorithm in practice are interior-point 
solvers.
• Recent studies e.g. by the FERC in the US suggest 
that a 5-10% reduction of costs could be saved if it 
were computationally practical to run a full AC OPF.

![Page 20](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_020.png)

---

## Page 21

DC power flow
Classification:
Confidence

![Page 21](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_021.png)

---

## Page 22

DC optimal power flow
•
As an example, let’s look at Transpower’s DC OPF (solved every 5 minutes for 
real-time dispatch) here

![Page 22](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_022.png)

---

## Page 23

DC optimal power flow
• Possible improvements:
• If we have a better estimate of the voltages, we can use 
them (constants) instead of 1 p.u. 
• Estimate of losses –  typical method: 
• Power flows are calculated via the DC power flow equations
• An approx. current can be estimated from this (assume 1 p.u. 
voltage)
• The resistance of the line – ignored so far – is used to calculate 
I2R losses. 
• However, the squaring of the current would create a nonlinear 
equality constraint - not a linear problem any more – so a 
piecewise linear approximation is typically used.

![Page 23](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_023.png)

---

## Page 24

DC optimal power flow
• After a solution from the DC OPF is found, a 
standard AC power flow (note, not OPF) is usually 
run to ensure the solution is feasible.

![Page 24](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_024.png)

---

## Page 25

OPF types
General
Problem name
Includes
Includes
Includes
Includes
Assumptions
Includes
Includes
problem
voltage angle
bus voltage
transmission
losses?
generator
contingency
type
constraints?
magnitude
constraints?
costs?
constraints?
constraints?
OPF
ACOPF, or Full
Yes
Yes
Yes
Yes
Yes
No
ACOPF
OPF
DCOPF
No
No; all
Yes
Maybe
Voltage magnitudes are
Yes
No
voltage
constant
magnitudes
fixed
OPF
Decoupled OPF
Yes
Yes
Yes
Yes
Power-voltage angle are
Yes
No
independent of voltage
magnitude-reactive
power
OPF
Security-
Yes
No
Yes
Yes
Voltage magnitudes are
Yes
Yes
Constrained
constant
Economic
Dispatch (SCED)
Power
Power Flow, or
No, but can be
Yes
No, but can
Yes
No
No
flow
Load Flow
added
be added
Economic
Economic
No
No
No
Depends
No transmission
No
dispatch
Dispatch
constraints
OPF
Security
Yes
Depends
Yes
Yes
Depends
Yes
Yes
Constrained OPF
(SCOPF)
Classification:
Confidence
Yes

![Page 25](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_025.png)

---

## Page 26

Security-constrained OPF
• Idea: power system dispatch not only has to allow a 
feasible solution, but also has to satisfy contingency 
constraints – e.g. if something plausible-but-
unexpected happens, the system has to stay within 
operational limits.  
• This is orders of magnitude more expensive than 
even AC OPF, as the full set of constraints for every 
contingency needs to be added!

![Page 26](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_026.png)

---

## Page 27

Security-constrained OPF
• What happens in practice is that the DC OPF is 
solved, and the solution checked against a subset 
of contingencies (note: this is not solving another 
OPF but simply plugging the DC OPF solution into a 
simplified SCOPF and checking for feasibility).
• If the solution is not SCOPF-feasible, heuristic 
constraints are used to add security and the DC 
OPF is re-solved, etc. until a SCOPF feasible solution 
is found.

![Page 27](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_027.png)

---

## Page 28

Locational marginal pricing
• The OPF can be (and is) used to calculate nodal 
prices (locational marginal prices), for example in 
NZ. 
• As before, the Lagrange multipliers represent prices 
and these are affected by losses, security 
constraints, etc.

![Page 28](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_028.png)

---

## Page 29

Summary
• One of the main uses of optimisation in power 
systems is in optimising dispatch (i.e. the power of 
each generator). 
• Due to computational complexity of the AC OPF / 
SCOPF, the DC OPF is almost always used in 
industry, but this may change in the next few 
decades.

![Page 29](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_029.png)

---

## Page 30

Power system state estimation
• Main idea – work out a best estimate of the states 
(voltages, currents, power flows) of the power system 
based on available measurements. 
• Could do power-flow but in reality:
• Might not have 2 measurements per bus (remember 
ENEL382)
• Any error is likely to result in non-convergence or useless 
results
• Power flow cannot integrate measurements such as P & Q 
line flows. 
• Widely used in the power industry – it is important to 
know what’s happening in the system.
• Often linked to the SCADA / EMSE system.

![Page 30](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_030.png)

---

## Page 31

Formulating state estimation as 
an optimisation problem
• For simplicity we’ll use the DC power flow 
equations we derived earlier this week.
• Unlike the Optimal Power Flow case, commercial 
products do run the full AC power-flow equations 
instead of the “DC” power flow approximation.

![Page 31](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_031.png)

---

## Page 32

Example (from Wood / 
Wallenberg, chapter 9)

![Page 32](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_032.png)

---

## Page 33

*[Page appears blank or contains only images]*

![Page 33](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_033.png)

---

## Page 34

Power system state estimation
• Different meters have different accuracy, so a basic 
idea is a weighted least-squares formulation. We’ll 
go through this (which is the basis for most state 
estimators in industry).

![Page 34](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_034.png)

---

## Page 35

Formulating state estimation as a 
weighted least-squares problem

![Page 35](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_035.png)

---

## Page 36

Formulating state estimation as a 
weighted least-squares problem

![Page 36](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_036.png)

---

## Page 37

Formulating state estimation as a 
weighted least-squares problem

![Page 37](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_037.png)

---

## Page 38

Formulating state estimation as a 
weighted least-squares problem

![Page 38](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_038.png)

---

## Page 39

Power system state estimation
• In power system state estimation, 
underdetermined problems are not solved. 
• Instead, “pseudo-measurements” are added to the 
measurement set to give a completely determined 
or over-determined problem. 
• These pseudo-measurements in the past were 
obtained by telephone call to the generator 
operators! They can also be based on historical / 
previous measurements. A large standard deviation 
is assigned as we have little confidence in the 
“pseudo-measurement”.

![Page 39](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_039.png)

---

## Page 40

Example (from Wood / 
Wallenberg, chapter 9)

![Page 40](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_040.png)

---

## Page 41

Example
Classification:
Confidence

![Page 41](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_041.png)

---

## Page 42

Example
Classification:
Confidence

![Page 42](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_042.png)

---

## Page 43

Practical considerations
• Generally, the nonlinear AC power-flow equations are 
solved. A common method is to use Newton’s method. 
• Phasor Measurement Units using GPS synchronization 
are becoming increasingly common and improving 
state estimation accuracy – but the state estimation 
problem is also getting harder due to inverter-based 
resources.
• More advanced topics:
• New algorithms to cope without enough measurements (in 
general: more generators = more measurements required), or 
without exact network data. 
• Detecting and removing bad data.

![Page 43](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_043.png)

---

## Page 44

How it all fits together
SYSTEM MODEL DESCRIPTION
BREAKERISWITCH
STATUS
DISPLAY TO
INDICATIONS
NETWORK
OPERATOR
TOPOLOGY
PROGRAM
UPDATED SYSTEM
POWER FLOWS
ELECTRICAL
STATE
VOLTAGES; ETC
MODEL
ESTIMATOR
TELEMETAY
DISPLAY TO
ANALOG MEASUREMENTS
OPERATOR
COMMUNICATIONS
EQUIPMENT
GENERATOR
BAD
OUTPUTS
MEASUREMENT
GENERATION
ALAAMS
RAISEILOWER
SIGNALS
AGC
STATE ESTIMATOR
OUTPUT
BASE POINTS AND
REMOTE
PARTICIPATION
TEAMINAL
FACTORS
UNITS IN
SUBSTATIONS
ECONOMIC
DISPATCH
PENALTY
CALCULATION
FACTOR
BASE POINTS,
CALCULATION
PARTICIPATION
FACTORS; OPTIMAL
VOLTAGE, TRANSFORMERI
TAPS; LOAD SHEDDING
OpF
SECURITY
CONTINGENCY
CONTINGENCY
CONSTRAINED
OPF
ANALYSIS
POTENTIAL
SELECTION
OVERLOAD
OVEALOADS
& VOLTAGE
& VOLTAGE
PROBLEMS
PROBLEMS
DISPLAY ALARMS
Classification:
Confidence

![Page 44](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_044.png)

---

## Page 45

Power system state estimation
• Further resources:
• Wood / Wallenberg textbook
• More detailed lecture notes: 
http://www.ee.unlv.edu/~eebag/State%20Estimation.pd
f
• https://www.kth.se/social/upload/518a08d3f276547862
95ca51/Lecture_15_StateEstimation.pdf
• https://ieeexplore.ieee.org/document/4596092 (New 
England example)
• https://home.engineering.iastate.edu/~jdm/ee553/SE1.
pdf 
• Lots of journal and conference papers on IEEE, etc.

![Page 45](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20Power%20Systems%20Optimisation%20for%20Learn%20v4-2/page_045.png)

---

