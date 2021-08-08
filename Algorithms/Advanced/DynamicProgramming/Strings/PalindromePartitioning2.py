"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3872/
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.



Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1


Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.
"""
from Common.ObjectTestingUtils import run_functional_tests


# TLE - O(N^3)
# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         dp = [[n-1] * n for _ in range(n)]
#         p = [[False] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 0
#             p[i][i] = True
#             if i+1 < n:
#                 dp[i][i+1] = 1 if s[i] != s[i+1] else 0
#                 p[i][i+1] = s[i] == s[i+1]
#
#         for l in range(3, n+1):
#             for i1 in range(n-l):
#                 i2 = i1 + l - 1
#                 if p[i1+1][i2-1] and s[i1] == s[i2]:
#                     p[i1][i2] = True
#                     dp[i1][i2] = 0
#
#         for l in range(3, n+1):
#             for i1 in range(n-l+1):
#                 i2 = i1 + l - 1
#                 for k in range(1, l-1):
#                     c = dp[i1][k] + dp[k+1][i2] + 1
#                     dp[i1][i2] = min(dp[i1][i2], c)
#
#         return dp[0][n-1]


# RECURSION DEPTH ERROR
# class Solution:
#     def minCut(self, s: str) -> int:
#         n = len(s)
#         p = [[False] * n for _ in range(n)]
#         for i in range(n):
#             p[i][i] = True
#             if i+1 < n:
#                 p[i][i+1] = s[i] == s[i+1]
#
#         for l in range(3, n+1):
#             for i1 in range(n-l):
#                 i2 = i1 + l - 1
#                 if p[i1+1][i2-1] and s[i1] == s[i2]:
#                     p[i1][i2] = True
#
#         min_part = n-1
#
#         def dfs(i: int, current: int):
#             nonlocal min_part
#             if i == n:
#                 min_part = min(min_part, current)
#             else:
#                 for j in range(i, n):
#                     if p[i][j]:
#                         dfs(j + 1, current+1)
#
#         dfs(0, 0)
#
#         return min_part


# Runtime: 788 ms, faster than 67.70% of Python3 online submissions for Palindrome Partitioning II.
# Memory Usage: 42.3 MB, less than 52.06% of Python3 online submissions for Palindrome Partitioning II.
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        p = [[False] * n for _ in range(n)]
        for i in range(n):
            p[i][i] = True
            if i+1 < n:
                p[i][i+1] = s[i] == s[i+1]

        for l in range(3, n+1):
            for i1 in range(n-l+1):
                i2 = i1 + l - 1
                if p[i1+1][i2-1] and s[i1] == s[i2]:
                    p[i1][i2] = True

        dp = [n-1] * n
        dp[0] = 0
        for i2 in range(1, n):
            if p[0][i2]:
                dp[i2] = 0
                continue
            dp[i2] = dp[i2-1] + 1
            for i1 in range(1, i2):
                if p[i1][i2]:
                    c = dp[i1-1] + 1
                    dp[i2] = min(dp[i2], c)

        return dp[n-1]


tests = [
    ["efe", 0],
    ["abcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmriocbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmriocbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmriocbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmriocbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmriocbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasbxascbascbascdkjdgjdfkvlmrioabcabasgrs", 1889],
    ["aab", 1],
    ["a", 0],
    ["ab", 1]
]

run_functional_tests(Solution().minCut, tests)