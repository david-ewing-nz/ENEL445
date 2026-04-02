# Applied Engineering Optimisation - OC - for Learn

*Converted from PDF: Applied Engineering Optimisation - OC - for Learn.pdf*

---

## Page 1

Classification: In-Confidence
Applied Engineering 
Optimisation
ENEL445

![Page 1](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_001.png)

---

## Page 2

Classification: In-Confidence
Week 6: Optimisation-based 
control
• Introduction to optimal control
• Key principles
• Predictive control
• Dynamic programming
• Reinforcement learning

![Page 2](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_002.png)

---

## Page 3

Classification: In-Confidence
Real-life applications
• Control: Most controllers in industry are 
proportional-integral, but model-predictive control 
(MPC) approaches are increasingly common.
• Dynamic Programming is widely used as a tool to 
solve computationally difficult problems – e.g. in 
2015 Win-And-Score-Predictor (UC) cricket 
predictor. It can also be used for:
• Reinforcement Learning: This is actually a form of 
optimal control -> lots of interest and increasing 
number of real-life applications.

![Page 3](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_003.png)

---

## Page 4

Classification: In-Confidence
Optimal control
• The main idea is to design control inputs that 
minimise a cost function which is based on our 
states from time 0 to the end of the prediction 
horizon (or infinity). 
• This means optimization across multiple time 
periods.

![Page 4](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_004.png)

---

## Page 5

Classification: In-Confidence
Horizon
• In some cases, we can consider the time period 
between now and infinity as the system converges 
to a point where the cost is zero.
• Example: LQR control (if you’re doing ENME403)
• However, in many practical cases this is not 
possible, approximate by choosing a distant horizon 
which recedes with time.
• This is called receding horizon control – another name 
for model predictive control
• The length of the horizon is a trade off between 
complexity and performance.

![Page 5](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_005.png)

---

## Page 6

Classification: In-Confidence
Mathematical preliminaries

![Page 6](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_006.png)

---

## Page 7

Classification: In-Confidence
Mathematical description

![Page 7](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_007.png)

---

## Page 8

Classification: In-Confidence
Model Predictive Control
• Direct application of constrained optimisation:

![Page 8](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_008.png)

---

## Page 9

Classification: In-Confidence
Model-predictive control
The main advantages are:
• An optimum trajectory is followed, unlike PI control 
which often overshoots, etc.
• Tends to work very well in practice even with short 
horizons.
• Constraints can be directly included in the optimization 
problem, e.g. x1 has to stay between 0 and 10 which is 
great for ensuring physical constraints are not violated 
(another issue with PI control).

![Page 9](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_009.png)

---

## Page 10

Classification: In-Confidence
Model-predictive control
The main disadvantages are:
• An accurate model is required, since this is used for 
predictive purposes. Bad model = bad control and 
could lead even to constraints not being satisfied.
• Complex and computationally expensive (especially 
as the horizon h becomes larger), and generally 
quite hard to prove stability.

![Page 10](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_010.png)

---

## Page 11

Classification: In-Confidence
Finite horizon approximation (1)
• In practice, we cannot evaluate an infinite horizon!
• Idea 1: approximate with a finite horizon
• Example 1
c(x,u) = x2 + u2
x
x
u
u

![Page 11](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_011.png)

---

## Page 12

Classification: In-Confidence
Example 1

![Page 12](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_012.png)

---

## Page 13

Classification: In-Confidence
Example 2: Buck converter
Code on Learn: h = 2, Ts = 10-4 s

![Page 13](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_013.png)

---

## Page 14

Classification: In-Confidence
Finite horizon approximation (2)
• Idea 2: solve MPC problem every K steps, use plan 
for K steps, then solve another MPC problem, etc.
• Variations: 
• add estimated final state cost ෠𝑉(x(t+T)) to truncate 
horizon. 
• If ෠𝑉 = V, MPC solution is the optimal solution.
• convert hard constraints to violation penalties – same 
idea as penalty methods in constrained optimisation!
• Why might this be a good idea? (Hint: think about 
disturbances)

![Page 14](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_014.png)

---

## Page 15

Classification: In-Confidence
Bellman’s Principle of Optimality
Even without 
constraints, 
intractable for 
large h

![Page 15](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_015.png)

---

## Page 16

Classification: In-Confidence
Bellman’s principle
• The value of this is that it allows us to work 
backwards to find the optimal solution.

![Page 16](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_016.png)

---

## Page 17

Classification: In-Confidence
Example

![Page 17](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_017.png)

---

## Page 18

Classification: In-Confidence
Discrete-time optimal control
an introduction to the use of Dynamic Programming
x k + 1 = uk
Jh(x) = x2
c(x, u) = Cxu 
h = 5
C x u =
x\u
1
2
3
1
4
2
5
2
4
5
3
3
4
2
1
1
2
3
0
1
2
3
4
5
V=9
V=1
c=4
c=4 V=4
c=4
V=5
V=5
V=5
c=2
V=7
c=3
V=8
c=1
V=6
c=2
V=10
c=3
V=9
c=1
V=7
c=2
V=11
c=3
V=10
c=1
V=8
c=2
V=12
c=3
V=11
c=1
V=9
19/59
x

![Page 18](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_018.png)

---

## Page 19

Classification: In-Confidence
Value function
• It is clear from this example that a value function 
V(x,k) exists, i.e. the cost of being at state x at time 
k. 
• If we knew this function exactly, we could work out 
the optimal next action easily.
• However, this is dependent on a finite horizon h 
and a well-defined final cost Jh(x,h). Also, what if 
the horizon is infinite?

![Page 19](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_019.png)

---

## Page 20

Classification: In-Confidence
Discount factors
• We could truncate (as in MPC) but often a better 
approach is to use a discount factor.
• An interpretation of this is that an immediate 
reward is better than the same reward tomorrow, 
but not by that much.

![Page 20](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_020.png)

---

## Page 21

Classification: In-Confidence
Value iterations
• For such problems there is no time dependence, so the 
Bellman optimality condition is that 
• We don’t know the true value function V, but this can 
be solved by value iteration
• We start with an initial guess V0 and then iterate, 
repeatedly computing Vk+1(x) for all states x until V 
converges. 
Vk+1(x)

![Page 21](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_021.png)

---

## Page 22

Classification: In-Confidence
Example
x\u
1
2
3
1
5
6
4
2
4
5
3
3
4
3
2
c(x, u)
x\u
1
2
3
1
3
3
3
2
1
3
3
3
2
3
3
f(x, u)
Exercise: 
• If the discount factor is 0.8, solve for V(x) via value iterations.
• Show that the theoretical value is V(x) = [12 11 10]T

![Page 22](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_022.png)

---

## Page 23

Classification: In-Confidence
Example
Code on Learn

![Page 23](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_023.png)

---

## Page 24

Classification: In-Confidence
Rewards
• Instead of a cost c(x, u) we can instead think of 
maximising a discount sum of rewards r(s,a) by 
choosing actions a.
• Usually reinforcement learning problems are posed 
this way.

![Page 24](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_024.png)

---

## Page 25

Classification: In-Confidence
Policy iteration (1)
• Now consider the case where we have a policy 
𝑎= 𝜋(𝑠) 
• The value of that policy at state s is now 
𝑉𝜋𝑠= 𝑟𝑠, 𝑎+ λ𝑉𝜋𝑓(𝑠, 𝜋(𝑠)
• This can be computed as the limit of
𝑉𝑘+1
𝜋
𝑠= 𝑟𝑠, 𝑎+ λ𝑉𝑘
𝜋𝑓(𝑠, 𝜋(𝑠)

![Page 25](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_025.png)

---

## Page 26

Classification: In-Confidence
Policy iteration (2)
1. Initialise policy 𝜋(𝑠) 
2. Compute value of this policy 𝑉𝜋 using the 
iterative approach on the previous slide.
3. Update 𝜋(𝑠) to be the greedy policy with respect 
to 𝑉𝜋 
𝜋(𝑠) ←arg max
𝑎
𝑉𝜋𝑓(𝑠, 𝑎)
4. Stop if policy has converged, otherwise return to 
Step 2.

![Page 26](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_026.png)

---

## Page 27

Classification: In-Confidence
Policy iteration (3)
• This process guarantees that each policy is a strict 
improvement over the previous one.
• Each policy evaluation is an iterative process, but by 
starting with the value function from the previous 
policy, typically convergence speed is increased.
• Policy iteration ultimately leads to the same 
outcome as value iteration, given that if you have 
the value function you can compute the optimal 
policy. But, in many cases it converges more 
quickly.

![Page 27](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_027.png)

---

## Page 28

Classification: In-Confidence
Markov decision processes
• In a Markov decision process, the transitions 
between states are random. We can easily amend 
the previous value function definitions for this case.

![Page 28](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_028.png)

---

## Page 29

Classification: In-Confidence
Learning from samples (1)
• In theory one could learn the value function from 
samples of s, a, and r. The optimal action is then 
in the deterministic case and, for an MDP:

![Page 29](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_029.png)

---

## Page 30

Classification: In-Confidence
Learning from samples (2)
• This is not ideal – we need to know the model and 
the reward function to recover the optimal action 
even if we have worked out the value function. 
• Better idea: learn the action-value function Q(s,a)
𝑄𝑠, 𝑎= 𝑟𝑠, 𝑎+ λ𝑉(𝑓𝑠, 𝑎)
Or

![Page 30](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_030.png)

---

## Page 31

Classification: In-Confidence
Learning from samples (3)
• The value function is easily obtained from Q
𝑉𝑠= max
𝑎
𝑄(𝑠, 𝑎)
• So the Q function satisfies the recursion 
(deterministic case):
𝑄𝑠, 𝑎= 𝑟𝑠, 𝑎+ λ max
𝑏
𝑄(𝑓(𝑠, 𝑎), 𝑏)

![Page 31](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_031.png)

---

## Page 32

Classification: In-Confidence
Monte Carlo exploration (basic 
idea)
1.
Choose a random start point and action, simulate a trajectory (where 
all actions except the starting one are greedy actions w.r.t. the 
current estimate of Q). 
2.
Calculate reward from the trajectory.
3.
Update estimate of Q based on this reward. 
4.
Repeat 1 until convergence. 
• This algorithm is the basis of many current approaches to reinforcement 
learning (e.g. AlphaZero etc). Many people believe that this algorithm 
always converges to the optimal action-value function, but it has never 
been proved.

![Page 32](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_032.png)

---

## Page 33

Classification: In-Confidence
Q learning (1)
• Unlike Monte-Carlo methods which update after 
complete trajectory has been sampled, Q learning 
updates for every sample. 
• Given samples s, a, r, s’, update:
• 𝛼𝑘 is the learning rate and is decayed to zero 
gradually.
𝑄𝑘+1 𝑠, 𝑎= 1 −𝛼𝑘𝑄𝑘𝑠, 𝑎+ 𝛼𝑘(𝑟𝑠, 𝑎+ λ max
𝑏
𝑄(𝑠′, 𝑏)

![Page 33](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_033.png)

---

## Page 34

Classification: In-Confidence
Q learning (2)
• In order to get samples, a policy is needed to 
choose actions a.
• Q learning is an off-policy method. It learns the 
value of the optimal policy whilst sampling using 
any policy. One common approach is the ε-greedy 
policy:

![Page 34](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_034.png)

---

## Page 35

Classification: In-Confidence
Continuous action/state-space
• If s is continuous then a functional approximation 
for Q(s, a) is required which must allow previously 
visited states to be interpolated, such as a neural 
network.
• If the action space is also continuous then a 
functional approximation can still be used as long 
as action of minimising Q(s, a) over a is feasible.
• Otherwise an actor-critic method can be employed - 
where a second network is used to return an action 
given a state (i.e. to represent a policy) and the policy 
network and Q network updated independently.

![Page 35](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_035.png)

---

## Page 36

Classification: In-Confidence
Summary: What method to 
choose?
1.
Dynamic Programming: Requires low state dimension, small 
number of inputs and a model. Particularly useful if the end 
point is known, as can then reverse time from there.
2.
Predictive Control: Effective way of dealing with constraints, 
but the n-step ahead optimisation needs to be able to be done 
efficiently, e.g. linear model, quadratic cost + constraints.
3.
Q-learning: Useful if no model is available and complex 
nonlinear control solutions are required. Can be implemented 
directly for low dimensional problems, otherwise needs 
functional approximations for the Q function and, possibly, the 
policy (e.g. if the action and/or state-space are continuous).

![Page 36](../course.material/figs/Applied%20Engineering%20Optimisation%20-%20OC%20-%20for%20Learn/page_036.png)

---

