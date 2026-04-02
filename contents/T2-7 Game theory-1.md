# T2-7 Game theory-1

*Converted from PDF: T2-7 Game theory-1.pdf*

---

## Page 1

Game Theory
ENEL445 Applied Engineering Optimisation
2025

![Page 1](../course.material/figs/T2-7%20Game%20theory-1/page_001.png)

---

## Page 2

Game Theory
●
Game theory is the mathematical analysis of decision 
making.
●
The interaction between two or more players is framed in 
terms of a game with a particular set of rules. 
●
Of interest may be the strategies that give optimal outcomes 
for each of the players or, conversely, the resulting outcomes 
when certain strategies are played.
●
Game theory came to prominence in the latter half of the 
twentieth century. Has led to several Nobel Prizes in 
economics, as well as significant advances in biology, 
computer science, and political science.

![Page 2](../course.material/figs/T2-7%20Game%20theory-1/page_002.png)

---

## Page 3

Game Theory
●
Examples of games: 
■
Driving game - Drivers manoeuvring in heavy traffic 
■
Auctioning game - Shoppers bidding on TradeMe
■
Bargaining game - Unions negotiating
■
Political game - Candidates in an election
■
Economic game - Supermarkets deciding prices
●
A game is being played whenever humans interact!
“Antony and Cleopatra played the courting game on a grand scale. 
Bill Gates made himself immensely rich by playing the computer 
software game. Hilter and Stalin played a game that killed off a 
substantial fraction of the world’s population. Kruschev and 
Kennedy played a game during the Cuban missile crisis that might 
have wiped us out altogether.”
Game Theory - A Very Short Introduction. K. Binmore

![Page 3](../course.material/figs/T2-7%20Game%20theory-1/page_003.png)

---

## Page 4

●
With such a wide field of application, game theory would be a 
universal panacea if it could always predict how people will 
play the many games of which social life largely consists.
●
Game theory isn’t able to solve all of the world's problems 
because it only works when people play games rationally.
●
So Game theory can’t predict the behaviour of love-sick 
teenagers or crazy political persons.
●
However people don’t always behave irrationally. Most of us 
at least try to spend our money sensibly - and we don’t do 
too badly most of the time or economic theory wouldn’t work 
at all.
Game Theory

![Page 4](../course.material/figs/T2-7%20Game%20theory-1/page_004.png)

---

## Page 5

●
Game theory was applied to design the rules that were used 
for the US and British governments to auction off the right to 
various radio frequencies for use with cell phones.
●
The result was that the American taxpayer made a profit of 
$20 billion - more than twice the prediction. Even more was 
made in a later British telecom auction of $35 billion in just 
one auction.
Game Theory

![Page 5](../course.material/figs/T2-7%20Game%20theory-1/page_005.png)

---

## Page 6

Example - Prisoner's Dilemma
●
The police have captured two criminals and are interrogating 
them in separate rooms, so they can't communicate with 
each other. The police offer each the following deal:
■
If A snitches on B, A goes free and B spends 20 years 
in jail. (A defects, B cooperates)
■
If B snitches on A, B goes free and A spends 20 years 
in jail. (A cooperates, B defects)
■
If neither of them snitch on each other, then they both 
spend one year in jail. (Mutual cooperation)
■
If they both snitch on each other, then they both 
spend 5 years in jail. (Mutual defection)
Payoff 
Matrix
A
B

![Page 6](../course.material/figs/T2-7%20Game%20theory-1/page_006.png)

---

## Page 7

Example - Prisoner's Dilemma
●
Assume that there is no “honour among thieves” and each 
prisoner only cares about minimising their own jail time.
●
Let’s assume the role of A. We're looking to minimise our 
prison time. Since we have no way of knowing whether our 
partner in crime has confessed, let’s first assume that they 
have not. If A doesn't confess either, both will go to prison for 
1 year. Not bad. But, if A confesses, he will go free, while his 
partner rots away in jail. From the above discussion, it is 
obvious that if B does not confess, A is definitely better off 
confessing.
A
B

![Page 7](../course.material/figs/T2-7%20Game%20theory-1/page_007.png)

---

## Page 8

Example - Prisoner's Dilemma
●
Now let’s look at the other possibility. Say B confesses. If A 
does not confess, he will go to jail for 20 years. But if he 
does confess, he will get only 5 years in prison. It is clearly 
better to confess in this case as well.
●
Is each prisoner better off confessing? It may seem so from 
the above discussion, but if we look at the payoff matrix, it is 
clear that the best payoff for both prisoners is when neither 
confesses! But game theory advocates that both confess.
A
B

![Page 8](../course.material/figs/T2-7%20Game%20theory-1/page_008.png)

---

## Page 9

Example - Prisoner's Dilemma
●
Can be generalised to any situation when two players are in 
a non-cooperative situation where the best all-around 
situation is for both to cooperate, but the worst individual 
outcome is to be cooperating while the other player defects.
●
On the one hand, it is tempting to defect, or confess. Since 
you have no way of influencing the other player's decision, 
no matter what they do, you're better off confessing. But on 
the other hand, you're both in the same boat. Both of you 
should be sensible enough to realise that cheating 
undermines the common good.
●
There is no single "right" solution to the Prisoner's Dilemma 
(that's why it's a dilemma). Its implications carry into 
psychology, economics, and many other fields.
https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/discussion.html

![Page 9](../course.material/figs/T2-7%20Game%20theory-1/page_009.png)

---

## Page 10

●
Formally, the minimax theorem states for a concave-convex 
function f:
Minimax

![Page 10](../course.material/figs/T2-7%20Game%20theory-1/page_010.png)

---

## Page 11

Maxi mini things
●
Maximax
●
Maximin
●
Minimax
●
Minimin(?)
https://cs.stanford.edu/people/eroberts/courses/soco/projects/1998-99/game-theory/Minimax.html

![Page 11](../course.material/figs/T2-7%20Game%20theory-1/page_011.png)

---

## Page 12

Maximax
●
Choose the best of the best possible outcomes.
●
Example Game: Two players simultaneously put either a blue or 
a red card on the table. 
■
If player 1 puts a red card on the table, whichever card 
player 2 puts down, no one wins anything. 
■
If player 1 puts a blue card on the table and player 2 puts 
a red card, then player 2 wins $1000 from player 1.
■
If player 1 puts a blue card on the table and player 2 puts 
a blue card down, then player 1 wins $1000 from player 
2.

![Page 12](../course.material/figs/T2-7%20Game%20theory-1/page_012.png)

---

## Page 13

Maximax
●
Applying the maximax principle: Player 1 will always play the 
blue card, since it has the maximum possible payoff of 1000. 
But as can be clearly seen from the table, assuming player 2 is 
rational, they will never play the blue card, since the red card 
gives him the dominant strategy. In such a case, if player 1 
plays by the maximax rule, player 1 will always lose.
●
The maximax principle is inherently irrational, as it does not take 
into account the other player's possible choices. Maximax is 
often adopted by naive decision-makers.

![Page 13](../course.material/figs/T2-7%20Game%20theory-1/page_013.png)

---

## Page 14

Maximin
●
Choose the best of the worst possible outcomes.
●
Maximin is a one-person game strategy.
●
Example Game: A player has only two choices to make - to 
gamble or not to gamble:
●
Applying the maximin principle: The player should never 
gamble, because he faces a risk of losing $1.

![Page 14](../course.material/figs/T2-7%20Game%20theory-1/page_014.png)

---

## Page 15

Minimax - One-person
●
Example Game: A company is trying to decide whether or not it 
should support a research project. Assume that the research 
project costs c units. If it succeeds, it will bring in a return of r 
units. If it fails, it will not bring in anything.
●
Reformulate the payoff matrix to a regret matrix

![Page 15](../course.material/figs/T2-7%20Game%20theory-1/page_015.png)

---

## Page 16

●
If the company supports the research and it fails, the company's 
regret will be c, the price of research. If the company supports 
the research and it succeeds, the company will have no regrets. 
If the company neglects research and it would have succeeded, 
its regret value is r-c, the return on the research.
●
The objective is to minimise the maximum possible regret.
Minimax - One-person

![Page 16](../course.material/figs/T2-7%20Game%20theory-1/page_016.png)

---

## Page 17

●
Applying the Minimax principle:
■
If (r-c) > c, the company should support research.
■
If (r-c) < c, the company should not support research.
●
In other words, the company should support research if c < r/2, 
i.e., if the expected return on research is more than twice its 
cost.
Minimax - One-person

![Page 17](../course.material/figs/T2-7%20Game%20theory-1/page_017.png)

---

## Page 18

●
Example Game: A received reports that B's convoy would be 
heading to reinforce their troops. The convoy could take one of 
two routes - the Northern or the Southern route. A have to 
decide where to disperse their reconnaissance aircraft - in the 
north or the south - in order to spot the convoy as early as 
possible.
●
The following payoff matrix shows the possible decisions made 
by A and B, with the outcomes expressed in the number of days 
of bombing A could achieve with each possibility
Minimax - Two-person
B
A

![Page 18](../course.material/figs/T2-7%20Game%20theory-1/page_018.png)

---

## Page 19

●
Applying the Minimax principle: To minimise the worst possible 
outcome, A would have to choose the north. This ensures them 
2 days of bombing, whereas they risk only 1 day of bombing if 
they focus on the south. Therefore, by minimax, the best 
strategy for A would be to focus on the north.
●
B can use the same strategy. The worst possible outcome for 
them is the 3 days of bombing which might occur if they took the 
southern route. Therefore, B would take the northern route.
Minimax - Two-person
B
A

![Page 19](../course.material/figs/T2-7%20Game%20theory-1/page_019.png)

---

## Page 20

●
Both A and B settled on the (North, North) square as the best 
outcome for both of them. Neither could do any better if the 
opponent was rational. In this case, the maximin and the 
minimax strategies produce the same result.
●
Nash equilibrium - A set of strategies for which no players can 
improve their payoffs by changing their strategies.
Minimax - Two-person
B
A

![Page 20](../course.material/figs/T2-7%20Game%20theory-1/page_020.png)

---

## Page 21

Mixed Strategies and Randomisation
●
In some cases, there is no saddle point, and the players have 
to choose their strategies with a degree of randomness.
●
Example Game: "Matching Pennies" Two players 
simultaneously place a penny on a table, either heads up or 
tails up. If the pennies are facing the same way, player 1 gets 
to keep both pennies. Otherwise, player 2 gets to keep both.

![Page 21](../course.material/figs/T2-7%20Game%20theory-1/page_021.png)

---

## Page 22

Mixed Strategies and Randomisation
●
There is no clearly defined strategy for each player. The best 
way to play is to choose the position of the coin randomly.
●
If either player follows this strategy, then in the long run, the 
payoffs for each will be 0.
●
Notice that if, say, player 1 uses a 50/50 strategy, while player 
2 plays heads 75% of the time, in the long run, both players 
will still have payoffs of 0. 
●
But if player 2 follows the 75/25 strategy, then player 1 can 
easily take advantage of it by playing heads more frequently, 
and therefore winning more frequently. So, it is important for 
each player to not only maintain a random strategy, but to also 
analyse the strategy of the other player.

![Page 22](../course.material/figs/T2-7%20Game%20theory-1/page_022.png)

---

## Page 23

Maxi mini things Summary
●
Maximax principle is ultra-optimistic, expecting the best 
possible payoff - choosing the best of the best possible 
outcomes.
●
Maximin is ultra-pessimistic, expecting the worst possible 
payoff - choosing the best of the worst possible outcomes.
●
Minimax Theorem proven by John Von Neumann
Minimax: Minimise the maximum loss
Maximin: Maximise the minimum gain
●
Nash equilibrium is a set of strategies for which no players 
can improve their payoffs by changing their strategies. In 
general, a game may have multiple Nash equilibria.

![Page 23](../course.material/figs/T2-7%20Game%20theory-1/page_023.png)

---

## Page 24

Game Theory Terminologies
●
Players of a game are said to have perfect information if the 
sequence of moves played by each player is known to all 
players. Combinatorial game is a deterministic game in which 
all players have perfect information e.g. chess, tic-tac-toe
●
A game is said to be solved when the optimal strategy (if one 
exists) is known.
●
Zero-sum game - sum of the payoffs for all players is constant. 
No player can achieve a higher payoff without decreasing the 
payoffs of the other players.
●
Simultaneous game - all players move effectively 
simultaneously e.g. The basic form of the prisoner's dilemma
●
Sequential game - moves are non-simultaneous e.g. Chess 
and tic-tac-toe

![Page 24](../course.material/figs/T2-7%20Game%20theory-1/page_024.png)

---

## Page 25

●
Symmetric games - both players have an identical choice of 
moves to be made simultaneously e.g. prisoner's dilemma
●
Asymmetric games - e.g. cake cutting problem
●
Strict/weakly dominant strategy - a strategy that is always 
better (or worse) than any other, regardless of other players’ 
actions.  I.e. a strategy that always yields a higher payoff 
than any other strategy. 
●
Dynamic games - games that have multiple, sequential in 
time, stages and decisions (e.g. the prisoner’s dilemma is not 
a dynamic game as there is only one decision to make). 
More from Jeremy at the end. 
Game Theory Terminologies

![Page 25](../course.material/figs/T2-7%20Game%20theory-1/page_025.png)

---

## Page 26

Game Theory Example
https://www.youtube.com/watch?v=kaMKInkV7Vs

![Page 26](../course.material/figs/T2-7%20Game%20theory-1/page_026.png)

---

## Page 27

Dynamic games - Jeremy
●
Dynamic games are common in competitive situations in 
real life (e.g. generator bidding in the NZ electricity market).
●
Some examples:
○
Differential games, e.g. Linear Quadratic games
○
Stochastic games (MDP)
●
The Nash equilibrium is the set of strategies of all players for 
which no single player can benefit by deviating from. This 
may or may not lead to a system equilibrium. 
●
In industry, Stackelberg games are often used 
(leader-follower). These are considered dynamic in the 
game theory sense but not in the optimization-based control 
sense (no states).

![Page 27](../course.material/figs/T2-7%20Game%20theory-1/page_027.png)

---

## Page 28

Exercises
●
Look up the terms that are new to you in this lecture and 
understand them.
●
Are there anything that you can think of that can be 
formulated as a game? What are the outcomes of using 
the different maxi, mini strategies?
Thanks!

![Page 28](../course.material/figs/T2-7%20Game%20theory-1/page_028.png)

---

