"""
https://leetcode.com/problems/is-graph-bipartite/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/585/week-2-february-8th-february-14th/3639/
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists. Each node is an integer between 0 and graph.length - 1. There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.



Example 1:


Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:


Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: We cannot find a way to divide the set of nodes into two independent subsets.


Constraints:

1 <= graph.length <= 100
0 <= graph[i].length < 100
0 <= graph[i][j] <= graph.length - 1
graph[i][j] != i
All the values of graph[i] are unique.
The graph is guaranteed to be undirected.
"""
from typing import List


# Runtime: 176 ms, faster than 63.57% of Python3 online submissions for Is Graph Bipartite?.
# Memory Usage: 14.8 MB, less than 55.03% of Python3 online submissions for Is Graph Bipartite?.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        labels = [0] * n
        for i in range(n):
            if labels[i]:
                continue
            toVisit = [[i, 1]]
            while toVisit:
                j, label = toVisit.pop()
                if labels[j]:
                    if labels[j] != label:
                        return False
                    else:
                        continue
                labels[j] = label
                for k in graph[j]:
                    toVisit.append([k, 3-label])
        return True


tests = [
    ([[1,3],[0,2],[1,3],[0,2]], True),
    ([[1,2,3],[0,2],[0,1,3],[0,2]], False),

    ([[]], True),  # ??

    ([[2],[3],[0],[1]], True),

    ([[],[],[],[]], True),
]

for test in tests:
    result = Solution().isBipartite(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))