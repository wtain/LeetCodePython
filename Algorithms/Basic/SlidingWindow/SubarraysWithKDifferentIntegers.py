"""
https://leetcode.com/problems/subarrays-with-k-different-integers/description/?envType=daily-question&envId=2024-03-30

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# NOT FINISHED
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#         cnt = Counter()
#         n = len(nums)
#         result = 0
#         i1 = 0
#         for i2 in range(n):
#             cnt[nums[i2]] += 1
#             if len(cnt.keys()) == k:
#                 result += 1
#             while len(cnt.keys()) > k and i1 < i2:
#                 cnt[nums[i1]] -= 1
#                 i1 += 1
#         return result

# Runtime
# 488
# ms
# Beats
# 6.87%
# of users with Python3
# Memory
# 20.07
# MB
# Beats
# 37.63%
# of users with Python3
# https://leetcode.com/problems/subarrays-with-k-different-integers/editorial/?envType=daily-question&envId=2024-03-30
# class Solution:
#     def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
#
#         def slidingWindowsAtMost(nums: List[int], distinctK: int) -> int:
#             freq = Counter()
#             left, total = 0, 0
#
#             for right in range(len(nums)):
#                 freq[nums[right]] += 1
#
#                 while len(freq.keys()) > distinctK:
#                     freq[nums[left]] -= 1
#                     if freq[nums[left]] == 0:
#                         del freq[nums[left]]
#                     left += 1
#                 total += right - left + 1
#             return total
#
#         return slidingWindowsAtMost(nums, k) - slidingWindowsAtMost(nums, k-1)


# Runtime
# 327
# ms
# Beats
# 80.83%
# of users with Python3
# Memory
# 20.56
# MB
# Beats
# 17.75%
# of users with Python3
# https://leetcode.com/problems/subarrays-with-k-different-integers/editorial/?envType=daily-question&envId=2024-03-30
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left, right, total, curr_cnt = 0, 0, 0, 0

        while right < len(nums):
            freq[nums[right]] += 1
            if freq[nums[right]] == 1:
                k -= 1

            if k < 0:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    k += 1
                left += 1
                curr_cnt = 0

            if k == 0:
                while freq[nums[left]] > 1:
                    freq[nums[left]] -= 1
                    left += 1
                    curr_cnt += 1
                total += (curr_cnt + 1)

            right += 1
        return total


tests = [
    [[1,2,1,2,3], 2, 7],
    [[1,2,1,3,4], 3, 3],
]

run_functional_tests(Solution().subarraysWithKDistinct, tests)
