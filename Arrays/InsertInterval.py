"""
https://leetcode.com/problems/insert-interval/
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.



Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]
Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]
Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]


Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals is sorted by intervals[i][0] in ascending order.
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

Runtime: 64 ms, faster than 99.60% of Python3 online submissions for Insert Interval.
Memory Usage: 17.3 MB, less than 72.92% of Python3 online submissions for Insert Interval.
"""
# from bisect import bisect_left
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        result = []
        inside = False
        added = False
        for interval in intervals:
            si, ei = interval
            if not inside:
                if si > end and not added:
                    result.append([start, end])
                    result.append(interval)
                    added = True
                elif si > end or ei < start:
                    result.append(interval)
                else:
                    inside = True
                    start = min(start, si)
                    end = max(end, ei)
            else:
                if end < si:
                    inside = False
                    added = True
                    result.append([start, end])
                    result.append(interval)
                elif end < ei:
                    result.append([start, ei])
                    added = True
                    inside = False
        if inside or not added:
            result.append([start, end])

        return result

# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         start, end = newInterval
#
#         def findInterval(p: int) -> int:
#             for i, interval in enumerate(intervals):
#                 si, ei = interval
#                 if si <= p <= ei:
#                     return i
#             return -1
#
#         start_idx = findInterval(start)
#         end_idx = findInterval(end)
#
#         return intervals



# Solution().insert([[1,3],[6,9]], [2,5])

tests = [
    ([[1,5]], [0,0], [[0,0],[1,5]]),

    ([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
    ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
    ([], [5,7], [[5,7]]),
    ([[1,5]], [2,3], [[1,5]]),
    ([[1,5]], [2,7], [[1,7]])
]

for test in tests:
    result = Solution().insert(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))