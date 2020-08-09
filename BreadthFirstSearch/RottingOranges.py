"""
https://leetcode.com/problems/rotting-oranges/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/550/week-2-august-8th-august-14th/3418/
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""
from typing import List


def printGrid(grid: List[List[int]]):
    for row in grid:
        print(row)
    print()

"""
Runtime: 64 ms, faster than 47.67% of Python3 online submissions for Rotting Oranges.
Memory Usage: 13.8 MB, less than 79.80% of Python3 online submissions for Rotting Oranges.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        BigValue = n * m + 1
        dist = [[BigValue for i in range(m)] for j in range(n)]
        # rotten = []
        # numFresh = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    # rotten.append((i, j))
                    dist[i][j] = 0
                # elif grid[i][j] == 1:
                    # numFresh += 1
        # changesMade = len(rotten) > 0
        changesMade = True
        while changesMade:
            changesMade = False
            # for idx in rotten:
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 0:
                        continue
                    dij = dist[i][j]
                    if i > 0 and grid[i-1][j] == 2:
                        grid[i][j] = 2
                        dist[i][j] = min(dist[i][j], dist[i-1][j] + 1)
                    if j > 0 and grid[i][j-1] == 2:
                        grid[i][j] = 2
                        dist[i][j] = min(dist[i][j], dist[i][j-1] + 1)
                    if i < n-1 and grid[i+1][j] == 2:
                        grid[i][j] = 2
                        dist[i][j] = min(dist[i][j], dist[i+1][j] + 1)
                    if j < m-1 and grid[i][j+1] == 2:
                        grid[i][j] = 2
                        dist[i][j] = min(dist[i][j], dist[i][j+1] + 1)
                    if dist[i][j] != dij:
                        changesMade = True
            # printGrid(dist)
        maxDist = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
                elif grid[i][j] == 0:
                    continue
                maxDist = max(maxDist, dist[i][j])
        return maxDist


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
print(Solution().orangesRotting([[0,2]]))  # 0
