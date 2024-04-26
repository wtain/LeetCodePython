"""
https://leetcode.com/problems/minimum-falling-path-sum-ii/description/?envType=daily-question&envId=2024-04-26

Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that no two elements chosen in adjacent rows are in the same column.



Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: 13
Explanation:
The possible falling paths are:
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
The falling path with the smallest sum is [1,5,7], so the answer is 13.
Example 2:

Input: grid = [[7]]
Output: 7


Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
-99 <= grid[i][j] <= 99
"""
from cmath import inf
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 5899
# ms
# Beats
# 15.48%
# of users with Python3
# Memory
# 40.14
# MB
# Beats
# 5.31%
# of users with Python3
# https://leetcode.com/problems/minimum-falling-path-sum-ii/editorial/?envType=daily-question&envId=2024-04-26
# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#
#         @cache
#         def impl(row, col):
#             if row == n-1:
#                 return grid[row][col]
#             next_min = inf
#             for next_row_col in range(n):
#                 if next_row_col != col:
#                     next_min = min(next_min, impl(row+1, next_row_col))
#             return grid[row][col] + next_min
#
#         result = inf
#         for col in range(n):
#             result = min(result, impl(0, col))
#         return result


# Runtime
# 3756
# ms
# Beats
# 28.32%
# of users with Python3
# Memory
# 20.04
# MB
# Beats
# 65.04%
# of users with Python3
# https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#
#         memo = [[inf] * n for _ in range(n)]
#
#         for col in range(n):
#             memo[n-1][col] = grid[n-1][col]
#
#         for row in range(n-2, -1, -1):
#             for col in range(n):
#                 next_min = inf
#                 for next_row_col in range(n):
#                     if next_row_col != col:
#                         next_min = min(next_min, memo[row + 1][next_row_col])
#                 memo[row][col] = next_min + grid[row][col]
#
#         result = inf
#         for col in range(n):
#             result = min(result, memo[0][col])
#         return result


# Runtime
# 223
# ms
# Beats
# 80.53%
# of users with Python3
# Memory
# 20.11
# MB
# Beats
# 34.96%
# of users with Python3
# https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
# class Solution:
#     def minFallingPathSum(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#
#         memo = [[inf] * n for _ in range(n)]
#
#         next_min1_c = None
#         next_min2_c = None
#
#         for col in range(n):
#             memo[n-1][col] = grid[n-1][col]
#             if next_min1_c is None or memo[n-1][col] <= memo[n-1][next_min1_c]:
#                 next_min2_c = next_min1_c
#                 next_min1_c = col
#             elif next_min2_c is None or memo[n-1][col] <= memo[n-1][next_min2_c]:
#                 next_min2_c = col
#
#         for row in range(n-2, -1, -1):
#             min1_c = None
#             min2_c = None
#
#             for col in range(n):
#                 if col != next_min1_c:
#                     memo[row][col] = grid[row][col] + memo[row+1][next_min1_c]
#                 else:
#                     memo[row][col] = grid[row][col] + memo[row + 1][next_min2_c]
#                 if min1_c is None or memo[row][col] <= memo[row][min1_c]:
#                     min2_c = min1_c
#                     min1_c = col
#                 elif min2_c is None or memo[row][col] <= memo[row][min2_c]:
#                     min2_c = col
#             next_min1_c = min1_c
#             next_min2_c = min2_c
#
#         return memo[0][next_min1_c]


# Runtime
# 207
# ms
# Beats
# 99.12%
# of users with Python3
# Memory
# 19.91
# MB
# Beats
# 80.97%
# of users with Python3
# https://leetcode.com/problems/minimum-falling-path-sum-ii/?envType=daily-question&envId=2024-04-26
class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        next_min1_c = None
        next_min2_c = None

        next_min1 = None
        next_min2 = None

        for col in range(n):
            if next_min1 is None or grid[n-1][col] <= next_min1:
                next_min2 = next_min1
                next_min2_c = next_min1_c
                next_min1 = grid[n-1][col]
                next_min1_c = col
            elif next_min2 is None or grid[n-1][col] <= next_min2:
                next_min2_c = col
                next_min2 = grid[n-1][col]

        for row in range(n-2, -1, -1):
            min1_c = None
            min2_c = None

            min1 = None
            min2 = None

            for col in range(n):
                if col != next_min1_c:
                    value = grid[row][col] + next_min1
                else:
                    value = grid[row][col] + next_min2
                if min1 is None or value <= min1:
                    min2 = min1
                    min2_c = min1_c
                    min1 = value
                    min1_c = col
                elif min2 is None or value <= min2:
                    min2_c = col
                    min2 = value
            next_min1 = min1
            next_min2 = min2
            next_min1_c = min1_c
            next_min2_c = min2_c

        return next_min1


tests = [
    [[[1,2,3],[4,5,6],[7,8,9]], 13],
    [[[7]], 7],
]

run_functional_tests(Solution().minFallingPathSum, tests)
