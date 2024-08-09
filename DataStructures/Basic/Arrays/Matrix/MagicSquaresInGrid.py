"""
https://leetcode.com/problems/magic-squares-in-grid/description/?envType=daily-question&envId=2024-08-09

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 contiguous magic square subgrids are there?

Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.



Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation:
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0


Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 37
# ms
# Beats
# 81.03%
# Analyze Complexity
# Memory
# 16.43
# MB
# Beats
# 86.67%
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = 0
        for i in range(n-2):
            for j in range(m-2):
                d1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
                d2 = grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]

                if d1 != d2:
                    continue
                f = True
                rs, cs = [0] * 3, [0] * 3

                seen = [False] * 10

                for i1 in range(3):
                    for j1 in range(3):
                        v = grid[i+i1][j+j1]
                        if v < 1 or v > 9 or seen[v]:
                            f = False
                            break
                        rs[i1] += v
                        cs[j1] += v
                        seen[v] = True
                if not f:
                    continue
                for k in range(3):
                    if cs[k] != d1 or rs[k] != d1:
                        f = False
                        break
                if f:
                    cnt += 1
        return cnt


tests = [
    [[[5,5,5],[5,5,5],[5,5,5]], 0],
    [[[4,3,8,4],[9,5,1,9],[2,7,6,2]], 1],
    [[[8]], 0],
]

run_functional_tests(Solution().numMagicSquaresInside, tests)
