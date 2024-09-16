"""
https://leetcode.com/problems/minimum-time-difference/description/?envType=daily-question&envId=2024-09-16

Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.


Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0


Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 86
# ms
# Beats
# 8.29%
# Analyze Complexity
# Memory
# 19.47
# MB
# Beats
# 97.94%
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = [int(t[:2]) * 60 + int(t[3:5]) for t in timePoints]
        times.sort()
        minInDay = 24 * 60
        minDiff = minInDay
        for i in range(len(times)):
            i2 = i + 1
            if i2 == len(times):
                diff = minInDay + times[0] - times[i]
            else:
                diff = times[i2] - times[i]
            minDiff = min(minDiff, diff)
        return minDiff


tests = [
    [["23:59","00:00"], 1],
    [["00:00","23:59","00:00"], 0],
]

run_functional_tests(Solution().findMinDifference, tests)
