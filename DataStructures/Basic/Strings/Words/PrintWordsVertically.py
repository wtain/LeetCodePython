"""
https://leetcode.com/problems/print-words-vertically/

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.



Example 1:

Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically.
 "HAY"
 "ORO"
 "WEU"
Example 2:

Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed.
"TBONTB"
"OEROOE"
"   T"
Example 3:

Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]


Constraints:

1 <= s.length <= 200
s contains only upper case English letters.
It's guaranteed that there is only one space between 2 words.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def printVertically(self, s: str) -> List[str]:
#         words = s.split(' ')
#         max_len = max(len(w) for w in words)
#         n = len(words)
#         result = [[" "] * n for _ in range(max_len)]
#         for i, w in enumerate(words):
#             for j, c in enumerate(w):
#                 result[j][i] = c
#         for i in range(n-1, -1, -1):
#             if result[-1][i] != " ":
#                 break
#             result[-1][i] = ""
#         return ["".join(l) for l in result]


# WRONG
# class Solution:
#     def printVertically(self, s: str) -> List[str]:
#         words = s.split(' ')
#         max_len = max(len(w) for w in words)
#         n = len(words)
#         result = [[" "] * n for _ in range(max_len)]
#         for i, w in enumerate(words):
#             for j, c in enumerate(w):
#                 result[j][i] = c
#         for i in range(n-1, -1, -1):
#             if result[-1][i] != " ":
#                 break
#             result[-1][i] = ""
#         for j in range(max_len-1, -1, -1):
#             if result[j][-1] != " " and result[j][-1] != "":
#                 break
#             result[j][-1] = ""
#         return ["".join(l) for l in result]


# Runtime: 28 ms, faster than 84.08% of Python3 online submissions for Print Words Vertically.
# Memory Usage: 14.3 MB, less than 23.57% of Python3 online submissions for Print Words Vertically.
class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(' ')
        max_len = max(len(w) for w in words)
        n = len(words)
        result = [[" "] * n for _ in range(max_len)]
        for i, w in enumerate(words):
            for j, c in enumerate(w):
                result[j][i] = c
        for j in range(max_len-1, -1, -1):
            for i in range(n - 1, -1, -1):
                if result[j][i] != " " and result[j][i] != "":
                    break
                result[j][i] = ""
        return ["".join(l) for l in result]


tests = [
    ["HOW ARE YOU", ["HAY","ORO","WEU"]],
    ["TO BE OR NOT TO BE", [
        "TBONTB",
        "OEROOE",
        "   T"]],
    ["CONTEST IS COMING", [
        "CIC",
        "OSO",
        "N M",
        "T I",
        "E N",
        "S G",
        "T"]],

    ["AA BBB C DDDD EEEEE F", [
        "ABCDEF",
        "AB DE",
        " B DE",
        "   DE",
        "    E"]],

    ["HOW A Y", ["HAY",
                 "O",
                 "W"]]
]

run_functional_tests(Solution().printVertically, tests)
