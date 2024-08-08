"""
https://leetcode.com/problems/spiral-matrix-iii/description/?envType=daily-question&envId=2024-08-08

You start at the cell (rStart, cStart) of an rows x cols grid facing east. The northwest corner is at the first row and column in the grid, and the southeast corner is at the last row and column.

You will walk in a clockwise spiral shape to visit every position in this grid. Whenever you move outside the grid's boundary, we continue our walk outside the grid (but may return to the grid boundary later.). Eventually, we reach all rows * cols spaces of the grid.

Return an array of coordinates representing the positions of the grid in the order you visited them.



Example 1:


Input: rows = 1, cols = 4, rStart = 0, cStart = 0
Output: [[0,0],[0,1],[0,2],[0,3]]
Example 2:


Input: rows = 5, cols = 6, rStart = 1, cStart = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]


Constraints:

1 <= rows, cols <= 100
0 <= rStart < rows
0 <= cStart < cols
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        result = []
        x, y = cStart, rStart
        ln = 1
        cur, dir = 0, 0
        dx, dy = 1, 0
        while len(result) < rows * cols:
            if 0 <= x < cols and 0 <= y < rows:
                result.append([y, x])
            x += dx
            y += dy
            cur += 1
            if cur == ln:
                cur = 0
                dir = (dir + 1) % 4
                if dir == 0:
                    dx, dy = 1, 0
                    ln += 1
                elif dir == 1:
                    dx, dy = 0, 1
                elif dir == 2:
                    dx, dy = -1, 0
                    ln += 1
                else:
                    dx, dy = 0, -1
        return result


tests = [
    [1, 4, 0, 0, [[0,0],[0,1],[0,2],[0,3]]],
    [5, 6, 1, 4, [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]],
]

run_functional_tests(Solution().spiralMatrixIII, tests)
