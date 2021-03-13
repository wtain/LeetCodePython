"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/589/week-2-march-8th-march-14th/3667/
https://leetcode.com/problems/integer-to-roman/

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral.



Example 1:

Input: num = 3
Output: "III"
Example 2:

Input: num = 4
Output: "IV"
Example 3:

Input: num = 9
Output: "IX"
Example 4:

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.


Constraints:

1 <= num <= 3999
"""

# Runtime: 40 ms, faster than 95.29% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.1 MB, less than 86.07% of Python3 online submissions for Integer to Roman.
# class Solution:
#     def intToRoman(self, num: int) -> str:
#         result = ""
#         m = num // 1000
#         result += "M" * m
#         num %= 1000
#
#         if num >= 900:
#             num -= 900
#             result += "CM"
#
#         if num >= 500:
#             num -= 500
#             result += "D"
#
#         if num >= 400:
#             num -= 400
#             result += "CD"
#
#         c = num // 100
#         num %= 100
#         result += 'C' * c
#
#         if num >= 90:
#             num -= 90
#             result += "XC"
#
#         if num >= 50:
#             num -= 50
#             result += "L"
#
#         if num >= 40:
#             num -= 40
#             result += "XL"
#
#         x = num // 10
#         num %= 10
#         result += 'X' * x
#
#         if num >= 9:
#             num -= 9
#             result += "IX"
#
#         if num >= 5:
#             num -= 5
#             result += "V"
#
#         if num >= 4:
#             num -= 4
#             result += "IV"
#
#         result += 'I' * num
#
#         return result

# Runtime: 44 ms, faster than 87.75% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.3 MB, less than 31.02% of Python3 online submissions for Integer to Roman.
# class Solution:
#     def intToRoman(self, num: int) -> str:
#
#         signs = [
#             ('?', 'M'),
#             ('D', 'C'),
#             ('L', 'X'),
#             ('V', 'I')
#         ]
#
#         i = 0
#         divisor = 10 ** (len(signs) - 1)
#         result = ""
#
#         while num:
#             c9 = 9 * divisor
#             c5 = 5 * divisor
#             c4 = 4 * divisor
#             c1 = divisor
#
#             if num >= c9:
#                 num -= c9
#                 result += signs[i][1] + signs[i-1][1]
#
#             if num >= c5:
#                 num -= c5
#                 result += signs[i][0]
#
#             if num >= c4:
#                 num -= c4
#                 result += signs[i][1] + signs[i][0]
#
#             c = num // c1
#             num %= c1
#             result += signs[i][1] * c
#
#             divisor //= 10
#             i += 1
#
#         return result

# Runtime: 52 ms, faster than 56.95% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.3 MB, less than 31.02% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        signs = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"]
        ]
        result = ""
        for sign in signs:
            d = sign[0]
            c = sign[1]
            x = num // d
            if x:
                num -= x * d
                result += c * x

        return result


tests = [
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV")
]

for test in tests:
    result = Solution().intToRoman(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + result)