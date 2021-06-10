"""
https://leetcode.com/problems/interleaving-string/
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3765/

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         if len(s1) + len(s2) != len(s3):
#             return False
#
#         @lru_cache
#         def solve(i1: int, i2: int, res: str) -> bool:
#             nonlocal s1, s2, s3
#             if res == s3 and i1 == len(s1) and i2 == len(s2):
#                 return True
#             if i1 < len(s1):
#                 if solve(i1+1, i2, res+s1[i1]):
#                     return True
#             if i2 < len(s2):
#                 if solve(i1, i2+1, res+s2[i2]):
#                     return True
#             return False
#
#         return solve(0, 0, "")


# Runtime: 44 ms, faster than 34.60% of Python3 online submissions for Interleaving String.
# Memory Usage: 14.4 MB, less than 73.39% of Python3 online submissions for Interleaving String.
# class Solution:
#     def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
#         n1, n2 = len(s1), len(s2)
#         if n1 + n2 != len(s3):
#             return False
#         dp = [[False] * (n2+1) for _ in range(n1+1)]
#         for i in range(n1+1):
#             for j in range(n2+1):
#                 if i == 0 and j == 0:
#                     dp[i][j] = True
#                 elif i == 0:
#                     dp[i][j] = dp[i][j-1] and s2[j-1] == s3[i+j-1]
#                 elif j == 0:
#                     dp[i][j] = dp[i-1][j] and s1[i - 1] == s3[i + j - 1]
#                 else:
#                     dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1] or \
#                                dp[i-1][j] and s1[i - 1] == s3[i + j - 1]
#         return dp[n1][n2]


# Runtime: 40 ms, faster than 45.56% of Python3 online submissions for Interleaving String.
# Memory Usage: 13.9 MB, less than 99.78% of Python3 online submissions for Interleaving String.
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 + n2 != len(s3):
            return False
        dp = [False] * (n2+1)
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0:
                    dp[j] = True
                elif i == 0:
                    dp[j] = dp[j-1] and s2[j-1] == s3[i+j-1]
                elif j == 0:
                    dp[j] = dp[j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[j] = dp[j - 1] and s2[j - 1] == s3[i + j - 1] or \
                            dp[j] and s1[i - 1] == s3[i + j - 1]
        return dp[n2]


tests = [
    ["aabcc", "dbbca", "aadbbcbcac", True],
    ["aabcc", "dbbca", "aadbbbaccc", False],
    ["", "", "", True],
    ["cabbcaaacacbac", "acabaabacabcca", "cacabaabacaabccbabcaaacacbac", True],
    ["bbaabacacbabcbaa", "abccccbaccaca", "bbccccababaaccacaccbaababcbaa", False]
]

run_functional_tests(Solution().isInterleave, tests)