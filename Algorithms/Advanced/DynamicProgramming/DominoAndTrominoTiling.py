"""
https://leetcode.com/problems/domino-and-tromino-tiling/

You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.



Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numTilings(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         states = [[0] * 4 for _ in range(n)]
#         # 0    0    1    1
#         # 0    1    0    1
#         states[0][0] = 1
#         states[0][3] = 1
#         for i in range(1, n):
#             states[i][0] = states[i-1][3]
#             states[i][1] = states[i-1][2] + states[i-1][0]
#             states[i][2] = states[i-1][1] + states[i-1][0]
#             states[i][3] = states[i-1][2] + states[i-1][1] + 2 * states[i-1][0] + states[i-1][3]
#
#         return states[-1][-1] % MOD

# WRONG
# class Solution:
#     def numTilings(self, n: int) -> int:
#         MOD = 10 ** 9 + 7
#         dp = [0] * (n+1)
#         dp[0] = 1
#         dp[1] = 1
#         if n >= 2:
#             dp[2] = 2
#         for i in range(3, n+1):
#             dp[i] = (dp[i-1] + 2*dp[i-2]) % MOD
#
#         return dp[-1]


# Runtime: 36 ms, faster than 63.08% of Python3 online submissions for Domino and Tromino Tiling.
# Memory Usage: 14.2 MB, less than 70.51% of Python3 online submissions for Domino and Tromino Tiling.
# https://leetcode.com/problems/domino-and-tromino-tiling/solution/
class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
        MOD = 10 ** 9 + 7
        prev_full = 1
        curr_full = 2
        curr_part = 1
        for i in range(3, n+1):
            tmp = curr_full
            curr_full = (curr_full + prev_full + 2 * curr_part) % MOD
            curr_part = (curr_part + prev_full) % MOD
            prev_full = tmp

        return curr_full


tests = [
    [10, 1255],
    [2, 2],
    [3, 5],
    [1, 1]
]

run_functional_tests(Solution().numTilings, tests)
