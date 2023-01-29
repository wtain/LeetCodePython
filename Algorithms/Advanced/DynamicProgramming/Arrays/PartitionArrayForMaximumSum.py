"""
https://leetcode.com/problems/partition-array-for-maximum-sum/

Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1


Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 109
1 <= k <= arr.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 494 ms
# Beats
# 91.90%
# Memory
# 13.9 MB
# Beats
# 92.62%
# https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/290863/java-c-python-dp-o-k-space/
# class Solution:
#     def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
#         n = len(arr)
#         dp = [0] * (n+1)
#         for i in range(1, n+1):
#             curr_max = 0
#             for kk in range(1, min(k, i)+1):
#                 curr_max = max(curr_max, arr[i-kk])
#                 dp[i] = max(dp[i], dp[i-kk] + curr_max * kk)
#         return dp[n]


# Runtime
# 474 ms
# Beats
# 95.95%
# Memory
# 13.9 MB
# Beats
# 92.62%
# https://leetcode.com/problems/partition-array-for-maximum-sum/solutions/290863/java-c-python-dp-o-k-space/
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * k
        for i in range(1, n+1):
            best = curr_max = 0
            for kk in range(1, min(k, i)+1):
                curr_max = max(curr_max, arr[i-kk])
                best = max(best, dp[(i-kk) % k] + curr_max * kk)
            dp[i % k] = best
        return dp[n % k]


tests = [
    [[1,15,7,9,2,5,10], 3, 84],
    [[1,4,1,5,7,3,6,1,9,9,3], 4, 83],
    [[1], 1, 1],
]

run_functional_tests(Solution().maxSumAfterPartitioning, tests)
