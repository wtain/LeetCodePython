"""
https://leetcode.com/problems/car-pooling/

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.



Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true


Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 112 ms, faster than 17.60% of Python3 online submissions for Car Pooling.
# Memory Usage: 14.9 MB, less than 51.55% of Python3 online submissions for Car Pooling.
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         trips = sorted([(src, cnt) for cnt, src, dst in trips] + [(dst, -cnt) for cnt, src, dst in trips])
#         current = 0
#         for t, d in trips:
#             current += d
#             if current > capacity:
#                 return False
#         return True


# Runtime: 77 ms, faster than 31.15% of Python3 online submissions for Car Pooling.
# Memory Usage: 15 MB, less than 18.85% of Python3 online submissions for Car Pooling.
# Runtime: 56 ms, faster than 99.22% of Python3 online submissions for Car Pooling.
# Memory Usage: 14.9 MB, less than 18.85% of Python3 online submissions for Car Pooling.
# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         current = 0
#         outs = []
#         for cnt, src, dst in sorted(trips, key=lambda x: x[1]):
#             while outs and outs[0][0] <= src:
#                 out_pos, out_cnt = heapq.heappop(outs)
#                 current -= out_cnt
#             current += cnt
#             if current > capacity:
#                 return False
#             heapq.heappush(outs, (dst, cnt))
#         return True


# Runtime: 60 ms, faster than 95.94% of Python3 online submissions for Car Pooling.
# Memory Usage: 14.9 MB, less than 18.85% of Python3 online submissions for Car Pooling.
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        t = [0] * 1001
        for cnt, src, dst in trips:
            t[src] += cnt
            t[dst] -= cnt
        current = 0
        for v in t:
            current += v
            if current > capacity:
                return False
        return True


tests = [
    [[[9,0,1],[3,3,7]], 4, False],
    [[[7,5,6],[6,7,8],[10,1,6]], 16, False],
    [[[2,1,5],[3,5,7]], 3, True],
    [[[2,1,5],[3,3,7]], 4, False],
    [[[2,1,5],[3,3,7]], 5, True]
]

run_functional_tests(Solution().carPooling, tests)
