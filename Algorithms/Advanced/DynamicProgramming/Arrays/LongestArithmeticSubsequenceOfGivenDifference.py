"""
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: arr = [1,2,3,4], difference = 1
Output: 4
Explanation: The longest arithmetic subsequence is [1,2,3,4].
Example 2:

Input: arr = [1,3,5,7], difference = 1
Output: 1
Explanation: The longest arithmetic subsequence is any single element.
Example 3:

Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
Output: 4
Explanation: The longest arithmetic subsequence is [7,5,3,1].


Constraints:

1 <= arr.length <= 105
-104 <= arr[i], difference <= 104
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def longestSubsequence(self, arr: List[int], difference: int) -> int:
#         n = len(arr)
#         longest = 1
#         dp = [1] * n
#         for i in range(1, n):
#             mx = 0
#             for j in range(i):
#                 if arr[j] + difference != arr[i]:
#                     continue
#                 mx = max(mx, dp[j])
#             dp[i] = 1 + mx
#             longest = max(longest, dp[i])
#         return longest


# Runtime: 588 ms, faster than 55.28% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
# Memory Usage: 27.6 MB, less than 99.67% of Python3 online submissions for Longest Arithmetic Subsequence of Given Difference.
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        longest = 1
        dp = defaultdict(int)
        dp[arr[0]] = 1
        for i in range(1, n):
            l = 1 + dp[arr[i]-difference]
            dp[arr[i]] = l
            longest = max(longest, l)
        return longest


tests = [
    [[1,2,3,4], 1, 4],
    [[1,3,5,7], 1, 1],
    [[1,5,7,8,5,3,4,2,1], -2, 4]
]

run_functional_tests(Solution().longestSubsequence, tests)
