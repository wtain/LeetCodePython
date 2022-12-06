"""
https://leetcode.com/problems/determine-if-two-events-have-conflict/

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

event1 = [startTime1, endTime1] and
event2 = [startTime2, endTime2].
Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.



Example 1:

Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
Output: true
Explanation: The two events intersect at time 2:00.
Example 2:

Input: event1 = ["01:00","02:00"], event2 = ["01:20","03:00"]
Output: true
Explanation: The two events intersect starting from 01:20 to 02:00.
Example 3:

Input: event1 = ["10:00","11:00"], event2 = ["14:00","15:00"]
Output: false
Explanation: The two events do not intersect.


Constraints:

evnet1.length == event2.length == 2.
event1[i].length == event2[i].length == 5
startTime1 <= endTime1
startTime2 <= endTime2
All the event times follow the HH:MM format.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 47 ms
# Beats
# 75.79%
# Memory
# 13.8 MB
# Beats
# 73.59%
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:

        def parse_time(timeString: str):
            return int(timeString[:2]) * 60 + int(timeString[3:])

        def parse_event(event):
            t1 = parse_time(event[0])
            t2 = parse_time(event[1])
            return t1, t2

        start1, end1 = parse_event(event1)
        start2, end2 = parse_event(event2)

        return start1 <= start2 <= end1 or start1 <= end2 <= end1 or \
               start2 <= start1 <= end2 or start2 <= end1 <= end2


tests = [
    [["15:19","17:56"], ["14:11","20:02"], True],
    [["01:15","02:00"], ["02:00","03:00"], True],
    [["01:00","02:00"], ["01:20","03:00"], True],
    [["10:00","11:00"], ["14:00","15:00"], False]
]

run_functional_tests(Solution().haveConflict, tests)
