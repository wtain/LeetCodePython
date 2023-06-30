"""
https://leetcode.com/problems/last-day-where-you-can-still-cross/description/

There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.



Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.


Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2981 ms
# Beats
# 36.41%
# Memory
# 25.2 MB
# Beats
# 90.76%
# https://leetcode.com/problems/last-day-where-you-can-still-cross/editorial/
# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#
#         def impl(day):
#             grid = [[0] * col for _ in range(row)]
#             queue = deque()
#             for r, c in cells[:day]:
#                 grid[r - 1][c - 1] = 1
#
#             for i in range(col):
#                 if not grid[0][i]:
#                     queue.append((0, i))
#                     grid[0][i] = -1
#
#             while queue:
#                 r, c = queue.popleft()
#                 if r == row - 1:
#                     return True
#                 for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
#                     nr, nc = r + dr, c + dc
#                     if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
#                         grid[nr][nc] = -1
#                         queue.append((nr, nc))
#
#         l, r = 1, row * col
#
#         while l < r:
#             mid = r - (r - l) // 2
#             if impl(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l



# Runtime
# 2462 ms
# Beats
# 43.48%
# Memory
# 41.3 MB
# Beats
# 7.61%
# https://leetcode.com/problems/last-day-where-you-can-still-cross/editorial/
# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#
#         def impl(day):
#             grid = [[0] * col for _ in range(row)]
#             for r, c in cells[:day]:
#                 grid[r - 1][c - 1] = 1
#
#             def dfs(r, c):
#                 if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] != 0:
#                     return False
#                 if r == row - 1:
#                     return True
#                 grid[r][c] = -1
#                 for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
#                     if dfs(r + dr, c + dc):
#                         return True
#                 return False
#
#             for i in range(col):
#                 if grid[0][i] == 0 and dfs(0, i):
#                     return True
#
#             return False
#
#         l, r = 1, row * col
#
#         while l < r:
#             mid = r - (r - l) // 2
#             if impl(mid):
#                 l = mid
#             else:
#                 r = mid - 1
#         return l




# Runtime
# 2057 ms
# Beats
# 63.4%
# Memory
# 25.8 MB
# Beats
# 60.87%
# https://leetcode.com/problems/last-day-where-you-can-still-cross/editorial/
# class Solution:
#     def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
#
#         class DSU:
#             def __init__(self, n):
#                 self.root = list(range(n))
#                 self.size = [1] * n
#
#             def find(self, x):
#                 if self.root[x] != x:
#                     self.root[x] = self.find(self.root[x])
#                 return self.root[x]
#
#             def union(self, x, y):
#                 rx, ry = self.find(x), self.find(y)
#                 if rx == ry:
#                     return
#                 if self.size[x] > self.size[y]:
#                     rx, ry = ry, rx
#                 self.root[rx] = ry
#                 self.size[ry] += self.size[rx]
#
#         dsu = DSU(row * col + 2)
#         grid = [[1] * col for _ in range(row)]
#         directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
#
#         for i in range(len(cells)-1, -1, -1):
#             r, c = cells[i][0] - 1, cells[i][1] - 1
#             grid[r][c] = 0
#             index_1 = r * col + c + 1
#             for dr, dc in directions:
#                 nr, nc = r + dr, c + dc
#                 index_2 = nr * col + nc + 1
#                 if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 0:
#                     dsu.union(index_1, index_2)
#             if r == 0:
#                 dsu.union(0, index_1)
#             if r == row-1:
#                 dsu.union(row * col + 1, index_1)
#             if dsu.find(0) == dsu.find(row * col + 1):
#                 return i
#
#         return 0


# Runtime
# 1510 ms
# Beats
# 97.83%
# Memory
# 25.8 MB
# Beats
# 62.50%
# https://leetcode.com/problems/last-day-where-you-can-still-cross/editorial/
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        class DSU:
            def __init__(self, n):
                self.root = list(range(n))
                self.size = [1] * n

            def find(self, x):
                if self.root[x] != x:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                rx, ry = self.find(x), self.find(y)
                if rx == ry:
                    return
                if self.size[x] > self.size[y]:
                    rx, ry = ry, rx
                self.root[rx] = ry
                self.size[ry] += self.size[rx]

        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            index_1 = r * col + c + 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                index_2 = nr * col + nc + 1
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                    dsu.union(index_1, index_2)
            if c == 0:
                dsu.union(0, index_1)
            if c == col - 1:
                dsu.union(row * col + 1, index_1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i

        return 0


tests = [
    [2, 6, [[2,5],[1,6],[1,1],[2,2],[2,3],[1,5],[2,1],[1,4],[2,6],[2,4],[1,2],[1,3]], 7],
    [2, 2, [[1,1],[2,1],[1,2],[2,2]], 2],
    [2, 2, [[1,1],[1,2],[2,1],[2,2]], 1],
    [3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]], 3],
]

run_functional_tests(Solution().latestDayToCross, tests)
