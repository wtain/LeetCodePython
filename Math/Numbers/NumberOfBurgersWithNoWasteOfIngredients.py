"""
https://leetcode.com/problems/number-of-burgers-with-no-waste-of-ingredients/

Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

Jumbo Burger: 4 tomato slices and 1 cheese slice.
Small Burger: 2 Tomato slices and 1 cheese slice.
Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].



Example 1:

Input: tomatoSlices = 16, cheeseSlices = 7
Output: [1,6]
Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese.
There will be no remaining ingredients.
Example 2:

Input: tomatoSlices = 17, cheeseSlices = 4
Output: []
Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
Example 3:

Input: tomatoSlices = 4, cheeseSlices = 17
Output: []
Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.


Constraints:

0 <= tomatoSlices, cheeseSlices <= 107
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# 38 ms
# Beats
# 54.86%
# Memory
# 13.8 MB
# Beats
# 66.67%
class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # number of burgers = cheeseSlices = a + b
        # 4*a+2*b = tomatoSlices
        # 2*a+b = tomatoSlices // 2
        # a = tomatoSlices // 2 - cheeseSlices
        if tomatoSlices % 2:
            return []
        jumbo_count = tomatoSlices // 2 - cheeseSlices
        if jumbo_count < 0:
            return []
        small_count = cheeseSlices - jumbo_count
        if small_count < 0:
            return []
        return [jumbo_count, small_count]


tests = [
    [2385088, 164763, []],
    [16, 7, [1,6]],
    [17, 4, []],
    [4, 17, []],
]

run_functional_tests(Solution().numOfBurgers, tests)
