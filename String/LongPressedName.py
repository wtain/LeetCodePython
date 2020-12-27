"""
https://leetcode.com/problems/long-pressed-name/
Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.



Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
Example 2:

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it wasn't in the typed output.
Example 3:

Input: name = "leelee", typed = "lleeelee"
Output: true
Example 4:

Input: name = "laiden", typed = "laiden"
Output: true
Explanation: It's not necessary to long press any character.


Constraints:

1 <= name.length <= 1000
1 <= typed.length <= 1000
name and typed contain only lowercase English letters.

Runtime: 32 ms, faster than 63.49% of Python3 online submissions for Long Pressed Name.
Memory Usage: 14.3 MB, less than 47.50% of Python3 online submissions for Long Pressed Name.
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n1 = len(name)
        n2 = len(typed)
        i1 = 0
        i2 = 0
        while i1 < n1 and i2 < n2:
            if name[i1] != typed[i2]:
                return False
            letter = name[i1]
            c1 = 1
            c2 = 1
            while i1 < n1 and letter == name[i1]:
                i1 += 1
                c1 += 1
            while i2 < n2 and letter == typed[i2]:
                i2 += 1
                c2 += 1
            if c2 < c1:
                return False
        return i1 == n1 and i2 == n2


tests = [
    ("alex", "aaleex", True),
    ("saeed", "ssaaedd", False),
    ("leelee", "lleeelee", True),
    ("laiden", "laiden", True)
]

for test in tests:
    result = Solution().isLongPressedName(test[0], test[1])
    expected = test[2]
    if result == expected:
        print("PASS")
    else:
        print("FAIL")