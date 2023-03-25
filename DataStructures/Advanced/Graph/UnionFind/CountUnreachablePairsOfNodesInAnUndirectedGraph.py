"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/description/

You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.



Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.


Constraints:

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.
"""
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]]) -> int:
#         p, rank = list(range(n)), [1] * n
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j):
#             i, j = get(i), get(j)
#             if i == j:
#                 return
#             if rank[i] >= rank[j]:
#                 rank[i] += rank[j]
#                 p[j] = p[i]
#             else:
#                 rank[j] += rank[i]
#                 p[i] = p[j]
#
#         for i, j in edges:
#             connect(i, j)
#
#         roots = [i for i in range(n) if i == p[i]]
#
#         result = 0
#         m = len(roots)
#         for i in range(m):
#             for j in range(i+1, m):
#                 result += rank[roots[i]] * rank[roots[j]]
#
#         return result

# Runtime
# 1992 ms
# Beats
# 98.22%
# Memory
# 73.7 MB
# Beats
# 94.31%
# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]]) -> int:
#         p, rank = list(range(n)), [1] * n
#
#         def get(i):
#             while i != p[i]:
#                 i = p[i]
#             return i
#
#         def connect(i, j):
#             i, j = get(i), get(j)
#             if i == j:
#                 return
#             if rank[i] >= rank[j]:
#                 rank[i] += rank[j]
#                 p[j] = p[i]
#             else:
#                 rank[j] += rank[i]
#                 p[i] = p[j]
#
#         for i, j in edges:
#             connect(i, j)
#
#         roots = [i for i in range(n) if i == p[i]]
#
#         result = 0
#
#         sums = list(accumulate(rank[i] for i in roots))
#         m = len(roots)
#
#         for j in range(m-1, 0, -1):
#             result += rank[roots[j]] * sums[j-1]
#
#         return result

# Runtime
# 1996 ms
# Beats
# 97.51%
# Memory
# 75.1 MB
# Beats
# 71.89%
class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        p, rank = list(range(n)), [1] * n

        def get(i):
            while i != p[i]:
                i = p[i]
            return i

        def connect(i, j):
            i, j = get(i), get(j)
            if i == j:
                return
            if rank[i] >= rank[j]:
                rank[i] += rank[j]
                p[j] = p[i]
            else:
                rank[j] += rank[i]
                p[i] = p[j]

        for i, j in edges:
            connect(i, j)

        sizes = [rank[i] for i in range(n) if i == p[i]]
        sums = list(accumulate(sizes))
        m = len(sizes)

        return sum(size * prev_sum for size, prev_sum in zip(reversed(sizes), reversed(sums[:-1])))


# 4 2 1
# 4 6 7
# 1 * 6 + 2 * 4


tests = [
    [3, [[0,1],[0,2],[1,2]], 0],
    [7, [[0,2],[0,5],[2,4],[1,6],[5,4]], 14],
]

run_functional_tests(Solution().countPairs, tests)
