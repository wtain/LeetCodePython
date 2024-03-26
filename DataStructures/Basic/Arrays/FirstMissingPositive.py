"""
https://leetcode.com/problems/first-missing-positive/description/?envType=daily-question&envId=2024-03-26

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.



Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 279
# ms
# Beats
# 79.68%
# of users with Python3
# Memory
# 30.31
# MB
# Beats
# 55.57%
# of users with Python3
# https://leetcode.com/problems/first-missing-positive/editorial/?envType=daily-question&envId=2024-03-26
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         seen = [False] * (n+1)
#
#         for num in nums:
#             if 0 < num <= n:
#                 seen[num] = True
#
#         for i in range(1, n+1):
#             if not seen[i]:
#                 return i
#
#         return n+1


# Runtime
# 289
# ms
# Beats
# 65.54%
# of users with Python3
# Memory
# 30.26
# MB
# https://leetcode.com/problems/first-missing-positive/editorial/?envType=daily-question&envId=2024-03-26
# class Solution:
#     def firstMissingPositive(self, nums: List[int]) -> int:
#         n = len(nums)
#         contains_1 = False
#         for i in range(n):
#             if nums[i] == 1:
#                 contains_1 = True
#             if nums[i] <= 0 or nums[i] > n:
#                 nums[i] = 1
#
#         if not contains_1:
#             return 1
#
#         for i in range(n):
#             value = abs(nums[i])
#             if value == n:
#                 nums[0] = -abs(nums[0])
#             else:
#                 nums[value] = - abs(nums[value])
#
#         for i in range(1, n):
#             if nums[i] > 0:
#                 return i
#
#         if nums[0] > 0:
#             return n
#
#         return n+1


# Runtime
# 297
# ms
# Beats
# 52.46%
# of users with Python3
# Memory
# 30.40
# MB
# Beats
# 55.57%
# of users with Python3
# https://leetcode.com/problems/first-missing-positive/editorial/?envType=daily-question&envId=2024-03-26
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        i = 0
        while i < n:
            correct_idx = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                return i + 1
        return n + 1


tests = [
    [[1,2,0], 3],
    [[3,4,-1,1], 2],
    [[7,8,9,11,12], 1],
    [[1], 2]
]

run_functional_tests(Solution().firstMissingPositive, tests)
