"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/

There are n computers numbered from 0 to n - 1 connected by ethernet cables connections forming a network where connections[i] = [ai, bi] represents a connection between computers ai and bi. Any computer can reach any other computer directly or indirectly through the network.

You are given an initial computer network connections. You can extract certain cables between two directly connected computers, and place them between any pair of disconnected computers to make them directly connected.

Return the minimum number of times you need to do this in order to make all the computers connected. If it is not possible, return -1.



Example 1:


Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between computers 1 and 3.
Example 2:


Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.


Constraints:

1 <= n <= 105
1 <= connections.length <= min(n * (n - 1) / 2, 105)
connections[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated connections.
No two computers are connected by more than one cable.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 480 ms
# Beats
# 91.45%
# Memory
# 34.2 MB
# Beats
# 61.37%
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        p, rank = list(range(n)), [1] * n

        def get(i):
            while i != p[i]:
                i = p[i]
            return i

        cnt = 0

        def connect(i, j):
            nonlocal cnt
            i, j = get(i), get(j)
            if i == j:
                cnt += 1
                return
            if rank[i] >= rank[j]:
                rank[i] += rank[j]
                p[j] = p[i]
            else:
                rank[j] += rank[i]
                p[i] = p[j]

        for a, b in connections:
            connect(a, b)

        roots = set(get(i) for i in range(n))
        if len(roots) == 1:
            return 0

        m = len(roots) - 1
        if m > cnt:
            return -1

        return m


tests = [
    [5, [[0,1],[0,2],[3,4],[2,3]], 0],
    [4, [[0,1],[0,2],[1,2]], 1],
    [6, [[0,1],[0,2],[0,3],[1,2],[1,3]], 2],
    [6, [[0,1],[0,2],[0,3],[1,2]], -1],
]

run_functional_tests(Solution().makeConnected, tests)
