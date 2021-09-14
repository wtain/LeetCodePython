"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3969/
https://leetcode.com/problems/largest-plus-sign/

You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.



Example 1:


Input: n = 5, mines = [[4,2]]
Output: 2
Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.
Example 2:


Input: n = 1, mines = [[0,0]]
Output: 0
Explanation: There is no plus sign, so return 0.


Constraints:

1 <= n <= 500
1 <= mines.length <= 5000
0 <= xi, yi < n
All the pairs (xi, yi) are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
#         left = [[0] * n for _ in range(n)]
#         right = [[0] * n for _ in range(n)]
#         up = [[0] * n for _ in range(n)]
#         down = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(n):
#                 left[i][j] = j
#                 right[i][j] = n-1-j
#                 up[i][j] = i
#                 down[i][j] = n - 1 - i
#
#         for i0, j0 in mines:
#             for i in range(i0, n):
#                 up[i][j0] -= 1
#             for j in range(j0, n):
#                 right[i0][j] -= 1
#             for i in range(i0, -1, -1):
#                 down[i][j0] -= 1
#             for j in range(j0, -1, -1):
#                 left[i0][j] -= 1
#
#         mx = 0
#         for i in range(n):
#             for j in range(n):
#                 v = min(left[i][j], right[i][j], up[i][j], down[i][j])
#                 mx = max(mx, v)
#
#         return mx


# Runtime: 4498 ms, faster than 23.91% of Python3 online submissions for Largest Plus Sign.
# Memory Usage: 18.7 MB, less than 61.62% of Python3 online submissions for Largest Plus Sign.
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[0] * n for _ in range(n)]
        banned = {tuple(mine) for mine in mines}
        result = 0
        for r in range(n):
            cnt = 0
            for c in range(n):
                cnt = 0 if (r,c) in banned else cnt+1
                dp[r][c] = cnt

            cnt = 0
            for c in range(n-1,-1,-1):
                cnt = 0 if (r, c) in banned else cnt + 1
                dp[r][c] = min(dp[r][c], cnt)

        for c in range(n):
            cnt = 0
            for r in range(n):
                cnt = 0 if (r,c) in banned else cnt+1
                dp[r][c] = min(dp[r][c], cnt)

            cnt = 0
            for r in range(n-1,-1,-1):
                cnt = 0 if (r, c) in banned else cnt + 1
                dp[r][c] = min(dp[r][c], cnt)
                result = max(result, dp[r][c])
        return result



tests = [
    [2, [[0,0],[0,1],[1,0]], 1],

    [5, [[4,2]], 2],
    [1, [[0,0]], 0]
]

run_functional_tests(Solution().orderOfLargestPlusSign, tests)