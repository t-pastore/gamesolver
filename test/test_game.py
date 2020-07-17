import unittest

from numpy.random import randint, uniform
from ..game import Game
from ..solution import Solution

class TestGame(unittest.TestCase):
    def testGame(self):
        m, n = randint(2, 5), randint(2, 5)
        A, B = randint(-10, 10, (m, n)), randint(-10, 10, (m, n))
        G = Game(A, B)
        G.solve()

    def testSolution(self):
        a, b = uniform(0, 1), uniform(0,1)
        S = Solution()
        S.appendPureNE(((0, 1), (1, 0)))
        S.appendMixedNE((a, b))
        print(S.pureNE)
        print(S.mixedNE)

if __name__=='__main__':
    unittest.main()