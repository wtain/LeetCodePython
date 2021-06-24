"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3782/
https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/

We are given an array nums of positive integers, and two positive integers left and right (left <= right).

Return the number of (contiguous, non-empty) subarrays such that the value of the maximum array element in that subarray is at least left and at most right.

Example:
Input:
nums = [2, 1, 4, 3]
left = 2
right = 3
Output: 3
Explanation: There are three subarrays that meet the requirements: [2], [2, 1], [3].
Note:

left, right, and nums[i] will be an integer in the range [0, 109].
The length of nums will be in the range of [1, 50000].
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#         cnt = 0
#         i, j = 0, 0
#         n = len(nums)
#         j = -1
#         mx = nums[0]
#         i = 0
#         while i < n:
#             mx = max(mx, nums[i])
#             # print(mx)
#             if left > mx or mx > right:
#                 while i < n and not (left <= nums[i] <= right):
#                     i += 1
#                 if i < n:
#                     mx = nums[i]
#                 j = i - 1
#             else:
#                 print(nums[j+1:i+1])
#                 cnt += 1
#                 i += 1
#
#         return cnt

# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/discuss/1278624/Python-simple-O(n)-solution-explained
# Runtime: 332 ms, faster than 71.61% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
# Memory Usage: 15.8 MB, less than 56.47% of Python3 online submissions for Number of Subarrays with Bounded Maximum.
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        li, ri, res = -1, -1, 0
        for i, x in enumerate(nums):
            if x >= left:
                li = i
            if x > right:
                ri = i
            res += li - ri
        return res


tests = [
    [[2,9,2,5,6], 2, 8, 7],

    [[2, 1, 4, 3], 2, 3, 3]
]

# [2]
# [2, 1]
# [3]

run_functional_tests(Solution().numSubarrayBoundedMax, tests)