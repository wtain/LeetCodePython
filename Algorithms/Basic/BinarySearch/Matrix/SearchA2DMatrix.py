"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 67 ms, faster than 43.02% of Python3 online submissions for Search a 2D Matrix.
# Memory Usage: 14.6 MB, less than 8.89% of Python3 online submissions for Search a 2D Matrix.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        N = len(matrix)
        if not N:
            return False
        M = len(matrix[0])
        if not M:
            return False
        l, r = 0, N
        while l < r:
            m = (l+r) // 2
            v = matrix[m][-1]
            if v == target:
                return True
            elif v < target:
                l = m + 1
            else:
                r = m
        if l >= N:
            return False
        row = l
        l, r = 0, M
        while l < r:
            m = (l + r) // 2
            v = matrix[row][m]
            if v == target:
                return True
            if v < target:
                l = m + 1
            else:
                r = m
        return False


tests = [
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3, True],
    [[[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13, False]
]

run_functional_tests(Solution().searchMatrix, tests)
