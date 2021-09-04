"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/612/week-5-july-29th-july-31st/3831/
https://leetcode.com/problems/01-matrix/

Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.



Example 1:


Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
Example 2:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
There is at least one 0 in mat.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 564 ms, faster than 89.77% of Python3 online submissions for 01 Matrix.
# Memory Usage: 17.3 MB, less than 53.89% of Python3 online submissions for 01 Matrix.
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        if not n:
            return []
        m = len(mat[0])
        bigval = n*m
        result = [[bigval] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    result[i][j] = 0
                else:
                    if i > 0:
                        result[i][j] = min(result[i][j], result[i-1][j] + 1)
                    if j > 0:
                        result[i][j] = min(result[i][j], result[i][j-1] + 1)

        for i1 in range(n):
            i = n-1-i1
            for j1 in range(m):
                j = m - 1 - j1
                if not mat[i][j]:
                    result[i][j] = 0
                else:
                    if i1 > 0:
                        result[i][j] = min(result[i][j], result[i+1][j] + 1)
                    if j1 > 0:
                        result[i][j] = min(result[i][j], result[i][j+1] + 1)

        return result


tests = [
    [
        [[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]],
        [[0,1,0,1,2],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]]
    ],
    [
        [[0,0,0],[0,1,0],[0,0,0]],
        [[0,0,0],[0,1,0],[0,0,0]]
    ],
    [
        [[0,0,0],[0,1,0],[1,1,1]],
        [[0,0,0],[0,1,0],[1,2,1]]
    ]
]

run_functional_tests(Solution().updateMatrix, tests)