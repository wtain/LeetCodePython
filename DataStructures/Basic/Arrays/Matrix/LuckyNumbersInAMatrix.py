"""
https://leetcode.com/problems/lucky-numbers-in-a-matrix/

Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.



Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]


Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10^5.
All elements in the matrix are distinct.
"""
from typing import List

from Common.MatrixUtils import matrix_size
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 156 ms, faster than 14.91% of Python3 online submissions for Lucky Numbers in a Matrix.
# Memory Usage: 14.6 MB, less than 43.69% of Python3 online submissions for Lucky Numbers in a Matrix.
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        row_mins = [10**5] * n
        col_maxes = [0] * m
        for i in range(n):
            for j in range(m):
                row_mins[i] = min(row_mins[i], matrix[i][j])
                col_maxes[j] = max(col_maxes[j], matrix[i][j])
        result = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == col_maxes[j] and matrix[i][j] == row_mins[i]:
                    result.append(matrix[i][j])
        return result


tests = [
    [[[3,7,8],[9,11,13],[15,16,17]], [15]],
    [[[1,10,4,2],[9,3,8,7],[15,16,17,12]], [12]],
    [[[7,8],[1,2]], [7]]
]

run_functional_tests(Solution().luckyNumbers, tests, input_metric=lambda test: matrix_size(test[0]))