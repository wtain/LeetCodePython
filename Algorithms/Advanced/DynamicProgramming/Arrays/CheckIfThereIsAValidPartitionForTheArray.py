"""
https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/description/

You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
Return true if the array has at least one valid partition. Otherwise, return false.



Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.
Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.


Constraints:

2 <= nums.length <= 105
1 <= nums[i] <= 106
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 805ms
# Beats 97.69%of users with Python3
# Memory
# Details
# 106.87mb
# Beats 25.38%of users with Python3
# class Solution:
#     def validPartition(self, nums: List[int]) -> bool:
#
#         @cache
#         def impl(m: int) -> bool:
#             if m == 0:
#                 return True
#             if m < 2:
#                 return False
#             if nums[m-1] == nums[m-2] and impl(m-2):
#                 return True
#             if m >= 3 and nums[m-1] == nums[m-2] == nums[m-3] and impl(m-3):
#                 return True
#             return m >= 3 and nums[m - 1] == nums[m - 2]+1 and nums[m-2] == nums[m - 3]+1 and impl(m - 3)
#
#         return impl(len(nums))


# Runtime
# Details
# 849ms
# Beats 93.08%of users with Python3
# Memory
# Details
# 30.52mb
# Beats 63.08%of users with Python3
# class Solution:
#     def validPartition(self, nums: List[int]) -> bool:
#         n = len(nums)
#         dp = [False] * (n+1)
#         dp[0] = True
#         dp[1] = False
#         dp[2] = nums[0] == nums[1]
#         for i in range(2, n):
#             dp[i+1] = nums[i] == nums[i-1] and dp[i-1] or \
#                       nums[i] == nums[i - 1] and nums[i-1] == nums[i-2] and dp[i - 2] or \
#                       nums[i] == nums[i - 1]+1 and nums[i - 1] == nums[i - 2]+1 and dp[i - 2]
#         return dp[-1]


# Runtime
# Details
# 866ms
# Beats 93.08%of users with Python3
# Memory
# Details
# 30.42mb
# Beats 68.46%of users with Python3
# https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/editorial/
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [True, False, False]
        for i in range(n):
            j = i + 1
            dp[j % 3] = i > 0 and nums[i] == nums[i-1] and dp[(j-2) % 3] or \
                      i > 1 and nums[i] == nums[i - 1] and nums[i-1] == nums[i-2] and dp[(j - 3) % 3] or \
                      i > 1 and nums[i] == nums[i - 1]+1 and nums[i - 1] == nums[i - 2]+1 and dp[(j-3) % 3]
        return dp[n % 3]


tests = [
    [[4,4,4,5,6], True],
    [[1,1,1,2], False],
]

run_functional_tests(Solution().validPartition, tests)
