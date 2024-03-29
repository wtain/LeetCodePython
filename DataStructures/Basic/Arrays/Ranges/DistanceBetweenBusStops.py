"""
https://leetcode.com/problems/distance-between-bus-stops/
A bus has n stops numbered from 0 to n - 1 that form a circle. We know the distance between all pairs of neighboring stops where distance[i] is the distance between the stops number i and (i + 1) % n.

The bus goes along both directions i.e. clockwise and counterclockwise.

Return the shortest distance between the given start and destination stops.



Example 1:



Input: distance = [1,2,3,4], start = 0, destination = 1
Output: 1
Explanation: Distance between 0 and 1 is 1 or 9, minimum is 1.


Example 2:



Input: distance = [1,2,3,4], start = 0, destination = 2
Output: 3
Explanation: Distance between 0 and 2 is 3 or 7, minimum is 3.


Example 3:



Input: distance = [1,2,3,4], start = 0, destination = 3
Output: 4
Explanation: Distance between 0 and 3 is 6 or 4, minimum is 4.


Constraints:

1 <= n <= 10^4
distance.length == n
0 <= start, destination < n
0 <= distance[i] <= 10^4
"""
from typing import List


# Runtime: 68 ms, faster than 8.84% of Python3 online submissions for Distance Between Bus Stops.
# Memory Usage: 15.2 MB, less than 38.76% of Python3 online submissions for Distance Between Bus Stops.
class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)

        def dist(start: int, destination: int) -> int:
            p1 = min(start, destination)
            p2 = max(start, destination)
            nonlocal distance, n
            res = 0
            for i in range(p1, p2):
                res += distance[i % n]
            return res

        p1 = min(start, destination)
        p2 = max(start, destination)

        return min(dist(p1, p2), dist(p2, n+p1))


tests = [
    ([7,10,1,12,11,14,5,0], 7, 2, 17),

    ([1,2,3,4], 0, 1, 1),
    ([1,2,3,4], 0, 2, 3),
    ([1,2,3,4], 0, 3, 4),
]

for test in tests:
    result = Solution().distanceBetweenBusStops(test[0], test[1], test[2])
    if result == test[3]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
