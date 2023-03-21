"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation:
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. Therefore, we return 9.
Example 3:

Input: nums = [2,10,2019]
Output: 0
Explanation: There is no subarray filled with 0. Therefore, we return 0.


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1098 ms
# Beats
# 67.49%
# Memory
# 24.5 MB
# Beats
# 78.9%
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        i1 = 0
        while i1 < n:
            while i1 < n and nums[i1]:
                i1 += 1
            i2 = i1
            while i2 < n and nums[i2] == 0:
                i2 += 1
            cnt = i2 - i1
            result += cnt * (cnt+1) // 2
            i1 = i2
        return result


tests = [
    [[1,3,0,0,2,0,0,4], 6],
    [[0,0,0,2,0,0], 9],
    [[2,10,2019], 0],
]

run_functional_tests(Solution().zeroFilledSubarray, tests)
