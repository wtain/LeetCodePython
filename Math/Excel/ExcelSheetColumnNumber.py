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
from functools import reduce
from itertools import accumulate

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 72 ms, faster than 7.07% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.5 MB, less than 99.81% of Python3 online submissions for Excel Sheet Column Number.
Runtime: 45 ms, faster than 52.76% of Python3 online submissions for Excel Sheet Column Number.
Memory Usage: 13.9 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
"""
# class Solution:
#     def titleToNumber(self, s: str) -> int:
#         result = 0
#         for c in s:
#             result *= 26
#             result += ord(c) - ord('A') + 1
#         return result


# Runtime: 45 ms, faster than 52.76% of Python3 online submissions for Excel Sheet Column Number.
# Memory Usage: 13.8 MB, less than 83.72% of Python3 online submissions for Excel Sheet Column Number.
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return reduce(lambda r, c: 26*r+ord(c) - ord('A') + 1, columnTitle, 0)


tests = [
    ["A", 1],
    ["AB", 28],
    ["ZY", 701]
]

run_functional_tests(Solution().titleToNumber, tests)
