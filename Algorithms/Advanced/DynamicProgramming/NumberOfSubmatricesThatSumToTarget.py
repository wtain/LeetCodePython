"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3711/
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.



Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0


Constraints:

1 <= matrix.length <= 100
1 <= matrix[0].length <= 100
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
"""
from typing import List

from Common.MatrixUtils import matrix_size
from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#
#         def calc_pref_sum() -> List[List[int]]:
#             nonlocal n, m, matrix
#             result = matrix
#             for i in range(n):
#                 for j in range(m):
#                     s00 = result[i-1][j-1] if i > 0 and j > 0 else 0
#                     s01 = result[i-1][j] if i > 0 else 0
#                     s10 = result[i][j-1] if j > 0 else 0
#                     result[i][j] += s01 + s10 - s00
#             return result
#
#         ps = calc_pref_sum()
#
#         cnt = 0
#         for i1 in range(n):
#             for i2 in range(i1, n):
#
#
#
#
#         return cnt


# Runtime: 972 ms, faster than 44.18% of Python3 online submissions for Number of Submatrices That Sum to Target.
# Memory Usage: 15.2 MB, less than 61.49% of Python3 online submissions for Number of Submatrices That Sum to Target.
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n = len(matrix)
        m = len(matrix[0])
        counts = {}
        dp = [0] * m

        def numSubmatrixSumTargetInRows(i1 : int, i2 : int) -> int:
            nonlocal matrix, target, counts, target, dp, n, m
            res, s = 0, 0
            for j in range(m):
                s += matrix[i2][j]
                dp[j] = s + (dp[j] if i1 != i2 else 0)
                res += counts.get(dp[j] - target, 0)
                counts[dp[j]] = counts.get(dp[j], 0) + 1
            return res

        cnt = 0
        for i in range(n):
            for j in range(i, n):
                counts[0] = 1
                cnt += numSubmatrixSumTargetInRows(i, j)
                counts = {}
        return cnt


tests = [
    [
        [[0,1,0],
         [1,1,1],
         [0,1,0]],
        0, 4
    ],
    [
        [[1,-1],[-1,1]],
        0, 5
    ],
    [
        [[904]],
        0, 0
    ]
]

run_functional_tests(Solution().numSubmatrixSumTarget, tests, input_metric=lambda test: matrix_size(test[0]))