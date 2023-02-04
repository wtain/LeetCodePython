"""
https://leetcode.com/problems/maximum-earnings-from-taxi/

There are n points on a road you are driving your taxi on. The n points on the road are labeled from 1 to n in the direction you are going, and you want to drive from point 1 to point n to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a 0-indexed 2D integer array rides, where rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point starti to point endi who is willing to give a tipi dollar tip.

For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only drive at most one passenger at a time.

Given n and rides, return the maximum number of dollars you can earn by picking up the passengers optimally.

Note: You may drop off a passenger and pick up a different passenger at the same point.



Example 1:

Input: n = 5, rides = [[2,5,4],[1,5,1]]
Output: 7
Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
Example 2:

Input: n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
Output: 20
Explanation: We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.


Constraints:

1 <= n <= 105
1 <= rides.length <= 3 * 104
rides[i].length == 3
1 <= starti < endi <= n
1 <= tipi <= 105
"""
import heapq
from collections import defaultdict, deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
#
#         def rides_conflict(ride1: List[int], ride2: List[int]) -> bool:
#
#             def includes(ride1: List[int], ride2: List[int]) -> bool:
#                 s1, e1, _ = ride1
#                 s2, e2, _ = ride2
#                 return s2 <= s1 < e2 or s2 <= e1 < e2
#
#             return includes(ride1, ride2) or includes(ride2, ride1)
#
#         def cost(ride: List[int]) -> int:
#             s, e, t = ride
#             return e - s + t
#
#         rides.sort()
#         m = len(rides)
#         dp = [[0, 0] for _ in range(m)]
#         dp[0] = [cost(rides[0]), rides[0][1]]
#         result = 0
#         for i in range(1, m):
#             best_cost, best_end = dp[i-1]
#             for j in range(i):
#                 if rides_conflict(rides[i], rides[j]):
#                     continue
#                 cost_j, end_j = dp[j]
#                 c = cost(rides[i]) + cost_j
#                 if c > best_cost:
#                     best_cost = c
#                     best_end = rides[i][1]
#
#             dp[i] = [best_cost, best_end]
#             result = max(result, dp[i][0])
#
#         return result


# Runtime
# 2253 ms
# Beats
# 38.3%
# Memory
# 45 MB
# Beats
# 27.87%
# https://leetcode.com/problems/maximum-earnings-from-taxi/solutions/1470935/c-python-dp-o-m-n-clean-concise/
# class Solution:
#     def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
#         ride_start_at = defaultdict(list)
#         for s, e, t in rides:
#             ride_start_at[s].append([e, e - s + t])
#
#         dp = [0] * (n+1)
#         for i in range(n-1, 0, -1):
#             for e, d in ride_start_at[i]:
#                 dp[i] = max(dp[i], dp[e] + d)
#             dp[i] = max(dp[i], dp[i+1])
#         return dp[1]


# Runtime
# 1796 ms
# Beats
# 82.62%
# Memory
# 33.6 MB
# Beats
# 66.23%
# https://leetcode.com/problems/maximum-earnings-from-taxi/solutions/2851910/java-priorityqueue-o-nlogn-time-o-n-space-easy-solution-same-as-max-profit-in-job-schedule/
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rides.sort()
        mx = 0
        queue = []
        for s, e, t in rides:
            profit = e - s + t

            while queue and s >= queue[0][0]:
                ride = heapq.heappop(queue)
                mx = max(mx, ride[1])

            heapq.heappush(queue, [e, profit + mx])

        while queue:
            ride = heapq.heappop(queue)
            mx = max(mx, ride[1])

        return mx


tests = [
    [10, [[2,3,6],[8,9,8],[5,9,7],[8,9,1],[2,9,2],[9,10,6],[7,10,10],[6,7,9],[4,9,7],[2,3,1]], 33],
    [5, [[2,5,4],[1,5,1]], 7],
    [20, [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]], 20],
]

run_functional_tests(Solution().maxTaxiEarnings, tests)
