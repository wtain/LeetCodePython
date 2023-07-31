"""
https://leetcode.com/problems/minimum-ascii-delete-sum-for-two-strings/

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.



Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.


Constraints:

1 <= s1.length, s2.length <= 1000
s1 and s2 consist of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 431ms
# Beats 95.80%of users with Python3
# Memory
# Details
# 21.02mb
# Beats 47.05%of users with Python3
# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         l1, l2 = len(s1), len(s2)
#         dp = [[0] * (l2+1) for _ in range(l1+1)]
#         for i in range(l1):
#             dp[i+1][0] = dp[i][0] + ord(s1[i])
#         for j in range(l2):
#             dp[0][j+1] = dp[0][j] + ord(s2[j])
#         for i in range(l1):
#             for j in range(l2):
#                 if s1[i] == s2[j]:
#                     dp[i+1][j+1] = dp[i][j]
#                 else:
#                     v1 = dp[i][j+1] + ord(s1[i])
#                     v2 = dp[i+1][j] + ord(s2[j])
#                     dp[i+1][j+1] = min(v1, v2)
#         return dp[l1][l2]


# Runtime
# Details
# 442ms
# Beats 95.11%of users with Python3
# Memory
# Details
# 16.52mb
# Beats 89.32%of users with Python3
# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         l1, l2 = len(s1), len(s2)
#         dp = [[0] * (l2+1) for _ in range(2)]
#         for j in range(l2):
#             dp[0][j+1] = dp[0][j] + ord(s2[j])
#         for i in range(l1):
#             i1 = i % 2
#             i2 = 1 - i1
#             dp[i2][0] = dp[i1][0] + ord(s1[i])
#             for j in range(l2):
#                 if s1[i] == s2[j]:
#                     dp[i2][j+1] = dp[i1][j]
#                 else:
#                     v1 = dp[i1][j+1] + ord(s1[i])
#                     v2 = dp[i2][j] + ord(s2[j])
#                     dp[i2][j+1] = min(v1, v2)
#         return dp[l1 % 2][l2]


# Runtime
# Details
# 428ms
# Beats 95.80%of users with Python3
# Memory
# Details
# 16.49mb
# Beats 91.25%of users with Python3
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            s1, s2 = s2, s1
            l1, l2 = l2, l1
        dp = [[0] * (l2+1) for _ in range(2)]
        for j in range(l2):
            dp[0][j+1] = dp[0][j] + ord(s2[j])
        for i in range(l1):
            i1 = i % 2
            i2 = 1 - i1
            dp[i2][0] = dp[i1][0] + ord(s1[i])
            for j in range(l2):
                if s1[i] == s2[j]:
                    dp[i2][j+1] = dp[i1][j]
                else:
                    v1 = dp[i1][j+1] + ord(s1[i])
                    v2 = dp[i2][j] + ord(s2[j])
                    dp[i2][j+1] = min(v1, v2)
        return dp[l1 % 2][l2]

# WRONG???
# class Solution:
#     def minimumDeleteSum(self, s1: str, s2: str) -> int:
#         l1, l2 = len(s1), len(s2)
#         dp = [[0] * (l2+1) for _ in range(2)]
#         for j in range(l2):
#             dp[0][j+1] = dp[0][j] + ord(s2[j])
#         for i in range(l1):
#             i1 = i % 2
#             i2 = 1 - i1
#             dp[i2][0] = dp[i1][0] + ord(s1[i])
#             for j in range(l2):
#                 if s1[i] == s2[j]:
#                     dp[i2][j+1] = dp[i1][j]
#                 else:
#                     v1 = dp[i1][j+1] + ord(s1[i1])
#                     v2 = dp[i2][j] + ord(s2[j])
#                     dp[i2][j+1] = min(v1, v2)
#         return dp[l1 % 2][l2]


tests = [
    ["sea", "eat", 231],
    ["delete", "leet", 403],
    ["ccaccjp", "fwosarcwge", 1399],
]

run_functional_tests(Solution().minimumDeleteSum, tests)
