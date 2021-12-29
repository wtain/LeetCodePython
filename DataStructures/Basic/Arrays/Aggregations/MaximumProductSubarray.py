"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

It is guaranteed that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 68.46% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.4 MB, less than 36.06% of Python3 online submissions for Maximum Product Subarray.
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        max_p, max_n = 0, 0
        if nums[0] > 0:
            max_p = nums[0]
        else:
            max_n = nums[0]
        max_prod = nums[0]
        for v in nums[1:]:
            if v > 0:
                max_p, max_n = max(max_p*v, v), min(max_n*v, v)
            else:
                max_p, max_n = max(max_n*v, v), min(max_p*v, v)
            max_prod = max(max_prod, max_p)
        return max_prod


tests = [
    [[2,3,-2,4], 6],
    [[-2,0,-1], 0],
]

run_functional_tests(Solution().maxProduct, tests)
