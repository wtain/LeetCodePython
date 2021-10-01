"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3977/
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.



Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 37 ms, faster than 20.95% of Python3 online submissions for Spiral Matrix.
# Memory Usage: 14.1 MB, less than 95.10% of Python3 online submissions for Spiral Matrix.
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        if not n:
            return []
        m = len(matrix[0])
        i, j = 0, 0
        state = 0 if m > 1 else 1
        i1, j1, i2, j2 = 0, 0, n-1, m-1
        result = []
        for k in range(n*m):
            result.append(matrix[i][j])
            if state == 0:
                j += 1
                if j == j2:
                    state = 1 if i1 < i2 else 2
                    i1 += 1
            elif state == 1:
                i += 1
                if i == i2:
                    state = 2 if j1 < j2 else 3
                    j2 -= 1
            elif state == 2:
                j -= 1
                if j == j1:
                    state = 3 if i1 < i2 else 0
                    i2 -= 1
            elif state == 3:
                i -= 1
                if i == i1:
                    state = 0 if j1 < j2 else 1
                    j1 += 1
        return result


tests = [
    [
        [[2,5],[8,4],[0,-1]],
        [2,5,4,-1,0,8]
    ],
    [
        [[1,2,3],[4,5,6],[7,8,9]],
        [1,2,3,6,9,8,7,4,5]
    ],
    [
        [[1,2,3,4],[5,6,7,8],[9,10,11,12]],
        [1,2,3,4,8,12,11,10,9,5,6,7]
    ]
]

run_functional_tests(Solution().spiralOrder, tests)