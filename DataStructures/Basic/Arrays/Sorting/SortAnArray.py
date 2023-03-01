"""
https://leetcode.com/problems/sort-an-array/

Given an array of integers nums, sort the array in ascending order.



Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]


Constraints:

1 <= nums.length <= 5 * 104
-5 * 104 <= nums[i] <= 5 * 104
"""
import random
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE on big array of same value
# Runtime: 728 ms, faster than 65.90% of Python3 online submissions for Sort an Array.
# Memory Usage: 25.1 MB, less than 11.90% of Python3 online submissions for Sort an Array.
# https://www.geeksforgeeks.org/quick-sort/
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         def partition(low: int, high: int) -> int:
#             nonlocal nums
#             r = random.randint(low, high)
#             nums[r], nums[high] = nums[high], nums[r]
#             pivot = nums[high]
#             i = low - 1
#             for j in range(low, high):
#                 if nums[j] < pivot:
#                     i += 1
#                     nums[i], nums[j] = nums[j], nums[i]
#             nums[i+1], nums[high] = nums[high], nums[i+1]
#             return i+1
#
#         def qsort(low: int, high: int):
#             while low < high:
#                 p = partition(low, high)
#                 qsort(low, p-1)
#                 low = p + 1
#
#         qsort(0, n-1)
#
#         return nums


# TLE
# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#
#         def helper(head, tail):
#             if head >= tail:
#                 return
#             l, r = head, tail
#             m = (r - l) // 2 + l
#             pivot = nums[m]
#             while r >= l:
#                 while r >= l and nums[l] < pivot:
#                     l += 1
#                 while r >= l and nums[r] > pivot:
#                     r -= 1
#                 if r >= l:
#                     nums[l], nums[r] = nums[r], nums[l]
#                     l += 1
#                     r -= 1
#                 helper(head, r)
#                 helper(l, tail)
#
#         helper(0, n-1)
#
#         return nums

# Runtime
# 2675 ms
# Beats
# 18.80%
# Memory
# 33.1 MB
# Beats
# 7.18%
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def heapify(n, i):
            l = 2 * i + 1
            r = 2 * i + 2

            largest = i
            if l < n and nums[largest] < nums[l]:
                largest = l
            if r < n and nums[largest] < nums[r]:
                largest = r

            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(n, largest)

        for i in reversed(range(n // 2 + 1)):
            heapify(n, i)

        for i in reversed(range(n)):
            nums[i], nums[0] = nums[0], nums[i]
            heapify(i, 0)

        return nums


tests = [
    [[-4,0,7,4,9,-5,-1,0,-7,-1], [-7,-5,-4,-1,-1,0,0,4,7,9]],
    [[2] * 50000, [2] * 50000],
    [[2] * 1000, [2] * 1000],
    [[5,2,3,1], [1,2,3,5]],
    [[5,1,1,2,0,0], [0,0,1,1,2,5]],
]


run_functional_tests(Solution().sortArray, tests)
