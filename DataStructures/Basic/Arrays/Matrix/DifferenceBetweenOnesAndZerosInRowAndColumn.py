"""
https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/description/?envType=daily-question&envId=2023-12-14

You are given a 0-indexed m x n binary matrix grid.

A 0-indexed m x n difference matrix diff is created with the following procedure:

Let the number of ones in the ith row be onesRowi.
Let the number of ones in the jth column be onesColj.
Let the number of zeros in the ith row be zerosRowi.
Let the number of zeros in the jth column be zerosColj.
diff[i][j] = onesRowi + onesColj - zerosRowi - zerosColj
Return the difference matrix diff.



Example 1:


Input: grid = [[0,1,1],[1,0,1],[0,0,1]]
Output: [[0,0,4],[0,0,4],[-2,-2,2]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 2 + 1 - 1 - 2 = 0
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 2 + 1 - 1 - 2 = 0
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 2 + 3 - 1 - 0 = 4
- diff[2][0] = onesRow2 + onesCol0 - zerosRow2 - zerosCol0 = 1 + 1 - 2 - 2 = -2
- diff[2][1] = onesRow2 + onesCol1 - zerosRow2 - zerosCol1 = 1 + 1 - 2 - 2 = -2
- diff[2][2] = onesRow2 + onesCol2 - zerosRow2 - zerosCol2 = 1 + 3 - 2 - 0 = 2
Example 2:


Input: grid = [[1,1,1],[1,1,1]]
Output: [[5,5,5],[5,5,5]]
Explanation:
- diff[0][0] = onesRow0 + onesCol0 - zerosRow0 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[0][1] = onesRow0 + onesCol1 - zerosRow0 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[0][2] = onesRow0 + onesCol2 - zerosRow0 - zerosCol2 = 3 + 2 - 0 - 0 = 5
- diff[1][0] = onesRow1 + onesCol0 - zerosRow1 - zerosCol0 = 3 + 2 - 0 - 0 = 5
- diff[1][1] = onesRow1 + onesCol1 - zerosRow1 - zerosCol1 = 3 + 2 - 0 - 0 = 5
- diff[1][2] = onesRow1 + onesCol2 - zerosRow1 - zerosCol2 = 3 + 2 - 0 - 0 = 5


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1391
# ms
# Beats
# 58.57%
# of users with Python3
# Memory
# 52.15
# MB
# Beats
# 52.14%
# of users with Python3
# class Solution:
#     def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
#         n = len(grid)
#         m = len(grid[0])
#         diff = [[0] * m for _ in range(n)]
#         onesrow = [0] * n
#         zerosrow = [0] * n
#         onescol = [0] * m
#         zeroscol = [0] * m
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j]:
#                     onesrow[i] += 1
#                     onescol[j] += 1
#                 else:
#                     zerosrow[i] += 1
#                     zeroscol[j] += 1
#         for i in range(n):
#             for j in range(m):
#                 diff[i][j] = onesrow[i] + onescol[j] - zerosrow[i] - zeroscol[j]
#         return diff



# Runtime
# 1371
# ms
# Beats
# 72.50%
# of users with Python3
# Memory
# 49.74
# MB
# Beats
# 78.21%
# of users with Python3
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/editorial/?envType=daily-question&envId=2023-12-14
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        diff = [[0] * m for _ in range(n)]
        onesrow = [0] * n
        onescol = [0] * m
        for i in range(n):
            for j in range(m):
                onesrow[i] += grid[i][j]
                onescol[j] += grid[i][j]
        for i in range(n):
            for j in range(m):
                diff[i][j] = 2*onesrow[i] + 2*onescol[j] - n - m
        return diff


tests = [
    [[[0,1,1],[1,0,1],[0,0,1]], [[0,0,4],[0,0,4],[-2,-2,2]]],
    [[[1,1,1],[1,1,1]], [[5,5,5],[5,5,5]]],
]

run_functional_tests(Solution().onesMinusZeros, tests)
