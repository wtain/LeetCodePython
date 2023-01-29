"""
https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.



Example 1:


Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.
Example 2:


Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.
Example 3:


Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation has score 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.


Constraints:

n == values.length
3 <= n <= 50
1 <= values[i] <= 100
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests



# Runtime
# 170 ms
# Beats
# 48.54%
# Memory
# 14.5 MB
# Beats
# 57.77%
# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/solutions/3035158/matrix-chain-multiplication-dp-memoization/
# class Solution:
#     def minScoreTriangulation(self, values: List[int]) -> int:
#         n = len(values)
#         dp = [[-1] * n for _ in range(n)]
#
#         def impl(i: int, j: int) -> int:
#             nonlocal dp, values, n
#             if i == j:
#                 return 0
#             mini = 10 ** 9
#             if dp[i][j] != -1:
#                 return dp[i][j]
#             for k in range(i, j):
#                 steps = values[i-1] * values[k] * values[j] + impl(i, k) + impl(k+1, j)
#                 mini = min(mini, steps)
#             dp[i][j] = mini
#             return mini
#
#         return impl(1, n-1)


# Runtime
# 143 ms
# Beats
# 61.65%
# Memory
# 14.9 MB
# Beats
# 30.58%
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)

        @cache
        def impl(i: int, j: int) -> int:
            nonlocal values, n
            if i == j:
                return 0
            mini = 10 ** 9
            for k in range(i, j):
                steps = values[i-1] * values[k] * values[j] + impl(i, k) + impl(k+1, j)
                mini = min(mini, steps)
            return mini

        return impl(1, n-1)


tests = [
    [[1,2,3], 6],
    [[3,7,4,5], 144],
    [[1,3,1,4,1,5], 13],
]

run_functional_tests(Solution().minScoreTriangulation, tests)
