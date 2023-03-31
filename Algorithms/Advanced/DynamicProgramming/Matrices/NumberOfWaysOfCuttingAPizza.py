"""
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/description/

Given a rectangular pizza represented as a rows x cols matrix containing the following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts.

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person. If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number, return this modulo 10^9 + 7.



Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1


Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 379 ms
# Beats
# 29.27%
# Memory
# 31.2 MB
# Beats
# 6.23%
# class Solution:
#     def ways(self, pizza: List[str], k: int) -> int:
#         MOD = 10 ** 9 + 7
#         n, m = len(pizza), len(pizza[0])
#
#         # ps = [[0] * m for _ in range(n)]
#         # ps[0][0] = int(pizza[0][0] == 'A')
#         # for j in range(1, m):
#         #     ps[0][j] = ps[0][j-1] + int(pizza[0][j] == 'A')
#         # for i in range(1, n):
#         #     ps[i][0] = ps[i-1][0] + int(pizza[i][0] == 'A')
#         #
#         # for i in range(1, n):
#         #     for j in range(1, m):
#         #         ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + int(pizza[i][j] == 'A')
#
#         # def has_apple(i0, j0, i, j):
#         #     result = ps[i][j]
#         #     if i0 > 0:
#         #         result -= ps[i0-1][j0]
#         #     if j0 > 0:
#         #         result -= ps[i0][j0-1]
#         #     if i0 > 0 and j0 > 0:
#         #         result += ps[i0-1][j0 - 1]
#         #     return int(result > 0)
#
#         @cache
#         def has_apple(i1, j1, i2, j2):
#             for i in range(i1, i2+1):
#                 for j in range(j1, j2+1):
#                     if pizza[i][j] == 'A':
#                         return True
#             return False
#
#         @cache
#         def impl(i0, j0, k):
#             nonlocal MOD, n, m
#             if k == 1:
#                 return 1 if has_apple(i0, j0, n-1, m-1) else 0
#             result = 0
#             for i in range(i0+1, n):
#                 if has_apple(i0, j0, i-1, m-1):
#                     result += impl(i, j0, k-1)
#                     result %= MOD
#             for j in range(j0+1, m):
#                 if has_apple(i0, j0, n-1, j-1):
#                     result += impl(i0, j, k-1)
#                     result %= MOD
#             return result % MOD
#
#         return impl(0, 0, k)


# Runtime
# 440 ms
# Beats
# 22.22%
# Memory
# 16.1 MB
# Beats
# 21.54%
class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        MOD = 10 ** 9 + 7
        n, m = len(pizza), len(pizza[0])

        ps = [[0] * m for _ in range(n)]
        ps[0][0] = int(pizza[0][0] == 'A')
        for j in range(1, m):
            ps[0][j] = ps[0][j-1] + int(pizza[0][j] == 'A')
        for i in range(1, n):
            ps[i][0] = ps[i-1][0] + int(pizza[i][0] == 'A')

        for i in range(1, n):
            for j in range(1, m):
                ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + int(pizza[i][j] == 'A')

        def has_apple(i1, j1, i2, j2):
            result = ps[i2][j2]
            if i1 > 0:
                result -= ps[i1 - 1][j2]
            if j1 > 0:
                result -= ps[i2][j1 - 1]
            if i1 > 0 and j1 > 0:
                result += ps[i1 - 1][j1 - 1]
            return int(result > 0)

        @cache
        def has_apple2(i1, j1, i2, j2):
            for i in range(i1, i2+1):
                for j in range(j1, j2+1):
                    if pizza[i][j] == 'A':
                        return True
            return False

        @cache
        def impl(i0, j0, k):
            nonlocal MOD, n, m
            if k == 1:
                return 1 if has_apple(i0, j0, n-1, m-1) else 0
            result = 0
            for i in range(i0+1, n):
                if has_apple(i0, j0, i-1, m-1):
                    result += impl(i, j0, k-1)
                    result %= MOD
            for j in range(j0+1, m):
                if has_apple(i0, j0, n-1, j-1):
                    result += impl(i0, j, k-1)
                    result %= MOD
            return result % MOD

        return impl(0, 0, k)


"""

A..
AAA
...

        for i1 in range(n):
            for i2 in range(i1, n):
                for j1 in range(m):
                    for j2 in range(j1, m):
                        if has_apple(i1,j1,i2,j2) != has_apple2(i1,j1,i2,j2):
                            print(i1,j1,i2,j2)

"""

tests = [
    [["AAAA"], 2, 3],
    [["A.",".A"], 2, 2],
    [["A..","AAA","..."], 3, 3],
    [["A..","AA.","..."], 3, 1],
    [["A..","A..","..."], 1, 1],
]

run_functional_tests(Solution().ways, tests)
