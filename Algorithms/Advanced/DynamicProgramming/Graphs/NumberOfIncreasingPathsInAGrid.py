"""
https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.



Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2281 ms
# Beats
# 66.51%
# Memory
# 119 MB
# Beats
# 27.19%
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(grid), len(grid[0])

        @cache
        def dfs(i, j):
            result = 1
            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                i1, j1 = i + di, j + dj
                if i1 < 0 or i1 >= n or j1 < 0 or j1 >= m:
                    continue
                if grid[i1][j1] >= grid[i][j]:
                    continue
                result += dfs(i1, j1) % MOD
            return result

        result = 0
        for i in range(n):
            for j in range(m):
                result += dfs(i, j)
                result %= MOD

        return result

# Runtime
# 2362 ms
# Beats
# 59.23%
# Memory
# 34.8 MB
# Beats
# 77.19%
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/editorial/
# class Solution:
#     def countPaths(self, grid: List[List[int]]) -> int:
#         MOD = 10 ** 9 + 7
#         n, m = len(grid), len(grid[0])
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#         dp = [[1] * m for _ in range(n)]
#         cells = [[i, j] for i in range(n) for j in range(m)]
#         cells.sort(key=lambda x: grid[x[0]][x[1]])
#         for i, j in cells:
#             for di, dj in directions:
#                 i1, j1 = i + di, j + dj
#                 if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] > grid[i][j]:
#                     dp[i1][j1] += dp[i][j]
#                     dp[i1][j1] %= MOD
#         return sum(sum(row) for row in dp) % MOD


# Runtime
# 2105 ms
# Beats
# 86.41%
# Memory
# 118.7 MB
# Beats
# 29.61%
# https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/editorial/
# class Solution:
#     def countPaths(self, grid: List[List[int]]) -> int:
#         MOD = 10 ** 9 + 7
#         n, m = len(grid), len(grid[0])
#         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         @cache
#         def dfs(i, j):
#             result = 1
#             for di, dj in directions:
#                 pi, pj = i + di, j + dj
#                 if 0 <= pi < n and 0 <= pj < m and grid[pi][pj] < grid[i][j]:
#                     result += dfs(pi, pj) % MOD
#             return result
#
#         return sum(dfs(i, j) for i in range(n) for j in range(m)) % MOD


tests = [
    [[[1,1],[3,4]], 8],
    [[[1],[2]], 3]
]

run_functional_tests(Solution().countPaths, tests)
