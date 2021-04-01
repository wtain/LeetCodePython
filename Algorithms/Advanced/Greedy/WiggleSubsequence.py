"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/590/week-3-march-15th-march-21st/3676/
https://leetcode.com/problems/wiggle-subsequence/

Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.
A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.



Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2


Constraints:

1 <= nums.length <= 1000
0 <= nums[i] <= 1000


Follow up: Could you solve this in O(n) time?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 172 ms, faster than 15.84% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.5 MB, less than 15.39% of Python3 online submissions for Wiggle Subsequence.
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         dp = [[1] * 2 for _ in range(n)]
#         if nums[1] > nums[0]:
#             dp[1][0] = 2
#         elif nums[1] < nums[0]:
#             dp[1][1] = 2
#         for i in range(2, n):
#             mx1 = mx2 = 1
#             for j in range(i):
#                 if nums[i] > nums[j]:
#                     mx2 = max(mx2, dp[j][1]+1)
#                 elif nums[i] < nums[j]:
#                     mx1 = max(mx1, dp[j][0]+1)
#             dp[i][0] = mx2
#             dp[i][1] = mx1
#         return max(dp[-1])


# Runtime: 28 ms, faster than 94.57% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.3 MB, less than 73.64% of Python3 online submissions for Wiggle Subsequence.
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         up = [1] * n
#         down = [1] * n
#         for i in range(1, n):
#             if nums[i] == nums[i-1]:
#                 up[i] = up[i - 1]
#                 down[i] = down[i - 1]
#             elif nums[i] > nums[i - 1]:
#                 up[i] = down[i-1] + 1
#                 down[i] = down[i-1]
#             else:
#                 down[i] = up[i-1] + 1
#                 up[i] = up[i-1]
#
#         return max(max(up), max(down))


# Runtime: 36 ms, faster than 62.24% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.4 MB, less than 46.29% of Python3 online submissions for Wiggle Subsequence.
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         up = down = mx = 1
#         for i in range(1, n):
#             if nums[i] > nums[i - 1]:
#                 up = down + 1
#                 mx = max(mx, up)
#             elif nums[i] < nums[i - 1]:
#                 down = up + 1
#                 mx = max(mx, down)
#
#         return mx


# Runtime: 32 ms, faster than 83.94% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.4 MB, less than 46.29% of Python3 online submissions for Wiggle Subsequence.
# class Solution:
#     def wiggleMaxLength(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n < 2:
#             return n
#         up = down = 1
#         for i in range(1, n):
#             if nums[i] > nums[i - 1]:
#                 up = down + 1
#             elif nums[i] < nums[i - 1]:
#                 down = up + 1
#
#         return max(up, down)


# Runtime: 28 ms, faster than 94.57% of Python3 online submissions for Wiggle Subsequence.
# Memory Usage: 14.4 MB, less than 46.29% of Python3 online submissions for Wiggle Subsequence.
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prevdiff = nums[1] - nums[0]
        result = 1 if prevdiff == 0 else 2
        for i in range(2, n):
            diff = nums[i] - nums[i-1]
            if diff > 0 and prevdiff <= 0 or diff < 0 and prevdiff >= 0:
                result += 1
                prevdiff = diff

        return result


tests = [
    ([3,3,3,2,5], 3),

    ([1, 4, 5, 7, 5, 5, 7, 2, 3], 6),

    ([0, 0], 1),
    ([0,0,0], 1),

    ([1,7,4,9,2,5], 6),
    ([1,17,5,10,13,15,10,5,16,8], 7),
    ([1,2,3,4,5,6,7,8,9], 2)
]

run_functional_tests(Solution().wiggleMaxLength, tests)