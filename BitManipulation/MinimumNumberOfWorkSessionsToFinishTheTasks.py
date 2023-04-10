"""
https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/

There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].



Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
Example 2:

Input: tasks = [3,1,3,1,1], sessionTime = 8
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish all the tasks except the last one in 3 + 1 + 3 + 1 = 8 hours.
- Second work session: finish the last task in 1 hour.
Example 3:

Input: tasks = [1,2,3,4,5], sessionTime = 15
Output: 1
Explanation: You can finish all the tasks in one work session.


Constraints:

n == tasks.length
1 <= n <= 14
1 <= tasks[i] <= 10
max(tasks[i]) <= sessionTime <= 15
"""
import sys
from collections import defaultdict
from functools import cache, lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         n = len(tasks)
#         result = 0
#         tasks.sort()
#         i, j = 0, n-1
#         while i <= j:
#             capacity = sessionTime
#             while j >= i and capacity >= tasks[j]:
#                 capacity -= tasks[j]
#                 j -= 1
#             while i <= j and capacity >= tasks[i]:
#                 capacity -= tasks[i]
#                 i += 1
#             result += 1
#         return result

# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         n = len(tasks)
#         # dp: mask -> min time
#         # dp(mask | taski) = min(dp(mask) + task[i])
#         masks = defaultdict(int)
#         masks[0] = 0
#         for i in range(n):
#             maski = 1 << i
#             for mask in masks:
#                 if mask & maski:
#                     continue


# Runtime
# 7836 ms
# Beats
# 8.27%
# Memory
# 243.2 MB
# Beats
# 8.27%
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/solutions/1436811/c-java-python-from-straightforward-to-optimized-bitmask-dp-o-2-n-n-clean-concise/
# class Solution:
#     def minSessions(self, tasks: List[int], sessionTime: int) -> int:
#         n = len(tasks)
#
#         def clearbit(x, k):
#             return ~(1 << k) & x
#
#         @cache
#         def dp(mask, remain_time):
#             if mask == 0:
#                 return 0
#             result = n
#             for i in range(n):
#                 if (mask >> i) & 1:
#                     new_mask = clearbit(mask, i)
#                     if tasks[i] <= remain_time:
#                         result = min(result, dp(new_mask, remain_time - tasks[i]))
#                     else:
#                         result = min(result, dp(new_mask, sessionTime - tasks[i])+1)
#             return result
#
#         return dp((1 << n) - 1, 0)


# Runtime
# 1017 ms
# Beats
# 41.32%
# Memory
# 38.9 MB
# Beats
# 28.93%
# https://leetcode.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks/solutions/1436811/c-java-python-from-straightforward-to-optimized-bitmask-dp-o-2-n-n-clean-concise/
class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        n = len(tasks)

        def clearbit(x, k):
            return ~(1 << k) & x

        @cache
        def dp(mask):
            if mask == 0:
                return 0, 0
            result = n
            remain_time = 0
            for i in range(n):
                if (mask >> i) & 1:
                    new_mask = clearbit(mask, i)
                    cnt_session, remain_time_session = dp(new_mask)
                    if tasks[i] <= remain_time_session:
                        remain_time_session -= tasks[i]
                    else:
                        cnt_session += 1
                        remain_time_session = sessionTime - tasks[i]
                    if cnt_session < result or cnt_session == result and remain_time_session > remain_time:
                        result, remain_time = cnt_session, remain_time_session
            return result, remain_time

        return dp((1 << n) - 1)[0]


tests = [
    [[1,5,7,10,3,8,4,2,6,2], 10, 5],
    [[1,2,3], 3, 2],
    [[3,1,3,1,1], 8, 2],
    [[1,2,3,4,5], 15, 1],
]

run_functional_tests(Solution().minSessions, tests)
