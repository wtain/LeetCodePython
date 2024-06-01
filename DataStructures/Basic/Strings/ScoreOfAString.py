"""
https://leetcode.com/problems/score-of-a-string/description/?envType=daily-question&envId=2024-06-01

You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.



Example 1:

Input: s = "hello"

Output: 13

Explanation:

The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.

Example 2:

Input: s = "zaz"

Output: 50

Explanation:

The ASCII values of the characters in s are: 'z' = 122, 'a' = 97. So, the score of s would be |122 - 97| + |97 - 122| = 25 + 25 = 50.



Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 41
# ms
# Beats
# 24.95%
# of users with Python3
# Memory
# 16.41
# MB
# Beats
# 82.79%
# of users with Python3
class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(a)-ord(b)) for a, b in zip(s, s[1:]))


tests = [
    ["hello", 13],
    ["zaz", 50],
]

run_functional_tests(Solution().scoreOfString, tests)
