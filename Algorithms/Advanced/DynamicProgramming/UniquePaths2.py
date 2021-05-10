"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/
https://leetcode.com/problems/unique-paths-ii/

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and space is marked as 1 and 0 respectively in the grid.



Example 1:


Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
Example 2:


Input: obstacleGrid = [[0,1],[0,0]]
Output: 1


Constraints:

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""
from typing import List

from Common.MatrixUtils import matrix_size
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 44 ms, faster than 49.87% of Python3 online submissions for Unique Paths II.
# Memory Usage: 14.5 MB, less than 33.52% of Python3 online submissions for Unique Paths II.
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        if not obstacleGrid[0][0]:
            dp[0][0] = 1
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    continue
                if i == 0 and j == 0:
                    continue
                n1, n2 = 0, 0
                if i > 0:
                    n1 = dp[i-1][j]
                if j > 0:
                    n2 = dp[i][j-1]
                dp[i][j] = n1 + n2
        return dp[m-1][n-1]


tests = [
    ([[0,0,0],[0,1,0],[0,0,0]], 2),
    ([[0,1],[0,0]], 1)
]


run_functional_tests(Solution().uniquePathsWithObstacles, tests, input_metric=lambda test: matrix_size(test[0]))