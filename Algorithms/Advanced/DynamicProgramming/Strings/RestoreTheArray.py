"""
https://leetcode.com/problems/restore-the-array/description/

A program was supposed to print an array of integers. The program forgot to print whitespaces and the array is printed as a string of digits s and all we know is that all integers in the array were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k, return the number of the possible arrays that can be printed as s using the mentioned program. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]
Example 2:

Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.
Example 3:

Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]


Constraints:

1 <= s.length <= 105
s consists of only digits and does not contain leading zeros.
1 <= k <= 109
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1501 ms
# Beats
# 69.86%
# Memory
# 176.2 MB
# Beats
# 12.33%
# class Solution:
#     def numberOfArrays(self, s: str, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         n = len(s)
#
#         @cache
#         def dp(i0):
#             if i0 == n:
#                 return 1
#             v = 0
#             result = 0
#             for i in range(i0, n):
#                 v *= 10
#                 v += int(s[i])
#                 if v > k or v == 0:
#                     break
#                 result += dp(i+1) % MOD
#             return result % MOD
#
#         return dp(0)


# Runtime
# 1246 ms
# Beats
# 95.89%
# Memory
# 17.9 MB
# Beats
# 93.15%
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(s)

        dp = [0] * (n+1)
        dp[n] = 1

        for i0 in range(n-1, -1, -1):
            v = 0
            result = 0
            for i in range(i0, n):
                v *= 10
                v += int(s[i])
                if v > k or v == 0:
                    break
                result += dp[i+1] % MOD
            dp[i0] = result % MOD

        return dp[0]

"""
n = len(s)
dp(n) = 1

dp(s0...s(n-1)) = sum(dp(si..s(n-1))))

"""



tests = [
    ["1000", 10000, 1],
    ["1000", 10, 0],
    ["1317", 2000, 8],
    ["171895851301603621199279559472582240564804526335544534392551", 905, 573330896],
]

run_functional_tests(Solution().numberOfArrays, tests)
