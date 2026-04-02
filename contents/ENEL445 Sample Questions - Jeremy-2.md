# ENEL445 Sample Questions - Jeremy-2

*Converted from PDF: ENEL445 Sample Questions - Jeremy-2.pdf*

---

## Page 1

Q1. Constrained Optimisation Basics. Consider the following optimization problem: 
min
𝑥1,𝑥2 𝑥22 + 𝑥1 
subject to  
𝑥1 ≥1 
𝑥1𝑥2 ≥1 
a) Write the Lagrangian function of this problem. 
b) Find the solution 𝑥1, 𝑥2 analytically.  
Note: this is harder than any test question.  
c) What type of problem is this? 
d) Suggest an algorithm to solve problems of this type. Explain i) the key concepts of your 
chosen algorithm, ii) why it may be a good choice to solve problems of this type. 
Q2. Duality. Consider the same problem as in Q1, except with the second constraint removed.  
a) Is the problem convex? If so, state how you know this. If not, state why. 
b) Calculate the Lagrangian dual function of this problem. 
c) Calculate, or otherwise determine, the duality gap. 
Q3. Optimal control. 
a) Explain the principles of model predictive control, including a mathematical formulation. List 
at least two main advantages and at least two disadvantages.  
b) Consider the system 𝑥𝑘+1 = 𝑥𝑘+ 𝑢𝑘+ 1 where 𝑥𝑘, 𝑢𝑘 are restricted to integers. The cost 
function is 𝑐(𝑥, 𝑢) = 𝑥2 + 𝑢2 and constraints as follows:  
0 ≤𝑥𝑘≤2 
−2 ≤𝑢𝑘≤1 
If the terminal cost is 2𝑥, and the prediction horizon is 2, work out the MPC control law 
assuming that the initial state is within 0 ≤𝑥𝑘≤2. 
c) (Advanced): Usually in practice a terminal constraint or cost is added, i.e. at the final state of 
the horizon there is a penalty and/or constraint to keep the final state within a desired 
region. Using your understanding of how MPC works, why might this be a good idea? Can 
you think of any disadvantages? 
d) Explain Bellmann’s principle of optimality in your own words. 
Q4. Reinforcement Learning 
a) When would you use value iteration or policy iteration, as opposed to e.g. Q learning? 
b) Explain how policy iteration works, giving an algorithm (either conceptually or 
mathematically).  
c) In Q Learning, why is it generally better to use an ε-greedy policy rather than a 100% greedy 
policy? 
d) (Advanced): Q Learning is an off-policy method. Adapt Q Learning to use its own policy and 
thus become an on-policy method. Then, look up the SARSA algorithm and compare.

![Page 1](../course.material/figs/ENEL445%20Sample%20Questions%20-%20Jeremy-2/page_001.png)

---

