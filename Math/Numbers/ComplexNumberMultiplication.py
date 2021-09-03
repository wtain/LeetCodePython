"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/616/week-4-august-22nd-august-28th/3917/
https://leetcode.com/problems/complex-number-multiplication/

A complex number can be represented as a string on the form "real+imaginaryi" where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the complex number that represents their multiplications.



Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.


Constraints:

num1 and num2 are valid complex numbers.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 92.57% of Python3 online submissions for Complex Number Multiplication.
# Memory Usage: 14.3 MB, less than 52.79% of Python3 online submissions for Complex Number Multiplication.
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:

        def complex(s: str) -> (int, int):

            def parse_int(s: str, i: int) -> (int, int):
                result = 0
                sign = 1
                if s[i] == '-':
                    sign = -1
                    i += 1
                elif s[i] == '+':
                    i += 1
                while str.isdigit(s[i]):
                    result = 10 * result + int(s[i])
                    i += 1
                return sign * result, i

            i = 0
            a, i = parse_int(s, i)
            i += 1
            b, i = parse_int(s, i)
            return a, b

        a1, b1 = complex(num1)
        a2, b2 = complex(num2)

        real = a1 * a2 - b1 * b2
        im = b1 * a2 + a1 * b2

        return str(real) + "+" + str(im) + "i"


tests = [
    ["1+1i", "1+1i", "0+2i"],
    ["1+-1i", "1+-1i", "0+-2i"]
]

run_functional_tests(Solution().complexNumberMultiply, tests)