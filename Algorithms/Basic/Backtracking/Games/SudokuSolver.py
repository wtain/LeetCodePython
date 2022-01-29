"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/615/week-3-august-15th-august-21st/3905/
https://leetcode.com/problems/sudoku-solver/

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.



Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
Explanation: The input board is shown above and the only valid solution is shown below:




Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.
"""
from typing import List

from Common.Helpers.MatrixUtils import make_matrix_values_test_metric
from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.FunctionalHelpers import make_inplace


# Runtime: 118 ms, faster than 84.12% of Python3 online submissions for Sudoku Solver.
# Memory Usage: 14.6 MB, less than 13.17% of Python3 online submissions for Sudoku Solver.
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        cols, rows, cells = [0] * 9, [0] * 9, [0] * 9
        n_empty = 81
        # hl = set()  # DBG

        def value_to_bit(v):
            return 1 << (v-1)

        def cell_from_indexes(i, j):
            ci, cj = i // 3, j // 3
            return 3 * ci + cj

        def setv(i, j, v):
            nonlocal cols, rows, cells, n_empty, board
            # nonlocal hl  # DBG
            ck = cell_from_indexes(i, j)
            bit = value_to_bit(v)
            cols[j] = cols[j] | bit
            rows[i] = rows[i] | bit
            cells[ck] = cells[ck] | bit
            n_empty -= 1
            # hl.add((i, j))  # DBG

        def unsetv(i, j, v):
            nonlocal cols, rows, cells, n_empty, board
            ck = cell_from_indexes(i, j)
            bit = value_to_bit(v)
            cols[j] -= bit
            rows[i] -= bit
            cells[ck] -= bit
            n_empty += 1

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                setv(i, j, int(board[i][j]))

        def solve():
            nonlocal n_empty, board, cols, rows, cells
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    ck = cell_from_indexes(i, j)
                    mask = cols[j] | rows[i] | cells[ck]
                    maskb = bin(mask)[2:].zfill(9)
                    cnt = maskb.count("1")
                    if cnt == 8:
                        v = 9 - maskb.find("0")
                        board[i][j] = str(v)
                        setv(i, j, v)

            for i in range(9):
                for v in range(1, 10):
                    bit = value_to_bit(v)
                    columns = set()
                    for j in range(9):
                        if str(v) == board[i][j]:
                            continue
                        if cols[j] & bit:
                            continue
                        if rows[i] & bit:
                            continue
                        if cells[cell_from_indexes(i, j)] & bit:
                            continue
                        columns.add(j)
                    if len(columns) == 1:
                        j = list(columns)[0]
                        board[i][j] = str(v)
                        setv(i, j, v)

            # for j in range(9):
            #     for v in range(1, 10):
            #         bit = value_to_bit(v)
            #         rowss = set()
            #         for i in range(9):
            #             if str(v) == board[i][j]:
            #                 continue
            #             if cols[j] & bit:
            #                 continue
            #             if rows[i] & bit:
            #                 continue
            #             if cells[cell_from_indexes(i, j)] & bit:
            #                 continue
            #             rowss.add(i)
            #         if len(rowss) == 1:
            #             i = list(rowss)[0]
            #             board[i][j] = str(v)
            #             setv(i, j, v)


        # printMatrix(board)  # DBG
        # print()  # DBG

        while n_empty:
            # hl = set()  # DBG
            n_empty_prev = n_empty
            solve()
            if n_empty_prev == n_empty:
                # print(n_empty)
                break
            # printMatrix(board, highlight=hl)  # DBG
            # print()  # DBG

        free_cells = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    continue
                ck = cell_from_indexes(i, j)
                mask = cols[j] | rows[i] | cells[ck]
                mask1 = 1

                values = []
                for u in range(1, 10):
                    if not mask & mask1:
                        values.append(u)
                    mask1 <<= 1
                # print(i, j, values)
                free_cells.append([len(values), i, j, values])
        free_cells.sort()
        # print(free_cells)

        def backtrack(index, values):
            nonlocal free_cells
            if index == len(free_cells):
                return values
            # print(values)
            i, j = free_cells[index][1], free_cells[index][2]
            for fcv in free_cells[index][3]:
                values.append(fcv)
                bit = value_to_bit(fcv)
                if not rows[i] & bit and not cols[j] & bit and not cells[cell_from_indexes(i, j)] & bit:
                    setv(i, j, fcv)
                    vv = backtrack(index+1, values)
                    if vv:
                        return vv
                    unsetv(i, j, fcv)
                values.pop()

        vv = backtrack(0, [])
        for index in range(len(vv)):
            i, j = free_cells[index][1], free_cells[index][2]
            v = vv[index]
            board[i][j] = str(v)


tests = [
    [
        [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]],
        [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    ],
    [
        [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]],
        [["5","1","9","7","4","8","6","3","2"],["7","8","3","6","5","2","4","1","9"],["4","2","6","1","3","9","8","7","5"],["3","5","7","9","8","6","2","4","1"],["2","6","4","3","1","7","5","9","8"],["1","9","8","5","2","4","3","6","7"],["9","7","5","8","6","3","1","2","4"],["8","3","2","4","9","1","7","5","6"],["6","4","1","2","7","5","9","8","3"]]
    ]
]

run_functional_tests(make_inplace(Solution().solveSudoku), tests, input_metric=make_matrix_values_test_metric('.'))