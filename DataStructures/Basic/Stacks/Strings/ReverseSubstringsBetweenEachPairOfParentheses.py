"""
https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/description/?envType=daily-question&envId=2024-07-11


Topics
Companies
Hint
You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.



Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.


Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         result = ""
#         st = []
#         inside = False
#         for c in s:
#             if inside:
#                 if c == ")":
#                     inside = False
#                     result += "".join(reversed(st))
#                     st = []
#                 else:
#                     st.append(c)
#             else:
#                 if c == "(":
#                     inside = True
#                 else:
#                     result += c
#         return result

# Runtime
# 42
# ms
# Beats
# 16.58%
# Analyze Complexity
# Memory
# 16.52
# MB
# Beats
# 40.89%
# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         st = [""]
#         for c in s:
#             if c == "(":
#                 st.append("")
#             elif c == ")":
#                 curr = st.pop()[::-1]
#                 st[-1] += curr
#             else:
#                 st[-1] += c
#         return st[-1]


# Runtime
# 30
# ms
# Beats
# 91.13%
# Analyze Complexity
# Memory
# 16.47
# MB
# Beats
# 81.94%
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/editorial/?envType=daily-question&envId=2024-07-11
class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        open_p_idx = []
        pair = [0] * n
        for i in range(n):
            if s[i] == '(':
                open_p_idx.append(i)
            if s[i] == ')':
                j = open_p_idx.pop()
                pair[i] = j
                pair[j] = i

        result = []
        curr_idx = 0
        direction = 1
        while curr_idx < n:
            if s[curr_idx] == '(' or s[curr_idx] == ")":
                curr_idx = pair[curr_idx]
                direction = -direction
            else:
                result.append(s[curr_idx])
            curr_idx += direction
        return "".join(result)


tests = [
    ["(abcd)", "dcba"],
    ["(u(love)i)", "iloveu"],
    ["(ed(et(oc))el)", "leetcode"],
]

run_functional_tests(Solution().reverseParentheses, tests)
