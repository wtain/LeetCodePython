"""
https://leetcode.com/problems/largest-triangle-area/
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.

Runtime: 108 ms, faster than 92.64% of Python3 online submissions for Largest Triangle Area.
Memory Usage: 14.3 MB, less than 32.56% of Python3 online submissions for Largest Triangle Area.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        max_area = 0.0
        for i in range(n-2):
            x1, y1 = points[i]
            for j in range(i+1, n-1):
                x2, y2 = points[j]
                for k in range(j+1, n):
                    x3, y3 = points[k]
                    area = 0.5 * abs((x2-x1) * (y3 - y1) - (y2-y1) * (x3-x1))
                    max_area = max(max_area, area)
        return max_area


tests = [
    [[[0,0],[0,1],[1,0],[0,2],[2,0]], 2]
]

run_functional_tests(Solution().largestTriangleArea, tests)
