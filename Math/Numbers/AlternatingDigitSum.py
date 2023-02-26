"""
https://leetcode.com/problems/alternating-digit-sum/

You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.



Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.
Example 2:

Input: n = 111
Output: 1
Explanation: (+1) + (-1) + (+1) = 1.
Example 3:

Input: n = 886996
Output: 0
Explanation: (+8) + (-8) + (+6) + (-9) + (+9) + (-6) = 0.


Constraints:

1 <= n <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 39 ms
# Beats
# 44.58%
# Memory
# 13.8 MB
# Beats
# 49.75%
class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        i = 0
        sign = 1
        while n:
            result += sign * (n % 10)
            sign = -sign
            i += 1
            n //= 10
        if i % 2 == 0:
            result = -result
        return result


tests = [
    [521, 4],
    [111, 1],
    [886996, 0],
]

run_functional_tests(Solution().alternateDigitSum, tests)
