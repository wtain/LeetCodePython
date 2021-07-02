"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.



Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
Example 2:

Input: nums = [1,5,2,4,1]
Output: 14
Example 3:

Input: nums = [8]
Output: 0


Constraints:

1 <= nums.length <= 5000
1 <= nums[i] <= 104
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 132 ms, faster than 49.28% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 15.2 MB, less than 21.18% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         cnt, n, prev = 0, len(nums), nums[0]
#         for i in range(1, n):
#             cnt += max(0, prev + 1 - nums[i])
#             prev = max(prev+1, nums[i])
#         return cnt


# Runtime: 144 ms, faster than 17.94% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 15.3 MB, less than 21.18% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return reduce(lambda res, x: (res[0] + max(0, res[1]+1-x), max(res[1]+1, x)), nums[1:], (0, nums[0]))[0]


tests = [
    [[1,1,1], 3],
    [[1,5,2,4,1], 14],
    [[8], 0]
]

run_functional_tests(Solution().minOperations, tests)