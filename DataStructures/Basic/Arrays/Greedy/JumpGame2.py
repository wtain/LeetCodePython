"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         jumps = 0
#         i = 0
#         while i < n-1:
#             mx = 0
#             mj = 0
#             for j in range(1, nums[i]+1):
#                 if i + nums[i+j] > mx:
#                     mj = j
#             jumps += 1
#             i += mj
#         return jumps


# Runtime: 32 ms, faster than 68.42% of Python3 online submissions for Jump Game II.
# Memory Usage: 14.1 MB, less than 79.51% of Python3 online submissions for Jump Game II.
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        furthest = 0
        curr_end = 0
        for i in range(n-1):
            furthest = max(furthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = furthest
        return jumps


tests = [
    [[2,3,1,1,4], 2],
    [[2,3,0,1,4], 2]
]

run_functional_tests(Solution().jump, tests)