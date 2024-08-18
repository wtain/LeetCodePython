"""
https://leetcode.com/problems/ugly-number-ii/description/?envType=daily-question&envId=2024-08-18

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.



Example 1:

Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.
Example 2:

Input: n = 1
Output: 1
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.


Constraints:

1 <= n <= 1690
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 89
# ms
# Beats
# 70.70%
# Analyze Complexity
# Memory
# 16.52
# MB
# Beats
# 71.48%
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        values = [1]
        i, j, k = 0, 0, 0
        while n > 1:
            n -= 1
            next = min(values[i]*2, values[j]*3, values[k]*5)
            if next == values[i]*2:
                i += 1
            if next == values[j]*3:
                j += 1
            if next == values[k]*5:
                k += 1
            values.append(next)
        return values[-1]


tests = [
    [10, 12],
    [1, 1],
]

run_functional_tests(Solution().nthUglyNumber, tests)
