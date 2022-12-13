"""
https://leetcode.com/problems/minimum-falling-path-sum/description/

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).



Example 1:


Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
Example 2:


Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is shown.


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 410 ms
# Beats
# 20.25%
# Memory
# 14.6 MB
# Beats
# 91.12%
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        prev = [matrix[0][j] for j in range(m)]
        for i in range(1, n):
            row = [0] * m
            for j in range(m):
                row[j] = prev[j] + matrix[i][j]
                if j > 0:
                    row[j] = min(row[j], prev[j-1] + matrix[i][j])
                if j < m-1:
                    row[j] = min(row[j], prev[j+1] + matrix[i][j])
            prev = row
        return min(prev)


tests = [
    [[[2,1,3],[6,5,4],[7,8,9]], 13],
    [[[-19,57],[-40,-5]], -59]
]

run_functional_tests(Solution().minFallingPathSum, tests)
