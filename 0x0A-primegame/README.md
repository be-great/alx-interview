This task involves implementing a function isWinner to determine the winner of a game involving prime numbers between Maria and Ben, played over multiple rounds. Let me break it down step by step.
Game Rules

    Players:
        Maria always goes first.
        Ben plays second.
    Game Setup:
        A set of consecutive integers from 1 to nn is given for each round.
    Moves:
        Players take turns picking a prime number from the set.
        When a prime is chosen, that number and all its multiples are removed from the set.
    Losing Condition:
        The player who cannot make a move loses the game.

Function Prototype
```python
def isWinner(x, nums):
```
- x: Number of rounds to be played.
- nums: An array containing nn, the size of the set, for each round.
## output
*Return the name of the player who won the most rounds.*
*If there's a tie, return None.*

## Exmaple:-
```python

x = 3 # we have three round
num = [4,5,1]
```
```txt
1- Round 1 (n = 4) array = [1,2,3,4]
    - player1 picks 4 => remove 2,4 => [1, 3] => we left with prime numbers
    - player2 picks 3 => remove 3 => [1] we left with prime numbers
    - player1 has no moves then *player2 win* 

2- Round 2 same steps
3- Round 3 same steps
```
