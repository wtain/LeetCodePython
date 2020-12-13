"""
https://leetcode.com/problems/burst-balloons/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3564/
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
Example:

Input: [3,1,5,8]
Output: 167
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167

Runtime: 384 ms, faster than 84.81% of Python3 online submissions for Burst Balloons.
Memory Usage: 14.8 MB, less than 56.27% of Python3 online submissions for Burst Balloons.
"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A = [1] + nums + [1]
        n = len(A)
        dp: List[List[int]] = [[0] * n for i in range(n)]

        for l in range(n+1):
            for i in range(n-l):
                mx = 0
                j = i + l
                for k in range(i+1, j):
                    v = A[i] * A[k] * A[j] + dp[i][k] + dp[k][j]
                    mx = max(mx, v)
                dp[i][j] = mx

        return dp[0][n-1]


print(Solution().maxCoins( [3,1,5,8]))  # 167