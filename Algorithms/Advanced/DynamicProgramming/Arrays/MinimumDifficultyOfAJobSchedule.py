"""
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/description/

You want to schedule a list of jobs in d days. Jobs are dependent (i.e To work on the ith job, you have to finish all the jobs j where 0 <= j < i).

You have to finish at least one task every day. The difficulty of a job schedule is the sum of difficulties of each day of the d days. The difficulty of a day is the maximum difficulty of a job done on that day.

You are given an integer array jobDifficulty and an integer d. The difficulty of the ith job is jobDifficulty[i].

Return the minimum difficulty of a job schedule. If you cannot find a schedule for the jobs return -1.



Example 1:


Input: jobDifficulty = [6,5,4,3,2,1], d = 2
Output: 7
Explanation: First day you can finish the first 5 jobs, total difficulty = 6.
Second day you can finish the last job, total difficulty = 1.
The difficulty of the schedule = 6 + 1 = 7
Example 2:

Input: jobDifficulty = [9,9,9], d = 4
Output: -1
Explanation: If you finish a job per day you will still have a free day. you cannot find a schedule for the given jobs.
Example 3:

Input: jobDifficulty = [1,1,1], d = 3
Output: 3
Explanation: The schedule is one job per day. total difficulty will be 3.


Constraints:

1 <= jobDifficulty.length <= 300
0 <= jobDifficulty[i] <= 1000
1 <= d <= 10
"""
from functools import lru_cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2658 ms
# Beats
# 29.39%
# Memory
# 14.9 MB
# Beats
# 53.21%
# https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/solutions/490316/java-c-python3-dp-o-nd-solution/
# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         n = len(jobDifficulty)
#         if n < d:
#             return -1
#
#         @lru_cache(None)
#         def dfs(i, d):
#             if d == 1:
#                 return max(jobDifficulty[i:])
#             res, mx = float('inf'), 0
#             for j in range(i, n-d+1):
#                 mx = max(mx, jobDifficulty[j])
#                 res = min(res, mx + dfs(j+1, d-1))
#             return res
#
#         return dfs(0, d)


# Runtime
# 2456 ms
# Beats
# 33.70%
# Memory
# 13.9 MB
# Beats
# 93.73%
# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         n, inf = len(jobDifficulty), float('inf')
#         dp = [[inf] * n + [0] for _ in range(d+1)]
#         for d in range(1, d+1):
#             for i in range(n - d + 1):
#                 maxd = 0
#                 for j in range(i, n-d+1):
#                     maxd = max(maxd, jobDifficulty[j])
#                     dp[d][i] = min(dp[d][i], maxd + dp[d-1][j+1])
#         return dp[d][0] if dp[d][0] < inf else -1


# Runtime
# 1080 ms
# Beats
# 83.82%
# Memory
# 14 MB
# Beats
# 93.73%
# class Solution:
#     def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
#         n, inf = len(jobDifficulty), float('inf')
#         if n < d:
#             return -1
#         dp = [inf] * n + [0]
#         for d in range(1, d+1):
#             for i in range(n - d + 1):
#                 maxd, dp[i] = 0, inf
#                 for j in range(i, n-d+1):
#                     maxd = max(maxd, jobDifficulty[j])
#                     dp[i] = min(dp[i], maxd + dp[j+1])
#         return dp[0]


# Runtime
# 121 ms
# Beats
# 97.5%
# Memory
# 13.9 MB
# Beats
# 99.9%
class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp, dp2 = [float('inf')] * n, [0] * n
        for d in range(d):
            st = []
            for i in range(d, n):
                dp2[i] = dp[i-1] + jobDifficulty[i] if i else jobDifficulty[i]
                while st and jobDifficulty[st[-1]] <= jobDifficulty[i]:
                    j = st.pop()
                    dp2[i] = min(dp2[i], dp2[j] - jobDifficulty[j] + jobDifficulty[i])
                if st:
                    dp2[i] = min(dp2[i], dp2[st[-1]])
                st.append(i)
            dp, dp2 = dp2, dp
        return dp[-1]


tests = [
    [[6,5,4,3,2,1], 2, 7],
    [[9,9,9], 4, -1],
    [[1,1,1], 3, 3]
]

run_functional_tests(Solution().minDifficulty, tests)
