"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/description/

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2683 ms
# Beats
# 24.40%
# Memory
# 14.7 MB
# Beats
# 56.91%
# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solutions/2812406/daily-leetcoding-challenge-november-day-14/
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        if n <= 1:
            return 0
        graph = [[] for _ in range(n)]

        for i in range(n):
            u = stones[i]
            for j in range(n):
                if i == j:
                    continue

                v = stones[j]
                if v[0] == u[0] or v[1] == u[1]:
                    graph[i].append(j)

        visited = [False] * n
        result = 0

        for i in range(n):
            if visited[i]:
                continue
            self.dfs(graph, visited, i)
            result += 1

        return n - result

    def dfs(self, graph, visited, start):
        visited[start] = True
        for x in graph[start]:
            if visited[x]:
                continue

            self.dfs(graph, visited, x)


tests = [
    [[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]], 5],
    [[[0,0],[0,2],[1,1],[2,0],[2,2]], 3],
    [[[0,0]], 0]
]

run_functional_tests(Solution().removeStones, tests)
