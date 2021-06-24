"""
https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.



Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 96.28% of Python3 online submissions for Check if the Sentence Is Pangram.
# Memory Usage: 14.4 MB, less than 15.23% of Python3 online submissions for Check if the Sentence Is Pangram.
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([c for c in sentence])) == 26


tests = [
    ["thequickbrownfoxjumpsoverthelazydog", True],
    ["leetcode", False]
]

run_functional_tests(Solution().checkIfPangram, tests)