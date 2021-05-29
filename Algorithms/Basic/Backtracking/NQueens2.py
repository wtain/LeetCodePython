"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3760/
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.



Example 1:


Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 9
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 48 ms, faster than 79.18% of Python3 online submissions for N-Queens II.
# Memory Usage: 14 MB, less than 99.31% of Python3 online submissions for N-Queens II.
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, cols, diag1, diag2):
            nonlocal n
            if row == n:
                return 1
            cnt = 0
            for col in range(n):
                curr_diag1 = row - col
                curr_diag2 = row + col
                if col in cols or curr_diag1 in diag1 or curr_diag2 in diag2:
                    continue
                cols.add(col)
                diag1.add(curr_diag1)
                diag2.add(curr_diag2)
                cnt += backtrack(row + 1, cols, diag1, diag2)
                cols.remove(col)
                diag1.remove(curr_diag1)
                diag2.remove(curr_diag2)
            return cnt

        return backtrack(0, set(), set(), set())


tests = [
    [4, 2],
    [1, 1]
]

run_functional_tests(Solution().totalNQueens, tests)