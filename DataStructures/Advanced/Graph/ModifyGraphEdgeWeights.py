"""
https://leetcode.com/problems/modify-graph-edge-weights/description/?envType=daily-question&envId=2024-08-30

You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.



Example 1:



Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
Example 2:



Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
Example 3:



Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.


Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges
"""
import heapq
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 9968
# ms
# Beats
# 5.81%
# Analyze Complexity
# Memory
# 19.68
# MB
# Beats
# 56.98%
# https://leetcode.com/problems/modify-graph-edge-weights/editorial/?envType=daily-question&envId=2024-08-30
# class Solution:
#     INF = int(2e9)
#
#     def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
#         current_shortest_distance = self.run_dijkstra(edges, n, source, destination)
#
#         if current_shortest_distance < target:
#             return []
#         matches_target = current_shortest_distance == target
#
#         for edge in edges:
#             if edge[2] > 0:
#                 continue
#             edge[2] = self.INF if matches_target else 1
#             if not matches_target:
#                 new_distance = self.run_dijkstra(edges, n, source, destination)
#                 if new_distance <= target:
#                     matches_target = True
#                     edge[2] += target - new_distance
#         return edges if matches_target else []
#
#     def run_dijkstra(self, edges, n, source, destination):
#         adj_matrix = [[self.INF] * n for _ in range(n)]
#         min_distance = [self.INF] * n
#         visited = [False] * n
#
#         min_distance[source] = 0
#         for nodeA, nodeB, weight in edges:
#             if weight != -1:
#                 adj_matrix[nodeA][nodeB] = weight
#                 adj_matrix[nodeB][nodeA] = weight
#
#         for _ in range(n):
#             nearest_unvisited_node = -1
#             for i in range(n):
#                 if not visited[i] and (nearest_unvisited_node == -1 or min_distance[i] < min_distance[nearest_unvisited_node]):
#                     nearest_unvisited_node = i
#             visited[nearest_unvisited_node] = True
#
#             for v in range(n):
#                 min_distance[v] = min(min_distance[v], min_distance[nearest_unvisited_node] + adj_matrix[nearest_unvisited_node][v])
#
#         return min_distance[destination]


# Runtime
# 2923
# ms
# Beats
# 53.49%
# Analyze Complexity
# Memory
# 19.13
# MB
# Beats
# 96.51%
# https://leetcode.com/problems/modify-graph-edge-weights/editorial/?envType=daily-question&envId=2024-08-30
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        INF = int(2e9)
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            if w != -1:
                graph[u].append((v, w))
                graph[v].append((u, w))

        current_shortest_distance = self._dijkstra(graph, source, destination)
        if current_shortest_distance < target:
            return []

        if current_shortest_distance == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = INF
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))

            new_distance = self._dijkstra(graph, source, destination)
            if new_distance <= target:
                edges[i][2] += target - new_distance

                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = INF
                return edges

        return []

    def _dijkstra(self, graph, src, destination):
        min_distance = [math.inf] * len(graph)
        min_distance[src] = 0
        min_heap = [(0, src)]

        while min_heap:
            d, u = heapq.heappop(min_heap)
            if d > min_distance[u]:
                continue
            for v, w in graph[u]:
                if d + w < min_distance[v]:
                    min_distance[v] = d+w
                    heapq.heappush(min_heap, (min_distance[v], v))
        return min_distance[destination]


tests = [
    [5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5, [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]], # todo: custom_check
    [3, [[0,1,-1],[0,2,5]], 0, 2, 6, []],
    [4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6, [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]],
]

run_functional_tests(Solution().modifiedGraphEdges, tests)
