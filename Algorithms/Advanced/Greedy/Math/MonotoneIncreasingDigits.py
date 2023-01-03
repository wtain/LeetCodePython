"""
https://leetcode.com/problems/monotone-increasing-digits/description/

An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.



Example 1:

Input: n = 10
Output: 9
Example 2:

Input: n = 1234
Output: 1234
Example 3:

Input: n = 332
Output: 299


Constraints:

0 <= n <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# 1. Split into digits
# 2. Go right to left, considering pairs
# 3. In case of inversion => right change to 9, previous decrement, fill all previous with 9s
# 4. If did not become 0, continue with the next one with step 3
#
#
#
# digits = split_into_digits(n)
#
# for high, low in pairs(digits):
#   if high == 0:
#     break
#   if low < high:
#     decrement low
#     high = 9
#
# return build_number(digits)


# Runtime
# 51 ms
# Beats
# 54.26%
# Memory
# 13.9 MB
# Beats
# 69.72%
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # Initialize result with 0, nines up to current digit with 9 and current power of ten to 1
        result, nines, power = 0, 9, 1
        while n:                             # Iterating the number from low digits, checking pairs
            digit_low = n % 10               # Lowest digit is modulo of 10
            n //= 10                         # Shift the number
            digit_high = n % 10              # Higher digit is modulo of 10 now
            if digit_low < digit_high:       # If we have found an inversion
                result = nines               # Set all digits up to the current one to 9s
                n -= 1                       # Decrement the remaining part of the number (which starts with the current higher digit)
            else:
                result += digit_low * power  # Otherwise add lowe digit to the number
            power *= 10                      # Shifting the power
            nines = 10 * nines + 9           # Adding another 9 not nines

        return result                        # Return the result


test = [
    [100, 99],
    [10, 9],
    [1234, 1234],
    [332, 299]
]

run_functional_tests(Solution().monotoneIncreasingDigits, test)
