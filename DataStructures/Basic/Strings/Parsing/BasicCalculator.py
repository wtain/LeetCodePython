"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3971/
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "1 + 1"
Output: 2
Example 2:

Input: s = " 2-1 + 2 "
Output: 3
Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23


Constraints:

1 <= s.length <= 3 * 105
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation.
'-' could be used as a unary operation but it has to be inside parentheses.
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 257 ms, faster than 5.77% of Python3 online submissions for Basic Calculator.
# Memory Usage: 16.8 MB, less than 11.19% of Python3 online submissions for Basic Calculator.
# class Solution:
#     def calculate(self, s: str) -> int:
#         n = len(s)
#         i = 0
#
#         def swallow_space():
#             nonlocal i, n
#             while i < n and str.isspace(s[i]):
#                 i += 1
#
#         def read_lexem() -> str:
#             nonlocal i, n
#             result = ""
#             swallow_space()
#             if i < n and not str.isdigit(s[i]):
#                 i += 1
#                 return s[i-1]
#             while i < n and str.isdigit(s[i]):
#                 result += s[i]
#                 i += 1
#             swallow_space()
#             return result
#
#         q = []
#         opstack = []
#         while i < n:
#             lex = read_lexem()
#             if not lex:
#                 break
#             if str.isdigit(lex[0]):
#                 q.append(int(lex))
#             elif lex == '(':
#                 opstack.append(lex)
#             elif lex == ')':
#                 while opstack and opstack[-1] != '(':
#                     q.append(opstack.pop())
#                 opstack.pop()
#             else:
#                 while opstack and opstack[-1] != '(':
#                     q.append(opstack.pop())
#                 opstack.append(lex)
#             # print(q)
#         while opstack:
#             q.append(opstack.pop())
#
#         st = []
#         for o in q:
#             if type(o) is int:
#                 st.append(o)
#             elif o == '+':
#                 o2 = st.pop()
#                 o1 = st.pop()
#                 st.append(o1 + o2)
#             elif o == '-':
#                 o2 = st.pop()
#                 o1 = st.pop() if st else 0
#                 st.append(o1 - o2)
#
#         return st[-1]


# Runtime: 99 ms, faster than 54.99% of Python3 online submissions for Basic Calculator.
# Memory Usage: 16 MB, less than 18.85% of Python3 online submissions for Basic Calculator.
# https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)

        def calc(i):
            num, st, sign = 0, [], "+"

            def update(op, v):
                if op == "+":
                    st.append(v)
                elif op == "-":
                    st.append(-v)

            while i < n:
                if s[i].isdigit():
                    num = 10 * num + int(s[i])
                elif s[i] in "+-":
                    update(sign, num)
                    num, sign = 0, s[i]
                elif s[i] == "(":
                    num, j = calc(i+1)
                    i = j - 1
                elif s[i] == ")":
                    update(sign, num)
                    return sum(st), i+1
                i += 1
            update(sign, num)
            return sum(st)
        return calc(0)


tests = [
    ["   (  3 ) ", 3],
    ["1 + 1", 2],
    [" 2-1 + 2 ", 3],
    ["(1+(4+5+2)-3)+(6+8)", 23],
    ["-(1+1)", -2]
]

run_functional_tests(Solution().calculate, tests)