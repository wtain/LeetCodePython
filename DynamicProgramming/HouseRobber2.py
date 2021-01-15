"""
https://leetcode.com/problems/house-robber-ii/
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [0]
Output: 0


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""
from typing import List


# Runtime: 32 ms, faster than 63.78% of Python3 online submissions for House Robber II.
# Memory Usage: 14.2 MB, less than 79.77% of Python3 online submissions for House Robber II.
class Solution:
    def rob(self, nums: List[int]) -> int:
        def robImpl(nums: List[int]) -> int:
            n = len(nums)
            if not n:
                return 0
            dp = [[0] * 2 for i in range(n)]
            dp[0][0] = nums[0]
            dp[0][1] = 0
            for i in range(1, n):
                dp[i][0] = max(nums[i] + dp[i-1][1], dp[i-1][0])
                dp[i][1] = max(dp[i-1][0], dp[i-1][1])
            return max(dp[-1][0], dp[-1][1])

        if len(nums) == 1:
            return nums[0]

        return max(robImpl(nums[1:]), robImpl(nums[:-1]))

tests = [
    ([1], 1),

    ([2,3,2], 3),
    ([1,2,3,1], 4),
    ([0], 0)
]

for test in tests:
    result = Solution().rob(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))