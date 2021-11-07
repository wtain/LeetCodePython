"""
https://leetcode.com/problems/unique-paths-iii/

You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.



Example 1:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:


Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:


Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 20
1 <= m * n <= 20
-1 <= grid[i][j] <= 2
There is exactly one starting cell and one ending cell.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 91.86% of Python3 online submissions for Unique Paths III.
# Memory Usage: 14.3 MB, less than 46.77% of Python3 online submissions for Unique Paths III.
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        i1, j1 = -1, -1
        cells = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    i1, j1 = i, j
                if grid[i][j] != -1:
                    cells += 1

        cnt = 0
        mask = [[False] * m for _ in range(n)]
        neighbours = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def impl(i: int, j: int, steps: int):
            nonlocal i1, j1, n, m, mask, grid, cnt
            if grid[i][j] == 2:
                if steps == cells - 1:
                    cnt += 1
                return
            mask[i][j] = True
            for di, dj in neighbours:
                ix, jx = i+di, j+dj
                if 0 <= ix < n and 0 <= jx < m and not mask[ix][jx] and grid[ix][jx] != -1:
                    impl(ix, jx, steps+1)

            mask[i][j] = False

        impl(i1, j1, 0)

        return cnt


tests = [
    [
        [[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2
    ],
    [
        [[1,0,0,0],[0,0,0,0],[0,0,0,2]], 4
    ],
    [
        [[0,1],[2,0]], 0
    ]
]

run_functional_tests(Solution().uniquePathsIII, tests)
