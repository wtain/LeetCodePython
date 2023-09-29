"""
https://leetcode.com/problems/monotonic-array/description/?envType=daily-question&envId=2023-09-29

An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.



Example 1:

Input: nums = [1,2,2,3]
Output: true
Example 2:

Input: nums = [6,5,4,4]
Output: true
Example 3:

Input: nums = [1,3,2]
Output: false


Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 803ms
# Beats 87.50%of users with Python3
# Memory
# Details
# 30.55MB
# Beats 57.79%of users with Python3
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        d1 = nums[1] - nums[0]
        for i in range(2, n):
            d = nums[i] - nums[i-1]
            if not d1:
                d1 = d
            if d1 * d < 0:
                return False
        return True


tests = [
    [[1,2,2,3], True],
    [[6,5,4,4], True],
    [[1,3,2], False],
]

run_functional_tests(Solution().isMonotonic, tests)
