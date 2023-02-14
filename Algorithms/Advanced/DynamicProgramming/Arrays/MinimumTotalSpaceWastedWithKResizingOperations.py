"""
https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

You are currently designing a dynamic array. You are given a 0-indexed integer array nums, where nums[i] is the number of elements that will be in the array at time i. In addition, you are given an integer k, the maximum number of times you can resize the array (to any size).

The size of the array at time t, sizet, must be at least nums[t] because there needs to be enough space in the array to hold all the elements. The space wasted at time t is defined as sizet - nums[t], and the total space wasted is the sum of the space wasted across every time t where 0 <= t < nums.length.

Return the minimum total space wasted if you can resize the array at most k times.

Note: The array can have any size at the start and does not count towards the number of resizing operations.



Example 1:

Input: nums = [10,20], k = 0
Output: 10
Explanation: size = [20,20].
We can set the initial size to be 20.
The total wasted space is (20 - 10) + (20 - 20) = 10.
Example 2:

Input: nums = [10,20,30], k = 1
Output: 10
Explanation: size = [20,20,30].
We can set the initial size to be 20 and resize to 30 at time 2.
The total wasted space is (20 - 10) + (20 - 20) + (30 - 30) = 10.
Example 3:

Input: nums = [10,20,15,30,20], k = 2
Output: 15
Explanation: size = [10,20,20,30,30].
We can set the initial size to 10, resize to 20 at time 1, and resize to 30 at time 3.
The total wasted space is (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 106
0 <= k <= nums.length - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         BigValue = float('inf')
#         dp = [[BigValue] * (k+1) for _ in range(n)]
#         for i in range(n-1, 0, -1):
#             for j in range(k, 0, -1):
#                 dp[i-1][j] = dp[i][j]
#                 dp[i-1][j-1] = max(0, nums[i] - nums[i-1])
#         return dp[0][0]

# WRONG
# class Solution:
#     def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         maxes = [0] * n
#         maxes[0] = nums[0]
#         for i in range(1, n):
#             maxes[i] = max(nums[i], maxes[i-1])
#         to_visit = [(n-1, k, 0, maxes[-1])]
#         result = float('inf')
#         while to_visit:
#             i, j, w, sz = to_visit.pop()
#             if i > 0:
#                 to_visit.append((i-1, j, w + max(0, maxes[i] - maxes[i-1]), sz))
#             else:
#                 result = min(result, w)
#             if j > 0:
#                 to_visit.append((i-1, j-1, w, maxes[i-1]))
#         return result


# WRONG
# class Solution:
#     def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         maxes = [0] * n
#         maxes[0] = nums[0]
#         for i in range(1, n):
#             maxes[i] = max(nums[i], maxes[i-1])
#         to_visit = [(n-1, k, 0, maxes[-1])]
#         result = float('inf')
#         while to_visit:
#             i, j, w, sz = to_visit.pop()
#             if i > 0:
#                 to_visit.append((i-1, j, w + sz - maxes[i] + max(0, maxes[i] - maxes[i-1]), sz))
#             else:
#                 result = min(result, w)
#             if j > 0:
#                 to_visit.append((i-1, j-1, w + sz - maxes[i], maxes[i-1]))
#         return result


# Runtime
# 6561 ms
# Beats
# 74.7%
# Memory
# 13.8 MB
# Beats
# 96.30%
# https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/solutions/2852427/python3-solution-dp-clean-concise/
class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] + [float('inf')] * n
        for kk in range(k+1):
            for i in range(n-1, -1, -1):
                csum = cmax = 0
                for j in range(i, kk-1, -1):
                    csum += nums[j]
                    cmax = max(cmax, nums[j])
                    dp[i+1] = min(dp[i+1], dp[j] + cmax * (i-j+1) - csum)
        return dp[-1]


tests = [
    [[10,20], 0, 10],
    [[10,20,30], 1, 10],
    [[10,20,15,30,20], 2, 15],
]

run_functional_tests(Solution().minSpaceWastedKResizing, tests)
