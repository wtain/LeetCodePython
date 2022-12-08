"""
https://leetcode.com/problems/valid-square/

Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).



Example 1:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true
Example 2:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false
Example 3:

Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true


Constraints:

p1.length == p2.length == p3.length == p4.length == 2
-104 <= xi, yi <= 104
"""
from itertools import product
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 79 ms
# Beats
# 14.47%
# Memory
# 13.9 MB
# Beats
# 51.20%
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:

        def distance2(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        points = [p1, p2, p3, p4]
        indexes = [[i, j] for i, j in product(range(4), range(4)) if j > i]
        distances2 = [
                    [distance2(points[i], points[j]), i, j]
                for i, j in indexes
        ]
        distances2.sort()
        if distances2[0][0] == 0:
            return False
        if distances2[0][0] != distances2[3][0]:
            return False
        if distances2[4][0] != distances2[5][0]:
            return False
        return True


tests = [
    [[0,0], [13,0], [5,12], [18,12], False],
    [[0,0], [0,0], [0,0], [0,0], False],
    [[0,0], [1,1], [1,0], [0,1], True],
    [[0,0], [1,1], [1,0], [0,12], False],
    [[1,0], [-1,0], [0,1], [0,-1], True]
]

run_functional_tests(Solution().validSquare, tests)
