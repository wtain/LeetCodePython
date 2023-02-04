"""
https://leetcode.com/problems/minimum-jumps-to-reach-home/

A certain bug's home is on the x-axis at position x. Help them get there from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.
The bug may jump forward beyond its home, but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the bug cannot jump to the position forbidden[i], and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home. If there is no possible sequence of jumps that lands the bug on position x, return -1.



Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.


Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.
"""
import sys
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# RecursionError: maximum recursion depth exceeded in comparison
# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#
#         is_forbidden = set(forbidden)
#
#         sys.setrecursionlimit(10010)
#
#         @cache
#         def impl(start: int, negative_jumps: int) -> int:
#             if start == x:
#                 return 0
#             if start < 0:
#                 return -1
#             if start-(2-negative_jumps)*b > x or start in is_forbidden:
#                 return -1
#             forward = impl(start+a, 0)
#             if negative_jumps < 2:
#                 backward = impl(start - b, negative_jumps+1)
#                 if backward == -1:
#                     return forward+1 if forward != -1 else -1
#                 if forward == -1:
#                     return backward+1 if backward != -1 else -1
#                 return min(backward, forward)+1
#             return forward+1 if forward != -1 else -1
#
#         return impl(0, 0)


# WRONG
# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         BigValue = float('Inf')
#         M = x+max(a, 2*b)
#         dp = [[BigValue] * 3 for _ in range((M+1))]
#         dp[0][0] = 0
#         for f in forbidden:
#             dp[f][0] = dp[f][1] = dp[f][2] = -1
#
#         level = [(0, 0)]
#         while level:
#             next_level = []
#             for current, negative_jumps in level:
#                 if current+a <= M and \
#                         dp[current][negative_jumps] + 1 < dp[current+a][0]:
#                     dp[current+a][0] = dp[current][negative_jumps] + 1
#                     next_level.append((current+a, 0))
#                 if negative_jumps+1 <= 2 and current - b >= 0 and \
#                         dp[current][negative_jumps] + 1 < dp[current - b][negative_jumps+1]:
#                     dp[current - b][negative_jumps+1] = dp[current][negative_jumps] + 1
#                     next_level.append((current - b, negative_jumps+1))
#             level = next_level
#
#         result = min(dp[x][i] for i in range(3))
#         return result if result != BigValue else -1


# Runtime
# 7454 ms
# Beats
# 5.1%
# Memory
# 302.1 MB
# Beats
# 5.1%
# class Solution:
#     def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
#         BigValue = float('Inf')
#         M = x+a * (abs(a-b)+1)
#         result = BigValue
#
#         is_forbidden = set(forbidden)
#
#         level = [(0, 0)]
#         jumps = 0
#         visited = set()
#         visited.add((0, 0))
#         while level:
#             next_level = []
#             for current, negative_jumps in level:
#                 if current == x:
#                     return jumps
#                 if current+a <= M \
#                         and (current+a, 0) not in visited\
#                         and (current+a) not in is_forbidden:
#                     visited.add((current+a, 0))
#                     next_level.append((current+a, 0))
#                 if negative_jumps+1 <= 1 \
#                         and current - b > 0 \
#                         and (current - b, negative_jumps+1) not in visited\
#                         and (current - b) not in is_forbidden:
#                     visited.add((current - b, negative_jumps+1))
#                     next_level.append((current - b, negative_jumps+1))
#             jumps += 1
#             level = next_level
#
#         return result if result != BigValue else -1

# Runtime
# 154 ms
# Beats
# 44.23%
# Memory
# 15.9 MB
# Beats
# 23.31%
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        BigValue = float('Inf')
        M = 6001
        result = BigValue

        is_forbidden = set(forbidden)

        level = [(0, 0)]
        jumps = 0
        visited = set()
        visited.add((0, 0))
        while level:
            next_level = []
            for current, negative_jumps in level:
                if current == x:
                    return jumps
                if current+a <= M \
                        and (current+a, 0) not in visited\
                        and (current+a) not in is_forbidden:
                    visited.add((current+a, 0))
                    next_level.append((current+a, 0))
                if negative_jumps+1 <= 1 \
                        and current - b > 0 \
                        and (current - b, negative_jumps+1) not in visited\
                        and (current - b) not in is_forbidden:
                    visited.add((current - b, negative_jumps+1))
                    next_level.append((current - b, negative_jumps+1))
            jumps += 1
            level = next_level

        return result if result != BigValue else -1


tests = [
    [[1362, 873, 1879, 725, 305, 794, 1135, 1358, 1717, 159, 1370, 1861, 583, 1193, 1921, 778, 1263, 239, 1224, 1925, 1505, 566, 5, 15], 560, 573, 64, 1036],
    [[162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98], 29, 98, 80, 121],
    [[128,178,147,165,63,11,150,20,158,144,136], 61, 170, 135, 6],
    [[14,4,18,1,15], 3, 15, 9, 3],
    [[8,3,16,6,12,20], 15, 13, 11, -1],
    [[1,6,2,14,5,17,4], 16, 9, 7, 2],
]

run_functional_tests(Solution().minimumJumps, tests)
# run_functional_tests(Solution().minimumJumps, tests, run_tests=3)
# run_functional_tests(Solution().minimumJumps, tests, run_tests=2)
# run_functional_tests(Solution().minimumJumps, tests, run_tests=4)
