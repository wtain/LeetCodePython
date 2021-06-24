"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3775/
https://leetcode.com/problems/stone-game-vii/

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones arranged in a row. On each player's turn, they can remove either the leftmost stone or the rightmost stone from the row and receive points equal to the sum of the remaining stones' values in the row. The winner is the one with the higher score when there are no stones left to remove.

Bob found that he will always lose this game (poor Bob, he always loses), so he decided to minimize the score's difference. Alice's goal is to maximize the difference in the score.

Given an array of integers stones where stones[i] represents the value of the ith stone from the left, return the difference in Alice and Bob's score if they both play optimally.



Example 1:

Input: stones = [5,3,1,4,2]
Output: 6
Explanation:
- Alice removes 2 and gets 5 + 3 + 1 + 4 = 13 points. Alice = 13, Bob = 0, stones = [5,3,1,4].
- Bob removes 5 and gets 3 + 1 + 4 = 8 points. Alice = 13, Bob = 8, stones = [3,1,4].
- Alice removes 3 and gets 1 + 4 = 5 points. Alice = 18, Bob = 8, stones = [1,4].
- Bob removes 1 and gets 4 points. Alice = 18, Bob = 12, stones = [4].
- Alice removes 4 and gets 0 points. Alice = 18, Bob = 12, stones = [].
The score difference is 18 - 12 = 6.
Example 2:

Input: stones = [7,90,5,1,100,10,10,2]
Output: 122


Constraints:

n == stones.length
2 <= n <= 1000
1 <= stones[i] <= 1000
"""
from functools import lru_cache
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def stoneGameVII(self, stones: List[int]) -> int:
#         n = len(stones)
#         S = sum(stones)
#         cs1 = [0] * n
#         cs2 = [0] * n
#         cs1[0] = stones[0]
#         for i in range(1, n):
#             cs1[i] = cs1[i-1] + stones[i]
#         cs2[-1] = stones[-1]
#         for i in range(n-2, -1, -1):
#             cs2[i] = cs2[i + 1] + stones[i]
#         # sum i..j = S - cs1[i-1] - cs2[j+1]
#         cs1 = [0] + cs1
#         cs2 = cs2 + [0]
#         # sum i..j = S - cs1[i] - cs2[j]
#         # F(0..n-1) = max(F(-1)-F(-2)) = max(F(0..n-2))
#         return 0


# https://leetcode.com/problems/stone-game-vii/discuss/1264544/Python-O(n*n)-dp-solution-how-to-avoid-TLE-explained
# Runtime: 8228 ms, faster than 8.24% of Python3 online submissions for Stone Game VII.
# Memory Usage: 21.7 MB, less than 85.29% of Python3 online submissions for Stone Game VII.
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        cs = [0] + list(accumulate(stones))
        @lru_cache(2000)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            sm = cs[j+1] - cs[i]
            return sm - min(stones[i] + dp(i+1, j), stones[j] + dp(i, j-1))

        return dp(0, n-1)




tests = [
    [[5,3,1,4,2], 6],
    [[7,90,5,1,100,10,10,2], 122]
]

run_functional_tests(Solution().stoneGameVII, tests)