"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3644/
https://leetcode.com/problems/arithmetic-slices/

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.


Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
"""
from typing import List


# Runtime: 1320 ms, faster than 5.03% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 209.8 MB, less than 5.03% of Python3 online submissions for Arithmetic Slices.
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#
#         dp = [[False] * (n+1) for _ in range(n)]
#
#         result = 0
#
#         for i in range(n + 1 - 3):
#             if A[i+2] - A[i+1] == A[i+1] - A[i]:
#                 dp[i][3] = True
#                 result += 1
#
#         for l in range(4, n+1):
#             for i in range(n+1-l):
#                 if dp[i][l-1] and A[i+l-1] - A[i+l-2] == A[i+l-2] - A[i+l-3]:
#                     dp[i][l] = True
#                     result += 1
#
#         return result

# Runtime: 40 ms, faster than 48.59% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.4 MB, less than 76.96% of Python3 online submissions for Arithmetic Slices.
from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 59 ms, faster than 41.02% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.1 MB, less than 75.02% of Python3 online submissions for Arithmetic Slices.
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)

        dp = [0] * n
        result = 0

        for i in range(2, n):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                result += dp[i]

        return result


tests = [
    ([1, 2, 3, 4], 3)
]


run_functional_tests(Solution().numberOfArithmeticSlices, tests)