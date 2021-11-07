"""
https://leetcode.com/problems/path-with-maximum-gold/

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

Every time you are located in a cell you will collect all the gold in that cell.
From your position, you can walk one step to the left, right, up, or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.
Example 2:

Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1016 ms, faster than 95.81% of Python3 online submissions for Path with Maximum Gold.
# Memory Usage: 14.4 MB, less than 50.58% of Python3 online submissions for Path with Maximum Gold.
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        result = 0
        n, m = len(grid), len(grid[0])
        used = [[False] * m for _ in range(n)]
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i, j in product(range(n), range(m)):
            if not grid[i][j]:
                used[i][j] = True

        def impl(i0: int, j0: int, gold: int):
            nonlocal result, n, m, used, grid, neighbors
            result = max(result, gold)
            used[i0][j0] = True
            for di, dj in neighbors:
                i, j = i0 + di, j0 + dj
                if 0 <= i < n and 0 <= j < m and not used[i][j]:
                    impl(i, j, gold + grid[i][j])
            used[i0][j0] = False

        for i, j in product(range(n), range(m)):
            if not used[i][j]:
                impl(i, j, grid[i][j])

        return result


tests = [
    [[[0,6,0],[5,8,7],[0,9,0]], 24],
    [[[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]], 28]
]

run_functional_tests(Solution().getMaximumGold, tests)
