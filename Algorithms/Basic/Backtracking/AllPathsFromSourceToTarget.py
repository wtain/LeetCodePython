"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).



Example 1:


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]


Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
import copy
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets


# Runtime: 116 ms, faster than 31.29% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.9 MB, less than 19.64% of Python3 online submissions for All Paths From Source to Target.
# https://leetcode.com/submissions/detail/370937565/
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         result = []
#         to_visit = []
#         n = len(graph)
#         if graph:
#             to_visit.append((0, [False] * n, []))
#         while to_visit:
#             current, visited, path = to_visit.pop()
#             visited[current] = True
#             path.append(current)
#             if current == n-1:
#                 result.append(path)
#             for neighbor in graph[current]:
#                 if not visited[neighbor]:
#                     to_visit.append((neighbor, copy.copy(visited), copy.copy(path)))
#         return result


# Runtime: 112 ms, faster than 34.15% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.9 MB, less than 19.64% of Python3 online submissions for All Paths From Source to Target.
# class Solution:
#     def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
#         result, to_visit, n = [], [], len(graph)
#         if graph:
#             to_visit.append((0, 0, []))
#         while to_visit:
#             current, visited, path = to_visit.pop()
#             visited |= 1 << current
#             path.append(current)
#             if current == n-1:
#                 result.append(path)
#             for neighbor in graph[current]:
#                 if not visited & (1 << neighbor):
#                     to_visit.append((neighbor, visited, copy.copy(path)))
#         return result


# Runtime: 116 ms, faster than 31.29% of Python3 online submissions for All Paths From Source to Target.
# Memory Usage: 15.5 MB, less than 92.32% of Python3 online submissions for All Paths From Source to Target.
# https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1600844/JAVA-or-DFS-or-96-Fast-or-Path-tracking-using-Bit-mask
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result, to_visit, n = [], [], len(graph)
        if graph:
            to_visit.append((0, 0, 0))
        while to_visit:
            current, visited, path = to_visit.pop()
            visited |= 1 << current
            path <<= 4
            path |= current
            if current == n-1:
                decoded = []
                while path:
                    node = path & 15
                    path >>= 4
                    decoded = [node] + decoded
                result.append([0] + decoded)
            for neighbor in graph[current]:
                if not visited & (1 << neighbor):
                    to_visit.append((neighbor, visited, path))
        return result


tests = [
    [
        [[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]
    ],
    [
        [[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    ],
    [
        [[1],[]], [[0,1]]
    ],
    [
        [[1,2,3],[2],[3],[]], [[0,1,2,3],[0,2,3],[0,3]]
    ],
    [
        [[1,3],[2],[3],[]], [[0,1,2,3],[0,3]]
    ]
]

run_functional_tests(Solution().allPathsSourceTarget, tests, custom_check=compareSets)
