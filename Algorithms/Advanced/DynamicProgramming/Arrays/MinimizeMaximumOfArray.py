"""
https://leetcode.com/problems/minimize-maximum-of-array/

You are given a 0-indexed array nums comprising of n non-negative integers.

In one operation, you must:

Choose an integer i such that 1 <= i < n and nums[i] > 0.
Decrease nums[i] by 1.
Increase nums[i - 1] by 1.
Return the minimum possible value of the maximum integer of nums after performing any number of operations.



Example 1:

Input: nums = [3,7,1,6]
Output: 5
Explanation:
One set of optimal operations is as follows:
1. Choose i = 1, and nums becomes [4,6,1,6].
2. Choose i = 3, and nums becomes [4,6,2,5].
3. Choose i = 1, and nums becomes [5,5,2,5].
The maximum integer of nums is 5. It can be shown that the maximum number cannot be less than 5.
Therefore, we return 5.
Example 2:

Input: nums = [10,1]
Output: 10
Explanation:
It is optimal to leave nums as is, and since 10 is the maximum value, we return 10.


Constraints:

n == nums.length
2 <= n <= 105
0 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 811 ms
# Beats
# 74.89%
# Memory
# 26.9 MB
# Beats
# 17.45%
# class Solution:
#     def minimizeArrayValue(self, nums: List[int]) -> int:
#         current_max = nums[0]
#         n = len(nums)
#         capacity = 0
#         for i in range(1, n):
#             if nums[i] > current_max:
#                 diff = nums[i] - current_max
#                 decrease = min(diff, capacity)
#                 capacity -= decrease
#                 diff -= decrease
#                 if diff > 0:
#                     each = diff // (i+1)
#                     current_max += each
#                     diff -= each * (i+1)
#                     if diff > 0:
#                         current_max += 1
#                         capacity = i + 1 - diff
#             else:
#                 capacity += current_max - nums[i]
#         return current_max


# Runtime
# 849 ms
# Beats
# 55.32%
# Memory
# 26.9 MB
# Beats
# 17.45%
# https://leetcode.com/problems/minimize-maximum-of-array/solutions/2706383/easy-java-solution-o-n/
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        cmax, csum = nums[0], nums[0]
        n = len(nums)
        for i in range(1, n):
            csum += nums[i]
            result = csum // (i+1) if csum % (i+1) == 0 else csum // (i+1) + 1
            cmax = max(cmax, result)
        return cmax


tests = [
    [[3,7,1,6], 5],
    [[10,1], 10],
    [[6,9,3,8,14], 8],
]

run_functional_tests(Solution().minimizeArrayValue, tests)
