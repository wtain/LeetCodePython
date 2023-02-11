"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.



Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]


Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 75 ms
# Beats
# 99.41%
# Memory
# 14.2 MB
# Beats
# 73.17%
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        red, blue = defaultdict(list), defaultdict(list)
        for u, v in redEdges:
            red[u].append(v)
        for u, v in blueEdges:
            blue[u].append(v)
        BigValue = float('Inf')
        shortest = [BigValue] * n
        shortest[0] = 0

        def step(level, next_level, visited_next, neighbors):
            for node, dist in level:
                shortest[node] = min(shortest[node], dist)
                for child in neighbors[node]:
                    if child in visited_next:
                        continue
                    next_level.append((child, dist+1))
                    visited_next.add(child)

        visited_red, visited_blue = set(), set()
        level_red, level_blue = [(0, 0)], [(0, 0)]
        while level_red or level_blue:
            level_red_next, level_blue_next = [], []

            step(level_red, level_blue_next, visited_blue, red)
            step(level_blue, level_red_next, visited_red, blue)

            level_blue, level_red = level_blue_next, level_red_next

        return [v if v != BigValue else -1 for v in shortest]


tests = [
    [3, [[0,1],[0,2]], [[1,0]], [0, 1, 1]],
    [5, [[0,1],[1,2],[2,3],[3,4]], [[1,2],[2,3],[3,1]], [0,1,2,3,7]],
    [3, [[0,1],[1,2]], [], [0,1,-1]],
    [3, [[0,1]], [[2,1]], [0,1,-1]]
]

run_functional_tests(Solution().shortestAlternatingPaths, tests)
