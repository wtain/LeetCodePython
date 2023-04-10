"""
https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/

You are given a 2D matrix of size m x n, consisting of non-negative integers. You are also given an integer k.

The value of coordinate (a, b) of the matrix is the XOR of all matrix[i][j] where 0 <= i <= a < m and 0 <= j <= b < n (0-indexed).

Find the kth largest value (1-indexed) of all the coordinates of matrix.



Example 1:

Input: matrix = [[5,2],[1,6]], k = 1
Output: 7
Explanation: The value of coordinate (0,1) is 5 XOR 2 = 7, which is the largest value.
Example 2:

Input: matrix = [[5,2],[1,6]], k = 2
Output: 5
Explanation: The value of coordinate (0,0) is 5 = 5, which is the 2nd largest value.
Example 3:

Input: matrix = [[5,2],[1,6]], k = 3
Output: 4
Explanation: The value of coordinate (1,0) is 5 XOR 1 = 4, which is the 3rd largest value.


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
0 <= matrix[i][j] <= 106
1 <= k <= m * n
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
#         n, m = len(matrix), len(matrix[0])
#         ps = [[0] * m for _ in range(n)]
#         ps[0][0] = matrix[0][0]
#         for i in range(1, n):
#             ps[i][0] = ps[i-1][0] ^ matrix[i][0]
#         for j in range(1, m):
#             ps[0][j] = ps[0][j-1] ^ matrix[0][j-1]
#         for i in range(1, n):
#             for j in range(1, m):
#                 ps[i][j] = ps[i-1][j-1] ^ ps[i-1][j] ^ ps[i][j-1] ^ matrix[i][j]
#         h = []
#         for i in range(n):
#             for j in range(m):
#                 if len(h) < k:
#                     heapq.heappush(h, ps[i][j])
#                 elif h[0] < ps[i][j]:
#                     heapq.heappop(h)
#                     heapq.heappush(h, ps[i][j])
#
#         return h[0]


# Runtime
# 3728 ms
# Beats
# 73.77%
# Memory
# 36.8 MB
# Beats
# 72.95%
class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        ps = [[0] * m for _ in range(n)]
        ps[0][0] = matrix[0][0]
        for i in range(1, n):
            ps[i][0] = ps[i-1][0] ^ matrix[i][0]
        for j in range(1, m):
            ps[0][j] = ps[0][j-1] ^ matrix[0][j]
        for i in range(1, n):
            for j in range(1, m):
                ps[i][j] = ps[i-1][j-1] ^ ps[i-1][j] ^ ps[i][j-1] ^ matrix[i][j]
        h = []
        for i in range(n):
            for j in range(m):
                if len(h) < k:
                    heapq.heappush(h, ps[i][j])
                elif h[0] < ps[i][j]:
                    heapq.heappop(h)
                    heapq.heappush(h, ps[i][j])

        return h[0]


tests = [
    [[[5,2],[1,6]], 1, 7],
    [[[5,2],[1,6]], 2, 5],
    [[[5,2],[1,6]], 3, 4],
    [[[10,9,5],[2,0,4],[1,0,9],[3,4,8]], 10, 1],
]

run_functional_tests(Solution().kthLargestValue, tests)
