"""
https://leetcode.com/problems/longest-well-performing-interval/

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.



Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0


Constraints:

1 <= hours.length <= 104
0 <= hours[i] <= 16
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         wp = [1 if h > 8 else -1 for h in hours]
#         start, end = -1, 0
#         longest = 0
#         n = len(wp)
#         current = 0
#         while end < n:
#             while end < n and current >= 0:
#                 current += wp[end]
#                 if current > 0:
#                     longest = max(longest, end - start)
#                 end += 1
#             current = 0
#             start = end-1
#
#         return longest

# class Solution:
#     def longestWPI(self, hours: List[int]) -> int:
#         wp = [1 if h > 8 else -1 for h in hours]
#         start, end = -1, 0
#         longest = 0
#         n = len(wp)
#         current = 0
#         while end < n:
#             while end < n and current >= 0:
#                 current += wp[end]
#                 if current > 0:
#                     longest = max(longest, end - start)
#                 end += 1
#             while start < end and current < 0:
#
#         return longest


# Runtime
# 217 ms
# Beats
# 72.78%
# Memory
# 14.6 MB
# Beats
# 80%
# https://leetcode.com/problems/longest-well-performing-interval/solutions/334565/java-c-python-o-n-solution-life-needs-996-and-669/
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        result = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score += (1 if h > 8 else -1)
            if score > 0:
                result = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                result = max(result, i - seen[score-1])
        return result


tests = [
    [[6,9,9], 3],
    [[6,6,9], 1],
    [[9,9,6,0,6,6,9], 3],
    [[6,6,6], 0],
]

run_functional_tests(Solution().longestWPI, tests)
