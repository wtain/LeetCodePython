"""
https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/

Given an integer array nums of positive integers, return the average value of all even integers that are divisible by 3.

Note that the average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.



Example 1:

Input: nums = [1,3,6,10,12,15]
Output: 9
Explanation: 6 and 12 are even numbers that are divisible by 3. (6 + 12) / 2 = 9.
Example 2:

Input: nums = [1,2,4,7,10]
Output: 0
Explanation: There is no single number that satisfies the requirement, so return 0.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000
"""
from typing import List

from numpy import mean

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 210 ms
# Beats
# 10.11%
# Memory
# 14.1 MB
# Beats
# 73.78%
# class Solution:
#     def averageValue(self, nums: List[int]) -> int:
#         values = [v for v in nums if v > 0 and v % 6 == 0]
#         if len(values) == 0:
#             return 0
#         return int(mean(values))


# Runtime
# 83 ms
# Beats
# 93.24%
# Memory
# 13.9 MB
# Beats
# 93.49%
class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s, cnt = 0, 0
        for v in nums:
            if v > 0 and v % 6 == 0:
                s += v
                cnt += 1
        return s // cnt if cnt > 0 else 0


tests = [
    [[1,3,6,10,12,15], 9],
    [[1,2,4,7,10], 0]
]

run_functional_tests(Solution().averageValue, tests)
