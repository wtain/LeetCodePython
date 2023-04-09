"""
https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/

There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.



Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.


Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         moves = defaultdict(list)
#         for i, j in edges:
#             moves[i].append(j)
#         n = len(colors)
#
#         def bfs(i0):
#             d = defaultdict(int)
#             d[colors[i0]] += 1
#             result = 1
#             level = [(i0, d)]
#             visited = set()
#             while level:
#                 next_level = []
#                 for i, d in level:
#                     for j in moves[i]:
#                         if j == i0:
#                             return -1
#                         d1 = d.copy()
#                         d1[colors[j]] += 1
#                         result = max(result, d1[colors[j]])
#                         next_level.append((j, d1))
#                         visited.add(j)
#                 level = next_level
#             return result
#
#         result = 0
#         for i in range(n):
#             res = bfs(i)
#             if res == -1:
#                 return -1
#             result = max(result, res)
#
#         return result


# WRONG/NOT FINISHED
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         moves = defaultdict(list)
#         for i, j in edges:
#             moves[i].append(j)
#         n = len(colors)
#
#         cache = {}
#
#         def dfs(i0, counts):
#             if i0 in counts:
#                 return counts[i0]
#             counts[colors[i0]] += 1
#             for j in moves[i0]:
#                 dfs(j, counts)
#             cache[i0] = counts.copy()
#             counts[colors[i0]] -= 1
#
#
#         result = 0
#         for i in range(n):
#             res = dfs(i, defaultdict(int))
#             if res == -1:
#                 return -1
#             result = max(result, res)
#
#         return result


# TLE
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         moves, back_moves = defaultdict(list), defaultdict(list)
#         for i, j in edges:
#             moves[i].append(j)
#             back_moves[j].append(i)
#         n = len(colors)
#
#         if not n:
#             return 0
#
#         def bfs(i0):
#             level = [i0]
#             while level:
#                 next_level = []
#                 for i in level:
#                     for j in moves[i]:
#                         if j == i0:
#                             return True
#                         next_level.append(j)
#                 level = next_level
#             return False
#
#         if any(bfs(i) for i in range(n)):
#             return -1
#
#         sinks = {i for i in range(n) if not moves[i]}
#         counts = [defaultdict(int) for _ in range(n)]
#
#         for sink in sinks:
#             counts[sink][colors[sink]] += 1
#
#         result = 1
#         to_visit = sinks.copy()
#         while to_visit:
#             next_level = set()
#             for node in to_visit:
#                 for child in back_moves[node]:
#                     new_counts = counts[node].copy()
#                     new_counts[colors[child]] += 1
#                     for char in new_counts:
#                         counts[child][char] = max(counts[child][char], new_counts[char])
#                         result = max(result, counts[child][char])
#                     next_level.add(child)
#             to_visit = next_level
#
#         return result


# TLE
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         moves, back_moves = defaultdict(list), defaultdict(list)
#         for i, j in edges:
#             moves[i].append(j)
#             back_moves[j].append(i)
#         n = len(colors)
#
#         if not n:
#             return 0
#
#         def bfs(i0):
#             level = [i0]
#             while level:
#                 next_level = []
#                 for i in level:
#                     for j in moves[i]:
#                         if j == i0:
#                             return True
#                         next_level.append(j)
#                 level = next_level
#             return False
#
#         if any(bfs(i) for i in range(n)):
#             return -1
#
#         sinks = {i for i in range(n) if not moves[i]}
#         counts = [defaultdict(int) for _ in range(n)]
#
#         for sink in sinks:
#             counts[sink][colors[sink]] += 1
#
#         result = 1
#         to_visit = sinks.copy()
#         while to_visit:
#             next_level = set()
#             for node in to_visit:
#                 for child in back_moves[node]:
#                     child_color = colors[child]
#                     for char in counts[node]:
#                         counts[child][char] = max(counts[child][char], counts[node][char])
#                         result = max(result, counts[child][char])
#                     counts[child][child_color] = max(counts[child][child_color], counts[node][child_color] + 1)
#                     result = max(result, counts[child][child_color])
#                     next_level.add(child)
#             to_visit = next_level
#
#         return result


# TLE
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         moves, back_moves = defaultdict(set), defaultdict(set)
#         for i, j in edges:
#             moves[i].add(j)
#             back_moves[j].add(i)
#         n = len(colors)
#
#         sinks = {i for i in range(n) if not moves[i]}
#         counts = [defaultdict(int) for _ in range(n)]
#
#         def has_loop():
#             nonlocal n
#             moves_copy = moves.copy()
#             level = sinks.copy()
#             while level:
#                 next_level = set()
#                 for node in level:
#                     for parent in back_moves[node]:
#                         moves_copy[parent].remove(node)
#                         if not moves_copy[parent]:
#                             next_level.add(parent)
#                 level = next_level
#             return any(moves[i] for i in range(n))
#
#         if has_loop():
#             return -1
#
#         result = 0
#
#         for sink in sinks:
#             counts[sink][colors[sink]] += 1
#             result = 1
#
#         to_visit = sinks.copy()
#         while to_visit:
#             next_level = set()
#             for node in to_visit:
#                 for child in back_moves[node]:
#                     child_color = colors[child]
#                     for char in counts[node]:
#                         counts[child][char] = max(counts[child][char], counts[node][char])
#                         result = max(result, counts[child][char])
#                     counts[child][child_color] = max(counts[child][child_color], counts[node][child_color] + 1)
#                     result = max(result, counts[child][child_color])
#                     next_level.add(child)
#             to_visit = next_level
#         return result


# Runtime
# 3326 ms
# Beats
# 11.91%
# Memory
# 75.6 MB
# Beats
# 99.40%
# https://leetcode.com/problems/largest-color-value-in-a-directed-graph/solutions/3395458/python-java-c-simple-solution-easy-to-understand/
# class Solution:
#     def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
#         n, k = len(colors), 26
#         indegrees = [0] * n
#         graph = [[] for _ in range(n)]
#         for u, v in edges:
#             graph[u].append(v)
#             indegrees[v] += 1
#         zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
#         counts = [[0] * k for _ in range(n)]
#         for i, c in enumerate(colors):
#             counts[i][ord(c) - ord('a')] += 1
#         max_count, visited = 0, 0
#         while zero_indegree:
#             u = zero_indegree.pop()
#             visited += 1
#             for v in graph[u]:
#                 for i in range(k):
#                     counts[v][i] = max(counts[v][i], counts[u][i] + (ord(colors[v]) - ord('a') == i))
#                 indegrees[v] -= 1
#                 if indegrees[v] == 0:
#                     zero_indegree.add(v)
#             max_count = max(max_count, max(counts[u]))
#         return max_count if visited == n else -1


# Runtime
# 1809 ms
# Beats
# 99.40%
# Memory
# 75.7 MB
# Beats
# 99.40%
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indegrees = [0] * n
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            indegrees[v] += 1
        zero_indegree = set(i for i in range(n) if indegrees[i] == 0)
        counts = [defaultdict(int) for _ in range(n)]
        for i, c in enumerate(colors):
            counts[i][c] += 1
        max_count, visited = 0, 0
        while zero_indegree:
            u = zero_indegree.pop()
            visited += 1
            for v in graph[u]:
                for c in counts[u]:
                    counts[v][c] = max(counts[v][c], counts[u][c] + (colors[v] == c))
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    zero_indegree.add(v)
            max_count = max(max_count, max(counts[u].values()))
        return max_count if visited == n else -1


tests = [
    ["abaca", [[0,1],[0,2],[2,3],[3,4]], 3],
    ["a", [[0,0]], -1],
    ["hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]], 3],
    ["keitgkggegyktyeytgyigkggktiigigkeyygtgytiygtkg", [[0,1],[1,2],[2,3],[1,3],[3,4],[4,5],[5,6],[3,6],[5,7],[6,8],[5,8],[7,8],[8,9],[7,10],[8,10],[9,10],[10,11],[9,11],[7,11],[5,12],[11,12],[11,13],[13,14],[12,14],[12,15],[10,15],[14,15],[7,15],[9,16],[13,16],[12,16],[15,16],[11,17],[14,17],[16,17],[15,18],[14,18],[17,18],[18,19],[14,19],[13,19],[14,20],[15,21],[12,21],[20,21],[19,22],[20,22],[21,22],[22,23],[19,23],[11,23],[18,23],[13,24],[23,24],[21,24],[24,25],[13,25],[23,25],[15,26],[23,26],[25,26],[24,26],[26,27],[25,27],[26,28],[27,28],[20,28],[23,28],[11,28],[23,29],[29,30],[25,31],[26,31],[15,32],[30,32],[31,33],[27,33],[30,33],[28,33],[29,34],[32,35],[33,35],[34,35],[35,36],[13,36],[34,36],[30,37],[36,37],[35,37],[24,37],[35,38],[34,39],[37,39],[37,40],[39,41],[37,41],[41,42],[38,42],[40,43],[43,44],[39,44],[35,44],[38,45],[44,45],[26,45]], 10],
    ["g", [], 1],
    ["", [], 0],
]

run_functional_tests(Solution().largestPathValue, tests)
