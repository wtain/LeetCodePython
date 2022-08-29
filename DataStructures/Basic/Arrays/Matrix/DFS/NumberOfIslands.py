"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 328 ms, faster than 89.83% of Python3 online submissions for Number of Islands.
# Memory Usage: 16.2 MB, less than 97.80% of Python3 online submissions for Number of Islands.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        cnt = 0
        n, m = len(grid), len(grid[0])

        def mark(i0: int, j0: int):
            toProcess = [(i0, j0)]
            while toProcess:
                i, j = toProcess.pop()
                grid[i][j] = '0'
                if i > 0 and grid[i-1][j] == '1':
                    toProcess.append((i-1, j))
                if j > 0 and grid[i][j-1] == '1':
                    toProcess.append((i, j-1))
                if i < n-1 and grid[i + 1][j] == '1':
                    toProcess.append((i + 1, j))
                if j < m-1 and grid[i][j + 1] == '1':
                    toProcess.append((i, j + 1))

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    cnt += 1
                    mark(i, j)

        return cnt


tests = [
    [
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], 1
    ],
    [
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], 3
    ]
]

run_functional_tests(Solution().numIslands, tests)
