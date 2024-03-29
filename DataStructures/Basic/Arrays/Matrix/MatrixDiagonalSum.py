"""
https://leetcode.com/problems/matrix-diagonal-sum/

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.



Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5


Constraints:

n == mat.length == mat[i].length
1 <= n <= 100
1 <= mat[i][j] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 100 ms, faster than 94.58% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14.6 MB, less than 45.33% of Python3 online submissions for Matrix Diagonal Sum.
# class Solution:
#     def diagonalSum(self, mat: List[List[int]]) -> int:
#         n, s = len(mat), 0
#         for i in range(n):
#             s += mat[i][i] + mat[i][n-1-i]
#         if n % 2:
#             s -= mat[n//2][n//2]
#         return s


# Runtime: 104 ms, faster than 82.48% of Python3 online submissions for Matrix Diagonal Sum.
# Memory Usage: 14.7 MB, less than 14.72% of Python3 online submissions for Matrix Diagonal Sum.
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        return sum(mat[i][i] + mat[i][-i-1] for i in range(len(mat))) - (mat[len(mat)//2][len(mat)//2] if len(mat) % 2 else 0)


tests = [
    [
        [[1,2,3],
          [4,5,6],
          [7,8,9]], 25
    ],
    [
        [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]], 8
    ],
    [
        [[5]],
        5
    ]
]

run_functional_tests(Solution().diagonalSum, tests)