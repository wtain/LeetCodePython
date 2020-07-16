"""
https://leetcode.com/problems/excel-sheet-column-number/
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701


Constraints:

1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
"""

"""
Runtime: 72 ms, faster than 7.07% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.5 MB, less than 99.81% of Python3 online submissions for Excel Sheet Column Number.
"""
class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0
        for c in s:
            result *= 26
            result += ord(c) - ord('A') + 1
        return result


print(Solution().titleToNumber("A"))  # 1
print(Solution().titleToNumber("AB"))  # 28
print(Solution().titleToNumber("ZY"))  # 701
