"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3720/
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
Example 2:


Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
Example 3:

Input: matrix = [[1]]
Output: [[1]]
Example 4:

Input: matrix = [[1,2],[3,4]]
Output: [[3,1],[4,2]]


Constraints:

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
"""
from typing import List

from Common.Helpers.FunctionalHelpers import make_inplace
from Common.Helpers.MatrixUtils import matrix_test_metric
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 94.83% of Python3 online submissions for Rotate Image.
# Memory Usage: 14.3 MB, less than 61.05% of Python3 online submissions for Rotate Image.
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        if not N:
            return None
        if len(matrix[0]) != N:
            return None

        N2 = N // 2
        N22 = (N+1) // 2
        N1 = N - 1
        for i in range(N22):
            for j in range(N2):
                tmp = matrix[i][j]
                matrix[j][N1 - i], tmp = tmp, matrix[j][N1 - i]
                matrix[N1 - i][N1 - j], tmp = tmp, matrix[N1 - i][N1 - j]
                matrix[N1 - j][i], tmp = tmp, matrix[N1 - j][i]
                matrix[i][j] = tmp

        """
        Do not return anything, modify matrix in-place instead.
        """
        return None


tests = [
    [
        [[1,2,3],[4,5,6],[7,8,9]],
        [[7,4,1],[8,5,2],[9,6,3]]
    ],
    [
        [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
        [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    ],
    [
        [[1]],
        [[1]]
    ],
    [
        [[1,2],[3,4]],
        [[3,1],[4,2]]
    ],
    [
        [],
        []
    ]
]


run_functional_tests(make_inplace(Solution().rotate), tests, input_metric=matrix_test_metric)