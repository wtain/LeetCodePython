"""
https://leetcode.com/problems/single-number-ii/description/

Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 103 ms
# Beats
# 36.89%
# Memory
# 18 MB
# Beats
# 86.89%
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        mask = 1
        for b in range(32):
            cnt = 0
            for vi in nums:
                if vi & mask:
                    cnt += 1
                    cnt %= 3
            if cnt:
                result |= mask
            mask <<= 1
        if result >= 1 << 31:
            result -= 1 << 32
        return result


tests = [
    [[2,2,3,2], 3],
    [[0,1,0,1,0,1,99], 99],
    [[-2,-2,1,1,4,1,4,4,-4,-2], -4],
]

run_functional_tests(Solution().singleNumber, tests)
