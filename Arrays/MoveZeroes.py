"""
https://leetcode.com/problems/move-zeroes/
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
from typing import List


"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        " " "
        Do not return anything, modify nums in-place instead.
        " " "

        n = len(nums)
        l = 0
        r = n-1
        while l < r:
            while l < n and nums[l] != 0:
                l += 1
            while r >= 0 and nums[r] == 0:
                r -= 1
            if l < r:
                tmp = nums[l]
                nums[l] = nums[r]
                nums[r] = tmp
                l += 1
                r -= 1
"""

"""
Runtime: 380 ms, faster than 7.69% of Python3 online submissions for Move Zeroes.
Memory Usage: 15 MB, less than 67.59% of Python3 online submissions for Move Zeroes.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        w = 0
        r = 0
        while r < n:
            while w < n and nums[w] != 0:
                w += 1
            if w == n:
                break
            r = w+1
            while r < n and nums[r] == 0:
                r += 1
            if r == n:
                break
            tmp = nums[w]
            nums[w] = nums[r]
            nums[r] = tmp
            w += 1
            r -= 1


l1 = [0, 1, 0, 3, 12]
Solution().moveZeroes(l1)
print(l1)  # [1,3,12,0,0]
