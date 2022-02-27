"""
https://leetcode.com/problems/remove-covered-intervals/

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.



Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1


Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 620 ms, faster than 5.20% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.4 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         n = len(intervals)
#         intervals.sort(key=lambda x: (x[0], -x[1]))
#         covered = [False] * n
#         m = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if intervals[j][0] >= intervals[i][1]:
#                     break
#                 if covered[j]:
#                     continue
#                 if intervals[j][1] <= intervals[i][1]:
#                     covered[j] = True
#                     m += 1
#         return n - m


# class Solution:
#     def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
#         n = len(intervals)
#         intervals.sort()
#         if not n:
#             return 0
#         r = intervals[0][1]
#         for i in range(1, n):
#
#         cnt = 1
#         return cnt


# Runtime: 174 ms, faster than 24.16% of Python3 online submissions for Remove Covered Intervals.
# Memory Usage: 14.5 MB, less than 86.23% of Python3 online submissions for Remove Covered Intervals.
# https://leetcode.com/problems/remove-covered-intervals/discuss/1786160/C%2B%2B-oror-O(nlogn)-oror-Custom-2D-vector-sort
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x: (x[0], -x[1]))
        result, prev_pos = 1, 0
        for i in range(1, n):
            if intervals[i][1] > intervals[prev_pos][1]:
                prev_pos = i
                result += 1
        return result


tests = [
    [[[1,3], [3, 5], [1, 6]], 1],
    [[[1,2],[1,4],[3,4]], 1],
    [[[3,10],[4,10],[5,11]], 2],
    [[[1,4],[3,6],[2,8]], 2],
    [[[1,4],[2,3]], 1]
]

run_functional_tests(Solution().removeCoveredIntervals, tests)
