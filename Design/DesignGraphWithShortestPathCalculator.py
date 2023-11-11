"""
https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/?envType=daily-question&envId=2023-11-11

There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.

Implement the Graph class:

Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.


Example 1:


Input
["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
[[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
Output
[null, 6, -1, null, 6]

Explanation
Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.


Constraints:

1 <= n <= 100
0 <= edges.length <= n * (n - 1)
edges[i].length == edge.length == 3
0 <= fromi, toi, from, to, node1, node2 <= n - 1
1 <= edgeCosti, edgeCost <= 106
There are no repeated edges and no self-loops in the graph at any point.
At most 100 calls will be made for addEdge.
At most 100 calls will be made for shortestPath.
"""
import heapq
import math
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# class Graph:
#
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.n = n
#         self.edges = edges
#         self.shortest = [[math.inf] * n for _ in range(n)]
#         transitions = [[] for _ in range(n)]
#         for a, b, w in edges:
#             self.shortest[a][b] = self.shortest[b][a] = w
#             transitions[a].append(b)
#             transitions[b].append(a)
#         distances = [0] * n
#         for i in range(n):
#             for j in range(n):
#                 if i == j:
#                     continue
#                 if self.shortest[i][j] == math.inf:
#                     continue
#                 for c in transitions[j]:
#                     d = distances[j] + self.shortest[j][c]
#                     distances[i] = min(distances[i], d)
#
#
#     def addEdge(self, edge: List[int]) -> None:
#         pass
#
#     def shortestPath(self, node1: int, node2: int) -> int:
#         return 0

# Runtime
# Details
# 546ms
# Beats 85.88%of users with Python3
# Memory
# Details
# 19.47MB
# Beats 60.59%of users with Python3
# # https://leetcode.com/problems/design-graph-with-shortest-path-calculator/editorial/?envType=daily-question&envId=2023-11-11
# class Graph:
#
#     def __init__(self, n: int, edges: List[List[int]]):
#         self.adj = [[] for _ in range(n)]
#         for edge in edges:
#             self.addEdge(edge)
#
#     def addEdge(self, edge: List[int]) -> None:
#         a, b, w = edge
#         self.adj[a].append((b, w))
#
#     def shortestPath(self, node1: int, node2: int) -> int:
#         n = len(self.adj)
#         pq = [(0, node1)]
#         cost_for_node = [math.inf] * n
#         cost_for_node[node1] = 0
#
#         while pq:
#             curr_cost, curr_node = heapq.heappop(pq)
#             if curr_cost > cost_for_node[curr_node]:
#                 continue
#             if curr_node == node2:
#                 return curr_cost
#             for neighbor, cost in self.adj[curr_node]:
#                 new_cost = curr_cost + cost
#                 if new_cost < cost_for_node[neighbor]:
#                     cost_for_node[neighbor] = new_cost
#                     heapq.heappush(pq, (new_cost, neighbor))
#         return -1


# Runtime
# Details
# 5122ms
# Beats 5.30%of users with Python3
# Memory
# Details
# 19.29MB
# Beats 85.29%of users with Python3
# https://leetcode.com/problems/design-graph-with-shortest-path-calculator/editorial/?envType=daily-question&envId=2023-11-11
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj = [[math.inf] * n for _ in range(n)]
        for a, b, w in edges:
            self.adj[a][b] = w
        for i in range(n):
            self.adj[i][i] = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    self.adj[j][k] = min(self.adj[j][k], self.adj[j][i] + self.adj[i][k])

    def addEdge(self, edge: List[int]) -> None:
        a, b, w = edge
        n = len(self.adj)
        for i in range(n):
            for j in range(n):
                self.adj[i][j] = min(self.adj[i][j], self.adj[i][a] + self.adj[b][j] + w)

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.adj[node1][node2] if self.adj[node1][node2] != math.inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)


tests = [
    [
        ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"],
        [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]],
        [null, 6, -1, null, 6]
    ]
]

run_object_tests(tests, cls=Graph)
