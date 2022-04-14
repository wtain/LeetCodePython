"""
https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.


Follow up:

How can we prove that at least one duplicate number must exist in nums?
Can you solve the problem in linear runtime complexity?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 628 ms, faster than 94.70% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 28 MB, less than 59.51% of Python3 online submissions for Find the Duplicate Number.
# Runtime: 735 ms, faster than 71.89% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 27.9 MB, less than 59.49% of Python3 online submissions for Find the Duplicate Number.
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)-1
        i1, i2 = 0, 0
        while True:
            i1, i2 = nums[i1], nums[nums[i2]]
            if i1 == i2:
                break
        i1 = 0
        while i1 != i2:
            i1, i2 = nums[i1], nums[i2]
        return i1


# Runtime: 2133 ms, faster than 5.04% of Python3 online submissions for Find the Duplicate Number.
# Memory Usage: 28 MB, less than 59.51% of Python3 online submissions for Find the Duplicate Number.
# https://leetcode.com/problems/find-the-duplicate-number/solution/
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         duplicate = 0
#         n = len(nums) - 1
#         bits = n.bit_length()
#         for bit in range(bits):
#             mask = 1 << bit
#             base_count, nums_count = 0, 0
#             for i in range(n+1):
#                 if i & mask:
#                     base_count += 1
#                 if nums[i] & mask:
#                     nums_count += 1
#             if nums_count > base_count:
#                 duplicate |= mask
#         return duplicate


# WRONG
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         n = len(nums) - 1
#         s = sum(nums)
#         s1 = n * (n+1) // 2
#         return s - s1


tests = [
    [[2,2,2,2,2], 2],
    [[1,3,4,2,2], 2],
    [[3,1,3,4,2], 3]
]

run_functional_tests(Solution().findDuplicate, tests)
