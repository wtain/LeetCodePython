"""
https://leetcode.com/problems/check-if-it-is-a-straight-line/description/

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 82 ms
# Beats
# 20.18%
# Memory
# 16.9 MB
# Beats
# 8%
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        v1x = coordinates[1][0] - coordinates[0][0]
        v1y = coordinates[1][1] - coordinates[0][1]

        for i in range(2, n):
            v2x = coordinates[i][0] - coordinates[0][0]
            v2y = coordinates[i][1] - coordinates[0][1]

            if v1x * v2y - v1y * v2x:
                return False
        return True


tests = [
    [[[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]], True],
    [[[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]], False],
    [[[1,2],[2,3]], True],
]

run_functional_tests(Solution().checkStraightLine, tests)
