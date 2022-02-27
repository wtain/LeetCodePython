"""
https://leetcode.com/problems/strange-printer/
There is a strange printer with the following two special requirements:

The printer can only print a sequence of the same character each time.
At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

Example 1:
Input: "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".
Example 2:
Input: "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
Hint: Length of the given string will not exceed 100.
"""


## WRONG
# class Solution:
#     def strangePrinter(self, s: str) -> int:
#
#         def compress(s: str) -> str:
#             n = len(s)
#             if not n:
#                 return ""
#             t = s[0]
#             for i in range(1, n):
#                 if t[-1] != s[i]:
#                     t += s[i]
#             return t
#
#         t = compress(s)
#         m = len(t)
#         dp = [0] * (m+1)
#         j0 = 1
#         for j in range(0, m):
#             if j > j0 and t[j-2] == t[j]:
#                 dp[j+1] = dp[j]
#                 j0 = j+1
#             else:
#                 dp[j+1] = dp[j] + 1
#         return dp[m]


## WRONG
# class Solution:
#     def strangePrinter(self, s: str) -> int:
#
#         def compress(s: str) -> str:
#             n = len(s)
#             if not n:
#                 return ""
#             t = s[0]
#             for i in range(1, n):
#                 if t[-1] != s[i]:
#                     t += s[i]
#             return t
#
#         t = compress(s)
#         m = len(t)
#         if not m:
#             return 0
#         dp = [[0] * m for i in range(m)]
#
#         for i in range(m):
#             dp[i][i] = 1
#             if i > 0:
#                 if t[i - 1] == t[i]:
#                     dp[i - 1][i] = 1
#                 else:
#                     dp[i - 1][i] = 2
#
#         for l in range(3, m+1):
#             for i in range(m-l+1):
#                 j = i + l - 1
#                 if t[i] == t[j]:
#                     dp[i][j] = dp[i + 1][j - 1] + 1
#                 else:
#                     dp[i][j] = dp[i + 1][j - 1] + 2
#
#         return dp[0][m-1]

# Runtime: 384 ms, faster than 83.63% of Python3 online submissions for Strange Printer.
# Memory Usage: 17.6 MB, less than 18.71% of Python3 online submissions for Strange Printer.
# class Solution:
#     def strangePrinter(self, s: str) -> int:
#
#         def compress(s: str) -> str:
#             n = len(s)
#             if not n:
#                 return ""
#             t = s[0]
#             for i in range(1, n):
#                 if t[-1] != s[i]:
#                     t += s[i]
#             return t
#
#         t = compress(s)
#         m = len(t)
#         if not m:
#             return 0
#
#         memo = {}
#
#         def dp(i: int, j: int) -> int:
#             nonlocal memo
#             if i > j:
#                 return 0
#             if (i, j) not in memo:
#                 res = dp(i+1, j) + 1
#                 for k in range(i+1, j+1):
#                     if t[k] == t[i]:
#                         res = min(res, dp(i, k-1) + dp(k+1, j))
#                 memo[i, j] = res
#             return memo[i, j]
#
#         return dp(0, m-1)

# Runtime: 1212 ms, faster than 18.13% of Python3 online submissions for Strange Printer.
# Memory Usage: 14.5 MB, less than 81.29% of Python3 online submissions for Strange Printer.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def strangePrinter(self, s: str) -> int:

        def compress(s: str) -> str:
            n = len(s)
            if not n:
                return ""
            t = s[0]
            for i in range(1, n):
                if t[-1] != s[i]:
                    t += s[i]
            return t

        t = compress(s)
        m = len(t)
        if not m:
            return 0

        dp = [[0] * m for i in range(m)]

        for i in range(m):
            dp[i][i] = 1
            if i > 0:
                if t[i - 1] == t[i]:
                    dp[i - 1][i] = 1
                else:
                    dp[i - 1][i] = 2

        for l in range(3, m+1):
            for i in range(m-l+1):
                res = 100
                v = 1 if t[i] == t[i+l-1] else 0
                for j in range(i+l-1, i, -1):
                    res = min(res, dp[i][j-1] + dp[j][i+l-1] - v)
                dp[i][i+l-1] = res

        return dp[0][m-1]


tests = [

    ["aaabbb", 2],
    ["aba", 2],

    ["", 0],
    ["aaabaaabaaaa", 3],
    ["abab", 3],

    ["ababcabab", 6]
]

run_functional_tests(Solution().strangePrinter, tests)
