"""
https://leetcode.com/problems/determine-if-a-cell-is-reachable-at-a-given-time/description/?envType=daily-question&envId=2023-11-08

You are given four integers sx, sy, fx, fy, and a non-negative integer t.

In an infinite 2D grid, you start at the cell (sx, sy). Each second, you must move to any of its adjacent cells.

Return true if you can reach cell (fx, fy) after exactly t seconds, or false otherwise.

A cell's adjacent cells are the 8 cells around it that share at least one corner with it. You can visit the same cell several times.



Example 1:


Input: sx = 2, sy = 4, fx = 7, fy = 7, t = 6
Output: true
Explanation: Starting at cell (2, 4), we can reach cell (7, 7) in exactly 6 seconds by going through the cells depicted in the picture above.
Example 2:


Input: sx = 3, sy = 1, fx = 7, fy = 3, t = 3
Output: false
Explanation: Starting at cell (3, 1), it takes at least 4 seconds to reach cell (7, 3) by going through the cells depicted in the picture above. Hence, we cannot reach cell (7, 3) at the third second.


Constraints:

1 <= sx, sy, fx, fy <= 109
0 <= t <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 40ms
# Beats 56.59%of users with Python3
# Memory
# Details
# 16.20MB
# Beats 94.64%of users with Python3
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        dx, dy = abs(fx - sx), abs(fy - sy)
        if dx == 0 and dy == 0:
            return t != 1
        return max(dx, dy) <= t


tests = [
    [2, 4, 7, 7, 6, True],
    [3, 1, 7, 3, 3, False],
    [1, 2, 1, 2, 1, False],
    [1, 1, 1, 1, 3, True],
    [1, 4, 1, 2, 1, False],
]

run_functional_tests(Solution().isReachableAtTime, tests)
