"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3695/
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.



Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         # n = len(s)
#         # dp = [0] * n
#         max_len = 0
#         curr_len = 0
#         balance = 0
#         for si in s:
#             if si == '(':
#                 balance += 1
#                 curr_len += 1
#             else:
#                 balance -= 1
#                 curr_len += 1
#                 if balance < 0:
#                     balance = 0
#                     curr_len = 0
#                 elif balance > 0:
#                     len1 = curr_len - balance
#                     max_len = max(max_len, len1)
#                 else:
#                     max_len = max(max_len, curr_len)
#         return max_len


# TLE
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#
#         def is_valid(ss: str) -> bool:
#             balance = 0
#             for ssi in ss:
#                 if ssi == '(':
#                     balance += 1
#                 else:
#                     balance -= 1
#                     if balance < 0:
#                         return False
#             return balance == 0
#
#         for l in range(2 * (n//2), 0, -2):
#             for i in range(n-l+1):
#                 if is_valid(s[i:i+l]):
#                     return l
#
#         return 0

# Runtime: 44 ms, faster than 71.31% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.3 MB, less than 95.18% of Python3 online submissions for Longest Valid Parentheses.
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         dp = [0] * n
#         max_len = 0
#         for i in range(1, n):
#             if s[i] == ')':
#                 if s[i-1] == '(':
#                     dp[i] = (dp[i-2] + 2) if i >= 2 else 2
#                 elif i - dp[i-1] > 0 and s[i-dp[i-1]-1] == '(':
#                     if i - dp[i-1] >= 2:
#                         dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
#                     else:
#                         dp[i] = dp[i - 1] + 2
#                 max_len = max(max_len, dp[i])
#
#         return max_len


# Runtime: 44 ms, faster than 71.31% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.7 MB, less than 37.58% of Python3 online submissions for Longest Valid Parentheses.
# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         n = len(s)
#         max_len = 0
#         st = [-1]
#         for i in range(n):
#             if s[i] == '(':
#                 st.append(i)
#             else:
#                 st.pop()
#                 if not st:
#                     st.append(i)
#                 else:
#                     max_len = max(max_len, i - st[-1])
#         return max_len

# Runtime: 52 ms, faster than 26.94% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.4 MB, less than 88.12% of Python3 online submissions for Longest Valid Parentheses.
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        max_len = 0
        for start, end, step, br in [(0, n, 1, '('), (n-1, -1, -1, ')')]:
            left, right = 0, 0
            for i in range(start, end, step):
                if s[i] == br:
                    left += 1
                else:
                    right += 1
                if left == right:
                    max_len = max(max_len, right+left)
                if right > left:
                    left, right = 0, 0
        return max_len




tests = [
    ("()(()", 2),

    ("(()", 2),
    (")()())", 4),
    ("", 0)
]

run_functional_tests(Solution().longestValidParentheses, tests)