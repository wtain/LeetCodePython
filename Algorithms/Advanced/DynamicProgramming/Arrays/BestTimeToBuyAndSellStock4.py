"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.


Constraints:

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 257 ms, faster than 38.65% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# Memory Usage: 13.9 MB, less than 95.05% of Python3 online submissions for Best Time to Buy and Sell Stock IV.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/discuss/2531752/Python3-DP-with-List-comprehension
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[-float('inf'), -float('inf')] for _ in range(k+1)]
        dp[0][1] = 0
        for price in prices:
            dp = [dp[0]] + \
                 [
                     [
                         max(dp[i][0], dp[i-1][1] - price), max(dp[i][1], dp[i][0] + price)
                     ] for i in range(1, len(dp))
                  ]
        return max(dp[i][1] for i in range(len(dp)))


tests = [
    [2, [2,4,1], 2],
    [2, [3,2,6,5,0,3], 7]
]

run_functional_tests(Solution().maxProfit, tests)
