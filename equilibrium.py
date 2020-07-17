import numpy as np

class Equilibrium():

    def __init__(self, A, B, strat1, strat2):
        self.A = A
        self.B = B
        self.s1 = strat1
        self.s2 = strat2

        self.isNE = True

    def isSustained(self, tolerance_margin=10**(-6)):
        opt_payoff_1 = self.A @ self.s2 @ self.s1
        for i in range(self.A.shape[0]):
            self.isNE = self.A[i] @ self.s2 <= opt_payoff_1 + tolerance_margin
            if not self.isNE: return

        opt_payoff_2 = self.B.T @ self.s1 @ self.s2
        for i in range(self.B.shape[1]):
            self.isNE = self.B.T[i] @ self.s1 <= opt_payoff_2 + tolerance_margin
            if not self.isNE: return



