"""
https://leetcode.com/problems/tallest-billboard/description/

You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.



Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.


Constraints:

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 788 ms
# Beats
# 41.67%
# Memory
# 27.3 MB
# Beats
# 29.17%
# https://leetcode.com/problems/tallest-billboard/editorial/
# class Solution:
#     def tallestBillboard(self, rods: List[int]) -> int:
#
#         def helper(half_rods):
#             states = set()
#             states.add((0, 0))
#             for r in half_rods:
#                 new_states = set()
#                 for left, right in states:
#                     new_states.add((left+r, right))
#                     new_states.add((left, right + r))
#                 states |= new_states
#
#             dp = {}
#             for left, right in states:
#                 dp[left - right] = max(dp.get(left - right, 0), left)
#             return dp
#
#         n = len(rods)
#         first_half = helper(rods[:n // 2])
#         second_half = helper(rods[n // 2:])
#         result = 0
#         for diff in first_half:
#             if -diff in second_half:
#                 result = max(result, first_half[diff] + second_half[-diff])
#
#         return result


# Runtime
# 572 ms
# Beats
# 64.58%
# Memory
# 16.9 MB
# Beats
# 62.50%
# https://leetcode.com/problems/tallest-billboard/editorial/
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        dp = { 0 : 0 }

        for r in rods:
            new_dp = dp.copy()
            for diff, taller in dp.items():
                shorter = taller - diff
                new_dp[diff + r] = max(new_dp.get(diff + r, 0), taller + r)
                new_diff = abs(shorter + r - taller)
                new_taller = max(shorter + r, taller)
                new_dp[new_diff] = max(new_dp.get(new_diff, 0), new_taller)
            dp = new_dp
        return dp.get(0, 0)


tests = [
    [[1,2,3,6], 6],
    [[1,2,3,4,5,6], 10],
    [[1,2], 0],
]

run_functional_tests(Solution().tallestBillboard, tests)
