"""
https://leetcode.com/problems/minimum-area-rectangle-ii/description/?envType=problem-list-v2&envId=array

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.



Example 1:


Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:


Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:


Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.


Constraints:

1 <= points.length <= 50
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
"""
import itertools
import math
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 458
# ms
# Beats
# 14.22%
# Analyze Complexity
# Memory
# 17.83
# MB
# Beats
# 88.73%
# class Solution:
#     def minAreaFreeRect(self, points: List[List[int]]) -> float:
#         result = math.inf
#         EPS = 1e-5
#         n = len(points)
#         for i1 in range(n):
#             x1, y1 = points[i1]
#             for i2 in range(n):
#                 if i2 == i1:
#                     continue
#                 x2, y2 = points[i2]
#                 v12 = [x2-x1, y2-y1]
#                 for i3 in range(i2+1, n):
#                     if i3 == i1 or i3 == i2:
#                         continue
#                     x3, y3 = points[i3]
#                     v13 = [x3 - x1, y3 - y1]
#                     if abs(v12[0]*v13[0] + v12[1]*v13[1]) >= EPS:
#                         continue
#                     for i4 in range(i3+1, n):
#                         if i4 in [i1, i2, i3]:
#                             continue
#                         x4, y4 = points[i4]
#                         xs, ys = x2 + v13[0], y2+v13[1]
#                         diff = (x4-xs) ** 2 + (y4-ys) ** 2
#                         if diff >= EPS:
#                             continue
#                         square = math.sqrt(v12[0] ** 2 + v12[1] ** 2) * math.sqrt(v13[0] ** 2 + v13[1] ** 2)
#                         result = min(result, square)
#         return result if result != math.inf else 0.0


# Runtime
# 600
# ms
# Beats
# 11.76%
# Analyze Complexity
# Memory
# 17.76
# MB
# Beats
# 96.57%
# https://leetcode.com/problems/minimum-area-rectangle-ii/editorial/?envType=problem-list-v2&envId=array
# class Solution:
#     def minAreaFreeRect(self, points: List[List[int]]) -> float:
#         EPS = 1e-7
#         points = set(map(tuple, points))
#
#         result = math.inf
#
#         for p1, p2, p3 in itertools.permutations(points, 3):
#             p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
#             if p4 in points:
#                 v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
#                 v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
#                 if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
#                     area = abs(v21) * abs(v31)
#                     result = min(result, area)
#         return result if result != math.inf else 0.0

# Runtime
# 19
# ms
# Beats
# 98.28%
# Analyze Complexity
# Memory
# 18.03
# MB
# Beats
# 79.66%
# https://leetcode.com/problems/minimum-area-rectangle-ii/editorial/?envType=problem-list-v2&envId=array
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        points = [complex(*z) for z in points]
        seen = defaultdict(list)
        for P, Q in itertools.combinations(points, 2):
            center = (P + Q) / 2
            radius = abs(center - P)
            seen[center, radius].append(P)

        result = math.inf
        for (center, radius), candidates in seen.items():
            for P, Q in itertools.combinations(candidates, 2):
                result = min(result, abs(P - Q) * abs(P - (2 * center - Q)))
        return result if result != math.inf else 0.0


tests = [
    [[[1,2],[2,1],[1,0],[0,1]], 2.00000],
    [[[0,1],[2,1],[1,1],[1,0],[2,0]], 1.00000],
    [[[0,3],[1,2],[3,1],[1,3],[2,1]], 0],
]

run_functional_tests(Solution().minAreaFreeRect, tests)
