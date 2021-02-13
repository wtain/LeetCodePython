"""
https://leetcode.com/problems/surface-area-of-3d-shapes/
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.



Example 1:

Input: [[2]]
Output: 10
Example 2:

Input: [[1,2],[3,4]]
Output: 34
Example 3:

Input: [[1,0],[0,2]]
Output: 16
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 46


Note:

1 <= N <= 50
0 <= grid[i][j] <= 50

Runtime: 88 ms, faster than 65.79% of Python3 online submissions for Surface Area of 3D Shapes.
Memory Usage: 14.4 MB, less than 31.95% of Python3 online submissions for Surface Area of 3D Shapes.

Runtime: 128 ms, faster than 8.65% of Python3 online submissions for Surface Area of 3D Shapes.
Memory Usage: 14.3 MB, less than 60.53% of Python3 online submissions for Surface Area of 3D Shapes.
"""
from typing import List


# class Solution:
#     def surfaceArea(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         result = 0
#         for i in range(n):
#             for j in range(n):
#                 if grid[i][j] > 0:
#                     result += 2
#                 if i == 0:
#                     result += grid[i][j]
#                 if i == n-1:
#                     result += grid[i][j]
#                 if 0 < i:
#                     result += abs(grid[i-1][j] - grid[i][j])
#                 if j == 0:
#                     result += grid[i][j]
#                 if j == n-1:
#                     result += grid[i][j]
#                 if 0 < j:
#                     result += abs(grid[i][j-1] - grid[i][j])
#
#         return result

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    result += 2
                    for k in range(4):
                        di, dj = neighbours[k]
                        i1 = i + di
                        j1 = j + dj
                        nv = 0
                        if 0 <= i1 < n and 0 <= j1 < n:
                            nv = grid[i1][j1]
                        result += max(grid[i][j] - nv, 0)

        return result


tests = [
    ([[2]], 10),
    ([[1,2],[3,4]], 34),
    ([[1,0],[0,2]], 16),
    ([[1,1,1],[1,0,1],[1,1,1]], 32),
    ([[2,2,2],[2,1,2],[2,2,2]], 46)
]

for test in tests:
    result = Solution().surfaceArea(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))
