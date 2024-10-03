# Pascal's Triangle
- Pascal's triangle is an arrangement of binomial coefficient ( is used to denote the number of possible ways to choose a subset of objects of a given numerosity from a larger set ).
- Explain:- 
<img src="pascals-triangle.png">

- Pascal's triangle are placed in such a way that each number is the sum of two numbers just above the number.
## Use:-
- To find the confficients of binomial expansion which is used in probability.
- Example 1: A coin is tossed three times, find the probability of getting exactly 2 tails.

- heads : (H), tails: (T)
- 2^3=8
- These outcomes can be written as:
    HHH, HHT, HTH, HTT, THH, THT, TTH, TTT.
- by looking there is 3 probability to getting exactly 2 tails: HTT, THT, TTH.
- <p>Connecting to Pascal’s Triangle 
 Pascal's Triangle helps us determine how many ways we can get a certain number of heads or tails in multiple tosses. </p>

In 3 tosses, the 4th row of Pascal's Triangle (1, 3, 3, 1) tells us (we don't count the row 0):
   - 1 way to ge 0 tails (HHH).
   - 3 way to get 1 tails (HHT, HTH, THH).
   - 3 way to get 2 tails (HTT, THT, TTH).
   - 1 way to get 3 tails (TTT).

- conclusion : This is why there are 3 ways to get exactly 2 tails.
<p> 3/8 *100% = 37.5% </p>
