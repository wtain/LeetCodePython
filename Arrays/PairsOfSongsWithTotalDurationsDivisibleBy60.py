"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/570/week-2-december-8th-december-14th/3559/
1010. Pairs of Songs With Total Durations Divisible by 60
Medium

892

67

Add to List

Share
You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60. Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.



Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


Constraints:

1 <= time.length <= 6 * 104
1 <= time[i] <= 500

Runtime: 200 ms, faster than 98.92% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
Memory Usage: 18.1 MB, less than 10.00% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.

"""
from bisect import bisect_left
from typing import List


# class Solution:
#     def numPairsDivisibleBy60(self, time: List[int]) -> int:
#         n = len(time)
#         for i in range(0, n):
#             time[i] %= 60
#         time.sort()
#         cnt = 0
#         for i in range(0, n-1):
#             j = i + 1
#             while j < n:
#                 target = (60 - time[i]) % 60
#                 j = bisect_left(time, target, j)
#                 if j < n and (time[j] + time[i]) % 60 == 0:
#                     cnt += 1
#
#                 j += 1
#         return cnt

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        n = len(time)
        counts = [0] * 60
        for i in range(0, n):
            counts[time[i] % 60] += 1
        cnt = 0
        for i in range(1, 30):
            cnt += counts[i] * counts[(60 - i) % 60]
        cnt += int((counts[0] * (counts[0] - 1) / 2))
        cnt += int((counts[30] * (counts[30] - 1) / 2))
        return cnt

# 20 30 30 40 40
# 20 30 40
# 1   2  2
print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))  # 3
print(Solution().numPairsDivisibleBy60([60,60,60]))  # 3



