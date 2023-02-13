"""
https://leetcode.com/problems/number-of-closed-islands/

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.



Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation:
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2


Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 173 ms
# Beats
# 22.20%
# Memory
# 15.1 MB
# Beats
# 14.41%
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        p = [[(i, j) for j in range(m)] for i in range(n)]
        rank = [[1 for _ in range(m)] for _ in range(n)]
        touches_borders = [[False for _ in range(m)] for _ in range(n)]

        def get(i, j) -> (int, int):
            while p[i][j] != (i, j):
                i, j = p[i][j]
            return i, j

        def connect(i1, j1, i2, j2):
            i1, j1 = get(i1, j1)
            i2, j2 = get(i2, j2)
            if rank[i1][j1] > rank[i2][j2]:
                p[i2][j2] = p[i1][j1]
            elif rank[i1][j1] < rank[i2][j2]:
                p[i1][j1] = p[i2][j2]
            else:
                rank[i1][j1] += 1
                p[i2][j2] = p[i1][j1]

        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    continue
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < m and not grid[i1][j1]:
                        connect(i, j, i1, j1)

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    continue
                if i == 0 or i == n-1 or j == 0 or j == m-1:
                    pi, pj = get(i, j)
                    touches_borders[pi][pj] = True

        return sum(1 for j in range(m) for i in range(n)
                   if not grid[i][j] and p[i][j] == (i, j) and not touches_borders[i][j])


tests = [
    [[[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]], 2],
    [[[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]], 1],
    [
               [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
        , 2
    ],
    [
        [
            [1,0,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,1,1,1,1,1,1],
            [0,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,0,0],
            [1,0,1,1,0,1,1,1,1,0,1,0,0,1,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1],
            [0,0,1,1,0,0,1,1,0,1,0,0,1,1,1,1,1,0,1,0,1,0,0,1,0,0,1,1,1,0],
            [0,1,0,0,1,0,1,1,0,0,0,1,1,0,1,1,1,0,1,0,0,1,0,1,1,1,0,0,0,1],
            [0,0,1,1,0,0,0,1,0,1,0,0,0,0,0,1,1,1,1,1,1,0,0,1,1,0,1,0,1,0],
            [1,1,1,0,1,1,1,1,1,0,0,1,0,0,0,1,1,0,1,1,1,0,0,0,0,0,0,0,1,1],
            [0,0,1,0,0,1,0,1,1,1,1,0,0,1,1,1,0,1,1,0,1,1,0,0,0,1,1,0,0,0],
            [1,1,1,1,0,0,0,1,1,1,0,0,1,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,0],
            [0,1,1,1,0,1,0,1,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1],
            [0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,1,0,0,1],
            [0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,0],
            [0,0,1,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1],
            [1,0,0,0,0,0,1,1,1,0,0,0,1,1,1,1,1,1,1,1,0,0,0,1,1,1,0,1,0,1],
            [1,1,0,1,1,1,0,1,1,0,1,0,0,1,0,1,0,1,0,1,0,1,1,1,0,0,0,1,0,1],
            [0,0,1,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,0],
            [1,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,0,1,1,1,0,1,0,1,1,1],
            [0,1,1,0,0,1,0,0,1,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1],
            [1,0,1,0,1,0,0,0,1,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,1,0,1,1,0,1],
            [0,1,0,1,0,0,1,0,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,1,1,0,0,0,1],
            [0,1,0,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,0,1,1,1,1,0,1,0],
            [1,0,0,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,0,0,1,1,0,1],
            [0,0,1,1,1,1,0,1,1,1,0,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1,1,0,0,0],
            [0,0,0,0,1,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,1,1,1,0,1,0,1,0,0,0],
            [1,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,1,1,1,0,0]
        ],
        39
    ],
]

run_functional_tests(Solution().closedIsland, tests)
