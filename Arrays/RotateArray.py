"""
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?


Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 2 * 10^4
It's guaranteed that nums[i] fits in a 32 bit-signed integer.
k >= 0
"""
from typing import List

"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0 or len(nums) == 0:
            return
        if k < 0:
            self.rotate(nums, -k)
        for m in range(k):
            temp = nums[len(nums)-1]
            for i in range(len(nums)-1, 0, -1):
                nums[i] = nums[i-1]
            nums[0] = temp
        "" "
        Do not return anything, modify nums in-place instead.
        "" "
"""


"""
Runtime: 76 ms, faster than 49.51% of Python3 online submissions for Rotate Array.
Memory Usage: 15.3 MB, less than 55.55% of Python3 online submissions for Rotate Array.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if k == 0 or n == 0:
            return
        i = 0
        moves = 0
        while moves < n:
            temp = nums[i]
            i0 = i
            j = (n + i - k) % n
            while j != i0:
                nums[i] = nums[j]
                i = j
                j = (i - k) % n
                moves += 1
            moves += 1
            nums[i] = temp
            i += 1

        """
        Do not return anything, modify nums in-place instead.
        """

a1 = [1, 2, 3, 4, 5, 6, 7]
Solution().rotate(a1, 3)
print(a1)  # [5,6,7,1,2,3,4]

a2 = [-1, -100, 3, 99]
Solution().rotate(a2, 2)
print(a2)  # [3,99,-1,-100]
