"""
https://leetcode.com/problems/minimum-time-to-complete-trips/description/

You are given an array time where time[i] denotes the time taken by the ith bus to complete one trip.

Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip. Also, each bus operates independently; that is, the trips of one bus do not influence the trips of any other bus.

You are also given an integer totalTrips, which denotes the number of trips all buses should make in total. Return the minimum time required for all buses to complete at least totalTrips trips.



Example 1:

Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0].
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0].
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1].
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.
Example 2:

Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.


Constraints:

1 <= time.length <= 105
1 <= time[i], totalTrips <= 107
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def minimumTime(self, time: List[int], totalTrips: int) -> int:
#         mx = float('inf') // len(time)
#         mn = 1
#         result = 0
#         while mn <= mx:
#             mid = (mx - mn) // 2 + mn
#             k = 0
#             for i in time:
#                 k += mid // i
#             if k >= totalTrips:
#                 result = mid
#                 mx = mid - 1
#             else:
#                 mn = mid + 1
#         return result

# Runtime
# 4851 ms
# Beats
# 9.75%
# Memory
# 28.5 MB
# Beats
# 70.25%
# https://leetcode.com/problems/minimum-time-to-complete-trips/solutions/3091195/binary-search-c/
class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:

        def good(x):
            cnt = 0
            for i in time:
                cnt += x // i
                if cnt >= 10 ** 18:
                    return True
            return cnt >= totalTrips

        s, e = 1, 10**18
        result = 0
        while s <= e:
            m = (s+e) // 2
            if good(m):
                e = m - 1
                result = m
            else:
                s = m + 1
        return result


tests = [
    [[1,2,3], 5, 3],
    [[2], 1, 2],
]

run_functional_tests(Solution().minimumTime, tests)
