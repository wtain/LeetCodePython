"""
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 244 ms, faster than 92.12% of Python3 online submissions for Binary Search.
# Memory Usage: 15.4 MB, less than 77.82% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r, = 0, len(nums)
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1


tests = [
    [[5], 5, 0],
    [[-1,0,3,5,9,12], 9, 4],
    [[-1,0,3,5,9,12], 2, -1]
]

run_functional_tests(Solution().search, tests)
