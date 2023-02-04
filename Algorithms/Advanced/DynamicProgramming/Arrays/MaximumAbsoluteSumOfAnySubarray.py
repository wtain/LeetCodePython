"""
https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is abs(numsl + numsl+1 + ... + numsr-1 + numsr).

Return the maximum absolute sum of any (possibly empty) subarray of nums.

Note that abs(x) is defined as follows:

If x is a negative integer, then abs(x) = -x.
If x is a non-negative integer, then abs(x) = x.


Example 1:

Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = abs(2+3) = abs(5) = 5.
Example 2:

Input: nums = [2,-5,1,-4,3,-2]
Output: 8
Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 546 ms
# Beats
# 59.9%
# Memory
# 27.7 MB
# Beats
# 85.66%
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        p, n = 0, 0
        max_abs_sum = 0
        for v in nums:
            p = max(p + v, v)
            n = min(n + v, v)
            max_abs_sum = max(max_abs_sum, abs(p), abs(n))
        return max_abs_sum


tests = [
    [[1,-3,2,3,-4], 5],
    [[2,-5,1,-4,3,-2], 8],
]

run_functional_tests(Solution().maxAbsoluteSum, tests)
