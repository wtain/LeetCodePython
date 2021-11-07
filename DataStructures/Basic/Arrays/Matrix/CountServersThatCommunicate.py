"""
https://leetcode.com/problems/count-servers-that-communicate/

You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.

Return the number of servers that communicate with any other server.



Example 1:



Input: grid = [[1,0],[0,1]]
Output: 0
Explanation: No servers can communicate with others.
Example 2:



Input: grid = [[1,0],[1,1]]
Output: 3
Explanation: All three servers can communicate with at least one other server.
Example 3:



Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
Output: 4
Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.


Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 250
1 <= n <= 250
grid[i][j] == 0 or 1
"""
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def countServers(self, grid: List[List[int]]) -> int:
#         n, m = len(grid), len(grid[0])
#         cols, rows = [0] * m, [0] * m
#         cnt = 0
#         for i,j in product(range(n), range(m)):
#             cols[j] += grid[i][j]
#             rows[i] += grid[i][j]
#             cnt += grid[i][j]
#         for i, j in product(range(n), range(m)):
#             if grid[i][j] == 1 and cols[i] == 1 and rows[j] == 1:
#                 cnt -= 1
#         return cnt

# Runtime: 520 ms, faster than 48.97% of Python3 online submissions for Count Servers that Communicate.
# Memory Usage: 15.7 MB, less than 87.59% of Python3 online submissions for Count Servers that Communicate.
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cols, rows = [0] * m, [0] * n
        cnt = 0
        for i,j in product(range(n), range(m)):
            cols[j] += grid[i][j]
            rows[i] += grid[i][j]
        for i, j in product(range(n), range(m)):
            if grid[i][j] == 1 and (cols[j] > 1 or rows[i] > 1):
                cnt += 1
        return cnt


tests = [
    [[[1,0],[0,1]], 0],
    [[[1,0],[1,1]], 3],
    [[[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]], 4],
    [[[0,0,0,0],[1,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1]], 8]
]

run_functional_tests(Solution().countServers, tests)
