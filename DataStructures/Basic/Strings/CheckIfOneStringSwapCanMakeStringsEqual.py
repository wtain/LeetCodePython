"""
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.



Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
Example 4:

Input: s1 = "abcd", s2 = "dcba"
Output: false


Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 63.28% of Python3 online submissions for Check if One Strings Swap Can Make Strings Equal.
# Memory Usage: 14.3 MB, less than 19.39% of Python3 online submissions for Check if One Strings Swap Can Make Strings Equal.
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        first_i = -1
        swapped = False
        for i in range(n):
            if s1[i] != s2[i]:
                if swapped:
                    return False
                if first_i == -1:
                    first_i = i
                else:
                    if s1[i] == s2[first_i] and s1[first_i] == s2[i]:
                       swapped = True
                    else:
                        return False
        if first_i >= 0 and not swapped:
            return False
        return True


tests = [
    ["aa", "ac", False],

    ["bank", "kanb", True],
    ["attack", "defend", False],
    ["kelb", "kelb", True],
    ["abcd", "dcba", False]
]


run_functional_tests(Solution().areAlmostEqual, tests)