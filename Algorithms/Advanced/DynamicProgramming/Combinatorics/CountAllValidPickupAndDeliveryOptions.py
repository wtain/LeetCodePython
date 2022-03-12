"""
https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/

Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
Example 2:

Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
Example 3:

Input: n = 3
Output: 90


Constraints:

1 <= n <= 500
"""
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
# #     def countOrders(self, n: int) -> int:
# #
# #         fact = [1] * 501
# #         for i in range(1, 501):
# #             fact[i] = fact[i-1] * i
# #
# #         MOD = 10 ** 9 + 7
# #
# #         def mixed(m: int) -> int:
# #             return fact[m] ** 2
# #
# #         dp = [0] * (n+1)
# #         dp[1] = 1
# #         for i in range(2, n+1):
# #             pass
# #
# #         return dp[n] % MOD


# TLE
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/
# class Solution:
#     def countOrders(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         @lru_cache
#         def total_ways(unpicked, undelivered):
#             if not unpicked and not undelivered:
#                 return 1
#             if unpicked < 0 or undelivered < 0 or undelivered < unpicked:
#                 return 0
#             res = unpicked * total_ways(unpicked-1, undelivered) % MOD
#             res += (undelivered - unpicked) * total_ways(unpicked, undelivered-1) % MOD
#             res %= MOD
#             return res
#
#         return total_ways(n, n)


# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/
# Runtime: 728 ms, faster than 21.02% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 19.8 MB, less than 19.03% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# class Solution:
#     def countOrders(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[0] * (n+1) for _ in range(n+1)]
#
#         for unpicked in range(n+1):
#             for undelivered in range(unpicked, n+1):
#                 if not unpicked and not undelivered:
#                     dp[unpicked][undelivered] = 1
#                     continue
#                 if unpicked > 0:
#                     dp[unpicked][undelivered] += unpicked * dp[unpicked-1][undelivered]
#                     dp[unpicked][undelivered] %= MOD
#                 if undelivered > unpicked:
#                     dp[unpicked][undelivered] += (undelivered-unpicked) * dp[unpicked][undelivered-1]
#                     dp[unpicked][undelivered] %= MOD
#         return dp[n][n]


# Runtime: 63 ms, faster than 34.37% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 13.9 MB, less than 71.02% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/
# class Solution:
#     def countOrders(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         result = 1
#         for i in range(1, n+1):
#             result *= i
#             result *= (2*i-1)
#             result %= MOD
#         return result


# Runtime: 28 ms, faster than 98.01% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# Memory Usage: 13.9 MB, less than 88.07% of Python3 online submissions for Count All Valid Pickup and Delivery Options.
# https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/solution/
class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        result = 1
        for i in range(1, 2*n+1):
            result *= i
            if not i % 2:
                result //= 2
            result %= MOD
        return result


tests = [
    [1, 1],
    [2, 6],
    [3, 90]
]

run_functional_tests(Solution().countOrders, tests)
