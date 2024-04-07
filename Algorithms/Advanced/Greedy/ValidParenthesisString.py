"""
https://leetcode.com/problems/valid-parenthesis-string/description/?envType=daily-question&envId=2024-04-07

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "(*)"
Output: true
Example 3:

Input: s = "(*))"
Output: true


Constraints:

1 <= s.length <= 100
s[i] is '(', ')' or '*'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 30
# ms
# Beats
# 87.55%
# of users with Python3
# Memory
# 16.45
# MB
# Beats
# 91.06%
# of users with Python3
class Solution:
    def checkValidString(self, s: str) -> bool:
        lo, hi = 0, 0
        n = len(s)
        for i in range(n):
            lo += 1 if s[i] == '(' else -1
            hi += 1 if s[i] != ')' else -1
            if hi < 0:
                return False
            lo = max(lo, 0)
        return lo == 0


tests = [
    ["()", True],
    ["(*)", True],
    ["(*))", True],
]

run_functional_tests(Solution().checkValidString, tests)
