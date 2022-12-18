"""
https://leetcode.com/problems/bulb-switcher-ii/

There is a room with n bulbs labeled from 1 to n that all are turned on initially, and four buttons on the wall. Each of the four buttons has a different functionality where:

Button 1: Flips the status of all the bulbs.
Button 2: Flips the status of all the bulbs with even labels (i.e., 2, 4, ...).
Button 3: Flips the status of all the bulbs with odd labels (i.e., 1, 3, ...).
Button 4: Flips the status of all the bulbs with a label j = 3k + 1 where k = 0, 1, 2, ... (i.e., 1, 4, 7, 10, ...).
You must make exactly presses button presses in total. For each press, you may pick any of the four buttons to press.

Given the two integers n and presses, return the number of different possible statuses after performing all presses button presses.



Example 1:

Input: n = 1, presses = 1
Output: 2
Explanation: Status can be:
- [off] by pressing button 1
- [on] by pressing button 2
Example 2:

Input: n = 2, presses = 1
Output: 3
Explanation: Status can be:
- [off, off] by pressing button 1
- [on, off] by pressing button 2
- [off, on] by pressing button 3
Example 3:

Input: n = 3, presses = 1
Output: 4
Explanation: Status can be:
- [off, off, off] by pressing button 1
- [off, on, off] by pressing button 2
- [on, off, on] by pressing button 3
- [off, on, on] by pressing button 4


Constraints:

1 <= n <= 1000
0 <= presses <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#
#         state = 0
#         for i in range(n):
#             state = (state << 1) + 1
#
#         all_ones = state
#
#         def flip(state, divisor=None, remainder=None):
#             new_state = 0
#             mask = 1
#             for i in range(n):
#                 new_state <<= 1
#                 bit = 1 if state & mask else 0
#                 if not divisor or (i+1) % divisor == remainder:
#                     new_state = new_state + (1-bit)
#                 else:
#                     new_state = new_state + bit
#                 mask <<= 1
#
#             return new_state
#
#         result = set()
#         to_visit = {(state, 0)}
#         visited = set()
#         while to_visit:
#             state, switches = to_visit.pop()
#             visited.add((state, switches))
#             if switches == presses:
#                 result.add(state)
#             else:
#                 state1 = flip(state)
#                 state2 = flip(state, 2, 0)
#                 state3 = flip(state, 2, 1)
#                 state4 = flip(state, 3, 1)
#                 if (state1, switches + 1) not in visited:
#                     to_visit.add((state1, switches+1))
#                 if (state2, switches + 1) not in visited:
#                     to_visit.add((state2, switches+1))
#                 if (state3, switches + 1) not in visited:
#                     to_visit.add((state3, switches+1))
#                 if (state4, switches + 1) not in visited:
#                     to_visit.add((state4, switches+1))
#
#         print(result)
#         return len(result)

# TLE
# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#
#         state = 0
#         for i in range(n):
#             state = (state << 1) + 1
#
#         all_ones = state
#
#         def flip(state, divisor=None, remainder=None):
#             mask = 1
#             new_state = state
#             for i in range(n):
#                 negative_mask = all_ones - mask
#                 bit = state & mask
#                 if not divisor or (i + 1) % divisor == remainder:
#                     new_state = (negative_mask & new_state) + mask - bit
#                 mask <<= 1
#
#             return new_state
#
#         # print(all_ones)
#         # print(flip(all_ones))
#         # print(flip(all_ones, 2, 0))
#         # print(flip(all_ones, 2, 1))
#         # print(flip(all_ones, 3, 1))
#         # print(flip(6))
#         # print(flip(6, 2, 0))
#         # print(flip(6, 2, 1))
#         # print(flip(6, 3, 1))
#
#         result = set()
#         to_visit = {(state, 0)}
#         visited = set()
#         while to_visit:
#             state, switches = to_visit.pop()
#             visited.add((state, switches))
#             if switches == presses:
#                 result.add(state)
#             else:
#                 states = [flip(state),
#                           flip(state, 2, 0),
#                           flip(state, 2, 1),
#                           flip(state, 3, 1)]
#                 for next_state in states:
#                     state_record = (next_state, switches+1)
#                     if state_record not in visited:
#                         to_visit.add(state_record)
#
#         # print(result)
#         return len(result)


# class Solution:
#     def flipLights(self, n: int, presses: int) -> int:
#
#         state = 0
#         for i in range(n):
#             state = (state << 1) + 1
#
#         all_ones = state
#
#         def flip(state, divisor=None, remainder=None):
#             mask = 1
#             new_state = state
#             for i in range(n):
#                 negative_mask = all_ones - mask
#                 bit = state & mask
#                 if not divisor or (i + 1) % divisor == remainder:
#                     new_state = (negative_mask & new_state) + mask - bit
#                 mask <<= 1
#
#             return new_state
#
#         level = {state}
#         for i in range(presses):
#             next_level = set()
#             for state in level:
#                 states = [flip(state),
#                           flip(state, 2, 0),
#                           flip(state, 2, 1),
#                           flip(state, 3, 1)]
#                 for next_state in states:
#                     next_level.add(next_state)
#             level = next_level
#
#         return len(level)


# Runtime
# 117 ms
# Beats
# 33.33%
# Memory
# 14 MB
# Beats
# 42.98%
class Solution:
    def flipLights(self, n: int, presses: int) -> int:

        all_ones, evens, odds, three = 0, 0, 0, 0
        for i in range(n):
            all_ones = (all_ones << 1) + 1
            evens = (evens << 1) + (1 if (i+1) % 2 == 0 else 0)
            odds = (odds << 1) + (1 if (i+1) % 2 == 1 else 0)
            three = (three << 1) + (1 if (i+1) % 3 == 1 else 0)

        state = all_ones

        level = {state}
        for i in range(presses):
            next_level = set()
            for state in level:
                states = [state ^ all_ones,
                          state ^ evens,
                          state ^ odds,
                          state ^ three]
                for next_state in states:
                    next_level.add(next_state)
            level = next_level

        return len(level)


tests = [
    [1, 1, 2],
    [2, 1, 3],
    [3, 1, 4],
    [3, 2, 7],
    [10, 10, 8],
    [1000, 1000, 8]
]

"""
3, 2

111
000             101             010             110
111 101 010 001 010 111 000 100 101 111 000 011 001 011 100 111
"""

# run_functional_tests(Solution().flipLights, tests, run_tests=[4])
# run_functional_tests(Solution().flipLights, tests, run_tests=[5])
run_functional_tests(Solution().flipLights, tests)
