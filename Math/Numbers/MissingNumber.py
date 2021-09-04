"""
https://leetcode.com/problems/missing-number/
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3659/
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
from typing import List


"""
Runtime: 156 ms, faster than 46.92% of Python3 online submissions for Missing Number.
Memory Usage: 15.1 MB, less than 40.52% of Python3 online submissions for Missing Number.
"""
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        s = (n * (n+1)) // 2
        return s - sum(nums)


print(Solution().missingNumber([3,0,1]))  # 2
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))  # 8

