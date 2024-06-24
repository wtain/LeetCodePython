"""
https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/description/?envType=daily-question&envId=2024-06-24

You are given a binary array nums and an integer k.

A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [0,1,0], k = 1
Output: 2
Explanation: Flip nums[0], then flip nums[2].
Example 2:

Input: nums = [1,1,0], k = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we cannot make the array become [1,1,1].
Example 3:

Input: nums = [0,0,0,1,0,1,1,0], k = 3
Output: 3
Explanation:
Flip nums[0],nums[1],nums[2]: nums becomes [1,1,1,1,0,1,1,0]
Flip nums[4],nums[5],nums[6]: nums becomes [1,1,1,1,1,0,0,0]
Flip nums[5],nums[6],nums[7]: nums becomes [1,1,1,1,1,1,1,1]


Constraints:

1 <= nums.length <= 105
1 <= k <= nums.length
"""
from collections import deque
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 780
# ms
# Beats
# 88.03%
# Analyze Complexity
# Memory
# 19.65
# MB
# Beats
# 51.41%
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/editorial/?envType=daily-question&envId=2024-06-24
# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         flipped = [False] * n
#         valid_flips_from_past_window = 0
#         flip_count = 0
#         for i in range(n):
#             if i >= k:
#                 if flipped[i-k]:
#                     valid_flips_from_past_window -= 1
#
#             if valid_flips_from_past_window % 2 == nums[i]:
#                 if i + k > n:
#                     return -1
#                 valid_flips_from_past_window += 1
#                 flipped[i] = True
#                 flip_count += 1
#         return flip_count


# Runtime
# 807
# ms
# Beats
# 42.25%
# Analyze Complexity
# Memory
# 19.64
# MB
# Beats
# 51.41%
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/editorial/?envType=daily-question&envId=2024-06-24
# class Solution:
#     def minKBitFlips(self, nums: List[int], k: int) -> int:
#         n = len(nums)
#         flip_queue = deque()
#         flipped = 0
#         result = 0
#         for i, num in enumerate(nums):
#             if i >= k:
#                 flipped ^= flip_queue[0]
#
#             if flipped == nums[i]:
#                 if i + k > n:
#                     return -1
#
#                 flip_queue.append(1)
#                 flipped ^= 1
#                 result += 1
#             else:
#                 flip_queue.append(0)
#             if len(flip_queue) > k:
#                 flip_queue.popleft()
#         return result


# Runtime
# 808
# ms
# Beats
# 39.44%
# Memory
# 19.62
# MB
# Beats
# 51.41%
# https://leetcode.com/problems/minimum-number-of-k-consecutive-bit-flips/editorial/?envType=daily-question&envId=2024-06-24
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        current_flips, total_flips = 0, 0
        n = len(nums)
        for i in range(n):
            if i >= k and nums[i-k] == 2:
                current_flips -= 1
            if current_flips % 2 == nums[i]:
                if i + k > n:
                    return -1
                nums[i] = 2
                current_flips += 1
                total_flips += 1
        return total_flips


tests = [
    [[0,1,0], 1, 2],
    [[1,1,0], 2, -1],
    [[0,0,0,1,0,1,1,0], 3, 3],
]

run_functional_tests(Solution().minKBitFlips, tests)
