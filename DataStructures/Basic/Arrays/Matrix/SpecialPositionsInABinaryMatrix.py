"""
https://leetcode.com/problems/special-positions-in-a-binary-matrix/

Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and columns are 0-indexed).



Example 1:

Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
Example 2:

Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions.
Example 3:

Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2
Example 4:

Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3


Constraints:

rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
"""
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 164 ms, faster than 68.93% of Python3 online submissions for Special Positions in a Binary Matrix.
# Memory Usage: 14.4 MB, less than 92.09% of Python3 online submissions for Special Positions in a Binary Matrix.
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        rows = [0] * n
        cols = [0] * m
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        return sum(1 for i, j in product(range(n), range(m)) if mat[i][j] and rows[i] == 1 and cols[j] == 1)


tests = [
    [[[1,0,0],
              [0,0,1],
              [1,0,0]], 1],
    [[[1,0,0],
              [0,1,0],
              [0,0,1]], 3],
    [[[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]], 2],
    [[[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]], 3]
]

run_functional_tests(Solution().numSpecial, tests)