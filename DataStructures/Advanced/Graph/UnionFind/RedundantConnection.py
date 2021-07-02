"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/606/week-4-june-22nd-june-28th/3791/
https://leetcode.com/problems/redundant-connection/

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.



Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]


Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 71.41% of Python3 online submissions for Redundant Connection.
# Memory Usage: 14.9 MB, less than 39.82% of Python3 online submissions for Redundant Connection.
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        p = list(range(n))
        rank = [0] * n

        def find(i: int) -> int:
            while p[i] != i:
                i = p[i]
            return i

        def union(i: int, j: int):
            i, j = find(i), find(j)
            if i == j:
                return
            if rank[i] < rank[j]:
                p[i] = j
            elif rank[i] > rank[j]:
                p[j] = i
            else:
                p[j] = i
                rank[i] += 1

        for i, j in edges:
            if find(i-1) == find(j-1):
                return [i, j]
            union(i-1, j-1)
        return []


tests = [
    [[[1,5],[3,4],[3,5],[4,5],[2,4]], [4,5]],

    [[[1,2],[1,3],[2,3]], [2,3]],
    [[[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]]
]

run_functional_tests(Solution().findRedundantConnection, tests)