"""
https://leetcode.com/problems/shortest-bridge/

You are given an n x n binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.



Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1


Constraints:

n == grid.length == grid[i].length
2 <= n <= 100
grid[i][j] is either 0 or 1.
There are exactly two islands in grid.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 995 ms
# Beats
# 15.53%
# Memory
# 16.2 MB
# Beats
# 77.93%
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        mark = [[0] * m for _ in range(n)]
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def mark_island(i0, j0, island):
            nonlocal mark, n, m, grid, neighbors
            queue = [(i0, j0)]
            visited = {i0, j0}
            while queue:
                i, j = queue.pop()
                mark[i][j] = island
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] and (i1, j1) not in visited:
                        visited.add((i1, j1))
                        queue.append((i1, j1))

        def mark_distances(distances):
            nonlocal mark, n, m, grid, neighbors
            to_visit = set()
            visited = set()
            for i in range(n):
                for j in range(m):
                    if distances[i][j] == 0:
                        to_visit.add((i, j))
                        visited.add((i, j))

            d = 0
            while to_visit:
                next_level = set()
                for i, j in to_visit:
                    distances[i][j] = d
                    for di, dj in neighbors:
                        i1, j1 = i + di, j + dj
                        if 0 <= i1 < n and 0 <= j1 < m and grid[i1][j1] == 0 and (i1, j1) not in visited:
                            next_level.add((i1, j1))
                            visited.add((i1, j1))
                to_visit = next_level
                d += 1

        islands = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not mark[i][j]:
                    islands += 1
                    mark_island(i, j, islands)

        BigValue = float('inf')
        distances1 = [[0 if mark[i][j] == 1 else BigValue for j in range(m)] for i in range(n)]
        distances2 = [[0 if mark[i][j] == 2 else BigValue for j in range(m)] for i in range(n)]

        mark_distances(distances1)
        mark_distances(distances2)

        min_dist = BigValue
        for i in range(n):
            for j in range(m):
                dist = distances1[i][j] + distances2[i][j] - 1
                min_dist = min(min_dist, dist)

        return min_dist


tests = [
    [[[0,1],[1,0]], 1],
    [[[0,1,0],[0,0,0],[0,0,1]], 2],
    [[[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]], 1],
]

run_functional_tests(Solution().shortestBridge, tests)
