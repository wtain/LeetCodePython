"""
https://leetcode.com/problems/corporate-flight-bookings/

There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.



Example 1:

Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]


Constraints:

1 <= bookings.length <= 20000
1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
1 <= bookings[i][2] <= 10000
"""
from typing import List


# TLE
# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
#         flights = [0] * n
#         for i,j,k in bookings:
#             for f in range(i, j+1):
#                 flights[f-1] += k
#         return flights

# TLE
# class Solution:
#     def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
#         flights = [0] * n
#         for f in range(n):
#             for i,j,k in bookings:
#                 if i <= f+1 <= j:
#                     flights[f] += k
#         return flights

# Runtime: 876 ms, faster than 52.16% of Python3 online submissions for Corporate Flight Bookings.
# Memory Usage: 28.1 MB, less than 91.64% of Python3 online submissions for Corporate Flight Bookings.
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flights = [0] * n
        for i,j,k in bookings:
            flights[i-1] += k
            if j < n:
                flights[j] -= k

        for i in range(1, n):
            flights[i] += flights[i-1]

        return flights



tests = [
    ([[1,2,10],[2,3,20],[2,5,25]], 5, [10,55,45,25,25])
]

for test in tests:
    result = Solution().corpFlightBookings(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))