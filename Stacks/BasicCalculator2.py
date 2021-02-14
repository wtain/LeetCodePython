"""
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""


# Runtime: 216 ms, faster than 6.88% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.5 MB, less than 86.21% of Python3 online submissions for Basic Calculator II.
# class Solution:
#     def calculate(self, s: str) -> int:
#
#         def is_operation(c: str) -> bool:
#             return c in ['+', '-', '*', '/']
#
#         def get_lexem(s: str, i: int) -> (str, int):
#             n = len(s)
#             while i < n and str.isspace(s[i]):
#                 i += 1
#             if i < n and is_operation(s[i]):
#                 return s[i], i + 1
#             lexem = ""
#             while i < n and str.isdigit(s[i]):
#                 lexem += s[i]
#                 i += 1
#             return lexem, i
#
#         opstack = []
#         vals = []
#
#         def perform_add_sub():
#             nonlocal opstack, vals
#             while opstack and opstack[-1] in ['+', '-']:
#                 op = opstack.pop()
#                 v2 = vals.pop()
#                 v1 = vals.pop()
#                 if op == '+':
#                     vals.append(v1 + v2)
#                 else:
#                     vals.append(v1 - v2)
#
#         i = 0
#         n = len(s)
#         while i < n:
#             lexem, i = get_lexem(s, i)
#             if not lexem:
#                 break
#             if is_operation(lexem):
#                 if lexem in ['+', '-']:
#                     perform_add_sub()
#                 opstack.append(lexem)
#             else:
#                 val = int(lexem)
#                 while opstack and opstack[-1] in ['*', '/']:
#                     op = opstack.pop()
#                     vl = vals.pop()
#                     if op == '*':
#                         val = vl * val
#                     else:
#                         val = vl // val
#                 vals.append(val)
#         perform_add_sub()
#         # print(vals)
#         return int(vals[0])

# int(-3/2)
# -1
# -3//2
# -2

# Runtime: 132 ms, faster than 22.52% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.7 MB, less than 66.99% of Python3 online submissions for Basic Calculator II.
# class Solution:
#     def calculate(self, s: str) -> int:
#         n = len(s)
#         result = 0
#         stack = []
#         i = 0
#         current = 0
#         operation = '+'
#         while i < n:
#             if str.isdigit(s[i]):
#                 current = 10 * current + (ord(s[i]) - ord('0'))
#             if i == n-1 or not str.isdigit(s[i]) and not str.isspace(s[i]):
#                 op = s[i]
#                 if operation == '-':
#                     stack.append(-current)
#                 elif operation == '+':
#                     stack.append(current)
#                 elif operation == '*':
#                     v1 = stack.pop()
#                     stack.append(v1 * current)
#                 else:
#                     v1 = stack.pop()
#                     stack.append(int(v1 / current))
#                 operation = op
#                 current = 0
#             i += 1
#         while stack:
#             result += stack.pop()
#         return result

# Runtime: 140 ms, faster than 19.24% of Python3 online submissions for Basic Calculator II.
# Memory Usage: 15.3 MB, less than 94.19% of Python3 online submissions for Basic Calculator II.
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        result = 0
        i = 0
        current = 0
        last = 0
        operation = '+'
        while i < n:
            if str.isdigit(s[i]):
                current = 10 * current + (ord(s[i]) - ord('0'))
            if i == n-1 or not str.isdigit(s[i]) and not str.isspace(s[i]):
                op = s[i]
                if operation == '-':
                    result += last
                    last = -current
                elif operation == '+':
                    result += last
                    last = current
                elif operation == '*':
                    last = last * current
                else:
                    last = int(last / current)
                operation = op
                current = 0
            i += 1
        result += last
        return result


tests = [
    ("14-3/2", 13),

    ("3+2*2", 7),
    (" 3/2 ", 1),
    (" 3+5 / 2 ", 5)
]

for test in tests:
    result = Solution().calculate(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))