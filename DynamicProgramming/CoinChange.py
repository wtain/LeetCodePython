"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3668/
https://leetcode.com/problems/coin-change/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
Example 4:

Input: coins = [1], amount = 1
Output: 1
Example 5:

Input: coins = [1], amount = 2
Output: 2


Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""
from typing import List


# Runtime: 956 ms, faster than 91.39% of Python3 online submissions for Coin Change.
# Memory Usage: 14.2 MB, less than 92.44% of Python3 online submissions for Coin Change.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for am in range(1, amount+1):
            v = -1
            for c in coins:
                am1 = am - c
                if am1 < 0:
                    continue
                if dp[am1] == -1:
                    continue
                newv = dp[am1] + 1
                if v == -1 or newv < v:
                    v = newv
            dp[am] = v
        return dp[amount]


tests = [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2)
]

for test in tests:
    result = Solution().coinChange(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))