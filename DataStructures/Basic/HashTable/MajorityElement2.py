"""
https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 104
-109 <= nums[i] <= 109


Follow up: Could you solve the problem in linear time and in O(1) space?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 105ms
# Beats 84.77%of users with Python3
# Memory
# Details
# 17.69MB
# Beats 84.36%of users with Python3
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m1, m2 = -1, -1
        i1, i2 = 0, 0
        for v in nums:
            if i1 == 0 and not (v == m2 and i2 > 0):
                m1 = v
                i1 = 1
            elif i2 == 0 and not (v == m1 and i1 > 0):
                m2 = v
                i2 = 1
            elif m1 == v:
                i1 += 1
            elif m2 == v:
                i2 += 1
            else:
                i1 -= 1
                i2 -= 1
        n3 = len(nums) // 3
        result = []
        if i1 > 0 and sum(1 for v in nums if v == m1) > n3:
            result.append(m1)
        if i2 > 0 and sum(1 for v in nums if v == m2) > n3:
            result.append(m2)
        return result


tests = [
    [[3,2,3], [3]],
    [[1], [1]],
    [[1,2], [1,2]],
]

run_functional_tests(Solution().majorityElement, tests)
