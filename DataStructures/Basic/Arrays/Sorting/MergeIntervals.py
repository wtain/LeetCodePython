"""
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 88 ms, faster than 53.48% of Python3 online submissions for Merge Intervals.
# Memory Usage: 16.2 MB, less than 54.91% of Python3 online submissions for Merge Intervals.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if not n:
            return []
        intervals.sort()
        result = [intervals[0]]
        for i in range(1, n):
            last = result[-1]
            current = intervals[i]
            if current[0] > last[1]:
                result.append(current)
            else:
                result[-1][1] = max(current[1], last[1])
        return result


tests = [
    [[[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]],
    [[[1,4],[4,5]], [[1,5]]]
]

run_functional_tests(Solution().merge, tests)
