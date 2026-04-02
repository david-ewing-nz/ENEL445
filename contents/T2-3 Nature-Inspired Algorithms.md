# T2-3 Nature-Inspired Algorithms

*Converted from PDF: T2-3 Nature-Inspired Algorithms.pdf*

---

## Page 1

Nature-Inspired Algorithms
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_001.png)

---

## Page 2

Outline
●Genetic Algorithm (GA)
●Particle Swarm Optimisation (PSO)

![Page 2](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_002.png)

---

## Page 3

Nature-inspired Algorithms
A higher-level strategy (meta-) that guides or controls heuristic 
methods to solve optimisation problems more effectively.

![Page 3](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_003.png)

---

## Page 4

Genetic Algorithm - Terminology
●
Gene
A design variable
●
Chromosome
A design point / vector
●
Population
A set of design points / chromosomes
●
Fitness
Objective function value for a chromosome
Population
F1
F2
Fnp

![Page 4](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_004.png)

---

## Page 5

●
Generation
One genetic algorithm iteration
●
Allele 
The value a gene takes for a
particular chromosome
●
Gene Representation
Method of encoding the numerical
value of the design variable
Genetic Algorithm - Terminology

![Page 5](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_005.png)

---

## Page 6

Gene Representation
●
Binary-encoded algorithms use bits to represent the design 
variables (also called bit-set or bit-string)
■
Each gene is represented as a string of 0 or 1
●
Real-encoded algorithms use real-valued numbers to 
represent the design variables
■
Each gene is represented as a real number

![Page 6](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_006.png)

---

## Page 7

https://www.tutorialspoint.com/ge
netic_algorithms/genetic_algorith
ms_fundamentals.htm
Genetic Algorithm

![Page 7](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_007.png)

---

## Page 8

Genetic Algorithm
●
GA starts with a set of design points (the population) rather 
than a single starting point, and each iteration (generation) 
updates this set in some way.
●
GAs evolve the population using three main steps:
(1)
Selection - Based on natural selection, where members 
of the population that acquire favourable adaptations are 
more likely to survive longer and contribute more to the 
population gene pool.
(2)
Crossover - Inspired by chromosomal crossover, which 
is the exchange of genetic material between 
chromosomes during sexual reproduction.
(3)
Mutation - Mimics genetic mutation, which is a 
permanent change in the gene sequence that occurs 
naturally.

![Page 8](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_008.png)

---

## Page 9

Initial Population
●
The first step in a genetic algorithm is to generate an initial 
set (population) of points.
●
As a rule of thumb, the population size should be 
approximately one order of magnitude larger than the 
number of design variables, and this size should be tuned.

![Page 9](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_009.png)

---

## Page 10

Selection
●
We choose chromosomes from the population for 
reproduction/recombination (called a mating pool) - 
choosing parents!
●
Desirable to choose a mating pool that improves in fitness 
(thus mimicking the concept of natural selection), but take 
care to also maintain diversity
●
Two popular methods of selection are:

![Page 10](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_010.png)

---

## Page 11

Selection
●
Tournament Selection 
■
Randomly select two chromosomes from the population 
until the requisite number of pairs is reached.
■
Compare the two chromosomes and select the one with 
the highest fitness to be in the mating pool

![Page 11](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_011.png)

---

## Page 12

Selection
●
Roulette Wheel Selection 
■
Better points are allocated a larger sector on the 
roulette wheel to have a higher probability of being 
selected.
■
Voltage divider!

![Page 12](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_012.png)

---

## Page 13

Crossover - Binary encoded
●
Chromosomes in the mating pool are combined to generate 
new chromosomes
●
Single-point crossover involves generating a random integer 
1 ≤ 𝑘 ≤ 𝑚−1 that defines the crossover point 
●
For one of the offspring, 
the first 𝑘 bits are taken from 
parent 1 and the remaining bits 
from parent 2, and vice versa
●
Various other strategies are 
possible

![Page 13](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_013.png)

---

## Page 14

Crossover - Real encoded
●
There are various options for the reproduction of 
real-encoded chromosomes. A standard method is linear 
crossover, which generates two or more points in the line 
defined by the two parent points. One option for linear 
crossover is to generate the following two points:
●
Another option is a simple crossover like the binary case 
where a random integer is generated to split the 
chromosomes. This simple crossover does not generate as 
much diversity as the binary case and relies more heavily on 
an effective mutation.

![Page 14](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_014.png)

---

## Page 15

Mutation
●
Mutation is a random operation performed to change the 
genetic information and introduces additional diversity into the 
population.
●
Even though selection and reproduction effectively recombine 
existing information, we might need new information, or 
recover useful genetic information that may have been lost.
●
Mutation for real-encoded chromosome is just adding a 
random number to each gene.

![Page 15](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_015.png)

---

## Page 16

Genetic Algorithm - Results
Binary-encoded

![Page 16](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_016.png)

---

## Page 17

Genetic Algorithm - Results
Real-encoded

![Page 17](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_017.png)

---

## Page 18

Genetic Algorithm - Constraint Handling
●
Constraints can be handled in many ways in a GA
●
For example in tournament selection, we can choose among 
two competitors as follows:
■
Reject chromosomes that are infeasible.
■
Among two infeasible chromosomes, choose the one 
with a smaller constraint violation.

![Page 18](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_018.png)

---

## Page 19

Genetic Algorithm - Convergence
●
Rigorous mathematical convergence criteria, like those used in 
gradient-based optimisation, do not apply to GAs. 
●
The most common way to terminate a GA is to specify a 
maximum number of iterations, which corresponds to a 
computational budget.
●
Monitoring the trends in population fitness:
■
Average of the population’s fitness
■
The fitness of the best member in the population
●
The best member can disappear as a result of crossover or 
mutation. To avoid this and to improve convergence, many 
GAs employ elitism. This means that the fittest population 
member is retained to guarantee that the population does not 
regress.

![Page 19](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_019.png)

---

## Page 20

Comparing Gene Representation
●
Binary-encoded algorithms use bits to represent the design 
variables (also called bit-set or bit-string)
■
Each gene is represented as a string of 1 or 0
■
Provides faster implementation of crossover and 
mutation operators.
■
However, it requires extra effort to convert into 
binary form and accuracy of algorithm depends upon 
the binary conversion.
●
Real-encoded algorithms use real-valued numbers to 
represent the design variables
■
Each gene is represented as a real number
■
Length of chromosome is shorter
■
Avoids the “Hamming cliff” issue of binary encoding, 
which is caused by the fact that many bits must 
change to move between adjacent real numbers 
(e.g., 0111 to 1000).

![Page 20](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_020.png)

---

## Page 21

https://en.wikipedia.org/wiki/Evolved_antenna
https://www.mathworks.com/help/antenna/ug
/miniaturize-rectangular-microstrip-patch-ant
enna-using-genetic-algorithm.html

![Page 21](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_021.png)

---

## Page 22

Electron beam transfer line design for
plasma driven Free Electron Lasers
M Rossetti Conti a b g
5
A Bacci
A_Giribono
VPetrillo b, ARRossi &,LSerafini
C_ Vaccarezza
Plasma driven particle accelerators represent the future of compact accelerating
machines and Eree Electron Lasers are going to benefit from these new technologies
One of the main issue of this new approach to FEL machines is the design of the
transfer line needed to match of the electron-beam with the magnetic undulators
Despite the reduction of the chromaticity of plasma beams is one of the main goals, the
target of this line is to be effective even in cases of beams with a considerable value of
chromaticity: The method here explained is based on the code GIOTTO (Bacci etal,,
2016) that works using a homemade genetic algorithm and that is capable of finding
optimal matching line layouts directly using a full 3D tracking code:
a: Transfer Line
8 m
b: Transfer Line
5.15 m
2 [m]
2 [m]
c: Transfer Line
d: Transfer Line
2 [m]

![Page 22](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_022.png)

---

## Page 23

Genetic Programming
https://en.wikipedia.org/wiki/
Genetic_programming

![Page 23](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_023.png)

---

## Page 24

https://en.wikipedia.org/wiki/List_of_genetic_algorithm_applications

![Page 24](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_024.png)

---

## Page 25

Scipy implementation

![Page 25](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_025.png)

---

## Page 26

Particle Swarm Optimisation 
(PSO)

![Page 26](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_026.png)

---

## Page 27

PSO
●
Stochastic population-based optimisation algorithm like the GA.
●
Inspired by “swarm intelligence” - property of a system whereby 
the collective behaviors of agents interacting locally with their 
environment cause coherent global patterns.
Eberhart and Kennedy, “New optimizer 
using particle swarm theory”, 1995.
“Dumb agents, properly connected into a swarm, yield smart results”

![Page 27](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_027.png)

---

## Page 28

PSO - Terminology
●
Particle / Agent
A design point / vector
●
Swarm 
A set of design points
●
The “swarm” in PSO is a set of design points that “move” in 
𝑛-dimensional space, looking for the best solution. 
●
The history of each point is relevant to the PSO algorithm, so 
we adopt the term particle. Each particle moves according 
to a velocity.
●
The velocity of a particle changes according to the past 
objective function values of that particle and the current 
objective values of the rest of the particles.

![Page 28](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_028.png)

---

## Page 29

PSO - Velocity 
●
Each particle remembers the location where it found its best 
result so far, and it exchanges information with the swarm 
about the location where the swarm has found the best result 
so far.
●
The position of particle 𝑖 for iteration 𝑘 + 1 is updated 
according to:

![Page 29](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_029.png)

---

## Page 30

PSO - Position update 
●
Because the time step is artificial, we can eliminate it by 
multiplying by Δt to yield the position update rule

![Page 30](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_030.png)

---

## Page 31

PSO - Initialisation
●
As with a GA, the initial set of points can be determined 
randomly or via more sophisticated sampling strategies.
●
The velocities are also randomly initialized, generally using 
some fraction of the domain size.
●
Particles must be prevented from going beyond constraint 
bounds. If a particle reaches a boundary and has a velocity 
pointing out of bounds, reset to velocity to zero or reorient it 
toward the interior for the next iteration.
●
It is also helpful to impose a maximum velocity. If the velocity 
is too large, the updated positions are unrelated to their 
previous positions, and the search is more random.
●
The maximum velocity might also decrease across iterations 
to shift from exploration toward exploitation.

![Page 31](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_031.png)

---

## Page 32

PSO - Convergence
●
Distance between each particle and the best particle
●
Best particle’s objective function value changes for the last 
few iterations
●
Difference between the best and worst particle.
●
Another alternative is to check whether the velocities for all 
particles are below some tolerance.
●
Some of these criteria that assume all the particles 
congregate (distance, velocities) do not work well for 
multimodal problems. In those cases, tracking only the best 
particle’s objective function value may be more appropriate.

![Page 32](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_032.png)

---

## Page 33

PSO
-
Results
X2
Fl
-2
-2
X1
X1
k=0
k=1
k=3
2
12
~l
F2
F2
X1
X1
X1
k=5
k=12
k=17

![Page 33](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_033.png)

---

## Page 34

*[Page appears blank or contains only images]*

![Page 34](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_034.png)

---

## Page 35

Boids
https://cs.stanford.edu/people/eroberts/courses/soco/projects/20
08-09/modeling-natural-systems/boids.html
https://eater.net/boids

![Page 35](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_035.png)

---

## Page 36

https://people.ece.cornell.edu/land/courses/
ece4760/labs/s2021/Boids/Boids.html
Boids on a PIC

![Page 36](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_036.png)

---

## Page 37

Other Nature Inspired Algorithms

![Page 37](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_037.png)

---

## Page 38

Other Nature Inspired Algorithms
https://www.nature.com/articles/s41598-024-54910-3

![Page 38](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_038.png)

---

## Page 39

The “Real” Evolutionary Algorithm
●
What constitutes an evolutionary algorithm is not well defined. 
●
Evolutionary algorithms are inspired by processes that occur in 
nature or society. There is a plethora of evolutionary algorithms 
in the literature, thanks to the fertile imagination of the research 
community and a never-ending supply of phenomena for 
inspiration.
●
These algorithms are more of an analogy of the phenomenon 
than an actual model. They are, at best, simplified models and, 
at worst, barely connected to the phenomenon. 
●
Nature-inspired algorithms tend to invent a specific terminology 
for the mathematical terms in the optimisation problem.

![Page 39](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_039.png)

---

## Page 40

DNA
The Nucleosome
"Beads-on-a
~String'
The 30nm Fibre
Isolated patches_
Genes under active transcription:
Less active genes_
Add core histones
Add histone H1.
Add further sc
V
Active Chromosome
The Metaphase Chromosome
During interphase
During cell division
Iffold proteins _
Add further scaffold proteins
Ec2b 
0
Q8
3
8orar

![Page 40](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_040.png)

---

## Page 41

Recurrent laryngeal nerve
https://en.wikipedia.org/wiki/
Recurrent_laryngeal_nerve

![Page 41](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_041.png)

---

## Page 42

Exercises
●
Come up with your own crossover strategies.
●
Think of other ways to handle constraints in a GA 
besides the ones described in the lecture slides.
●
Pick some points in 2D, and parameter values for the 
PSO algorithm and sketch the next point that the 
algorithm takes you to.

![Page 42](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_042.png)

---

## Page 43

Thanks!

![Page 43](../course.material/figs/T2-3%20Nature-Inspired%20Algorithms/page_043.png)

---

