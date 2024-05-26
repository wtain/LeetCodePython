"""
https://leetcode.com/problems/student-attendance-record-ii/description/?envType=daily-question&envId=2024-05-26

An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.



Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316


Constraints:

1 <= n <= 105
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests

# MLE
# https://leetcode.com/problems/student-attendance-record-ii/editorial/?envType=daily-question&envId=2024-05-26
# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def eligible_combinations(n, total_absences, consequtive_lates):
#             if total_absences >= 2 or consequtive_lates >= 3:
#                 return 0
#             if n == 0:
#                 return 1
#
#             count = eligible_combinations(n-1, total_absences, 0)
#             count += eligible_combinations(n-1, total_absences+1, 0)
#             count += eligible_combinations(n-1, total_absences, consequtive_lates+1)
#             count %= MOD
#             return count
#
#         return eligible_combinations(n, 0, 0)


# Runtime
# 4870
# ms
# Beats
# 35.55%
# of users with Python3
# Memory
# 64.23
# MB
# Beats
# 45.50%
# of users with Python3
# https://leetcode.com/problems/student-attendance-record-ii/editorial/?envType=daily-question&envId=2024-05-26
# class Solution:
#     def checkRecord(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         dp = [[[0] * 3 for _ in range(2)] for _ in range(n+1)]
#
#         dp[0][0][0] = 1
#
#         for length in range(n):
#             for total_absences in range(2):
#                 for consecutive_lates in range(3):
#                     dp[length+1][total_absences][0] = (dp[length+1][total_absences][0] + dp[length][total_absences][consecutive_lates]) % MOD
#                     if total_absences < 1:
#                         dp[length + 1][total_absences+1][0] = (dp[length+1][total_absences+1][0] + dp[length][total_absences][consecutive_lates]) % MOD
#                     if consecutive_lates < 2:
#                         dp[length + 1][total_absences][consecutive_lates+1] = (dp[length+1][total_absences][consecutive_lates+1] + dp[length][total_absences][consecutive_lates]) % MOD
#
#         count = 0
#         for total_absences in range(2):
#             for consecutive_lates in range(3):
#                 count += dp[n][total_absences][consecutive_lates]
#                 count %= MOD
#
#         return count


# Runtime
# 3519
# ms
# Beats
# 53.56%
# of users with Python3
# Memory
# 16.50
# MB
# Beats
# 89.57%
# of users with Python3
# https://leetcode.com/problems/student-attendance-record-ii/editorial/?envType=daily-question&envId=2024-05-26
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7

        dp_curr = [[0] * 3 for _ in range(2)]
        dp_next = [[0] * 3 for _ in range(2)]

        dp_curr[0][0] = 1

        for _ in range(n):
            for total_absences in range(2):
                for consecutive_lates in range(3):
                    dp_next[total_absences][0] = (dp_next[total_absences][0] + dp_curr[total_absences][consecutive_lates]) % MOD
                    if total_absences < 1:
                        dp_next[total_absences+1][0] = (dp_next[total_absences+1][0] + dp_curr[total_absences][consecutive_lates]) % MOD
                    if consecutive_lates < 2:
                        dp_next[total_absences][consecutive_lates+1] = (dp_next[total_absences][consecutive_lates+1] + dp_curr[total_absences][consecutive_lates]) % MOD
            dp_curr = [row[:] for row in dp_next]
            dp_next = [[0] * 3 for _ in range(2)]

        count = sum(dp_curr[total_absences][consecutive_lates] for total_absences in range(2) for consecutive_lates in range(3)) % MOD

        return count


tests = [
    [2, 8],
    [1, 3],
    [10101, 183236316],
]

run_functional_tests(Solution().checkRecord, tests)
