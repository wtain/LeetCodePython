"""
https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.



Example 1:

Input: amount = [1,4,2]
Output: 4
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup and a warm cup.
Second 2: Fill up a warm cup and a hot cup.
Second 3: Fill up a warm cup and a hot cup.
Second 4: Fill up a warm cup.
It can be proven that 4 is the minimum number of seconds needed.
Example 2:

Input: amount = [5,4,4]
Output: 7
Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.
Example 3:

Input: amount = [5,0,0]
Output: 5
Explanation: Every second, we fill up a cold cup.


Constraints:

amount.length == 3
0 <= amount[i] <= 100
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 78 ms
# Beats
# 14.77%
# Memory
# 13.8 MB
# Beats
# 62.81%
# class Solution:
#     def fillCups(self, amount: List[int]) -> int:
#         h = list(-h for h in amount)
#         heapq.heapify(h)
#         result = 0
#         while h[0] != 0:
#             h1 = -heapq.heappop(h)
#             h2 = -heapq.heappop(h)
#             h1 -= 1
#             if h2:
#                 h2 -= 1
#             result += 1
#             heapq.heappush(h, -h1)
#             heapq.heappush(h, -h2)
#         return result


# Runtime
# 87 ms
# Beats
# 7.30%
# Memory
# 13.9 MB
# Beats
# 15.30%
# class Solution:
#     def fillCups(self, amount: List[int]) -> int:
#         h = list(-h for h in amount)
#         heapq.heapify(h)
#         result = 0
#         while h[0] != 0:
#             h1 = -heapq.heappop(h)
#             h2 = -heapq.heappop(h)
#             h3 = -heapq.heappop(h)
#             diff = h2 - h3
#             if diff == 0:
#                 diff = 1
#             h1 -= diff
#             if h2:
#                 h2 -= diff
#             result += diff
#             heapq.heappush(h, -h1)
#             heapq.heappush(h, -h2)
#             heapq.heappush(h, -h3)
#         return result


# Runtime
# 60 ms
# Beats
# 60.50%
# Memory
# 13.9 MB
# Beats
# 15.30%
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        result = 0
        while amount[-1] > 0:
            h3, h2, h1 = amount
            diff = h2 - h3
            if diff == 0:
                diff = 1
            h1 -= diff
            if h2:
                h2 -= diff
            result += diff
            amount = sorted([h1, h2, h3])
        return result


tests = [
    [[1,4,2], 4],
    [[5,4,4], 7],
    [[5,0,0], 5]
]

run_functional_tests(Solution().fillCups, tests)
