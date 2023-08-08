"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 55ms
# Beats 60.27%of users with Python3
# Memory
# Details
# 16.65mb
# Beats 72.11%of users with Python3
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        b, e = 0, len(nums)-1
        while b <= e:
            n = e - b
            m = b + n // 2
            if nums[m] == target:
                return m
            if nums[b] <= nums[m]:
                if target > nums[m]:
                    b = m+1
                elif target >= nums[b]:
                    e = m-1
                else:
                    b = m+1
            elif target < nums[m]:
                e = m-1
            elif target <= nums[e]:
                b = m+1
            else:
                e = m-1
        return -1


tests = [
    [[4,5,6,7,0,1,2], 0, 4],
    [[4,5,6,7,0,1,2], 3, -1],
    [[1], 0, -1],
]

run_functional_tests(Solution().search, tests)
