"""
https://leetcode.com/problems/find-the-closest-palindrome/description/?envType=daily-question&envId=2024-08-24

Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.



Example 1:

Input: n = "123"
Output: "121"
Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.


Constraints:

1 <= n.length <= 18
n consists of only digits.
n does not have leading zeros.
n is representing an integer in the range [1, 1018 - 1].
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#         i, j = 0, len(n)-1
#         result = 0
#         p1, p2 = 1, 1
#         low = 0
#         while i <= j:
#             result *= 10
#             result += int(n[i])
#             if i == j:
#                 break
#             p1 *= 10
#             p2 *= 10
#             low *= 10
#             low += int(n[i])
#             i += 1
#             j -= 1
#         result += low
#         return str(result)


# Runtime
# 44
# ms
# Beats
# 8.64%
# Analyze Complexity
# Memory
# 16.64
# MB
# Beats
# 28.21%
# https://leetcode.com/problems/find-the-closest-palindrome/editorial/?envType=daily-question&envId=2024-08-24
# class Solution:
#     def nearestPalindromic(self, n: str) -> str:
#
#         def half_to_palindrome(left, even):
#             res = left
#             if not even:
#                 left //= 10
#             while left > 0:
#                 res *= 10
#                 res += left % 10
#                 left //= 10
#             return res
#
#         len_n = len(n)
#         i = len_n // 2 - 1 if len_n % 2 == 0 else len_n // 2
#         first_half = int(n[:i+1])
#         possibilities = [
#             half_to_palindrome(first_half, len_n % 2 == 0),
#             half_to_palindrome(first_half+1, len_n % 2 == 0),
#             half_to_palindrome(first_half-1, len_n % 2 == 0),
#             10 ** (len_n-1)-1,
#             10 ** len_n + 1
#         ]
#         diff = math.inf
#         res = 0
#         nl = int(n)
#         for cand in possibilities:
#             if cand == nl:
#                 continue
#             if abs(cand - nl) < diff:
#                 diff = abs(cand - nl)
#                 res = cand
#             elif abs(cand - nl) == diff:
#                 res = min(res, cand)
#         return str(res)


# Runtime
# 50
# ms
# Beats
# 6.61%
# Analyze Complexity
# Memory
# 16.61
# MB
# Beats
# 28.21%
# https://leetcode.com/problems/find-the-closest-palindrome/editorial/?envType=daily-question&envId=2024-08-24
class Solution:
    def convert(self, num):
        s = str(num)
        n = len(s)
        l, r = (n-1)//2, n // 2
        s_list = list(s)
        while l >= 0:
            s_list[r] = s_list[l]
            r += 1
            l -= 1
        return int("".join(s_list))

    def next_palindrome(self, num):
        left, right = 0, num
        res = -math.inf
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin < num:
                res = palin
                left = mid + 1
            else:
                right = mid - 1
        return res

    def prev_palindrome(self, num):
        left, right = 0, int(1e18)
        res = -math.inf
        while left <= right:
            mid = (right - left) // 2 + left
            palin = self.convert(mid)
            if palin > num:
                res = palin
                right = mid - 1
            else:
                left = mid + 1
        return res

    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        a, b = self.next_palindrome(num), self.prev_palindrome(num)
        if abs(a - num) <= abs(b - num):
            return str(a)
        return str(b)


tests = [
    ["123", "121"],
    ["1", "0"],
]

run_functional_tests(Solution().nearestPalindromic, tests)
