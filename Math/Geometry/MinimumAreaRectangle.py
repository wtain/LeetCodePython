"""
https://leetcode.com/problems/minimum-area-rectangle/description/?envType=problem-list-v2&envId=array

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.



Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2


Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.
"""
import math
from collections import defaultdict
from typing import List

from sortedcontainers import SortedList

from Common.ObjectTestingUtils import run_functional_tests


"""
Runtime
681
ms
Beats
74.21%
Analyze Complexity
Memory
18.24
MB
Beats
28.12%
"""
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        Xs, Ys = defaultdict(SortedList), defaultdict(SortedList)
        for i, p in enumerate(points):
            x, y = p
            Xs[x].add(i)
            Ys[y].add(i)
        N = len(points)
        min_area = math.inf
        for i in range(N):
            x1 = points[i][0]
            y1 = points[i][1]
            for j in range(i+1, N):
                x2 = points[j][0]
                y2 = points[j][1]
                w = abs(x2 - x1)
                h = abs(y2 - y1)
                if not w or not h:
                    continue
                if w*h > min_area:
                    continue
                if not set.intersection(set(Xs[x1]), set(Ys[y2])):
                    continue
                if not set.intersection(set(Xs[x2]), set(Ys[y1])):
                    continue
                min_area = w*h

        return min_area if min_area < math.inf else 0


tests = [
    [[[3,2],[3,1],[4,4],[1,1],[4,3],[0,3],[0,2],[4,0]], 0],
    [[[1,1],[1,3],[3,1],[3,3],[2,2]], 4],
    [[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]], 2],
]

run_functional_tests(Solution().minAreaRect, tests)
