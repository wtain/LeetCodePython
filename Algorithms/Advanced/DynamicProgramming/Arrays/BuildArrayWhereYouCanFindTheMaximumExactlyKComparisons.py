"""
https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/description/?envType=daily-question&envId=2023-10-07

You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.



Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]


Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 819ms
# Beats 61.95%of users with Python3
# Memory
# Details
# 43.59MB
# Beats 9.73%of users with Python3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/editorial/?envType=daily-question&envId=2023-10-07
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def dp(i, max_so_far, remain):
#             if i == n:
#                 return 1 if remain == 0 else 0
#
#             res = (max_so_far * dp(i+1, max_so_far, remain)) % MOD
#             for num in range(max_so_far+1, m+1):
#                 res = (res + dp(i+1, num, remain - 1)) % MOD
#             return res
#
#         return dp(0, 0, k)


# Runtime
# Details
# 1011ms
# Beats 33.63%of users with Python3
# Memory
# Details
# 20.35MB
# Beats 75.22%of users with Python3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/editorial/?envType=daily-question&envId=2023-10-07
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         dp = [[[0] * (k+1) for _ in range(m+1)] for __ in range(n+1)]
#         MOD = 10 ** 9 + 7
#
#         for num in range(len(dp[0])):
#             dp[n][num][0] = 1
#
#         for i in range(n-1, -1, -1):
#             for max_so_far in range(m, -1, -1):
#                 for remain in range(k+1):
#                     ans = (max_so_far * dp[i+1][max_so_far][remain]) % MOD
#
#                     if remain > 0:
#                         for num in range(max_so_far+1, m+1):
#                             ans = (ans + dp[i+1][num][remain-1]) % MOD
#
#                     dp[i][max_so_far][remain] = ans
#         return dp[0][0][k]


# Runtime
# Details
# 791ms
# Beats 65.49%of users with Python3
# Memory
# Details
# 16.50MB
# Beats 95.58%of users with Python3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/editorial/?envType=daily-question&envId=2023-10-07
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         dp = [[0] * (k+1) for _ in range(m+1)]
#         prev_dp = [[0] * (k+1) for _ in range(m+1)]
#         MOD = 10 ** 9 + 7
#
#         for num in range(len(dp)):
#             prev_dp[num][0] = 1
#
#         for i in range(n-1, -1, -1):
#             dp = [[0] * (k + 1) for _ in range(m + 1)]
#             for max_so_far in range(m, -1, -1):
#                 for remain in range(k+1):
#                     ans = (max_so_far * prev_dp[max_so_far][remain]) % MOD
#
#                     if remain > 0:
#                         for num in range(max_so_far+1, m+1):
#                             ans = (ans + prev_dp[num][remain-1]) % MOD
#
#                     dp[max_so_far][remain] = ans
#             prev_dp = dp
#         return dp[0][k]


# Runtime
# Details
# 956ms
# Beats 46.90%of users with Python3
# Memory
# Details
# 43.01MB
# Beats 16.81%of users with Python3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/editorial/?envType=daily-question&envId=2023-10-07
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def dp(i, max_num, cost):
#             if i == 1:
#                 return cost == 1
#
#             ans = (max_num * dp(i-1, max_num, cost)) % MOD
#             for num in range(1, max_num):
#                 ans = (ans + dp(i-1, num, cost-1)) % MOD
#             return ans
#
#         ans = 0
#
#         for num in range(1, m+1):
#             ans = (ans + dp(n, num, k)) % MOD
#
#         return ans


# Runtime
# Details
# 986ms
# Beats 39.82%of users with Python3
# Memory
# Details
# 20.33MB
# Beats 75.22%of users with Python3
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[[0] * (k+1) for _ in range(m+1)] for __ in range(n+1)]
#
#         for num in range(1, m+1):
#             dp[1][num][1] = 1
#
#         for i in range(1, n+1):
#             for max_num in range(1, m+1):
#                 for cost in range(1, k+1):
#                     ans = (max_num * dp[i - 1][max_num][cost]) % MOD
#                     for num in range(1, max_num):
#                         ans = (ans + dp[i - 1][num][cost - 1]) % MOD
#                     dp[i][max_num][cost] += ans
#                     dp[i][max_num][cost] %= MOD
#
#         ans = 0
#         for num in range(1, m+1):
#             ans = (ans + dp[n][num][k]) % MOD
#
#         return ans


# Runtime
# Details
# 205ms
# Beats 80.53%of users with Python3
# Memory
# Details
# 24.19MB
# Beats 55.75%of users with Python3
# class Solution:
#     def numOfArrays(self, n: int, m: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[[0] * (k+1) for _ in range(m+1)] for __ in range(n+1)]
#         prefix = [[[0] * (k+1) for _ in range(m+1)] for __ in range(n+1)]
#         for num in range(1, m+1):
#             dp[1][num][1] = 1
#             prefix[1][num][1] = prefix[1][num - 1][1] + 1
#
#         for i in range(1, n+1):
#             for max_num in range(1, m+1):
#                 for cost in range(1, k+1):
#                     ans = (max_num * dp[i - 1][max_num][cost]) % MOD
#                     ans = (ans + prefix[i - 1][max_num-1][cost - 1]) % MOD
#                     dp[i][max_num][cost] += ans
#                     dp[i][max_num][cost] %= MOD
#                     prefix[i][max_num][cost] = (prefix[i][max_num-1][cost] + dp[i][max_num][cost]) % MOD
#
#         return prefix[n][m][k]


# Runtime
# Details
# 161ms
# Beats 86.73%of users with Python3
# Memory
# Details
# 16.57MB
# Beats 92.92%of users with Python3
# https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/editorial/?envType=daily-question&envId=2023-10-07
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prev_dp = [[0] * (k + 1) for _ in range(m + 1)]
        prev_prefix = [[0] * (k + 1) for _ in range(m + 1)]

        for num in range(1, m+1):
            dp[num][1] = 1

        for i in range(1, n+1):
            if i > 1:
                dp = [[0] * (k + 1) for _ in range(m + 1)]
            prefix = [[0] * (k + 1) for _ in range(m + 1)]
            for max_num in range(1, m+1):
                for cost in range(1, k+1):
                    ans = (max_num * prev_dp[max_num][cost]) % MOD
                    ans = (ans + prev_prefix[max_num-1][cost - 1]) % MOD
                    dp[max_num][cost] += ans
                    dp[max_num][cost] %= MOD
                    prefix[max_num][cost] = (prefix[max_num-1][cost] + dp[max_num][cost]) % MOD
            prev_dp = dp
            prev_prefix = prefix

        return prefix[m][k]


tests = [
    [2, 3, 1, 6],
    [5, 2, 3, 0],
    [9, 1, 1, 1],
    [50, 100, 25, 34549172],
]

run_functional_tests(Solution().numOfArrays, tests)
