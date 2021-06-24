"""
https://leetcode.com/problems/bulb-switcher/

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.



Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb is on.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 1


Constraints:

0 <= n <= 109
"""
from math import sqrt

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def bulbSwitch(self, n: int) -> int:
#         cnt = 0
#         for i in range(1, n+1):
#             if i == int(sqrt(i)) ** 2:
#                 cnt += 1
#         return cnt
# 1) PASS, took: 45.755 on size=99999999
# 2) PASS, took: 0.000 on size=3
# 3) PASS, took: 0.000 on size=0
# 4) PASS, took: 0.000 on size=1
# OVERALL: SUCCESS


# Runtime: 32 ms, faster than 54.43% of Python3 online submissions for Bulb Switcher.
# Memory Usage: 14.2 MB, less than 63.03% of Python3 online submissions for Bulb Switcher.
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))


tests = [
    [99999999, 9999],
    [3, 1],
    [0, 0],
    [1, 1]
]

run_functional_tests(Solution().bulbSwitch, tests)