"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3987/
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/

You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.



Example 1:

Input:
grid =
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
k = 1
Output: 6
Explanation:
The shortest path without eliminating any obstacle is 10.
The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
Example 2:

Input:
grid =
[[0,1,1],
 [1,1,1],
 [1,0,0]],
k = 1
Output: -1
Explanation:
We need to eliminate at least two obstacles to find such a walk.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 40
1 <= k <= m * n
grid[i][j] == 0 or 1
grid[0][0] == grid[m - 1][n - 1] == 0
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         dp = [[[-1] * (k+1) for _ in range(m)] for _ in range(n)]
#         to_visit = [(0, 0, k)]
#         neigh = [(-1,0), (1,0), (0,-1), (0,1)]
#         step = 0
#         while to_visit:
#             next_level = []
#             for i, j, s in to_visit:
#                 dp[i][j][s] = step
#                 for di,dj in neigh:
#                     i1, j1 = i+di, j+dj
#                     if 0 <= i1 < n and 0 <= j1 < m:
#                         s1 = s - grid[i1][j1]
#                         if s1 >= 0:
#                             next_level.append((i1, j1, s1))
#             to_visit = next_level
#             step += 1
#         return min(dp[n-1][m-1])


# WRONG
# class Solution:
#     def shortestPath(self, grid: List[List[int]], k: int) -> int:
#         n, m = len(grid), len(grid[0])
#         BIGVALUE = n * m * k
#         dp = [[[BIGVALUE] * (k+1) for _ in range(m)] for _ in range(n)]
#         dp[0][0][k] = 0
#         for i in range(n):
#             for j in range(m):
#                 for s in range(k+1):
#                     if grid[i][j]:
#                         dp[i][j][]
#         result = min(dp[n - 1][m - 1])
#         if result == BIGVALUE:
#             result -1
#         return result


# Runtime: 68 ms, faster than 92.64% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
# Memory Usage: 15.5 MB, less than 67.38% of Python3 online submissions for Shortest Path in a Grid with Obstacles Elimination.
# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1484735/Python-short-bfs-explained
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        q, v = deque([(0, 0, 0, k)]), set()
        if k >= m+n-2:
            return m+n-2

        while q:
            steps, x, y, k = q.popleft()
            if (x, y) == (n-1,m-1):
                return steps
            for dx, dy in (x, y-1), (x, y+1), (x-1,y), (x+1,y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dx][dy] >= 0:
                    nx = (dx, dy, k - grid[dx][dy])
                    if nx not in v:
                        v.add(nx)
                        q.append((steps+1,) + nx)

        return -1


tests = [
    [
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]],
        1, 6
    ],
    [
[[0,1,1],
 [1,1,1],
 [1,0,0]],
        1, -1
    ]
]

run_functional_tests(Solution().shortestPath, tests)