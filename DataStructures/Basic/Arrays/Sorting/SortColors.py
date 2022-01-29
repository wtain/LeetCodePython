"""
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.



Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]


Constraints:

n == nums.length
1 <= n <= 300
nums[i] is 0, 1, or 2.


Follow up: Could you come up with a one-pass algorithm using only constant extra space?
"""
from typing import List

from Common.Helpers.FunctionalHelpers import make_inplace
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 98.68% of Python3 online submissions for Sort Colors.
# Memory Usage: 14 MB, less than 92.36% of Python3 online submissions for Sort Colors.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        i, l, r = 0, 0, n
        while i < r:
            if nums[i] == 0 and i >= l:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1


tests = [
    [[2,0,2,1,1,0], [0,0,1,1,2,2]],
    [[2,0,1], [0,1,2]],
    [[0], [0]],
    [[1], [1]]
]

run_functional_tests(make_inplace(Solution().sortColors), tests)