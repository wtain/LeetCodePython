"""
https://leetcode.com/problems/k-concatenation-maximum-sum/

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 109 + 7.



Example 1:

Input: arr = [1,2], k = 3
Output: 9
Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2
Example 3:

Input: arr = [-1,-2], k = 7
Output: 0


Constraints:

1 <= arr.length <= 105
1 <= k <= 105
-104 <= arr[i] <= 104
"""
from itertools import accumulate, chain
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 438 ms
# Beats
# 97.56%
# Memory
# 27.8 MB
# Beats
# 90.24%
# class Solution:
#     def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
#         n = len(arr)
#         s = sum(arr)
#         if all(v < 0 for v in arr):
#             return 0
#         if k == 1:
#             max_sum, cur_sum = 0, 0
#             for v in arr:
#                 cur_sum = max(cur_sum + v, v)
#                 max_sum = max(max_sum, cur_sum)
#             return max_sum
#         arr2 = arr * 2
#         cur_sum = max_sum = 0
#         cur_start = 0
#         max_start, max_end = -1, -1
#         for i in range(2*n):
#             if cur_sum >= 0:
#                 cur_sum = cur_sum + arr2[i]
#             else:
#                 cur_sum = arr2[i]
#                 cur_start = i
#             if cur_sum > max_sum:
#                 max_sum = cur_sum
#                 max_start, max_end = cur_start, i
#         if max_start < n and max_end < n:
#             return max_sum
#         if s < 0:
#             return max_sum
#         MOD = 10**9 + 7
#         return (max_sum + s * (k-2)) % MOD


# Runtime
# 530 ms
# Beats
# 59.75%
# Memory
# 28.7 MB
# Beats
# 25.61%
# # https://leetcode.com/problems/k-concatenation-maximum-sum/solutions/3032432/python-3-2-7-lines-two-versions-w-example-t-m-99-12/
# class Solution:
#     def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
#         if max(arr) <= 0:
#             return 0
#         sm, ct, mx = sum(arr), 0, 0
#         if k > 1:
#             arr.extend(arr)
#         for v in arr:
#             ct = max(ct + v, 0)
#             mx = max(mx, ct)
#         MOD = 10 ** 9 + 7
#         return (mx + (k-2) * sm * (k > 1) * (sm > 0)) % MOD


# Runtime
# 504 ms
# Beats
# 78.66%
# Memory
# 30.2 MB
# Beats
# 7.32%
# https://leetcode.com/problems/k-concatenation-maximum-sum/solutions/3032432/python-3-2-7-lines-two-versions-w-example-t-m-99-12/
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        acc = list(accumulate(chain(*[arr]*(2-(k == 1))), lambda x, y: max(0, x+y), initial=0))
        MOD = 10 ** 9 + 7
        return (max(acc) + (k-2) * sum(arr)*(sum(arr) > 0) * (k>1)) % MOD


tests = [
    [[1,2], 3, 9],
    [[1,-2,1], 5, 2],
    [[-1,-2], 7, 0],
]

run_functional_tests(Solution().kConcatenationMaxSum, tests)
