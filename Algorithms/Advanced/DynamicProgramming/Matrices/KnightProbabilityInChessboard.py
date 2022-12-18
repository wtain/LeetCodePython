"""
https://leetcode.com/problems/knight-probability-in-chessboard/

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.


Each time the knight is to move, it chooses one of eight possible moves uniformly at random (even if the piece would go off the chessboard) and moves there.

The knight continues moving until it has made exactly k moves or has moved off the chessboard.

Return the probability that the knight remains on the board after it has stopped moving.



Example 1:

Input: n = 3, k = 2, row = 0, column = 0
Output: 0.06250
Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight on the board.
From each of those positions, there are also two moves that will keep the knight on the board.
The total probability the knight stays on the board is 0.0625.
Example 2:

Input: n = 1, k = 0, row = 0, column = 0
Output: 1.00000


Constraints:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n - 1
"""
from itertools import product

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#
#         neighbors = [
#             (-1, -2), (-2, -1),
#             ( 1, -2), (-2,  1),
#             (-1,  2), ( 2, -1),
#             ( 1,  2), ( 2,  1),
#         ]
#         choice_probability = 1.0 / len(neighbors)
#
#         states = [(row, column, 1.0)]
#         for i in range(k):
#             next_level = []
#             for r, c, probability in states:
#                 for dr, dc in neighbors:
#                     next_level.append((r+dr, c+dc, probability*choice_probability))
#             states = next_level
#
#         def is_in_grid(r, c):
#             return 0 <= r < n and 0 <= c < n
#
#         return sum(probability for r, c, probability in states if is_in_grid(r, c))


# MLE
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#
#         neighbors = [
#             (-1, -2), (-2, -1),
#             ( 1, -2), (-2,  1),
#             (-1,  2), ( 2, -1),
#             ( 1,  2), ( 2,  1),
#         ]
#         choice_probability = 1.0 / len(neighbors)
#
#         def is_in_grid(r, c):
#             return 0 <= r < n and 0 <= c < n
#
#         states = [(row, column, 1.0)]
#         for i in range(k):
#             next_level = []
#             for r0, c0, probability in states:
#                 for dr, dc in neighbors:
#                     r, c = r0 + dr, c0 + dc
#                     if is_in_grid(r, c):
#                         next_level.append((r, c, probability*choice_probability))
#             states = next_level
#
#         return sum(probability for r, c, probability in states)


# UNFINISHED
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#
#         neighbors = [
#             (-1, -2), (-2, -1),
#             ( 1, -2), (-2,  1),
#             (-1,  2), ( 2, -1),
#             ( 1,  2), ( 2,  1),
#         ]
#         choice_probability = 1.0 / len(neighbors)
#
#         def is_in_grid(r, c):
#             return 0 <= r < n and 0 <= c < n
#
#         dp = [[0] * n for _ in range(n)]
#         for r, c in product(range(n), range(n)):
#             pass
#
#         states = [(row, column, 1.0)]
#         for i in range(k):
#             next_level = []
#             for r0, c0, probability in states:
#                 for dr, dc in neighbors:
#                     r, c = r0 + dr, c0 + dc
#                     if is_in_grid(r, c):
#                         next_level.append((r, c, probability*choice_probability))
#             states = next_level
#
#         return sum(probability for r, c, probability in states)


# Runtime
# 1629 ms
# Beats
# 5.8%
# Memory
# 13.9 MB
# Beats
# 90.2%
# https://leetcode.com/problems/knight-probability-in-chessboard/solutions/127573/knight-probability-in-chessboard/
# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         dp = [[0] * n for _ in range(n)]
#         dp[row][column] = 1
#         neighbors = [
#             (-1, -2), (-2, -1),
#             ( 1, -2), (-2,  1),
#             (-1,  2), ( 2, -1),
#             ( 1,  2), ( 2,  1),
#         ]
#
#         def is_in_grid(r, c):
#             return 0 <= r < n and 0 <= c < n
#
#         for _ in range(k):
#             dp2 = [[0] * n for _ in range(n)]
#             for r, c in product(range(n), range(n)):
#                 for dr, dc in neighbors:
#                     if is_in_grid(r+dr, c+dc):
#                         dp2[r+dr][c+dc] += dp[r][c] / 8.0
#             dp = dp2
#         return sum(map(sum, dp))


# Runtime
# 3481 ms
# Beats
# 5.8%
# Memory
# 14.9 MB
# Beats
# 60.6%
class Solution:
    def knightProbability(self, n: int, k: int, r0: int, c0: int) -> float:
        def canonical(r, c):
            if 2 * r > n: r = n - 1 - r
            if 2 * c > n: c = n - 1 - c
            if r > c: r, c = c, r
            return r*n+c

        def matrix_mult(A, B):
            ZB = list(zip(*B))
            return [[sum(a*b for a,b in zip(row, col)) for col in ZB] for row in A]

        def matrix_expo(A, K):
            if K == 0:
                return [[+(i==j) for j in range(len(A))] for i in range(len(A))]
            if K == 1:
                return A
            elif K % 2:
                return matrix_mult(matrix_expo(A, K-1), A)
            B = matrix_expo(A, K // 2)
            return matrix_mult(B, B)

        neighbors = [
            (-1, -2), (-2, -1),
            ( 1, -2), (-2,  1),
            (-1,  2), ( 2, -1),
            ( 1,  2), ( 2,  1),
        ]

        def is_in_grid(r, c):
            return 0 <= r < n and 0 <= c < n

        index = [0] * (n*n)
        t = 0
        for r, c in product(range(n), range(n)):
            if r*n+c == canonical(r, c):
                index[r*n+c] = t
                t += 1
            else:
                index[r*n+c] = index[canonical(r, c)]

        T = []
        for r, c in product(range(n), range(n)):
            if r * n + c == canonical(r, c):
                row = [0] * t
                for dr, dc in neighbors:
                    if is_in_grid(r+dr, c+dc):
                        row[index[(r+dr)*n+c+dc]] += 0.125
                T.append(row)

        Tk = matrix_expo(T, k)
        i = index[r0 * n + c0]
        return sum(Tk[i])


tests = [
    [3, 2, 0, 0, 0.06250],
    [1, 0, 0, 0, 1.00000],
    [8, 30, 6, 4, 0.00019]
]

# run_functional_tests(Solution().knightProbability, tests, run_tests=3)
run_functional_tests(Solution().knightProbability, tests)
