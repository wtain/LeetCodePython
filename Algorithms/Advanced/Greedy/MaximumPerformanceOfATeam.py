"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/603/week-1-june-1st-june-7th/3768/
https://leetcode.com/problems/maximum-performance-of-a-team/

You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.

Choose at most k different engineers out of the n engineers to form a team with the maximum performance.

The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.

Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.



Example 1:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.
Example 2:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.
Example 3:

Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72


Constraints:

1 <= <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
#         engineers = sorted([-s*e, s, e] for s, e in zip(speed, efficiency))
#         MOD = 10**9 + 7
#         sum_speed = engineers[0][1]
#         min_ef = engineers[0][2]
#         engineers = engineers[1:]
#         for i in range(1, k):
#             engineers1 = sorted([-s, s, e] for p, s, e in engineers if e >= min_ef)
#             engineers2 = sorted([-s, s, e] for p, s, e in engineers if e < min_ef and s * e > sum_speed * (min_ef - e))
#             engineers3 = sorted([-s, s, e] for p, s, e in engineers if e < min_ef and s * e <= sum_speed * (min_ef - e))
#             s1, e1, s2, e2 = 0, 0, 0, 0
#             if engineers1:
#                 s1, e1 = engineers1[0][1:]
#             if engineers2:
#                 s2, e2 = engineers2[0][1:]
#             if min_ef*(sum_speed+s1) > e2*(sum_speed+s2):
#                 sum_speed += s1
#                 engineers = engineers1[1:] + engineers2[:] + engineers3
#             else:
#                 sum_speed += s2
#                 min_ef = e2
#                 engineers = engineers1[:] + engineers2[1:] + engineers3
#             # print(sum_speed, min_ef)
#
#         return sum_speed * min_ef % MOD


# Runtime: 572 ms, faster than 5.85% of Python3 online submissions for Maximum Performance of a Team.
# Memory Usage: 29.9 MB, less than 86.77% of Python3 online submissions for Maximum Performance of a Team.
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        MOD = 10**9 + 7
        candidates = sorted(zip(efficiency, speed), reverse=True)

        speed_h = []
        speed_sum, perf = 0, 0
        for ce, cs in candidates:
            if len(speed_h) > k-1:
                speed_sum -= heapq.heappop(speed_h)
            heapq.heappush(speed_h, cs)
            speed_sum += cs
            perf = max(perf, speed_sum * ce)

        return perf % MOD


tests = [
    [6, [10,5,1,7,4,2], [2,1,1,1,7,3], 6, 32],

    [4, [2,5,5,5], [3,3,3,5], 4, 51],

    [6, [2,10,3,1,5,8], [5,4,3,9,7,2], 2, 60],
    [6, [2,10,3,1,5,8], [5,4,3,9,7,2], 3, 68],
    [6, [2,10,3,1,5,8], [5,4,3,9,7,2], 4, 72]
]

run_functional_tests(Solution().maxPerformance, tests)