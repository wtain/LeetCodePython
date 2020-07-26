"""
https://leetcode.com/problems/convert-a-number-to-hexadecimal/
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"
"""

"""
Runtime: 32 ms, faster than 57.10% of Python3 online submissions for Convert a Number to Hexadecimal.
Memory Usage: 13.8 MB, less than 53.33% of Python3 online submissions for Convert a Number to Hexadecimal.
"""
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = 2**32 + num
        result: str = ""
        digits = "0123456789abcdef"
        while num > 0:
            d = num % 16
            result += digits[d]
            num //= 16
        return result[::-1]


print(Solution().toHex(26))  # 1a
print(Solution().toHex(-1))  # ffffffff
print(Solution().toHex(0))  # 0
