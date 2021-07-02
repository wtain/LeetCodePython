"""
https://leetcode.com/problems/maximum-ascending-subarray-sum/

Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi < numsi+1. Note that a subarray of size 1 is ascending.



Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
Example 4:

Input: nums = [100,10,1]
Output: 100


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 79.84% of Python3 online submissions for Maximum Ascending Subarray Sum.
# Memory Usage: 14.3 MB, less than 10.32% of Python3 online submissions for Maximum Ascending Subarray Sum.
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        prev = -math.inf
        curr_sum = 0
        for n in nums:
            if prev >= n:
                curr_sum = 0
            curr_sum += n
            prev = n
            max_sum = max(max_sum, curr_sum)
        return max_sum


tests = [
    [[10,20,30,5,10,50], 65],
    [[10,20,30,40,50], 150],
    [[12,17,15,13,10,11,12], 33],
    [[100,10,1], 100]
]

run_functional_tests(Solution().maxAscendingSum, tests)