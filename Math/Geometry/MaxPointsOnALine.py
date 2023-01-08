"""
https://leetcode.com/problems/max-points-on-a-line/description/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
import math
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3156 ms
# Beats
# 6.9%
# Memory
# 13.8 MB
# Beats
# 99.64%
# class Solution:
#     def maxPoints(self, points: List[List[int]]) -> int:
#         n = len(points)
#         if n <= 2:
#             return n
#         max_points_in_line = 0
#         for i in range(n-1):
#             x1, y1 = points[i][0], points[i][1]
#             for j in range(i+1, n):
#                 x2, y2 = points[j][0], points[j][1]
#                 points_in_line = 0
#                 for k in range(n):
#                     x, y = points[k][0], points[k][1]
#                     if (x-x1)*(y2-y1) == (y-y1)*(x2-x1):
#                         points_in_line += 1
#                 max_points_in_line = max(max_points_in_line, points_in_line)
#
#         return max_points_in_line


# Runtime
# 364 ms
# Beats
# 26.24%
# Memory
# 14.1 MB
# Beats
# 53.74%
# https://leetcode.com/problems/max-points-on-a-line/solutions/2910679/max-points-on-a-line/
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        max_points_in_line = 0
        for i in range(n):
            x1, y1 = points[i][0], points[i][1]
            counts = defaultdict(int)
            for j in range(n):
                if i == j:
                    continue
                x2, y2 = points[j][0], points[j][1]
                counts[math.atan2(y2-y1, x2-x1)] += 1
                max_points_in_line = max(max_points_in_line, max(counts.values())+1)

        return max_points_in_line


tests = [
    [[[1,1],[2,2],[3,3]], 3],
    [[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4],
]

run_functional_tests(Solution().maxPoints, tests)
