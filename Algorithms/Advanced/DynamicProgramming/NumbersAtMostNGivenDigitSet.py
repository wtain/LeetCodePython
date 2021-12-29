"""
https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

Given an array of digits which is sorted in non-decreasing order. You can write numbers using each digits[i] as many times as we want. For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less than or equal to a given integer n.



Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation:
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation:
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1


Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
digits is sorted in non-decreasing order.
1 <= n <= 109
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 62.96% of Python3 online submissions for Numbers At Most N Given Digit Set.
# Memory Usage: 14.3 MB, less than 78.70% of Python3 online submissions for Numbers At Most N Given Digit Set.
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/
# class Solution:
#     def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
#         s = str(n)
#         k = len(s)
#         dp = [0] * k + [1]
#         for i in range(k-1, -1, -1):
#             for d in digits:
#                 if d < s[i]:
#                     dp[i] += len(digits) ** (k-i-1)
#                 elif d == s[i]:
#                     dp[i] += dp[i+1]
#
#         return dp[0] + sum(len(digits) ** i for i in range(1, k))


# Runtime: 20 ms, faster than 99.07% of Python3 online submissions for Numbers At Most N Given Digit Set.
# Memory Usage: 14.2 MB, less than 91.67% of Python3 online submissions for Numbers At Most N Given Digit Set.
# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        b = len(digits)
        s = str(n)
        k = len(s)
        A = []

        for c in s:
            if c in digits:
                A.append(digits.index(c) + 1)
            else:
                i = bisect.bisect(digits, c)
                A.append(i)
                if i == 0:
                    for j in range(len(A)-1, 0, -1):
                        if A[j]:
                            break
                        A[j] += b
                        A[j-1] -= 1
                A.extend([b] * (k - len(A)))
                break
        result = 0
        for x in A:
            result = result * b + x
        return result


tests = [
    [["1","3","5","7"], 100, 20],
    [["1","4","9"], 1000000000, 29523],
    [["7"], 8, 1]
]

run_functional_tests(Solution().atMostNGivenDigitSet, tests)
