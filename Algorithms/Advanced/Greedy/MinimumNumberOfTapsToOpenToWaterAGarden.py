"""
https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/description/

There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. (i.e The length of the garden is n).

There are n + 1 taps located at points [0, 1, ..., n] in the garden.

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water the area [i - ranges[i], i + ranges[i]] if it was open.

Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered return -1.



Example 1:


Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
Example 2:

Input: n = 3, ranges = [0,0,0,0]
Output: -1
Explanation: Even if you activate all the four taps you cannot water the whole garden.


Constraints:

1 <= n <= 104
ranges.length == n + 1
0 <= ranges[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 442ms
# Beats 33.81%of users with Python3
# Memory
# Details
# 16.66MB
# Beats 73.81%of users with Python3
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/editorial/
# class Solution:
#     def minTaps(self, n: int, ranges: List[int]) -> int:
#         BIGVALUE = 10 ** 9
#         dp = [BIGVALUE] * (n+1)
#         dp[0] = 0
#         for i in range(n+1):
#             start = max(0, i - ranges[i])
#             end = min(n, i + ranges[i])
#             for j in range(start, end+1):
#                 dp[end] = min(dp[end], dp[j]+1)
#         return dp[n] if dp[n] != BIGVALUE else -1



# Runtime
# Details
# 117ms
# Beats 95.71%of users with Python3
# Memory
# Details
# 16.81MB
# Beats 46.90%of users with Python3
# https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/editorial/
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_reach = [0] * (n+1)
        for i in range(n+1):
            start = max(0, i - ranges[i])
            end = min(n, i + ranges[i])
            max_reach[start] = max(max_reach[start], end)
        taps = 0
        curr_end, next_end = 0, 0
        for i in range(n+1):
            if i > next_end:
                return -1
            if i > curr_end:
                taps += 1
                curr_end = next_end
            next_end = max(next_end, max_reach[i])
        return taps


tests = [
    [5, [3,4,1,1,0,0], 1],
    [3, [0,0,0,0], -1],
]

run_functional_tests(Solution().minTaps, tests)
