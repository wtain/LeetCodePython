"""
https://leetcode.com/problems/dungeon-game/

The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.



Example 1:


Input: dungeon = [[-2,-3,3],[-5,-10,1],[10,30,-5]]
Output: 7
Explanation: The initial health of the knight must be at least 7 if he follows the optimal path: RIGHT-> RIGHT -> DOWN -> DOWN.
Example 2:

Input: dungeon = [[0]]
Output: 1


Constraints:

m == dungeon.length
n == dungeon[i].length
1 <= m, n <= 200
-1000 <= dungeon[i][j] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 85 ms, faster than 38.39% of Python3 online submissions for Dungeon Game.
# Memory Usage: 15.2 MB, less than 71.93% of Python3 online submissions for Dungeon Game.
# https://leetcode.com/submissions/detail/356692143/
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        dp = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if i < n-1 and j < m-1:
                    dp[i][j] = min(0, dungeon[i][j] + max(dp[i + 1][j], dp[i][j + 1]))
                elif i < n-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i + 1][j])
                elif j < m-1:
                    dp[i][j] = min(0, dungeon[i][j] + dp[i][j + 1])
                else:
                    dp[i][j] = min(0, dungeon[i][j])
        return 1 - dp[0][0]


tests = [
    [[[-2,-3,3],[-5,-10,1],[10,30,-5]], 7],
    [[[0]], 1]
]

run_functional_tests(Solution().calculateMinimumHP, tests)