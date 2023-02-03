"""
https://leetcode.com/problems/zigzag-conversion/description/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"


Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""
from functools import reduce
from itertools import accumulate, chain

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 61 ms
# Beats
# 72.7%
# Memory
# 14 MB
# Beats
# 48.57%
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if not numRows:
#             return s
#
#         n = len(s)
#         j, dj = 0, 1
#         v = [""] * numRows
#         for i in range(n):
#             v[j] += s[i]
#             if j + dj == numRows:
#                 dj = -dj
#             if j + dj == -1:
#                 dj = 1
#             if numRows > 1:
#                 j += dj
#         return reduce(lambda r, s: (r+s), v, "")


# Runtime
# 97 ms
# Beats
# 38.64%
# Memory
# 13.8 MB
# Beats
# 94.57%
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows <= 1:
#             return s
#         n = len(s)
#         cycle_length = numRows + (numRows-2)
#         result = ""
#         for remainder in range(numRows):
#             if remainder in [0, numRows-1]:
#                 result += s[remainder::cycle_length]
#             else:
#                 result += "".join(s[i] for i in sorted(chain(range(remainder,n,cycle_length),
#                                                              range(cycle_length-remainder,n,cycle_length))))
#         return result


# Runtime
# 100 ms
# Beats
# 37.61%
# Memory
# 13.9 MB
# Beats
# 94.57%
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        n = len(s)
        cycle_length = numRows + (numRows-2)
        result = ""
        for remainder in range(numRows):
            if remainder in [0, numRows-1]:
                result += s[remainder::cycle_length]
            else:
                result += "".join(s[i]+s[j] if j < n else s[i]
                                  for i, j in zip(range(remainder,n,cycle_length),
                                                  range(cycle_length-remainder,n+cycle_length,cycle_length)))
        return result


tests = [
    ["PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"],
    ["PAYPALISHIRING", 4, "PINALSIGYAHRPI"],
    ["A", 1, "A"],
]

run_functional_tests(Solution().convert, tests)
