"""
https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/description/?envType=daily-question&envId=2024-03-05

Given a string s consisting only of characters 'a', 'b', and 'c'. You are asked to apply the following algorithm on the string any number of times:

Pick a non-empty prefix from the string s where all the characters in the prefix are equal.
Pick a non-empty suffix from the string s where all the characters in this suffix are equal.
The prefix and the suffix should not intersect at any index.
The characters from the prefix and suffix must be the same.
Delete both the prefix and the suffix.
Return the minimum length of s after performing the above operation any number of times (possibly zero times).



Example 1:

Input: s = "ca"
Output: 2
Explanation: You can't remove any characters, so the string stays as is.
Example 2:

Input: s = "cabaabac"
Output: 0
Explanation: An optimal sequence of operations is:
- Take prefix = "c" and suffix = "c" and remove them, s = "abaaba".
- Take prefix = "a" and suffix = "a" and remove them, s = "baab".
- Take prefix = "b" and suffix = "b" and remove them, s = "aa".
- Take prefix = "a" and suffix = "a" and remove them, s = "".
Example 3:

Input: s = "aabccabba"
Output: 3
Explanation: An optimal sequence of operations is:
- Take prefix = "aa" and suffix = "a" and remove them, s = "bccabb".
- Take prefix = "b" and suffix = "bb" and remove them, s = "cca".


Constraints:

1 <= s.length <= 105
s only consists of characters 'a', 'b', and 'c'.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 59
# ms
# Beats
# 91.47%
# of users with Python3
# Memory
# 17.34
# MB
# Beats
# 75.83%
# of users with Python3
class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        i1, i2 = 0, n-1
        while i1 <= i2:
            if i1 == i2:
                return 1
            c1, c2 = s[i1], s[i2]
            if c1 != c2:
                return i2 - i1 + 1
            while i1 <= i2 and s[i1] == c1:
                i1 += 1
            while i1 <= i2 and s[i2] == c2:
                i2 -= 1

        return 0


# bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb
# cbc

tests = [
    ["ca", 2],
    ["cabaabac", 0],
    ["aabccabba", 3],
    ["bbbbbbbbbbbbbbbbbbbbbbbbbbbabbbbbbbbbbbbbbbccbcbcbccbbabbb", 1],
]

run_functional_tests(Solution().minimumLength, tests)
