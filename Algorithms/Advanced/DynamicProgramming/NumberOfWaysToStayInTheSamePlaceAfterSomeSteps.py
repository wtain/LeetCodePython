"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/description/?envType=daily-question&envId=2023-10-15

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8


Constraints:

1 <= steps <= 500
1 <= arrLen <= 106
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 402ms
# Beats 45.00%of users with Python3
# Memory
# Details
# 108.64MB
# Beats 21.11%of users with Python3
# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def dp(steps, pos):
#             if steps == 0:
#                 return 1 if pos == 0 else 0
#             result = dp(steps-1, pos)
#             if pos + 1 < arrLen:
#                 result += dp(steps-1, pos+1)
#             if pos - 1 >= 0:
#                 result += dp(steps-1, pos-1)
#             result %= MOD
#             return result
#
#         return dp(steps, 0)


# MEM EXCEEDED
# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#
#         MOD = 10 ** 9 + 7
#         dp = [[0] * arrLen for _ in range(steps+1)]
#         dp[0][0] = 1
#
#         for s in range(1, steps+1):
#             for pos in range(arrLen):
#                 dp[s][pos] = dp[s-1][pos]
#                 if pos + 1 < arrLen:
#                     dp[s][pos] += dp[s - 1][pos+1]
#                 if pos - 1 >= 0:
#                     dp[s][pos] += dp[s - 1][pos-1]
#                 dp[s][pos] %= MOD
#
#         return dp[steps][0]


# Runtime
# Details
# 425ms
# Beats 37.22%of users with Python3
# Memory
# Details
# 22.04MB
# Beats 68.33%of users with Python3
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/?envType=daily-question&envId=2023-10-15
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        arrLen = min(arrLen, steps)

        MOD = 10 ** 9 + 7
        dp = [[0] * arrLen for _ in range(steps+1)]
        dp[0][0] = 1

        for s in range(1, steps+1):
            for pos in range(arrLen):
                dp[s][pos] = dp[s-1][pos]
                if pos + 1 < arrLen:
                    dp[s][pos] += dp[s - 1][pos+1]
                if pos - 1 >= 0:
                    dp[s][pos] += dp[s - 1][pos-1]
                dp[s][pos] %= MOD

        return dp[steps][0]


# TLE
# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#
#         MOD = 10 ** 9 + 7
#         prev_dp = [0] * arrLen
#         prev_dp[0] = 1
#
#         for s in range(1, steps+1):
#             dp = [0] * arrLen
#             for pos in range(arrLen):
#                 dp[pos] = prev_dp[pos]
#                 if pos + 1 < arrLen:
#                     dp[pos] += prev_dp[pos+1]
#                 if pos - 1 >= 0:
#                     dp[pos] += prev_dp[pos-1]
#                 dp[pos] %= MOD
#             prev_dp = dp
#
#         return dp[0]


# Runtime
# Details
# 316ms
# Beats 68.89%of users with Python3
# Memory
# Details
# 16.30MB
# Beats 92.78%of users with Python3
# https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/editorial/?envType=daily-question&envId=2023-10-15
# class Solution:
#     def numWays(self, steps: int, arrLen: int) -> int:
#
#         arrLen = min(arrLen, steps)
#
#         MOD = 10 ** 9 + 7
#         prev_dp = [0] * arrLen
#         prev_dp[0] = 1
#
#         for s in range(1, steps+1):
#             dp = [0] * arrLen
#             for pos in range(arrLen):
#                 dp[pos] = prev_dp[pos]
#                 if pos + 1 < arrLen:
#                     dp[pos] += prev_dp[pos+1]
#                 if pos - 1 >= 0:
#                     dp[pos] += prev_dp[pos-1]
#                 dp[pos] %= MOD
#             prev_dp = dp
#
#         return dp[0]


tests = [
    [3, 2, 4],
    [2, 4, 2],
    [4, 2, 8],
]

run_functional_tests(Solution().numWays, tests)
