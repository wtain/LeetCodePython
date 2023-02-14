"""
https://leetcode.com/problems/maximum-number-of-points-with-cost/

You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.


Example 1:


Input: points = [[1,2,3],[1,5,1],[3,1,1]]
Output: 9
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 2), (1, 1), and (2, 0).
You add 3 + 5 + 3 = 11 to your score.
However, you must subtract abs(2 - 1) + abs(1 - 0) = 2 from your score.
Your final score is 11 - 2 = 9.
Example 2:


Input: points = [[1,5],[2,3],[4,2]]
Output: 11
Explanation:
The blue cells denote the optimal cells to pick, which have coordinates (0, 1), (1, 1), and (2, 0).
You add 5 + 3 + 4 = 12 to your score.
However, you must subtract abs(1 - 1) + abs(1 - 0) = 1 from your score.
Your final score is 12 - 1 = 11.


Constraints:

m == points.length
n == points[r].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= points[r][c] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# NAIVE
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n, m = len(points), len(points[0])
#         dp = [points[0][j] for j in range(m)]
#         BigNegativeValue = float('-inf')
#         result = BigNegativeValue
#         for i in range(1, n):
#             dp2 = [BigNegativeValue] * m
#             for j in range(m):
#                 for j1 in range(m):
#                     dp2[j] = max(dp2[j], dp[j1] + points[i][j] - abs(j - j1))
#                     result = max(result, dp2[j])
#             dp = dp2
#         return result

# Runtime
# 2263 ms
# Beats
# 67.48%
# Memory
# 48.5 MB
# Beats
# 25.95%
# https://leetcode.com/problems/maximum-number-of-points-with-cost/solutions/2826885/maximum-number-of-points-with-cost/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n, m = len(points), len(points[0])
        dp = points[0]
        for i in range(1, n):
            dp2 = [0] * m
            temp = 0
            for j in range(m):
                temp = max(temp, dp[j] + j)
                dp2[j] = temp - j + points[i][j]
            temp = -m
            for j in range(m-1,-1,-1):
                temp = max(temp, dp[j] - j)
                dp2[j] = max(dp2[j], temp + j + points[i][j])
            dp = dp2
        return max(dp)


tests = [
    [[[0,3,0,4,2],[5,4,2,4,1],[5,0,0,5,1],[2,0,1,0,3]], 15],
    [[[1,2,3],[1,5,1],[3,1,1]], 9],
    [[[1,5],[2,3],[4,2]], 11],
]

run_functional_tests(Solution().maxPoints, tests)
