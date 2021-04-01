"""
https://leetcode.com/problems/maximize-distance-to-closest-person/

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.



Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1


Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
"""
from typing import List


# Runtime: 140 ms, faster than 49.28% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.6 MB, less than 80.01% of Python3 online submissions for Maximize Distance to Closest Person.
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        dists = [0] * n
        prev = -n
        for i in range(n):
            if seats[i] == 1:
                prev = i
            dists[i] = i - prev
        prev = 2 * n
        for i in range(n-1,-1,-1):
            if seats[i] == 1:
                prev = i
            dists[i] = min(prev - i, dists[i])
        return max(dists)


tests = [
    ([1,0,0,0,1,0,1], 2),
    ([1,0,0,0], 3),
    ([0,1], 1)
]

for test in tests:
    result = Solution().maxDistToClosest(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))