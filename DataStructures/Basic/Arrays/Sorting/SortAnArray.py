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


# Runtime: 728 ms, faster than 65.90% of Python3 online submissions for Sort an Array.
# Memory Usage: 25.1 MB, less than 11.90% of Python3 online submissions for Sort an Array.
# https://www.geeksforgeeks.org/quick-sort/
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        def partition(low: int, high: int) -> int:
            nonlocal nums
            r = random.randint(low, high)
            nums[r], nums[high] = nums[high], nums[r]
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] < pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i+1], nums[high] = nums[high], nums[i+1]
            return i+1

        def qsort(low: int, high: int):
            while low < high:
                p = partition(low, high)
                qsort(low, p-1)
                low = p + 1

        qsort(0, n-1)

        return nums


tests = [
    [[5,2,3,1], [1,2,3,5]],
    [[5,1,1,2,0,0], [0,0,1,1,2,5]],
]


run_functional_tests(Solution().sortArray, tests)
