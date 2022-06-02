"""
https://leetcode.com/problems/transpose-matrix/

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.





Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 116 ms, faster than 31.50% of Python3 online submissions for Transpose Matrix.
# Memory Usage: 14.8 MB, less than 55.33% of Python3 online submissions for Transpose Matrix.
# https://leetcode.com/submissions/detail/338428994/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        result = [[0] * n for _ in range(m)]
        for i in range(n):
            for j in range(m):
                result[j][i] = matrix[i][j]
        return result


tests = [
    [[[1,2,3],[4,5,6],[7,8,9]], [[1,4,7],[2,5,8],[3,6,9]]],
    [[[1,2,3],[4,5,6]], [[1,4],[2,5],[3,6]]]
]

run_functional_tests(Solution().transpose, tests)
