"""
https://leetcode.com/problems/check-if-every-row-and-column-contains-all-numbers/

An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.



Example 1:


Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.
Example 2:


Input: matrix = [[1,1,1],[1,2,3],[1,2,3]]
Output: false
Explanation: In this case, n = 3, but the first row and the first column do not contain the numbers 2 or 3.
Hence, we return false.


Constraints:

n == matrix.length == matrix[i].length
1 <= n <= 100
1 <= matrix[i][j] <= n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1390 ms, faster than 19.11% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
# Memory Usage: 14.5 MB, less than 44.28% of Python3 online submissions for Check if Every Row and Column Contains All Numbers.
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n):
            c, r = set(), set()
            for j in range(n):
                if matrix[i][j] <= 0 or matrix[i][j] > n:
                    return False
                r.add(matrix[i][j])
                c.add(matrix[j][i])
            if len(c) < n or len(r) < n:
                return False
        return True


tests = [
    [[[1]], True],
    [[[1,2,3],[3,1,2],[2,3,1]], True],
    [[[1,1,1],[1,2,3],[1,2,3]], False]
]

run_functional_tests(Solution().checkValid, tests)
