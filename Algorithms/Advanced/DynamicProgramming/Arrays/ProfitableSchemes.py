"""
https://leetcode.com/problems/profitable-schemes/description/

There is a group of n members, and a list of various crimes they could commit. The ith crime generates a profit[i] and requires group[i] members to participate in it. If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least minProfit profit, and the total number of members participating in that subset of crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).


Constraints:

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#
#         result = 0
#         m = len(group)
#
#         def dp(n, i0, p):
#             nonlocal result, m
#             if p >= minProfit:
#                 result += 1
#             if i0 == m:
#                 return
#             for i in range(i0, m):
#                 dp(n - group[i], i+1, p + profit[i])
#
#         dp(n, 0, 0)
#
#         return result

# TLE
# https://leetcode.com/problems/profitable-schemes/editorial/
# class Solution:
#     def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def dp(pos, count, p):
#             if pos == len(group):
#                 return 1 if p >= minProfit else 0
#
#             totalWays = dp(pos+1, count, p)
#             if count + group[pos] <= n:
#                 totalWays += dp(pos+1, count+group[pos], p + profit[pos])
#
#             return totalWays % MOD
#
#         return dp(0, 0, 0)


# Runtime
# 3637 ms
# Beats
# 33.33%
# Memory
# 48.2 MB
# Beats
# 38.10%
# https://leetcode.com/problems/profitable-schemes/editorial/
class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        MOD = 10 ** 9 + 7

        dp = [[[0] * 101 for _ in range(101)] for _ in range(101)]

        for count in range(n+1):
            dp[len(group)][count][minProfit] = 1

        for index in range(len(group)-1, -1, -1):
            for count in range(n+1):
                for p in range(minProfit+1):
                    dp[index][count][p] = dp[index+1][count][p]
                    if count + group[index] <= n:
                        dp[index][count][p] += dp[index+1][count + group[index]][min(minProfit, p + profit[index])]
                        dp[index][count][p] %= MOD

        return dp[0][0][0]


tests = [
    [5, 3, [2,2], [2,3], 2],
    [10, 5, [2,3,5], [6,7,8], 7],
    [100, 5, [2,3,5], [6,7,8], 7],
    [1, 1, [2,2,2,2,2], [1,2,1,1,0], 0],
]

run_functional_tests(Solution().profitableSchemes, tests)
