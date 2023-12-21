"""
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/description/?envType=daily-question&envId=2023-12-21

Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between two points such that no points are inside the area.

A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height). The widest vertical area is the one with the maximum width.

Note that points on the edge of a vertical area are not considered included in the area.



Example 1:

​
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: Both the red and the blue area are optimal.
Example 2:

Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
Output: 3


Constraints:

n == points.length
2 <= n <= 105
points[i].length == 2
0 <= xi, yi <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 695
# ms
# Beats
# 100.00%
# of users with Python3
# Memory
# 59.96
# MB
# Beats
# 6.69%
# of users with Python3
class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[0])
        n = len(points)
        result = 0
        for i in range(1, n):
            p1 = points[i-1]
            p2 = points[i]
            result = max(result, p2[0] - p1[0])
        return result


tests = [
    [[[8,7],[9,9],[7,4],[9,7]], 1],
    [[[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]], 3],
]

run_functional_tests(Solution().maxWidthOfVerticalArea, tests)

