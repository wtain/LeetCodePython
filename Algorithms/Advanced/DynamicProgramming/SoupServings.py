"""
https://leetcode.com/problems/soup-servings/

There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.



Example 1:

Input: n = 50
Output: 0.62500
Explanation: If we choose the first two operations, A will become empty first.
For the third operation, A and B will become empty at the same time.
For the fourth operation, B will become empty first.
So the total probability of A becoming empty first plus half the probability that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) = 0.625.
Example 2:

Input: n = 100
Output: 0.71875


Constraints:

0 <= n <= 109
"""
import sys
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def soupServings(self, n: int) -> float:
#         to_visit = [(n, n, 1.0)]
#         result = 0.0
#         while to_visit:
#             a, b, probability = to_visit.pop()
#             if a > 0 and b > 0:
#                 to_visit.append((max(a - 100, 0), b, 0.25 * probability))
#                 to_visit.append((max(a-75, 0), max(b-25, 0), 0.25*probability))
#                 to_visit.append((max(a-50, 0), max(b-50, 0), 0.25*probability))
#                 to_visit.append((max(a-25, 0), max(b-75, 0), 0.25*probability))
#             if a == 0 and b > 0:
#                 result += probability
#             elif a == 0 and b == 0:
#                 result += 0.5*probability
#         return result


# RECURSION TOO DEEP
# class Solution:
#     def soupServings(self, n: int) -> float:
#
#         @lru_cache(None)
#         def dp(a: int, b: int) -> float:
#             if a == 0 and b > 0:
#                 return 1.0
#             elif a == 0 and b == 0:
#                 return 0.5
#             elif a > 0 and b > 0:
#                 return 0.25 * dp(max(a - 100, 0), b) + \
#                        0.25 * dp(max(a-75, 0), max(b-25, 0)) + \
#                        0.25 * dp(max(a-50, 0), max(b-50, 0)) + \
#                        0.25 * dp(max(a-25, 0), max(b-75, 0))
#             return 0
#
#         return dp(n, n)


# WRONG
# class Solution:
#     def soupServings(self, n: int) -> float:
#
#         sys.setrecursionlimit(10010)
#
#         level = 0
#
#         @lru_cache(None)
#         def dp(a: int, b: int) -> float:
#             nonlocal level
#             if a == 0 and b > 0:
#                 return 1.0
#             elif a == 0 and b == 0:
#                 return 0.5
#             elif a > 0 and b > 0:
#                 if level == 5000:
#                     return 0.0
#                 level += 1
#                 result = 0.25 * dp(max(a - 100, 0), b) + \
#                          0.25 * dp(max(a-75, 0), max(b-25, 0)) + \
#                          0.25 * dp(max(a-50, 0), max(b-50, 0)) + \
#                          0.25 * dp(max(a-25, 0), max(b-75, 0))
#                 level -= 1
#                 return result
#             return 0
#
#         return dp(n, n)


# class Solution:
#     def soupServings(self, n: int) -> float:
#         if n > 4800:
#             return 1.0
#         to_visit = [(n, n, 1.0)]
#         result = 0.0
#         while to_visit:
#             a, b, probability = to_visit.pop()
#             if a > 0 and b > 0:
#                 to_visit.append((max(a - 100, 0), b, 0.25 * probability))
#                 to_visit.append((max(a-75, 0), max(b-25, 0), 0.25*probability))
#                 to_visit.append((max(a-50, 0), max(b-50, 0), 0.25*probability))
#                 to_visit.append((max(a-25, 0), max(b-75, 0), 0.25*probability))
#             if a == 0 and b > 0:
#                 result += probability
#             elif a == 0 and b == 0:
#                 result += 0.5*probability
#         return result


# Runtime
# 41 ms
# Beats
# 84.15%
# Memory
# 14.6 MB
# Beats
# 62.19%
# see https://leetcode.com/problems/soup-servings/solutions/195582/a-mathematical-analysis-of-the-soup-servings-problem/
class Solution:
    def soupServings(self, n: int) -> float:

        if n > 4800:
            return 1.0

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a == 0 and b > 0:
                return 1.0
            elif a == 0 and b == 0:
                return 0.5
            elif a > 0 and b > 0:
                return 0.25 * dp(max(a - 100, 0), b) + \
                       0.25 * dp(max(a-75, 0), max(b-25, 0)) + \
                       0.25 * dp(max(a-50, 0), max(b-50, 0)) + \
                       0.25 * dp(max(a-25, 0), max(b-75, 0))
            return 0

        return dp(n, n)


tests = [
    [50, 0.62500],
    [100, 0.71875],
    [800, 0.96162],
    [660295675, 1.0]
]

run_functional_tests(Solution().soupServings, tests)
