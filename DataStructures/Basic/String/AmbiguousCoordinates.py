"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/599/week-2-may-8th-may-14th/3741/
https://leetcode.com/problems/ambiguous-coordinates/

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]
Example 2:
Input: s = "(00011)"
Output:  ["(0.001, 1)", "(0, 0.011)"]
Explanation:
0.0, 00, 0001 or 00.01 are not allowed.
Example 3:
Input: s = "(0123)"
Output: ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]
Example 4:
Input: s = "(100)"
Output: [(10, 0)]
Explanation:
1.0 is not allowed.


Note:

4 <= s.length <= 12.
s[0] = "(", s[s.length - 1] = ")", and the other elements in s are digits.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 33.33% of Python3 online submissions for Ambiguous Coordinates.
# Memory Usage: 14.1 MB, less than 98.33% of Python3 online submissions for Ambiguous Coordinates.
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:

        def possibilities(a: str) -> List[str]:

            def all_zeros(x: str) -> bool:
                for c in x:
                    if c != '0':
                        return False
                return True

            m = len(a)
            res = []
            if a[0] != '0' or len(a) == 1:
                res.append(a)
            for j in range(1, m):
                lo = a[:j]
                if lo[0] == '0' and len(lo) > 1:
                    continue
                hi = a[j:]
                if hi[-1] == '0':
                    continue
                if all_zeros(hi):
                    continue
                v = f"{lo}.{hi}"
                if v != "0.0":
                    res.append(v)
            return res

        s1 = s[1:-1]
        n = len(s1)
        result = []
        for i in range(1, n):
            a = s1[:i]
            b = s1[i:]
            for ap in possibilities(a):
                for bp in possibilities(b):
                    result.append(f"({ap}, {bp})")
        return result


tests = [
    ["(0010)", ["(0.01, 0)"]],

    ["(123)", ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]],
    ["(00011)", ["(0.001, 1)", "(0, 0.011)"]],
    ["(0123)", ["(0, 123)", "(0, 12.3)", "(0, 1.23)", "(0.1, 23)", "(0.1, 2.3)", "(0.12, 3)"]],
    ["(100)", ["(10, 0)"]]
]

def customCheck(test, result) -> bool:
    return set(test[-1]) == set(result)

run_functional_tests(Solution().ambiguousCoordinates, tests, custom_check=customCheck)