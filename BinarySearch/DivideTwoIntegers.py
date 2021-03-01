"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3654/
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For this problem, assume that your function returns 231 − 1 when the division result overflows.


Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1


Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


# Runtime: 36 ms, faster than 52.92% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 14.1 MB, less than 94.93% of Python3 online submissions for Divide Two Integers.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT = -(1 << 31)
        MAX_INT = (1 << 31) - 1
        if not divisor or dividend == MIN_INT and divisor == -1:
            return MAX_INT
        if dividend == MIN_INT and divisor == 1:
            return MIN_INT
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            t = divisor
            multiple = 1
            while dividend >= (t << 1):
                t <<= 1
                multiple <<= 1
            dividend -= t
            result += multiple
        return result if sign > 0 else -result


tests = [
    (10, 3, 3),
    (7, -3, -2),
    (0, 1, 0),
    (1, 1, 1)
]

for test in tests:
    result = Solution().divide(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))