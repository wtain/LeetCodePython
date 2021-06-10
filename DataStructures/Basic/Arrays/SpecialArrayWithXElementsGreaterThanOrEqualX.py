"""
https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/

You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.



Example 1:

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.
Example 2:

Input: nums = [0,0]
Output: -1
Explanation: No numbers fit the criteria for x.
If x = 0, there should be 0 numbers >= x, but there are 2.
If x = 1, there should be 1 number >= x, but there are 0.
If x = 2, there should be 2 numbers >= x, but there are 0.
x cannot be greater since there are only 2 numbers in nums.
Example 3:

Input: nums = [0,4,3,0,4]
Output: 3
Explanation: There are 3 values that are greater than or equal to 3.
Example 4:

Input: nums = [3,6,7,7,0]
Output: -1


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums, n = sorted(nums), len(nums)
#         for i in range(1, n+1):
#             j = bisect.bisect_right(nums, i)
#             if 0 < j < n and nums[j-1] == nums[j]:
#                 continue
#             if n - j - 1 == i:
#                 return i + 1
#         return -1


# WRONG
# class Solution:
#     def specialArray(self, nums: List[int]) -> int:
#         nums, i, j = sorted(nums), 0, len(nums)
#         while i < j:
#             i += 1
#             j = bisect.bisect_right(nums, i, 0, j)
#         return -1


# Runtime: 36 ms, faster than 79.48% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
# Memory Usage: 14.1 MB, less than 75.68% of Python3 online submissions for Special Array With X Elements Greater Than or Equal X.
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)+1):
            j = bisect.bisect_left(nums, i)
            if len(nums) - j == i:
                return i
        return -1


tests = [
    [[3], 1],
    [[3,5], 2],
    [[0,0], -1],
    [[0,4,3,0,4], 3],
    [[3,6,7,7,0], -1]
]

run_functional_tests(Solution().specialArray, tests)
