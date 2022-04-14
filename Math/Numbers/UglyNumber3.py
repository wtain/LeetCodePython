"""
https://leetcode.com/problems/ugly-number-iii/

An ugly number is a positive integer that is divisible by a, b, or c.

Given four integers n, a, b, and c, return the nth ugly number.



Example 1:

Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.
Example 2:

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.
Example 3:

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.


Constraints:

1 <= n, a, b, c <= 109
1 <= a * b * c <= 1018
It is guaranteed that the result will be in range [1, 2 * 109].

Write a function f(k) to determine how many ugly numbers smaller than k. As f(k) is non-decreasing, try binary search.

Find all ugly numbers in [1, LCM(a, b, c)] (LCM is Least Common Multiple). Use inclusion-exclusion principle to expand the result.
"""
from math import gcd

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 31.35% of Python3 online submissions for Ugly Number III.
# Memory Usage: 13.9 MB, less than 91.75% of Python3 online submissions for Ugly Number III.
# https://leetcode.com/problems/ugly-number-iii/discuss/1873045/C%2B%2B-oror-Binary-Search-oror-100-faster-oror-Ugly-NUmber-ororor
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def number_of_ugly_numbers_less_than(k: int) -> int:
            nonlocal a, b, c
            lcm1, lcm2, lcm3 = a*b // gcd(a,b), c*b // gcd(c,b), a*c // gcd(a,c)
            lcm = lcm1 * c // gcd(lcm1, c)
            return k // a + k // b + k // c - k // lcm1 - k // lcm2 - k // lcm3 + k // lcm

        l, r = min(a, min(b,c)), 10**18
        while l <= r:
            m = l + (r-l) // 2
            cnt = number_of_ugly_numbers_less_than(m)
            if cnt == n:
                cnt1 = number_of_ugly_numbers_less_than(m-1)
                if cnt1 != n:
                    return m
                r = m-1
            elif cnt > n:
                r = m - 1
            else:
                l = m+1

        return -1


tests = [
    [1000000000, 2, 217983653, 336916467, 1999999984],
    [3,2,3,5,4],
    [4,2,3,4,6],
    [5,2,11,13,10]
]

run_functional_tests(Solution().nthUglyNumber, tests)
