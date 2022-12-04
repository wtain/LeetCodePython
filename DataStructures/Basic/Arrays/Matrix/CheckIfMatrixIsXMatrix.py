"""
https://leetcode.com/problems/check-if-matrix-is-x-matrix/

A square matrix is said to be an X-Matrix if both of the following conditions hold:

All the elements in the diagonals of the matrix are non-zero.
All other elements are 0.
Given a 2D integer array grid of size n x n representing a square matrix, return true if grid is an X-Matrix. Otherwise, return false.



Example 1:


Input: grid = [[2,0,0,1],[0,3,1,0],[0,5,2,0],[4,0,0,2]]
Output: true
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is an X-Matrix.
Example 2:


Input: grid = [[5,7,0],[0,3,1],[0,5,0]]
Output: false
Explanation: Refer to the diagram above.
An X-Matrix should have the green elements (diagonals) be non-zero and the red elements be 0.
Thus, grid is not an X-Matrix.


Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
0 <= grid[i][j] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 838 ms
# Beats
# 5.74%
# Memory
# 15.1 MB
# Beats
# 19.37%
class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        return all(all(
                       (
                           bool(v) == bool(i == j or i + j + 1 == len(grid))
                         )
                       for j, v in enumerate(row)
                   )
                   for i, row in enumerate(grid)
                   )


# Runtime
# 286 ms
# Beats
# 91.68%
# Memory
# 14.8 MB
# Beats
# 99.43%
# class Solution:
#     def checkXMatrix(self, grid: List[List[int]]) -> bool:
#         n = len(grid)
#         for i in range(n):
#             for j in range(n):
#                 if i == j or i+j+1 == n:
#                     if grid[i][j] == 0:
#                         return False
#                 else:
#                     if grid[i][j] != 0:
#                         return False
#         return True


tests = [
    [[[5,0,0,1],[0,4,1,5],[0,5,2,0],[4,1,0,2]], False],
    [[[2, 0, 0, 1], [0, 3, 1, 0], [0, 5, 2, 0], [4, 0, 0, 2]], True],
    [[[5, 7, 0], [0, 3, 1], [0, 5, 0]], False]
]

run_functional_tests(Solution().checkXMatrix, tests)
