"""
https://leetcode.com/problems/largest-number/description/?envType=daily-question&envId=2024-09-18

Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.



Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
"""
import functools
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         return "".join(reversed(sorted([str(v) for v in nums])))


# class Solution:
#     def largestNumber(self, nums: List[int]) -> str:
#         snums = [str(v) for v in nums]
#         return "".join(reversed(sorted([str(v) for v in nums])))


# Runtime
# 39
# ms
# Beats
# 68.62%
# Analyze Complexity
# Memory
# 16.57
# MB
# Beats
# 32.99%
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a, b):
            if a + b < b + b:
                return -1
            elif a + b > b + a:
                return 1
            return 0

        ns = list(reversed(sorted([str(v) for v in nums], key=functools.cmp_to_key(cmp))))
        if ns[0] == "0":
            return "0"
        return "".join(ns)


tests = [
    [[0,0], "0"],
    [[10,2], "210"],
    [[3,30,34,5,9], "9534330"],
]

run_functional_tests(Solution().largestNumber, tests)
