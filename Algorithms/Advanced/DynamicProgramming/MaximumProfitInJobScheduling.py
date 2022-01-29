"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3950/
https://leetcode.com/problems/maximum-profit-in-job-scheduling/

We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.



Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6


Constraints:

1 <= startTime.length == endTime.length == profit.length <= 5 * 104
1 <= startTime[i] < endTime[i] <= 109
1 <= profit[i] <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1212 ms, faster than 7.04% of Python3 online submissions for Maximum Profit in Job Scheduling.
# Memory Usage: 126.9 MB, less than 5.01% of Python3 online submissions for Maximum Profit in Job Scheduling.
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1411876/Java-DP-%2B-binary-search
# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         jobs = sorted(zip(startTime, endTime, profit))
#         n = len(jobs)
#
#         @lru_cache(None)
#         def dp(k: int) -> int:
#             if k == n:
#                 return 0
#
#             def bin_search(et: int) -> int:
#                 if et > jobs[-1][0]:
#                     return n
#                 l, r = 0, n
#                 while l < r:
#                     mid = l + (r-l) // 2
#                     if jobs[mid][0] < et:
#                         l = mid +1
#                     else:
#                         r = mid
#                 return r
#
#             sti = bin_search(jobs[k][1])
#             return max(dp(k+1), jobs[k][2] + dp(sti))
#
#         return dp(0)


# Runtime: 773 ms, faster than 31.11% of Python3 online submissions for Maximum Profit in Job Scheduling.
# Memory Usage: 39.9 MB, less than 24.38% of Python3 online submissions for Maximum Profit in Job Scheduling.
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1430324/c%2B%2B-solution-without-binary-search
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        times = sorted(startTime + endTime)
        idx = {t: i for i, t in enumerate(times)}
        jobs = sorted(zip(startTime, endTime, profit))
        j, m = 1, len(times)
        dp = [0] * (m+1)
        for i in range(n):
            st, end, val = jobs[i]
            st, end = idx[st], idx[end]
            while j <= st:
                dp[j] = max(dp[j-1], dp[j])
                j += 1
            dp[end] = max(dp[end], dp[st] + val)
        while j <= m:
            dp[j] = max(dp[j-1], dp[j])
            j += 1
        return dp[m]


tests = [
    [[1,2,3,3], [3,4,5,6], [50,10,40,70], 120],
    [[1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60], 150],
    [[1,1,1], [2,3,4], [5,6,4], 6]
]

run_functional_tests(Solution().jobScheduling, tests)