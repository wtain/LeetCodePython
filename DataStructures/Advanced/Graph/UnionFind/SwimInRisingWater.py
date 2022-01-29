"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3785/
https://leetcode.com/problems/swim-in-rising-water/

On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distance in zero time. Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0). What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input: [[0,2],[1,3]]
Output: 3
Explanation:
At time 0, you are in grid location (0, 0).
You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.

You cannot reach point (1, 1) until time 3.
When the depth of water is 3, we can swim anywhere inside the grid.
Example 2:

Input: [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output: 16
Explanation:
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6

The final route is marked in bold.
We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

2 <= N <= 50.
grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
import heapq
from typing import List

from Common.Helpers.MatrixUtils import matrix_test_metric
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 628 ms, faster than 8.96% of Python3 online submissions for Swim in Rising Water.
# Memory Usage: 14.9 MB, less than 62.56% of Python3 online submissions for Swim in Rising Water.
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         n2 = n**2
#
#         def exists_path(t: int) -> bool:
#             p = [0] * n2
#             # size = [1] * n2
#             rank = p.copy()
#             getid = lambda i, j: i*n+j
#             for i in range(n):
#                 for j in range(n):
#                     p[getid(i, j)] = getid(i, j)
#
#             def find(x: int) -> int:
#                 while p[x] != x:
#                     x, p[x] = p[x], p[p[x]]
#                 return x
#
#             def union(x: int, y: int):
#                 x = find(x)
#                 y = find(y)
#                 if x == y:
#                     return
#                 if rank[x] < rank[y]:
#                     x, y = y, x
#                 p[y] = x
#                 if rank[x] == rank[y]:
#                     rank[x] += 1
#
#             for i in range(n):
#                 for j in range(n):
#                     if grid[i][j] > t:
#                         continue
#                     if i+1 < n and grid[i+1][j] <= t:
#                         union(getid(i, j), getid(i+1, j))
#                     if j+1 < n and grid[i][j+1] <= t:
#                         union(getid(i, j), getid(i, j+1))
#
#             clusters = [[0] * n for _ in range(n)]
#             for i in range(n):
#                 for j in range(n):
#                     clusters[i][j] = find(getid(i, j))
#
#             return find(getid(0, 0)) == find(getid(n-1, n-1))
#
#         l, r = 0, max([grid[i][j] for i, j in product(range(n), range(n))]) + 1
#         # for i in range(l, r):
#         #     if exists_path(i):
#         #         return i
#         while l < r:
#             # print(l, r)
#             m = l + (r - l) // 2
#             if not exists_path(m):
#                 # print(f"{m} - doesn't exist")
#                 l = m + 1
#             else:
#                 # print(f"{m} - exist")
#                 r = m
#
#         return l


# Runtime: 136 ms, faster than 48.96% of Python3 online submissions for Swim in Rising Water.
# Memory Usage: 15.1 MB, less than 20.80% of Python3 online submissions for Swim in Rising Water.
# https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained
# class UF:
#     def __init__(self, n: int):
#         self.p = list(range(n))
#         self.rank = [0] * n
#
#     def find(self, x: int) -> int:
#         while self.p[x] != x:
#             x = self.p[x]
#         return x
#
#     def union(self, x: int, y: int):
#         x, y = self.find(x), self.find(y)
#         if x == y:
#             return
#         if self.rank[x] < self.rank[y]:
#             self.p[x] = y
#         elif self.rank[x] > self.rank[y]:
#             self.p[y] = x
#         else:
#             self.p[y] = x
#             self.rank[x] += 1
#
#
# class Solution:
#     def swimInWater(self, grid: List[List[int]]) -> int:
#         d, n = {}, len(grid)
#         n2 = n ** 2
#         for i, j in product(range(n), range(n)):
#             d[grid[i][j]] = (i, j)
#
#         uf = UF(n2)
#         grid = [[0] * n for _ in range(n)]
#         neighbours = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#
#         getid = lambda i, j: i * n + j
#
#         for i in range(n2):
#             x, y = d[i]
#             grid[x][y] = 1
#             for dx, dy in neighbours:
#                 if 0 <= x + dx < n and 0 <= y + dy < n and grid[x+dx][y+dy]:
#                     uf.union(getid(x, y), getid(x+dx, y+dy))
#             if uf.find(0) == uf.find(n2-1):
#                 return i
#         return -1

# Runtime: 108 ms, faster than 66.08% of Python3 online submissions for Swim in Rising Water.
# Memory Usage: 15 MB, less than 40.32% of Python3 online submissions for Swim in Rising Water.
# https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        n2 = n ** 2
        res = 0
        st = [[grid[0][0], 0, 0]]
        neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()
        visited.add((0, 0))
        for k in range(n2):
            h, i, j = heapq.heappop(st)
            res = max(res, h)
            if i == n-1 and j == n-1:
                return res

            for di, dj in neighbors:
                if 0 <= i + di < n and 0 <= j+dj < n and (i+di, j+dj) not in visited:
                    heapq.heappush(st, [max(h, grid[i+di][j+dj]), i+di, j+dj])
                    visited.add((i+di, j+dj))
        return -1


tests = [
    [
        [
            [10,12, 4, 6],
            [ 9,11, 3, 5],
            [ 1, 7,13, 8],
            [ 2, 0,15,14]
        ],
        14
    ],
    [
        [
            [0,2],
            [1,3]
        ],
        3
    ],
    [
        [
            [ 0, 1, 2, 3, 4],
            [24,23,22,21, 5],
            [12,13,14,15,16],
            [11,17,18,19,20],
            [10, 9, 8, 7, 6]
        ],
        16
    ]
]

run_functional_tests(Solution().swimInWater, tests, input_metric=matrix_test_metric)