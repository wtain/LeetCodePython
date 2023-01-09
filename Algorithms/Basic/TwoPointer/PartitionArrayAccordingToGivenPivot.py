"""
https://leetcode.com/problems/partition-array-according-to-given-pivot/

You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. For elements less than pivot, if i < j and nums[i] < pivot and nums[j] < pivot, then pi < pj. Similarly for elements greater than pivot, if i < j and nums[i] > pivot and nums[j] > pivot, then pi < pj.
Return nums after the rearrangement.



Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation:
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
Example 2:

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation:
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.


Constraints:

1 <= nums.length <= 105
-106 <= nums[i] <= 106
pivot equals to an element of nums.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         i = 0
#         for j in range(1, n):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         return nums

# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         l, r = 0, n-1
#         while l < r:
#
#         return nums

# https://leetcode.com/problems/partition-array-according-to-given-pivot/solutions/2883811/simple-java-solution/
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         numless, numequal, numgreater = 0, 0, 0
#         for i in range(n):
#             if nums[i] < pivot:
#                 numless += 1
#             elif nums[i] > pivot:
#                 numgreater += 1
#             else:
#                 numequal += 1
#
#         return nums


# WRONG
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         l, r = 0, n-1
#         while l < r:
#             while l < r and nums[l] < pivot:
#                 l += 1
#             while l < r and nums[r] > pivot:
#                 r -= 1
#             if l >= n or r < 0:
#                 break
#             nums[l], nums[r] = nums[r], nums[l]
#             l += 1
#             r -= 1
#         return nums

# https://leetcode.com/problems/partition-array-according-to-given-pivot/solutions/2711593/python-easy-solution-faster-than-99-21-in-o-n-complexity/
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:


# WRONG
# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         w = 0
#         l, r = 0, n-1
#         while l < r:
#             if nums[l] < pivot:
#                 nums[w] = nums[l]
#                 w += 1
#                 l += 1
#             elif nums[r] < pivot:
#                 nums[w] = nums[r]
#                 w += 1
#                 r -= 1
#             else:
#                 l += 1
#                 r -= 1
#         for i in range(n):
#             if nums[i] == pivot:
#                 nums[w], nums[i] = nums[i], nums[w]
#                 w += 1
#
#         return nums

# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         wl, wr = 0, n-1
#         i = 0
#         while i < n and i < wr:
#             if nums[i] >= pivot:
#                 nums[i], nums[wr] = nums[wr], nums[i]
#                 wr -= 1
#             else:
#                 i += 1
#
#         return nums


# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         nums.append(pivot)
#         i = 0
#         for j in range(n):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         nums[i], nums[n] = nums[n], nums[i]
#         nums.pop()
#         return nums


# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         nums = [pivot] + nums
#         n = len(nums)
#         last = n-1
#         i = 0
#         while i < n:
#             i += 1
#             if nums[i] <= pivot:
#                 nums[i], nums[i-1] = nums[i-1], nums[i]
#             elif nums[i] > pivot and last > i:
#                 nums[i], nums[last] = nums[last], nums[i]
#                 last -= 1
#                 i -= 1
#             else:
#                 break
#         return nums[1:]

# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         i = 0
#         for j in range(n):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         for j in range(i, n):
#             if nums[j] == pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         return nums


# class Solution:
#     def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
#         n = len(nums)
#         i = 0
#         for j in range(n):
#             if nums[j] < pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i += 1
#         i0 = i
#         i = n - 1
#         for j in range(n-1, i0-1, -1):
#             if nums[j] > pivot:
#                 nums[i], nums[j] = nums[j], nums[i]
#                 i -= 1
#         return nums


# Runtime
# 1439 ms
# Beats
# 93.7%
# Memory
# 31.6 MB
# Beats
# 33.96%
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        n = len(nums)
        result = [pivot] * n
        wl, wr = 0, n-1
        for i in range(n):
            if nums[i] < pivot:
                result[wl] = nums[i]
                wl += 1
        for i in range(n-1, -1, -1):
            if nums[i] > pivot:
                result[wr] = nums[i]
                wr -= 1
        return result


tests = [
    [[9,12,5,10,14,3,10], 10, [9,5,3,10,10,12,14]],
    [[-3,4,3,2], 2, [-3,2,4,3]],
]

run_functional_tests(Solution().pivotArray, tests)
