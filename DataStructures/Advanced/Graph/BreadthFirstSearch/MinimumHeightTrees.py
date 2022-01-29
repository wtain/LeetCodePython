"""
https://leetcode.com/problems/minimum-height-trees/

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.



Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]


Constraints:

1 <= n <= 2 * 104
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         d = defaultdict(list)
#         for n1,n2 in edges:
#             d[n1].append(n2)
#             d[n2].append(n1)
#         max_heights = []
#         for i in range(n):
#             max_depth = 0
#             level = deque()
#             level.append(i)
#             visited = set()
#             while level:
#                 num_nodes = len(level)
#                 for _ in range(num_nodes):
#                     node = level.popleft()
#                     visited.add(node)
#                     for child in d[node]:
#                         if child in visited:
#                             continue
#                         level.append(child)
#                 max_depth += 1
#             max_heights.append(max_depth)
#         mh = min(max_heights)
#         return [i for i, h in enumerate(max_heights) if mh == h]


# EVEN SLOWER
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         d = defaultdict(list)
#         for n1,n2 in edges:
#             d[n1].append(n2)
#             d[n2].append(n1)
#
#         distances = [[-1] * n for _ in range(n)]
#         for i in range(n):
#             distances[i][i] = 0
#
#         def dist(i: int, j: int) -> int:
#             if distances[i][j] == -1:
#                 level = deque()
#                 level.append(i)
#                 visited = set()
#                 l = 0
#                 while level:
#                     num_nodes = len(level)
#                     for _ in range(num_nodes):
#                         node = level.popleft()
#                         visited.add(node)
#                         for child in d[node]:
#                             distances[i][node] = distances[node][i] = l
#                             if child in visited:
#                                 continue
#                             level.append(child)
#                     l += 1
#             return distances[i][j]
#
#         depths = []
#         for i in range(n):
#             max_depth = 0
#             for j in range(n):
#                 max_depth = max(max_depth, dist(i, j))
#             depths.append(max_depth)
#
#         mh = min(depths)
#         return [i for i, h in enumerate(depths) if mh == h]
from Common.Helpers.ResultComparators import compareSets


# WRONG
# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#         d = defaultdict(list)
#         for n1, n2 in edges:
#             d[n1].append(n2)
#             d[n2].append(n1)
#
#         leaves = []
#         for i in range(n):
#             if len(d[i]) < 2:
#                 leaves.append(i)
#
#         level = deque(leaves)
#         visited = set()
#         while level:
#             cnt = len(level)
#             prev_level = level.copy()
#             visited2 = set()
#             for _ in range(cnt):
#                 node = level.popleft()
#                 visited.add(node)
#                 for child in d[node]:
#                     if child in visited or child in visited2:
#                         continue
#                     visited2.add(child)
#                     level.append(child)
#
#         return list(prev_level)


# Runtime: 224 ms, faster than 94.96% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 18.2 MB, less than 91.01% of Python3 online submissions for Minimum Height Trees.
# Runtime: 236 ms, faster than 69.64% of Python3 online submissions for Minimum Height Trees.
# Memory Usage: 18.5 MB, less than 76.05% of Python3 online submissions for Minimum Height Trees.
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return [i for i in range(n)]

        d = defaultdict(list)
        for n1, n2 in edges:
            d[n1].append(n2)
            d[n2].append(n1)

        leaves = []
        for i in range(n):
            if len(d[i]) < 2:
                leaves.append(i)

        remaining = n
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor = d[leaf].pop()
                d[neighbor].remove(leaf)
                if len(d[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves


tests = [
    [4, [[1,0],[1,2],[1,3]], [1]],
    [6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3,4]],
    [1, [], [0]],
    [2, [[0,1]], [0,1]]
]

run_functional_tests(Solution().findMinHeightTrees, tests, custom_check=compareSets)