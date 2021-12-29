"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 92.68% of Python3 online submissions for Single Element in a Sorted Array.
# Memory Usage: 16.4 MB, less than 75.51% of Python3 online submissions for Single Element in a Sorted Array.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        n2 = n // 2
        l, r = 0, n2
        while l < r:
            m2 = l + (r - l) // 2
            m = 2 * m2
            m1 = m + 1
            if nums[m] == nums[m1]:
                l = m2+1
            elif m > 0 and nums[m] == nums[m-1]:
                r = m2
            else:
                return nums[m]
        return nums[2*l]


tests = [
    [[1,1,2,3,3,4,4,8,8], 2],
    [[3,3,7,7,10,11,11], 10]
]

run_functional_tests(Solution().singleNonDuplicate, tests)
