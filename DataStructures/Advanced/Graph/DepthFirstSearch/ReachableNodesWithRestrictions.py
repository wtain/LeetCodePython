"""
https://leetcode.com/problems/reachable-nodes-with-restrictions/

There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.

Note that node 0 will not be a restricted node.



Example 1:


Input: n = 7, edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], restricted = [4,5]
Output: 4
Explanation: The diagram above shows the tree.
We have that [0,1,2,3] are the only nodes that can be reached from node 0 without visiting a restricted node.
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], restricted = [4,2,1]
Output: 3
Explanation: The diagram above shows the tree.
We have that [0,5,6] are the only nodes that can be reached from node 0 without visiting a restricted node.


Constraints:

2 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
1 <= restricted.length < n
1 <= restricted[i] < n
All the values of restricted are unique.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2028 ms
# Beats
# 41.29%
# Memory
# 71.4 MB
# Beats
# 97.3%
class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        neighbors = defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        reachable_count = 0
        to_visit = [0]
        restricted_nodes = set(restricted)
        visited = {0}
        while to_visit:
            node = to_visit.pop()
            reachable_count += 1
            for neighbor in neighbors[node]:
                if neighbor not in restricted_nodes and neighbor not in visited:
                    to_visit.append(neighbor)
                    visited.add(neighbor)
        return reachable_count


tests = [
    [7, [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]], [4,5], 4],
    [7, [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]], [4,2,1], 3],
]

run_functional_tests(Solution().reachableNodes, tests)
