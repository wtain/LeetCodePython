"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:

1 <= points.length <= 1000
-106 <= xi, yi <= 106
All pairs (xi, yi) are distinct.
"""
import heapq
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1568 ms, faster than 79.99% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 81.5 MB, less than 73.67% of Python3 online submissions for Min Cost to Connect All Points.
# https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
# class UnionFind:
#     def __init__(self, size):
#         self.group = list(range(size))
#         self.rank = [0] * size
#
#     def find(self, i) -> int:
#         if self.group[i] != i:
#             self.group[i] = self.find(self.group[i])
#         return self.group[i]
#
#     def union(self, i, j) -> bool:
#         g1, g2 = self.find(i), self.find(j)
#         if g1 == g2:
#             return False
#         if self.rank[g1] > self.rank[g2]:
#             self.group[g2] = g1
#         elif self.rank[g1] < self.rank[g2]:
#             self.group[g1] = g2
#         else:
#             self.group[g1] = g2
#             self.rank[g2] += 1
#         return True
#
#
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         all_edges = []
#         for i in range(n):
#             for j in range(i+1, n):
#                 w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
#                 all_edges.append((w, i, j))
#
#         all_edges.sort()
#         uf = UnionFind(n)
#         mst_cost, edges_used = 0, 0
#         for w, i, j in all_edges:
#             if uf.union(i, j):
#                 mst_cost += w
#                 edges_used += 1
#                 if edges_used == n-1:
#                     break
#         return mst_cost


# Runtime: 1369 ms, faster than 86.02% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 78.6 MB, less than 84.22% of Python3 online submissions for Min Cost to Connect All Points.
# https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         h = [(0, 0)]
#         in_mst = [False] * n
#
#         mst_cost, edges_used = 0, 0
#
#         while edges_used < n:
#             w, i = heapq.heappop(h)
#             if in_mst[i]:
#                 continue
#             in_mst[i] = True
#             mst_cost += w
#             edges_used += 1
#             for j in range(n):
#                 if not in_mst[j]:
#                     next_w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
#                     heapq.heappush(h, (next_w, j))
#         return mst_cost


# Runtime: 1189 ms, faster than 91.56% of Python3 online submissions for Min Cost to Connect All Points.
# Memory Usage: 14.5 MB, less than 96.99% of Python3 online submissions for Min Cost to Connect All Points.
# https://leetcode.com/problems/min-cost-to-connect-all-points/solution/
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        h = [(0, 0)]
        in_mst = [False] * n

        mst_cost, edges_used = 0, 0
        min_dist = [math.inf] * n
        min_dist[0] = 0

        while edges_used < n:
            curr_min_edge = math.inf
            i = -1

            for j in range(n):
                if not in_mst[j] and curr_min_edge > min_dist[j]:
                    curr_min_edge, i = min_dist[j], j

            mst_cost += curr_min_edge
            edges_used += 1
            in_mst[i] = True

            for j in range(n):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                if not in_mst[j] and min_dist[j] > w:
                    min_dist[j] = w
        return mst_cost


tests = [
    [[[0,0],[2,2],[3,10],[5,2],[7,0]], 20],
    [[[3,12],[-2,5],[-4,1]], 18]
]

run_functional_tests(Solution().minCostConnectPoints, tests)
