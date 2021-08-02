"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/613/week-1-august-1st-august-7th/3835/
https://leetcode.com/problems/making-a-large-island/

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.



Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.
Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.
Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.


Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 500
grid[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 3740 ms, faster than 59.72% of Python3 online submissions for Making A Large Island.
# Memory Usage: 34.3 MB, less than 36.56% of Python3 online submissions for Making A Large Island.
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        cnt = n * m
        p = list(range(cnt))
        rank = [0] * cnt
        weight = [1] * cnt

        def find(i: int) -> int:
            while p[i] != i:
                i = p[i]
            return i

        def union(i: int, j: int):
            i, j = find(i), find(j)
            if i == j:
                return
            if rank[i] < rank[j]:
                p[i] = j
                weight[j] += weight[i]
            elif rank[i] > rank[j]:
                p[j] = i
                weight[i] += weight[j]
            else:
                p[j] = i
                weight[i] += weight[j]
                rank[i] += 1

        def id(i: int, j: int) -> int:
            nonlocal n
            return i*n+j

        for i in range(n):
            for j in range(m):
                if not grid[i][j]:
                    continue
                if i > 0 and grid[i-1][j]:
                    union(id(i, j), id(i-1, j))
                if j > 0 and grid[i][j-1]:
                    union(id(i, j), id(i, j-1))

        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    continue
                w1 = w2 = w3 = w4 = 0
                added = set()
                added.add(-1)
                p1 = find(id(i-1, j)) if i > 0 else -1
                p2 = find(id(i, j-1)) if j > 0 else -1
                p3 = find(id(i+1, j)) if i+1 < m else -1
                p4 = find(id(i, j+1)) if j+1 < m else -1
                if i > 0 and grid[i-1][j] and p1 not in added:
                    added.add(p1)
                    w1 = weight[p1]
                if j > 0 and grid[i][j-1] and p2 not in added:
                    added.add(p2)
                    w2 = weight[p2]
                if i+1 < n and grid[i+1][j] and p3 not in added:
                    added.add(p3)
                    w3 = weight[p3]
                if j+1 < m and grid[i][j+1] and p4 not in added:
                    added.add(p4)
                    w4 = weight[p4]
                w = 1 + w1 + w2 + w3 + w4
                result = max(result, w)

        if not result:
            result = cnt
        return result



tests = [
    [[[1,0],[0,1]], 3],
    [[[1,1],[1,0]], 4],
    [[[1,1],[1,1]], 4]
]

run_functional_tests(Solution().largestIsland, tests)