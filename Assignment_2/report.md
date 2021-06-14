# Assignment 2 - Report

**Aakash Aanegola - 2019101009**

**Aakash Jain          - 2019101028**

# Value iteration analysis

## Trace - Main

The result obtained after value iteration is consistent with what we would do in Indiana Jones' situation. 

**Position W**
When Indiana Jones is in the west position, he can only take the actions STAY, RIGHT and SHOOT. The policy obtained after value iteration suggests that we move right if MM is dormant most of the time. This is optimal as the probability that we hit MM with the actions HIT/SHOOT are higher in the centre/east positions. However, he does choose to shoot when he has 3 arrows, and MM health is 25. This is because instead of moving to the east/centre states and risking MM transitioning to the ready state, it is better for him to take a shot from the west state. Moving to the centre state also risks losing all of his arrows, and hence is far from optimal. 

If MM is ready, however, the actions that he takes become smarter. If Indiana has no arrows, then most of the time, he will prefer moving right. This is because staying in the same location has an unbounded total cost, and it is worth risking the damage to IJ to move right and closer to MM to deal damage. However, IJ prefers staying when MMs health is 50 as the utility of MMs health increasing to 75 is a lot less than the gain from moving closer to MM and incurring a step cost. When he has 1 arrow, the utility of keeping the arrow is high when MM's health is 25 (as an arrow has a higher probability of dealing damage than a swing from the sword), and hence he chooses to stay. The same can't be said for when MM's health is 50, as the utility of MM's health decreasing to 25 (given the low probability) is higher than that of staying at 50. When MM's health is 75, and he has only 1 arrow, the combination of SHOOT and HIT can take MM out (ideally), and hence the utility of keeping the arrow is higher than the gain from hitting MM (with low probability). When Indiana has 2 arrows, however, he behaves differently. He will now shoot when MM has 25 and 75 health as he will still have 1 arrow left over after that, and then he can choose the optimal moves given that he has only one arrow. The utility of ending the game early is high, and since the utility of having 1 arrow and health at 25 is also lucrative, he chooses to shoot when MM has health 25 as both the possible states he ends up in have good utilities. However, when MM has 50 health, he chooses to stay as shooting means he loses an arrow and then ends up in a less valuable state than one in which he has two arrows. When he has 3 arrows, however, he will choose to shoot if MM has 100, 50, or 25 health. If MM has 25 health, this means that IJ can choose to shoot twice from the west state and end the game early before prioritizing closeness to MM in order to deliver the final strike. if MM has 50 health, the value of damaging MM and still having 2 arrows is high as he still has an arrow to spare and can end the game, and if that misses can try getting closer to MM to deliver the final strike. When MM has 100 health, it makes sense to shoot as holding three arrows is quite useless even if he gets close to MM as the probability that MM doesn't attack for three consecutive turns after movement is quite low. This means that Indiana chooses to use an arrow in an attempt to make MM's health 75 as that state has higher utility. 

The materials that Indiana has at the west state are inconsequential and don't affect his actions as much as the number of arrows, and hence they do not have much effect on the optimal policy. 

**Position N**

When Indiana is in the north position, and MM is dormant, he chooses to go down if he lacks material. However, if he has material, he will choose to craft arrows. This makes sense as gaining arrows that have a higher probability of doing damage than his sword is better than any other action. Since MM is dormant, it makes sense to get closer to MM to try and deal some damage. However, if he already has 3 arrows, he will choose to go down irrespective of how much material he has. This is because crafting when he has 3 arrows doesn't lead to any benefit, but reduces the material by one which is intrinsically a worse state. However when MM is ready, if he is in the north position and has material, he will choose to craft. This is because crafting is a guaranteed STAY with a cost of 1 material (this doesn't hold if he already has 3 arrows, as MM attacks first, and wasting the material if MM attacks is not worth it). 

**Position E**

In the east position, Indiana's behaviour is fairly predictable. Consider a case where he would seek to avoid an attack from MM. This would entail moving to C, and then to W/S/N and then staying there until MM attacks, after which he would have to return to E in order to return to his original state. This entire process takes a minimum of 4 steps, and there is a 75% probability that he will be attacked anyway, and a 25% probability that he will be attacked when he's in the C position which is a lot worse for him. Hence he chooses to simply shoot or hit based on the state of MM. If he has arrows  he will most often choose to SHOOT as it deals damage. In the case where MM is ready and has a health of 100, it makes more sense to him to HIT as even if he SHOOTs and MM attacks, the state will be reset and he will have 0 arrows. Since HIT deals 50 damage, it makes more sense to HIT and soak up the reward. However, since being at the state where MMs health is 25/50/75 is more valuable than 50/75/100 respectively, he chooses to shoot in order to deal damage or preserve the state based on whether MM attacks or not. 

**Position S**

If Indiana ends up in the south state, then more often than not he will choose to take the action UP. This is because GATHER, UP, UP, CRAFT, DOWN is a total of 5 turns which is too high a penalty to pay for a chance to get arrows. This means that Indiana just uses the GATHER very rarely. Additionally, he uses the STAY action when MM is ready as the teleportation to E is actually desirable. Since crafting/gathering isn't feasible he tends to go to the position E and simply attack MM which means that the chance to be teleported to E is beneficial seeing as MM attacks before Indiana makes a move. 

**Position C**

When Indiana is in the center position, he simply chooses to avoid MM by moving UP (N, W, S would have had very similar values). If MM is dormant, he will choose to move closer to MM in order to land a hit with a higher probability. However, if MM is ready and has 25 health and he has arrows available, he will choose to SHOOT in an attempt to take MM out. 

**Convergence rate**

We know that value iteration converges at a rate of gamma, and this seems to hold. for our error to become sub 0.001 it takes roughly 120 iterations. 

### Policy

The policy starts off with seemingly random moves as the values of the states haven't been set yet. However, after a certain point, we observe that the policy doesn't change much and the error in the value function keeps decreasing. The threshold of 0.001 might be too low, and we might be able to obtain the same policy with fewer iterations if we tweak this value. 

## Task 2.1

In this task we changed the effect of the LEFT action from the east state. Instead of leading Indiana to the centre state it instead takes him to the west position. This however doesn't change the optimal policy as it doesn't benefit Indiana in any way. If he does take the LEFT action from the EAST state in order to avoid MMs attack 50% of the time, he will still have to move back to the center and then back to east to reset his state after waiting for MM to attack at west. This is equivalent to taking a hit from MM and hence is never the optimum action. 

## Task 2.2

Now we see rather erratic behavior. Since the cost for the STAY action is 0, Indiana just chooses to STAY at a position where MM can't reach him. This becomes the terminating state as IJ will not be getting any negative reward and any other action will lead to less reward. The only times he will try and take out MM is when MM has health equal to 25. However, STAYing at N/S is worse than staying at W due to the random probability of being ejected to E. This means that sometimes he will try and go to the south state and then to the west state (optimum terminal state). IJ does choose to craft at north if MMs health is 25 as the arrow can come in handy to end the run. When he is in the east position, he chooses to stay if MMs state is ready and health is 75 at times as it makes sense not to incur any step cost given that the action may be incapacitated. In the south position, the only actions that he takes are STAY and UP as STAYing incurs no penalty, and moving UP makes sense in order to go to the west position and terminate there. 

## Task 2.3

When $\gamma=0.25$ Indiana prefers an immediate reward over the long-term benefit. This is seen in his taking the action SHOOT from the position west. Holding on to the arrow to deal damage with a higher probability later on is a much better alternative but since Indiana discounts the reward he gets later on, he chooses the instant gratification with less probability. He also doesn't recognize that sometimes taking the hit from MM may result in a greater overall reward and chooses to avoid MM ending up at a greater cost. He also chooses to gather materials a lot more than he did before again ignoring the fact that crafting arrows is a very expensive task given that his current position is south. When he is in the south position he chooses to expend his arrows and move away from MM even though that gets him higher cost in the long run. He also chooses to hit even though the probability of landing a hit is very low. 

## Simulation - 1

```python
<MM still dormant>
STATE=(W, 0, 0, D, 100) : ACTION RIGHT : NEW STATE=(('C', '0', '0', 'D', '100')) : SCORE=-20
<MM still dormant>
STATE=(C, 0, 0, D, 100) : ACTION RIGHT : NEW STATE=(('E', '0', '0', 'D', '100')) : SCORE=-40
<MM still dormant>
STATE=(E, 0, 0, D, 100) : ACTION HIT : NEW STATE=(('E', '0', '0', 'D', '100')) : SCORE=-60
<MM still dormant>
STATE=(E, 0, 0, D, 100) : ACTION HIT : NEW STATE=(('E', '0', '0', 'D', '50')) : SCORE=-80
<MM still dormant>
STATE=(E, 0, 0, D, 50) : ACTION HIT : NEW STATE=(('E', '0', '0', 'D', '50')) : SCORE=-100
<MM still dormant>
STATE=(E, 0, 0, D, 50) : ACTION HIT : NEW STATE=(('E', '0', '0', 'D', '50')) : SCORE=-120
<MM still dormant>
STATE=(E, 0, 0, D, 50) : ACTION HIT : NEW STATE=(('E', '0', '0', 'D', '50')) : SCORE=-140
<MM now ready to attack>
STATE=(E, 0, 0, R, 50) : ACTION HIT : NEW STATE=(('E', '0', '0', 'R', '50')) : SCORE=-160
<MM still ready>
STATE=(E, 0, 0, R, 50) : ACTION HIT : NEW STATE=(('E', '0', '0', 'R', '0')) : SCORE=-180
<MM Defeated> STATE=(E, 0, 0, R, 0) : ACTION NONE : SCORE=-130
```

Indiana behaves according to our expectations. He always chooses to move towards MM and attack with whatever he has, in this case only the HIT action. 

## Simulation - 2

```python
<MM Attacked> STATE=(C, 2, 0, D, 100) : ACTION INCAPACITATED : SCORE=-60
<MM now ready to attack>
STATE=(C, 2, 0, R, 100) : ACTION UP : NEW STATE=(('N', '2', '0', 'R', '100')) : SCORE=-80
<MM still ready>
STATE=(N, 2, 0, R, 100) : ACTION CRAFT : NEW STATE=(('N', '1', '2', 'R', '100')) : SCORE=-100
<MM Missed> STATE=(N, 1, 2, D, 100) : ACTION VIABLE : SCORE=-100
STATE=(N, 1, 2, D, 100) : ACTION DOWN : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-120
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-140
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-160
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-180
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-200
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-220
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-240
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-260
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-280
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '100')) : SCORE=-300
<MM still dormant>
STATE=(E, 1, 2, D, 100) : ACTION HIT : NEW STATE=(('E', '1', '2', 'D', '50')) : SCORE=-320
<MM still dormant>
STATE=(E, 1, 2, D, 50) : ACTION SHOOT : NEW STATE=(('E', '1', '1', 'D', '25')) : SCORE=-340
<MM now ready to attack>
STATE=(E, 1, 1, R, 25) : ACTION SHOOT : NEW STATE=(('E', '1', '0', 'R', '0')) : SCORE=-360
<MM Defeated> STATE=(E, 1, 0, R, 0) : ACTION NONE : SCORE=-310
```

In this case again, we follow the expected policy, that is avoid the attack initially, then CRAFT to stay in the state with 100% probability and then go to the east position and attack. However, he preserves the arrows as he realizes that they are worth a lot more when MMs health is low due to their high chance of success. This is because if MM is dormant, it makes sense to get its health down as low as possible before using the arrows. 

# Linear programming

### Creating the A matrix

Creating the A matrix was pretty straightforward. For every state that we can transition to from the current state given an action, we add to the value (outflow) of that state and subtract from the value (inflow) of the state that it ends up in under the column of the state-action pair. The rows of the matrix represent the different states, and the columns represent all the valid state-action pairs. We also factor in the probability that MM transitions from D to R and the probability of MM attacking.  

### Finding the policy

To find the policy we simply select the action that has the highest x value for that particular state. Since we initialized the state with (C, 2, 3, D, 100) the policy isn't defined for some of the states (mainly unreachable west states) as the agent will never reach there under the given policy. The linear programming solution returns a policy very close to that of value iteration and is optimal given the starting state. 

### Multiple policies

If every alpha is strictly positive, then we obtain a singular optimal policy. Since in our case alpha isn't strictly positive it doesn't return the optimal policy for every state (as seen in the actions from the west position). We can get different policies by tweaking alpha as that indicates changing the starting position distribution. Tweaking R also can result in a different policy as the rewards perceived for a given state are different. Changing A is equivalent to changing the MDP itself, and hence isn't a viable way to change the policy (even though it would change it).