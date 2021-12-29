"""
https://leetcode.com/problems/nth-magical-number/

A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.



Example 1:

Input: n = 1, a = 2, b = 3
Output: 2
Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
Example 3:

Input: n = 5, a = 2, b = 4
Output: 10
Example 4:

Input: n = 3, a = 6, b = 4
Output: 8


Constraints:

1 <= n <= 109
2 <= a, b <= 4 * 104
"""
from math import gcd

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 76 ms, faster than 22.22% of Python3 online submissions for Nth Magical Number.
# Memory Usage: 14.3 MB, less than 31.31% of Python3 online submissions for Nth Magical Number.
# https://leetcode.com/problems/nth-magical-number/solution/
# class Solution:
#     def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
#         MOD = 10 ** 9 + 7
#         L = a // gcd(a, b) * b
#         M = L // a + L // b - 1
#         q, r = divmod(n, M)
#         if r == 0:
#             return q * L % MOD
#         heads = [a, b]
#         for _ in range(r-1):
#             if heads[0] <= heads[1]:
#                 heads[0] += a
#             else:
#                 heads[1] += b
#         return (q * L + min(heads)) % MOD


# Runtime: 20 ms, faster than 100.00% of Python3 online submissions for Nth Magical Number.
# Memory Usage: 14.2 MB, less than 59.60% of Python3 online submissions for Nth Magical Number.
# https://leetcode.com/problems/nth-magical-number/solution/
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10 ** 9 + 7
        L = a // gcd(a, b) * b

        def magic_less(x):
            return x // a + x // b - x // L

        lo = 0
        hi = n * min(a, b)
        while lo < hi:
            mi = (lo+hi) // 2
            if magic_less(mi) < n:
                lo = mi + 1
            else:
                hi = mi
        return lo % MOD


tests = [
    [1, 2, 3, 2],
    [4, 2, 3, 6],
    [5, 2, 4, 10],
    [3, 6, 4, 8]
]

run_functional_tests(Solution().nthMagicalNumber, tests)
