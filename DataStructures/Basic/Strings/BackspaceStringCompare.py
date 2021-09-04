"""
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?

Runtime: 28 ms, faster than 82.54% of Python3 online submissions for Backspace Strings Compare.
Memory Usage: 14.3 MB, less than 27.62% of Python3 online submissions for Backspace Strings Compare.
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        n1 = len(S)
        n2 = len(T)
        i = n1-1
        j = n2-1

        def fetch(S: str, i: int) -> int:
            nSkip = 0
            while i >= 0 and (S[i] == '#' or nSkip > 0):
                if S[i] == '#':
                    nSkip += 1
                else:
                    nSkip -= 1
                i -= 1
            return i

        while i >= 0 and j >= 0:
            i = fetch(S, i)
            j = fetch(T, j)
            if i < 0 and j < 0:
                return True
            if i < 0 or j < 0:
                break
            if S[i] != T[j]:
                return False
            i -= 1
            j -= 1
        if i >= 0 and S[i] == '#':
            i = fetch(S, i)
        if j >= 0 and T[j] == '#':
            j = fetch(T, j)
        return i < 0 and j < 0


tests = [("nzp#o#g", "b#nzp#o#g", True),

         ("ab#c", "ad#c", True),
         ("ab##", "c#d#", True),
         ("a##c", "#a#c", True),
         ("a#c", "b", False)]

for test in tests:
    if Solution().backspaceCompare(test[0], test[1]) != test[2]:
        print("FAIL")
    else:
        print("PASS")