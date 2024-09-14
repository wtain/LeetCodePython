"""
https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/description/?envType=daily-question&envId=2024-09-14

You are given an integer array nums of size n.

Consider a non-empty subarray from nums that has the maximum possible bitwise AND.

In other words, let k be the maximum value of the bitwise AND of any subarray of nums. Then, only subarrays with a bitwise AND equal to k should be considered.
Return the length of the longest such subarray.

The bitwise AND of an array is the bitwise AND of all the numbers in it.

A subarray is a contiguous sequence of elements within an array.



Example 1:

Input: nums = [1,2,3,3,2,2]
Output: 2
Explanation:
The maximum possible bitwise AND of a subarray is 3.
The longest subarray with that value is [3,3], so we return 2.
Example 2:

Input: nums = [1,2,3,4]
Output: 1
Explanation:
The maximum possible bitwise AND of a subarray is 4.
The longest subarray with that value is [4], so we return 1.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def longestSubarray(self, nums: List[int]) -> int:
#         n = len(nums)
#         l, r = 0, 0
#         v = nums[0]
#         while r < n:
#
#             nv = v & nums[l]
#         return 0


# Runtime
# 674
# ms
# Beats
# 24.73%
# Analyze Complexity
# Memory
# 31.19
# MB
# Beats
# 62.91%
# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/editorial/?envType=daily-question&envId=2024-09-14
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = result = current_streak = 0
        for v in nums:
            if max_val < v:
                max_val = v
                result = current_streak = 0

            if max_val == v:
                current_streak += 1
            else:
                current_streak = 0

            result = max(result, current_streak)
        return result


tests = [
    [[1,2,3,3,2,2], 2],
    [[1,2,3,4], 1],
]

run_functional_tests(Solution().longestSubarray, tests)
