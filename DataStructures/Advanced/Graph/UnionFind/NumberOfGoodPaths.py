"""
https://leetcode.com/problems/number-of-good-paths/description/

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.



Example 1:


Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
Example 2:


Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
Example 3:


Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.


Constraints:

n == vals.length
1 <= n <= 3 * 104
0 <= vals[i] <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
#         n = len(vals)
#         nodes = defaultdict(list)
#         for a, b in edges:
#             nodes[a].append(b)
#             nodes[b].append(a)
#
#         good_path_count = 0
#
#         def dfs(node, parent):
#             nonlocal good_path_count
#             good_path_count += 1
#             max_value = vals[node]
#             max_child_values = []
#             for child in nodes[node]:
#                 if child == parent:
#                     continue
#                 max_child_value = dfs(child, node)
#                 max_child_values.append(max_child_value)
#                 max_value = max(max_value, max_child_value)
#             return max_value
#
#         dfs(0, -1)
#
#         return good_path_count



# Runtime
# 2306 ms
# Beats
# 82.59%
# Memory
# 32.5 MB
# Beats
# 90.49%
# https://leetcode.com/problems/number-of-good-paths/solutions/2892908/number-of-good-paths/
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        p1, p2 = self.find(i), self.find(j)
        if p1 == p2:
            return
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        nodes = defaultdict(list)
        for a, b in edges:
            nodes[a].append(b)
            nodes[b].append(a)

        n = len(vals)
        values_to_nodes = defaultdict(list)
        for i in range(n):
            values_to_nodes[vals[i]].append(i)

        dsu = UnionFind(n)
        good_path_count = 0
        for value in sorted(values_to_nodes.keys()):
            for node in values_to_nodes[value]:
                if node not in nodes:
                    continue
                for neighbor in nodes[node]:
                    if vals[node] >= vals[neighbor]:
                        dsu.union(node, neighbor)

            group = defaultdict(int)
            for u in values_to_nodes[value]:
                group[dsu.find(u)] += 1

            for key in group.keys():
                size = group[key]
                good_path_count += size * (size+1) // 2

        return good_path_count


tests = [
    [[1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]], 6],
    [[1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]], 7],
    [[1], [], 1],
]

run_functional_tests(Solution().numberOfGoodPaths, tests)
