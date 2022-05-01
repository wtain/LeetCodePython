"""
https://leetcode.com/problems/valid-tic-tac-toe-state/

Given a Tic-Tac-Toe board as a string array board, return true if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array that consists of characters ' ', 'X', and 'O'. The ' ' character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares ' '.
The first player always places 'X' characters, while the second player always places 'O' characters.
'X' and 'O' characters are always placed into empty squares, never filled ones.
The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.


Example 1:


Input: board = ["O  ","   ","   "]
Output: false
Explanation: The first player always plays "X".
Example 2:


Input: board = ["XOX"," X ","   "]
Output: false
Explanation: Players take turns making moves.
Example 3:


Input: board = ["XOX","O O","XOX"]
Output: true


Constraints:

board.length == 3
board[i].length == 3
board[i][j] is either 'X', 'O', or ' '.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def validTicTacToe(self, board: List[str]) -> bool:
#         nx, no = 0, 0
#         for line in board:
#             for c in line:
#                 if c == 'X':
#                     nx += 1
#                 elif c == 'O':
#                     no += 1
#         if not 0 <= nx-no <= 1:
#             return False
#         if board[0][0] == board[1][1] == board[2][2]:
#             if board[0][0] == 'O':
#                 return no == nx
#             if board[0][0] == 'X':
#                 return no == nx-1
#         if board[2][0] == board[1][1] == board[2][0]:
#             if board[2][0] == 'O':
#                 return no == nx
#             if board[2][0] == 'X':
#                 return no == nx-1
#         nh, nv = 0, 0
#         for line in board:
#             if line[0] == ' ':
#                 continue
#             if line[0] == line[1] == line[2]:
#                 nh += 1
#                 if line[0] == 'X' and nx == no:
#                     return False
#         if nh > 1:
#             return False
#         for i in range(3):
#             if board[0][i] == ' ':
#                 continue
#             if board[0][i] == board[1][i] == board[2][i]:
#                 nv += 1
#         return nv <= 1


# Runtime: 34 ms, faster than 77.36% of Python3 online submissions for Valid Tic-Tac-Toe State.
# Memory Usage: 13.9 MB, less than 44.98% of Python3 online submissions for Valid Tic-Tac-Toe State.
# https://leetcode.com/problems/valid-tic-tac-toe-state/discuss/1985927/Clean-Python-solution-with-explanation
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        cnt = Counter("".join(board))
        wins_search_space = board + \
                            list("".join(x) for x in zip(*board)) + \
                            [
                                "".join(board[i][i] for i in range(3)),
                                "".join(board[i][2-i] for i in range(3))
                            ]
        x_wins = "XXX" in wins_search_space
        o_wins = "OOO" in wins_search_space
        if x_wins and o_wins:
            return False
        elif x_wins:
            return cnt["X"] - cnt["O"] == 1
        elif o_wins:
            return cnt["X"] - cnt["O"] == 0
        else:
            return 0 <= cnt["X"] - cnt["O"] <= 1


tests = [
    [["O  ","   ","   "], False],
    [["XOX"," X ","   "], False],
    [["XOX","O O","XOX"], True],
    [["OOO","XXX","   "], False],
    [["XXX","OOX","OOX"], True],
    [["XXX",
      "XOO",
      "OO "], False],
    [["OXX",
      "XOX",
      "OXO"], False]
]

# run_functional_tests(Solution().validTicTacToe, tests, run_tests=5)
run_functional_tests(Solution().validTicTacToe, tests)
