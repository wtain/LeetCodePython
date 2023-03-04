"""
https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

You are given an integer array nums and two integers minK and maxK.

A fixed-bound subarray of nums is a subarray that satisfies the following conditions:

The minimum value in the subarray is equal to minK.
The maximum value in the subarray is equal to maxK.
Return the number of fixed-bound subarrays.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,3,5,2,7,5], minK = 1, maxK = 5
Output: 2
Explanation: The fixed-bound subarrays are [1,3,5] and [1,3,5,2].
Example 2:

Input: nums = [1,1,1,1], minK = 1, maxK = 1
Output: 10
Explanation: Every subarray of nums is a fixed-bound subarray. There are 10 possible subarrays.


Constraints:

2 <= nums.length <= 105
1 <= nums[i], minK, maxK <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 884 ms
# Beats
# 76.53%
# Memory
# 28.7 MB
# Beats
# 41.16%
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        result = 0
        mini, maxi, c = 0, 0, 0
        n = len(nums)
        for i in range(n):
            if nums[i] == minK:
                mini = i
            if nums[i] == maxK:
                maxi = i
            if nums[i] < minK or nums[i] > maxK:
                c = i + 1
                mini = maxi = i
            if nums[mini] == minK and nums[maxi] == maxK:
                result += min(mini - c, maxi - c) + 1
        return result


tests = [
    [[1,3,5,2,7,5], 1, 5, 2],
    [[1,1,1,1], 1, 1, 10],
]

run_functional_tests(Solution().countSubarrays, tests)
