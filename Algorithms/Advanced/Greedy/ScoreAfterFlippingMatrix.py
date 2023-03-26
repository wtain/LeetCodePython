"""
https://leetcode.com/problems/score-after-flipping-matrix/

You are given an m x n binary matrix grid.

A move consists of choosing any row or column and toggling each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Every row of the matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score after making any number of moves (including zero moves).



Example 1:


Input: grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation: 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
Example 2:

Input: grid = [[0]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
grid[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 49 ms
# Beats
# 10.75%
# Memory
# 13.9 MB
# Beats
# 67.74%
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        def flip_row(i):
            nonlocal m
            for j in range(m):
                grid[i][j] = 1 - grid[i][j]

        def flip_column(j):
            nonlocal n
            for i in range(n):
                grid[i][j] = 1 - grid[i][j]

        def row_value(i):
            nonlocal m
            value = 0
            for j in range(m):
                value = 2 * value + grid[i][j]
            return value

        for i in range(n):
            if grid[i][0] == 0:
                flip_row(i)

        for j in range(m):
            cnt = sum(grid[i][j] for i in range(n))
            if cnt < n - cnt:
                flip_column(j)

        return sum(row_value(i) for i in range(n))


tests = [
    [[[0,0,1,1],[1,0,1,0],[1,1,0,0]], 39],
    [[[0]], 1],
]

run_functional_tests(Solution().matrixScore, tests)
