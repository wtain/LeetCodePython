"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3719/
https://leetcode.com/problems/critical-connections-in-a-network/

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:



Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.


Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2136 ms, faster than 95.51% of Python3 online submissions for Critical Connections in a Network.
# Memory Usage: 86.2 MB, less than 65.57% of Python3 online submissions for Critical Connections in a Network.
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:

        def build_connections():
            nonlocal n, connections
            conn_matrix = [[] for _ in range(n)]
            for a, b in connections:
                conn_matrix[a].append(b)
                conn_matrix[b].append(a)
            return conn_matrix

        conn_matrix = build_connections()
        marked = [False] * n
        # in_stack = [False] * n
        low_link = [-1] * n
        index = [-1] * n
        timer = 0
        # st = []
        # strong_conns = [[False] * n for _ in range(n)]
        result = []

        def strong_connect(i: int, p: int = -1):
            # nonlocal conn_matrix, marked, in_stack, low_link, st, strong_conns, timer, result
            nonlocal conn_matrix, marked, low_link, timer, result
            # st.append(i)
            # in_stack[i] = True
            marked[i] = True
            timer += 1
            index[i] = timer
            low_link[i] = timer

            for j in conn_matrix[i]:
                if j == p:
                    continue
                if not marked[j]:
                    strong_connect(j, i)
                    low_link[i] = min(low_link[i], low_link[j])
                    if low_link[j] > index[i]:
                        result.append([i, j])
                # elif in_stack[j]:
                else:
                    low_link[i] = min(low_link[i], index[j])

            # if low_link[i] == i:
            #     while st:
            #         j = st.pop()
            #         in_stack[j] = False
            #         if i != j:
            #             strong_conns[i][j] = True
            #             strong_conns[j][i] = True
            #         if j == i:
            #             break

        for i in range(n):
            if not marked[i]:
                strong_connect(i)

        # result = []
        #
        # for i, j in connections:
        #     if not strong_conns[i][j] and not strong_conns[j][i]:
        #         result.append([i, j])

        return result


# Runtime: 2344 ms, faster than 55.55% of Python3 online submissions for Critical Connections in a Network.
# Memory Usage: 86.2 MB, less than 65.57% of Python3 online submissions for Critical Connections in a Network.
# class Solution:
#
#     def __init__(self):
#         self.timer = 0
#
#     def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
#         marked, tvisit, fup = [False] * n, [-1] * n, [-1] * n
#         result = []
#         graph = defaultdict(list)
#
#         def dfs(curr: int, par: int = -1):
#             marked[curr] = True
#             self.timer += 1
#             tvisit[curr] = fup[curr] = self.timer
#             for child in graph[curr]:
#                 if child == par:
#                     continue
#                 if marked[child]:
#                     fup[curr] = min(fup[curr], tvisit[child])
#                 else:
#                     dfs(child, curr)
#                     fup[curr] = min(fup[curr], fup[child])
#                     if fup[child] > tvisit[curr]:
#                         result.append([curr, child])
#
#         for i, j in connections:
#             graph[i].append(j)
#             graph[j].append(i)
#
#         for i in range(n):
#             if not marked[i]:
#                 dfs(i)
#
#         return result




tests = [
    [4, [[0,1],[1,2],[2,0],[1,3]], [[1,3]]]
]

run_functional_tests(Solution().criticalConnections, tests)