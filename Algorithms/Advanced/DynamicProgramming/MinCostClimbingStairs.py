"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3770/
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.



Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: Cheapest is: start on cost[1], pay that cost, and go to the top.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: Cheapest is: start on cost[0], and only step on 1s, skipping cost[3].


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 88 ms, faster than 6.54% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.4 MB, less than 44.78% of Python3 online submissions for Min Cost Climbing Stairs.
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         n = len(cost)
#         cost += [0]
#         dp = [0] * (n+1)
#         dp[0], dp[1] = cost[0], cost[1]
#         for i in range(2, n+1):
#             dp[i] = cost[i] + min(dp[i-1], dp[i-2])
#         return dp[n]


# Runtime: 92 ms, faster than 5.57% of Python3 online submissions for Min Cost Climbing Stairs.
# Memory Usage: 14.4 MB, less than 44.78% of Python3 online submissions for Min Cost Climbing Stairs.
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost += [0]
        dp0, dp1, dp2 = cost[0], cost[1], 0
        for i in range(2, n+1):
            dp2 = cost[i] + min(dp0, dp1)
            dp0, dp1 = dp1, dp2
        return dp2


tests = [
    [[10,15,20], 15],
    [[1,100,1,1,1,100,1,1,100,1], 6]
]

run_functional_tests(Solution().minCostClimbingStairs, tests)