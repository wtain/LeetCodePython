"""
https://leetcode.com/problems/flip-string-to-monotone-increasing/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3876/

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.



Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.


Constraints:

1 <= s.length <= 105
s[i] is either '0' or '1'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 536 ms, faster than 5.30% of Python3 online submissions for Flip Strings to Monotone Increasing.
# Memory Usage: 26.4 MB, less than 5.30% of Python3 online submissions for Flip Strings to Monotone Increasing.
# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         n = len(s)
#         dp = [[0, 0] for _ in range(n)]
#         if s[0] == '0':
#             dp[0][0] = 0
#             dp[0][1] = 1
#         else:
#             dp[0][0] = 1
#             dp[0][1] = 0
#         for i in range(1, n):
#             if s[i] == '0':
#                 dp[i][0] = dp[i-1][0]
#                 dp[i][1] = min(dp[i-1][1] + 1, dp[i-1][0])
#             else:
#                 dp[i][0] = dp[i-1][0]+1
#                 dp[i][1] = min(dp[i-1][1], dp[i-1][0])
#         return min(dp[-1][0], dp[-1][1])


# Runtime: 204 ms, faster than 13.26% of Python3 online submissions for Flip Strings to Monotone Increasing.
# Memory Usage: 14.9 MB, less than 48.48% of Python3 online submissions for Flip Strings to Monotone Increasing.
# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         n = len(s)
#         if s[0] == '0':
#             dp0 = 0
#             dp1 = 1
#         else:
#             dp0 = 1
#             dp1 = 0
#         for i in range(1, n):
#             if s[i] == '0':
#                 dp1 = min(dp1 + 1, dp0)
#             else:
#                 dp1 = min(dp1, dp0)
#                 dp0 = dp0 + 1
#         return min(dp0, dp1)


# https://leetcode.com/problems/flip-string-to-monotone-increasing/solution/
# Runtime: 360 ms, faster than 5.30% of Python3 online submissions for Flip Strings to Monotone Increasing.
# Memory Usage: 18.8 MB, less than 7.95% of Python3 online submissions for Flip Strings to Monotone Increasing.
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        P = [0]
        for c in s:
            P.append(P[-1] + int(c))

        return min(P[j] + len(s)-j-(P[-1]-P[j]) for j in range(len(P)))


tests = [
    ["01110", 1],
    ["00110", 1],
    ["010110", 2],
    ["00011000", 2]
]

run_functional_tests(Solution().minFlipsMonoIncr, tests)