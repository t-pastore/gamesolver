from itertools import combinations

### Functions to call

def findKComb(n):
    """
    Find all the 2<=k<=len(supp) combinations in a range
    :param n: int
    :return: List[tuples[int]]
    """
    target = list(range(n))
    res = []
    for k in range(2, n+1):
        c_k = combinations(target, k)
        res += list(c_k)
    return res


def findMaxIndices(nums):
    """
    Find all the indices corresponding to the max element in a list
    :param nums: List[int]
    :return: List[int]
    """
    res = []
    M = max(nums)
    for i in range(len(nums)):
        if nums[i] == M:
            res.append(i)
    return res

