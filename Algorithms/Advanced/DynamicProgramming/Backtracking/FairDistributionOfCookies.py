"""
https://leetcode.com/problems/fair-distribution-of-cookies/

You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.



Example 1:

Input: cookies = [8,15,10,20,8], k = 2
Output: 31
Explanation: One optimal distribution is [8,15,8] and [10,20]
- The 1st child receives [8,15,8] which has a total of 8 + 15 + 8 = 31 cookies.
- The 2nd child receives [10,20] which has a total of 10 + 20 = 30 cookies.
The unfairness of the distribution is max(31,30) = 31.
It can be shown that there is no distribution with an unfairness less than 31.
Example 2:

Input: cookies = [6,1,3,2,2,4,1,2], k = 3
Output: 7
Explanation: One optimal distribution is [6,1], [3,2,2], and [4,1,2]
- The 1st child receives [6,1] which has a total of 6 + 1 = 7 cookies.
- The 2nd child receives [3,2,2] which has a total of 3 + 2 + 2 = 7 cookies.
- The 3rd child receives [4,1,2] which has a total of 4 + 1 + 2 = 7 cookies.
The unfairness of the distribution is max(7,7,7) = 7.
It can be shown that there is no distribution with an unfairness less than 7.


Constraints:

2 <= cookies.length <= 8
1 <= cookies[i] <= 105
2 <= k <= cookies.length
"""
import math
from math import inf
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def distributeCookies(self, cookies: List[int], k: int) -> int:
#         n = len(cookies)
#         result = float('Inf')
#
#         def impl(i: int, sums: List[int], unfairness: int):
#             nonlocal result, k, n
#             if i == n:
#                 result = min(result, unfairness)
#                 return
#             for j in range(k):
#                 sums[j] += cookies[i]
#                 impl(i+1, sums, max(unfairness, sums[j]))
#                 sums[j] -= cookies[i]
#
#         impl(0, [0] * k, 0)
#
#         return result


# Runtime
# 873 ms
# Beats
# 45.47%
# Memory
# 13.9 MB
# Beats
# 67.82%
# class Solution:
#     def distributeCookies(self, cookies: List[int], k: int) -> int:
#         n = len(cookies)
#         result = math.inf
#         cookies.sort(reverse=True)
#
#         def impl(i: int, sums: List[int]):
#             nonlocal result, k, n
#             if i == n:
#                 result = min(result, max(sums))
#                 return
#             for j in range(k):
#                 if sums[j] + cookies[i] < result:
#                     sums[j] += cookies[i]
#                     impl(i+1, sums)
#                     sums[j] -= cookies[i]
#
#         impl(0, [0] * k)
#
#         return result


# Runtime
# 163 ms
# Beats
# 53.37%
# Memory
# 13.9 MB
# Beats
# 67.82%
# https://leetcode.com/problems/fair-distribution-of-cookies/solutions/2141573/dp-submask-enumeration-most-optimal-solution-100-faster-c/
class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        M = (1 << n)

        dp = [[math.inf] * M for _ in range(k+1)]
        sums = [0] * M

        for mask in range(M):
            total = 0
            for i in range(n):
                if mask & (1 << i):
                    total += cookies[i]
            sums[mask] = total

        dp[0][0] = 0
        for person in range(1, k+1):
            for mask in range(M):
                submask = mask
                while submask:
                    dp[person][mask] = min(dp[person][mask], max(sums[submask], dp[person-1][mask ^ submask]))
                    submask = (submask - 1) & mask

        return dp[k][-1]


# mask = 00000000b
# code = code1 * k + ci
# mask x code => result


# code=0, mask=00000, v=0
# 	code=1, mask=10000, v=8
#
# DP([c1,c2,...cn], k)  =



tests = [
    [[8,15,10,20,8], 2, 31],
    [[6,1,3,2,2,4,1,2], 3, 7],
    [[64,32,16,8,4,2,1,1000], 8, 1000],
]

run_functional_tests(Solution().distributeCookies, tests)
