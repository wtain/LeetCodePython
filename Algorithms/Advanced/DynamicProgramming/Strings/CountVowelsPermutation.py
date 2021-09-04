"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3802/
https://leetcode.com/problems/count-vowels-permutation/

Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 260 ms, faster than 53.87% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 18 MB, less than 35.05% of Python3 online submissions for Count Vowels Permutation.
# class Solution:
#     def countVowelPermutation(self, n: int) -> int:
#         dp = [[1] * 5 for _ in range(n)]
#         MOD = 10**9 + 7
#         for i in range(1, n):
#             # A -> E
#             dp[i][0] = dp[i - 1][1]
#             # E -> A, I
#             dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % MOD
#             # I -> A, E, O, U
#             dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][3] + dp[i - 1][4]) % MOD
#             # O -> I, U
#             dp[i][3] = (dp[i - 1][2] + dp[i - 1][4]) % MOD
#             # U -> A
#             dp[i][4] = dp[i - 1][0]
#         return sum(dp[n-1]) % MOD


# Runtime: 96 ms, faster than 97.17% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 14.2 MB, less than 82.47% of Python3 online submissions for Count Vowels Permutation.
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        MOD = 10**9 + 7
        for _ in range(1, n):
            a, e, i, o, u = e, (a + i) % MOD, (a + e + o + u) % MOD, (i + u) % MOD, a
        return (a + e + i + o + u) % MOD


tests = [
    [144, 18208803],
    [1, 5],
    [2, 10],
    [5, 68]
]

run_functional_tests(Solution().countVowelPermutation, tests)