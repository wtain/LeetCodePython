"""
https://leetcode.com/problems/fraction-to-recurring-decimal/
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.



Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"
Example 4:

Input: numerator = 4, denominator = 333
Output: "0.(012)"
Example 5:

Input: numerator = 1, denominator = 5
Output: "0.2"


Constraints:

-231 <= numerator, denominator <= 231 - 1
denominator != 0
"""
from typing import Dict


# Runtime: 24 ms, faster than 95.15% of Python3 online submissions for Fraction to Recurring Decimal.
# Memory Usage: 14.4 MB, less than 66.23% of Python3 online submissions for Fraction to Recurring Decimal.
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)
        if numerator < 0 or denominator < 0:
            result = self.fractionToDecimal(abs(numerator), abs(denominator))
            return "-" + result if result != "0" else "0"
        rem = numerator // denominator
        if rem > 0:
            result = str(rem)

            fract = self.fractionToDecimal(numerator-rem * denominator, denominator)
            if fract[0] == "0":
                fract = fract[1:]
            return result + fract
        remainder = numerator
        seen: Dict[int, int] = {}
        result = ""
        i = 0
        while remainder:
            if remainder in seen:
                result = result[0:seen[remainder]+1] + "(" + result[seen[remainder]+1:] + ")"
                break
            seen[remainder] = i
            res = remainder // denominator
            result += str(res)
            if i == 0:
                result += "."

            i += 1
            remainder -= res * denominator
            remainder *= 10
        if not result:
            result = "0"
        if result[-1] == ".":
            result = result[0:-1]
        return result


tests = [
    (0, -5, "0"),

    (-2147483648, 3, "-715827882.(6)"),

    (-50, 8, "-6.25"),

    (0, 2, "0"),

    (1, 2, "0.5"),
    (2, 1, "2"),
    (2, 3, "0.(6)"),
    (4, 333, "0.(012)"),
    (1, 5, "0.2")
]

for test in tests:
    result = Solution().fractionToDecimal(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + result)