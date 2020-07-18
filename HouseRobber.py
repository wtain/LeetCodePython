"""
https://leetcode.com/problems/house-robber/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
"""
from typing import List

"""
Runtime: 32 ms, faster than 69.04% of Python3 online submissions for House Robber.
Memory Usage: 13.8 MB, less than 59.62% of Python3 online submissions for House Robber.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        result: List[List[int]] = [[0] * 2 for i in range(n)]
        result[0][0] = 0
        result[0][1] = nums[0]
        for i in range(1, n):
            result[i][0] = max(result[i - 1][0], result[i - 1][1])
            result[i][1] = max(nums[i] + result[i - 1][0], result[i - 1][1])

        return max(result[n - 1][0], result[n - 1][1])


print(Solution().rob([]))  # 0
print(Solution().rob([1, 2, 3, 1]))  # 4
print(Solution().rob([2, 7, 9, 3, 1]))  # 12
