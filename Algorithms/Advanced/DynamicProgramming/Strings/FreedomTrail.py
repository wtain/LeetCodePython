"""
https://leetcode.com/problems/freedom-trail/description/?envType=daily-question&envId=2024-04-27

In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring" and use the dial to spell a specific keyword to open the door.

Given a string ring that represents the code engraved on the outer ring and another string key that represents the keyword that needs to be spelled, return the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You should spell all the characters in key one by one by rotating ring clockwise or anticlockwise to make each character of the string key aligned at the "12:00" direction and then by pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:

You can rotate the ring clockwise or anticlockwise by one place, which counts as one step. The final purpose of the rotation is to align one of ring's characters at the "12:00" direction, where this character must equal key[i].
If the character key[i] has been aligned at the "12:00" direction, press the center button to spell, which also counts as one step. After the pressing, you could begin to spell the next character in the key (next stage). Otherwise, you have finished all the spelling.


Example 1:


Input: ring = "godding", key = "gd"
Output: 4
Explanation:
For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
Also, we need 1 more step for spelling.
So the final output is 4.
Example 2:

Input: ring = "godding", key = "godding"
Output: 13


Constraints:

1 <= ring.length, key.length <= 100
ring and key consist of only lower case English letters.
It is guaranteed that key could always be spelled by rotating ring.
"""
import heapq
from cmath import inf
from collections import defaultdict
from functools import cache

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# # https://leetcode.com/problems/freedom-trail/editorial/?envType=daily-question&envId=2024-04-27
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         ring_len, key_len = len(ring), len(key)
#
#         def count_steps(curr, next):
#             steps_between = abs(curr - next)
#             steps_around = ring_len - steps_between
#             return min(steps_between, steps_around)
#
#         def try_lock(ring_index, key_index, min_steps):
#             if key_index == len(key):
#                 return 0
#             for i in range(ring_len):
#                 if ring[i] == key[key_index]:
#                     total_steps = count_steps(ring_index, i) + 1 + try_lock(i, key_index+1, inf)
#                     min_steps = min(min_steps, total_steps)
#             return min_steps
#         return try_lock(0, 0, inf)


# Runtime
# 214
# ms
# Beats
# 40.78%
# of users with Python3
# Memory
# 17.70
# MB
# Beats
# 17.65%
# of users with Python3
# https://leetcode.com/problems/freedom-trail/editorial/?envType=daily-question&envId=2024-04-27
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         ring_len, key_len = len(ring), len(key)
#
#         def count_steps(curr, next):
#             steps_between = abs(curr - next)
#             steps_around = ring_len - steps_between
#             return min(steps_between, steps_around)
#
#         @cache
#         def try_lock(ring_index, key_index):
#             if key_index == key_len:
#                 return 0
#             min_steps = inf
#             for char_index in range(ring_len):
#                 if ring[char_index] == key[key_index]:
#                     min_steps = min(min_steps, count_steps(ring_index, char_index) + 1 + try_lock(char_index, key_index+1))
#             return min_steps
#         return try_lock(0, 0)


# Runtime
# 2657
# ms
# Beats
# 5.49%
# of users with Python3
# Memory
# 16.80
# MB
# Beats
# 65.49%
# of users with Python3
# https://leetcode.com/problems/freedom-trail/editorial/?envType=daily-question&envId=2024-04-27
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         ring_len, key_len = len(ring), len(key)
#         best_steps = [[inf] * (key_len + 1) for _ in range(ring_len)]
#
#         def count_steps(curr, next):
#             steps_between = abs(curr - next)
#             steps_around = ring_len - steps_between
#             return min(steps_between, steps_around)
#
#         for row in best_steps:
#             row[key_len] = 0
#
#         for key_index in range(key_len - 1, -1, -1):
#             for ring_index in range(ring_len):
#                 for char_index in range(ring_len):
#                     if ring[char_index] == key[key_index]:
#                         best_steps[ring_index][key_index] = min(best_steps[ring_index][key_index], 1 + count_steps(ring_index, char_index) + best_steps[char_index][key_index+1])
#
#         return best_steps[0][0]


# Runtime
# 2564
# ms
# Beats
# 6.27%
# of users with Python3
# Memory
# 16.52
# MB
# Beats
# 90.20%
# of users with Python3
# https://leetcode.com/problems/freedom-trail/editorial/?envType=daily-question&envId=2024-04-27
# class Solution:
#     def findRotateSteps(self, ring: str, key: str) -> int:
#         ring_len, key_len = len(ring), len(key)
#         prev = [0 for _ in range(ring_len)]
#
#         def count_steps(curr, next):
#             steps_between = abs(curr - next)
#             steps_around = ring_len - steps_between
#             return min(steps_between, steps_around)
#
#         for key_index in range(key_len - 1, -1, -1):
#             curr = [inf for _ in range(ring_len)]
#             for ring_index in range(ring_len):
#                 for char_index in range(ring_len):
#                     if ring[char_index] == key[key_index]:
#                         curr[ring_index] = min(curr[ring_index], 1 + count_steps(ring_index, char_index) + prev[char_index])
#             prev = curr.copy()
#
#         return prev[0]


# Runtime
# 118
# ms
# Beats
# 60.00%
# of users with Python3
# Memory
# 16.83
# MB
# Beats
# 59.22%
# of users with Python3
# # https://leetcode.com/problems/freedom-trail/editorial/?envType=daily-question&envId=2024-04-27
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len, key_len = len(ring), len(key)

        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = ring_len - steps_between
            return min(steps_between, steps_around)

        char_idx = defaultdict(list)
        for i, char in enumerate(ring):
            char_idx[char].append(i)

        heap = [(0, 0, 0)]
        seen = set()

        while heap:
            total_steps, ring_index, key_index = heapq.heappop(heap)

            if key_index == key_len:
                break

            if (ring_index, key_index) in seen:
                continue

            seen.add((ring_index, key_index))

            for next_index in char_idx[key[key_index]]:
                heapq.heappush(heap, (total_steps + count_steps(ring_index, next_index), next_index, key_index + 1))

        return total_steps + key_len


tests = [
    ["godding", "gd", 4],
    ["godding", "godding", 13],
]

run_functional_tests(Solution().findRotateSteps, tests)
