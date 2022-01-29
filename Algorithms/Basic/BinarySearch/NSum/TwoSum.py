"""
https://leetcode.com/problems/two-sum/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3836/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

# Runtime: 36 ms, faster than 85.07% of Python online submissions for Two Sum.
# Memory Usage: 15 MB, less than 5.04% of Python online submissions for Two Sum.
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # Tuples (value, index)
#         nums_sorted = sorted([(x, i) for (i, x) in enumerate(nums)], key=lambda x: x[0])
#         for (i, t) in enumerate(nums_sorted):
#             t2 = target - t[0]
#
#             i2 = bisect_left(nums_sorted, (t2, -1), i + 1)
#
#             if i2 < len(nums_sorted) and nums_sorted[i2][0] == t2:
#                 return t[1], nums_sorted[i2][1]
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 72 ms, faster than 50.87% of Python3 online submissions for Two Sum.
# Memory Usage: 15.8 MB, less than 9.37% of Python3 online submissions for Two Sum.
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_sorted = sorted([(x, i) for (i, x) in enumerate(nums)], key=lambda x: x[0])
#         for (i, t) in enumerate(nums_sorted):
#             t2 = target - t[0]
#
#             i2 = bisect_left(nums_sorted, (t2, -1), i + 1)
#
#             if i2 < len(nums_sorted) and nums_sorted[i2][0] == t2:
#                 return [t[1], nums_sorted[i2][1]]


# Runtime: 64 ms, faster than 57.69% of Python3 online submissions for Two Sum.
# Memory Usage: 15.6 MB, less than 9.37% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted([(x, i) for (i, x) in enumerate(nums)], key=lambda x: x[0])
        l, r = 0, len(nums)-1
        while l < r:
            s = nums_sorted[l][0] + nums_sorted[r][0]
            if s == target:
                return [nums_sorted[l][1], nums_sorted[r][1]]
            elif s < target:
                l += 1
            else:
                r -= 1


# s = Solution()
#
# r = s.twoSum([0,4,3,0], 0) # 0 3
# print(r)
#
# r = s.twoSum([2, 7, 11, 15], 9) # 0 1
# print(r)
#
# r = s.twoSum([3,2,4], 6) # 1 2
# print(r)
#
# r = s.twoSum([3,3], 6) # 0 1
# print(r)
#
# r = s.twoSum([3,2,3], 6) # 0 2
# print(r)

tests = [
    [[0,4,3,0], 0, [0, 3]],
    [[2, 7, 11, 15], 9, [0, 1]],
    [[3,2,4], 6, [1, 2]],
    [[3,3], 6, [0, 1]],
    [[3,2,3], 6, [0, 2]]
]

run_functional_tests(Solution().twoSum, tests)