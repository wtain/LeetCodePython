"""
https://leetcode.com/problems/largest-submatrix-with-rearrangements/description/?envType=daily-question&envId=2023-11-26

You are given a binary matrix matrix of size m x n, and you are allowed to rearrange the columns of the matrix in any order.

Return the area of the largest submatrix within matrix where every element of the submatrix is 1 after reordering the columns optimally.



Example 1:


Input: matrix = [[0,0,1],[1,1,1],[1,0,1]]
Output: 4
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
Example 2:


Input: matrix = [[1,0,1,0,1]]
Output: 3
Explanation: You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
Example 3:

Input: matrix = [[1,1,0],[1,0,1]]
Output: 2
Explanation: Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m * n <= 105
matrix[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1117
# ms
# Beats
# 32.64%
# of users with Python3
# Memory
# 42.84
# MB
# Beats
# 18.06%
# of users with Python3
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/editorial/?envType=daily-question&envId=2023-11-26
# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         result = 0
#         for row in range(m):
#             for col in range(n):
#                 if matrix[row][col] != 0 and row > 0:
#                     matrix[row][col] += matrix[row-1][col]
#             curr_row = sorted(matrix[row], reverse=True)
#             for i in range(n):
#                 result = max(result, curr_row[i] * (i+1))
#         return result


# Runtime
# 1072
# ms
# Beats
# 86.11%
# of users with Python3
# Memory
# 39.83
# MB
# Beats
# 88.19%
# of users with Python3
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/editorial/?envType=daily-question&envId=2023-11-26
# class Solution:
#     def largestSubmatrix(self, matrix: List[List[int]]) -> int:
#         m, n = len(matrix), len(matrix[0])
#         result = 0
#         prev_row = [0] * n
#         for row in range(m):
#             curr_row = matrix[row][:]
#             for col in range(n):
#                 if curr_row[col] != 0 and row > 0:
#                     curr_row[col] += prev_row[col]
#             sorted_row = sorted(curr_row, reverse=True)
#             for i in range(n):
#                 result = max(result, sorted_row[i] * (i+1))
#             prev_row = curr_row
#         return result


# Runtime
# 1106
# ms
# Beats
# 45.14%
# of users with Python3
# Memory
# 40.09
# MB
# Beats
# 73.61%
# of users with Python3
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/editorial/?envType=daily-question&envId=2023-11-26
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        result = 0
        prev_heights = []

        for row in range(m):
            heights = []
            seen = [False] * n

            for height, col in prev_heights:
                if matrix[row][col] == 1:
                    heights.append((height+1, col))
                    seen[col] = True
            for col in range(n):
                if not seen[col] and matrix[row][col] == 1:
                    heights.append((1, col))
            for i in range(len(heights)):
                result = max(result, heights[i][0] * (i+1))
            prev_heights = heights
        return result


tests = [
    [[[0,0,1],[1,1,1],[1,0,1]], 4],
    [[[1,0,1,0,1]], 3],
    [[[1,1,0],[1,0,1]], 2],
]

run_functional_tests(Solution().largestSubmatrix, tests)
