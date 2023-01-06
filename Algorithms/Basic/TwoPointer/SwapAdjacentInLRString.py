"""
https://leetcode.com/problems/swap-adjacent-in-lr-string/

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.



Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false


Constraints:

1 <= start.length <= 104
start.length == end.length
Both start and end will only consist of characters in 'L', 'R', and 'X'.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# NOT FINISHED
# class Solution:
#     def canTransform(self, start: str, end: str) -> bool:
#         balance = defaultdict(int)
#         n = len(start)
#         i = 0
#         while i < n:
#             i0 = i
#             balance[start[i]] += 1
#             balance[end[i]] -= 1
#             i += 1
#             while i < n and (balance['R'] != 0 and balance['L'] != 0 and balance['X'] != 0):
#                 balance[start[i]] += 1
#                 balance[end[i]] -= 1
#                 i += 1
#             if balance['R'] != 0 or balance['L'] != 0 or balance['X'] != 0:
#                 return False
#             if start[i0:i] == end[i0:i]:
#                 continue
#         return False


# Runtime
# 88 ms
# Beats
# 56.32%
# Memory
# 14.1 MB
# Beats
# 54.98%
# https://leetcode.com/problems/swap-adjacent-in-lr-string/solutions/2826070/c-easy-fast/
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        i, j = 0, 0
        while i < n and j < n:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i == n and j == n:
                return True
            if i == n or j == n:
                return False
            if start[i] != end[j]:
                return False
            if start[i] == 'R' and i > j:
                return False
            if start[i] == 'L' and i < j:
                return False
            i += 1
            j += 1
        while i < n and start[i] == 'X':
            i += 1
        while j < n and end[j] == 'X':
            j += 1
        return i == j


tests = [
    ["RXXLRXRXL", "XRLXXRRLX", True],
    ["X", "L", False]
]

run_functional_tests(Solution().canTransform, tests)
