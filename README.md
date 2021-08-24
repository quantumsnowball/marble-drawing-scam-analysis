# Marble Drawing Scam Analysis

## The Original Game
One day my friend sent me the follow image and ask if this gambling game is even legit. It is a gambling game about marbles drawing, so we should be able to see if it is a scam by using simple maths and probability theory.

![original.jpg](original.jpg)

## Rules
1. A price of $20 can play this game ten times
1. Each time darw 12 marbles from a pool of 24 marbles having 8 reds, 8 whites, and 8 blues respectively
2. Count the number of marbles that belong to each of the 3 color, then arrange the count in descending order
3. Receive the correspondinly rewards according to the payoff table
```python
payoffs = {
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

## Probability


## Expected Rewards


## Improvement on the Game