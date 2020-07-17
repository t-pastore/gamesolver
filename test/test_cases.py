import unittest

from ..game import Game
import numpy as np


class TestCasesForGame(unittest.TestCase):
    def testEquality(self, a=None, b=None):
        if a and b:
            self.assertEqual(len(a), len(b))
            for tup_a, tup_b in zip(a, b):
                for arr_a, arr_b in zip(tup_a, tup_b):
                    self.assertTrue((arr_a.round(6) == arr_b.round(6)).all())


    def test1(self):  # Footballer against goalkeeper
        ans = [(np.array([.5, .5]), np.array([.5, .5]))]
        A = np.array([
            [1, 0],
            [0, 1]
        ])
        B = 1 - A
        G = Game(A, B)
        G.solve()
        self.testEquality(G.sol.mixedNE, ans)


    def test2(self): # Rock, paper, scissors
        one_third = 1/3.
        ans = [(np.array([one_third] * 3), np.array([one_third] * 3))]
        A = np.array([
            [0, 1, -1],
            [-1, 0, 1],
            [1, -1, 0]
        ])
        B = - A
        G = Game(A, B)
        G.solve()
        self.testEquality(G.sol.mixedNE, ans)

    def test3(self):
        ans = [(np.array([0.28571429, 0.71428571]), np.array([0.2, 0., 0.8]))]
        A = np.array([
            [6, 2, 3],
            [2, 7, 4]
        ])
        B = np.array([
            [1, 7, 6],
            [7, 2, 5]
        ])
        G = Game(A, B)
        G.solve()
        self.testEquality(G.sol.mixedNE, ans)


    def test4(self):
        ans = [(np.array([1, 0]), np.array([1, 0]))]
        A = np.array([
            [5, 5],
            [0, 0]
        ])
        B = np.array([
            [5, 0],
            [5, 0]
        ])
        G = Game(A, B)
        G.solve()
        self.testEquality(G.sol.pureNE, ans)


if __name__=='__main__':
    unittest.main()