"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/604/week-2-june-8th-june-14th/3774/
https://leetcode.com/problems/my-calendar-i/

Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to both events.)

For each call to the method MyCalendar.book, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:

MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation:
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.


Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""

from Common.Constants import true, false, null
from Common.ObjectTestingUtils import run_object_tests


# WRONG
# from sortedcontainers import SortedList
# class MyCalendar:
#
#     def __init__(self):
#         self.meetings = SortedList([])
#
#     def book(self, start: int, end: int) -> bool:
#         i = self.meetings.bisect_right([start])
#         if i == len(self.meetings) or \
#                 self.meetings[i][1] <= end or \
#                 self.meetings[i][0] <= start and \
#                 (i+1 == len(self.meetings) or self.meetings[i+1][1] >= end):
#             self.meetings.add([end, start])
#             print(list(map(lambda x: (x[1], x[0]), self.meetings)))
#             return True
#         return False

# from sortedcontainers import SortedList
# class MyCalendar:
#
#     def __init__(self):
#         self.starts = SortedList([])
#         self.ends = SortedList([])
#
#     def book(self, start: int, end: int) -> bool:
#         n = len(self.starts)
#         i1 = self.ends.bisect_right(start)
#         i2 = self.starts.bisect_left(end)
#         print(start, end)
#         print(list(zip(self.starts, self.ends)))
#         print(i1, i2)
#         if abs(i1-i2) > 1:
#             return False
#         if n > 0:
#             if i1 < n and self.ends[i1] > start:
#                 return False
#             if i2+1 < n and self.starts[i2+1] < end:
#                 return False
#         self.starts.add(start)
#         self.ends.add(end)
#         return True


# Runtime: 576 ms, faster than 37.87% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.8 MB, less than 87.92% of Python3 online submissions for My Calendar I.
# class MyCalendar:
#
#     def __init__(self):
#         self.intervals = []
#
#     def book(self, start: int, end: int) -> bool:
#         for s,e in self.intervals:
#             if end > s and start < e:
#                 return False
#         self.intervals.append([start, end])
#         return True

# from sortedcontainers import SortedList
# class MyCalendar:
#
#     def __init__(self):
#         self.intervals = SortedList([])
#
#     def book(self, start: int, end: int) -> bool:
#         i = self.intervals.bisect_left([start])
#         print(self.intervals)
#         print(i)
#         if i < len(self.intervals) and self.intervals[i][0] < end and self.intervals[i][1] > start:
#             return False
#         self.intervals.add([end, start])
#         return True


# Runtime: 396 ms, faster than 41.67% of Python3 online submissions for My Calendar I.
# Memory Usage: 14.8 MB, less than 87.92% of Python3 online submissions for My Calendar I.
# class MyCalendar:
#
#     class Node:
#         def __init__(self, start, end):
#             self.start = start
#             self.end = end
#             self.left = self.right = None
#
#         def insert(self, node):
#             if node.start >= self.end:
#                 if not self.right:
#                     self.right = node
#                     return True
#                 return self.right.insert(node)
#             elif node.end <= self.start:
#                 if not self.left:
#                     self.left = node
#                     return True
#                 return self.left.insert(node)
#             else:
#                 return False
#
#     def __init__(self):
#         self.root = None
#
#     def book(self, start: int, end: int) -> bool:
#         node = MyCalendar.Node(start, end)
#         if self.root is None:
#             self.root = node
#             return True
#         return self.root.insert(node)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)


# Runtime: 300 ms, faster than 49.31% of Python3 online submissions for My Calendar I.
# Memory Usage: 15.3 MB, less than 5.97% of Python3 online submissions for My Calendar I.
# from sortedcontainers import SortedList
# class MyCalendar:
#
#     def __init__(self):
#         self.intervals = SortedList([])
#
#     @staticmethod
#     def rangesCross(r1: List[int], r2: List[int]) -> bool:
#         return r2[0] <= r1[0] < r2[1] or r2[0] < r1[1] < r2[1] or \
#                r1[0] <= r2[0] < r1[1] or r1[0] < r2[1] < r1[1]
#
#     def book(self, start: int, end: int) -> bool:
#         n = len(self.intervals)
#         i = self.intervals.bisect_left([start])
#         j = i
#         i -= 1
#         range = [start, end]
#         # print("Inserting", [start, end])
#         # print("into", list(map(lambda x: [x[0], x[1]], self.intervals)))
#         # if 0 <= i < n:
#         #     print("Candidate: ", [self.intervals[i][0], self.intervals[i][1]])
#         # if 0 <= j < n:
#         #     print("Next: ", [self.intervals[j][0], self.intervals[j][1]])
#         if 0 <= j < n and self.rangesCross(self.intervals[j], range) or \
#            0 <= i < n and self.rangesCross(self.intervals[i], range):
#             return False
#         self.intervals.add(range)
#         return True

# https://leetcode.com/problems/my-calendar-i/discuss/1262532/Python-Sortedlist-solution-explained
# Runtime: 348 ms, faster than 44.31% of Python3 online submissions for My Calendar I.
# Memory Usage: 15.4 MB, less than 5.97% of Python3 online submissions for My Calendar I.
from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.intervals = SortedList([])

    def book(self, start: int, end: int) -> bool:
        i1 = self.intervals.bisect_right(start)
        i2 = self.intervals.bisect_left(end)
        if i1 == i2 and i1 % 2 == 0:
            self.intervals.add(start)
            self.intervals.add(end)
            return True
        return False


tests = [
    [
        ["MyCalendar","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"],
        [[],[20,29],[13,22],[44,50],[1,7],[2,10],[14,20],[19,25],[36,42],[45,50],[47,50],[39,45],[44,50],[16,25],[45,50],[45,50],[12,20],[21,29],[11,20],[12,17],[34,40],[10,18],[38,44],[23,32],[38,44],[15,20],[27,33],[34,42],[44,50],[35,40],[24,31]],
        [null,true,false,true,true,false,true,false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false]
    ],
    [
        ["MyCalendar","book","book","book","book","book","book","book","book","book","book"],
        [[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]],
        [null,true,true,false,false,true,false,true,true,true,false]
    ],
    [
        ["MyCalendar", "book", "book", "book"],
        [[], [10, 20], [15, 25], [20, 30]],
        [None, true, false, true]
    ]
]

run_object_tests(tests, cls=MyCalendar)