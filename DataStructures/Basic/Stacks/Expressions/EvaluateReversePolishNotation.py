"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3755/
https://leetcode.com/problems/evaluate-reverse-polish-notation/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.



Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 68 ms, faster than 48.89% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.3 MB, less than 96.45% of Python3 online submissions for Evaluate Reverse Polish Notation.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                v2 = st.pop()
                v1 = st.pop()
                if token == '+':
                    st.append(v1 + v2)
                elif token == '-':
                    st.append(v1 - v2)
                elif token == '*':
                    st.append(v1 * v2)
                elif token == '/':
                    st.append(int(v1 / v2))
            else:
                st.append(int(token))

        return st[0] if st else 0


tests = [
    # [["2","1","+","3","*"], 9],
    # [["4","13","5","/","+"], 6],
    [["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22]
]

run_functional_tests(Solution().evalRPN, tests)