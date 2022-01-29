"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3870/
https://leetcode.com/problems/stone-game/

Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.



Example 1:

Input: piles = [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.


Constraints:

2 <= piles.length <= 500
piles.length is even.
1 <= piles[i] <= 500
sum(piles) is odd.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 80.62% of Python3 online submissions for Stone Game.
# Memory Usage: 14.7 MB, less than 51.65% of Python3 online submissions for Stone Game.
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n = len(piles)
#
#         @lru_cache(None)
#         def impl(i1: int, i2: int, s1: int, s2: int) -> bool:
#             nonlocal n
#             if i1 == i2 - 1:
#                 return s1 + max(piles[i1], piles[i2]) > s2 + min(piles[i1], piles[i2])
#             return impl(i1+1, i2-1, piles[i1], piles[i2]) or impl(i1+1, i2-1, piles[i2], piles[i1])
#
#         return impl(0, n-1, 0, 0)


# Runtime: 420 ms, faster than 39.43% of Python3 online submissions for Stone Game.
# Memory Usage: 20.1 MB, less than 35.92% of Python3 online submissions for Stone Game.
# https://leetcode.com/problems/stone-game/solution/
# class Solution:
#     def stoneGame(self, piles: List[int]) -> bool:
#         n = len(piles)
#         dp = [[0] * (n+2) for _ in range(n+2)]
#         for sz in range(1, n+1):
#             i = 0
#             for j in range(sz-1, n):
#                 parity = (j + i + n) % 2
#                 if parity:
#                     dp[i+1][j+1] = max(piles[i] + dp[i+2][j+1], piles[j] + dp[i+1][j])
#                 else:
#                     dp[i + 1][j + 1] = max(-piles[i] + dp[i + 2][j + 1], -piles[j] + dp[i + 1][j])
#                 i += 1
#         return dp[1][n] > 0


# Runtime: 32 ms, faster than 91.90% of Python3 online submissions for Stone Game.
# Memory Usage: 14.3 MB, less than 77.04% of Python3 online submissions for Stone Game.
# https://leetcode.com/problems/stone-game/solution/
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True


tests = [
    [[5,3,4,5], True],
    [[5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5,5,3,4,5], True]
]

run_functional_tests(Solution().stoneGame, tests)