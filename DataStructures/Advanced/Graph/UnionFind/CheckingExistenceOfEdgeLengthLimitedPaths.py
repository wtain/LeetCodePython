"""
https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/description/

An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.



Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Exaplanation: The above figure shows the given graph.


Constraints:

2 <= n <= 105
1 <= edgeList.length, queries.length <= 105
edgeList[i].length == 3
queries[j].length == 3
0 <= ui, vi, pj, qj <= n - 1
ui != vi
pj != qj
1 <= disi, limitj <= 109
There may be multiple edges between two nodes.
"""
from typing import List

from Common.Constants import true, false
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1884 ms
# Beats
# 88.5%
# Memory
# 64 MB
# Beats
# 7.55%
# https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/editorial/
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        class UnionFind:
            def __init__(self, size):
                self.group = list(range(size))
                self.rank = [0] * size

            def find(self, node):
                while node != self.group[node]:
                    node = self.group[node]
                return self.group[node]

            def join(self, node1, node2):
                group1, group2 = self.find(node1), self.find(node2)
                if group1 == group2:
                    return
                if self.rank[group1] > self.rank[group2]:
                    self.group[group2] = group1
                elif self.rank[group1] < self.rank[group2]:
                    self.group[group1] = group2
                else:
                    self.group[group1] = group2
                    self.rank[group2] += 1

            def are_connected(self, node1, node2):
                return self.find(node1) == self.find(node2)

        uf = UnionFind(n)
        m = len(queries)
        result = [False] * m

        q_with_index = [[] for _ in range(m)]
        for i in range(m):
            q_with_index[i] = queries[i]
            q_with_index[i].append(i)

        edgeList.sort(key = lambda x: x[2])
        q_with_index.sort(key= lambda x: x[2])

        edge_index = 0

        for [p, q, limit, index] in q_with_index:
            while edge_index < len(edgeList) and edgeList[edge_index][2] < limit:
                node1, node2 = edgeList[edge_index][0], edgeList[edge_index][1]
                uf.join(node1, node2)
                edge_index += 1
            result[index] = uf.are_connected(p, q)

        return result


tests = [
    [3, [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], [[0,1,2],[0,2,5]], [false,true]],
    [5, [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], [[0,4,14],[1,4,13]], [true,false]],
]

run_functional_tests(Solution().distanceLimitedPathsExist, tests)
