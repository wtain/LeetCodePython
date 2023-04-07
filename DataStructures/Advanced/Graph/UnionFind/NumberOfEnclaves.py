"""
https://leetcode.com/problems/number-of-enclaves/description/

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.



Example 1:


Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.
Example 2:


Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] is either 0 or 1.
"""
from collections import defaultdict
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#
#         p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1] * m for _ in range(n)]
#
#         def get(i, j):
#             while (i, j) != p[i][j]:
#                 i, j = p[i][j]
#             return i, j
#
#         def connect(i1, j1, i2, j2):
#             i1, j1 = get(i1, j1)
#             i2, j2 = get(i2, j2)
#             if rank[i1][j1] >= rank[i2][j2]:
#                 p[i2][j2] = p[i1][j1]
#                 rank[i1][j1] += rank[i2][j2]
#             else:
#                 p[i1][j1] = p[i2][j2]
#                 rank[i2][j2] += rank[i1][j1]
#
#         for i in range(1, n):
#             i1 = i - 1
#             for j in range(1, m):
#                 j1 = j - 1
#                 if not grid[i][j]:
#                     continue
#                 if grid[i][j1]:
#                     connect(i, j, i, j1)
#                 if grid[i1][j]:
#                     connect(i, j, i1, j)
#
#         for i in range(n):
#             if grid[i][0]:
#                 i0, j0 = get(i, 0)
#                 rank[i0][j0] = 0
#             if grid[i][m-1]:
#                 i0, j0 = get(i, m-1)
#                 rank[i0][j0] = 0
#
#         for j in range(m):
#             if grid[0][j]:
#                 i0, j0 = get(0, j)
#                 rank[i0][j0] = 0
#             if grid[n-1][j]:
#                 i0, j0 = get(n-1, j)
#                 rank[i0][j0] = 0
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 i0, j0 = get(i, j)
#                 if (i0, j0) == (i, j):
#                     result += rank[i0][j0]
#
#         return result


# Runtime
# 1035 ms
# Beats
# 9.13%
# Memory
# 19.5 MB
# Beats
# 84.69%
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#
#         p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1] * m for _ in range(n)]
#
#         def get(i, j):
#             while (i, j) != p[i][j]:
#                 i, j = p[i][j]
#             return i, j
#
#         def connect(i1, j1, i2, j2):
#             i1, j1 = get(i1, j1)
#             i2, j2 = get(i2, j2)
#             if rank[i1][j1] >= rank[i2][j2]:
#                 p[i2][j2] = p[i1][j1]
#                 rank[i1][j1] += rank[i2][j2]
#             else:
#                 p[i1][j1] = p[i2][j2]
#                 rank[i2][j2] += rank[i1][j1]
#
#         for i in range(1, n):
#             i1 = i - 1
#             for j in range(1, m):
#                 j1 = j - 1
#                 if not grid[i][j]:
#                     continue
#                 if grid[i][j1]:
#                     connect(i, j, i, j1)
#                 if grid[i1][j]:
#                     connect(i, j, i1, j)
#
#         for i in range(n):
#             if grid[i][0]:
#                 i0, j0 = get(i, 0)
#                 rank[i0][j0] = 0
#             if grid[i][m-1]:
#                 i0, j0 = get(i, m-1)
#                 rank[i0][j0] = 0
#
#         for j in range(m):
#             if grid[0][j]:
#                 i0, j0 = get(0, j)
#                 rank[i0][j0] = 0
#             if grid[n-1][j]:
#                 i0, j0 = get(n-1, j)
#                 rank[i0][j0] = 0
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 i0, j0 = get(i, j)
#                 if rank[i0][j0]:
#                     result += 1
#
#         return result


# Runtime
# 972 ms
# Beats
# 14.72%
# Memory
# 19.3 MB
# Beats
# 85.8%
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#
#         p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1] * m for _ in range(n)]
#
#         def get(i, j):
#             while (i, j) != p[i][j]:
#                 i, j = p[i][j]
#             return i, j
#
#         def connect(i1, j1, i2, j2):
#             i1, j1 = get(i1, j1)
#             i2, j2 = get(i2, j2)
#             if rank[i1][j1] > rank[i2][j2]:
#                 p[i2][j2] = p[i1][j1]
#             elif rank[i1][j1] < rank[i2][j2]:
#                 p[i1][j1] = p[i2][j2]
#             else:
#                 p[i2][j2] = p[i1][j1]
#                 rank[i1][j1] += 1
#
#         for i in range(1, n):
#             i1 = i - 1
#             for j in range(1, m):
#                 j1 = j - 1
#                 if not grid[i][j]:
#                     continue
#                 if grid[i][j1]:
#                     connect(i, j, i, j1)
#                 if grid[i1][j]:
#                     connect(i, j, i1, j)
#
#         for i in range(n):
#             if grid[i][0]:
#                 i0, j0 = get(i, 0)
#                 rank[i0][j0] = 0
#             if grid[i][m-1]:
#                 i0, j0 = get(i, m-1)
#                 rank[i0][j0] = 0
#
#         for j in range(m):
#             if grid[0][j]:
#                 i0, j0 = get(0, j)
#                 rank[i0][j0] = 0
#             if grid[n-1][j]:
#                 i0, j0 = get(n-1, j)
#                 rank[i0][j0] = 0
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 i0, j0 = get(i, j)
#                 if rank[i0][j0]:
#                     result += 1
#
#         return result


# Runtime
# 790 ms
# Beats
# 37.69%
# Memory
# 81.7 MB
# Beats
# 31.11%
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         def dfs(i, j):
#             nonlocal n, m
#             grid[i][j] = 0
#             found_bound = i in [0, n-1] or j in [0, m-1]
#             result = 1
#             for di, dj in neighbors:
#                 i1, j1 = i + di, j + dj
#                 if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1]:
#                     res1, fb = dfs(i1, j1)
#                     result += res1
#                     if fb:
#                         found_bound = True
#
#             return result if not found_bound else 0, found_bound
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 result += dfs(i, j)[0]
#
#         return result


# Runtime
# 756 ms
# Beats
# 43.48%
# Memory
# 19.6 MB
# Beats
# 84.69%
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         def dfs(i, j):
#             nonlocal n, m
#
#             to_visit = [(i, j)]
#             found_bound = False
#             result = 0
#
#             while to_visit:
#                 i, j = to_visit.pop()
#                 if not grid[i][j]:
#                     continue
#                 result += 1
#                 grid[i][j] = 0
#                 found_bound = found_bound or i in [0, n-1] or j in [0, m-1]
#
#                 for di, dj in neighbors:
#                     i1, j1 = i + di, j + dj
#                     if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1]:
#                         to_visit.append((i1, j1))
#
#             return result if not found_bound else 0
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 result += dfs(i, j)
#
#         return result


# Runtime
# 810 ms
# Beats
# 34.94%
# Memory
# 15.5 MB
# Beats
# 98.72%
# class Solution:
#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
#
#         def dfs(i, j):
#             nonlocal n, m
#
#             to_visit = {(i, j)}
#             found_bound = False
#             result = 0
#
#             while to_visit:
#                 i, j = to_visit.pop()
#                 result += 1
#                 grid[i][j] = 0
#                 found_bound = found_bound or i in [0, n-1] or j in [0, m-1]
#
#                 for di, dj in neighbors:
#                     i1, j1 = i + di, j + dj
#                     if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] and (i1, j1) not in to_visit:
#                         to_visit.add((i1, j1))
#
#             return result if not found_bound else 0
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if not grid[i][j]:
#                     continue
#                 result += dfs(i, j)
#
#         return result

# Runtime
# 745 ms
# Beats
# 45.44%
# Memory
# 17.5 MB
# Beats
# 87.24%
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):
            nonlocal n, m

            to_visit = [(i, j)]
            found_bound = False
            result = 0
            grid[i][j] = 0

            while to_visit:
                i, j = to_visit.pop()
                result += 1
                found_bound = found_bound or i in [0, n-1] or j in [0, m-1]

                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1]:
                        to_visit.append((i1, j1))
                        grid[i1][j1] = 0

            return result if not found_bound else 0

        result = 0
        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    continue
                result += dfs(i, j)

        return result


tests = [
    [[[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]], 3],
    [[[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]], 0],
    [
        [[0,1,1,0,0,0,0,1,1,0,0,0],[1,0,1,1,1,0,1,0,1,1,1,0],[1,1,0,1,0,0,1,1,0,1,1,1],[1,0,0,1,1,0,1,0,1,0,1,0],[1,0,0,0,0,1,0,0,1,1,0,1],[1,1,1,0,0,0,1,0,0,1,1,1],[1,1,1,0,0,0,0,1,0,1,0,1],[0,1,1,1,1,0,0,1,1,0,0,0],[0,1,0,1,0,1,0,1,0,0,0,1],[0,0,1,0,1,1,0,0,0,1,1,1]],
        10
    ],
    [
        [[0,0,0,1,1,1,0,1,1,1,1,1,0,0,0],[1,1,1,1,0,0,0,1,1,0,0,0,1,1,1],[1,1,1,0,0,1,0,1,1,1,0,0,0,1,1],[1,1,0,1,0,1,1,0,0,0,1,1,0,1,0],[1,1,1,1,0,0,0,1,1,1,0,0,0,1,1],[1,0,1,1,0,0,1,1,1,1,1,1,0,0,0],[0,1,0,0,1,1,1,1,0,0,1,1,1,0,0],[0,0,1,0,0,0,0,1,1,0,0,1,0,0,0],[1,0,1,0,0,1,0,0,0,0,0,0,1,0,1],[1,1,1,0,1,0,1,0,1,1,1,0,0,1,0]],
        27
    ],
]

run_functional_tests(Solution().numEnclaves, tests)
