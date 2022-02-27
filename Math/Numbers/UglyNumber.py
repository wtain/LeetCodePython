"""
https://leetcode.com/problems/ugly-number/
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−231,  231 − 1].
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 28 ms, faster than 91.79% of Python3 online submissions for Ugly Number.
Memory Usage: 13.9 MB, less than 37.73% of Python3 online submissions for Ugly Number.
"""
class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        def factor(num: int, divisor: int) -> int:
            while 0 == num % divisor:
                num //= divisor
            return num
        num = factor(num, 5)
        num = factor(num, 3)
        num = factor(num, 2)
        return 1 == num


tests = [
    [0, False],
    [6, True],
    [8, True],
    [14, False],
    [-2147483648, False]
]

run_functional_tests(Solution().isUgly, tests)
