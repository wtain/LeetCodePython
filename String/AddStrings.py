"""
https://leetcode.com/problems/add-strings/
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

"""
Runtime: 44 ms, faster than 73.75% of Python3 online submissions for Add Strings.
Memory Usage: 13.7 MB, less than 90.81% of Python3 online submissions for Add Strings.
"""
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = ""
        n1 = len(num1)
        n2 = len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        for i in range(max(n1, n2)):
            d1 = d2 = 0
            if i < n1:
                d1 = ord(num1[i]) - ord('0')
            if i < n2:
                d2 = ord(num2[i]) - ord('0')
            s = d1 + d2 + carry
            carry = s // 10
            s %= 10
            result += chr(ord('0') + s)
        if carry > 0:
            result += '1'
        return result[::-1]


print(Solution().addStrings("111", "99"))  # 210
print(Solution().addStrings("1", "9"))  # 10
