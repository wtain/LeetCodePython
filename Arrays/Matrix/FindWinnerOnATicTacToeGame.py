"""
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player A always places "X" characters, while the second player B always places "O" characters.
"X" and "O" characters are always placed into empty squares, never on filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.



Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"
Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO "
"   "    "   "    "   "    "   "    "   "    "O  "
Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"
Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "


Constraints:

1 <= moves.length <= 9
moves[i].length == 2
0 <= moves[i][j] <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""
from typing import List


# Runtime: 32 ms, faster than 71.45% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
# Memory Usage: 14.3 MB, less than 42.62% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
# class Solution:
#     def tictactoe(self, moves: List[List[int]]) -> str:
#         field = [[' '] * 3 for i in range(3)]
#         turn = 0
#         for (i, j) in moves:
#             field[i][j] = 'A' if turn == 0 else 'B'
#             turn = 1 - turn
#
#         def checkWin(i: int, j: int, di: int, dj: int, ch: str) -> bool:
#             nonlocal field
#             for k in range(3):
#                 if field[i][j] != ch:
#                     return False
#                 i += di
#                 j += dj
#             return True
#
#         def checkWinAll(ch: str) -> bool:
#             checks = [
#                 [0, 0, 1, 0],
#                 [0, 0, 0, 1],
#                 [0, 1, 1, 0],
#                 [1, 0, 0, 1],
#                 [0, 2, 1, 0],
#                 [2, 0, 0, 1],
#                 [0, 0, 1, 1],
#                 [2, 0, -1, 1],
#             ]
#             nonlocal field
#             for check in checks:
#                 if checkWin(check[0], check[1], check[2], check[3], ch):
#                     return True
#             return False
#
#         if checkWinAll('A'):
#             return "A"
#         if checkWinAll('B'):
#             return "B"
#
#         return "Draw" if len(moves) == 9 else "Pending"


# Runtime: 24 ms, faster than 97.68% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
# Memory Usage: 14.2 MB, less than 90.98% of Python3 online submissions for Find Winner on a Tic Tac Toe Game.
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        turn = 1
        cols = [0] * 3
        rows = [0] * 3
        diag = [0] * 2
        for (i, j) in moves:
            cols[j] += turn
            rows[i] += turn
            if i == j:
                diag[0] += turn
            if i + j == 2:
                diag[1] += turn
            if cols[j] == 3 or rows[i] == 3 or 3 in diag:
                return "A"
            if cols[j] == -3 or rows[i] == -3 or -3 in diag:
                return "B"
            turn = -turn

        return "Draw" if len(moves) == 9 else "Pending"


tests = [
    ([[1,2],[2,1],[1,0],[0,0],[0,1],[2,0],[1,1]], "A"),

    ([[0,0],[2,0],[1,1],[2,1],[2,2]], "A"),
    ([[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]], "B"),
    ([[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]], "Draw"),
    ([[0,0],[1,1]], "Pending")
]

for test in tests:
    result = Solution().tictactoe(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + result)