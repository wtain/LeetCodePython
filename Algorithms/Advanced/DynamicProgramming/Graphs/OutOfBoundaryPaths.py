"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3790/
https://leetcode.com/problems/out-of-boundary-paths/

There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent four cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 109 + 7.



Example 1:


Input: m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
Output: 6
Example 2:


Input: m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
Output: 12


Constraints:

1 <= m, n <= 50
0 <= maxMove <= 50
0 <= startRow <= m
0 <= startColumn <= n
"""
from functools import lru_cache

from Common.ObjectTestingUtils import run_functional_tests


# https://leetcode.com/problems/out-of-boundary-paths/solution/

# Runtime: 84 ms, faster than 97.92% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 20.3 MB, less than 22.08% of Python3 online submissions for Out of Boundary Paths.
# class Solution:
#     def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
#         MOD = 10**9 + 7
#
#         @lru_cache(None)
#         def findPathsImpl(N: int, i: int, j: int) -> int:
#             # print(N, i, j)
#             if i == -1 or j == -1 or i == m or j == n:
#                 return 1
#             if N == 0:
#                 return 0
#             return (findPathsImpl(N - 1, i - 1, j) +
#                     findPathsImpl(N - 1, i, j - 1) +
#                     findPathsImpl(N - 1, i + 1, j) +
#                     findPathsImpl(N - 1, i, j + 1)) % MOD
#
#         return findPathsImpl(maxMove, startRow, startColumn) % MOD

# Runtime: 192 ms, faster than 31.43% of Python3 online submissions for Out of Boundary Paths.
# Memory Usage: 14.6 MB, less than 82.86% of Python3 online submissions for Out of Boundary Paths.
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * n for _ in range(m)]
        dp[startRow][startColumn] = 1
        cnt = 0
        for k in range(maxMove):
            tmp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    if i == 0:
                        cnt = (cnt + dp[i][j]) % MOD
                    if i == m - 1:
                        cnt = (cnt + dp[i][j]) % MOD
                    if j == 0:
                        cnt = (cnt + dp[i][j]) % MOD
                    if j == n-1:
                        cnt = (cnt + dp[i][j]) % MOD
                    tmp[i][j] = ((dp[i - 1][j] if i > 0 else 0) +
                                 (dp[i][j - 1] if j > 0 else 0) +
                                 (dp[i+1][j] if i < m-1 else 0) +
                                 (dp[i][j + 1] if j < n-1 else 0)) % MOD
            dp = tmp

        return cnt


tests = [
    [2, 2, 2, 0, 0, 6],
    [1, 3, 3, 0, 1, 12]
]

run_functional_tests(Solution().findPaths, tests)