
"""
https://leetcode.com/problems/valid-parentheses/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 48 ms, faster than 17.45% of Python3 online submissions for Valid Parentheses.
Memory Usage: 14.2 MB, less than 5.17% of Python3 online submissions for Valid Parentheses.
"""
# class Solution:
#     def isValid(self, s: str) -> bool:
#         st = []
#         for c in s:
#             if c == '(':
#                 r = [c, 1]
#                 if len(st) == 0 or st[len(st)-1][0] != '(':
#                     st.append(r)
#                 else:
#                     st[len(st) - 1][1] += 1
#             elif c == '[':
#                 r = [c, 1]
#                 if len(st) == 0 or st[len(st)-1][0] != '[':
#                     st.append(r)
#                 else:
#                     st[len(st) - 1][1] += 1
#             elif c == '{':
#                 r = [c, 1]
#                 if len(st) == 0 or st[len(st)-1][0] != '{':
#                     st.append(r)
#                 else:
#                     st[len(st) - 1][1] += 1
#             elif c == '}':
#                 if len(st) == 0 or st[len(st)-1][0] != '{':
#                     return False
#                 else:
#                     st[len(st) - 1][1] -= 1
#             elif c == ']':
#                 if len(st) == 0 or st[len(st)-1][0] != '[':
#                     return False
#                 else:
#                     st[len(st) - 1][1] -= 1
#             elif c == ')':
#                 if len(st) == 0 or st[len(st)-1][0] != '(':
#                     return False
#                 else:
#                     st[len(st) - 1][1] -= 1
#             if len(st) > 0 and st[len(st) - 1][1] == 0:
#                 st.pop()
#         return len(st) == 0


# Runtime: 36 ms, faster than 23.34% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.6 MB, less than 8.35% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:

        class CompressedStack:

            def __init__(self):
                self.st = []

            def push(self, c: chr):
                if len(self.st) == 0 or self.st[-1][0] != c:
                    self.st.append([c, 1])
                else:
                    self.st[-1][1] += 1

            def pop(self) -> chr:
                c = self.st[-1][0]
                self.st[-1][1] -= 1
                if self.st[-1][1] == 0:
                    self.st.pop()
                return c

            def isEmpty(self) -> bool:
                return len(self.st) == 0

        st = CompressedStack()
        braces = {"}": "{",
                  "]": "[",
                  ")": "("}

        def isOpeningBracket(ch: chr) -> bool:
            return ch in braces.values()

        for c in s:
            if isOpeningBracket(c):
                st.push(c)
            elif st.isEmpty():
                return False
            else:
                br = braces[c]
                if st.pop() != br:
                    return False

        return st.isEmpty()


tests = [
    ["[", False],
    ["()", True],
    ["()[]{}", True],
    ["(]", False],
    ["([)]", False],
    ["{[]}", True],
]

run_functional_tests(Solution().isValid, tests)
