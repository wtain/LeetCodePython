"""
https://leetcode.com/problems/minesweeper/

Let's play the minesweeper game (Wikipedia, online game)!

You are given an m x n char matrix board representing the game board where:

'M' represents an unrevealed mine,
'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent mines (i.e., above, below, left, right, and all 4 diagonals),
digit ('1' to '8') represents how many mines are adjacent to this revealed square, and
'X' represents a revealed mine.
You are also given an integer array click where click = [clickr, clickc] represents the next click position among all the unrevealed squares ('M' or 'E').

Return the board after revealing this position according to the following rules:

If a mine 'M' is revealed, then the game is over. You should change it to 'X'.
If an empty square 'E' with no adjacent mines is revealed, then change it to a revealed blank 'B' and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square 'E' with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.


Example 1:


Input: board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
Output: [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
Example 2:


Input: board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
Output: [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 50
board[i][j] is either 'M', 'E', 'B', or a digit from '1' to '8'.
click.length == 2
0 <= clickr < m
0 <= clickc < n
board[clickr][clickc] is either 'M' or 'E'.
"""
import copy
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 716 ms
# Beats
# 5.4%
# Memory
# 19.5 MB
# Beats
# 5.53%
# class Solution:
#     def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
#         n, m = len(board), len(board[0])
#         i, j = click
#
#         def reveal(i: int, j: int):
#             nonlocal n, m
#             board[i][j] = 'B'
#             neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
#             n_mines = 0
#             to_reveal = []
#             for di, dj in neighbors:
#                 i1, j1 = i + di, j + dj
#                 if i1 < 0 or i1 >= n or j1 < 0 or j1 >= m:
#                     continue
#                 if board[i1][j1] == 'M':
#                     n_mines += 1
#                 elif board[i1][j1] == 'E':
#                     to_reveal.append([i1, j1])
#             if n_mines > 0:
#                 board[i][j] = str(n_mines)
#             else:
#                 for i1, j1 in to_reveal:
#                     reveal(i1, j1)
#
#         if board[i][j] == 'M':
#             board[i][j] = 'X'
#         elif board[i][j] == 'E':
#             reveal(i, j)
#
#         return board


# Runtime
# 552 ms
# Beats
# 16.67%
# Memory
# 14.6 MB
# Beats
# 72.61%
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        n, m = len(board), len(board[0])
        i, j = click

        def reveal(i0: int, j0: int):
            nonlocal n, m
            to_reveal = [[i0, j0]]
            while to_reveal:
                i, j = to_reveal.pop()
                board[i][j] = 'B'
                neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
                n_mines = 0
                to_reveal_next = []
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if i1 < 0 or i1 >= n or j1 < 0 or j1 >= m:
                        continue
                    if board[i1][j1] == 'M':
                        n_mines += 1
                    elif board[i1][j1] == 'E':
                        to_reveal_next.append([i1, j1])
                if n_mines > 0:
                    board[i][j] = str(n_mines)
                else:
                    to_reveal += to_reveal_next

        if board[i][j] == 'M':
            board[i][j] = 'X'
        elif board[i][j] == 'E':
            reveal(i, j)

        return board


tests = [
    [
        [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]],
        [3,0],
        [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    ],
    [
        [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]],
        [1,2],
        [["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]
    ]
]

run_functional_tests(Solution().updateBoard, tests)
