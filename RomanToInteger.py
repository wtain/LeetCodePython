"""
https://leetcode.com/problems/roman-to-integer/
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""

"""
Runtime: 64 ms, faster than 25.24% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.1 MB, less than 5.01% of Python3 online submissions for Roman to Integer.
"""
class Solution:

    def readGroup(self, s: str, i, n: int) -> (chr, int, int):
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        return s[i], j-i, j

    def romanToInt(self, s: str) -> int:
        result = 0
        n = len(s)
        i = 0

        while i < n:
            ch, cnt, i = self.readGroup(s, i, n)
            if ch == 'M':
                result += 1000 * cnt
            elif ch == 'D':
                result += 500
            elif ch == 'C':
                if i < n and s[i] == 'M':
                    result += 1000 - 100 * cnt
                    i += 1
                elif i < n and s[i] == 'D':
                    result += 500 - 100 * cnt
                    i += 1
                else:
                    result += 100 * cnt
            elif ch == 'L':
                result += 50
            elif ch == 'X':
                if i < n and s[i] == 'C':
                    result += 100 - 10 * cnt
                    i += 1
                elif i < n and s[i] == 'L':
                    result += 50 - 10 * cnt
                    i += 1
                else:
                    result += 10 * cnt
            elif ch == 'V':
                result += 5
            elif ch == 'I':
                if i < n and s[i] == 'X':
                    result += 10 - cnt
                    i += 1
                elif i < n and s[i] == 'V':
                    result += 5 - cnt
                    i += 1
                else:
                    result += cnt

        return result


print(Solution().romanToInt("III"))  # 3
print(Solution().romanToInt("IV"))  # 4
print(Solution().romanToInt("IX"))  # 9
print(Solution().romanToInt("LVIII"))  # 58
print(Solution().romanToInt("MCMXCIV"))  # 1994