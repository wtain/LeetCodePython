"""
https://leetcode.com/problems/count-submatrices-with-all-ones/

Given an m x n binary matrix mat, return the number of submatrices that have all ones.



Example 1:


Input: mat = [[1,0,1],[1,1,0],[1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2.
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:


Input: mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3.
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2.
There are 2 rectangles of side 3x1.
There is 1 rectangle of side 3x2.
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.


Constraints:

1 <= m, n <= 150
mat[i][j] is either 0 or 1.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         n, m = len(mat), len(mat[0])
#         dp1, dp2 = [[0] * m for _ in range(n)], [[0] * m for _ in range(n)]
#         for i in range(n):
#             dp2[i][0] = mat[i][0]
#         for j in range(m):
#             dp1[0][j] = mat[0][j]
#
#         for i in range(1, n):
#             for j in range(m):
#                 if mat[i][j]:
#                     dp1[i][j] = dp1[i-1][j] + 1
#         for i in range(n):
#             for j in range(1, m):
#                 if mat[i][j]:
#                     dp2[i][j] = dp2[i][j-1] + 1
#
#         result = 0
#         for i in range(n):
#             for j in range(m):
#                 result += dp1[i][j] * dp2[i][j]
#         return result


# Runtime
# 1269 ms
# Beats
# 38.41%
# Memory
# 14.6 MB
# Beats
# 68.87%
# # https://leetcode.com/problems/count-submatrices-with-all-ones/solutions/720265/java-detailed-explanation-from-o-mnm-to-o-mn-by-using-stack/
# class Solution:
#     def numSubmat(self, mat: List[List[int]]) -> int:
#         n, m = len(mat), len(mat[0])
#
#         def count_one_row(h: List[int]) -> int:
#             nonlocal m
#             result, l = 0, 0
#             for i in range(m):
#                 if h[i]:
#                     l += 1
#                 else:
#                     l = 0
#                 result += l
#             return result
#
#         result = 0
#         for up in range(n):
#             h = [1] * m
#             for down in range(up, n):
#                 for i in range(m):
#                     h[i] *= mat[down][i]
#                 result += count_one_row(h)
#
#         return result

# Runtime
# 276 ms
# Beats
# 89.7%
# Memory
# 14.8 MB
# Beats
# 23.18%
# https://leetcode.com/problems/count-submatrices-with-all-ones/solutions/720265/java-detailed-explanation-from-o-mnm-to-o-mn-by-using-stack/
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        def helper(h: List[int]) -> int:
            nonlocal m
            s = [0] * m
            st = []
            for i in range(m):
                while st and h[st[-1]] > h[i]:
                    st.pop()

                if st:
                    pre_index = st[-1]
                    s[i] = s[pre_index]
                    s[i] += h[i] * (i - pre_index)
                else:
                    s[i] = h[i] * (i+1)
                st.append(i)
            return sum(s)

        result = 0
        h = [0] * m
        for i in range(n):
            for j in range(m):
                h[j] = h[j] + 1 if mat[i][j] else 0
            result += helper(h)

        return result


tests = [
    [[[1,0,1],[1,1,0],[1,1,0]], 13],
    [[[0,1,1,0],[0,1,1,1],[1,1,1,0]], 24],
]

run_functional_tests(Solution().numSubmat, tests)
