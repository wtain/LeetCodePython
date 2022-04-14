"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.



Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104


Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 93 ms, faster than 25.20% of Python3 online submissions for Search in Rotated Sorted Array II.
# Memory Usage: 14.5 MB, less than 25.03% of Python3 online submissions for Search in Rotated Sorted Array II.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        b, e = 0, len(nums)-1
        while b <= e:
            if nums[b] == nums[e]:
                if nums[e] == target:
                    return True
                v = nums[b]
                while b < e and nums[b] == v:
                    b += 1
                while b < e and nums[e] == v:
                    e -= 1
            n = e - b
            m = b + n // 2
            if nums[m] == target:
                return True
            elif nums[b] <= nums[m]:
                if target > nums[m]:
                    b = m + 1
                elif target >= nums[b]:
                    e = m - 1
                else:
                    b = m + 1
            elif target < nums[m]:
                e = m - 1
            elif target <= nums[e]:
                b = m + 1
            else:
                e = m - 1
        return False


tests = [
    [[2,2,2,3,2,2,2], 3, True],
    [[2,5,6,0,0,1,2], 0, True],
    [[2,5,6,0,0,1,2], 3, False]
]

run_functional_tests(Solution().search, tests)
