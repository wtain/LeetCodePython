"""
https://leetcode.com/problems/rectangle-area/description/

Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).



Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16


Constraints:

-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 119 ms
# Beats
# 29.72%
# Memory
# 14.1 MB
# Beats
# 26.26%
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def cross_intervals(i1, i2):
            if i1[0] > i2[0]:
                return cross_intervals(i2, i1)
            if i2[0] >= i1[1]:
                return [0, 0]
            return [i2[0], min(i1[1], i2[1])]

        def get_cross(r1, r2):
            wint1 = [r1[0][0], r1[1][0]]
            hint1 = [r1[0][1], r1[1][1]]
            wint2 = [r2[0][0], r2[1][0]]
            hint2 = [r2[0][1], r2[1][1]]

            wint = cross_intervals(wint1, wint2)
            hint = cross_intervals(hint1, hint2)

            return [[wint[0], hint[0]], [wint[1], hint[1]]]

        def area(r):
            return (r[1][0] - r[0][0]) * (r[1][1] - r[0][1])

        p1, p2, p3, p4 = [ax1, ay1], [ax2, ay2], [bx1, by1], [bx2, by2]

        r1, r2 = [p1, p2], [p3, p4]

        return area(r1) + area(r2) - area(get_cross(r1, r2))


tests = [
    [-3, 0, 3, 4, 0, -1, 9, 2, 45],
    [-2, -2, 2, 2, -2, -2, 2, 2, 16],

    [-2, -2, 2, 2, 3, 3, 4, 4, 17]
]

run_functional_tests(Solution().computeArea, tests)
