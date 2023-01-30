"""
https://leetcode.com/problems/maximum-width-ramp/

A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.



Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.


Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         stack = []
#
#         max_ramp = 0
#         for v in nums:
#             while stack and stack[-1]
#         return max_ramp


# Runtime
# 285 ms
# Beats
# 97.35%
# Memory
# 21 MB
# Beats
# 64.16%
# https://leetcode.com/problems/maximum-width-ramp/solutions/208348/java-c-python-o-n-using-stack/
# class Solution:
#     def maxWidthRamp(self, nums: List[int]) -> int:
#         stack = []
#         max_ramp = 0
#         for i, v in enumerate(nums):
#             if not stack or nums[stack[-1]] > v:
#                 stack.append(i)
#         for j in reversed(range(len(nums))):
#             while stack and nums[stack[-1]] <= nums[j]:
#                 max_ramp = max(max_ramp, j - stack.pop())
#         return max_ramp


# Runtime
# 409 ms
# Beats
# 50%
# Memory
# 21 MB
# Beats
# 46.46%
# https://leetcode.com/problems/maximum-width-ramp/solutions/209582/o-n-time-o-n-space-using-two-array/
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        mins, maxes = [0] * n, [0] * n
        mins[0] = nums[0]
        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])
        maxes[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            maxes[i] = max(maxes[i+1], nums[i])
        left, right = 0, 0
        result = 0
        while right < n:
            if mins[left] <= maxes[right]:
                result = max(result, right-left)
                right += 1
            else:
                left += 1
        return result


tests = [
    [[6,0,8,2,1,5], 4],
    [[9,8,1,0,1,9,4,0,4,1], 7],
]

run_functional_tests(Solution().maxWidthRamp, tests)
