"""
https://leetcode.com/problems/count-sub-islands/

You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.



Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.


Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 7518 ms
# Beats
# 6.24%
# Memory
# 85.4 MB
# Beats
# 56.54%
# class Solution:
#
#     class UnionFind:
#
#         def __init__(self, grid: List[List[int]]):
#             n, m = len(grid), len(grid[0])
#             self.p = [[(i, j) for j in range(m)] for i in range(n)]
#             self.rank = [[0 for _ in range(m)] for _ in range(n)]
#             neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#             for i in range(n):
#                 for j in range(m):
#                     if not grid[i][j]:
#                         continue
#                     for di, dj in neighbors:
#                         i1, j1 = i + di, j + dj
#                         if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1]:
#                             self.connect(i, j, i1, j1)
#
#         def get(self, i: int, j: int) -> (int, int):
#             while (i, j) != self.p[i][j]:
#                 i, j = self.p[i][j]
#             return i, j
#
#         def connect(self, i1: int, j1: int, i2: int, j2: int):
#             i1, j1 = self.get(i1, j1)
#             i2, j2 = self.get(i2, j2)
#             if self.rank[i1][j1] > self.rank[i2][j2]:
#                 self.p[i2][j2] = (i1, j1)
#             elif self.rank[i1][j1] < self.rank[i2][j2]:
#                 self.p[i1][j1] = (i2, j2)
#             else:
#                 self.rank[i1][j1] += 1
#                 self.p[i2][j2] = (i1, j1)
#
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         n, m = len(grid1), len(grid1[0])
#         uf1, uf2 = Solution.UnionFind(grid1), Solution.UnionFind(grid2)
#
#         notsubislands = set()
#         superislands = defaultdict(set)
#         for i in range(n):
#             for j in range(m):
#                 if not grid2[i][j]:
#                     continue
#                 island2 = uf2.get(i, j)
#                 if not grid1[i][j]:
#                     notsubislands.add(island2)
#                     continue
#                 if island2 in notsubislands:
#                     continue
#                 island1 = uf1.get(i, j)
#                 superislands[island2].add(island1)
#
#         return sum(1 for island in superislands if len(superislands[island]) == 1 and island not in notsubislands)


# Runtime
# 2991 ms
# Beats
# 82.76%
# Memory
# 23.2 MB
# Beats
# 93.31%
# https://leetcode.com/problems/count-sub-islands/solutions/1284306/98-faster-simple-approach-well-explained/
class Solution:

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        n, m = len(grid1), len(grid1[0])

        def destroy(grid2: List[List[int]], i: int, j: int):
            nonlocal n, m
            to_visit = [(i, j)]
            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while to_visit:
                i, j = to_visit.pop()
                grid2[i][j] = 0
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < m and grid2[i1][j1]:
                        to_visit.append((i1, j1))

        for i in range(n):
            for j in range(m):
                if grid2[i][j] and not grid1[i][j]:
                    destroy(grid2, i, j)

        subisland_count = 0
        for i in range(n):
            for j in range(m):
                if grid2[i][j]:
                    destroy(grid2, i, j)
                    subisland_count += 1
        return subisland_count


tests = [
    [[[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]], 3],
    [[[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]], 2],
]

run_functional_tests(Solution().countSubIslands, tests)
