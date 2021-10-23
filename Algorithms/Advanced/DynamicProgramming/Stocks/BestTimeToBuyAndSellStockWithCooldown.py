"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
Example 2:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 5000
0 <= prices[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 76.30% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
# Memory Usage: 14.6 MB, less than 63.31% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if not n:
            return 0
        dp = [[0, 0] for _ in range(n)]
        dp[0][1] = -prices[0]
        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], dp[i-1][1] + prices[i])

            if i >= 2:
                dp[i][1] = max(dp[i-1][1], dp[i-2][0] - prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        return dp[-1][0]


tests = [
    [[1,2,3,0,2], 3],
    [[1], 0]
]

run_functional_tests(Solution().maxProfit, tests)