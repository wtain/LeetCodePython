"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3801/
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Given an m x n matrix matrix and an integer k, return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.



Example 1:


Input: matrix = [[1,0,1],[0,-2,3]], k = 2
Output: 2
Explanation: Because the sum of the blue rectangle [[0, 1], [-2, 3]] is 2, and 2 is the max number no larger than k (k = 2).
Example 2:

Input: matrix = [[2,2,-1]], k = 3
Output: 3


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-100 <= matrix[i][j] <= 100
-105 <= k <= 105


Follow up: What if the number of rows is much larger than the number of columns?
"""
import math
from typing import List

from sortedcontainers import SortedSet

from Common.ObjectTestingUtils import run_functional_tests
from Common.RandomUtils import random_matrix


# SLOW
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         m = len(matrix[0])
#         ma = matrix.copy()
#         for i in range(1, n):
#             ma[i][0] += ma[i-1][0]
#         for j in range(1, m):
#             ma[0][j] += ma[0][j-1]
#         for i in range(1, n):
#             for j in range(1, m):
#                 ma[i][j] += ma[i-1][j] + ma[i][j-1] - ma[i-1][j-1]
#         max_sum = 0
#         for i1 in range(n):
#             for j1 in range(m):
#                 for i2 in range(i1, n):
#                     for j2 in range(j1, m):
#                         s = ma[i2][j2]
#                         if i1 > 0:
#                             s -= ma[i1-1][j2]
#                         if j1 > 0:
#                             s -= ma[i2][j1-1]
#                         if i1 > 0 and j1 > 0:
#                             s += ma[i1-1][j1-1]
#                         if s > k:
#                             continue
#                         max_sum = max(max_sum, s)
#         return max_sum


# SAME, SLOW
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         n, m, min_v = len(matrix), len(matrix[0]), min(min(matrix))
#
#         for i in range(n):
#             for j in range(m):
#                 matrix[i][j] -= min_v
#
#         ma = matrix.copy()
#
#         for i in range(1, n):
#             ma[i][0] += ma[i-1][0]
#         for j in range(1, m):
#             ma[0][j] += ma[0][j-1]
#         for i in range(1, n):
#             for j in range(1, m):
#                 ma[i][j] += ma[i-1][j] + ma[i][j-1] - ma[i-1][j-1]
#         max_sum = 0
#         for i1 in range(n):
#             for j1 in range(m):
#                 for i2 in range(i1, n):
#                     for j2 in range(j1, m):
#                         s = ma[i2][j2]
#                         if i1 > 0:
#                             s -= ma[i1-1][j2]
#                         if j1 > 0:
#                             s -= ma[i2][j1-1]
#                         if i1 > 0 and j1 > 0:
#                             s += ma[i1-1][j1-1]
#                         s += min_v * (i2 - i1 + 1) * (j2 - j1 + 1)
#                         if s > k:
#                             continue
#                         max_sum = max(max_sum, s)
#         return max_sum


# WRONG
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         def transpose(matrix: List[List[int]]) -> List[List[int]]:
#             n, m = len(matrix), len(matrix[0])
#             mt = [[0] * n for _ in range(m)]
#             for i in range(n):
#                 for j in range(m):
#                     mt[j][i] = matrix[i][j]
#             return mt
#
#         n, m, min_v = len(matrix), len(matrix[0]), min(min(matrix))
#         if n > m:
#             return self.maxSumSubmatrix(transpose(matrix), k)
#
#         for i in range(n):
#             for j in range(m):
#                 matrix[i][j] -= min_v
#
#         ma = matrix.copy()
#
#         for i in range(1, n):
#             ma[i][0] += ma[i-1][0]
#         for j in range(1, m):
#             ma[0][j] += ma[0][j-1]
#         for i in range(1, n):
#             for j in range(1, m):
#                 ma[i][j] += ma[i-1][j] + ma[i][j-1] - ma[i-1][j-1]
#         max_sum = 0
#         for n1 in range(1, n+1):
#             for m1 in range(1, m+1):
#                 diff = min_v * n1 * m1
#                 target = k - diff
#                 for j in range(m-m1):
#                     i1, i2 = 0, n-n1
#                     jj = j + m1
#                     while i1 < i2:
#                         i = i1 + (i2-i1) // 2
#                         # i..i+n1, j..j+m1
#                         ii = i + n1
#                         s = ma[ii][jj]
#                         if i > 0:
#                             s -= ma[i-1][jj]
#                         if j > 0:
#                             s -= ma[ii][j-1]
#                         if i > 0 and j > 0:
#                             s += ma[i-1][j-1]
#                         s += diff
#                         if s <= k:
#                             max_sum = max(max_sum, s)
#                         if s == target:
#                             return s
#                         if s < target:
#                             i1 = i + 1
#                         else:
#                             i2 = i
#
#         return max_sum

# Runtime: 6052 ms, faster than 9.83% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 15.4 MB, less than 15.77% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         n, m = len(matrix), len(matrix[0])
#         result = -math.inf
#
#         def update_result(row_sum: List[int]):
#             nonlocal k, result
#             s = 0
#             sorted_sum = SortedSet()
#             sorted_sum.add(0)
#             for rs in row_sum:
#                 s += rs
#                 xi = sorted_sum.bisect_left(s - k)
#                 if xi < len(sorted_sum):
#                     x = sorted_sum[xi]
#                     result = max(result, s - x)
#                 sorted_sum.add(s)
#
#         for i in range(n):
#             row_sum = [0] * m
#             for row in range(i, n):
#                 for col in range(m):
#                     row_sum[col] += matrix[row][col]
#                 update_result(row_sum)
#                 if result == k:
#                     return result
#
#         return result


# Runtime: 4892 ms, faster than 13.40% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 15.8 MB, less than 5.95% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Runtime: 5740 ms, faster than 10.42% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 15.8 MB, less than 5.95% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
# class Solution:
#     def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
#         n, m = len(matrix), len(matrix[0])
#
#         def transpose(matrix: List[List[int]]) -> List[List[int]]:
#             nonlocal n, m
#             mt = [[0] * n for _ in range(m)]
#             for i in range(n):
#                 for j in range(m):
#                     mt[j][i] = matrix[i][j]
#             return mt
#
#         if n > m:
#             return self.maxSumSubmatrix(transpose(matrix), k)
#
#         result = -math.inf
#
#         def update_result(row_sum: List[int]):
#             nonlocal k, result
#             s = 0
#             sorted_sum = SortedSet()
#             sorted_sum.add(0)
#             for rs in row_sum:
#                 s += rs
#                 xi = sorted_sum.bisect_left(s - k)
#                 if xi < len(sorted_sum):
#                     x = sorted_sum[xi]
#                     result = max(result, s - x)
#                 sorted_sum.add(s)
#
#         for i in range(n):
#             row_sum = [0] * m
#             for row in range(i, n):
#                 for col in range(m):
#                     row_sum[col] += matrix[row][col]
#                 update_result(row_sum)
#                 if result == k:
#                     return result
#
#         return result

# Runtime: 2164 ms, faster than 48.81% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# Memory Usage: 15.8 MB, less than 5.95% of Python3 online submissions for Max Sum of Rectangle No Larger Than K.
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/solution/
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])

        def get_max_kadane(nums: List[int]) -> int:
            max_kadane, cs = -math.inf, 0
            for n in nums:
                cs = max(n, cs+n)
                max_kadane = max(max_kadane, cs)
            return max_kadane

        def transpose(matrix: List[List[int]]) -> List[List[int]]:
            nonlocal n, m
            mt = [[0] * n for _ in range(m)]
            for i in range(n):
                for j in range(m):
                    mt[j][i] = matrix[i][j]
            return mt

        if n > m:
            return self.maxSumSubmatrix(transpose(matrix), k)

        result = -math.inf

        def update_result(row_sum: List[int]):
            nonlocal k, result
            ks = get_max_kadane(row_sum)
            if ks <= k:
                result = max(result, ks)
                return
            s = 0
            sorted_sum = SortedSet()
            sorted_sum.add(0)
            for rs in row_sum:
                s += rs
                xi = sorted_sum.bisect_left(s - k)
                if xi < len(sorted_sum):
                    x = sorted_sum[xi]
                    result = max(result, s - x)
                sorted_sum.add(s)

        for i in range(n):
            row_sum = [0] * m
            for row in range(i, n):
                for col in range(m):
                    row_sum[col] += matrix[row][col]
                update_result(row_sum)
                if result == k:
                    return result

        return result



tests = [
    [
        [[2,2,-1]],
        0,
        -1
    ],
    [
        [
            [1,0,1],
            [0,-2,3]
        ],
        2,
        2
    ],
    [
        [
            [2,2,-1]
        ],
        3,
        3
    ],
    [
        random_matrix(10, 10, -10, 10),
        10,
        10
    ],
    [
        random_matrix(100, 100, -10, 10),
        50,
        50
    ]
]

run_functional_tests(Solution().maxSumSubmatrix, tests)