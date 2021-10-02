"""
https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""


"""
0 -> A
1 -> B
....
25 -> Z
"""

"""
Runtime: 52 ms, faster than 7.95% of Python3 online submissions for Excel Sheet Column Title.
Memory Usage: 14 MB, less than 16.67% of Python3 online submissions for Excel Sheet Column Title.
"""
class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        n -= 1
        while n >= 0:
            i = n % 26
            result = chr(ord('A') + i) + result
            n //= 26
            n -= 1
        return result


print(Solution().convertToTitle(1))  # A
print(Solution().convertToTitle(28))  # AB
print(Solution().convertToTitle(701))  # ZY
