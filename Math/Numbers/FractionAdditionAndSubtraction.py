"""
https://leetcode.com/problems/fraction-addition-and-subtraction/

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, say 2, you need to change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.



Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"
Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"
Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
Example 4:

Input: expression = "5/3+1/3"
Output: "2/1"


Constraints:

The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
The number of given fractions will be in the range [1, 10].
The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 98.11% of Python3 online submissions for Fraction Addition and Subtraction.
# Memory Usage: 14.3 MB, less than 30.19% of Python3 online submissions for Fraction Addition and Subtraction.
class Solution:
    def fractionAddition(self, expression: str) -> str:
        rn, rd = 0, 1
        i, m = 0, len(expression)

        def read_next(i0: int) -> (str, int):
            i = i0
            if expression[i] in "+-":
                i += 1
            while i < m and expression[i] not in "+-":
                i += 1
            return expression[i0:i], i

        while i < m:
            lex, i = read_next(i)
            sign = 1
            if lex[0] == '-':
                sign = -1
                lex = lex[1:]
            nom, denom = lex.split('/')
            nom, denom = sign*int(nom), int(denom)
            n = rn * denom + nom * rd
            d = denom * rd
            cd = math.gcd(n, d)
            rn, rd = n // cd, d // cd

        return str(rn) + "/" + str(rd)


tests = [
    ["-1/2+1/2", "0/1"],
    ["-1/2+1/2+1/3", "1/3"],
    ["1/3-1/2", "-1/6"],
    ["5/3+1/3", "2/1"]
]

run_functional_tests(Solution().fractionAddition, tests)
