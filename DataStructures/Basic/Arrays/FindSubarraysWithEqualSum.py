"""
https://leetcode.com/problems/find-subarrays-with-equal-sum/

Given a 0-indexed integer array nums, determine whether there exist two subarrays of length 2 with equal sum. Note that the two subarrays must begin at different indices.

Return true if these subarrays exist, and false otherwise.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [4,2,4]
Output: true
Explanation: The subarrays with elements [4,2] and [2,4] have the same sum of 6.
Example 2:

Input: nums = [1,2,3,4,5]
Output: false
Explanation: No two subarrays of size 2 have the same sum.
Example 3:

Input: nums = [0,0,0]
Output: true
Explanation: The subarrays [nums[0],nums[1]] and [nums[1],nums[2]] have the same sum of 0.
Note that even though the subarrays have the same content, the two subarrays are considered different because they are in different positions in the original array.


Constraints:

2 <= nums.length <= 1000
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 67 ms
# Beats
# 60.77%
# Memory
# 14 MB
# Beats
# 43.92%
class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        seen = set()
        n = len(nums)
        for i in range(n-1):
            cs = nums[i] + nums[i+1]
            if cs in seen:
                return True
            seen.add(cs)
        return False


tests = [
    [[4,2,4], True],
    [[1,2,3,4,5], False],
    [[0,0,0], True]
]

run_functional_tests(Solution().findSubarrays, tests)
