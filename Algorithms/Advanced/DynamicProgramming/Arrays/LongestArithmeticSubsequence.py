"""
https://leetcode.com/problems/longest-arithmetic-subsequence/

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).


Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].


Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def longestArithSeqLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n <= 2:
#             return n
#
#         def longestArithmeticSubsequenceOfDiff(diff: int) -> int:
#             nonlocal nums, n
#             L = [1] * n
#             maxlen = 1
#             indices = {nums[0]: 0}
#             for i in range(1, n):
#                 val = nums[i] - diff
#                 if val in indices:
#                     L[i] = L[indices[val]] + 1
#                     maxlen = max(maxlen, L[i])
#                 if nums[i] not in indices:
#                     indices[nums[i]] = i
#             return maxlen
#
#         longest_sequence_length = 2
#         return longestArithmeticSubsequenceOfDiff(3)
#         # low, high = 1, max(nums) - min(nums)
#         # while low <= high:
#         #     med = (low + high) // 2
#         #     length = longestArithmeticSubsequenceOfDiff(med)
#         return longest_sequence_length


# Runtime
# 3749 ms
# Beats
# 54.65%
# Memory
# 66.4 MB
# Beats
# 18.91%
# https://leetcode.com/problems/longest-arithmetic-subsequence/solutions/274611/java-c-python-dp/
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp, n = {}, len(nums)
        for i in range(n):
            for j in range(i+1, n):
                dp[j, nums[j] - nums[i]] = dp.get((i, nums[j] - nums[i]), 1) + 1
        return max(dp.values())


tests = [
    [[3,6,9,12], 4],
    [[9,4,7,2,10], 3],
    [[20,1,15,3,10,5,8], 4],
]

run_functional_tests(Solution().longestArithSeqLength, tests)
