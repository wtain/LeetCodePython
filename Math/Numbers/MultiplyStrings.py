"""
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
from Common.ObjectTestingUtils import run_functional_tests



# Runtime: 188 ms, faster than 25.41% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.2 MB, less than 82.06% of Python3 online submissions for Multiply Strings.
# class Solution:
#     def multiply(self, num1: str, num2: str) -> str:
#         n1, n2 = len(num1), len(num2)
#         result = [0] * (n1 + n2 + 1)
#         for i in range(n1):
#             i1 = n1 - 1 - i
#             carry = 0
#             result1 = [0] * (n2+1)
#             d1 = int(num1[i1])
#             for j in range(n2):
#                 j1 = n2 - 1 - j
#                 d2 = int(num2[j1])
#                 dr = carry + d1*d2
#                 carry = dr // 10
#                 dr %= 10
#                 result1[j1+1] = dr
#             result1[0] = carry
#             carry = 0
#             for j in range(n2+1):
#                 j1, i2 = n2 - j, n1+n2 - j - i
#                 d1, d2 = result[i2], result1[j1]
#                 dr = carry + d1 + d2
#                 carry = dr // 10
#                 dr %= 10
#                 result[i2] = dr
#             result[0] += carry
#         start = 0
#         while start < n1+n2+1 and result[start] == 0:
#             start += 1
#         if start == len(result):
#             return "0"
#         return "".join(str(c) for c in result[start:])


# Runtime: 144 ms, faster than 42.64% of Python3 online submissions for Multiply Strings.
# Memory Usage: 14.4 MB, less than 29.49% of Python3 online submissions for Multiply Strings.
# https://leetcode.com/problems/multiply-strings/solution/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = len(num1), len(num2)
        result = [0] * (n1 + n2 + 1)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(n1):
            for j in range(n2):
                k = i + j
                carry = result[k]
                res = int(num1[i]) * int(num2[j]) + carry
                result[k] = res % 10
                result[k+1] += res // 10
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        return "".join(str(c) for c in result[::-1])


tests = [
    ["2", "3", "6"],
    ["123", "456", "56088"],
    ["0", "0", "0"]
]

run_functional_tests(Solution().multiply, tests)
