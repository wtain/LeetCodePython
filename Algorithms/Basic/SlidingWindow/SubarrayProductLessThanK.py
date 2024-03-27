"""
https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-27

Given an array of integers nums and an integer k, return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.



Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0


Constraints:

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 490
# ms
# Beats
# 87.78%
# of users with Python3
# Memory
# 19.22
# MB
# Beats
# 50.02%
# of users with Python3
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        p, cnt = 1, 0
        i1 = 0
        for i2 in range(n):
            p *= nums[i2]
            while p >= k and i1 < i2:
                p //= nums[i1]
                i1 += 1
            if p < k:
                cnt += i2 - i1 + 1
        return cnt


tests = [
    [[10,5,2,6], 100, 8],
    [[1,2,3], 0, 0],
]

run_functional_tests(Solution().numSubarrayProductLessThanK, tests)
