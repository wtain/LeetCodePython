"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3740/
https://leetcode.com/problems/range-sum-query-2d-immutable/

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).


Example 1:


Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
-105 <= matrix[i][j] <= 105
0 <= row1 <= row2 < m
0 <= col1 <= col2 < n
At most 104 calls will be made to sumRegion.
"""
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 112 ms, faster than 57.02% of Python3 online submissions for Range Sum Query 2D - Immutable.
# Memory Usage: 17.3 MB, less than 53.93% of Python3 online submissions for Range Sum Query 2D - Immutable.
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        if not self.n:
            return
        self.m = len(matrix[0])
        self.ps = [[0] * self.m for _ in range(self.n)]
        for i in range(self.n):
            for j in range(self.m):
                v = matrix[i][j]
                s00, s01, s10 = 0, 0, 0
                if i and j:
                    s00 = self.ps[i-1][j-1]
                if i:
                    s01 = self.ps[i-1][j]
                if j:
                    s10 = self.ps[i][j-1]
                self.ps[i][j] = s01 + s10 - s00 + v

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s0, s1, s2, s3 = 0, 0, 0, 0
        s0 = self.ps[row2][col2]
        if row1 and col1:
            s3 = self.ps[row1-1][col1-1]
        if row1:
            s2 = self.ps[row1 - 1][col2]
        if col1:
            s1 = self.ps[row2][col1 - 1]
        return s0 - s1 - s2 + s3


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


tests = [
    [
        ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
        [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]],
        [null, 8, 11, 12]
    ]
]

run_object_tests(tests, cls=NumMatrix)