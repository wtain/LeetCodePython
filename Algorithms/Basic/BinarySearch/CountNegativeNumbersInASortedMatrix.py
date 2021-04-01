"""
https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.



Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0
Example 3:

Input: grid = [[1,-1],[-1,-1]]
Output: 3
Example 4:

Input: grid = [[-1]]
Output: 1


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100


Follow up: Could you find an O(n + m) solution?
"""
from typing import List


# Runtime: 132 ms, faster than 20.49% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15.1 MB, less than 78.23% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         cnt = 0
#         for row in grid:
#             for v in row:
#                 if v < 0:
#                     cnt += 1
#         return cnt

# Runtime: 116 ms, faster than 82.75% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15.1 MB, less than 78.23% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# class Solution:
#     def countNegatives(self, grid: List[List[int]]) -> int:
#         cnt = 0
#         for row in grid:
#             n = len(row)
#             l = 0
#             r = n
#             while l < r:
#                 m = l + (r - l) // 2
#                 if row[m] >= 0:
#                     l = m+1
#                 else:
#                     r = m
#             cnt += n - l
#         return cnt


# Runtime: 116 ms, faster than 82.75% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15.1 MB, less than 78.23% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        cnt = 0
        n = len(grid)
        m = len(grid[0])
        l = 0
        r = m
        while l < r:
            mid = l + (r - l) // 2
            if grid[0][mid] >= 0:
                l = mid+1
            else:
                r = mid
        cnt += m - l
        for i in range(1, n):
            while l >= m or l >= 0 and grid[i][l] < 0:
                l -= 1
            l += 1
            # print(grid[i][:l+1])

            cnt += m - l
        return cnt



tests = [
    ([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8),
    ([[3,2],[1,0]], 0),
    ([[1,-1],[-1,-1]], 3),
    ([[-1]], 1)
]

for test in tests:
    result = Solution().countNegatives(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))