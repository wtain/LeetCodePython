"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3651/
https://leetcode.com/problems/score-of-parentheses/

Given a balanced parentheses string S, compute the score of the string based on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.


Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6


Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""


# Runtime: 32 ms, faster than 56.58% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.4 MB, less than 12.96% of Python3 online submissions for Score of Parentheses.
# class Solution:
#     def scoreOfParentheses(self, S: str) -> int:
#         st = []
#         level = 0
#         for c in S:
#             if c == '(':
#                 st.append([0, level])
#                 level += 1
#             else:
#                 val = 0
#                 while st and st[-1][1] == level:
#                     val += st.pop()[0]
#                 if val == 0:
#                     val = 1
#                 else:
#                     val *= 2
#                 level -= 1
#                 st[-1][0] = val
#         while len(st) > 1:
#             val = st.pop(0)[0]
#             st[-1][0] += val
#         return st[-1][0]

# Runtime: 32 ms, faster than 56.58% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.1 MB, less than 73.28% of Python3 online submissions for Score of Parentheses.
# class Solution:
#     def scoreOfParentheses(self, S: str) -> int:
#         st = [0]
#         for c in S:
#             if c == '(':
#                 st.append(0)
#             else:
#                 v = st.pop()
#                 st[-1] += max(1, 2*v)
#         return st[-1]

# Runtime: 28 ms, faster than 83.50% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14.2 MB, less than 44.43% of Python3 online submissions for Score of Parentheses.
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result = balance = 0
        for i, a in enumerate(S):
            if a == '(':
                balance += 1
            else:
                balance -= 1
                if S[i-1] == '(':
                    result += 1 << balance
        return result


tests = [
    ("()", 1),
    ("(())", 2),
    ("()()", 2),
    ("(()(()))", 6)
]

for test in tests:
    result = Solution().scoreOfParentheses(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))