"""
https://leetcode.com/problems/path-with-minimum-effort/
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3617/
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.



Example 1:



Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
Example 2:



Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
Output: 1
Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells, which is better than route [1,3,5,3,5].
Example 3:


Input: heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output: 0
Explanation: This route does not require any effort.


Constraints:

rows == heights.length
columns == heights[i].length
1 <= rows, columns <= 100
1 <= heights[i][j] <= 106
"""
from collections import defaultdict
from heapq import heapify, heappop
from itertools import product
from typing import List, Dict, DefaultDict


# TLE
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#
#         class Node:
#             def __init__(self):
#                 self.adjacent = {}
#
#             def getAdjacent(self, cost: int) -> List[int]:
#                 if not self.adjacent.get(cost):
#                     self.adjacent[cost] = []
#                 return self.adjacent[cost]
#
#             def addEdge(self, cost: int, target: int):
#                 self.getAdjacent(cost).append(target)
#
#         def buildGraph(heights: List[List[int]]) -> (Dict[int, Node], int):
#             graph : Dict[int, Node] = {}
#             h = len(heights)
#             w = len(heights[0])
#
#             maxCost = 0
#
#             def addEdge(x1, y1, x2, y2):
#                 nonlocal h, w, graph, heights, maxCost
#
#                 def getNode(index: int) -> Node:
#                     nonlocal graph
#                     if not graph.get(index):
#                         graph[index] = Node()
#                     return graph[index]
#
#                 index1 = y1 * w + x1
#                 index2 = y2 * w + x2
#                 if 0 <= x1 < w and 0 <= y1 < h and 0 <= x2 < w and 0 <= y2 < h:
#                     cost = abs(heights[y1][x1] - heights[y2][x2])
#                     maxCost = max(maxCost, cost)
#                     getNode(index1).addEdge(cost, index2)
#                     getNode(index2).addEdge(cost, index1)
#
#             for y in range(h):
#                 for x in range(w):
#                     addEdge(x, y, x + 1, y)
#                     addEdge(x, y, x, y + 1)
#
#             return graph, maxCost
#
#         def findPath(graph: Dict[int, Node], source: int, destination: int, maxCost: int) -> bool:
#             toVisit = []
#             visited = []
#             toVisit.append(source)
#             while toVisit:
#                 current = toVisit.pop()
#                 visited.append(current)
#                 if current == destination:
#                     return True
#                 adjacent = graph[current].adjacent
#                 for adj_cost in adjacent.keys():
#                     if adj_cost <= maxCost:
#                         neighbours = adjacent[adj_cost]
#                         for neighbour in neighbours:
#                             if neighbour not in toVisit and neighbour not in visited:
#                                 toVisit.append(neighbour)
#             return False
#
#         h = len(heights)
#         w = len(heights[0])
#         source = 0
#         destination = w*h-1
#         graph, maxCost = buildGraph(heights)
#
#         l = 0
#         r = maxCost+1
#
#         # for i in range(l, r):
#         #     if findPath(graph, source, destination, i):
#         #         return i
#
#         while l < r:
#             m = l + (r - l) // 2
#             if findPath(graph, source, destination, m):
#                 r = m
#             else:
#                 l = m+1
#
#         return r


# TLE
# class Solution:
#     def minimumEffortPath(self, heights: List[List[int]]) -> int:
#
#         h = len(heights)
#         w = len(heights[0])
#
#         def findPath(heights: List[List[int]], maxCost: int, source, destination) -> bool:
#             nonlocal w, h
#             toVisit = []
#             toVisit.append(source)
#             visited = []
#             while toVisit:
#                 current = toVisit.pop()
#                 visited.append(current)
#                 x, y = current
#                 if current == destination:
#                     return True
#                 if x+1 < w and \
#                         abs(heights[y][x] - heights[y][x+1]) <= maxCost and \
#                         (x+1, y) not in visited:
#                     toVisit.append((x+1, y))
#                 if y+1 < h and \
#                         abs(heights[y][x] - heights[y+1][x]) <= maxCost and \
#                         (x, y+1) not in visited:
#                     toVisit.append((x, y+1))
#                 if x-1 >= 0 and \
#                         abs(heights[y][x] - heights[y][x-1]) <= maxCost and \
#                         (x-1, y) not in visited:
#                     toVisit.append((x-1, y))
#                 if y-1 >= 0 and \
#                         abs(heights[y][x] - heights[y-1][x]) <= maxCost and \
#                         (x, y-1) not in visited:
#                     toVisit.append((x, y-1))
#
#             return False
#
#         maxCost = max(max(heights)) - min(min(heights))
#
#         l = 0
#         r = maxCost+1
#
#         # for i in range(l, r):
#         #     if findPath(heights, i, (0, 0), (w-1, h-1)):
#         #         return i
#
#         while l < r:
#             m = l + (r - l) // 2
#             # print(l, r, m)
#             if findPath(heights, m, (0, 0), (w-1, h-1)):
#                 r = m
#             else:
#                 l = m+1
#
#         return r

# Runtime: 916 ms, faster than 48.18% of Python3 online submissions for Path With Minimum Effort.
# Memory Usage: 17.8 MB, less than 16.74% of Python3 online submissions for Path With Minimum Effort.
class Solution:
    class WeightedUnionFind:
        def __init__(self, n: int):
            self.weigths = [0] * n
            self.ids = list(range(n))

        def find(self, p: int) -> int:
            while p != self.ids[p]:
                parent = self.ids[p]
                self.ids[p] = self.ids[parent]
                p = parent
            return p

        def union(self, p : int, q: int):
            parent_p = self.find(p)
            parent_q = self.find(q)

            if parent_p == parent_q:
                return

            if self.weigths[parent_p] > self.weigths[parent_q]:
                parent_q, parent_p = parent_p, parent_q

            self.ids[parent_p] = parent_q
            self.weigths[parent_q] += self.weigths[parent_p]

        def connected(self, p: int, q: int) -> bool:
            return self.find(p) == self.find(q)

    def build(self, heights: List[List[int]]) -> List[tuple]:
        h = len(heights)
        w = len(heights[0])
        edges = []
        for i, j in product(range(h), range(w)):
            id = i * w + j
            if i:
                cost = abs(heights[i][j] - heights[i-1][j])
                id2 = (i-1) * w + j
                edges.append((cost, id, id2))
            if j:
                cost = abs(heights[i][j] - heights[i][j-1])
                id2 = i * w + j - 1
                edges.append((cost, id, id2))
        return edges


    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h = len(heights)
        w = len(heights[0])
        edges = self.build(heights)
        heapify(edges)
        uf = self.WeightedUnionFind(w * h)
        weight = source = 0
        target = w * h - 1
        while not uf.connected(source, target):
            weight, root, child = heappop(edges)
            uf.union(root, child)
        return weight

    
    
tests = [

    ([[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]], 5),

    ([[1,2,2],[3,8,2],[5,3,5]], 2),
    ([[1,2,3],[3,8,4],[5,3,5]], 1),
    ([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]], 0)
]

for test in tests:
    result = Solution().minimumEffortPath(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
