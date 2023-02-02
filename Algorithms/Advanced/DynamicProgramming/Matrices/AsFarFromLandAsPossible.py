"""
https://leetcode.com/problems/as-far-from-land-as-possible/

Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land, find a water cell such that its distance to the nearest land cell is maximized, and return the distance. If no land or water exists in the grid, return -1.

The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.



Example 1:


Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
Example 2:


Input: grid = [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 100
grid[i][j] is 0 or 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 707 ms
# Beats
# 53.93%
# Memory
# 16.3 MB
# Beats
# 8.83%
# class Solution:
#     def maxDistance(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         level = [(i, j) for j in range(m) for i in range(n) if grid[i][j]]
#         BigValue = n*m
#         distances = [[BigValue] * m for _ in range(n)]
#         visited = set()
#         for i, j in level:
#             visited.add((i, j))
#             distances[i][j] = 0
#         neighbors = [
#             (1, 0),
#             (-1, 0),
#             (0, 1),
#             (0, -1)
#         ]
#         max_distance = -1
#         while level:
#             next_level = []
#             for i, j in level:
#                 for di, dj in neighbors:
#                     i1, j1 = i + di, j + dj
#                     if 0 <= i1 < n and 0 <= j1 < m and (i1, j1) not in visited and grid[i1][j1] == 0:
#                         visited.add((i1, j1))
#                         distances[i1][j1] = min(distances[i1][j1], distances[i][j]+1)
#                         max_distance = max(distances[i1][j1], max_distance)
#                         next_level.append((i1, j1))
#             level = next_level
#         return max_distance


# Runtime
# 524 ms
# Beats
# 90.81%
# Memory
# 14.3 MB
# Beats
# 97.22%
# https://leetcode.com/problems/as-far-from-land-as-possible/solutions/3043174/as-far-from-land-as-possible/
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        BigValue = n**2+1
        distance = [[BigValue] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    distance[i][j] = 0
                else:
                    distance[i][j] = min(distance[i][j],
                                         distance[i-1][j]+1 if i > 0 else BigValue,
                                         distance[i][j-1]+1 if j > 0 else BigValue)

        max_distance = -1
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                distance[i][j] = min(distance[i][j],
                                     distance[i+1][j]+1 if i < n-1 else BigValue,
                                     distance[i][j+1]+1 if j < n-1 else BigValue)
                max_distance = max(max_distance, distance[i][j])
        return -1 if max_distance == BigValue or max_distance == 0 else max_distance


tests = [
    [[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]], -1],
    [[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]], -1],
    [[[1,0,1],[0,0,0],[1,0,1]], 2],
    [[[1,0,0],[0,0,0],[0,0,0]], 4],
]

run_functional_tests(Solution().maxDistance, tests)
