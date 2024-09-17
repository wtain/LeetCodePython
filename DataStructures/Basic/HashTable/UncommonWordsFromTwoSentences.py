"""
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/?envType=daily-question&envId=2024-09-17

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.



Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"

Output: ["sweet","sour"]

Explanation:

The word "sweet" appears only in s1, while the word "sour" appears only in s2.

Example 2:

Input: s1 = "apple apple", s2 = "banana"

Output: ["banana"]



Constraints:

1 <= s1.length, s2.length <= 200
s1 and s2 consist of lowercase English letters and spaces.
s1 and s2 do not have leading or trailing spaces.
All the words in s1 and s2 are separated by a single space.
"""
from collections import Counter
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 39
# ms
# Beats
# 29.74%
# Analyze Complexity
# Memory
# 16.52
# MB
# Beats
# 44.21%
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        w1 = Counter(s1.split(' '))
        w2 = Counter(s2.split(' '))
        wu1 = {w for w in w1 if w1[w] == 1}
        wu2 = {w for w in w2 if w2[w] == 1}
        w1 = set(w1)
        w2 = set(w2)
        wu1 = wu1.difference(w2)
        wu2 = wu2.difference(w1)
        return list(set.symmetric_difference(wu1, wu2))


tests = [
    ["s z z z s", "s z ejt", ["ejt"]],
    ["this apple is sweet", "this apple is sour", ["sweet","sour"]],
    ["apple apple", "banana", ["banana"]],
]

run_functional_tests(Solution().uncommonFromSentences, tests, custom_check=compareSets)
