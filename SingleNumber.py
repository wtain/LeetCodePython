"""
https://leetcode.com/problems/single-number/

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""
from typing import List

"""
Runtime: 116 ms, faster than 37.86% of Python3 online submissions for Single Number.
Memory Usage: 16.4 MB, less than 17.61% of Python3 online submissions for Single Number.
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for n in nums:
            result = result ^ n
        return result


print(Solution().singleNumber([2,2,1]))  # 1
print(Solution().singleNumber([4,1,2,1,2]))  # 4
