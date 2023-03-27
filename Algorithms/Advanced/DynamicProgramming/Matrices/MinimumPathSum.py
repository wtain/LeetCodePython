"""
https://leetcode.com/problems/minimum-path-sum/description/

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.



Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 104 ms
# Beats
# 47.72%
# Memory
# 15.7 MB
# Beats
# 80.67%
# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         dp = [[0] * m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 if not i and not j:
#                     dp[i][j] = grid[i][j]
#                     continue
#                 v = math.inf
#                 if i > 0:
#                     v = min(v, dp[i-1][j])
#                 if j > 0:
#                     v = min(v, dp[i][j-1])
#                 dp[i][j] = v + grid[i][j]
#         return dp[-1][-1]


# Runtime
# 113 ms
# Beats
# 25.97%
# Memory
# 14.7 MB
# Beats
# 92.19%
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[0] * m for _ in range(2)]
        for i in range(n):
            for j in range(m):
                i1 = i % 2
                i2 = 1 - i1
                if not i and not j:
                    dp[i][j] = grid[i][j]
                    continue
                v = math.inf
                if i > 0:
                    v = min(v, dp[i2][j])
                if j > 0:
                    v = min(v, dp[i1][j-1])
                dp[i1][j] = v + grid[i][j]
        return dp[i % 2][-1]


tests = [
    [[[1,3,1],[1,5,1],[4,2,1]], 7],
    [[[1,2,3],[4,5,6]], 12],
]

run_functional_tests(Solution().minPathSum, tests)
