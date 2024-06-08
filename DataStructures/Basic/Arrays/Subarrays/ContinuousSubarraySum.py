"""
https://leetcode.com/problems/continuous-subarray-sum/description/

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.



Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2708 ms
# Beats
# 15.1%
# Memory
# 31.1 MB
# Beats
# 93.49%
# class Solution:
#
#     def checkSubarraySumZero(self, nums: List[int]) -> bool:
#         i, n = 0, len(nums)
#
#         def find(i) -> int:
#             nonlocal n, nums
#             for j in range(n):
#                 if not nums[j]:
#                     return j
#             return n
#
#         while i < n:
#             i = find(i)
#             if i == n:
#                 return False
#             i += 1
#             if i == n:
#                 return False
#             if not nums[i]:
#                 return True
#             i += 1
#         return False
#
#     def checkSubarraySumImpl(self, nums: List[int], k: int) -> bool:
#         n = len(nums)
#         ps = [0] * n
#         rems = defaultdict(int)
#         ps[0] = nums[0] % k
#         for i in range(1, n):
#             ps[i] = (ps[i-1] + nums[i]) % k
#             rems[ps[i]] = rems[ps[i]] + 1
#         for i in range(n):
#             if i < n-1:
#                 rems[ps[i+1]] = rems[ps[i+1]] - 1
#             if i > 0 and not ps[i]:
#                 return True
#             if rems[ps[i]] > 0:
#                 return True
#         return False
#
#     def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         if len(nums) < 2:
#             return False
#         if not k:
#             return self.checkSubarraySumZero(nums)
#         if k < 0:
#             k = -k
#         return self.checkSubarraySumImpl(nums, k)


# Runtime
# 847
# ms
# Beats
# 25.60%
# of users with Python3
# Memory
# 36.06
# MB
# Beats
# 91.22%
# of users with Python3
# https://leetcode.com/problems/continuous-subarray-sum/editorial/?envType=daily-question&envId=2024-06-08
class Solution:

    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        mod_seen = { 0: -1 }

        for i in range(len(nums)):
            prefix_mod = (prefix_mod + nums[i]) % k
            if prefix_mod in mod_seen:
                if i - mod_seen[prefix_mod] > 1:
                    return True
            else:
                mod_seen[prefix_mod] = i
        return False


tests = [
    [[23,2,4,6,7], 6, True],
    [[23,2,6,4,7], 6, True],
    [[23,2,6,4,7], 13, False]
]

run_functional_tests(Solution().checkSubarraySum, tests)
