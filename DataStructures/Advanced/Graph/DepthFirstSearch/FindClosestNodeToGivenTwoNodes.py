"""
https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from i, then edges[i] == -1.

You are also given two integers node1 and node2.

Return the index of the node that can be reached from both node1 and node2, such that the maximum between the distance from node1 to that node, and from node2 to that node is minimized. If there are multiple answers, return the node with the smallest index, and if no possible answer exists, return -1.

Note that edges may contain cycles.



Example 1:


Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
Output: 2
Explanation: The distance from node 0 to node 2 is 1, and the distance from node 1 to node 2 is 1.
The maximum of those two distances is 1. It can be proven that we cannot get a node with a smaller maximum distance than 1, so we return node 2.
Example 2:


Input: edges = [1,2,-1], node1 = 0, node2 = 2
Output: 2
Explanation: The distance from node 0 to node 2 is 2, and the distance from node 2 to itself is 0.
The maximum of those two distances is 2. It can be proven that we cannot get a node with a smaller maximum distance than 2, so we return node 2.


Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
0 <= node1, node2 < n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1830 ms
# Beats
# 34.48%
# Memory
# 34.2 MB
# Beats
# 66.9%
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def dfs(node: int) -> List[int]:
            nonlocal edges, n
            distances = [-1] * n
            to_visit = [(node, 0)]
            visited = set()
            while to_visit:
                node, distance = to_visit.pop()
                visited.add(node)
                distances[node] = distance
                if edges[node] != -1 and edges[node] not in visited:
                    to_visit.append((edges[node], distance+1))
            return distances

        distances1 = dfs(node1)
        distances2 = dfs(node2)

        min_dist, min_index = float('Inf'), -1

        for i in range(n):
            if distances1[i] == -1 or distances2[i] == -1:
                continue
            distance = max(distances1[i], distances2[i])
            if min_dist > distance:
                min_dist = distance
                min_index = i

        return min_index


tests = [
    [[4,4,4,5,1,2,2], 1, 1, 1],
    [[2,2,3,-1], 0, 1, 2],
    [[1,2,-1], 0, 2, 2],
]

run_functional_tests(Solution().closestMeetingNode, tests)
