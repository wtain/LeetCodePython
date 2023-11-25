"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/?envType=daily-question&envId=2023-11-25

You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).



Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]


Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= nums[i + 1] <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 793
# ms
# Beats
# 14.10%
# of users with Python3
# Memory
# 32.74
# MB
# Beats
# 6.73%
# of users with Python3
# class Solution:
#     def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         prefix, suffix = [0] * n, [0] * n
#         prefix[0] = nums[0]
#         for i in range(1, n):
#             prefix[i] = prefix[i-1] + nums[i]
#         suffix[-1] = nums[-1]
#         for i in range(n-2, -1, -1):
#             suffix[i] = suffix[i+1] + nums[i]
#         result = [0] * n
#         for i in range(n):
#             left = prefix[i-1] if i > 0 else 0
#             right = suffix[i+1] if i+1 < n else 0
#             result[i] = nums[i] * i - left + right - nums[i] * (n-i-1)
#         return result

# Runtime
# 710
# ms
# Beats
# 78.21%
# of users with Python3
# Memory
# 31.89
# MB
# Beats
# 30.45%
# of users with Python3
# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/editorial/?envType=daily-question&envId=2023-11-25
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        result = []
        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            left_count = i
            right_count = n - 1 - i
            left_total = left_count * nums[i] - left_sum
            right_total = right_sum - right_count * nums[i]
            result.append(left_total+right_total)
            left_sum += nums[i]
        return result


tests = [
    [[2,3,5], [4,3,5]],
    [[1,4,6,8,10], [24,15,13,15,21]],
]

run_functional_tests(Solution().getSumAbsoluteDifferences, tests)
