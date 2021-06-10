"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3764/
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.



Example 1:


Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:

Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 240 ms, faster than 5.10% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.4 MB, less than 90.91% of Python3 online submissions for Max Area of Island.
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         max_area = 0
#         visited = [[False] * m for _ in range(n)]
#
#         def visit_island(i: int, j: int) -> int:
#             nonlocal n, m, grid, visited
#             deltas = [
#                 [1, 0],
#                 [-1, 0],
#                 [0, 1],
#                 [0, -1]
#             ]
#             to_visit = [[i, j]]
#             area = 0
#             while to_visit:
#                 [i, j] = to_visit.pop()
#                 visited[i][j] = True
#                 area += 1
#                 for [di, dj] in deltas:
#                     i1, j1 = i + di, j + dj
#                     if 0 <= i1 < n and 0 <= j1 < m:
#                         if grid[i1][j1] == 1 and not visited[i1][j1] and [i1, j1] not in to_visit:
#                             to_visit.append([i1, j1])
#             return area
#
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] != 1:
#                     continue
#                 if visited[i][j]:
#                     continue
#                 area = visit_island(i, j)
#                 max_area = max(max_area, area)
#         return max_area


# Runtime: 180 ms, faster than 9.94% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.5 MB, less than 86.15% of Python3 online submissions for Max Area of Island.
# Runtime: 148 ms, faster than 44.75% of Python3 online submissions for Max Area of Island.
# Memory Usage: 14.5 MB, less than 86.15% of Python3 online submissions for Max Area of Island.
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nm = n * m

        def make_set():
            r = [0] * (nm)
            p = [0] * (nm)
            w = [0] * (nm)
            for i in range(nm):
                x, y = i % m, i // m
                p[i] = i
                if grid[y][x] == 1:
                    w[i] = 1
            return r, p, w

        def find_set(x: int):
            nonlocal p, r
            while p[x] != x:
                x = p[x]
            return p[x]

        def union(x: int, y: int):
            nonlocal p, r, w
            if p[x] == p[y]:
                return

            if r[x] > r[y]:
                p[y] = x
                w[x] += w[y]
            else:
                p[x] = y
                w[y] += w[x]
                if r[x] == r[y]:
                    r[y] += 1

        r, p, w = make_set()

        for i in range(nm):
            x, y = i % m, i // m
            if grid[y][x] != 1:
                continue
            if x+1 < m and grid[y][x+1] == 1:
                union(find_set(i), find_set(i+1))
            if y+1 < n and grid[y+1][x] == 1:
                union(find_set(i), find_set(i+m))

        return max(w)


# WRONG
# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         nm = n * m
#
#         def make_set():
#             r, p, w = [0] * (nm), [0] * (nm), [0] * (nm)
#             for i in range(nm):
#                 x, y = i % m, i // m
#                 p[i] = i
#                 if grid[y][x] == 1:
#                     w[i] = 1
#             return r, p, w
#
#         def find_set(x: int):
#             nonlocal p, r
#             while p[x] != x:
#                 x = p[x]
#             return p[x]
#
#         def union(x: int, y: int):
#             nonlocal p, r, w
#             if p[x] == p[y]:
#                 return
#
#             if r[x] > r[y]:
#                 p[y] = x
#                 w[x] += w[y]
#             else:
#                 p[x] = y
#                 w[y] += w[x]
#                 if r[x] == r[y]:
#                     r[y] += 1
#
#         r, p, w = make_set()
#         max_w = 0
#
#         for i in range(nm):
#             x, y = i % m, i // m
#             if grid[y][x] != 1:
#                 continue
#             if x+1 < m and grid[y][x+1] == 1:
#                 union(find_set(i), find_set(i+1))
#                 max_w = max(max_w, w[p[i+1]])
#             if y+1 < n and grid[y+1][x] == 1:
#                 union(find_set(i), find_set(i+m))
#                 max_w = max(max_w, w[p[i+m]])
#
#             max_w = max(max_w, w[p[i]])
#
#         return max_w


tests = [
    [
        [[1,1,0,1,0,0,1,1],
         [0,1,0,1,1,1,1,0],
         [1,1,1,1,0,0,0,1]], 14
    ],
    [
        [
            [1, 1],
            [1, 1]
        ],
        4
    ],
    [
        [
            [1,0,1],
            [1,1,1],
            [0,0,1]
        ],
        6
    ],
    [
        [[1,1,0,0,0],
         [1,1,0,0,0],
         [0,0,0,1,1],
         [0,0,0,1,1]],
        4
    ],
    [
        [[0,0,1,0,0,0,0,1,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,1,1,0,1,0,0,0,0,0,0,0,0],
         [0,1,0,0,1,1,0,0,1,0,1,0,0],
         [0,1,0,0,1,1,0,0,1,1,1,0,0],
         [0,0,0,0,0,0,0,0,0,0,1,0,0],
         [0,0,0,0,0,0,0,1,1,1,0,0,0],
         [0,0,0,0,0,0,0,1,1,0,0,0,0]],
        6
    ],
    [
        [[0,0,0,0,0,0,0,0]],
        0
    ]
]

run_functional_tests(Solution().maxAreaOfIsland, tests, input_metric=lambda test: len(test[0])*len(test[0][0]))