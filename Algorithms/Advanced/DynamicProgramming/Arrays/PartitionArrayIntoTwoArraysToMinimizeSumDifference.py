"""
https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/description/

You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.



Example 1:

example-1
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
Example 2:

Input: nums = [-36,36]
Output: 72
Explanation: One optimal partition is: [-36] and [36].
The absolute difference between the sums of the arrays is abs((-36) - (36)) = 72.
Example 3:

example-3
Input: nums = [2,-1,0,4,-2,-9]
Output: 0
Explanation: One optimal partition is: [2,4,-9] and [-1,0,-2].
The absolute difference between the sums of the arrays is abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0.


Constraints:

1 <= n <= 15
nums.length == 2 * n
-107 <= nums[i] <= 107
"""
import bisect
from itertools import combinations
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         n2 = n // 2
#         S = sum(nums)
#         dp = {(0, 0)}
#         for num in nums:
#             dp |= {(num + v, c+1) for v, c in dp}
#         return min(abs(S - v - v) for (v, c) in dp if c == n2)

# TLE
# class Solution:
#     def minimumDifference(self, nums: List[int]) -> int:
#         n = len(nums)
#         n2 = n // 2
#         S = sum(nums)
#         dp = {(0, 0)}
#         for num in nums:
#             dp |= {(num + v, c+1) for v, c in dp if c < n2}
#         return min(abs(S - v - v) for (v, c) in dp if c == n2)


# Runtime
# 3365 ms
# Beats
# 65.49%
# Memory
# 16.5 MB
# Beats
# 69.65%
# https://leetcode.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference/solutions/1513435/python-easy-explanation-meet-in-the-middle/
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2

        def get_sums(part: List[int]):
            nonlocal n
            result = {}
            for k in range(1, n+1):
                sums = []
                for comb in combinations(part, k):
                    s = sum(comb)
                    sums.append(s)
                result[k] = sums
            return result

        left_part, right_part = nums[:n], nums[n:]
        left_sums, right_sums = get_sums(left_part), get_sums(right_part)
        result = abs(sum(left_part) - sum(right_part))
        total = sum(nums)
        half = total // 2
        for k in range(1, n):
            left, right = left_sums[k], right_sums[n-k]
            right.sort()
            for x in left:
                r = half - x
                p = bisect.bisect_left(right, r)
                for q in [p, p-1]:
                    if 0 <= q < len(right):
                        left_ans_sum = x + right[q]
                        right_ans_sum = total - left_ans_sum
                        diff = abs(right_ans_sum - left_ans_sum)
                        result = min(result, diff)
        return result


tests = [
    [[3,9,7,3], 2],
    [[-36,36], 72],
    [[2,-1,0,4,-2,-9], 0],
    [[7772197,4460211,-7641449,-8856364,546755,-3673029,527497,-9392076,3130315,-5309187,-4781283,5919119,3093450,1132720,6380128,-3954678,-1651499,-7944388,-3056827,1610628,7711173,6595873,302974,7656726,-2572679,0,2121026,-5743797,-8897395,-9699694], 1],
]

run_functional_tests(Solution().minimumDifference, tests)
