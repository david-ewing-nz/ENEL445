# Dynamic games-2

*Converted from PDF: Dynamic games-2.pdf*

---

## Page 1

Classification: In-Confidence 
Dynamic games 
Dynamic games have multiple time-steps (rather than a single decision leading to a payoff, as in 
the Prisoner’s Dilemma for example). An example is Linear Quadratic (LQ) Games which are a 
class of dynamic games involving multiple decision-makers (players) where each player aims to 
minimize a quadratic cost function subject to linear dynamics. They extend the Linear Quadratic 
Regulator (LQR) framework to game-theoretic settings. 
State-space: 
𝑥𝑘+1 = 𝐴𝑥𝑘+ ∑𝐵𝑖𝑢𝑘
𝑖
𝑁
𝑖=1
 
where 𝑥𝑘 is the state at time k, 𝐴, 𝐵𝑖 are system matrices and 𝑢𝑘
𝑖 is the control input (decision) 
for player i at time k.  
Each player is trying to minimise their own cost: 
𝐽𝑖= ∑(𝑥𝑘
⊤𝑄𝑖𝑥𝑘+ 𝑢𝑘
𝑖⊤𝑅𝑖𝑢𝑘
𝑖)
∞
𝑘=0
 
Via a feedback law  
𝑢𝑘
𝑖= −𝐾𝑖𝑥𝑘 
Similarly to standard LQR control, there is an Algebraic Riccati Equation which can be solved to 
find K such that u is the Nash equilibrium of the dynamic game.  
Finance applications 
Stackelberg game 
Suppose two firms are producing the same product and competing. The market price depends 
on the quantity produced, as follows:   
𝑃(𝑄) = 𝑎−𝑏𝑄, where 𝑄= 𝑞1 + 𝑞2 
Where P is the market price, a, b are constants, and Q is the quantity produced by both firms 1 
(leader) and 2 (follower). How much should each firm produce? 
Profit (= - cost) function:  
π1 = (𝑃−𝑐)𝑞1 = (𝑎−𝑏(𝑞1 + 𝑞2) −𝑐)𝑞1 
π2 = (𝑃−𝑐)𝑞2 = (𝑎−𝑏(𝑞1 + 𝑞2) −𝑐)𝑞2 
In a Stackelberg game, the leader chooses their decision first and the follower adopts the best 
response. Often, there is a first-mover advantage.  
The follower’s response will be optimised based on the leader’s decision (𝑞1).

![Page 1](../course.material/figs/Dynamic%20games-2/page_001.png)

---

## Page 2

Classification: In-Confidence 
𝑑𝜋2
𝑑𝑞2
= 𝑎−𝑏(𝑞1 + 2𝑞2) −𝑐= 0 
𝑞2 = 𝑎−𝑐−𝑏𝑞1
2𝑏
 
The leader makes their move assuming an optimal response by the follower: 
𝜋1 = (𝑎−𝑏(𝑞1 + 𝑎−𝑐−𝑏𝑞1
2𝑏
) −𝑐) 𝑞1 
The optimal quantities are: 
𝑞1
∗= 𝑎−𝑐
2𝑏,
𝑞2
∗= 𝑎−𝑐
4𝑏 
This may be compared to the other major economic game-theoretic model, the Cournot model, 
which assumes simultaneous decisions, resulting in: 
𝑞1
∗= 𝑎−𝑐
3𝑏,
𝑞2
∗= 𝑎−𝑐
3𝑏

![Page 2](../course.material/figs/Dynamic%20games-2/page_002.png)

---

