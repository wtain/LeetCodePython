"""
https://leetcode.com/problems/path-with-maximum-probability/

You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.



Example 1:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
Output: 0.25000
Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
Example 2:



Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
Output: 0.30000
Example 3:



Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
Output: 0.00000
Explanation: There is no path between 0 and 2.


Constraints:

2 <= n <= 10^4
0 <= start, end < n
start != end
0 <= a, b < n
a != b
0 <= succProb.length == edges.length <= 2*10^4
0 <= succProb[i] <= 1
There is at most one edge between every two nodes.
"""
import heapq
from collections import defaultdict, deque
from typing import List

from numpy import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 832 ms, faster than 39.54% of Python3 online submissions for Path with Maximum Probability.
# Memory Usage: 26.3 MB, less than 31.99% of Python3 online submissions for Path with Maximum Probability.
# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         nodes = [[] for _ in range(n)]
#         for e, p in zip(edges, succProb):
#             i, j = e
#             heapq.heappush(nodes[i], (-math.log(p), j))
#             heapq.heappush(nodes[j], (-math.log(p), i))
#         to_visit = [(0, start)]
#         found, best = False, 0
#         while to_visit:
#             p, index = heapq.heappop(to_visit)
#             if index == end and (not found or best > p):
#                 found, best = True, p
#             for cp, c in nodes[index]:
#                 heapq.heappush(to_visit, (p+cp, c))
#             nodes[index] = []
#         if not found:
#             return 0
#         return math.exp(-best)


# Runtime
# 675
# ms
# Beats
# 5.64%
# Analyze Complexity
# Memory
# 28.95
# MB
# Beats
# 37.69%
# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         nodes = [[] for _ in range(n)]
#         for e, p in zip(edges, succProb):
#             i, j = e
#             if p:
#                 heapq.heappush(nodes[i], (-math.log(p), j))
#                 heapq.heappush(nodes[j], (-math.log(p), i))
#             else:
#                 heapq.heappush(nodes[i], (math.inf, j))
#                 heapq.heappush(nodes[j], (math.inf, i))
#         to_visit = [(0, start)]
#         found, best = False, 0
#         while to_visit:
#             p, index = heapq.heappop(to_visit)
#             if index == end and (not found or best > p):
#                 found, best = True, p
#             for cp, c in nodes[index]:
#                 heapq.heappush(to_visit, (p+cp, c))
#             nodes[index] = []
#         if not found:
#             return 0
#         return math.exp(-best)


# Runtime
# 579
# ms
# Beats
# 21.57%
# Analyze Complexity
# Memory
# https://leetcode.com/problems/path-with-maximum-probability/editorial/?envType=daily-question&envId=2024-08-31
# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         max_prob = [0] * n
#         max_prob[start] = 1
#         for i in range(n-1):
#             has_update = 0
#             for j in range(len(edges)):
#                 u, v = edges[j]
#                 path_prob = succProb[j]
#                 if max_prob[u] * path_prob > max_prob[v]:
#                     max_prob[v] = max_prob[u] * path_prob
#                     has_update = 1
#                 if max_prob[v] * path_prob > max_prob[u]:
#                     max_prob[u] = max_prob[v] * path_prob
#                     has_update = 1
#             if not has_update:
#                 break
#         return max_prob[end]


# Runtime
# 580
# ms
# Beats
# 20.71%
# Analyze Complexity
# Memory
# 27.90
# MB
# Beats
# 78.69%
# https://leetcode.com/problems/path-with-maximum-probability/editorial/?envType=daily-question&envId=2024-08-31
# class Solution:
#     def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
#         graph = defaultdict(list)
#         for i, (a, b) in enumerate(edges):
#             graph[a].append([b, succProb[i]])
#             graph[b].append([a, succProb[i]])
#
#         max_prob = [0.0] * n
#         max_prob[start] = 1.0
#
#         queue = deque([start])
#         while queue:
#             cur_node = queue.popleft()
#             for next_node, path_prob in graph[cur_node]:
#                 if max_prob[cur_node] * path_prob > max_prob[next_node]:
#                     max_prob[next_node] = max_prob[cur_node] * path_prob
#                     queue.append(next_node)
#         return max_prob[end]


# Runtime
# 510
# ms
# Beats
# 97.53%
# Analyze Complexity
# Memory
# 29.80
# MB
# Beats
# 19.10%
# https://leetcode.com/problems/path-with-maximum-probability/editorial/?envType=daily-question&envId=2024-08-31
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        pq = [(-1.0, start)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob
            for next_node, path_prob in graph[cur_node]:
                if -cur_prob * path_prob > max_prob[next_node]:
                    max_prob[next_node] = -cur_prob * path_prob
                    heapq.heappush(pq, (-max_prob[next_node], next_node))
        return 0.0



tests = [
    [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2, 0.25000],
    [3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2, 0.30000],
    [3, [[0,1]], [0.5], 0, 2, 0],

    [
        5,
        [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],
        [0.37,0.17,0.93,0.23,0.39,0.04],
        3,
        4,
        0.21390
     ],

    [3, [[0,1],[1,2],[0,2]], [0.5,0.0,0.00001], 0, 2, 0.00001],
]

run_functional_tests(Solution().maxProbability, tests)
