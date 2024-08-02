"""
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description/?envType=daily-question&envId=2024-08-02

A swap is defined as taking two distinct positions in an array and swapping the values in them.

A circular array is defined as an array where we consider the first element and the last element to be adjacent.

Given a binary circular array nums, return the minimum number of swaps required to group all 1's present in the array together at any location.



Example 1:

Input: nums = [0,1,0,1,1,0,0]
Output: 1
Explanation: Here are a few of the ways to group all the 1's together:
[0,0,1,1,1,0,0] using 1 swap.
[0,1,1,1,0,0,0] using 1 swap.
[1,1,0,0,0,0,1] using 2 swaps (using the circular property of the array).
There is no way to group all 1's together with 0 swaps.
Thus, the minimum number of swaps required is 1.
Example 2:

Input: nums = [0,1,1,1,0,0,1,1,0]
Output: 2
Explanation: Here are a few of the ways to group all the 1's together:
[1,1,1,0,0,0,0,1,1] using 2 swaps (using the circular property of the array).
[1,1,1,1,1,0,0,0,0] using 2 swaps.
There is no way to group all 1's together with 0 or 1 swaps.
Thus, the minimum number of swaps required is 2.
Example 3:

Input: nums = [1,1,0,0,1]
Output: 0
Explanation: All the 1's are already grouped together due to the circular property of the array.
Thus, the minimum number of swaps required is 0.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""
import math
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# 788
# ms
# Beats
# 16.44%
# Analyze Complexity
# Memory
# 23.38
# MB
# Beats
# 5.18%
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/editorial/?envType=daily-question&envId=2024-08-02
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#
#         def helper(v):
#             n = len(nums)
#             right_sum = [0] * (n+1)
#
#             for i in range(n-1, -1, -1):
#                 right_sum[i] = right_sum[i+1]
#                 if nums[i] == v ^ 1:
#                     right_sum[i] += 1
#
#             total = right_sum[0]
#             curr_swap_cnt = 0
#             min_swaps = total - right_sum[n-total]
#
#             for i in range(total):
#                 if nums[i] == (v ^ 1):
#                     curr_swap_cnt += 1
#                     remaining = total - i - 1
#                     req_swaps = ((i+1) - curr_swap_cnt) + (remaining - right_sum[n-remaining])
#                     min_swaps = min(min_swaps, req_swaps)
#             return min_swaps
#
#         return min(helper(0), helper(1))


# Runtime
# 723
# ms
# Beats
# 51.80%
# Analyze Complexity
# Memory
# 20.29
# MB
# Beats
# 71.40%
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/editorial/?envType=daily-question&envId=2024-08-02
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         def helper(v):
#             n = len(nums)
#             total_val_cnt = 0
#             for i in range(n-1, -1, -1):
#                 if nums[i] == v:
#                     total_val_cnt += 1
#
#             if total_val_cnt == n or total_val_cnt == 0:
#                 return 0
#
#             start, end = 0, 0
#             max_val_in_window = 0
#             cur_val_in_window = 0
#
#             while end < total_val_cnt:
#                 if nums[end] == v:
#                     cur_val_in_window += 1
#                 end += 1
#             max_val_in_window = max(max_val_in_window, cur_val_in_window)
#
#             while end < n:
#                 if nums[start] == v:
#                     cur_val_in_window -= 1
#                 start += 1
#                 if nums[end] == v:
#                     cur_val_in_window += 1
#                 end += 1
#                 max_val_in_window = max(max_val_in_window, cur_val_in_window)
#             return total_val_cnt - max_val_in_window
#
#         return min(helper(0), helper(1))

# Runtime
# 760
# ms
# Beats
# 30.40%
# Analyze Complexity
# Memory
# 20.68
# MB
# Beats
# 37.84%
# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/editorial/?envType=daily-question&envId=2024-08-02
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        min_swaps = math.inf
        total_ones = sum(nums)
        ones_count = nums[0]
        end = 0

        for start in range(len(nums)):
            if start != 0:
                ones_count -= nums[start-1]
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]
            min_swaps = min(min_swaps, total_ones - ones_count)
        return min_swaps


tests = [
    [[0,1,0,1,1,0,0], 1],
    [[0,1,1,1,0,0,1,1,0], 2],
    [[1,1,0,0,1], 0],
]

run_functional_tests(Solution().minSwaps, tests)
