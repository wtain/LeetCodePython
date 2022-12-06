"""
https://leetcode.com/problems/number-of-common-factors/

Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.



Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.
Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.


Constraints:

1 <= a, b <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 35 ms
# Beats
# 89.55%
# Memory
# 13.8 MB
# Beats
# 62.28%
class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        divisor_max = max(a, b)
        common_divisor_count = 1
        for d in range(2, divisor_max+1):
            if a % d == 0 and b % d == 0:
                common_divisor_count += 1
        return common_divisor_count


tests = [
    [12, 6, 4],
    [25, 30, 2]
]

run_functional_tests(Solution().commonFactors, tests)
