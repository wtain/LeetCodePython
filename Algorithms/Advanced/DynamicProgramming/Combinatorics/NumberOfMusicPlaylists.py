"""
https://leetcode.com/problems/number-of-music-playlists/description/

Your music player contains n different songs. You want to listen to goal songs (not necessarily different) during your trip. To avoid boredom, you will create a playlist so that:

Every song is played at least once.
A song can only be played again only if k other songs have been played.
Given n, goal, and k, return the number of possible playlists that you can create. Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: n = 3, goal = 3, k = 1
Output: 6
Explanation: There are 6 possible playlists: [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], and [3, 2, 1].
Example 2:

Input: n = 2, goal = 3, k = 0
Output: 6
Explanation: There are 6 possible playlists: [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], and [1, 2, 2].
Example 3:

Input: n = 2, goal = 3, k = 1
Output: 2
Explanation: There are 2 possible playlists: [1, 2, 1] and [2, 1, 2].


Constraints:

0 <= k < n <= goal <= 100
"""
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 56ms
# Beats 80.45%of users with Python3
# Memory
# Details
# 16.51mb
# Beats 72.18%of users with Python3
# https://leetcode.com/problems/number-of-music-playlists/editorial/
# class Solution:
#     def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [[0 for _ in range(n+1)] for _ in range(goal+1)]
#         dp[0][0] = 1
#
#         for i in range(1, goal+1):
#             for j in range(1, min(i, n) + 1):
#                 dp[i][j] = dp[i-1][j-1] * (n - j+1) % MOD
#                 if j > k:
#                     dp[i][j] = (dp[i][j] + dp[i-1][j] * (j-k)) % MOD
#         return dp[goal][n]


# Runtime
# Details
# 87ms
# Beats 37.59%of users with Python3
# Memory
# Details
# 20.09mb
# Beats 6.02%of users with Python3
# https://leetcode.com/problems/number-of-music-playlists/editorial/
# class Solution:
#     def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
#         MOD = 10 ** 9 + 7
#
#         @cache
#         def impl(i, j):
#             if i == 0 and j == 0:
#                 return 1
#             if i == 0 or j == 0:
#                 return 0
#
#             res = impl(i-1,j-1) * (n - j+1) % MOD
#             if j > k:
#                 res += impl(i-1,j) * (j-k)
#                 res %= MOD
#             return res
#
#         return impl(goal, n)


# Runtime
# Details
# 59ms
# Beats 73.68%of users with Python3
# Memory
# Details
# 16.40mb
# Beats 90.98%of users with Python3
# https://leetcode.com/problems/number-of-music-playlists/editorial/
class Solution:
    MOD = 10 ** 9 + 7

    def power(self, base, ex):
        result = 1
        while ex > 0:
            if ex & 1:
                result = (result * base) % self.MOD
            ex >>= 1
            base = (base * base) % self.MOD
        return result

    def precalc_fac(self, n):
        self.fact = [1] * (n+1)
        self.invfact = [1] * (n+1)
        for i in range(1, n+1):
            self.fact[i] = (self.fact[i-1] * i) % self.MOD
            self.invfact[i] = self.power(self.fact[i], self.MOD-2)

    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        self.precalc_fac(n)
        sign, res = 1, 0

        for i in range(n, k-1, -1):
            temp = self.power(i-k, goal-k)
            temp = (temp * self.invfact[n-i]) % self.MOD
            temp = (temp * self.invfact[i-k]) % self.MOD
            res = (res + sign * temp + self.MOD) % self.MOD
            sign *= -1
        return self.fact[n] * res % self.MOD


tests = [
    [3, 3, 1, 6],
    [2, 3, 0, 6],
    [2, 3, 1, 2],
]

run_functional_tests(Solution().numMusicPlaylists, tests)
