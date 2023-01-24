"""
https://leetcode.com/problems/snakes-and-ladders/description/

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 do not have a snake or ladder.

Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of moves required to reach the square n2. If it is not possible to reach the square, return -1.



Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation:
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1


Constraints:

n == board.length == board[i].length
2 <= n <= 20
grid[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 do not have any ladders or snakes.
"""
import random
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 352 ms
# Beats
# 13.64%
# Memory
# 13.9 MB
# Beats
# 93.18%
# class Solution:
#     def snakesAndLadders(self, board: List[List[int]]) -> int:
#
#         # get_index(number) -> (i, j)
#         # move()
#
#         n, m = len(board), len(board[0])
#         k = n * m
#         line = [0] * k
#         i, j = n-1, 0
#         dj = 1
#         for c in range(k):
#             line[c] = board[i][j]-1 if board[i][j] != -1 else -1
#             j1 = j + dj
#             if j1 == m or j1 == -1:
#                 dj = -dj
#                 i -= 1
#             else:
#                 j += dj
#
#         level = [0]
#         moves = 0
#         visited = set()
#         while level:
#             next_level = []
#             for i in level:
#                 if i == k-1:
#                     return moves
#                 for next_i in range(i+1, min(k-1, i+6)+1):
#                     if next_i >= k:
#                         break
#                     if next_i in visited:
#                         continue
#                     visited.add(next_i)
#                     if line[next_i] != -1 and next_i != 0 and next_i != k-1:
#                         next_i = line[next_i]
#                     next_level.append(next_i)
#             moves += 1
#             level = next_level
#         return -1


# Runtime
# 114 ms
# Beats
# 89.21%
# Memory
# 13.8 MB
# Beats
# 99.79%
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        def get_indexes(index: int, n: int) -> (int, int):
            i1 = index // n
            i = n-1 - i1
            if i1 % 2 == 0:
                j = index % n
            else:
                j = n-1 - index % n
            return i, j

        n = len(board)
        k = n ** 2

        def get_value(index: int) -> int:
            nonlocal board, n
            i, j = get_indexes(index, n)
            value = board[i][j]
            return value-1 if value != -1 else -1

        level = [0]
        moves = 0
        visited = set()
        while level:
            next_level = []
            for i in level:
                if i == k-1:
                    return moves
                for next_i in range(i+1, min(k-1, i+6)+1):
                    if next_i >= k:
                        break
                    if next_i in visited:
                        continue
                    visited.add(next_i)
                    next_value = get_value(next_i)
                    if next_value != -1 and next_i != 0 and next_i != k-1:
                        next_i = next_value
                    next_level.append(next_i)
            moves += 1
            level = next_level
        return -1


tests = [
    [
        [
            [-1,1,2,-1],
            [2,13,15,-1],
            [-1,10,-1,-1],
            [-1,6,2,8]
        ],
        2
    ],
    [
        [
            [-1,7,-1],
            [-1,6,9],
            [-1,-1,2]
        ],
        1
    ],
    [
        [
            [-1,-1,-1],
            [-1,9,8],
            [-1,8,9]
        ],
        1
    ],
    [
        [
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ],
        4
    ],
    [
        [
            [-1,-1],
            [-1,3]
        ],
        1
    ],
]

# run_functional_tests(Solution().snakesAndLadders, tests, run_tests=3)
run_functional_tests(Solution().snakesAndLadders, tests)
