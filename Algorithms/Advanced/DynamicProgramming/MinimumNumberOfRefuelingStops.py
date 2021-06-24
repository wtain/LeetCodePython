"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3776/
https://leetcode.com/problems/minimum-number-of-refueling-stops/

A car travels from a starting position to a destination which is target miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas station that is station[i][0] miles east of the starting position, and has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there.  If the car reaches the destination with 0 fuel left, it is still considered to have arrived.



Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation:
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach the target.
We made 2 refueling stops along the way, so we return 2.


Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# https://leetcode.com/problems/minimum-number-of-refueling-stops/solution/
# Runtime: 1048 ms, faster than 29.87% of Python3 online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 14.7 MB, less than 36.85% of Python3 online submissions for Minimum Number of Refueling Stops.
# class Solution:
#     def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
#         dp = [startFuel] + [0] * len(stations)
#         for i, (loc, cap) in enumerate(stations):
#             for t in range(i, -1, -1):
#                 if dp[t] >= loc:
#                     dp[t+1] = max(dp[t+1], dp[t] + cap)
#         for i, d in enumerate(dp):
#             if d >= target:
#                 return i
#         return -1


# Runtime: 116 ms, faster than 89.45% of Python3 online submissions for Minimum Number of Refueling Stops.
# Memory Usage: 14.5 MB, less than 88.91% of Python3 online submissions for Minimum Number of Refueling Stops.
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        pq = []
        stations.append((target, float('inf')))
        res = prev = 0
        tank = startFuel
        for loc, cap in stations:
            tank -= loc - prev
            while pq and tank < 0:
                tank += -heapq.heappop(pq)
                res += 1
            if tank < 0:
                return -1
            heapq.heappush(pq, -cap)
            prev = loc
        return res


tests = [
    [1, 1, [], 0],
    [100, 1, [[10,100]], -1],
    [100, 10, [[10,60],[20,30],[30,30],[60,40]], 2]
]

run_functional_tests(Solution().minRefuelStops, tests)