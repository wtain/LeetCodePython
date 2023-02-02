"""
https://leetcode.com/problems/largest-1-bordered-square/

Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.



Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1


Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#
#         dp = [[[0,0,0,0] for _ in range(m)] for _ in range(n)]
#
#         for i in range(n):
#             dp[i][0][0] = grid[i][0]
#             dp[i][-1][1] = grid[i][-1]
#
#         for j in range(n):
#             dp[0][j][2] = grid[0][j]
#             dp[-1][j][3] = grid[-1][j]
#
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1:
#                     if i > 0:
#                         dp[i][j][0] = dp[i-1][j][0] + 1
#                     if j > 0:
#                         dp[i][j][2] = dp[i][j-1][2] + 1
#
#         for i in range(n-1, -1, -1):
#             for j in range(m-1, -1, -1):
#                 if grid[i][j] == 1:
#                     if i < n-1:
#                         dp[i][j][1] = dp[i+1][j][1] + 1
#                     if j < m-1:
#                         dp[i][j][3] = dp[i][j+1][3] + 1
#
#         return 0


# Runtime
# 176 ms
# Beats
# 83.33%
# Memory
# 14.1 MB
# Beats
# 99.24%
# https://leetcode.com/problems/largest-1-bordered-square/solutions/345334/clean-java-dp-over-100-just-to-store-the-maximum-possibility/
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dpr, dpc = [[0] * (m+1) for _ in range(n+1)], [[0] * (m+1) for _ in range(n+1)]
        dist, mx = 0, 0
        for r in range(1, n+1):
            for c in range(1, m+1):
                if grid[r-1][c-1] == 0:
                    continue
                dpr[r][c] = dpr[r-1][c] + 1
                dpc[r][c] = dpc[r][c-1] + 1
                dist = min(dpr[r][c], dpc[r][c])
                for i in range(dist, 0, -1):
                    if dpr[r][c-i+1] >= i and dpc[r-i+1][c] >= i:
                        mx = max(mx, i*i)
                        break
        return mx


tests = [
    [[[1,1,0],[1,0,1],[1,1,1],[1,1,1],[1,1,1],[1,1,0],[1,1,1],[1,1,0]], 9],
    [[[1,1,1],[1,0,1],[1,1,1]], 9],
    [[[1,1,0,0]], 1],
]

run_functional_tests(Solution().largest1BorderedSquare, tests)
