"""
https://leetcode.com/problems/cherry-pickup-ii/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3571/

Given a rows x cols matrix grid representing a field of cherries. Each cell in grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at the top-left corner (0,0) , and Robot #2 is located at the top-right corner (0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.


Example 1:



Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:



Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4


Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100

Hint
Use dynamic programming,
define DP[i][j][k]: The maximum cherries that both robots can take
starting on the ith row, and column j and k of Robot 1 and 2 respectively.

Runtime: 2304 ms, faster than 10.55% of Python3 online submissions for Cherry Pickup II.
Memory Usage: 18.1 MB, less than 79.88% of Python3 online submissions for Cherry Pickup II.

Runtime: 2160 ms, faster than 13.68% of Python3 online submissions for Cherry Pickup II.
Memory Usage: 14.7 MB, less than 92.58% of Python3 online submissions for Cherry Pickup II.

"""
from typing import List


# class Solution:
#     def cherryPickup(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         m = len(grid[0])
#         dp = [[[-1] * m for i in range(m)] for j in range(n)]
#         if m > 1:
#             dp[0][0][m-1] = grid[0][0] + grid[0][m-1]
#         else:
#             dp[0][0][m - 1] = grid[0][0]
#         result = 0
#         for i in range(1, n):
#             for j in range(m):
#                 for k in range(m):
#                     maxv = -1
#                     for dj in range(-1, 2, 1):
#                         jj = j + dj
#                         if jj < 0 or jj >= m:
#                             continue
#                         for dk in range(-1, 2, 1):
#                             kk = k + dk
#                             if kk < 0 or kk >= m:
#                                 continue
#                             maxv = max(maxv, dp[i-1][jj][kk])
#                     if maxv == -1:
#                         continue
#                     maxv += grid[i][j]
#                     if j != k:
#                         maxv += grid[i][k]
#                     dp[i][j][k] = maxv
#                     result = max(result, maxv)
#         return result

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1] * m for i in range(m)]
        if m > 1:
            dp[0][m-1] = grid[0][0] + grid[0][m-1]
        else:
            dp[0][m - 1] = grid[0][0]
        result = 0
        for i in range(1, n):
            newDp = [[-1] * m for i in range(m)]
            for j in range(m):
                for k in range(m):
                    maxv = -1
                    for dj in range(-1, 2, 1):
                        jj = j + dj
                        if jj < 0 or jj >= m:
                            continue
                        for dk in range(-1, 2, 1):
                            kk = k + dk
                            if kk < 0 or kk >= m:
                                continue
                            maxv = max(maxv, dp[jj][kk])
                    if maxv == -1:
                        continue
                    maxv += grid[i][j]
                    if j != k:
                        maxv += grid[i][k]
                    newDp[j][k] = maxv
                    result = max(result, maxv)
            dp = newDp
        return result


print(Solution().cherryPickup([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]]))  # 24

print(Solution().cherryPickup([
        [1,0,0,0,0,0,1],
        [2,0,0,0,0,3,0],
        [2,0,9,0,0,0,0],
        [0,3,0,5,4,0,0],
        [1,0,2,3,0,0,6]]))  # 28

print(Solution().cherryPickup([[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]))  # 22

print(Solution().cherryPickup([[1,1],[1,1]]))  # 4