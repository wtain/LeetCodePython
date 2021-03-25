"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3674/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6


Constraints:

1 < prices.length <= 5 * 104
0 < prices[i], fee < 5 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def maxProfit(self, prices: List[int], fee: int) -> int:
#         n = len(prices)
#         dp = [[0] * 2 for _ in range(n+1)]
#         dp[0][1] = None
#         for i in range(n):
#             dp[i + 1][0] = max(dp[i][0], dp[i][1] + prices[i] - fee) if dp[i][1] is not None else dp[i][0]
#             dp[i + 1][1] = max(dp[i][1], dp[i][0] - prices[i]) if dp[i][1] is not None else dp[i][0] - prices[i] if dp[i][0] - prices[i] >= 0 else None
#         # print(dp)
#         return dp[n][0]

# Runtime: 680 ms, faster than 85.87% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
# Memory Usage: 21.5 MB, less than 33.33% of Python3 online submissions for Best Time to Buy and Sell Stock with Transaction Fee.
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        cash, hold = 0, -prices[0]
        for p in prices[1:]:
            cash = max(cash, hold + p - fee)
            hold = max(hold, cash - p)
        return cash


tests = [
    ([1,3,2,8,4,9], 2, 8),
    ([1,3,7,5,10,3], 3, 6)
]

run_functional_tests(Solution().maxProfit, tests)