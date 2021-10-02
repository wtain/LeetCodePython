"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3752/
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.



Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]


Constraints:

1 <= n <= 9

"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#
#         if n == 1:
#             return [["Q"]]
#
#         result1 = self.solveNQueens(n-1)
#
#         result = []
#         for i in range(n):
#             for field1 in result1:
#                 first_line = '.' * i + "Q" + '.' * (n - i - 1)
#                 field = [first_line] + [row1[:i] + '.' + row1[i:] for row1 in field1]
#                 result.append(field)
#
#         return result

# Runtime: 56 ms, faster than 84.09% of Python3 online submissions for N-Queens.
# Memory Usage: 14.9 MB, less than 11.69% of Python3 online submissions for N-Queens.
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        result = []

        def create_board(state):
            return ["".join(row) for row in state]

        def backtrack(row: int, cols, diag1, diag2, state):
            nonlocal result, n
            if row == n:
                result.append(create_board(state))
                return
            for col in range(n):
                curr_diag1 = row - col
                curr_diag2 = row + col
                if col in cols or curr_diag1 in diag1 or curr_diag2 in diag2:
                    continue
                cols.add(col)
                diag1.add(curr_diag1)
                diag2.add(curr_diag2)
                state[row][col] = 'Q'
                backtrack(row+1, cols, diag1, diag2, state)
                cols.remove(col)
                diag1.remove(curr_diag1)
                diag2.remove(curr_diag2)
                state[row][col] = '.'

        board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), board)
        return result


tests = [
    [4, [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]],
    [1, [["Q"]]]
]

run_functional_tests(Solution().solveNQueens, tests)