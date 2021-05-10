"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).



Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.


Constraints:

n == nums.length
1 <= n <= 104
-105 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 188 ms, faster than 40.54% of Python3 online submissions for Non-decreasing Array.
# Memory Usage: 15.4 MB, less than 23.13% of Python3 online submissions for Non-decreasing Array.
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        j = -1
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                if j != -1:
                    return False
                j = i - 1
        if j <= 0:
            return True
        if j >= n-2:
            return True
        return nums[j-1] <= nums[j+1] or nums[j] <= nums[j+2]


tests = [
    [[4,2,3], True],
    [[4,2,1], False]
]

run_functional_tests(Solution().checkPossibility, tests)