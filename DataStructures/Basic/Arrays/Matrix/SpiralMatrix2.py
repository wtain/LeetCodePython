"""
https://leetcode.com/problems/spiral-matrix-ii/

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.



Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]


Constraints:

1 <= n <= 20
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 38 ms, faster than 72.82% of Python3 online submissions for Spiral Matrix II.
# Memory Usage: 13.9 MB, less than 41.06% of Python3 online submissions for Spiral Matrix II.
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        i, j = 0, 0
        state = 0 if n > 1 else 1
        i1, i2 = 0, n - 1
        j1, j2 = 0, n - 1
        for k in range(n*n):
            result[i][j] = k+1
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
    [3, [[1,2,3],[8,9,4],[7,6,5]]],
    [1, [[1]]]
]

run_functional_tests(Solution().generateMatrix, tests)
