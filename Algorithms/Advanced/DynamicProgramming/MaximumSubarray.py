"""
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List

"""
Runtime: 88 ms, faster than 27.46% of Python3 online submissions for Maximum Subarray.
Memory Usage: 14.7 MB, less than 21.36% of Python3 online submissions for Maximum Subarray.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = ms = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            s = max(s+n, n)
            ms = max(ms, s)
        return ms


print(Solution().maxSubArray([-2, 1]))  # 1
print(Solution().maxSubArray([1]))  # 1
print(Solution().maxSubArray([-1]))  # -1
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6