"""
https://leetcode.com/problems/stone-game-iv/

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.



Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).


Constraints:

1 <= n <= 105
"""
from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#
#         squares = set()
#         dp = [False] * (n + 1)
#
#         for i in range(1, n+1):
#             i2 = i ** 2
#             if i2 > n:
#                 break
#             squares.add(i2)
#             dp[i2] = True
#
#         for i in range(1, n+1):
#             if dp[i]:
#                 continue
#             found = False
#             for j in range(1, i):
#                 m = i - j
#                 if m not in squares:
#                     continue
#                 if not dp[j]:
#                     found = True
#                     break
#             if found:
#                 dp[i] = True
#
#         return dp[n]


# TLE?
# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#
#         squares = set()
#         dp = [False] * (n + 1)
#
#         for i in range(1, n+1):
#             i2 = i ** 2
#             if i2 > n:
#                 break
#             squares.add(i2)
#             dp[i2] = True
#
#         for i in range(1, n+1):
#             if dp[i]:
#                 continue
#             found = False
#             for j in range(i-1, 0, -1):
#                 m = i - j
#                 if m not in squares:
#                     continue
#                 if not dp[j]:
#                     found = True
#                     break
#             if found:
#                 dp[i] = True
#
#         return dp[n]


# Runtime: 1128 ms, faster than 65.27% of Python3 online submissions for Stone Game IV.
# Memory Usage: 14.9 MB, less than 76.05% of Python3 online submissions for Stone Game IV.
# class Solution:
#     def winnerSquareGame(self, n: int) -> bool:
#
#         squares = set()
#         dp = [False] * (n + 1)
#
#         for i in range(1, n+1):
#             i2 = i ** 2
#             if i2 > n:
#                 break
#             squares.add(i2)
#             dp[i2] = True
#
#         for i in range(1, n+1):
#             if dp[i]:
#                 continue
#             for m in squares:
#                 j = i - m
#                 if j > 0 and not dp[j]:
#                     dp[i] = True
#                     break
#
#         return dp[n]


# Runtime: 283 ms, faster than 86.83% of Python3 online submissions for Stone Game IV.
# Memory Usage: 14.8 MB, less than 92.22% of Python3 online submissions for Stone Game IV.
# https://leetcode.com/problems/stone-game-iv/solution/
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        nr1 = int(n ** 0.5) + 1
        for i in range(n+1):
            if dp[i]:
                continue
            for k in range(1, nr1):
                k2 = k*k
                if i + k2 <= n:
                    dp[i + k2] = True
                else:
                    break
        return dp[n]


tests = [
    [1, True],
    [2, False],
    [4, True],
    [10, False],
    [47, True],
    [100, True],
    [1023, True],
    [18082, True]
]

run_functional_tests(Solution().winnerSquareGame, tests)
