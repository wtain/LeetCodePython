"""
https://leetcode.com/problems/longest-subsequence-with-limited-sum/

You are given an integer array nums of length n, and an integer array queries of length m.

Return an array answer of length m where answer[i] is the maximum size of a subsequence that you can take from nums such that the sum of its elements is less than or equal to queries[i].

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [4,5,2,1], queries = [3,10,21]
Output: [2,3,4]
Explanation: We answer the queries as follows:
- The subsequence [2,1] has a sum less than or equal to 3. It can be proven that 2 is the maximum size of such a subsequence, so answer[0] = 2.
- The subsequence [4,5,1] has a sum less than or equal to 10. It can be proven that 3 is the maximum size of such a subsequence, so answer[1] = 3.
- The subsequence [4,5,2,1] has a sum less than or equal to 21. It can be proven that 4 is the maximum size of such a subsequence, so answer[2] = 4.
Example 2:

Input: nums = [2,3,4,5], queries = [1]
Output: [0]
Explanation: The empty subsequence is the only subsequence that has a sum less than or equal to 1, so answer[0] = 0.


Constraints:

n == nums.length
m == queries.length
1 <= n, m <= 1000
1 <= nums[i], queries[i] <= 106
"""
import bisect
from typing import List

import numpy as numpy

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2313 ms
# Beats
# 12.69%
# Memory
# 14.2 MB
# Beats
# 41.40%
# # https://leetcode.com/problems/longest-subsequence-with-limited-sum/solutions/2644327/longest-subsequence-with-limited-sum/
# class Solution:
#     def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
#         n = len(nums)
#         nums.sort()
#         result = []
#         for q in queries:
#             i, s = 0, 0
#             while i < n and s + nums[i] <= q:
#                 s += nums[i]
#                 i += 1
#             result.append(i)
#         return result


# https://leetcode.com/problems/longest-subsequence-with-limited-sum/solutions/2644327/longest-subsequence-with-limited-sum/
# Runtime
# 530 ms
# Beats
# 39.92%
# Memory
# 32.4 MB
# Beats
# 8.74%
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presums = numpy.cumsum(nums)
        result = []
        for q in queries:
            index = bisect.bisect_right(presums, q)
            result.append(index)
        return result


tests = [
    [[4,5,2,1], [3,10,21], [2,3,4]],
    [[2,3,4,5], [1], [0]]
]


run_functional_tests(Solution().answerQueries, tests)
