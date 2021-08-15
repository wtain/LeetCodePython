"""
https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

Given a string s, return true if s is a good string, or false otherwise.

A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).



Example 1:

Input: s = "abacbc"
Output: true
Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
Example 2:

Input: s = "aaabb"
Output: false
Explanation: The characters that appear in s are 'a' and 'b'.
'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 83.19% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
# Memory Usage: 14.4 MB, less than 32.82% of Python3 online submissions for Check if All Characters Have Equal Number of Occurrences.
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        cnts = Counter(s).values()
        return min(cnts) == max(cnts)


tests = [
    ["abacbc", True],
    ["aaabb", False]
]

run_functional_tests(Solution().areOccurrencesEqual, tests)