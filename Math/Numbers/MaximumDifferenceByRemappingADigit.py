"""
https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

You are given an integer num. You know that Danny Mittal will sneakily remap one of the 10 possible digits (0 to 9) to another digit.

Return the difference between the maximum and minimum values Danny can make by remapping exactly one digit in num.

Notes:

When Danny remaps a digit d1 to another digit d2, Danny replaces all occurrences of d1 in num with d2.
Danny can remap a digit to itself, in which case num does not change.
Danny can remap different digits for obtaining minimum and maximum values respectively.
The resulting number after remapping can contain leading zeroes.
We mentioned "Danny Mittal" to congratulate him on being in the top 10 in Weekly Contest 326.


Example 1:

Input: num = 11891
Output: 99009
Explanation:
To achieve the maximum value, Danny can remap the digit 1 to the digit 9 to yield 99899.
To achieve the minimum value, Danny can remap the digit 1 to the digit 0, yielding 890.
The difference between these two numbers is 99009.
Example 2:

Input: num = 90
Output: 99
Explanation:
The maximum value that can be returned by the function is 99 (if 0 is replaced by 9) and the minimum value that can be returned by the function is 0 (if 9 is replaced by 0).
Thus, we return 99.


Constraints:

1 <= num <= 108
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 32 ms
# Beats
# 68.23%
# Memory
# 13.8 MB
# Beats
# 53.85%
class Solution:
    def minMaxDifference(self, num: int) -> int:

        power = 1
        while 10*power <= num:
            power *= 10

        v1, v2 = 0, 0
        p = power
        changed1, changed2 = False, False
        map1, map2 = list(range(10)), list(range(10))
        while p >= 1:
            d = num // p
            num %= p
            if not changed1 and d:
                map1[d] = 0
                changed1 = True
            if not changed2 and d != 9:
                map2[d] = 9
                changed2 = True
            v1 = 10 * v1 + map1[d]
            v2 = 10 * v2 + map2[d]
            p //= 10

        return v2 - v1


tests = [
    [100000000, 900000000],
    [11891, 99009],
    [90, 99],
]

run_functional_tests(Solution().minMaxDifference, tests)
