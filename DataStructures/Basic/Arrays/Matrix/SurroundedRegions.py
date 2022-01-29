"""
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.



Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.FunctionalHelpers import make_inplace


# Runtime: 140 ms, faster than 71.97% of Python3 online submissions for Surrounded Regions.
# Memory Usage: 15.3 MB, less than 98.97% of Python3 online submissions for Surrounded Regions.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        n, m = len(board), len(board[0])
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def mark(i: int, j: int):
            nonlocal n, m, board, neighbors
            to_visit = [(i, j)]
            while to_visit:
                i, j = to_visit.pop()
                board[i][j] = 'B'
                for neigh in neighbors:
                    i1, j1 = i + neigh[0], j + neigh[1]
                    if 0 <= i1 < n and 0 <= j1 < m and board[i1][j1] == 'O':
                        to_visit.append((i1, j1))

        for i in range(n):
            if board[i][0] == 'O':
                mark(i, 0)
            if board[i][m-1] == 'O':
                mark(i, m-1)

        for j in range(m):
            if board[0][j] == 'O':
                mark(0, j)
            if board[n-1][j] == 'O':
                mark(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'B':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'


tests = [
    [
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    ],
    [
        [["X"]],
        [["X"]]
    ]
]

run_functional_tests(make_inplace(Solution().solve), tests)
