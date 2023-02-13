"""
https://leetcode.com/problems/regions-cut-by-slashes/

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.



Example 1:


Input: grid = [" /","/ "]
Output: 2
Example 2:


Input: grid = [" /","  "]
Output: 1
Example 3:


Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.


Constraints:

n == grid.length == grid[i].length
1 <= n <= 30
grid[i][j] is either '/', '\', or ' '.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def regionsBySlashes(self, grid: List[str]) -> int:
#         n, m = len(grid), len(grid[0])
#         # rank_h = [[1 for _ in range(m)] for _ in range(n+1)]
#         # rank_v = [[1 for _ in range(m+1)] for _ in range(n)]
#         K = (n + 1) * (m + 1) * 2
#         rank = [1 for _ in range(K)]
#         p = list(range(K))
#
#         def index(i, j, type):
#             nonlocal n, m
#             return (n+1) * (m+1) * type + i * (m+1) + j
#
#         def vertical_left(i, j):
#             return index(i, j, 1)
#
#         def vertical_right(i, j):
#             return index(i, j+1, 1)
#
#         def horizontal_top(i, j):
#             return index(i, j, 0)
#
#         def horizontal_bottom(i, j):
#             return index(i+1, j, 0)
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j):
#             i = get(i)
#             j = get(j)
#             if rank[i] >= rank[j]:
#                 rank[i] += 1
#                 p[j] = p[i]
#             else:
#                 rank[j] += 1
#                 p[i] = p[j]
#
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == '\\':
#                     connect(horizontal_top(i, j), vertical_right(i, j))
#                     connect(horizontal_bottom(i, j), vertical_left(i, j))
#                     # connect(index(i, j, 0), index(i, j+1, 1))
#                     # connect(index(i+1, j, 0), index(i+1, j, 1))
#                 elif grid[i][j] == '/':
#                     connect(horizontal_top(i, j), vertical_left(i, j))
#                     connect(horizontal_bottom(i, j), vertical_right(i, j))
#                     # connect(index(i, j, 0), index(i, j, 1))
#                     # connect(index(i+1, j, 0), index(i, j+1, 1))
#                 else:
#                     connect(horizontal_top(i, j), vertical_left(i, j))
#                     connect(horizontal_top(i, j), vertical_right(i, j))
#                     connect(horizontal_bottom(i, j), vertical_left(i, j))
#                     connect(horizontal_bottom(i, j), vertical_right(i, j))
#                     # connect(index(i, j, 0), index(i, j, 1))
#                     # connect(index(i + 1, j, 0), index(i, j + 1, 1))
#                     # connect(index(i, j, 0), index(i, j + 1, 1))
#
#         unions = set()
#         for i in range(K):
#             unions.add(get(i))
#
#         return len(unions)


# Runtime
# 152 ms
# Beats
# 88.70%
# Memory
# 14.2 MB
# Beats
# 80.40%
# https://leetcode.com/problems/regions-cut-by-slashes/solutions/205641/regions-cut-by-slashes/
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        K = 4 * n * n
        rank = [1 for _ in range(K)]
        p = list(range(K))

        def get(i):
            while i != p[i]:
                i = p[i]
            return i

        def connect(i, j):
            i = get(i)
            j = get(j)
            if rank[i] >= rank[j]:
                rank[i] += 1
                p[j] = p[i]
            else:
                rank[j] += 1
                p[i] = p[j]

        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                if grid[i][j] in '\\ ':
                    connect(root + 0, root + 2)
                    connect(root + 1, root + 3)
                if grid[i][j] in '/ ':
                    connect(root + 0, root + 1)
                    connect(root + 2, root + 3)
                if i + 1 < n: connect(root + 3, root+4*n + 0)
                if i - 1 >= 0: connect(root + 0, root-4*n + 3)
                if j + 1 < n: connect(root + 2, root+4 + 1)
                if j - 1 >= 0: connect(root + 1, root-4 + 2)

        return sum(p[x] == x for x in range(4*n*n))


tests = [
    [[" /","/ "], 2],
    [[" /","  "], 1],
    [["/\\","\\/"], 5],
]

run_functional_tests(Solution().regionsBySlashes, tests)
