"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 284 ms, faster than 27.79% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 22.4 MB, less than 16.24% of Python3 online submissions for Product of Array Except Self.
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         l, r = [1] * n, [1] * n
#         l[0] = nums[0]
#         for i in range(1, n):
#             l[i] = nums[i] * l[i-1]
#         r[-1] = nums[-1]
#         for i in range(n-2, -1, -1):
#             r[i] = nums[i] * r[i+1]
#         result = [1] * n
#         for i in range(n):
#             if i > 0:
#                 result[i] *= l[i-1]
#             if i < n-1:
#                 result[i] *= r[i+1]
#         return result


# Runtime: 301 ms, faster than 23.91% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.2 MB, less than 58.80% of Python3 online submissions for Product of Array Except Self.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prev = 1
        for i in range(n):
            result[i] *= prev
            prev *= nums[i]
        prev = 1
        for i in range(n-1, -1, -1):
            result[i] *= prev
            prev *= nums[i]
        return result


tests = [
    [[1,2,3,4], [24,12,8,6]],
    [[-1,1,0,-3,3], [0,0,9,0,0]]
]

run_functional_tests(Solution().productExceptSelf, tests)
