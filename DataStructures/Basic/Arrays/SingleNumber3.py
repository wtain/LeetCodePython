"""
https://leetcode.com/problems/single-number-iii/

Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]


Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 64 ms, faster than 57.17% of Python3 online submissions for Single Number III.
# Memory Usage: 15.7 MB, less than 84.86% of Python3 online submissions for Single Number III.
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        v = reduce(lambda a, x: a ^ x, nums, 0)
        mask = 1
        while not (v & mask):
            mask <<= 1

        v0, v1 = 0, 0
        for vi in nums:
            if vi & mask:
                v1 ^= vi
            else:
                v0 ^= vi
        return [v0, v1]


tests = [
    [[1,2,1,3,2,5], [3, 5]],
    [[-1,0], [-1,0]],
    [[0,1], [0,1]]
]

run_functional_tests(Solution().singleNumber, tests, custom_check=compareSets)
