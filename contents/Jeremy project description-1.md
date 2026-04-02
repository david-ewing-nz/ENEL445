# Jeremy project description-1

*Converted from PDF: Jeremy project description-1.pdf*

---

## Page 1

Chapter 6
Design Projects
6.1
Suggested Project l: Power system optimization
Brief highlights
Solve
relatively realistic power systems optimisation problem
Compete with YOur classmates for the
solution
bonus marks awarded) _
MATLAB
O1'
Python
software  used;
evaluation and (sub-optimal) solution code
provided as
starting point.
High flexibility:
wide range of possible approaches are possible
6.1.1
Introduction
In this assigument, VOur task
will be t0
design
function to optimize the
build and
operation of generation
and storage if so desired) for & given pOwer system:
The aim is
to maximize cash (i.e   profits plus any starting cash left unused; excluding asset value)
at the end of a year-long simulation:
In the build stage, vour programme will be given details of the system and parameters
for each type of generation and decide what to build:
In the operation stage, YOur second
module will decide how much generation (of each type) to supply to the system for each
hourly time period.
MATLAB and Python code to
run the year-long simulation is providled on
with
an example (sub-optimal) solution_
Either language is fully acceptable and
will result in equivalent performance in the final evaluation_
Those exceedingly short f
time have the option only to optimize the build process while
the given operation
code.
Such solutions should not expect the very highest marks, but
result is still
possible_
The following sections explain the problem in detail.
However, please note that the
code and associated comments mnay explain the problem more clearly than any written
text.
It is also
not necessary
t0
understand the simulation detail
below
one could
modily the provided code into an objective function and optimize the any/all parameters
by any appropriate method without using intuition O Other knowledge
49
best
Learn.
along
using
good

![Page 1](../course.material/figs/Jeremy%20project%20description-1/page_001.png)

---

## Page 2

50
CHAPTER 6.
DESIGN PROJECTS
Generation
Build cost
$ millions
MW
Capacity [actor
Wind
N (1.1,
0.112)
Uniform
[0 507]
Geothermal
N(4.8 0.482
100%
Hydro
N(2.8,
0.282
N (45% ,
4.592
Solar
N(0.8,
0.082
Average 24.587
Table 6.1: Generation options
6.1.2
Notation
We will denote a Gaussian random variable X with mean /4 and standlard deviation
by
X ~N(p; 02)
6.1.3
Problem formulation
Generation options
Four generation options are provided:
Wind is modelled by
a random wind capacity factor
0.00 to 0.50
i.e.
the
available wind power ranges rom 0 to 50% of built capacity (uniform distribution)_
This value changes at each time period
Hydro is fully coutrollable up to its rated power.
However; the overall capacity
factor throughout the year is limited to a constant value which is set for each year-
long simulation via a Gaussian random variable with 0.45 mean and 0.045 standard
deviation:
When the cumulative total of hydro exports reaches this nuber,
it is
assumed that the hydro generator is out of water and
n0 further   generation is
permitted.
For simplicity; in-flows and out-flows etc.
are not explicitly modelled:
Geothermal is fully controllable up to its rated powCr _
Solar is modelled by
24-hour
capacity factor from 0.00 to 0.80 with 20%
multiplicative randomness at cach time period
uniform distribution).
Full details
are given in the provided code
Table 6.1 shows the parameters for each generation option.
Each Gaussian random
variable has 10% standard deviation. Each uniform random variable is given bounds.
Storage
Battery storage is available with the following parameters:
The cost is S150,000 per MWh.
This is randomized for each vear-long simulation
via a Gaussian random variable with 10% standard deviation_
It is assumed that the rated power in MW is equal to the rated capacity in MWh
i.e.
charge
discharge time of one hour_
One-way efficiency is 97.59.
The usable state-of-charge is from 0% to 100F.
Batteries are fully charged at the start of the simulation.
from
cycle

![Page 2](../course.material/figs/Jeremy%20project%20description-1/page_002.png)

---

## Page 3

6.1.
SUGGESTED PROJECT 1: POWER SYSTEM OPTIMIZATION
51
Load
The system mean load
is chosen randomly for each year-long simulation, uniformly
distributed between [1000.2000] MW
For each time-period, the load at that time period
is a Gaussian random variable with the mean as chosen above and
standard deviation
of 500 MW_
i.e. load(t)
N(Lavg,
5002
MW.
Pricing
The market price will be set by the following formula at each time period t:
base_price(t)
base
ce_average
base_price_average/1O*randn
price(t)
base_price(t)
load(t)*priceCoefficientl
wind_capacity_factor(t) *priceCoefficient2
where base_price_average
N(150,
152) , priceCoefficient1
N(0.075, 0.00752) ,
and
ceCoefficient2
N(150,
152
are chosen randomly for each year-long simula-
tion. This price (in $ per MWh) will be multiplied by the amount (in MWh) you decide
to generate; and the result added to VOur funds_
If vour programme does not return suflicient generation;
the interface will penalize
this as follows:
A shortfall of up to external
MWs (t) will be purchased at market price_
Any further shortfall cannot be
supplied and
a penalty cost of S1OOO per MWh will
be deducted from your funds
If Your programme returns excess generation, this is curtailed
spilled for free.
6.1.4
Solution
methodology
Possible approaches include gradient-based methods; particle swarm optimization; neural
networks; etc.
Computational time may
be
limitation, and it will be imperative to
explain YOur approach and desigu choices clearly:
A solution has two parts:
A module build_plants () to decide how much of each type of power plant to build
at the start of each year-E
simulation
The interface will check if the proposed
build is feasible, and throw an error if not _
2
A module operate_plants () to decide how much generation of each type to offer
at each time-step_
For solar; wind and geothermal generation, this is trivial as there
is no benefit to reducing output (since curtailment is free). However , it is non-trivial
to work out when battery storage should
Or
discharge; and
given the finite
amount of hydro energy
when to use hydro to avoid short falls_
Only
few constraints are placed upon your solution:
No forecast O future information will be given; i.e. at a time period T , information
from
a future
time-step t > T will not be known
Lavg
-pric
pric
-long
charge

![Page 3](../course.material/figs/Jeremy%20project%20description-1/page_003.png)

---

## Page 4

52
CHAPTER 6.
DESIGN PROJECTS
operate_plants () should execute in less than lms on a standard computer in the
compute lab:
If vour code is close to this
this should not be
an
issue in most
cases) , please time YOur code and include the info in YOur report _
You may use any
method,
e.g.
(https
/au.mathworks
com/help/matlab/ref/timeit.html)
Or
the Profiler tool in MATLAB, O profile 01 cProfile in Python_
build_plants ()
should execute in less than ls
on
standard computer in the
computer lab
If your code is close to this (this should not be
an issue in most
cases) . please time YOur code and include the info in YOur report . You may use any
method as per the above
In order to get You started, & demonstration solution has been provided:
build_plants () spends 20% of its money buildling each of wind, geothermal, hydro,
solar, and battery storage, regardless of given costs and other parameters
This is
far from optimal.
operate_plants ()
uses simple logic to avoid a shortfall whenever possible.  Wind;
solar and geothermal generations
are
run at their maximum available capacity at
that point in time_
If there is still a shortfall, any hydro generation is used to cover
the shortfall,and if there is still a shortfall, any stored energy in the battery is used
to reduce or (if possible)
the shortfall.
There is also consicerable room for
improvement in this module_
Hints
Not all the starting funds need to be used building generation and/O storage. Since
the objective is to mnaximize cash at the end of one year; it may be beneficial to
under-invest. Any unused starting funds will be added to Your cash
at the end
to make your final score_
Because there are penalties for failing to supply load
as in the real world) , it may
be beneficial to have a mnix of generation and/or storage
The ideal mix of generation and 
O1" storage is likely to depend o1 the loading; costs,
and capacity factors which are randomized each year-long simulation:
You may wish
to adjust YOur' build plans based on this info which is passed to build_plants ()
as
opposed to sticking to fixed proportions pCr the demo solution
As is often the case for pOwcr system optimization problems, the global optimization
problem may be computationally impractical to solve. Firstly, there are & number
of stochastic (random) variables, the exact value of which is not known in advance_
Secondly; there
are 8760 time periods; and for each time period, generation
storage
MW contributions
are
design variables (i.e.
they need to be optimized)
potentially resulting in
over"  40,000 design variables and
even
more
constraints_
Hence, it may be helpful to look for ways to simplify O decompose the problem_
6.1.5
Deliverables
The progress report should cover the following:
little background
intuition about
the problem;
short overview of possible methods to use for the problem;
plan for
avoic
flow

![Page 4](../course.material/figs/Jeremy%20project%20description-1/page_004.png)

---

## Page 5

6.1.
SUGGESTED PROJECT 1: POWER SYSTEM OPTIMIZATION
53
Item
Weight
Presentation
0.25
Quality of the technical design
0.50
Performance
0.25
Table 6.2: Final report
marking
vour solution; any progress-to-date
It is very easy to find
solution; even by trial and
erTor, better than the given starting solution, so it is expected to show some preliminary
improvement by the time of the progress report_
The final report should explain Your solution in-depth (see below), and be accompa-
nied by the MATLAB or Python code used to implement YOur solution. Please email this
to me at jeremy watson@canterburyac.nz O1" upload to the Learn dropbox.
Your solution
will be tested in the given environment and (per the next section) somne marks will be
awarded for performance_
6.1.6
Marking
The final report will be assessed as in Table 6.2:
Guidelines
Please take note of the following:
Presentation: Reports should be tidy and concise.
Use graphs
figures as appropriate
to illustrate your solution:   Any format is acceptable
although IEEE conference format
(https:
WWW
org/conferences/publishing/templates html) is suggested.
It is impor-
tant to focus on the parts you developed;
as
opposed to explaining the problem and/or
provicled code.
Quality of the technical design:
Explain
what methods vou tried and justify vour
final choice.
Solutions which attempt t0 Optimize both the build and operation process
are
encouraged, and should demonstrate benefit compared to only optimizing the build
using the provided operation code. Comparisons of different optimisation approaches are
encouraged.
Performance:
you should test your code with the provided evaluation function (0n
LEARN) and report its score in  VOUr final report_
I will independently evaluate vour
solution by changing the rng seed and running the simulation with totalSimulations
to 100,
which the average score will be taken.
Marks  will
be awarded as
follows:
The best solution from the class will score full marks for this section, so
as it
achieves
score of $6.5 billion or better_
Marks thereafter will be awarded based
O11 the average score, using linear inter-
polation where the best score is 100 % and the class median score is set at 70%.
However, regardless of this calculation;
n0
negative marks will be awarded; all com-
plete and working solutions better than the starting solution will score at least 30%
for this section_
ieeeS
from
equal
long

![Page 5](../course.material/figs/Jeremy%20project%20description-1/page_005.png)

---

## Page 6

54
CHAPTER 6.
DESIGN PROJECTS
Bonus marks of 10% (of the marks assigned to performance)
will be awarded for
any solution which outperforms my
own sub-optimal solution_
If this results in
mark exceeding 100%, the mark will not be capped.

![Page 6](../course.material/figs/Jeremy%20project%20description-1/page_006.png)

---

