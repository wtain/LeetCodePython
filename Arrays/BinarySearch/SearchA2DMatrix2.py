"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3650/
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.


Example 1:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true
Example 2:


Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false


Constraints:

m == matrix.length
n == matrix[i].length
1 <= n, m <= 300
-109 <= matix[i][j] <= 109
All the integers in each row are sorted in ascending order.
All the integers in each column are sorted in ascending order.
-109 <= target <= 109
"""
from typing import List


# Runtime: 248 ms, faster than 9.23% of Python3 online submissions for Search a 2D Matrix II.
# Memory Usage: 20.5 MB, less than 68.22% of Python3 online submissions for Search a 2D Matrix II.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if not n:
            return False
        m = len(matrix[0])
        row, col = 0, m-1
        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False


tests = [
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5, True),
    ([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20, False)
]

for test in tests:
    result = Solution().searchMatrix(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
