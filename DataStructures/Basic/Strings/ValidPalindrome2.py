"""
https://leetcode.com/problems/valid-palindrome-ii/

Given a string s, return true if the s can be palindrome after deleting at most one character from it.



Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false


Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 164 ms, faster than 65.01% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 14.4 MB, less than 91.68% of Python3 online submissions for Valid Palindrome II.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = 0, n-1
        i0, j0 = -1, -1
        can_skip_i, can_skip_j = True, True
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            elif can_skip_i:
                can_skip_i = False
                i0, j0 = i, j
                i += 1
            elif can_skip_j:
                can_skip_j = False
                i, j = i0, j0
                j -= 1
            else:
                return False
        return True


tests = [
    ["aba", True],
    ["abca", True],
    ["abc", False]
]

run_functional_tests(Solution().validPalindrome, tests)
