"""
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 508 ms
# Beats
# 38.33%
# Memory
# 14.4 MB
# Beats
# 56.78%
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        p = list(range(n))
        rank = [0] * n

        def get(i: int) -> int:
            while p[i] != i:
                i = p[i]
            return i

        def connect(i: int, j: int):
            i, j = get(i), get(j)
            if rank[i] > rank[j]:
                p[j] = i
            elif rank[j] > rank[i]:
                p[i] = j
            else:
                p[j] = i
                rank[i] += 1

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    connect(i, j)

        provinces = set([get(i) for i in range(n)])

        return len(provinces)


tests = [
    [[[1,1,0],[1,1,0],[0,0,1]], 2],
    [[[1,0,0],[0,1,0],[0,0,1]], 3]
]

run_functional_tests(Solution().findCircleNum, tests)
