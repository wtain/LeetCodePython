"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3808/
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 4360 ms, faster than 13.60% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.8 MB, less than 17.70% of Python3 online submissions for Longest Increasing Subsequence.
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         n = len(nums)
#         L = [1] * n
#         result = 1
#         for i in range(1, n):
#             mx = 0
#             for j in range(i):
#                 if nums[j] >= nums[i]:
#                     continue
#                 mx = max(mx, L[j])
#             L[i] = mx + 1
#             result = max(result, L[i])
#         return result


# TLE
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         st = []
#         n = len(nums)
#         ml = 1
#         for i in range(n):
#             added = False
#             m = len(st)
#             for j in range(m):
#                 if st[j][0] < nums[i]:
#                     st.append([nums[i], st[j][1]+1])
#                     ml = max(ml, st[-1][1])
#                     added = True
#             if not added:
#                 st.append([nums[i], 1])
#         return ml


# Runtime: 132 ms, faster than 71.36% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.6 MB, less than 74.98% of Python3 online submissions for Longest Increasing Subsequence.
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         subs = [nums[0]]
#         for a in nums:
#             if a > subs[-1]:
#                 subs.append(a)
#             else:
#                 i = 0
#                 while a > subs[i]:
#                     i += 1
#                 subs[i] = a
#         return len(subs)


# Runtime: 76 ms, faster than 88.06% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.5 MB, less than 74.98% of Python3 online submissions for Longest Increasing Subsequence.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = []
        for a in nums:
            i = bisect.bisect_left(subs, a)
            if i == len(subs):
                subs.append(a)
            else:
                subs[i] = a
        return len(subs)


tests = [
    [[10,9,2,5,3,7,101,18], 4],
    [[0,1,0,3,2,3], 4],
    [[7,7,7,7,7,7,7], 1]
]

run_functional_tests(Solution().lengthOfLIS, tests)