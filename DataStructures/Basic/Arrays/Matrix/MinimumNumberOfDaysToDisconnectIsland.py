"""
https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/description/?envType=daily-question&envId=2024-08-11

You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.



Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 975
# ms
# Beats
# 40.19%
# Analyze Complexity
# Memory
# 16.74
# MB
# Beats
# 59.81%
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/editorial/?envType=daily-question&envId=2024-08-11
# class Solution:
#     def minDays(self, grid: List[List[int]]) -> int:
#         rows, cols = len(grid), len(grid[0])
#
#         def _count_islands():
#             visited = set()
#             count = 0
#             for i in range(rows):
#                 for j in range(cols):
#                     if grid[i][j] == 1 and (i, j) not in visited:
#                         _explore_island(i, j, visited)
#                         count += 1
#             return count
#
#         def _explore_island(i, j, visited):
#             if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0 or (i, j) in visited:
#                 return
#             visited.add((i, j))
#             for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                 _explore_island(i + di, j + dj, visited)
#
#         if _count_islands() != 1:
#             return 0
#
#         for i in range(rows):
#             for j in range(cols):
#                 if grid[i][j] == 1:
#                     grid[i][j] = 0
#                     if _count_islands() != 1:
#                         return 1
#                     grid[i][j] = 1
#
#         return 2


# Runtime
# 68
# ms
# Beats
# 79.44%
# Analyze Complexity
# Memory
# 17.02
# MB
# Beats
# 36.45%
# https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/editorial/?envType=daily-question&envId=2024-08-11
class Solution:
    DIRECTIONS = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        ap_info = {"has_articulation_point": False, "time": 0}
        land_cells = 0
        island_count = 0

        discovery_time = [
            [-1] * cols for _ in range(rows)
        ]
        lowest_reachable = [
            [-1] * cols for _ in range(rows)
        ]
        parent_cell = [
            [-1] * cols for _ in range(rows)
        ]

        def _find_articulation_point(row, col):
            discovery_time[row][col] = ap_info["time"]
            ap_info["time"] += 1
            lowest_reachable[row][col] = discovery_time[row][col]
            children = 0
            for direction in self.DIRECTIONS:
                new_row = row + direction[0]
                new_col = col + direction[1]
                if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 1:
                    if discovery_time[new_row][new_col] == -1:
                        children += 1
                        parent_cell[new_row][new_col] = (row * cols + col)
                        _find_articulation_point(new_row, new_col)

                        lowest_reachable[row][col] = min(lowest_reachable[row][col], lowest_reachable[new_row][new_col])

                        if (lowest_reachable[new_row][new_col] >= discovery_time[row][col] and parent_cell[row][col] != -1):
                            ap_info["has_articulation_point"] = True
                    elif new_row * cols + new_col != parent_cell[row][col]:
                        lowest_reachable[row][col] = min(lowest_reachable[row][col], discovery_time[new_row][new_col])

            if parent_cell[row][col] == -1 and children > 1:
                ap_info["has_articulation_point"] = True

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land_cells += 1
                    if discovery_time[i][j] == -1:
                        _find_articulation_point(i, j)
                        island_count += 1
        if island_count == 0 or island_count >= 2:
            return 0

        if land_cells == 1:
            return 1

        if ap_info["has_articulation_point"]:
            return 1
        return 2


tests = [
    [[[1,1,0,0,1,1,0,1,0,1,1,1,1],[1,1,0,1,0,1,1,0,1,1,1,0,0],[0,0,1,1,1,0,0,1,1,1,1,0,0],[1,1,1,0,1,0,1,1,1,1,1,1,1],[1,1,1,0,1,1,0,1,1,1,1,0,1],[0,0,1,1,1,1,1,1,1,1,0,1,1],[1,1,1,0,0,1,1,1,0,1,1,1,1],[0,1,1,1,1,1,1,1,1,0,1,0,0],[1,1,1,1,1,1,1,1,0,0,1,0,1],[1,0,1,1,1,1,0,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,0,1],[1,1,0,1,1,0,1,0,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,1,1,0,1],[1,1,0,1,1,1,1,0,1,1,0,1,1],[1,0,1,1,1,1,1,1,1,1,1,0,1]], 0],
    [[[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2],
    [[[1,1]], 2],
]

run_functional_tests(Solution().minDays, tests)
