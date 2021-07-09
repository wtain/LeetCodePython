"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3803/
https://leetcode.com/problems/reshape-the-matrix/

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the row number and column number of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.



Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 84 ms, faster than 84.71% of Python3 online submissions for Reshape the Matrix.
# Memory Usage: 15 MB, less than 62.07% of Python3 online submissions for Reshape the Matrix.
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len((mat[0]))
        if n*m != r*c:
            return mat
        result = [[0] * c for _ in range(r)]
        y, x = 0, 0
        for i in range(n):
            for j in range(m):
                result[y][x] = mat[i][j]
                x += 1
                if x == c:
                    x = 0
                    y += 1
        return result


tests = [
    [[[1,2],[3,4]], 1, 4, [[1,2,3,4]]],
    [[[1,2],[3,4]], 2, 4, [[1,2],[3,4]]],
]

run_functional_tests(Solution().matrixReshape, tests)