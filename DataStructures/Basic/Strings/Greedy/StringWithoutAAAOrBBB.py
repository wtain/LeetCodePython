"""
https://leetcode.com/problems/string-without-aaa-or-bbb/

Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.


Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"


Constraints:

0 <= a, b <= 100
It is guaranteed such an s exists for the given a and b.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def strWithout3a3b(self, a: int, b: int) -> str:
#         result = ""
#         while a and b:
#             if a > b:
#                 t = min(a, 2*b) // 2
#                 result += "aab" * t
#                 a -= 2 * t
#                 b -= t
#             elif b > a:
#                 t = min(2 * a, b) // 2
#                 result += "bba" * t
#                 a -= t
#                 b -= 2 * t
#             else:
#                 t = min(a, b)
#                 result += "ab" * t
#                 a -= t
#                 b -= t
#         if a:
#             if result and result[-1] == 'a':
#                 result = "a" * (a-1) + result + "a"
#             else:
#                 result += "a" * a
#         if b:
#             if result and result[-1] == 'b':
#                 result = "b" * (b-1) + result + "b"
#             else:
#                 result += "b" * b
#         return result

# class Solution:
#     def strWithout3a3b(self, a: int, b: int) -> str:
#         result = ""
#         if a > b:
#             t = a // b
#             r = a % b
#
#         return result

# class Solution:
#     def strWithout3a3b(self, a: int, b: int) -> str:
#         result = ""
#         while a and b:
#             if a > b:
#                 t = min(a, 2*b) // 2
#                 result += "aab" * t
#                 a -= 2 * t
#                 b -= t
#             elif b > a:
#                 t = min(2 * a, b) // 2
#                 result += "bba" * t
#                 a -= t
#                 b -= 2 * t
#             else:
#                 t = min(a, b)
#                 result += "ab" * t
#                 a -= t
#                 b -= t
#         if a:
#             if result and result[-1] == 'a':
#                 result = "a" + result + "a" * (a-1)
#             else:
#                 result += "a" * a
#         if b:
#             if result and result[-1] == 'b':
#                 result = "b" + result + "b" * (b-1)
#             else:
#                 result += "b" * b
#         return result


# WRONG
# class Solution:
#     def strWithout3a3b(self, a: int, b: int) -> str:
#
#         def solve(x: int, y: int, cx: str, cy: str) -> str:
#             if x and y:
#                 if x >= 2*y:
#                     return (cx * 2 + cy) * y + cx * (x-2*y)
#                 elif x >= y:
#                     return (cx + cy) * y + cx * (x-y)
#             else:
#                 return cx * x
#
#         return solve(a, b, 'a', 'b') if a >= b else solve(b, a, 'b', 'a')


# Runtime: 24 ms, faster than 98.93% of Python3 online submissions for String Without AAA or BBB.
# Memory Usage: 14.2 MB, less than 55.73% of Python3 online submissions for String Without AAA or BBB.
class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:

        def solve(x: int, y: int, cx: str, cy: str) -> str:
            if x and y:
                if x >= 2*y:
                    return (cx * 2 + cy) * y + cx * (x-2*y)
                elif x >= y:
                    p = x - y
                    y -= p
                    return (cx * 2 + cy) * p + (cx + cy) * y
            else:
                return cx * x

        return solve(a, b, 'a', 'b') if a >= b else solve(b, a, 'b', 'a')


tests = [
    [1, 2, "abb"],
    [4, 1, "aabaa"],

    [4, 2, ""],
    [10, 8, ""],

    [4, 5, "babababab"],

    [4, 7, "bbabbababab"]
]


def check(test, result: str) -> bool:
    a, b = test[:2]
    c = Counter(result)
    if c.get('a') != a or c.get('b') != b:
        return False
    if result.find("aaa") != -1:
        return False
    return result.find("bbb") == -1


run_functional_tests(Solution().strWithout3a3b, tests, custom_check=check)
