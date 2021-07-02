"""
https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).

For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.

Return the maximum such product difference.



Example 1:

Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.
Example 2:

Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.


Constraints:

4 <= nums.length <= 104
1 <= nums[i] <= 104
"""
import heapq
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 172 ms, faster than 60.86% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# Memory Usage: 15.2 MB, less than 95.99% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         nums = sorted(nums)
#         return nums[-2] * nums[-1] - nums[0] * nums[1]


# Runtime: 172 ms, faster than 60.86% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# Memory Usage: 15.4 MB, less than 83.12% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# class Solution:
#     def maxProductDifference(self, nums: List[int]) -> int:
#         h1, h2 = [], []
#         heapq.heappush(h1, nums[0])
#         heapq.heappush(h1, nums[1])
#         heapq.heappush(h2, -nums[0])
#         heapq.heappush(h2, -nums[1])
#         n = len(nums)
#         for i in range(2, n):
#             if nums[i] > h1[0]:
#                 heapq.heappop(h1)
#                 heapq.heappush(h1, nums[i])
#             if -nums[i] > h2[0]:
#                 heapq.heappop(h2)
#                 heapq.heappush(h2, -nums[i])
#         return h1[0] * h1[1] - h2[0] * h2[1]


# Runtime: 168 ms, faster than 73.98% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
# Memory Usage: 15.4 MB, less than 57.43% of Python3 online submissions for Maximum Product Difference Between Two Pairs.
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        min1, min2, max1, max2 = math.inf, math.inf, -math.inf, -math.inf
        for n in nums:
            if n < min1:
                min2, min1 = min1, n
            elif n < min2:
                min2 = n
            if n > max1:
                max2, max1 = max1, n
            elif n > max2:
                max2 = n
        return max1 * max2 - min1 * min2


tests = [
    [[5,6,2,7,4], 34],
    [[4,2,5,9,7,4,8], 64]
]

run_functional_tests(Solution().maxProductDifference, tests)