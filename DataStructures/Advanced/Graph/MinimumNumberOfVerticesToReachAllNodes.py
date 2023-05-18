"""
https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.



Example 1:



Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex. From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].
Example 2:



Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them. Also any of these vertices can reach nodes 1 and 4.


Constraints:

2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= fromi, toi < n
All pairs (fromi, toi) are distinct.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1241 ms
# Beats
# 21.49%
# Memory
# 55.1 MB
# Beats
# 16.24%
# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
#         transitions_back = [[] for _ in range(n)]
#         for i, j in edges:
#             transitions_back[j].append(i)
#         source_nodes = [i for i in range(n) if not transitions_back[i]]
#         return source_nodes


# Runtime
# 1167 ms
# Beats
# 67.29%
# Memory
# 55 MB
# Beats
# 20.27%
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        transitions_back = [0 for _ in range(n)]
        for i, j in edges:
            transitions_back[j] += 1
        source_nodes = [i for i in range(n) if not transitions_back[i]]
        return source_nodes


tests = [
    [6, [[0,1],[0,2],[2,5],[3,4],[4,2]], [0,3]],
    [5, [[0,1],[2,1],[3,1],[1,4],[2,4]], [0,2,3]],
]

run_functional_tests(Solution().findSmallestSetOfVertices, tests)
