"""
https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.



Example 1:


Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
Example 2:


Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.


Constraints:

1 <= n <= 50
1 <= m <= 50
1 <= indices.length <= 100
0 <= indices[i][0] < n
0 <= indices[i][1] < m
"""
from typing import List

# Runtime: 64 ms, faster than 17.22% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 14.4 MB, less than 47.36% of Python3 online submissions for Cells with Odd Values in a Matrix.
# class Solution:
#     def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
#         cols = [0] * n
#         rows = [0] * m
#         for r, c in indices:
#             cols[r] += 1
#             rows[c] += 1
#         cnt = 0
#         for r in range(n):
#             for c in range(m):
#                 if (cols[r] + rows[c]) % 2 == 1:
#                     cnt += 1
#         return cnt


# Runtime: 60 ms, faster than 20.36% of Python3 online submissions for Cells with Odd Values in a Matrix.
# Memory Usage: 14.5 MB, less than 18.41% of Python3 online submissions for Cells with Odd Values in a Matrix.
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        cols = [0] * n
        rows = [0] * m
        for r, c in indices:
            cols[r] ^= 1
            rows[c] ^= 1
        cnt = 0
        for r in range(n):
            for c in range(m):
                if cols[r] ^ rows[c] == 1:
                    cnt += 1
        return cnt


tests = [
    (28, 38, [[17,16],[26,31],[19,12],[22,24],[17,28],[23,21],[27,32],[23,27],[23,33],[18,7],[4,20],[0,31],[25,33],[5,22]], 460),

    (2, 3, [[0,1],[1,1]], 6),
    (2, 2, [[1,1],[0,0]], 0),
]

for test in tests:
    result = Solution().oddCells(test[0], test[1], test[2])
    if result == test[3]:
        print("PASS")
    else:
        print("FAIL - " + str(result))