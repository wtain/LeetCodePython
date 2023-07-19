"""
https://leetcode.com/problems/non-overlapping-intervals/description/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 1523ms
# Beats 22.81%of users with Python3
# Memory
# Details
# 55.27mb
# Beats 78.77%of users with Python3
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        if not n:
            return 0
        last_end = intervals[0][0]
        max_num_intervals = 0
        for start, end in intervals:
            if last_end > start:
                last_end = min(last_end, end)
            else:
                max_num_intervals += 1
                last_end = end
        return n - max_num_intervals


tests = [
    [[[1,2],[2,3],[3,4],[1,3]], 1],
    [[[1,2],[1,2],[1,2]], 2],
    [[[1,2],[2,3]], 0],
]

run_functional_tests(Solution().eraseOverlapIntervals, tests)
