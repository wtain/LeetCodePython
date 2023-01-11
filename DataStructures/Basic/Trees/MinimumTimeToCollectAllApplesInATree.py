"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/description/

Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.



Example 1:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
Example 2:


Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
Output: 0


Constraints:

1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
fromi < toi
hasApple.length == n
"""
from typing import List

from Common.Constants import true, false
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         nodes = [[] for _ in range(n)]
#         for edge in edges:
#             nodes[edge[0]].append(edge[1])
#
#         def dfs(node: int) -> (bool, int):
#             nonlocal nodes, hasApple
#             distance = 2 if node else 0
#             has_apples = hasApple[node]
#             for child in nodes[node]:
#                 child_has_apple, child_distance = dfs(child)
#                 has_apples = has_apples or child_has_apple
#                 if child_has_apple:
#                     distance += child_distance
#             return has_apples, distance if has_apples else 0

# Runtime
# 693 ms
# Beats
# 87.82%
# Memory
# 49.5 MB
# Beats
# 85.90%
# class Solution:
#     def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
#         nodes = [[] for _ in range(n)]
#         for edge in edges:
#             nodes[edge[0]].append(edge[1])
#             nodes[edge[1]].append(edge[0])
#
#         visited = set()
#
#         def dfs(node: int) -> (bool, int):
#             nonlocal nodes, hasApple, visited
#             visited.add(node)
#             distance = 2 if node else 0
#             has_apples = hasApple[node]
#             for child in nodes[node]:
#                 if child in visited:
#                     continue
#                 child_has_apple, child_distance = dfs(child)
#                 has_apples = has_apples or child_has_apple
#                 if child_has_apple:
#                     distance += child_distance
#             return has_apples, distance if has_apples else 0
#
#         return dfs(0)[1]


# Runtime
# 671 ms
# Beats
# 94.87%
# Memory
# 49.3 MB
# Beats
# 97.44%
# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/solutions/2864715/minimum-time-to-collect-all-apples-in-a-tree/
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        nodes = [[] for _ in range(n)]
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        def dfs(node: int, parent: int) -> int:
            nonlocal nodes, hasApple
            distance = 0
            for child in nodes[node]:
                if child == parent:
                    continue
                child_distance = dfs(child, node)
                if child_distance or hasApple[child]:
                    distance += child_distance + 2
            return distance

        return dfs(0, -1)


tests = [
    [4, [[0,2],[0,3],[1,2]], [false,true,false,false], 4],
    [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [false,false,true,false,true,true,false], 8],
    [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [false,false,true,false,false,true,false], 6],
    [7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [false,false,false,false,false,false,false], 0],
]

run_functional_tests(Solution().minTime, tests)
