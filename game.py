from .solver import Solver
from .equilibrium import Equilibrium
from .solution import Solution
from .func import *
import numpy as np

class Game:
    def __init__(self, A, B):
        self.A = A
        self.B = B
        self.supp1 = findKComb(A.shape[0])
        self.supp2 = findKComb(B.shape[1])

        self.sol = Solution()


    def findPureNE(self):
        for i in range(self.B.shape[0]):
            col_BR = findMaxIndices(self.B[i])  # best-response of col player
            for j in col_BR:
                if self.A[:, j].argmax() == i:
                    s1, s2 = np.zeros(self.A.shape[0]), np.zeros(self.B.shape[1])
                    s1[i] = 1
                    s2[j] = 1
                    self.sol.appendPureNE((s1, s2))


    def findMixedNE(self):
        for c1 in self.supp1:
            for c2 in self.supp2:
                c1 = list(c1)
                c2 = list(c2)
                A_sub = self.A[:, c2][c1]
                B_sub = self.B[:, c2][c1]

                sA = Solver(A_sub)
                sB = Solver(B_sub.T)

                sB.solve()
                sA.solve()
                s1 = sB.sol
                s2 = sA.sol

                if any(s1 < 0) or any(s2 < 0): continue

                if len(s1) > 0 and len(s2) > 0:
                    opt_strat1, opt_strat2 = np.zeros(self.A.shape[0]), np.zeros(self.B.shape[1])
                    opt_strat1[c1] = s1
                    opt_strat2[c2] = s2
                    eq = Equilibrium(self.A, self.B, opt_strat1, opt_strat2)
                    eq.isSustained()
                    if eq.isNE:
                        self.sol.appendMixedNE((opt_strat1, opt_strat2))


    def solve(self):
        self.findPureNE()
        self.findMixedNE()

