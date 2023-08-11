"""
https://leetcode.com/problems/coin-change-ii/description/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.



Example 1:

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1
Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.
Example 3:

Input: amount = 10, coins = [10]
Output: 1


Constraints:

1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 170ms
# Beats 78.17%of users with Python3
# Memory
# Details
# 16.66mb
# Beats 68.27%of users with Python3
# class Solution:
#     def change(self, amount: int, coins: List[int]) -> int:
#         if not coins:
#             return 0 if amount else 1
#         n = amount + 1
#         dp = [0] * n
#         dp[0] = 1
#         for coin in coins:
#             for current_amount in range(1, n):
#                 new_amount = current_amount - coin
#                 if new_amount >= 0:
#                     dp[current_amount] += dp[new_amount]
#         return dp[amount]

# Runtime
# Details
# 182ms
# Beats 76.74%of users with Python3
# Memory
# Details
# 16.47mb
# Beats 89.60%of users with Python3
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = amount + 1
        dp = [0] * n
        dp[0] = 1
        for coin in coins:
            for current_amount in range(1, n):
                new_amount = current_amount - coin
                if new_amount >= 0:
                    dp[current_amount] += dp[new_amount]
        return dp[amount]


tests = [
    [10, [], 0],
    [5, [1,2,5], 4],
    [3, [2], 0],
    [10, [10], 1]
]

run_functional_tests(Solution().change, tests)
