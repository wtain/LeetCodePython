"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/

Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 295 ms
# Beats
# 11.35%
# Memory
# 29.1 MB
# Beats
# 41.5%
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i1, i2 = 0, 0
        cs = 0
        n = len(nums)
        minlen = n
        found = False
        while i1 < n:
            if cs < target and i2 < n:
                cs += nums[i2]
                i2 += 1
            else:
                cs -= nums[i1]
                i1 += 1
            ln = i2 - i1
            if cs >= target and (minlen > ln or not found):
                minlen = ln
                found = True
        return minlen if found else 0


tests = [
    [7, [2,3,1,2,4,3], 2],
    [4, [1,4,4], 1],
    [11, [1,1,1,1,1,1,1,1], 0],
]

run_functional_tests(Solution().minSubArrayLen, tests)
