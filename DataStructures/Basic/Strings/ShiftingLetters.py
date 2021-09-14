"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/637/week-2-september-8th-september-14th/3968/
https://leetcode.com/problems/shifting-letters/

You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.



Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.
Example 2:

Input: s = "aaa", shifts = [1,2,3]
Output: "gfd"


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
shifts.length == s.length
0 <= shifts[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 855 ms, faster than 41.70% of Python3 online submissions for Shifting Letters.
# Memory Usage: 28.1 MB, less than 13.86% of Python3 online submissions for Shifting Letters.
# class Solution:
#     def shiftingLetters(self, s: str, shifts: List[int]) -> str:
#         n = len(s)
#         v = 0
#         shifts2 = [0] * n
#         for i in range(n-1, -1, -1):
#             shifts2[i] = shifts[i] + v
#             v += shifts[i]
#         return "".join([chr(ord('a') + (ord(c) - ord('a') + shift) % 26) for c, shift in zip(s, shifts2)])


# Runtime: 1059 ms, faster than 21.40% of Python3 online submissions for Shifting Letters.
# Memory Usage: 27.7 MB, less than 40.30% of Python3 online submissions for Shifting Letters.
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        result = []
        t = sum(shifts) % 26
        for i, c in enumerate(s):
            idx = ord(c) - ord('a')
            result.append(chr(ord('a') + (idx + t) % 26 ))
            t = (t - shifts[i]) % 26
        return "".join(result)


tests = [
    ["abc", [3,5,9], "rpl"],
    ["aaa", [1,2,3], "gfd"]
]

run_functional_tests(Solution().shiftingLetters, tests)