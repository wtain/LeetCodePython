"""
https://leetcode.com/problems/game-of-life/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/573/week-5-december-29th-december-31st/3586/
According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.



Example 1:


Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
Example 2:


Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.


Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

Runtime: 32 ms, faster than 75.07% of Python3 online submissions for Game of Life.
Memory Usage: 14.4 MB, less than 27.97% of Python3 online submissions for Game of Life.
"""
from typing import List


# Runtime: 61 ms, faster than 20.36% of Python3 online submissions for Game of Life.
# Memory Usage: 14 MB, less than 51.25% of Python3 online submissions for Game of Life.
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                cnt = 0
                for i2 in range(-1, 2):
                    for j2 in range(-1, 2):
                        if i2 == 0 and j2 == 0:
                            continue
                        i1 = i + i2
                        j1 = j + j2
                        if 0 <= i1 < n and 0 <= j1 < m:
                            if board[i1][j1] & 1 == 1:
                                cnt += 1
                board[i][j] |= cnt << 1
        for i in range(n):
            for j in range(m):
                alive = board[i][j] & 1 == 1
                cnt = board[i][j] >> 1
                if alive:
                    if cnt < 2:
                        board[i][j] = 0
                    elif 2 <= cnt <= 3:
                        board[i][j] = 1
                    elif cnt > 3:
                        board[i][j] = 0
                else:
                    if cnt == 3:
                        board[i][j] = 1
                    else:
                        board[i][j] = 0


board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(board)
print(board)
"""
[
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
]
"""

print("---")

board = [[1,1],[1,0]]
Solution().gameOfLife(board)
print(board)
"""
[
    [1,1],
    [1,1]
]
"""