"""
https://leetcode.com/problems/maximal-rectangle/

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.



Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0


Constraints:

rows == matrix.length
cols == matrix[i].length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 208 ms, faster than 69.09% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 15.2 MB, less than 96.86% of Python3 online submissions for Maximal Rectangle.
# https://leetcode.com/problems/maximal-rectangle/discuss/1603962/C%2B%2B-2-Solutions-or-Better-to-Optimal-with-Explanation-or-Easy-to-Understand
# class Solution:
#     def maximalRectangle(self, matrix: List[List[str]]) -> int:
#         n = len(matrix)
#         if not n:
#             return 0
#         m = len(matrix[0])
#         if not m:
#             return 0
#
#         def maximal_rectangle(dp: List[int]) -> int:
#             st = [-1]
#             max_area = 0
#             for i in range(len(dp)+1):
#                 val = dp[i] if i < len(dp) else -1
#                 while st[-1] != -1 and dp[st[-1]] > val:
#                     h = dp[st[-1]]
#                     st.pop()
#                     w = i - st[-1] - 1
#                     max_area = max(max_area, w*h)
#                 st.append(i)
#             return max_area
#
#         dp = [0] * m
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 if matrix[i][j] == '0':
#                     dp[j] = 0
#                 else:
#                     dp[j] += 1
#             result = max(result, maximal_rectangle(dp))
#
#         return result


# Runtime: 200 ms, faster than 79.81% of Python3 online submissions for Maximal Rectangle.
# Memory Usage: 15.5 MB, less than 68.88% of Python3 online submissions for Maximal Rectangle.
# https://leetcode.com/problems/maximal-rectangle/discuss/1603766/Python-O(mn)-solution-explained
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def hist(heights: List[int]) -> int:
            st, res = [], 0
            for i, h in enumerate(heights + [0]):
                while st and heights[st[-1]] >= h:
                    H = heights[st.pop()]
                    W = i if not st else i - st[-1]-1
                    res = max(res, H*W)
                st.append(i)
            return res

        if not matrix or not matrix[0]:
            return 0
        n, m, result = len(matrix), len(matrix[0]), 0
        row = [0] * m
        for i in range(n):
            for j in range(m):
                row[j] = 0 if matrix[i][j] == '0' else row[j] + 1
            result = max(result, hist(row))
        return result


tests = [
    [
        [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]],
        6
    ],
    [
        [], 0
    ],
    [
        [["0"]], 0
    ],
    [
        [["1"]], 1
    ],
    [
        [["0","0"]], 0
    ]
]

run_functional_tests(Solution().maximalRectangle, tests)
