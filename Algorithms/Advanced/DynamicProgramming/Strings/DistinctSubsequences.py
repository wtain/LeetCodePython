"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3980/
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.



Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag


Constraints:

1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 352 ms, faster than 46.62% of Python3 online submissions for Distinct Subsequences.
# Memory Usage: 58.2 MB, less than 53.38% of Python3 online submissions for Distinct Subsequences.
# https://leetcode.com/problems/distinct-subsequences/discuss/1472589/Python-short-dp-solution-explained
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(n):
            for j in range(m):
                dp[i+1][j+1] = dp[i][j+1]
                if s[i] == t[j]:
                    dp[i+1][j+1] += dp[i][j]
        return dp[-1][-1]


# Runtime: 376 ms, faster than 38.51% of Python3 online submissions for Distinct Subsequences.
# Memory Usage: 91.3 MB, less than 5.24% of Python3 online submissions for Distinct Subsequences.
# https://leetcode.com/problems/distinct-subsequences/discuss/1472589/Python-short-dp-solution-explained
# class Solution:
#     def numDistinct(self, s: str, t: str) -> int:
#         n, m = len(s), len(t)
#
#         @lru_cache(None)
#         def dp(i, j):
#             if i == -1:
#                 return j == -1
#             if j == -1:
#                 return j == -1
#             return dp(i-1, j) + (s[i] == t[j]) * dp(i-1, j-1)
#
#         return dp(n-1, m-1)


tests = [
    ["rabbbit", "rabbit", 3],
    ["babgbag", "bag", 5]
]

run_functional_tests(Solution().numDistinct, tests)