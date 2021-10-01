"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.



Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.


Constraints:

1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 360 ms, faster than 93.85% of Python3 online submissions for Longest Common Subsequence.
# Memory Usage: 14.4 MB, less than 91.15% of Python3 online submissions for Longest Common Subsequence.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        if n2 > n1:
            n1, text1, n2, text2 = n2, text2, n1, text1
        dp = [[0] * (n2+1) for _ in range(2)]
        for i in range(n1):
            i1 = i % 2
            i2 = 1 - i1
            for j in range(n2):
                if text1[i] == text2[j]:
                    dp[i2][j + 1] = dp[i1][j] + 1
                else:
                    dp[i2][j + 1] = max(dp[i2][j], dp[i1][j+1])
        return dp[n1 % 2][n2]


tests = [
    ["abcde", "ace", 3],
    ["abc", "abc", 3],
    ["abc", "def", 0]
]

run_functional_tests(Solution().longestCommonSubsequence, tests)