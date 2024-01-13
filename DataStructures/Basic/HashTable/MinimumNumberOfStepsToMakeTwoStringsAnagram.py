"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/?envType=daily-question&envId=2024-01-13

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.



Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.


Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 103
# ms
# Beats
# 88.16%
# of users with Python3
# Memory
# 17.98
# MB
# Beats
# 11.97%
# of users with Python3
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1, c2 = Counter(s), Counter(t)
        result = 0
        for c in c1:
            result += max(c1[c] - c2[c], 0)
        return result


tests = [
    ["bab", "aba", 1],
    ["leetcode", "practice", 5],
    ["anagram", "mangaar", 0],
]

run_functional_tests(Solution().minSteps, tests)
