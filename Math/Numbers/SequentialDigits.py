"""
https://leetcode.com/problems/sequential-digits/

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.



Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 96.83% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.4 MB, less than 22.22% of Python3 online submissions for Sequential Digits.
# class Solution:
#     def sequentialDigits(self, low: int, high: int) -> List[int]:
#
#         # def get_digits(value: int) -> List[int]:
#         #     digits = []
#         #     while value:
#         #         digit = value % 10
#         #         value //= 10
#         #         digits = [digit] + digits
#         #     return digits
#         #
#         # d1, d2 = get_digits(low), get_digits(high)
#         # while len(d1) < len(d2):
#         #     d1 = [0] + d1
#         #
#         # n = len(d1)
#
#         def get_digit_count(v: int) -> int:
#             n = 0
#             while v:
#                 n += 1
#                 v //= 10
#             return n
#
#         n = get_digit_count(high)
#
#         result = []
#         seen = set()
#
#         def search(current: int, pos: int, prev: int):
#             nonlocal result, n
#             if pos == n:
#                 if low <= current <= high and current not in seen:
#                     result.append(current)
#                     seen.add(current)
#             else:
#                 base = 10 * current
#                 if prev <= 0:
#                     for digit in range(prev+1, 10):
#                         search(base + digit, pos+1, digit)
#                 elif prev < 9:
#                     digit = prev + 1
#                     search(base + digit, pos + 1, digit)
#
#                 if prev == -1:
#                     search(0, pos + 1, -1)
#
#         search(0, 0, -1)
#
#         return sorted(result)


# Runtime: 24 ms, faster than 96.83% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.4 MB, less than 22.22% of Python3 online submissions for Sequential Digits.
# https://leetcode.com/problems/sequential-digits/discuss/1712841/C%2B%2B-0ms-stored-all-possible-sequence-and-checked-them-constant-complexity
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []

        def get_digit_count(v: int) -> int:
            n = 0
            while v:
                n += 1
                v //= 10
            return n

        n1, n2 = get_digit_count(low), get_digit_count(high)
        seqDigits = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9], [12, 23, 34, 45, 56, 67, 78, 89],
            [123, 234, 345, 456, 567, 678, 789], [1234, 2345, 3456, 4567, 5678, 6789],
            [12345, 23456, 34567, 45678, 56789], [123456, 234567, 345678, 456789],
            [1234567, 2345678, 3456789], [12345678, 23456789], [123456789]
        ]

        for i in range(max(n1-1, 0), min(n2, 9)):
            for j in range(0, len(seqDigits[i])):
                v = seqDigits[i][j]
                if low <= v <= high:
                    result.append(v)

        return result


tests = [
    [100, 300, [123,234]],
    [1000, 13000, [1234,2345,3456,4567,5678,6789,12345]],
    [10, 1000000000, [12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789]]
]


run_functional_tests(Solution().sequentialDigits, tests)
