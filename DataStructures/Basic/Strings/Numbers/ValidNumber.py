"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3744/
https://leetcode.com/problems/valid-number/

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
"""
import re

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 44 ms, faster than 5.95% of Python3 online submissions for Valid Number.
# Memory Usage: 14.3 MB, less than 60.64% of Python3 online submissions for Valid Number.
# class Solution:
#     def isNumber(self, s: str) -> bool:
#         n = len(s)
#         i = 0
#
#         # N -> (D|I)[(e|E)I]
#         # D -> [(+|-)](D1|D2|D3)
#         # D1 -> d+.
#         # D2 -> d+.d+
#         # D3 -> .d+
#         # I ->[(+|-)]d+
#
#         def N(i: int) -> bool:
#             nonlocal s, n
#             result = []
#             result += D(i)
#             result += I(i)
#             if n in result:
#                 return True
#             for i in result:
#                 if str.upper(s[i]) != 'E':
#                     continue
#                 i += 1
#                 if n in I(i):
#                     return True
#             return False
#
#         def D(i: int) -> List[int]:
#             nonlocal s, n
#             if i == n:
#                 return []
#             if s[i] in ['+', '-']:
#                 i += 1
#             if i == n:
#                 return []
#             result = []
#             result += D1(i)
#             result += D2(i)
#             result += D3(i)
#             return result
#
#         def digits(i: int) -> (int, bool):
#             if i == n or not str.isdigit(s[i]):
#                 return i, False
#             while i < n and str.isdigit(s[i]):
#                 i += 1
#             return i, True
#
#         def I(i: int) -> List[int]:
#             nonlocal s, n
#             if i == n:
#                 return []
#             if s[i] in ['+', '-']:
#                 i += 1
#             i, f = digits(i)
#             if not f:
#                 return []
#             return [i]
#
#         def D1(i: int) -> List[int]:
#             nonlocal s, n
#             i, f = digits(i)
#             if not f or i == n or s[i] != '.':
#                 return []
#             return [i+1]
#
#         def D2(i: int) -> List[int]:
#             nonlocal s, n
#             i, f = digits(i)
#             if not f or i == n or s[i] != '.':
#                 return []
#             return [digits(i+1)[0]]
#
#         def D3(i: int) -> List[int]:
#             nonlocal s, n
#             if i == n or s[i] != '.':
#                 return []
#             i, f = digits(i + 1)
#             if not f:
#                 return []
#             return [i]
#
#         return N(i)

        # def parse_integer(canBeEmpty: bool) -> bool:
        #     nonlocal i, n, s
        #     if i < n and s[i] in ['+', '-']:
        #         i += 1
        #     i0 = i
        #     while i < n and str.isdigit(s[i]):
        #         i += 1
        #     return canBeEmpty or i > i0
        #
        # if not n:
        #     return False
        #
        # if s[i] == '.':
        #     if not parse_integer(False):
        #         return False
        #     if i == n:
        #         return True
        #     if s[i] not in ['e', 'E']:
        #         return False
        #     i += 1
        #     return parse_integer(False)
        #
        # if s[i] in ['+', '-']:
        #     i += 1
        #     if not parse_integer(True):
        #         return False
        #     if i == n:
        #         return True
        #     if s[i] == '.':
        #         i += 1
        #
        # return False


#         # N -> (D|I)[(e|E)I]
#         # D -> [(+|-)](D1|D2|D3)
#         # D1 -> d+.
#         # D2 -> d+.d+
#         # D3 -> .d+
#         # I ->[(+|-)]d+

# Runtime: 36 ms, faster than 53.27% of Python3 online submissions for Valid Number.
# Memory Usage: 14.3 MB, less than 60.64% of Python3 online submissions for Valid Number.
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.compile("^[+-]?((\d+\.\d*)|(\.\d+)|(\d+))([eE][+-]?\d+)?$").match(s) is not None


tests = [

    ["0", True],
    ["e", False],
    [".", False],
    [".1", True],
]

for n in ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]:
    tests.append([n, True])

for n in ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
    tests.append([n, False])

run_functional_tests(Solution().isNumber, tests)
# run_functional_tests(Solution().isNumber, [["-0.1", True]])
# run_functional_tests(Solution().isNumber, [[".", False]])
# run_functional_tests(Solution().isNumber, [["95a54e53", False]])
# run_functional_tests(Solution().isNumber, [["+6e-1", True]])


