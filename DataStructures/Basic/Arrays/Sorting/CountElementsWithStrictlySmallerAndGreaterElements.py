"""
https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements/

Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.



Example 1:

Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
Example 2:

Input: nums = [-3,3,3,90]
Output: 2
Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.


Constraints:

1 <= nums.length <= 100
-105 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 54 ms, faster than 62.34% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .
# Memory Usage: 13.8 MB, less than 89.42% of Python3 online submissions for Count Elements With Strictly Smaller and Greater Elements .
class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i1, i2 = 0, n-1
        while i1 < n and nums[0] == nums[i1]:
            i1 += 1
        while i2 >= 0 and nums[-1] == nums[i2]:
            i2 -= 1
        return max(0, i2-i1+1)


tests = [
    [[-89,39,39,-89,39,39], 0],
    [[11,7,2,15], 2],
    [[-3,3,3,90], 2]
]

run_functional_tests(Solution().countElements, tests)
