"""
https://leetcode.com/problems/image-overlap/

You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.



Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0


Constraints:

n == img1.length == img1[i].length
n == img2.length == img2[i].length
1 <= n <= 30
img1[i][j] is either 0 or 1.
img2[i][j] is either 0 or 1.
"""
from collections import defaultdict
from typing import List

import numpy as np

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1038 ms, faster than 28.31% of Python3 online submissions for Image Overlap.
# Memory Usage: 14 MB, less than 85.54% of Python3 online submissions for Image Overlap.
# https://leetcode.com/problems/image-overlap/solution/
# class Solution:
#     def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
#         n = len(img1)
#
#         def match(i0: int, j0: int, img1, img2) -> int:
#             nonlocal n
#             res1, res2 = 0, 0
#             for i1, i2 in enumerate(range(i0, n)):
#                 for j1, j2 in enumerate(range(j0, n)):
#                     v1 = img1[i1][j1]
#                     v2 = img2[i2][j2]
#                     res1 += v1 * v2
#                     v1 = img1[i1][j2]
#                     v2 = img2[i2][j1]
#                     res2 += v1 * v2
#             return max(res1, res2)
#
#         max_res = 0
#         for i0 in range(n):
#             for j0 in range(n):
#                 res1 = match(i0, j0, img1, img2)
#                 res2 = match(i0, j0, img2, img1)
#                 max_res = max(max_res, max(res1, res2))
#         return max_res


# Runtime: 748 ms, faster than 50.00% of Python3 online submissions for Image Overlap.
# Memory Usage: 14.6 MB, less than 50.60% of Python3 online submissions for Image Overlap.
# https://leetcode.com/problems/image-overlap/solution/
# class Solution:
#     def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
#         n = len(img1)
#
#         def non_zero_cells(img):
#             ret = []
#             for x in range(n):
#                 for y in range(n):
#                     if img[x][y]:
#                         ret.append((x, y))
#             return ret
#
#         trans_cnt = defaultdict(int)
#         max_overlaps = 0
#         A1, B1 = non_zero_cells(img1), non_zero_cells(img2)
#
#         for (x1, y1) in A1:
#             for (x2, y2) in B1:
#                 vec = (x2 - x1, y2-y1)
#                 trans_cnt[vec] += 1
#                 max_overlaps = max(max_overlaps, trans_cnt[vec])
#         return max_overlaps

# Runtime: 882 ms, faster than 40.36% of Python3 online submissions for Image Overlap.
# Memory Usage: 32 MB, less than 11.45% of Python3 online submissions for Image Overlap.
# https://leetcode.com/problems/image-overlap/solution/
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        A, B = np.array(img1), np.array(img2)
        n = len(A)
        B_padded = np.pad(B, n-1, mode='constant', constant_values=(0, 0))

        max_overlaps = 0
        for xs in range(2*n - 1):
            for ys in range(2*n-1):
                kernel = B_padded[xs:xs+n, ys:ys+n]
                non_zero = np.sum(A * kernel)
                max_overlaps = max(max_overlaps, non_zero)

        return max_overlaps


tests = [
    [[[1,1,0],[0,1,0],[0,1,0]],  [[0,0,0],[0,1,1],[0,0,1]], 3],
    [[[1]], [[1]], 1],
    [[[0]], [[0]], 0],
    [
        [[0,0,0,0,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],
        [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0]],
        1
    ]
]

run_functional_tests(Solution().largestOverlap, tests)
