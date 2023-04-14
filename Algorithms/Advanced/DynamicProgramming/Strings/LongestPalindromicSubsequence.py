"""
https://leetcode.com/problems/longest-palindromic-subsequence/description/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".
Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".


Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1751 ms
# Beats
# 47.46%
# Memory
# 30.5 MB
# Beats
# 71.90%
# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:
#         n = len(s)
#         if not n:
#             return 0
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 1
#         for l in range(2, n+1):
#             for i in range(n-l+1):
#                 j = i + l - 1
#                 if l == 2 and s[i] == s[j]:
#                     dp[i][j] = 2
#                 elif s[i] == s[j]:
#                     dp[i][j] = 2 + dp[i+1][j-1]
#                 else:
#                     dp[i][j] = max(dp[i+1][j], dp[i][j-1])
#         return dp[0][-1]

# Runtime
# 1665 ms
# Beats
# 50.18%
# Memory
# 30.5 MB
# Beats
# 71.90%
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]


tests = [
    ["bbbab", 4],
    ["cbbd", 2],
]

run_functional_tests(Solution().longestPalindromeSubseq, tests)
