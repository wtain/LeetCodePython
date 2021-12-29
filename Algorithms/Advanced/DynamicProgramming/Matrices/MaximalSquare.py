"""
https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0


Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 328 ms, faster than 18.04% of Python3 online submissions for Maximal Square.
# Memory Usage: 15.6 MB, less than 78.05% of Python3 online submissions for Maximal Square.
# https://leetcode.com/submissions/detail/342778299/
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        if not n:
            return 0
        m = len(matrix[0])
        dp = [0] * (m+1)
        max_size, prev = 0, 0
        for i in range(1, n+1):
            for j in range(1, m+1):
                tmp = dp[j]
                if matrix[i-1][j-1] == '1':
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                    max_size = max(max_size, dp[j])
                else:
                    dp[j] = 0
                prev = tmp
        return max_size ** 2


tests = [
    [[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 4],
    [[["0","1"],["1","0"]], 1],
    [[["0"]], 0],
    [[["1","0","1","0"],["1","0","1","1"],["1","0","1","1"],["1","1","1","1"]], 4]
]

run_functional_tests(Solution().maximalSquare, tests)
