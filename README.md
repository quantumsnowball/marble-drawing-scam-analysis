# Marble Drawing Scam Analysis

## The Original Game
One day my friend sent me the follow image and ask if this gambling game is even legit. It is a gambling game about marbles drawing, so we should be able to see if it is a scam by using simple maths and probability theory.

![original.jpg](original.jpg)

## Rules
1. A price of $20 can play this game 10 times
1. Each time darw 12 marbles from a pool of 24 marbles having 8 reds, 8 whites, and 8 blues respectively
2. Count the number of marbles that belong to each of the 3 color, then arrange the counts in descending order
3. Receive the corresponding rewards according to the payoff table
```python
rewards = {
    '840': +300,
    '831': +100,
    '822': +120,
    '750': +60,
    '741': +40,
    '732': +15,
    '660': +100,
    '651': +10,
    '642': +5,
    '633': +5,
    '552': +5,
    '543': -30,
    '444': +5,
}
```
The `543` case corresponds to a negative number, meaning that when the result matches this case, the player will be punished instead of being rewarded.

## Probability
As this game has very clear finite outcomes in its probability spaces, we can easily calculate the probabilities of each of these payoff cases, which should sum up to 1.

### Calculation
For detail analysis please refer to [probability.ipynb](https://github.com/quantumsnowball/marble_drawing_scam_analysis/blob/master/probability.ipynb) and [original.py](https://github.com/quantumsnowball/marble_drawing_scam_analysis/blob/master/original.py)

## Expected Rewards
After calculating the probabilities for each of these outcomes, we simply multiple the payoffs to get the expected rewards for each outome, and sum them up to get the average reward for playing this game. Player's expected rewards can be calculated by subtracting the average cost of playing the game from the expected reward. Then we can judge if this is a fair game or not.

### Calculation
For detail analysis please refer to [probability.ipynb](https://github.com/quantumsnowball/marble_drawing_scam_analysis/blob/master/probability.ipynb) and [original.py](https://github.com/quantumsnowball/marble_drawing_scam_analysis/blob/master/original.py)

## Simulation
There is another way to get the probabilities for all cases, and it is by simulation. Please refer to [simulation.ipynb](https://github.com/quantumsnowball/marble-drawing-scam-analysis/blob/master/simulation.ipynb) for details.

## Conclusion
As proved in [probability.ipynb](https://github.com/quantumsnowball/marble-drawing-scam-analysis/blob/master/probability.ipynb), on average the player is lossing 12 dollars on every play. Clearly this game is a scam. This is because the player is having close to 49% of getting case `543` which corresponds to a punishment of $30. Although in some cases player may win more $100 - $300, but these are extremely rare cases. Without indepth calculation, the player may think that these events are equally likely to occure, but we have shown that this is far from being true. It is this huge difference in perception which makes this game a scam.

## Improvement on the Game
While the reward levels for this game may not be on a very good setting, thus it is possible to fine tune the rewards to make this game more interesting and exciting. The biggest problem is that the player of the original game tend to lose money very quickly. He will soon realize that there is something wrong with this game. Soon he will quit the game with or without know the real reason.

### Re-designing the game
If we are going to improve this game, I will propose the following improvement:
1. Avoid punishing the player by removing the negative reward case
2. Let the player have the feeling of winning big if he doesn't know the real probabilities
3. Adjust the fee of the game to keep an overall positive expected return for the house

### New Rewards
```python
rewards={
    '543': 1, 
    '444': 2, 
    '642': 4, 
    '633': 8, 
    '552': 16, 
    '732': 32, 
    '651': 64, 
    '741': 128, 
    '831': 256, 
    '750': 512, 
    '822': 1024, 
    '660': 2048, 
    '840': 4096
},
```
We have removed the negative punishment case and make it pay a $1 rewards, the player will feel better since he is guaranteed to collect rewards everytime. We also increase the maximum reward for the very rare cases. This will give the player an illusion that he can win big sometimes, but in fact this happen far less likely than he can imagine.

### Implementation
Detail implementation of the re-designed game is documentated in [new_game_3_colors.ipynb](https://github.com/quantumsnowball/marble-drawing-scam-analysis/blob/master/new_game_3_colors.ipynb) and [game.py](https://github.com/quantumsnowball/marble-drawing-scam-analysis/blob/master/game.py). As the implementaion is generic, you can also create a completely different version of the game. E.g. you can incresae the total number of color and create a 4-colors marble drawing game as shown in [new_game_4_colors.ipynb](https://github.com/quantumsnowball/marble-drawing-scam-analysis/blob/master/new_game_4_colors.ipynb)