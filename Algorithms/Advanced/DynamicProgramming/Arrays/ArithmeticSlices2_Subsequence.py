"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3970/
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.



Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.


Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
"""
from collections import defaultdict
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 648 ms, faster than 77.99% of Python3 online submissions for Arithmetic Slices II - Subsequence.
# Memory Usage: 52.5 MB, less than 91.39% of Python3 online submissions for Arithmetic Slices II - Subsequence.
# https://leetcode.com/problems/arithmetic-slices-ii-subsequence/solution/
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#
#         dp, result = [defaultdict(int) for _ in range(n)], 0
#         for i in range(1, n):
#             for j in range(i):
#                 delta = A[i] - A[j]
#                 sm = 0
#                 if delta in dp[j]:
#                     sm = dp[j][delta]
#                 dp[i][delta] += sm+1
#                 result += sm
#
#         return result


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        n = len(A)
        dp, result = [defaultdict(int) for _ in range(n)], 0
        for i in range(1, n):
            for j in range(i):
                delta = A[i] - A[j]
                sm = dp[j][delta]
                dp[i][delta] += sm+1
                result += sm
        return result

# PRINTS PATHES
# class Solution:
#     def numberOfArithmeticSlices(self, A: List[int]) -> int:
#         n = len(A)
#
#         dp, result = [defaultdict(int) for _ in range(n)], 0
#         prev = [defaultdict(list) for _ in range(n)]
#         for i in range(1, n):
#             for j in range(i):
#                 delta = A[i] - A[j]
#                 sm = dp[j][delta]
#                 dp[i][delta] += sm+1
#                 prev[i][delta].append(j)
#                 result += sm
#
#         def print_pathes(v, i):
#             for j in prev[i][delta]:
#                 v.append(A[j])
#                 if len(v) >= 3:
#                     print(list(reversed(v)))
#                 print_pathes(v, j)
#                 v.pop()
#
#         for i in range(n):
#             for delta in prev[i]:
#                 v = [A[i]]
#                 print_pathes(v, i)
#
#         return result


"""
2 4 6
2 4 6 8
2 4 6 8 10
4 6 8
4 6 8 10
6 8 10
2 6 10
"""

tests = [
    [[2,4,6,8,10], 7],
    [[7,7,7,7,7], 16]
]

run_functional_tests(Solution().numberOfArithmeticSlices, tests)