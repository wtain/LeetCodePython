"""
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/description/?envType=daily-question&envId=2024-03-29

You are given an integer array nums and a positive integer k.

Return the number of subarrays where the maximum element of nums appears at least k times in that subarray.

A subarray is a contiguous sequence of elements within an array.



Example 1:

Input: nums = [1,3,2,3,3], k = 2
Output: 6
Explanation: The subarrays that contain the element 3 at least 2 times are: [1,3,2,3], [1,3,2,3,3], [3,2,3], [3,2,3,3], [2,3,3] and [3,3].
Example 2:

Input: nums = [1,4,2,1], k = 3
Output: 0
Explanation: No subarray contains the element 4 at least 3 times.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= k <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# NOT SOLVED
# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         mx = max(nums)
#         n = len(nums)
#         cnts = [0] * n
#         c = 0
#         for i in range(n):
#             if nums[i] == mx:
#                 c += 1
#             cnts[i] = c
#         result = 0
#         i1 = 0
#         for i2 in range(n):
#             c = nums[i2]
#             while c >= k:
#                 c -= nums[i1]
#                 i1 += 1
#                 result += 1
#         return result


# Runtime
# 869
# ms
# Beats
# 66.03%
# of users with Python3
# Memory
# 30.77
# MB
# Beats
# 97.33%
# of users with Python3
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/editorial/?envType=daily-question&envId=2024-03-29
# class Solution:
#     def countSubarrays(self, nums: List[int], k: int) -> int:
#         mx = max(nums)
#         result = start = max_cnt = 0
#
#         for end in range(len(nums)):
#             if nums[end] == mx:
#                 max_cnt += 1
#             while max_cnt == k:
#                 if nums[start] == mx:
#                     max_cnt -= 1
#                 start += 1
#             result += start
#         return result


# Runtime
# 874
# ms
# Beats
# 61.07%
# of users with Python3
# Memory
# 30.86
# MB
# Beats
# 80.15%
# of users with Python3
# https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/editorial/?envType=daily-question&envId=2024-03-29
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        idx = []
        result = 0

        for index, elem in enumerate(nums):
            if elem == mx:
                idx.append(index)
            freq = len(idx)
            if freq >= k:
                result += idx[-k] + 1
        return result


tests = [
    [[1,3,2,3,3], 2, 6],
    [[1,4,2,1], 3, 0],
]

run_functional_tests(Solution().countSubarrays, tests)
