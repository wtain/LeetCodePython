"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3888/
https://leetcode.com/problems/set-matrix-zeroes/

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.



Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]


Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1


Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""
from typing import List

from Common.FunctionalUtils import in_place_to_function
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 166 ms, faster than 9.57% of Python3 online submissions for Set Matrix Zeroes.
# Memory Usage: 15.2 MB, less than 46.95% of Python3 online submissions for Set Matrix Zeroes.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row0Z, col0Z = False, False
        n, m = len(matrix), len(matrix[0])
        for j in range(m):
            if not matrix[0][j]:
                row0Z = True
                break
        for i in range(n):
            if not matrix[i][0]:
                col0Z = True
                break
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][j]:
                    matrix[0][j] = matrix[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[0][j] or not matrix[i][0]:
                    matrix[i][j] = 0
        if row0Z:
            for j in range(m):
                 matrix[0][j] = 0
        if col0Z:
            for i in range(n):
                 matrix[i][0] = 0


tests = [
    [[[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]],
    [[[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]]
]

run_functional_tests(in_place_to_function(Solution().setZeroes), tests)