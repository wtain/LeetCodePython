"""
https://leetcode.com/problems/spiral-matrix-iv/description/?envType=daily-question&envId=2024-09-09

ou are given two integers m and n, which represent the dimensions of a matrix.

You are also given the head of a linked list of integers.

Generate an m x n matrix that contains the integers in the linked list presented in spiral order (clockwise), starting from the top-left of the matrix. If there are remaining empty spaces, fill them with -1.

Return the generated matrix.



Example 1:


Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
Explanation: The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
Example 2:


Input: m = 1, n = 4, head = [0,1,2]
Output: [[0,1,2,-1]]
Explanation: The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.


Constraints:

1 <= m, n <= 105
1 <= m * n <= 105
The number of nodes in the list is in the range [1, m * n].
0 <= Node.val <= 1000
"""
from typing import Optional, List

from Common.DataTypes.Leetcode import ListNode
from Common.ListUtils import build_list
from Common.ObjectTestingUtils import run_functional_tests


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
#         result = [[-1] * n for _ in range(m)]
#         i1, i2 = 0, m-1
#         j1, j2 = 0, n-1
#         i, j = 0, 0
#         di, dj = 0, 1
#         curr = head
#         while curr:
#             result[i][j] = curr.val
#             curr = curr.next
#             # if i + di > i2 or i + di < i1:
#             #     dj = -di
#             # if j + dj > j2 or j + dj < j1:
#             #     di = dj
#
#             i += di
#             j += dj
#             if dj == 1 and j == j2:
#                 di, dj = 1, 0
#                 i1 += 1
#             if di == 1 and i == i2:
#                 di, dj = 0, -1
#                 j2 -= 1
#             if dj == -1 and j == j1:
#                 di, dj = -1, 0
#                 i2 -= 1
#             if di == -1 and i == i1:
#                 di, dj = 0, 1
#                 j1 += 1
#
#         return result


# Runtime
# 722
# ms
# Beats
# 28.41%
# Analyze Complexity
# Memory
# 53.58
# MB
# Beats
# 100.00%
# https://leetcode.com/problems/spiral-matrix-iv/editorial/?envType=daily-question&envId=2024-09-09
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1] * n for _ in range(m)]
        i, j = 0, 0
        dir = 0
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        curr = head
        while curr:
            result[i][j] = curr.val
            di, dj = dirs[dir]
            ii, jj = i + di, j + dj
            if min(ii, jj) < 0 or ii >= m or jj >= n or result[ii][jj] != -1:
                dir = (dir + 1) % 4

            di, dj = dirs[dir]
            i += di
            j += dj
            curr = curr.next

        return result


tests = [
    [10, 1, build_list([8,24,5,21,10,11,11,12,6,17]), [[8],[24],[5],[21],[10],[11],[11],[12],[6],[17]]],
    [3, 5, build_list([3,0,2,6,8,1,7,9,4,2,5,5,0]), [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]],
    [1, 4, build_list([0,1,2]), [[0,1,2,-1]]],
]

run_functional_tests(Solution().spiralMatrix, tests)
