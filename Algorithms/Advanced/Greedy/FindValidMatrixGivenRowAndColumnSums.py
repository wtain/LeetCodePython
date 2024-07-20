"""
https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/description/?envType=daily-question&envId=2024-07-20

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.



Example 1:

Input: rowSum = [3,8], colSum = [4,7]
Output: [[3,0],
         [1,7]]
Explanation:
0th row: 3 + 0 = 3 == rowSum[0]
1st row: 1 + 7 = 8 == rowSum[1]
0th column: 3 + 1 = 4 == colSum[0]
1st column: 0 + 7 = 7 == colSum[1]
The row and column sums match, and all matrix elements are non-negative.
Another possible matrix is: [[1,2],
                             [3,5]]
Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]


Constraints:

1 <= rowSum.length, colSum.length <= 500
0 <= rowSum[i], colSum[i] <= 108
sum(rowSum) == sum(colSum)
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 548
# ms
# Beats
# 67.87%
# Analyze Complexity
# Memory
# 21.72
# MB
# Beats
# 53.07%
# class Solution:
#     def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
#         n, m = len(rowSum), len(colSum)
#         result = [[0] * m for _ in range(n)]
#         for i in range(n):
#             for j in range(m):
#                 x = min(rowSum[i], colSum[j])
#                 result[i][j] = x
#                 rowSum[i] -= x
#                 colSum[j] -= x
#         return result


# Runtime
# 371
# ms
# Beats
# 89.53%
# Analyze Complexity
# Memory
# 21.73
# MB
# Beats
# 53.07%
# Analyze Complexity
# https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/editorial/?envType=daily-question&envId=2024-07-20
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        result = [[0] * m for _ in range(n)]
        i = j = 0
        while i < n and j < m:
            result[i][j] = min(rowSum[i], colSum[j])
            rowSum[i] -= result[i][j]
            colSum[j] -= result[i][j]
            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        return result


tests = [
    [[3,8], [4,7], [[3,0],[1,7]]],
    [[5,7,10], [8,6,8], [[0,5,0], [6,1,0], [2,0,8]]],
]


def customCheck(test, result) -> bool:
    rowSumExpected, colSumExpected = test[0], test[1]
    n, m = len(result), len(result[0])
    rowSum, colSum = [0] * n, [0] * m
    for i in range(n):
        for j in range(m):
            rowSum[i] += result[i][j]
            colSum[j] += result[i][j]
    return rowSum == rowSumExpected and colSum == colSumExpected



run_functional_tests(Solution().restoreMatrix, tests, custom_check=customCheck)
