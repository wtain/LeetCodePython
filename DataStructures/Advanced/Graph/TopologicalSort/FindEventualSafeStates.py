"""
https://leetcode.com/problems/find-eventual-safe-states/

There is a directed graph of n nodes with each node labeled from 0 to n - 1. The graph is represented by a 0-indexed 2D integer array graph where graph[i] is an integer array of nodes adjacent to node i, meaning there is an edge from node i to each node in graph[i].

A node is a terminal node if there are no outgoing edges. A node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node).

Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.



Example 1:

Illustration of graph
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Explanation: The given graph is shown above.
Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
Example 2:

Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
Output: [4]
Explanation:
Only node 4 is a terminal node, and every path starting at node 4 leads to node 4.


Constraints:

n == graph.length
1 <= n <= 104
0 <= graph[i].length <= n
0 <= graph[i][j] <= n - 1
graph[i] is sorted in a strictly increasing order.
The graph may contain self-loops.
The number of edges in the graph will be in the range [1, 4 * 104].
"""
from collections import deque, defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         n = len(graph)
#
#         unsafe = set()
#
#         def dfs(start: int) -> bool:
#             nonlocal n, graph, unsafe
#             visited = set()
#             to_visit = [start]
#             is_loop = False
#             while to_visit:
#                 node = to_visit.pop()
#                 visited.add(node)
#                 for next in graph[node]:
#                     if next == start or next in unsafe:
#                         is_loop = True
#                     if next not in visited:
#                         to_visit.append(next)
#             if is_loop:
#                 unsafe.add(start)
#             return is_loop
#
#         return [i for i in range(n) if not dfs(i)]


# Runtime
# 803 ms
# Beats
# 64.78%
# Memory
# 25.8 MB
# Beats
# 7.72%
# https://leetcode.com/problems/find-eventual-safe-states/solutions/127433/find-eventual-safe-states/
# class Solution:
#     def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
#         n = len(graph)
#         safe = set()
#         graph = [set(nodes) for nodes in graph]
#         rgraph = [set() for _ in range(n)]
#         queue = deque()
#         for node, neighbors in enumerate(graph):
#             if not neighbors:
#                 queue.append(node)
#             for next in neighbors:
#                 rgraph[next].add(node)
#
#         while queue:
#             node = queue.popleft()
#             safe.add(node)
#             for parent in rgraph[node]:
#                 graph[parent].remove(node)
#                 if len(graph[parent]) == 0:
#                     queue.append(parent)
#
#         return list(sorted(safe))


# Runtime
# 690 ms
# Beats
# 85.47%
# Memory
# 21.7 MB
# Beats
# 65.44%
# https://leetcode.com/problems/find-eventual-safe-states/solutions/127433/find-eventual-safe-states/
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = defaultdict(int)

        def dfs(node):
            if color[node] != WHITE:
                return color[node] == BLACK

            color[node] = GRAY
            for neighbor in graph[node]:
                if color[neighbor] == BLACK:
                    continue
                if color[neighbor] == GRAY or not dfs(neighbor):
                    return False
            color[node] = BLACK
            return True

        return list(filter(dfs, range(len(graph))))


tests = [
    [[[1,3,4,5,7,9],[1,3,8,9],[3,4,5,8],[1,8],[5,7,8],[8,9],[7,8,9],[3],[],[]], [5,8,9]],
    [[[1,2,3,4],[1,2,3,4],[3,4],[4],[]], [2,3,4]],
    [[[0],[2,3,4],[3,4],[0,4],[]], [4]],
    [[[1,2],[2,3],[5],[0],[5],[],[]], [2,4,5,6]],
    [[[1,2,3,4],[1,2],[3,4],[0,4],[]], [4]],
]

run_functional_tests(Solution().eventualSafeNodes, tests)
