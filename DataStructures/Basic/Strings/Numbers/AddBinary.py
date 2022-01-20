"""
https://leetcode.com/problems/add-binary/
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 56 ms, faster than 12.22% of Python3 online submissions for Add Binary.
Memory Usage: 13.8 MB, less than 67.84% of Python3 online submissions for Add Binary.
"""
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         result = ""
#
#         n1 = len(a)
#         n2 = len(b)
#
#         i1 = n1-1
#         i2 = n2-1
#         carry = 0
#
#         while carry > 0 or i1 >= 0 or i2 >= 0:
#             d1 = 0
#             if i1 >= 0:
#                 d1 = ord(a[i1]) - ord('0')
#                 i1 -= 1
#
#             d2 = 0
#             if i2 >= 0:
#                 d2 = ord(b[i2]) - ord('0')
#                 i2 -= 1
#
#             res = d1 + d2 + carry
#
#             carry = res // 2
#             res %= 2
#             result += chr(ord('0') + res)
#
#         return result[::-1]


# Runtime: 70 ms, faster than 5.46% of Python3 online submissions for Add Binary.
# Memory Usage: 14.3 MB, less than 22.51% of Python3 online submissions for Add Binary.
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        a, b = int(a), int(b)
        carry = 0
        while carry or a or b:
            a1, b1 = a % 10, b % 10
            r = a1 + b1 + carry
            carry = r > 1
            r %= 2
            a //= 10
            b //= 10
            result += str(r)
        return result[::-1] if result else "0"


tests = [
    ["0", "0", "0"],
    ["11", "1", "100"],
    ["1010", "1011", "10101"]
]

run_functional_tests(Solution().addBinary, tests)
