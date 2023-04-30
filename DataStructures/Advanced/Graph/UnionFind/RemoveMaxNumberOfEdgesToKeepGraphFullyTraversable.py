"""
https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/description/

Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.



Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.




Constraints:

1 <= n <= 105
1 <= edges.length <= min(105, 3 * n * (n - 1) / 2)
edges[i].length == 3
1 <= typei <= 3
1 <= ui < vi <= n
All tuples (typei, ui, vi) are distinct.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2261 ms
# Beats
# 36.48%
# Memory
# 56.6 MB
# Beats
# 18.87%
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        class UnionFind:
            def __init__(self, n):
                self.rank = [0] * n
                self.p = list(range(n))
                self.count = n

            def get(self, i):
                while i != self.p[i]:
                    i = self.p[i]
                return self.p[i]

            def connect(self, i, j):
                i, j = self.get(i), self.get(j)
                if i == j:
                    return
                self.count -= 1
                if self.rank[i] > self.rank[j]:
                    self.p[j] = self.p[i]
                elif self.rank[i] < self.rank[j]:
                    self.p[i] = self.p[j]
                else:
                    self.p[j] = self.p[i]
                    self.rank[i] += 1

            def is_connected(self, i, j):
                i, j = self.get(i), self.get(j)
                return i == j

            def is_fully_connected(self):
                return self.count == 1

        edges.sort(key=lambda x: -x[0])

        n_removed = 0
        uf1, uf2 = UnionFind(n), UnionFind(n)
        for type, i, j in edges:
            i -= 1
            j -= 1
            if type == 3:
                if uf1.is_connected(i, j):
                    n_removed += 1
                else:
                    uf1.connect(i, j)
                    uf2.connect(i, j)
            elif type == 1:
                if uf1.is_connected(i, j):
                    n_removed += 1
                else:
                    uf1.connect(i, j)
            elif type == 2:
                if uf2.is_connected(i, j):
                    n_removed += 1
                else:
                    uf2.connect(i, j)

        if not uf1.is_fully_connected() or not uf2.is_fully_connected():
            return -1

        return n_removed


tests = [
    [4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2],
    [4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0],
    [4, [[3,2,3],[1,1,2],[2,3,4]], -1]
]

run_functional_tests(Solution().maxNumEdgesToRemove, tests)
