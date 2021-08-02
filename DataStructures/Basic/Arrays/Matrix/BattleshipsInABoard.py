"""
https://leetcode.com/problems/battleships-in-a-board/

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).



Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 68 ms, faster than 89.86% of Python3 online submissions for Battleships in a Board.
# Memory Usage: 14.6 MB, less than 94.42% of Python3 online submissions for Battleships in a Board.
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        cnt = 0
        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i-1][j] == 'X':
                    continue
                if j > 0 and board[i][j-1] == 'X':
                    continue
                cnt += 1
        return cnt


tests = [
    [
        [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]],
        2
    ],
    [
        [["."]],
        0
    ]
]

run_functional_tests(Solution().countBattleships, tests)