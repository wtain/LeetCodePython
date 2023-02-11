"""
https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

You are given an m x n grid. Each cell of grid represents a street. The street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). A valid path in the grid is a path that starts from the upper left cell (0, 0) and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.



Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2119 ms
# Beats
# 34.93%
# Memory
# 22.9 MB
# Beats
# 86.99%
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        p, rank = [[(i, j) for j in range(m)] for i in range(n)], [[1 for _ in range(m)] for _ in range(n)]

        def get(i, j):
            while p[i][j] != (i, j):
                i, j = p[i][j]
            return i, j

        def connect(i1, j1, i2, j2):
            i1, j1 = get(i1, j1)
            i2, j2 = get(i2, j2)
            if rank[i1][j1] >= rank[i2][j2]:
                p[i2][j2] = p[i1][j1]
                rank[i1][j1] += 1
            else:
                p[i1][j1] = p[i2][j2]
                rank[i2][j2] += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] in [1, 4, 6] and j+1 < m and grid[i][j+1] in [1, 3, 5]:
                    connect(i, j, i, j+1)
                if grid[i][j] in [2, 3, 4] and i+1 < n and grid[i+1][j] in [2, 5, 6]:
                    connect(i, j, i+1, j)

        return get(0, 0) == get(n-1, m-1)


tests = [
    [[[2,4,3],[6,5,2]], True],
    [[[1,2,1],[1,2,1]], False],
    [[[1,1,2]], False],
]

run_functional_tests(Solution().hasValidPath, tests)
