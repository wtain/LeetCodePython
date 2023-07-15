"""
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description/

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.



Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.


Constraints:

1 <= k <= events.length
1 <= k * events.length <= 106
1 <= startDayi <= endDayi <= 109
1 <= valuei <= 106
"""
import bisect
from collections import defaultdict
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         events.sort()
#         dp = defaultdict(int)
#         for s, e, v in events:
#             pass
#         return 0


# Runtime
# Details
# 931ms
# Beats 71.85%of users with Python3
# Memory
# Details
# 201.16mb
# Beats 15.56%of users with Python3
# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/editorial/
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         events.sort()
#         n = len(events)
#         starts = [start for start, end, value in events]
#
#         @cache
#         def dfs(cur_index, count):
#             if count == 0 or cur_index == n:
#                 return 0
#             next_index = bisect.bisect_right(starts, events[cur_index][1])
#             return max(dfs(cur_index+1, count), events[cur_index][2] + dfs(next_index, count-1))
#
#         return dfs(0, k)


# Runtime
# Details
# 1251ms
# Beats 18.52%of users with Python3
# Memory
# Details
# 62.44mb
# Beats 84.44%of users with Python3
# # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/editorial/
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         n = len(events)
#         dp = [[0] * (n+1) for _ in range(k+1)]
#         events.sort()
#         starts = [start for start, end, value in events]
#         for cur_index in range(n-1, -1, -1):
#             for count in range(1, k+1):
#                 next_index = bisect.bisect_right(starts, events[cur_index][1])
#                 dp[count][cur_index] = max(dp[count][cur_index+1], events[cur_index][2] + dp[count-1][next_index])
#         return dp[k][0]


# Runtime
# Details
# 890ms
# Beats 85.93%of users with Python3
# Memory
# Details
# 202.24mb
# Beats 14.82%of users with Python3
# # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/editorial/
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         events.sort()
#         n = len(events)
#         starts = [start for start, end, value in events]
#         next_indices = [bisect.bisect_right(starts, events[cur_index][1]) for cur_index in range(n)]
#
#         @cache
#         def dfs(cur_index, count):
#             if count == 0 or cur_index == n:
#                 return 0
#             next_index = next_indices[cur_index]
#             return max(dfs(cur_index+1, count), events[cur_index][2] + dfs(next_index, count-1))
#
#         return dfs(0, k)


# Runtime
# Details
# 1064ms
# Beats 49.63%of users with Python3
# Memory
# Details
# 62.53mb
# Beats 71.11%of users with Python3
# # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/editorial/
# class Solution:
#     def maxValue(self, events: List[List[int]], k: int) -> int:
#         n = len(events)
#         dp = [[0] * (n+1) for _ in range(k+1)]
#         events.sort()
#         starts = [start for start, end, value in events]
#         for cur_index in range(n-1, -1, -1):
#             next_index = bisect.bisect_right(starts, events[cur_index][1])
#             for count in range(1, k+1):
#                 dp[count][cur_index] = max(dp[count][cur_index+1], events[cur_index][2] + dp[count-1][next_index])
#         return dp[k][0]


# Runtime
# Details
# 943ms
# Beats 67.41%of users with Python3
# Memory
# Details
# 158.41mb
# Beats 48.15%of users with Python3
# # https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/editorial/
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = [[-1] * n for _ in range(k+1)]

        def dfs(cur_index, count, prev_ending_time):
            if count == k or cur_index == n:
                return 0
            if events[cur_index][0] <= prev_ending_time:
                return dfs(cur_index+1, count, prev_ending_time)
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]
            result = max(dfs(cur_index+1, count, prev_ending_time), dfs(cur_index+1, count+1, events[cur_index][1]) + events[cur_index][2])
            dp[count][cur_index] = result
            return result

        return dfs(0, 0, -1)


tests = [
    [[[1,2,4],[3,4,3],[2,3,1]], 2, 7],
    [[[1,2,4],[3,4,3],[2,3,10]], 2, 10],
    [[[1,1,1],[2,2,2],[3,3,3],[4,4,4]], 3, 9],
]

run_functional_tests(Solution().maxValue, tests)
