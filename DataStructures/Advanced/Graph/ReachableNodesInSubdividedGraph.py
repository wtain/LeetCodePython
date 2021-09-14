"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3972/
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/

You are given an undirected graph (the "original graph") with n nodes labeled from 0 to n - 1. You decide to subdivide each edge in the graph into a chain of nodes, with the number of new nodes varying between each edge.

The graph is given as a 2D array of edges where edges[i] = [ui, vi, cnti] indicates that there is an edge between nodes ui and vi in the original graph, and cnti is the total number of new nodes that you will subdivide the edge into. Note that cnti == 0 means you will not subdivide the edge.

To subdivide the edge [ui, vi], replace it with (cnti + 1) new edges and cnti new nodes. The new nodes are x1, x2, ..., xcnti, and the new edges are [ui, x1], [x1, x2], [x2, x3], ..., [xcnti+1, xcnti], [xcnti, vi].

In this new graph, you want to know how many nodes are reachable from the node 0, where a node is reachable if the distance is maxMoves or less.

Given the original graph and maxMoves, return the number of nodes that are reachable from node 0 in the new graph.



Example 1:


Input: edges = [[0,1,10],[0,2,1],[1,2,2]], maxMoves = 6, n = 3
Output: 13
Explanation: The edge subdivisions are shown in the image above.
The nodes that are reachable are highlighted in yellow.
Example 2:

Input: edges = [[0,1,4],[1,2,6],[0,2,8],[1,3,1]], maxMoves = 10, n = 4
Output: 23
Example 3:

Input: edges = [[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], maxMoves = 17, n = 5
Output: 1
Explanation: Node 0 is disconnected from the rest of the graph, so only node 0 is reachable.


Constraints:

0 <= edges.length <= min(n * (n - 1) / 2, 104)
edges[i].length == 3
0 <= ui < vi < n
There are no multiple edges in the graph.
0 <= cnti <= 104
0 <= maxMoves <= 109
1 <= n <= 3000
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
#         E = [{} for _ in range(n)]
#         for v1, v2, m in edges:
#             v1, v2 = min(v1, v2), max(v1, v2)
#             E[v1][v2] = (0, m)
#         cnt = 1
#         level = [(0, maxMoves)]
#         visited = set()
#         visited.add(0)
#         while level:
#             next_level = []
#             # print(level)
#             for node, steps in level:
#                 for next_node in E[node]:
#                     if next_node in visited:
#                         continue
#                     w1, w2 = E[node][next_node]
#                     weight = w2 - w1
#                     if steps > weight:
#                         rest = steps - weight - 1
#                         cnt += 1 + weight
#                         if rest > 0:
#                             next_level.append((next_node, rest))
#                     else:
#                         cnt += steps
#             level = next_level
#         return cnt


# Runtime: 860 ms, faster than 23.81% of Python3 online submissions for Reachable Nodes In Subdivided Graph.
# Memory Usage: 21.7 MB, less than 43.65% of Python3 online submissions for Reachable Nodes In Subdivided Graph.
# https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/solution/
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        E = [{} for _ in range(n)]
        for v1, v2, m in edges:
            E[v1][v2] = E[v2][v1] = m

        cnt = 0
        pq = [(0, 0)]
        dist = {0: 0}
        visited = {}
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
            cnt += 1
            for next_node, w in E[node].items():
                v = min(w, maxMoves - d)
                visited[node, next_node] = v
                d2 = d + w + 1
                if d2 < dist.get(next_node, maxMoves+1):
                    heapq.heappush(pq, (d2, next_node))
                    dist[next_node] = d2
        for u, v, w in edges:
            cnt += min(w, visited.get((u, v), 0) + visited.get((v, u), 0))
        return cnt


tests = [
    [[[0,1,10],[0,2,1],[1,2,2]], 6, 3, 13],
    [[[0,1,4],[1,2,6],[0,2,8],[1,3,1]], 10, 4, 23],
    [[[1,2,4],[1,4,5],[1,3,1],[2,3,4],[3,4,5]], 17, 5, 1]
]

run_functional_tests(Solution().reachableNodes, tests)