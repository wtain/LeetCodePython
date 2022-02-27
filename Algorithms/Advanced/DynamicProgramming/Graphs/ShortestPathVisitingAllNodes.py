"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/

You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.



Example 1:


Input: graph = [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:


Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]


Constraints:

n == graph.length
1 <= n <= 12
0 <= graph[i].length < n
graph[i] does not contain i.
If graph[a] contains b, then graph[b] contains a.
The input graph is always connected.
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         all_visited = (1 << n) - 1
#         shortest = 2 * n + 1
#
#         def impl(visited: int, i: int, length: int):
#             nonlocal all_visited, shortest, n
#             if length >= shortest:
#                 return
#             if visited == all_visited:
#                 shortest = min(shortest, length)
#                 return
#             for j in graph[i]:
#                 impl(visited | (1 << j), j, length + 1)
#
#         for i in range(n):
#             impl(1 << i, i, 0)
#
#         return shortest

# TLE
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         all_visited = (1 << n) - 1
#         shortest = 2 * n + 1
#
#         @lru_cache
#         def impl(visited: int, i: int, length: int):
#             nonlocal all_visited, shortest, n
#             if length >= shortest:
#                 return
#             if visited == all_visited:
#                 shortest = min(shortest, length)
#                 return
#             for j in graph[i]:
#                 impl(visited | (1 << j), j, length + 1)
#
#         for i in range(n):
#             impl(1 << i, i, 0)
#
#         return shortest

# SLOW
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         n = len(graph)
#         all_visited = (1 << n) - 1
#         shortest = 2 * n + 1
#
#         @lru_cache
#         def impl(visited: int, i: int, length: int):
#             nonlocal all_visited, shortest, n
#             if length >= shortest:
#                 return
#             if visited == all_visited:
#                 shortest = min(shortest, length)
#                 return
#             for j in graph[i]:
#                 if visited & (1 << j):
#                     continue
#                 impl(visited | (1 << j), j, length + 1)
#             for j in graph[i]:
#                 if not visited & (1 << j):
#                     continue
#                 impl(visited | (1 << j), j, length + 1)
#
#         for i in range(n):
#             impl(1 << i, i, 0)
#
#         return shortest


# Runtime: 716 ms, faster than 30.70% of Python3 online submissions for Shortest Path Visiting All Nodes.
# Memory Usage: 44.7 MB, less than 14.92% of Python3 online submissions for Shortest Path Visiting All Nodes.
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
# class Solution:
#     def shortestPathLength(self, graph: List[List[int]]) -> int:
#         def dp(node, mask):
#             state = (node, mask)
#             if state in cache:
#                 return cache[state]
#             if mask & (mask-1) == 0:
#                 return 0
#             cache[state] = float("inf")
#             for neighbor in graph[node]:
#                 if mask & (1 << neighbor):
#                     already_visited = 1 + dp(neighbor, mask)
#                     not_visited = 1 + dp(neighbor, mask ^ (1 << node))
#                     cache[state] = min(cache[state], already_visited, not_visited)
#             return cache[state]
#
#         n = len(graph)
#         ending_mask = (1 << n) - 1
#         cache = {}
#         return min(dp(node, ending_mask) for node in range(n))


# Runtime: 329 ms, faster than 54.55% of Python3 online submissions for Shortest Path Visiting All Nodes.
# Memory Usage: 19.2 MB, less than 49.40% of Python3 online submissions for Shortest Path Visiting All Nodes.
# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solution/
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0

        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps

                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))
            steps += 1
            queue = next_queue


tests = [
    [[[1,2,3],[0],[0],[0]], 4],  # [1,0,2,0,3]
    [[[1],[0,2,4],[1,3,4],[2],[1,2]], 4],  # [0,1,4,2,3]
    [[[1,4],[0,3,10],[3],[1,2,6,7],[0,5],[4],[3],[3],[10],[10],[1,9,8]], 15],
    [[[7],[3],[3,9],[1,2,4,5,7,11],[3],[3],[9],[3,10,8,0],[7],[11,6,2],[7],[3,9]], 17]
]

run_functional_tests(Solution().shortestPathLength, tests)
