"""
https://leetcode.com/problems/seat-reservation-manager/description/?envType=daily-question&envId=2023-11-06

Design a system that manages the reservation state of n seats that are numbered from 1 to n.

Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats numbered from 1 to n. All seats are initially available.
int reserve() Fetches the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.


Example 1:

Input
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
Output
[null, 1, 2, null, 2, 3, 4, 5, null]

Explanation
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].


Constraints:

1 <= n <= 105
1 <= seatNumber <= n
For each call to reserve, it is guaranteed that there will be at least one unreserved seat.
For each call to unreserve, it is guaranteed that seatNumber will be reserved.
At most 105 calls in total will be made to reserve and unreserve.
"""
import heapq

from sortedcontainers import SortedSet

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# Details
# 450ms
# Beats 50.00%of users with Python3
# Memory
# Details
# 43.98MB
# Beats 67.29%of users with Python3
# class SeatManager:
#
#     def __init__(self, n: int):
#         self.seats = list(range(1, n+1))
#         heapq.heapify(self.seats)
#
#     def reserve(self) -> int:
#         return heapq.heappop(self.seats)
#
#     def unreserve(self, seatNumber: int) -> None:
#         heapq.heappush(self.seats, seatNumber)


# Runtime
# Details
# 368ms
# Beats 98.26%of users with Python3
# Memory
# Details
# 42.48MB
# Beats 95.17%of users with Python3
# https://leetcode.com/problems/seat-reservation-manager/editorial/?envType=daily-question&envId=2023-11-06
# class SeatManager:
#
#     def __init__(self, n: int):
#         self.seats = []
#         self.marker = 1
#
#     def reserve(self) -> int:
#         if self.seats:
#             return heapq.heappop(self.seats)
#         result = self.marker
#         self.marker += 1
#         return result
#
#     def unreserve(self, seatNumber: int) -> None:
#         heapq.heappush(self.seats, seatNumber)


# Runtime
# Details
# 493ms
# Beats 12.07%of users with Python3
# Memory
# Details
# 42.82MB
# Beats 89.54%of users with Python3
# https://leetcode.com/problems/seat-reservation-manager/editorial/?envType=daily-question&envId=2023-11-06
class SeatManager:

    def __init__(self, n: int):
        self.seats = SortedSet()
        self.marker = 1

    def reserve(self) -> int:
        if self.seats:
            return self.seats.pop(0)
        result = self.marker
        self.marker += 1
        return result

    def unreserve(self, seatNumber: int) -> None:
        self.seats.add(seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


tests = [
    [
        ["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"],
        [[5], [], [], [2], [], [], [], [], [5]],
        [null, 1, 2, null, 2, 3, 4, 5, null]
    ]
]

run_object_tests(tests, cls=SeatManager)
