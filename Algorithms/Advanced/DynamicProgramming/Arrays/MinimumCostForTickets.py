"""
https://leetcode.com/problems/minimum-cost-for-tickets/submissions/386078604/

You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.



Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.


Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG?
# class Solution:
#     def mincostTickets(self, days: List[int], costs: List[int]) -> int:
#         n, m = len(days), len(costs)
#         travels = [False] * 366
#         for i in range(n):
#             travels[days[i]] = True
#         dp = [0] * 366
#         for i in range(1, 366):
#             v = dp[i-1] + costs[0]
#             if not travels[i]:
#                 v = min(dp[i-1], v)
#             if i - 7 + 1 >= 1:
#                 v = min(v, dp[i-7] + costs[1])
#             if i - 30 + 1 >= 1:
#                 v = min(v, dp[i-30] + costs[2])
#             dp[i] = v
#         return dp[365]

# Runtime
# 38 ms
# Beats
# 93.28%
# Memory
# 13.9 MB
# Beats
# 58.35%
# https://leetcode.com/problems/minimum-cost-for-tickets/solutions/3349623/python-java-c-simple-solution-easy-to-understand/
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        travel_days = set(days)
        for i in range(1, 366):
            if i not in travel_days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
        return dp[-1]


tests = [
    [[1,4,6,7,8,20], [2,7,15], 11],
    [[1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15], 17],
    [[1,5,8,10,13,20,29,31,37,48,52,53,54,61,63,64,65,67,72,73,74,79,81,84,85,86,87,88,91,94,98,100,108,112,115,116,120,121,123,131,132,135,137,139,141,145,147,152,163,165,166,173,174,178,179,182,187,198,202,203,204,206,208,210,212,213,216,224,230,234,237,239,240,242,247,249,250,257,259,261,263,265,266,272,273,274,275,279,280,281,284,288,292,293,297,298,300,301,304,306,309,318,323,326,328,330,332,335,336,339,341,342,345,350,351,362,365], [15,8,3], 39],
]

run_functional_tests(Solution().mincostTickets, tests)
