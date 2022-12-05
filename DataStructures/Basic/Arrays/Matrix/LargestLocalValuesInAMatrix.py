"""
https://leetcode.com/problems/largest-local-values-in-a-matrix/

You are given an n x n integer matrix grid.

Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:

maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.

Return the generated matrix.



Example 1:


Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
Output: [[9,9],[8,6]]
Explanation: The diagram above shows the original matrix and the generated matrix.
Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
Example 2:


Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
Output: [[2,2,2],[2,2,2],[2,2,2]]
Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.


Constraints:

n == grid.length == grid[i].length
3 <= n <= 100
1 <= grid[i][j] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 595 ms
# Beats
# 11.14%
# Memory
# 14.4 MB
# Beats
# 87.16%
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        result = [[0] * (n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                i1, i2 = i, i + 2
                j1, j2 = j, j + 2
                mx = grid[i1][j1]
                for i0 in range(i1, i2+1):
                    for j0 in range(j1, j2+1):
                        mx = max(mx, grid[i0][j0])
                result[i][j] = mx
        return result



# WRONG
# class Solution:
#     def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
#         n = len(grid)
#         result = [[0] * (n-2) for _ in range(n-2)]
#         for i in range(n-2):
#             for j in range(n-2):
#                 for k in range(3):
#                     result[i][j] = max(result[i][j], grid[i+k][j+1])
#         for i in range(n-2):
#             for j in range(n-2):
#                 for k in range(3):
#                     result[i][j] = max(result[i][j], grid[i+1][j+k])
#         return result


tests = [
    [[[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]], [[9,9],[8,6]]],
    [[[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]], [[2,2,2],[2,2,2],[2,2,2]]]
]

run_functional_tests(Solution().largestLocal, tests)
