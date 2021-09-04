"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/636/week-1-september-1st-september-7th/3963/
https://leetcode.com/problems/sum-of-distances-in-tree/

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.



Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]


Constraints:

1 <= n <= 3 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG - broken assumption
# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         E = [[] for _ in range(n)]
#         P = [-1] * n
#         for a, b in edges:
#             E[min(a, b)].append(max(a, b))
#             P[max(a, b)] = min(a, b)
#         dist = [[0] * n for _ in range(n)]
#         distances = [0] * n
#         for i in range(n):
#             distances[i] = distances[P[i]] + i
#             dist[P[i]][i] = 1
#             dist[i][P[i]] = 1
#             for j in range(i):
#                 distances[j] += dist[P[i]][j] + 1
#                 dist[i][j] = dist[P[i]][j] + 1
#                 dist[j][i] = dist[P[i]][j] + 1
#
#         return distances


# TLE
# class Solution:
#     def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
#         E = [[] for _ in range(n)]
#         for a, b in edges:
#             E[a].append(b)
#             E[b].append(a)
#
#         P = [-1] * n
#         to_visit = [0]
#         visited = set()
#         dist = [[0] * n for _ in range(n)]
#         distances = [0] * n
#         while to_visit:
#             node = to_visit.pop()
#             if P[node] != -1:
#                 distances[node] = distances[P[node]] + len(visited)
#                 dist[P[node]][node] = 1
#                 dist[node][P[node]] = 1
#
#             for child in E[node]:
#                 if child not in visited and P[child] == -1:
#                     to_visit.append(child)
#                     P[child] = node
#
#             for prev in visited:
#                 pdist = dist[P[node]][prev] if P[node] != -1 else 0
#                 distances[prev] += pdist + 1
#                 dist[node][prev] = pdist + 1
#                 dist[prev][node] = pdist + 1
#
#             visited.add(node)
#
#         return distances


# https://leetcode.com/problems/sum-of-distances-in-tree/solution/
# Runtime: 989 ms, faster than 58.56% of Python3 online submissions for Sum of Distances in Tree.
# Memory Usage: 63.6 MB, less than 66.44% of Python3 online submissions for Sum of Distances in Tree.
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        E = [[] for _ in range(n)]
        for a, b in edges:
            E[a].append(b)
            E[b].append(a)

        count = [1] * n
        result = [0] * n

        def dfs(node = 0, parent = None):
            for child in E[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    result[node] += result[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in E[node]:
                if child != parent:
                    result[child] = result[node] - count[child] + n - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return result


tests = [
    [
        3,
        [[2,1],[0,2]],
        [3,3,2]
    ],
    [
        6,
        [[0,1],[0,2],[2,3],[2,4],[2,5]],
        [8,12,6,10,10,10]
    ],
    [
        1,
        [],
        [0]
    ],
    [
        2,
        [[1,0]],
        [1,1]
    ]
]

run_functional_tests(Solution().sumOfDistancesInTree, tests)