# T2-6 Simulated annealing-annotated-1

*Converted from PDF: T2-6 Simulated annealing-annotated-1.pdf*

---

## Page 1

Simulated Annealing
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_001.png)

---

## Page 2

Outline
●Introduction to Statistical Mechanics
●Simulated Annealing
●Applications

![Page 2](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_002.png)

---

## Page 3

Statistical Mechanics

![Page 3](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_003.png)

---

## Page 4

●
A box with 100 identical 
coins.
●
Shake it.
●
Some will end up heads, 
some tails.
●
Assume each of these 
different configurations is 
equally likely.
Statistical Mechanics
100
30
210

![Page 4](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_004.png)

---

## Page 5

Statistical Mechanics
HHTHTT…
50 heads, 50 tails
THTTHH…
53 heads, 47 tails
HTTTTH…
90 heads, 10 tails
HHHHHH…
100 heads, 0 tails
●
The system could be described by a very large number of 
equally likely microstates.
●
What we actually measure is the macrostates of the system, 
which are not equally likely.
 
"Cr=
microstates
macrostates
29
- 35
!-
10
ID
50 ! (100
- 50) !
- 3D
100 !
28
10
=
347 ! 8410
-30
10
los !
13
-
2x10
- 30
90 ! Is!
IC
on

![Page 5](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_005.png)

---

## Page 6

Statistical Mechanics
●
Microstates - position of particles, velocity of particles
●
Macrostates - pressure, temperature, volume, density
●
The most likely macrostate that the system will find itself in is 
the one that corresponds to the largest number of microstates.
●
In general it is impossible to measure which microstate a 
realistic system is in. It is only possible to measure the 
macrostate of the system.
X Hard to
measure
- Easier
to
meas
Arrow of
time

![Page 6](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_006.png)

---

## Page 7

A Statistical Definition of Temperature
●
Two systems are in thermal contact with each other but 
thermally isolated from their surroundings:
●
The ith system has energy Ei and can be in any one of Ωi(Ei) 
microstates.
●
The whole system (two systems combined) can be in any one 
of Ω1(E1)Ω2(E2) microstates.
●
The systems are able to exchange energy with each other 
and we will assume that they have been joined together for a 
sufficiently long time that they have come into thermal 
equilibrium (E1 and E2 have fixed values.)
T

![Page 7](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_007.png)

---

## Page 8

A Statistical Definition of Temperature
●
Crucial insight: A system will appear to choose a macroscopic 
configuration that maximises the number of microstates.
●
Based on the following assumptions:
■
Each one of the possible microstates is equally likely.
■
The system’s internal dynamics are such that the 
microstates of the system are continually changing.
■
Eventually, the system will explore all possible 
microstates and spend an equal time in each of them
●
The system will most likely be found in a configuration that is 
represented by the most number of microstates.
“For a large system, ‘most likely’ becomes overwhelmingly likely.. to 
the level where it becomes an utterly reliable prediction on whose basis 
you can design an aircraft engine and trust your life to it! ”
Concepts in Thermal Physics S. J. Blundell and K. M. Blundell

![Page 8](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_008.png)

---

## Page 9

A Statistical Definition of Temperature
●
For our two connected systems, the most probable division of 
energy between the two systems is the one that maximises 
Ω1(E1)Ω2(E2).
●
We can maximise this expression with respect to E1
(t(E) AzlEn))
= o
Etot = EstEr
Ette, (EitE)
↓
W
o
=
1 +d
=- --
↳
dEz

![Page 9](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_009.png)

---

## Page 10

A Statistical Definition of Temperature
-
↓=d
coolness
~
blue
&
deter
Boltzmann
Cust
Boltzmann
Distribution
IddE
=Jed
↑~
Side
= BfldE,
3()=
In R ,
= BE
a
=18

![Page 10](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_010.png)

---

## Page 11

Boltzmann Distribution
●
Boltzmann distribution (also called Gibbs distribution) is a 
probability distribution that gives the probability that a system 
in thermal equilibrium will be in a certain state as a function of 
that state's energy and the temperature of the system.
E
–E
P(E)
P(E)

![Page 11](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_011.png)

---

## Page 12

Boltzmann Distribution
Concepts in Thermal Physics S. J. 
Blundell and K. M. Blundell

![Page 12](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_012.png)

---

## Page 13

Simulated Annealing

![Page 13](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_013.png)

---

## Page 14

●
The algorithm is inspired by the process of annealing.
●
Atoms in a material form a crystal lattice structure. If the 
material is heated, the atoms are in a rapid state of motion. 
The motion randomises their positions and prevents them 
coming to rest in an orderly arrangement.
●
As the material cools down, the atoms slow down, and if the 
cooling is slow enough, i.e., annealing, the atoms 
reconfigure into a minimum-energy state.
●
If the material is cooled rapidly, i.e., quenched, the metal 
re-crystallises into a different higher-energy state (called an 
amorphous state).
Simulated Annealing
Kirkpatrick et al., Optimization 
by simulated annealing, 1983.

![Page 14](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_014.png)

---

## Page 15

MassHine
Annealing Schedule
Wa
Ae
L
Anneblng Poinc
600
589
€
Sitalq Point
520
500 €
400 *'
80 €
RT
20 mins
40 mns
10 mins
30 Mins
30 ming
40 Wins
40 mins
(Time)
450_mins (2 5 hours)

![Page 15](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_015.png)

---

## Page 16

CONTAINER GLASS
Source: Eurotherm
Annealing Lehr
Spouts
lib
KuM
Molding
Conveying Belt
"Solid" glass
Further cooling during conveying
Source: BDF Industries
CelSian
IMI-NFG Course on Processing of Glass
Lecture 9: Annealing and Tempering
NFC
Glass & Solar
mathieu hubert@celsian.nl
13

![Page 16](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_016.png)

---

## Page 17

www.nogrid.com/index.php/en/product/nogrid-points-blow1
Disordered Structure
Ordered Structure

![Page 17](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_017.png)

---

## Page 18

●
From statistical mechanics, the Boltzmann distribution 
describes the probability of a system occupying a given 
energy state:
●
This equation shows that as the temperature decreases, the 
probability of occupying a higher-energy state decreases, but 
is not zero.
●
Therefore an atom could jump to a higher-energy state with 
some small probability, unlike in classical mechanics.
Simulated Annealing
E
P(E)
–E

![Page 18](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_018.png)

---

## Page 19

●
This probabilistic property imparts an exploratory nature to 
the optimisation algorithm.
Simulated Annealing
f(x)
x
x(k)
Accept it with some 
probability
Always accept it
Global minimum

![Page 19](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_019.png)

---

## Page 20

●
Objective function value = Energy level 
●
Temperature is a parameter controlled by the optimiser, 
which begins high and slowly “cooled” to drive convergence. 
●
At the kth iteration, the design variables are given by 𝑥(𝑘), and 
the objective function value (or energy) is given by 𝑓 (𝑥(𝑘)). 
●
A new state 𝑥new is selected. If the energy level decreases, 
the new state is accepted. If the energy level increases, the 
new state might still be accepted with probability
otherwise the state remains unchanged.
Simulated Annealing

![Page 20](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_020.png)

---

## Page 21

●
A new state 𝑥new is usually selected at random in the 
neighbourhood of 𝑥.
●
A neighbouring state is usually related to the current state 
compared to picking a pure random state from the entire set. 
In defining the neighbourhood structure, we might wish to 
define transition probabilities so that all neighbours are not 
equally likely. This type of structure is common in Markov 
chain problems.
Simulated Annealing

![Page 21](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_021.png)

---

## Page 22

●
Sampling algorithm
●
Top 10 Algorithm of the 20th century
Metropolis Algorithm
M(RT)^2 (1953) Equation of state 
calculations by fast computing machines.

![Page 22](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_022.png)

---

## Page 23

Metropolis Algorithm
●
Suppose we are in state i and we generate a new state j by 
making some change to state i.
●
We choose the particular change uniformly at random from a 
set of possible changes - a move set.
●
We then either accept or reject the new state with 
acceptance probability Pa given by:
●
If the move is rejected then we do nothing, if move accepted 
we change the system to the new state
M(RT)^2 (1953) Equation of state 
calculations by fast computing machines.

![Page 23](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_023.png)

---

## Page 24

Metropolis Algorithm
M(RT)^2 (1953) Equation of state 
calculations by fast computing machines.

![Page 24](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_024.png)

---

## Page 25

●
The complete Markov chain Monte Carlo (MCMC) simulation 
involves the following steps:
1.
Choose a random starting state.
2.
Choose a move uniformly at random from an allowed 
set of moves.
3.
Calculate the acceptance probability Pa
4.
With probability Pa accept the move: the state of the 
system changes to the new state; otherwise reject it: 
system stays in its current state for one more step of 
the calculation.
5.
Measure the value of interest in the current state.
6.
Go to step 2.
Metropolis Algorithm
M(RT)^2 (1953) Equation of state 
calculations by fast computing machines.

![Page 25](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_025.png)

---

## Page 26

●
The temperature level provides control on the level of 
expected exploration.
Cooling
https://www.intechopen.com/chapters/38520

![Page 26](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_026.png)

---

## Page 27

1.
A common approach is an exponential decrease where 𝑇0 is the 
initial temperature, 𝛼 is the cooling rate, and 𝑘 is the iteration 
number. The cooling rate 𝛼 is close to 1, such as 0.8~0.99:
2.
Another simple approach is the equation below where the 
exponent 𝛽 is usually in the range of 1~4. A higher exponent 
corresponds to spending more time at low temperatures:
3.
The temperature is kept constant for a fixed number of iterations, 
or successful moves, before decreasing.
●
Cooling schedule, or annealing schedule - process for 
decreasing the temperature throughout the optimisation.
Cooling
&
#
T

![Page 27](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_027.png)

---

## Page 28

Cooling
k

![Page 28](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_028.png)

---

## Page 29

Cooling
k

![Page 29](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_029.png)

---

## Page 30

●
Cooling should occur slowly to improve the ability to recover 
from a local optimum, imitating the annealing process 
instead of the quenching process.
●
The cooling schedule can substantially impact the 
algorithm’s performance, and some experimentation is 
usually required to select an appropriate schedule for the 
problem at hand.
Cooling

![Page 30](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_030.png)

---

## Page 31

●
Constraints can be handled in simulated annealing without 
resorting to penalties by rejecting any infeasible states.
●
Can be applied to continuous multimodal problems as well. 
Motivation is similar: Initial high temperature permits escape 
from local minima. By slowly cooling, the initial exploration 
gives way to exploitation. Only change is in the neighbour 
function. A typical approach is to generate a random direction 
and choose a step size proportional to the temperature. 
Thus, smaller, more conservative steps are taken as the 
algorithm progresses.
●
Purely random step directions are not particularly efficient for 
many continuous problems. One variation adopts concepts 
from the Nelder-Mead algorithm to improve efficiency.
Simulated Annealing 
Press et al., Numerical Recipes in C: The Art of Scientific Computing, 1992.

![Page 31](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_031.png)

---

## Page 32

Applications

![Page 32](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_032.png)

---

## Page 33

Application 1 - Travelling Salesperson
●
The objective is the total Euclidean distance of a path that 
traverses all points and returns to the starting point.
●
The design variables are a sequence of integers 
corresponding to the order in which the salesperson 
traverses the points.

![Page 33](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_033.png)

---

## Page 34

Application 1 - Travelling Salesperson
https://eng-git.canterbury.ac.nz/jch425/teaching/-/tree/main/enel445?ref_type=heads

![Page 34](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_034.png)

---

## Page 35

Application 1 - Travelling Salesperson
●
The final path might not be the global optimum - these 
finite-time methods are only approximations of the full 
combinatorial search.
●
But the methodology is 
effective and fast for this 
problem in finding a 
near-optimal solution.
●
Stochastic method - fix 
seed for reproducibility
https://en.wikipedia.org/wiki/Simulated_annealing

![Page 35](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_035.png)

---

## Page 36

Application 2 - Physical Design of Computers
●
Original motivation of Kirkpatrick et al.
https://www.intechopen.com/chapters/38549
Simulated Annealing Technique for Routing in a 
Rectangular Mesh Network
https://www.hindawi.com/journals/mse/2014/127359/

![Page 36](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_036.png)

---

## Page 37

Application 3 - Ordering an Election
https://www.youtube.com/watch?v=Lq-Y7crQo44&t=1394s

![Page 37](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_037.png)

---

## Page 38

Application 4 - Untangling Earphones
https://www.youtube.com/watch?v=Lq-Y7crQo44&t=1394s

![Page 38](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_038.png)

---

## Page 39

Exercises
●
Look up the terms that are new to you in this lecture and 
understand them.
●
Think of a problem and apply the simulated annealing 
algorithm to it.
●
Try and combine simulated annealing with 
Nelder-Mead, Particle Swarm Optimisation or any other 
algorithm(s) you’ve learnt so far. 
How would your hybrid algorithm proceed?
Thanks!

![Page 39](../course.material/figs/T2-6%20Simulated%20annealing-annotated-1/page_039.png)

---

