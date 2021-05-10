"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3725/
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect.bisect_left(nums, target)
        if 0 <= l < len(nums) and nums[l] == target:
            r = bisect.bisect_right(nums, target) - 1
        else:
            return [-1, -1]
        return [l, r]


tests = [
    [
        [5,7,7,8,8,10], 8, [3, 4]
    ],
    [
        [5,7,7,8,8,10], 6, [-1, -1]
    ],
    [
        [], 0, [-1, -1]
    ]
]

run_functional_tests(Solution().searchRange, tests)