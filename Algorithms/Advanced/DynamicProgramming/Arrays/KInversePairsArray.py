"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3784/
https://leetcode.com/problems/k-inverse-pairs-array/

For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].

Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.



Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pairs.
Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.


Constraints:

1 <= n <= 1000
0 <= k <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# TLE - 1000, 1000 - did not submit
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[0] * (k+1) for _ in range(n+1)]
#         for i in range(1, n+1):
#             dp[i][0] = 1
#         for i in range(1, n+1):
#             for j in range(1, k+1):
#                 s = 0
#                 for l in range(min(j, i-1)+1):
#                     s += dp[i-1][j-l] % MOD
#                 dp[i][j] = s % MOD
#         return dp[n][k]

# Runtime: 588 ms, faster than 38.36% of Python3 online submissions for K Inverse Pairs Array.
# Memory Usage: 53.5 MB, less than 20.55% of Python3 online submissions for K Inverse Pairs Array.
# class Solution:
#     def kInversePairs(self, n: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[0] * (k+1) for _ in range(n+1)]
#         for i in range(1, n+1):
#             dp[i][0] = 1
#         for i in range(1, n+1):
#             for j in range(1, k+1):
#                 v1 = dp[i-1][j - i] if j >= i else 0
#                 v = (dp[i-1][j] + MOD - v1) % MOD
#                 dp[i][j] = (dp[i][j-1] + v) % MOD
#         return (dp[n][k] + MOD - (dp[n][k-1] if k > 0 else 0)) % MOD


# Runtime: 596 ms, faster than 36.99% of Python3 online submissions for K Inverse Pairs Array.
# Memory Usage: 52.6 MB, less than 42.47% of Python3 online submissions for K Inverse Pairs Array.
class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            maxk = min(k, i * (i-1) // 2)
            for j in range(1, maxk+1):
                v1 = dp[i-1][j - i] if j >= i else 0
                v = (dp[i-1][j] + MOD - v1) % MOD
                dp[i][j] = (dp[i][j-1] + v) % MOD
        return dp[n][k]


tests = [
    [10, 4, 440],
    [3, 0, 1],
    [3, 1, 2]
]

run_functional_tests(Solution().kInversePairs, tests)