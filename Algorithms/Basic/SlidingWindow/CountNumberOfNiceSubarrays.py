"""
https://leetcode.com/problems/count-number-of-nice-subarrays/description/?envType=daily-question&envId=2024-06-22

Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16


Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         result = 0
#         n = len(nums)
#         cnt = 0
#         i1 = 0
#         for i2 in range(n):
#             if nums[i2] % 2:
#                 cnt += 1
#             if cnt == k:
#                 result += 1
#             while cnt > k and i1 < i2:
#                 if nums[i1] % 2:
#                     cnt -= 1
#                     if cnt == k:
#                         result += 1
#                 i1 += 1
#         return result


# class Solution:
#     def numberOfSubarrays(self, nums: List[int], k: int) -> int:
#         result = 0
#         n = len(nums)
#         cnt = 0
#         i1, i2 = -1, 0
#         while i2 < n:
#             while i2 < n and cnt < k:
#                 if nums[i2] % 2:
#                     cnt += 1
#                 i2 += 1
#         return result

# Runtime
# 646
# ms
# Beats
# 30.80%
# Analyze Complexity
# Memory
# 23.59
# MB
# Beats
# 67.27%
# https://leetcode.com/problems/count-number-of-nice-subarrays/editorial/?envType=daily-question&envId=2024-06-22
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def at_most(k):
            size, subarrays, start = 0, 0, 0
            for end in range(n):
                size += nums[end] % 2
                while size > k:
                    size -= nums[start] % 2
                    start += 1
                subarrays += end - start + 1
            return subarrays

        return at_most(k) - at_most(k-1)


tests = [
    [[1,1,2,1,1], 3, 2],
    [[2,4,6], 1, 0],
    [[2,2,2,1,2,2,1,2,2,2], 2, 16],
]

run_functional_tests(Solution().numberOfSubarrays, tests)
