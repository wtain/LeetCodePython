"""
https://leetcode.com/problems/powx-n/description/

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).



Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25


Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if not n:
#             return 0.0
#         if x == 1.0:
#             return 1.0
#         if n < 0:
#             n = -n
#             x = -1.0 / x
#
#         d = 1 << 30
#         p = 30
#         while d > n:
#             d >>= 1
#             p -= 1
#         powers = [0.0] * 32
#         powers[0] = x
#         for i in range(1, p+1):
#             powers[i] = powers[i-1] * powers[i-1]
#
#         r = 1.0
#         while n:
#             dig = n // d
#             n %= d
#             if dig:
#                 r *= powers[p]
#
#             d >>= 1
#             p -= 1
#         return r


# Runtime
# Details
# 52ms
# Beats 26.00%of users with Python3
# Memory
# Details
# 16.38mb
# Beats 41.10%of users with Python3
# https://leetcode.com/problems/powx-n/editorial/
# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         if n == 0:
#             return 1.0
#         if n < 0:
#             return 1.0 / self.myPow(x, -n)
#         if n % 2 == 1:
#             return x * self.myPow(x * x, (n-1) // 2)
#         else:
#             return self.myPow(x * x, n // 2)


# Runtime
# Details
# 43ms
# Beats 80.40%of users with Python3
# Memory
# Details
# 16.38mb
# Beats 41.10%of users with Python3
# https://leetcode.com/problems/powx-n/editorial/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            n = -n
            x = 1.0 / x
        r = 1.0
        while n:
            if n % 2 == 1:
                r *= x
                n -= 1
            x *= x
            n //= 2
        return r


tests = [
    [2.00000, 10, 1024.00000],
    [2.10000, 3, 9.26100],
    [2.00000, -2, 0.25000],
    [34.00515, -3, 3e-05],
]

run_functional_tests(Solution().myPow, tests)
