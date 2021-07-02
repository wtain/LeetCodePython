"""
https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).



Example 1:

Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
Example 2:

Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.
Example 3:

Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
Example 4:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is already strictly increasing, so return true.


Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# WRONG
# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         n = len(nums)
#         changed = False
#         for i in range(1, n):
#             if nums[i-1] < nums[i]:
#                 continue
#             if changed:
#                 return False
#             if i+1 < n and nums[i+1] - nums[i-1] < 2:
#                 return False
#             nums[i] = nums[i-1]+1
#             changed = True
#         return True


# WRONG
# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         n = len(nums)
#         l, r = 0, n-1
#         while l+1 < r and nums[l] < nums[l+1]:
#             l += 1
#         while l < r and nums[r-1] < nums[r]:
#             r -= 1
#         if l >= r:
#             return True
#         print(nums[l:r+1])
#         return False

# For each index i in nums remove this index.
# If the array becomes sorted return true, otherwise revert to the original array and try different index.


# Runtime: 596 ms, faster than 16.29% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.
# Memory Usage: 14.4 MB, less than 50.11% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.
# class Solution:
#     def canBeIncreasing(self, nums: List[int]) -> bool:
#         n = len(nums)
#         for i in range(n):
#             prev = None
#             is_sorted = True
#             for j in range(n):
#                 if i == j:
#                     continue
#                 if prev is not None:
#                     if nums[j] <= prev:
#                         is_sorted = False
#                         break
#                 prev = nums[j]
#             if is_sorted:
#                 return True
#         return False


# Runtime: 48 ms, faster than 90.77% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.
# Memory Usage: 14.6 MB, less than 15.00% of Python3 online submissions for Remove One Element to Make the Array Strictly Increasing.
# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/discuss/1305915/Java-0ms-beats-100
class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        removed = False
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                continue
            a2 = nums[i-2] if i >= 2 else -math.inf
            a1 = nums[i+1] if i < n-1 else math.inf
            if a2 < nums[i] < a1 or a2 < nums[i - 1] < a1:
                if removed:
                    return False
                removed = True
            else:
                return False
        return True


tests = [
    [[1,2,10,5,7], True],
    [[2,3,1,2], False],
    [[1,1,1], False],


    [[1,2,1,4,5], True]
]

run_functional_tests(Solution().canBeIncreasing, tests)