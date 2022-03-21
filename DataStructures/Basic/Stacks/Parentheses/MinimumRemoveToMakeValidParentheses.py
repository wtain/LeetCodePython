"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3645/
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"


Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.
"""


# Runtime: 452 ms, faster than 13.86% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 16 MB, less than 55.49% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = ""
        b1 = 0
        for c in s:
            if c == '(':
                b1 += 1
            elif c == ')':
                b1 -= 1
            if b1 >= 0:
                result += c
            else:
                b1 += 1
        b2 = 0
        result, s = "", result
        for c in reversed(s):
            if c == ')':
                b2 += 1
            elif c == '(':
                b2 -= 1
            if b2 >= 0:
                result = c + result
            else:
                b2 += 1
        return result


tests = [
    ["lee(t(c)o)de)", "lee(t(c)o)de"],
    ["a)b(c)d", "ab(c)d"],
    ["))((", ""],
    ["(a(b(c)d)", "a(b(c)d)"]
]

run_functional_tests(Solution().minRemoveToMakeValid, tests)
