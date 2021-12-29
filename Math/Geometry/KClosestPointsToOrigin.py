"""
https://leetcode.com/problems/k-closest-points-to-origin/

Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).



Example 1:


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.


Constraints:

1 <= k <= points.length <= 104
-104 < xi, yi < 104
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 608 ms, faster than 98.10% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.5 MB, less than 99.08% of Python3 online submissions for K Closest Points to Origin.
# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         return sorted(points, key=lambda p: p[0]**2 + p[1]**2)[:k]


# Runtime: 1220 ms, faster than 5.01% of Python3 online submissions for K Closest Points to Origin.
# Memory Usage: 19.8 MB, less than 76.94% of Python3 online submissions for K Closest Points to Origin.
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        for p in points:
            heapq.heappush(result, [-(p[0]**2+p[1]**2), p])
            if len(result) > k:
                heapq.heappop(result)
        res2 = []
        for i in range(k):
            d, p = heapq.heappop(result)
            res2 = [p] + res2
        return res2


tests = [
    [[[1,3],[-2,2]], 1, [[-2,2]]],
    [[[3,3],[5,-1],[-2,4]], 2, [[3,3],[-2,4]]]
]

run_functional_tests(Solution().kClosest, tests)
