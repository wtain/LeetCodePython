"""
https://leetcode.com/problems/projection-area-of-3d-shapes/
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.



Example 1:

Input: [[2]]
Output: 5
Example 2:

Input: [[1,2],[3,4]]
Output: 17
Explanation:
Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input: [[1,0],[0,2]]
Output: 8
Example 4:

Input: [[1,1,1],[1,0,1],[1,1,1]]
Output: 14
Example 5:

Input: [[2,2,2],[2,1,2],[2,2,2]]
Output: 21


Note:

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50

Runtime: 72 ms, faster than 64.42% of Python3 online submissions for Projection Area of 3D Shapes.
Memory Usage: 14.5 MB, less than 12.88% of Python3 online submissions for Projection Area of 3D Shapes.

Runtime: 80 ms, faster than 20.25% of Python3 online submissions for Projection Area of 3D Shapes.
Memory Usage: 14.4 MB, less than 12.88% of Python3 online submissions for Projection Area of 3D Shapes.
"""
from typing import List


# class Solution:
#     def projectionArea(self, grid: List[List[int]]) -> int:
#         h = len(grid)
#         w = len(grid[0])
#         result = 0
#         xz = [0] * w
#         yz = [0] * h
#         for i in range(h):
#             for j in range(w):
#                 if grid[i][j] > 0:
#                     result += 1
#                 if grid[i][j] > xz[j]:
#                     result += grid[i][j] - xz[j]
#                     xz[j] = grid[i][j]
#                 if grid[i][j] > yz[i]:
#                     result += grid[i][j] - yz[i]
#                     yz[i] = grid[i][j]
#         return result

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 0
        for i in range(n):
            maxi = 0
            maxj = 0
            for j in range(n):
                if grid[i][j] > 0:
                    result += 1
                maxi = max(maxi, grid[i][j])
                maxj = max(maxj, grid[j][i])
            result += maxi + maxj
        return result


tests = [
    ([[2]], 5),
    ([[1,2],[3,4]], 17),
    ([[1,0],[0,2]], 8),
    ([[1,1,1],[1,0,1],[1,1,1]], 14),
    ([[2,2,2],[2,1,2],[2,2,2]], 21)
]

for test in tests:
    result = Solution().projectionArea(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))
