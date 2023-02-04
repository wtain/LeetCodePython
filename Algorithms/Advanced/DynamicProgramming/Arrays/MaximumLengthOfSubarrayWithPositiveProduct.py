"""
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Given an array of integers nums, find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.



Example 1:

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.
Example 2:

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation: The longest subarray with positive product is [1,-2,-3] which has a product of 6.
Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.
Example 3:

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 671 ms
# Beats
# 58.10%
# Memory
# 27.5 MB
# Beats
# 89.94%
# class Solution:
#     def getMaxLen(self, nums: List[int]) -> int:
#         cp, cn = 0, 0
#         if nums[0] > 0:
#             cp += 1
#         elif nums[0] < 0:
#             cn += 1
#         longest_positive = cp
#         n = len(nums)
#         for i in range(1, n):
#             cp0, cn0 = cp, cn
#             if nums[i] > 0:
#                 cp += 1
#                 if cn > 0:
#                     cn += 1
#             elif nums[i] < 0:
#                 if cp0 > 0:
#                     cn = cp0 + 1
#                 else:
#                     cn = 1
#                 if cn0 > 0:
#                     cp = cn0 + 1
#                 else:
#                     cp = 0
#             else:
#                 cn = cp = 0
#             longest_positive = max(longest_positive, cp)
#         return longest_positive


# Runtime
# 604 ms
# Beats
# 92.32%
# Memory
# 28 MB
# Beats
# 72.77%
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/solutions/2583428/c-simplest-solution-74ms-beats-100/
class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        cp, cn = 0, 0
        result = 0
        for v in nums:
            if v == 0:
                cp = cn = 0
            else:
                if v < 0:
                    cp, cn = cn, cp
                if cp > 0 or v > 0:
                    cp += 1
                if cn > 0 or v < 0:
                    cn += 1
                result = max(result, cp)
        return result


tests = [
    [[9,-8,-9,3,-10,2], 4],
    [[1,0,-1,-2,-3,4], 3],
    [[1,-2,-3,4], 4],
    [[0,1,-2,-3,-4], 3],
    [[-1,-2,-3,0,1], 2],
]

run_functional_tests(Solution().getMaxLen, tests)
# run_functional_tests(Solution().getMaxLen, tests, run_tests=3)
