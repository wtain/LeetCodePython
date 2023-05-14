"""
https://leetcode.com/problems/maximize-score-after-n-operations/description/

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.



Example 1:

Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1
Example 2:

Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
Example 3:

Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14


Constraints:

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 106
"""
import math
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2100 ms
# Beats
# 65.19%
# Memory
# 16.6 MB
# Beats
# 74.5%
# https://leetcode.com/problems/maximize-score-after-n-operations/editorial/
# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         m = len(nums)
#         n = m // 2
#
#         def impl(mask, pairs_picked, memo):
#             nonlocal m
#
#             if memo[mask] != -1:
#                 return memo[mask]
#
#             max_score = 0
#
#             for i in range(m):
#                 if mask & (1 << i):
#                     continue
#                 for j in range(i+1, m):
#                     if mask & (1 << j):
#                         continue
#                     new_mask = mask | (1 << i) | (1 << j)
#                     curr_score = (pairs_picked + 1) * math.gcd(nums[i], nums[j])
#                     remaining_score = impl(new_mask, pairs_picked+1, memo)
#                     max_score = max(max_score, curr_score + remaining_score)
#             memo[mask] = max_score
#             return max_score
#
#         memo_size = 1 << m
#         memo = [-1] * memo_size
#         return impl(0, 0, memo)

# Runtime
# 2741 ms
# Beats
# 50.63%
# Memory
# 16.7 MB
# Beats
# 74.5%
# https://leetcode.com/problems/maximize-score-after-n-operations/editorial/
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        max_states = 1 << len(nums)
        final_mask = max_states - 1
        dp = [0] * max_states

        for state in range(final_mask, -1, -1):
            if state == final_mask:
                dp[state] = 0
                continue
            numbers_taken = bin(state).count('1')
            if numbers_taken % 2:
                continue
            pairs_formed = numbers_taken // 2

            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if state >> i & 1 or state >> j & 1:
                        continue
                    current_score = (pairs_formed+1) * math.gcd(nums[i], nums[j])
                    state_after_picking_curr_pair = state | (1 << i) | (1 << j)
                    remaining_score = dp[state_after_picking_curr_pair]
                    dp[state] = max(dp[state], current_score + remaining_score)
        return dp[0]


tests = [
    [[1,2], 1],
    [[3,4,6,8], 11],
    [[1,2,3,4,5,6], 14],
]

run_functional_tests(Solution().maxScore, tests)
