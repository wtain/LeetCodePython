"""
https://leetcode.com/problems/search-insert-position/
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""
from typing import List

"""
Runtime: 80 ms, faster than 19.71% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.5 MB, less than 48.69% of Python3 online submissions for Search Insert Position.
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m
        return l


print(Solution().searchInsert([1,3,5,6], 5))  # 2
print(Solution().searchInsert([1,3,5,6], 2))  # 1
print(Solution().searchInsert([1,3,5,6], 7))  # 4
print(Solution().searchInsert([1,3,5,6], 0))  # 0