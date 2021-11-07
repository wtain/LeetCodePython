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

from Common.ObjectTestingUtils import run_functional_tests

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


tests = [
    [[1,2,3,1], True],
    [[1,2,3,4], False],
    [[1,1,1,3,3,4,3,2,4,2], True]
]

run_functional_tests(Solution().containsDuplicate, tests)
