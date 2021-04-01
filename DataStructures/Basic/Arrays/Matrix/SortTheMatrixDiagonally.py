"""
https://leetcode.com/problems/sort-the-matrix-diagonally/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3614/
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.



Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
"""
from collections import defaultdict
from typing import List


# Runtime: 152 ms, faster than 7.36% of Python3 online submissions for Sort the Matrix Diagonally.
# Memory Usage: 14.7 MB, less than 25.18% of Python3 online submissions for Sort the Matrix Diagonally.
# class Solution:
#     def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
#         n = len(mat)
#         m = len(mat[0])
#         result = [[0] * m for i in range(n)]
#         d = n + m + 1
#         v = 101
#         i0 = n-1
#         j0 = 0
#         for i in range(d):
#             counts = [0] * v
#             i1 = i0
#             j1 = j0
#             while i1 < n and j1 < m:
#                 counts[mat[i1][j1]] += 1
#                 i1 += 1
#                 j1 += 1
#             i1 = i0
#             j1 = j0
#             k = 0
#             while i1 < n and j1 < m:
#                 while not counts[k]:
#                     k += 1
#                 result[i1][j1] = k
#                 counts[k] -= 1
#                 i1 += 1
#                 j1 += 1
#             if i0 == 0:
#                 j0 += 1
#             else:
#                 i0 -= 1
#         return result
from sortedcontainers import SortedDict


# Runtime: 192 ms, faster than 5.15% of Python3 online submissions for Sort the Matrix Diagonally.
# Memory Usage: 15.3 MB, less than 9.17% of Python3 online submissions for Sort the Matrix Diagonally.
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])
        result = [[0] * m for i in range(n)]
        d = n + m + 1
        i0 = n-1
        j0 = 0
        for i in range(d):
            counts = SortedDict()
            i1 = i0
            j1 = j0
            while i1 < n and j1 < m:
                v = mat[i1][j1]
                counts[v] = (counts.get(v) or 0) + 1
                i1 += 1
                j1 += 1
            i1 = i0
            j1 = j0
            k = 0
            while i1 < n and j1 < m:
                k = counts.keys()[0]
                result[i1][j1] = k
                counts[k] -= 1
                if not counts[k]:
                    counts.pop(k)
                i1 += 1
                j1 += 1
            if i0 == 0:
                j0 += 1
            else:
                i0 -= 1
        return result



tests = [
    ([[3,3,1,1],[2,2,1,2],[1,1,1,2]], [[1,1,1,1],[1,2,2,2],[1,2,3,3]])
]

for test in tests:
    result = Solution().diagonalSort(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))