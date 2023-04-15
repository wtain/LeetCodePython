"""
https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/description/

There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.



Example 1:


Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.


Constraints:

n == piles.length
1 <= n <= 1000
1 <= piles[i][j] <= 105
1 <= k <= sum(piles[i].length) <= 2000
"""
from functools import cache
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# O(n^k) - top-down, recursive
# class Solution:
#     def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
#         n = len(piles)
#         # for i in range(n):
#         #     piles[i] = list(accumulate(piles[i], lambda s, t: s+t))
#
#         def dp(indices, k):
#             if k == 0:
#                 return 0
#             result = 0
#             for i in range(n):
#                 if indices[i] < len(piles[i]):
#                     indices[i] += 1
#                     res = dp(indices, k-1) + piles[i][indices[i]-1]
#                     indices[i] -= 1
#                     result = max(result, res)
#             return result
#
#         return dp([0] * n, k)

# class Solution:
#     def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
#         n = len(piles)
#         # for i in range(n):
#         #     piles[i] = list(accumulate(piles[i], lambda s, t: s+t))
#
#         def dp(indices, k):
#             if k == 0:
#                 return 0
#             result = 0
#             for i in range(n):
#                 if indices[i] < len(piles[i]):
#                     indices[i] += 1
#                     res = dp(indices, k-1) + piles[i][indices[i]-1]
#                     indices[i] -= 1
#                     result = max(result, res)
#             return result
#
#         return dp([0] * n, k)


# class Solution:
#     def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
#         n = len(piles)
#         dp = [[0] * (k+1) for _ in range(n)]
#         for j in range(min(len(piles[0]), k)):
#             dp[0][j+1] = dp[0][j] + piles[0][j]
#
#         for i in range(1, n):
#             for j in range(min(len(piles[i]), k)):
#                 dp[i][j + 1] = max(dp[i][j] + piles[i][j], dp[i-1][j+1])
#
#         return dp[-1][-1]


# Runtime
# 8284 ms
# Beats
# 5.3%
# Memory
# 53.6 MB
# Beats
# 67.30%
# https://leetcode.com/problems/maximum-value-of-k-coins-from-piles/editorial/
class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for coins in range(k+1):
                cs = 0
                for current_coins in range(min(len(piles[i-1]), coins)+1):
                    if current_coins > 0:
                        cs += piles[i-1][current_coins-1]
                    dp[i][coins] = max(dp[i][coins], dp[i-1][coins - current_coins] + cs)

        return dp[-1][-1]

"""
i0...i(n-1)
sum(ij) == k
sum(prefix(ij)) -> max
prefix(ij) = piles[i][0] + ... + piles[i][j-1]
"""


tests = [
    [[[1,100,3],[7,8,9]], 2, 101],
    [[[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7, 706],
]

run_functional_tests(Solution().maxValueOfCoins, tests)
