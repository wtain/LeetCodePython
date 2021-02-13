"""
https://leetcode.com/problems/squares-of-a-sorted-array/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3567/
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.



Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.

Runtime: 240 ms, faster than 31.40% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 16.3 MB, less than 13.21% of Python3 online submissions for Squares of a Sorted Array.
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result: List[int] = [0] * n
        i1 = 0
        i2 = n-1
        for w in reversed(range(n)):
            if abs(nums[i1]) > abs(nums[i2]):
                result[w] = nums[i1] ** 2
                i1 += 1
            else:
                result[w] = nums[i2] ** 2
                i2 -= 1

        return result


print(Solution().sortedSquares([-4,-1,0,3,10]))  # [0,1,9,16,100]
print(Solution().sortedSquares([-7,-3,2,3,11]))  # [4,9,9,49,121]
