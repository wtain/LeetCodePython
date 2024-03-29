"""
https://leetcode.com/problems/edit-distance/description/

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character


Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


Constraints:

0 <= word1.length, word2.length <= 500
word1 and word2 consist of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 165 ms
# Beats
# 66.43%
# Memory
# 17.5 MB
# Beats
# 55.49%
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2+1) for _ in range(n1+1)]

        for i in range(n1+1):
            dp[i][0] = i
        for j in range(n2+1):
            dp[0][j] = j

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1]+1, dp[i-1][j] + 1, dp[i][j-1]+1)

        return dp[n1][n2]


# WRONG
# class Solution:
#     def minDistance(self, word1: str, word2: str) -> int:
#         n1, n2 = len(word1), len(word2)
#         dp = [[0] * (n2+1) for _ in range(2)]
#
#         for i in range(n1+1):
#             dp[i % 2][0] = i
#         for j in range(n2+1):
#             dp[0][j] = j
#
#         for i in range(1, n1+1):
#             i1 = i % 2
#             i2 = 1 - i1
#             for j in range(1, n2+1):
#                 if word1[i-1] == word2[j-1]:
#                     dp[i1][j] = dp[i2][j-1]
#                 else:
#                     dp[i1][j] = min(dp[i2][j-1]+1, dp[i2][j] + 1, dp[i1][j-1]+1)
#
#         return dp[n1 % 2][n2]


tests = [
    ["horse", "ros", 3],
    ["intention", "execution", 5],
]


run_functional_tests(Solution().minDistance, tests)