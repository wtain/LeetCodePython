"""
https://leetcode.com/problems/shift-2d-grid/

Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.



Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 181 ms, faster than 79.11% of Python3 online submissions for Shift 2D Grid.
# Memory Usage: 14.3 MB, less than 61.56% of Python3 online submissions for Shift 2D Grid.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        if not n:
            return []
        m = len(grid[0])
        nm = n*m
        cnt = 0
        for i in range(n):
            for j in range(m):
                ij = i * m + j
                ij1 = (ij + k) % nm
                v = grid[i][j]
                while ij != ij1:
                    i1 = ij1 // m
                    j1 = ij1 % m

                    grid[i1][j1], v = v, grid[i1][j1]
                    cnt += 1
                    ij1 = (ij1+k) % nm
                grid[i][j] = v
                cnt += 1
                if cnt == nm:
                    return grid
        return grid


tests = [
    [[[1,2,3],[4,5,6],[7,8,9]], 1, [[9,1,2],[3,4,5],[6,7,8]]],
    [[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4, [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]],
    [[[1,2,3],[4,5,6],[7,8,9]], 9, [[1,2,3],[4,5,6],[7,8,9]]]
]

run_functional_tests(Solution().shiftGrid, tests)
