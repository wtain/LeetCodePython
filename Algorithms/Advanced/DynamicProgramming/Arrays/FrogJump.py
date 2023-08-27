"""
https://leetcode.com/problems/frog-jump/description/

A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.



Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.


Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         n = len(stones)
#         dp = [False] * n
#         dp[0] = True
#         return False


# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         n = len(stones)
#         level = [(0, 0)]
#         while level:
#             next_level = []
#             for stone, jump in level:
#                 for step in [jump-1, jump+1]:
#                     if step <= 0:
#                         continue
#                     next_stone = stone + step
#                     if next_stone >= n:
#                         continue
#                     if next_stone == n-1:
#                         return True
#                     next_level.append((next_stone, step))
#             level = next_level
#         return False

# Runtime
# Details
# 119ms
# Beats 91.77%of users with Python3
# Memory
# Details
# 24.06MB
# Beats 58.33%of users with Python3
# https://leetcode.com/problems/frog-jump/editorial/
# class Solution:
#     def canCross(self, stones: List[int]) -> bool:
#         mark = {stone: i for i, stone in enumerate(stones)}
#         n = len(stones)
#
#         @cache
#         def solve(index, prev_jump):
#             if index == n-1:
#                 return True
#
#             res = False
#             for next_jump in [prev_jump-1, prev_jump, prev_jump+1]:
#                 next_stone = stones[index] + next_jump
#                 if next_jump > 0 and next_stone in mark:
#                     res |= solve(mark[next_stone], next_jump)
#                     if res:
#                         return True
#             return res
#
#         return solve(0, 0)


# Runtime
# Details
# 2104ms
# Beats 20.94%of users with Python3
# Memory
# Details
# 48.09MB
# Beats 17.38%of users with Python3
# https://leetcode.com/problems/frog-jump/editorial/
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mark = {stone: i for i, stone in enumerate(stones)}
        n = len(stones)

        dp = [[False] * 2001 for _ in range(2001)]
        dp[0][0] = True
        for index in range(n):
            for prev_jump in range(n+1):
                if dp[index][prev_jump]:
                    for delta in [-1, 0, 1]:
                        jump = prev_jump + delta
                        next_stone = stones[index] + jump
                        if next_stone in mark:
                            dp[mark[next_stone]][jump] = True

        for index in range(n+1):
            if dp[n-1][index]:
                return True
        return False



tests = [
    [[0,1,3,5,6,8,12,17], True],
    [[0,1,2,3,4,8,9,11], False],
]

run_functional_tests(Solution().canCross, tests)
