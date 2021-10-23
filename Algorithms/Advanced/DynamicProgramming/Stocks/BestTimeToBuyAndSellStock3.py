"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0


Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1296 ms, faster than 54.92% of Python3 online submissions for Best Time to Buy and Sell Stock III.
# Memory Usage: 27.9 MB, less than 69.80% of Python3 online submissions for Best Time to Buy and Sell Stock III.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result, n = 0, len(prices)
        if not n:
            return 0
        max_profit1, max_profit2 = [0] * n, [0] * n
        min1, max2 = prices[0], prices[-1]
        for i in range(1, n):
            max_profit1[i] = max(prices[i] - min1, max_profit1[i-1])
            min1 = min(min1, prices[i])
            i1 = n - 1 - i

            max_profit2[i1] = max(max2 - prices[i1], max_profit2[i1+1])
            max2 = max(max2, prices[i1])
        for i in range(n):
            result = max(result, max_profit1[i] + max_profit2[i])
        return result


tests = [
    [[3,3,5,0,0,3,1,4], 6],
    [[1,2,3,4,5], 4],
    [[7,6,4,3,1], 0],
    [[1], 0]
]

run_functional_tests(Solution().maxProfit, tests)