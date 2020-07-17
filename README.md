# Simple implementation of gamesolver module
---
## Example: Rock, Paper, Scissors
---

Consider the famous Rock, Paper, Scissors game. Payoffs for players 1 and 2 are represented through matrices `A` and `B`.


```python
import numpy as np
import gamesolver as gs

A = np.array([
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0]
])

B = - A
```

`Game` is a class that inputs the two payoff matrices and offers different solution methods which are all encapsulated in the `.solve()` method.


```python
G = gs.Game(A, B)
G.solve()
```

`Game` has an object `solution` of class `Solution` which contains the Nash equilibria. Pure strategy Nash equilibria are accessible through `.pureNE` and mixed strategy Nash equilibria are accessible through `.mixedNE`. It outputs a list of tuples of arrays: each tuple represents a pair of optimal strategies for player 1 and 2.


```python
S = G.sol
print(S)  # print an object of class Solution
```

    <gamesolver.solution.Solution object at 0x118bbbf10>



```python
print(S.pureNE)  # print pure Nash equilibria
print(S.mixedNE) # print mixed Nash equilibria
```

    []
    [(array([0.33333333, 0.33333333, 0.33333333]), array([0.33333333, 0.33333333, 0.33333333]))]


There is no pure strategy equilibrium in Rock, Papers, Scissors, and the equilibrium strategy is to play uniformly over the whole set of strategies.

---
## A more complicated example

Consider the following game. Player 1 and 2 have payoff matrices `A` and `B` respectively.


```python
A = np.array([
    [6, 2, 3],
    [2, 7, 4]
])

B = np.array([
    [1, 7, 6],
    [7, 2, 5]
])
```

There is no pure strategy equilibrium in this game. When considering the whole set of strategies, there is no mixed strategy equilibrium neither, because the indifference conditions for player 2 yield incompatible results. One therefore need to check all the strategy supports, \textit{i.e.} columns `(0,1)`, `(0,2)`, `(1,2)` and `(0,1,2)`. Indeed, a restricted set of strategies can yield an equilibrium if the other player anticipate this restriction as optimal.


```python
G = gs.Game(A, B)
G.solve()

print(G.sol.pureNE)
print(G.sol.mixedNE)
```

    []
    [(array([0.28571429, 0.71428571]), array([0.2, 0. , 0.8]))]


Therefore, the optimal strategy for player 1 is to play roughly the first row strategy 28.6% of the time and the second row strategy the rest of the time. Player 2 restricts her set to the first and last columns and play them 20% and 80% of the time respectively.

---
## Time complexity analysis

Time complexity increases exponentially because of the need to check all the supports. Indeed, for `n` strategies, the number of sets of strategies to check is:
\begin{align*}
    \sum_{k=2}^n C_n^k = \sum_{k=1}^n C_n^k - C_n^1 = 2^n - n
\end{align*}

---
## Tests

The module uses `unittest`. To run tests:

`python -m unittest discover`


```python

```
