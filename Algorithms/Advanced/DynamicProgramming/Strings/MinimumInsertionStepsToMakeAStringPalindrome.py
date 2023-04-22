"""
https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.



Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.
Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".
Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".


Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1888 ms
# Beats
# 5.8%
# Memory
# 358.6 MB
# Beats
# 5.68%
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/editorial/
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         n = len(s)
#         s_reverse = "".join(reversed(s))
#
#         @cache
#         def lcs(m, n):
#             if m == 0 or n == 0:
#                 return 0
#             if s[m-1] == s_reverse[n-1]:
#                 return 1 + lcs(m-1, n-1)
#             return max(lcs(m-1, n), lcs(m, n-1))
#
#         return n - lcs(n, n)

# Runtime
# 1355 ms
# Beats
# 19.7%
# Memory
# 15.9 MB
# Beats
# 85.80%
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/editorial/
# class Solution:
#     def minInsertions(self, s: str) -> int:
#         n = len(s)
#         s_reverse = "".join(reversed(s))
#
#         def lcs(m, n):
#             dp = [[0] * (n+1) for _ in range(m+1)]
#             for i in range(m+1):
#                 for j in range(n+1):
#                     if i == 0 or j == 0:
#                         dp[i][j] = 0
#                     elif s[i-1] == s_reverse[j-1]:
#                         dp[i][j] = 1 + dp[i-1][j-1]
#                     else:
#                         dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#             return dp[-1][-1]
#
#         return n - lcs(n, n)


# Runtime
# 1152 ms
# Beats
# 48.48%
# Memory
# 14 MB
# Beats
# 93.51%
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        s_reverse = "".join(reversed(s))

        def lcs(m, n):
            dp = [0] * (n+1)
            dp_prev = [0] * (n+1)
            for i in range(m+1):
                for j in range(n+1):
                    if i == 0 or j == 0:
                        dp[j] = 0
                    elif s[i-1] == s_reverse[j-1]:
                        dp[j] = 1 + dp_prev[j-1]
                    else:
                        dp[j] = max(dp_prev[j], dp[j-1])
                dp_prev = dp.copy()

            return dp[-1]

        return n - lcs(n, n)


tests = [
    ["zzazz", 0],
    ["mbadm", 2],
    ["leetcode", 5],
]

run_functional_tests(Solution().minInsertions, tests)
