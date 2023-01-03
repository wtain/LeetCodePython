"""
https://leetcode.com/problems/my-calendar-ii/description/

You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.


Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked.
myCalendarTwo.book(50, 60); // return True, The event can be booked.
myCalendarTwo.book(10, 40); // return True, The event can be double booked.
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.


Constraints:

0 <= start < end <= 109
At most 1000 calls will be made to book.
"""
from sortedcontainers import SortedList

from Common.Constants import true, false, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 1028 ms
# Beats
# 71.11%
# Memory
# 15.3 MB
# Beats
# 11.67%
class MyCalendarTwo:

    def __init__(self):
        self.starts = SortedList([[0, 0]])
        self.res = 0

    def split(self, x: int):
        idx = self.starts.bisect_left([x, 0])
        if idx < len(self.starts) and self.starts[idx][0] == x:
            return idx
        self.starts.add([x, self.starts[idx - 1][1]])

    def book(self, start: int, end: int) -> bool:
        self.split(start)
        self.split(end)
        if any(interval[1] >= 2 for interval in self.starts.irange([start, 0], [end, 0], (True, False))):
            return False
        for interval in self.starts.irange([start, 0], [end, 0], (True, False)):
            interval[1] += 1
            self.res = max(self.res, interval[1])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)


tests = [
    [
        ["MyCalendarTwo", "book", "book", "book", "book", "book", "book"],
        [[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]],
        [null, true, true, true, false, true, true]
    ]
]

run_object_tests(tests, cls=MyCalendarTwo)
