"""
https://leetcode.com/problems/find-all-groups-of-farmland/

You are given a 0-indexed m x n binary matrix land where a 0 represents a hectare of forested land and a 1 represents a hectare of farmland.

To keep the land organized, there are designated rectangular areas of hectares that consist entirely of farmland. These rectangular areas are called groups. No two groups are adjacent, meaning farmland in one group is not four-directionally adjacent to another farmland in a different group.

land can be represented by a coordinate system where the top left corner of land is (0, 0) and the bottom right corner of land is (m-1, n-1). Find the coordinates of the top left and bottom right corner of each group of farmland. A group of farmland with a top left corner at (r1, c1) and a bottom right corner at (r2, c2) is represented by the 4-length array [r1, c1, r2, c2].

Return a 2D array containing the 4-length arrays described above for each group of farmland in land. If there are no groups of farmland, return an empty array. You may return the answer in any order.



Example 1:


Input: land = [[1,0,0],[0,1,1],[0,1,1]]
Output: [[0,0,0,0],[1,1,2,2]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[0][0].
The second group has a top left corner at land[1][1] and a bottom right corner at land[2][2].
Example 2:


Input: land = [[1,1],[1,1]]
Output: [[0,0,1,1]]
Explanation:
The first group has a top left corner at land[0][0] and a bottom right corner at land[1][1].
Example 3:


Input: land = [[0]]
Output: []
Explanation:
There are no groups of farmland.


Constraints:

m == land.length
n == land[i].length
1 <= m, n <= 300
land consists of only 0's and 1's.
Groups of farmland are rectangular in shape.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1965 ms
# Beats
# 19.81%
# Memory
# 48.5 MB
# Beats
# 26.24%
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        p = [[(i, j) for j in range(m)] for i in range(n)]
        rank = [[0 for j in range(m)] for i in range(n)]

        def get(i, j):
            while (i, j) != p[i][j]:
                i, j = p[i][j]
            return i, j

        def connect(i1, j1, i2, j2):
            i1, j1 = get(i1, j1)
            i2, j2 = get(i2, j2)
            if rank[i1][j1] > rank[i2][j2]:
                p[i2][j2] = i1, j1
            elif rank[i1][j1] < rank[i2][j2]:
                p[i1][j1] = i2, j2
            else:
                p[i2][j2] = i1, j1
                rank[i1][j1] += 1

        for i in range(n):
            i1 = i + 1
            for j in range(m):
                if not land[i][j]:
                    continue
                j1 = j + 1
                if i1 < n and land[i1][j]:
                    connect(i, j, i1, j)
                if j1 < m and land[i][j1]:
                    connect(i, j, i, j1)

        mini, maxi, minj, maxj = {}, {}, {}, {}
        for i in range(n):
            for j in range(m):
                if not land[i][j]:
                    continue
                if p[i][j] not in mini:
                    mini[p[i][j]] = i
                else:
                    mini[p[i][j]] = min(mini[p[i][j]], i)
                if p[i][j] not in maxi:
                    maxi[p[i][j]] = i
                else:
                    maxi[p[i][j]] = max(maxi[p[i][j]], i)
                if p[i][j] not in minj:
                    minj[p[i][j]] = j
                else:
                    minj[p[i][j]] = min(minj[p[i][j]], j)
                if p[i][j] not in maxj:
                    maxj[p[i][j]] = j
                else:
                    maxj[p[i][j]] = max(maxj[p[i][j]], j)

        return [[mini[i], minj[i], maxi[i], maxj[i]] for i in maxi]


tests = [
    [[[1,0,0],[0,1,1],[0,1,1]], [[0,0,0,0],[1,1,2,2]]],
    [[[1,1],[1,1]], [[0,0,1,1]]],
    [[[0]], []],
]

run_functional_tests(Solution().findFarmland, tests)
