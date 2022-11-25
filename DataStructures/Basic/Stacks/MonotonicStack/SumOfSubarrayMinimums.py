"""
https://leetcode.com/problems/sum-of-subarray-minimums/description/

Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444


Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 507 ms
# Beats
# 90.8%
# Memory
# 18.9 MB
# Beats
# 60.96%
# # https://leetcode.com/problems/sum-of-subarray-minimums/solutions/2700011/sum-of-subarray-minimums/
# class Solution:
#     def sumSubarrayMins(self, arr: List[int]) -> int:
#         MOD = 10**9+7
#         st = []
#         smins = 0
#
#         for i in range(len(arr)+1):
#             while st and (i == len(arr) or arr[st[-1]] >= arr[i]):
#                 mid = st.pop()
#                 left_bound = -1 if not st else st[-1]
#                 right_bound = i
#                 cnt = (mid - left_bound) * (right_bound - mid)
#                 smins += cnt * arr[mid]
#             st.append(i)
#
#         return smins % MOD


# Runtime
# 471 ms
# Beats
# 95.84%
# Memory
# 18.8 MB
# Beats
# 60.96%
# https://leetcode.com/problems/sum-of-subarray-minimums/solutions/2700011/sum-of-subarray-minimums/
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        st = []
        dp = [0] * len(arr)
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            if st:
                prev_smaller = st[-1]
                dp[i] = dp[prev_smaller] + (i - prev_smaller) * arr[i]
            else:
                dp[i] = (i+1) * arr[i]
            st.append(i)
        return sum(dp) % MOD


tests = [
    [[3,1,2,4], 17],
    [[11,81,94,43,3], 444]
]

run_functional_tests(Solution().sumSubarrayMins, tests)
