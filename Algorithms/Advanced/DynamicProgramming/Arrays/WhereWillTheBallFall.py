"""
https://leetcode.com/problems/where-will-the-ball-fall/description/

You have a 2-D grid of size m x n representing a box, and you have n balls. The box is open on the top and bottom sides.

Each cell in the box has a diagonal board spanning two corners of the cell that can redirect a ball to the right or to the left.

A board that redirects the ball to the right spans the top-left corner to the bottom-right corner and is represented in the grid as 1.
A board that redirects the ball to the left spans the top-right corner to the bottom-left corner and is represented in the grid as -1.
We drop one ball at the top of each column of the box. Each ball can get stuck in the box or fall out of the bottom. A ball gets stuck if it hits a "V" shaped pattern between two boards or if a board redirects the ball into either wall of the box.

Return an array answer of size n where answer[i] is the column that the ball falls out of at the bottom after dropping the ball from the ith column at the top, or -1 if the ball gets stuck in the box.



Example 1:



Input: grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
Output: [1,-1,-1,-1,-1]
Explanation: This example is shown in the photo.
Ball b0 is dropped at column 0 and falls out of the box at column 1.
Ball b1 is dropped at column 1 and will get stuck in the box between column 2 and 3 and row 1.
Ball b2 is dropped at column 2 and will get stuck on the box between column 2 and 3 and row 0.
Ball b3 is dropped at column 3 and will get stuck on the box between column 2 and 3 and row 0.
Ball b4 is dropped at column 4 and will get stuck on the box between column 2 and 3 and row 1.
Example 2:

Input: grid = [[-1]]
Output: [-1]
Explanation: The ball gets stuck against the left wall.
Example 3:

Input: grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
Output: [0,1,2,3,4,-1]


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is 1 or -1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# WRONG
# https://leetcode.com/problems/where-will-the-ball-fall/solutions/2634524/where-will-the-ball-fall/
# class Solution:
#     def findBall(self, grid: List[List[int]]) -> List[int]:
#         n = len(grid[0])
#         m = len(grid)
#         result = [0] * n
#         dp = [[0] * n for _ in range(m+1)]
#         for row in range(m, -1, -1):
#             for col in range(n):
#                 if row == m:
#                     grid[row][col] = col
#                     continue
#                 next_col = col + grid[row][col]
#                 if next_col < 0 or next_col > n-1 or grid[row][col] != grid[row][next_col]:
#                     dp[row][col] = -1
#                 else:
#                     dp[row][col] = dp[row+1][next_col]
#                 if row == 0:
#                     result[col] = dp[row][col]
#         return result


# Runtime
# 703 ms
# Beats
# 5.1%
# Memory
# 14.2 MB
# Beats
# 84.52%
# https://leetcode.com/problems/where-will-the-ball-fall/solutions/2634524/where-will-the-ball-fall/
class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def move(a, b):
            if a == -1 or b == 0:
                return -1
            return a + b

        balls = range(len(grid[0]))
        for row in grid:
            z = list(zip([1] + row, row + [-1]))
            moves = [sum(z[i + 1] if r > 0 else z[i]) // 2 for i, r in enumerate(row)]
            balls = [move(a, moves[a]) for a in balls]
        return balls


tests = [
    [[[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]], [1,-1,-1,-1,-1]],
    [[[-1]], [-1]],
    [[[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]], [0,1,2,3,4,-1]]
]

run_functional_tests(Solution().findBall, tests)
