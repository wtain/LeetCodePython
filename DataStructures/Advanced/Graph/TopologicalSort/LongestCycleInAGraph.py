"""
https://leetcode.com/problems/longest-cycle-in-a-graph/description/

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.



Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:


Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.


Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i
"""
import math
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def longestCycle(self, edges: List[int]) -> int:
#         n = len(edges)
#         connections = list(range(n))
#         result = -1
#         detected = set()
#         for j in range(1, n+1):
#             for i in range(n):
#                 if i in detected:
#                     continue
#                 if connections[i] == -1:
#                     continue
#                 connections[i] = edges[connections[i]]
#                 if connections[i] == i:
#                     result = j
#                     detected.add(i)
#         return result

# Runtime
# 1432 ms
# Beats
# 51.40%
# Memory
# 185.9 MB
# Beats
# 13.9%
# https://leetcode.com/problems/longest-cycle-in-a-graph/solutions/3341640/python3-solution/
class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        visit = set()
        ranks = [math.inf] * n

        def impl(i, rank):
            if i in visit or edges[i] == -1:
                return -1

            if ranks[i] < rank:
                return rank - ranks[i]

            ranks[i] = rank
            val = impl(edges[i], rank+1)
            visit.add(i)
            return val

        return max(impl(t, 0) for t in range(n))


tests = [
    [[3,3,4,2,3], 3],
    [[2,-1,3,1], -1],
    [[3,4,0,2,-1,2], 3],
]

run_functional_tests(Solution().longestCycle, tests)
