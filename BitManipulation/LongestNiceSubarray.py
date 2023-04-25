"""
https://leetcode.com/problems/longest-nice-subarray/

You are given an array nums consisting of positive integers.

We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

Return the length of the longest nice subarray.

A subarray is a contiguous part of an array.

Note that subarrays of length 1 are always considered nice.



Example 1:

Input: nums = [1,3,8,48,10]
Output: 3
Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
- 3 AND 8 = 0.
- 3 AND 48 = 0.
- 8 AND 48 = 0.
It can be proven that no longer nice subarray can be obtained, so we return 3.
Example 2:

Input: nums = [3,1,5,11,13]
Output: 1
Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 673 ms
# Beats
# 85.60%
# Memory
# 29.4 MB
# Beats
# 12.84%
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 1
        i1 = 0
        n = len(nums)
        current = 0
        for i in range(n):
            while i1 < i and current & nums[i]:
                current ^= nums[i1]
                i1 += 1
            current |= nums[i]
            longest = max(longest, i-i1+1)

        return longest


tests = [
    [[1,3,8,48,10], 3],
    [[3,1,5,11,13], 1],
]

run_functional_tests(Solution().longestNiceSubarray, tests)
