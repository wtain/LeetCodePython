"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3826/
https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/

Given a positive integer n, return the number of the integers in the range [0, n] whose binary representations do not contain consecutive ones.



Example 1:

Input: n = 5
Output: 5
Explanation:
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 satisfy the rule.
Example 2:

Input: n = 1
Output: 2
Example 3:

Input: n = 2
Output: 3


Constraints:

1 <= n <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def findIntegers(self, n: int) -> int:
#
#         def has_conseq_ones(i: int) -> bool:
#             was1 = False
#             while i:
#                 dig = i % 2
#                 if dig and was1:
#                     return True
#                 was1 = dig == 1
#                 i //= 2
#             return False
#
#         def naive(a: int, b: int) -> int:
#             result = 0
#             for i in range(a, b+1):
#                 if has_conseq_ones(i):
#                     continue
#                 result += 1
#             return result
#
#         # n0 = 1
#         # n1 = 0
#
#         p = 1
#         while 2 ** (p+1) < n + 2:
#             p += 1
#
#         n0 = 1
#         n1 = 0
#         n1_prev = 1
#         cnt = 1
#         for k in range(1, p+1):
#             n0_new = cnt
#             n1_new = n1 + n1_prev
#             cnt = n0_new + n1_new
#             n1_prev, n1, n0 = n1, n1_new, n0_new
#
#         # cnt_less_than_2k(n) + cnt(2^k..n)
#
#         return cnt + naive(2**p, n)

# class Solution:
#     def findIntegers(self, n: int) -> int:
#
#         if n == 0:
#             return 1
#
#         def has_conseq_ones(i: int) -> bool:
#             was1 = False
#             while i:
#                 dig = i % 2
#                 if dig and was1:
#                     return True
#                 was1 = dig == 1
#                 i //= 2
#             return False
#
#         def naive(a: int, b: int) -> int:
#             return sum(1 for i in range(a, b+1) if not has_conseq_ones(i))
#
#         p = 1
#         while 2 ** (p+1) < n + 2:
#             p += 1
#
#         n1 = 0
#         n1_prev = 1
#         cnt = 1
#         for k in range(1, p+1):
#             n0_new = cnt
#             n1_new = n1 + n1_prev
#             cnt = n0_new + n1_new
#             n1_prev, n1, n0 = n1, n1_new, n0_new
#         return cnt + naive(2**p, n)

# WRONG
# class Solution:
#     def findIntegers(self, n: int) -> int:
#
#         def impl(n: int, first_zero: bool) -> int:
#
#             if n == 0:
#                 return 1
#
#             p = 1
#             while 2 ** (p + 1) < n + 2:
#                 p += 1
#
#             n1 = 0
#             n1_prev = 1
#             cnt = 1
#             for k in range(1, p + 1):
#                 n0_new = cnt
#                 n1_new = n1 + n1_prev
#                 cnt = n0_new + n1_new
#                 n1_prev, n1, n0 = n1, n1_new, n0_new
#             if not first_zero:
#                 cnt -= n1
#             if n >= 2 ** p:
#                 n1 = n - 2 ** p
#                 # if n1 >= 2 ** (p-1):
#                 #     n1 = n1 - 2 ** (p-1)
#                 cnt += impl(n1, False)
#             return cnt
#         return impl(n, True)


# https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/solution/
# Runtime: 32 ms, faster than 84.62% of Python3 online submissions for Non-negative Integers without Consecutive Ones.
# Memory Usage: 14.2 MB, less than 67.95% of Python3 online submissions for Non-negative Integers without Consecutive Ones.
class Solution:
    def findIntegers(self, n: int) -> int:
        f = [0] * 32
        f[0] = 1
        f[1] = 2
        for i in range(2, 32):
            f[i] = f[i-1] + f[i-2]
        i, s, prev_bit = 30, 0, 0
        while i >= 0:
            if n & (1 << i) != 0:
                s += f[i]
                if prev_bit == 1:
                    s -= 1
                    break
                prev_bit = 1
            else:
                prev_bit = 0
            i -= 1
        return s + 1


tests = [
    [6, 5],
    [70, 26],

    [100000, 4181],
    [1000000, 17711],
    [10000000, 103682],
    [67, 24],
    [68, 25],
    [69, 26],
    [70, 26],
    [90, 34],
    [96, 34],
    [100, 34],
    [66, 24],
    [65, 23],
    [64, 22],
    [63, 21],
    [10, 8],
    [5, 5],
    [1, 2],
    [2, 3]
]

run_functional_tests(Solution().findIntegers, tests)