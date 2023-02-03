"""
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

Given an array of integers arr, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
All sub-arrays sum are [1,4,9,3,8,5].
Odd sums are [1,9,3,5] so the answer is 4.
Example 2:

Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [[2],[2,4],[2,4,6],[4],[4,6],[6]]
All sub-arrays sum are [2,6,12,4,10,6].
All sub-arrays have even sum and the answer is 0.
Example 3:

Input: arr = [1,2,3,4,5,6,7]
Output: 16


Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1684 ms
# Beats
# 42.12%
# Memory
# 32.3 MB
# Beats
# 5.13%
# class Solution:
#     def numOfSubarrays(self, arr: List[int]) -> int:
#         n = len(arr)
#         dp = [[0] * 2 for _ in range(n)]
#         dp[0][arr[0] % 2] = 1
#         MOD = 10**9 + 7
#         for i in range(1, n):
#             if arr[i] % 2 == 0:
#                 dp[i][0] = dp[i-1][0] + 1
#                 dp[i][1] = dp[i-1][1]
#             else:
#                 dp[i][0] = dp[i - 1][1]
#                 dp[i][1] = dp[i - 1][0] + 1
#             dp[i][0] %= MOD
#             dp[i][1] %= MOD
#         return sum(odd for even, odd in dp) % MOD


# Runtime
# 1349 ms
# Beats
# 52.75%
# Memory
# 18.6 MB
# Beats
# 29.67%
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [0] * 2
        dp[arr[0] % 2] = 1
        MOD = 10**9 + 7
        result = dp[1]
        for i in range(1, n):
            if arr[i] % 2 == 0:
                dp[0] += 1
            else:
                dp[0], dp[1] = dp[1], dp[0] + 1
            dp[0] %= MOD
            dp[1] %= MOD
            result += dp[1]
        return result % MOD


tests = [
    [[1,3,5], 4],
    [[2,4,6], 0],
    [[1,2,3,4,5,6,7], 16],
]

run_functional_tests(Solution().numOfSubarrays, tests)
# run_functional_tests(Solution().numOfSubarrays, tests, run_tests=3)
