"""
https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/description/

You are given an array of integers nums and an integer target.

Return the number of non-empty subsequences of nums such that the sum of the minimum and maximum element on it is less or equal to target. Since the answer may be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [3,5,6,7], target = 9
Output: 4
Explanation: There are 4 subsequences that satisfy the condition.
[3] -> Min value + max value <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)
Example 2:

Input: nums = [3,3,6,8], target = 10
Output: 6
Explanation: There are 6 subsequences that satisfy the condition. (nums can have repeated numbers).
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
Example 3:

Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 106
1 <= target <= 106
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 917 ms
# Beats
# 60.61%
# Memory
# 28.6 MB
# Beats
# 14.83%
# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         MOD = 10 ** 9 + 7
#         nums.sort()
#         n = len(nums)
#         result = 0
#         for i in range(n):
#             t = target - nums[i]
#             i1 = bisect.bisect_right(nums, t) - 1
#             if i1 >= i:
#                 result += pow(2, i1 - i, MOD)
#                 result %= MOD
#
#         return result


# Runtime
# 614 ms
# Beats
# 98.98%
# Memory
# 29.2 MB
# Beats
# 8.18%
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/editorial/
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)

        power = [0] * n
        power[0] = 1
        for i in range(1, n):
            power[i] = (power[i-1] * 2) % MOD

        result = 0
        left, right = 0, n-1
        while left <= right:
            if nums[left] + nums[right] <= target:
                result += power[right - left]
                result %= MOD
                left += 1
            else:
                right -= 1

        return result


tests = [
    [[3,5,6,7], 9, 4],
    [[3,3,6,8], 10, 6],
    [[2,3,3,4,6,7], 12, 61],
]

run_functional_tests(Solution().numSubseq, tests)
