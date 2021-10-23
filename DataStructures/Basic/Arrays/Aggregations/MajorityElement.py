"""
https://leetcode.com/problems/majority-element/
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 216 ms, faster than 33.40% of Python3 online submissions for Majority Element.
Memory Usage: 15.3 MB, less than 24.30% of Python3 online submissions for Majority Element.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        maj = -1
        cnt = 0
        for i in range(n):
            if 0 == cnt:
                maj = nums[i]
                cnt = 1
            elif nums[i] == maj:
                cnt += 1
            else:
                cnt -= 1
        return maj


tests = [
    [[3,2,3], 3],
    [[2,2,1,1,1,2,2], 2],
    [[3,3,4],3]
]

run_functional_tests(Solution().majorityElement, tests)