"""
https://leetcode.com/problems/island-perimeter/
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""
from typing import List


"""
Runtime: 544 ms, faster than 91.02% of Python3 online submissions for Island Perimeter.
Memory Usage: 14 MB, less than 73.81% of Python3 online submissions for Island Perimeter.
"""
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        p = 0
        for i in range(0, n):
            for j in range(0, m):
                if grid[i][j] == 0:
                    continue
                cnt = 0
                if i > 0 and grid[i-1][j]:
                    cnt += 1
                if j > 0 and grid[i][j - 1]:
                    cnt += 1
                if i < n-1 and grid[i+1][j]:
                    cnt += 1
                if j < m-1 and grid[i][j+1]:
                    cnt += 1
                p += 4 - cnt
        return p


print(Solution().islandPerimeter([[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]))  # 16
