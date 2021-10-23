"""
https://leetcode.com/problems/contains-duplicate/
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
from typing import List, Set

"""
Runtime: 164 ms, faster than 27.55% of Python3 online submissions for Contains Duplicate.
Memory Usage: 19.1 MB, less than 63.78% of Python3 online submissions for Contains Duplicate.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen: Set[int] = set()
        for ni in nums:
            if ni in seen:
                return True
            seen.add(ni)
        return False


print(Solution().containsDuplicate([1,2,3,1]))  # True
print(Solution().containsDuplicate([1,2,3,4]))  # False
print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))  # True
