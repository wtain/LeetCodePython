"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/

You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.
Example 2:

Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.


Constraints:

1 <= n, k <= 30
1 <= target <= 1000
"""
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         @lru_cache(None)
#         def dp(n: int, target: int) -> int:
#             if target < 0:
#                 return 0
#             if n == 0:
#                 if target == 0:
#                     return 1
#                 else:
#                     return 0
#             if n == 1:
#                 if target <= k:
#                     return 1
#                 else:
#                     return 0
#             return sum(dp(n-1, target-i) for i in range(1, k+1)) % MOD
#
#         return dp(n, target)


# Runtime
# 549 ms
# Beats
# 71.67%
# Memory
# 14.5 MB
# Beats
# 70.32%
# class Solution:
#     def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         # DP (n, target)
#         dp = [[0] * (target+1+k+1+1) for _ in range(n+1)]
#         for i in range(1, k+1):
#             dp[1][i] = 1
#
#         for i in range(1, n):
#             for t in range(0, target+1):
#                 if dp[i][t] == 0:
#                     continue
#                 for j in range(1, k+1):
#                     dp[i+1][t+j] += dp[i][t]
#                     dp[i + 1][t + j] %= MOD
#
#         return dp[n][target]


# Runtime
# 553 ms
# Beats
# 71.49%
# Memory
# 13.8 MB
# Beats
# 98.65%
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        # DP (n, target)
        dp = [0] * (target+k+1)
        for i in range(1, k+1):
            dp[i] = 1

        for i in range(n-1):
            next_dp = [0] * (target+k+1)
            for t in range(0, target+1):
                if dp[t] == 0:
                    continue
                for j in range(1, k+1):
                    if t+j > target:
                        break
                    next_dp[t+j] += dp[t]
                    next_dp[t + j] %= MOD
            dp = next_dp

        return dp[target]


tests = [
    [1, 6, 3, 1],
    [2, 6, 7, 6],
    [30, 30, 500, 222616187]
]

run_functional_tests(Solution().numRollsToTarget, tests)
