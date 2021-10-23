"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 420 ms, faster than 51.39% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 21.4 MB, less than 79.52% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            j = abs(nums[i]) - 1
            if nums[j] > 0:
                nums[j] = - nums[j]
        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i+1)

        return result


tests = [
    [[4,3,2,7,8,2,3,1], [5, 6]]
]
run_functional_tests(Solution().findDisappearedNumbers, tests)
