"""
https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 60 ms, faster than 21.73% of Python3 online submissions for Sqrt(x).
Memory Usage: 13.7 MB, less than 90.91% of Python3 online submissions for Sqrt(x).
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        while l < r:
            m = l + (r - l) // 2
            m2 = m ** 2
            if m2 > x:
                r = m
            elif m2 < x:
                l = m+1
            else:
                return m

        if l**2 > x:
            l -= 1

        return l


tests = [
    [4, 2],
    [8, 2],
    [100, 10],
    [101, 10],
    [99, 9]
]

run_functional_tests(Solution().mySqrt, tests)
