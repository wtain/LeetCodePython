"""
https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.



Example 1:


Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.
Example 2:


Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.
Example 3:


Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.


Constraints:

maze.length == m
maze[i].length == n
1 <= m, n <= 100
maze[i][j] is either '.' or '+'.
entrance.length == 2
0 <= entrancerow < m
0 <= entrancecol < n
entrance will always be an empty cell.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1929 ms
# Beats
# 54.26%
# Memory
# 14.6 MB
# Beats
# 68.60%
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        steps = 0
        n = len(maze)
        m = len(maze[0])
        i0, j0 = entrance[0], entrance[1]
        maze[i0][j0] = '+'
        level = [[i0, j0]]
        neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while level:
            next_level = []
            steps += 1
            for i, j in level:
                for di, dj in neighbors:
                    i1, j1 = i + di, j + dj
                    if 0 <= i1 < n and 0 <= j1 < m:
                        if maze[i1][j1] == '.':
                            if i1 == 0 or i1 == n-1 or j1 ==0 or j1 == m-1:
                                return steps
                            maze[i1][j1] = '+'
                            next_level.append([i1, j1])
            level = next_level
        return -1


tests = [
    [[["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2], 1],
    [[["+","+","+"],[".",".","."],["+","+","+"]], [1,0], 2],
    [[[".","+"]], [0,0], -1]
]

run_functional_tests(Solution().nearestExit, tests)
