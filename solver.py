import numpy as np

class Solver():
    def __init__(self, A):
        self.matrix = A
        self.sol = np.array([])

    def solve(self):
        if len(self.matrix) == 0: return None
        if len(self.matrix[0]) == 0: return None

        m, n = len(self.matrix), len(self.matrix[0])
        X = []
        for i in range(1, m):
            diff_expected_val = []
            for j in range(n):
                diff_expected_val.append(self.matrix[0][j] - self.matrix[i][j])
            X.append(diff_expected_val)
        X = np.array(X + [[1] * n])
        Y = np.array([0] * (m - 1) + [1])

        try:
            X_inv = np.linalg.inv(X)
            self.sol = X_inv @ Y
        except:
            # raise Warning("X is not invertible. The system is not solvable")
            return None


