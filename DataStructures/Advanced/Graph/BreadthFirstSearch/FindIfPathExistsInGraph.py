"""
https://leetcode.com/problems/find-if-path-exists-in-graph/

There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.



Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.


Constraints:

1 <= n <= 2 * 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2459 ms, faster than 39.10% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 104.8 MB, less than 82.73% of Python3 online submissions for Find if Path Exists in Graph.
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
#         to_visit = [start]
#         visited = set()
#         neighbors = [[] for _ in range(n)]
#         for b,e in edges:
#             neighbors[b].append(e)
#             neighbors[e].append(b)
#         while to_visit:
#             next_level = []
#             for i in to_visit:
#                 if i == end:
#                     return True
#                 visited.add(i)
#                 for j in neighbors[i]:
#                     if j not in visited:
#                         next_level.append(j)
#             to_visit = next_level
#         return False


# Runtime: 1933 ms, faster than 67.34% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 104.8 MB, less than 87.85% of Python3 online submissions for Find if Path Exists in Graph.
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
#         to_visit, visited, neighbors = [start], set(), [[] for _ in range(n)]
#         for b,e in edges:
#             neighbors[b].append(e)
#             neighbors[e].append(b)
#         while to_visit:
#             next_level = []
#             for i in to_visit:
#                 if i == end:
#                     return True
#                 visited.add(i)
#                 next_level += [j for j in neighbors[i] if j not in visited]
#             to_visit = next_level
#         return False


# Runtime: 2252 ms, faster than 47.73% of Python3 online submissions for Find if Path Exists in Graph.
# Memory Usage: 104.6 MB, less than 91.55% of Python3 online submissions for Find if Path Exists in Graph.
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        to_visit1, visited1, to_visit2, visited2, neighbors = [start], set(), [end], set(), [[] for _ in range(n)]
        for b,e in edges:
            neighbors[b].append(e)
            neighbors[e].append(b)
        while to_visit1 or to_visit2:
            next_level = []
            for i in to_visit1:
                if i in visited2:
                    return True
                visited1.add(i)
                next_level += [j for j in neighbors[i] if j not in visited1]
            to_visit1 = next_level

            next_level = []
            for i in to_visit2:
                if i in visited1:
                    return True
                visited2.add(i)
                next_level += [j for j in neighbors[i] if j not in visited2]
            to_visit2 = next_level
        return False


tests = [
    [3, [[0,1],[1,2],[2,0]], 0, 2, True],
    [6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False]
]

run_functional_tests(Solution().validPath, tests)