"""
https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

Given an array of strings patterns and a string word, return the number of strings in patterns that exist as a substring in word.

A substring is a contiguous sequence of characters within a string.



Example 1:

Input: patterns = ["a","abc","bc","d"], word = "abc"
Output: 3
Explanation:
- "a" appears as a substring in "abc".
- "abc" appears as a substring in "abc".
- "bc" appears as a substring in "abc".
- "d" does not appear as a substring in "abc".
3 of the strings in patterns appear as a substring in word.
Example 2:

Input: patterns = ["a","b","c"], word = "aaaaabbbbb"
Output: 2
Explanation:
- "a" appears as a substring in "aaaaabbbbb".
- "b" appears as a substring in "aaaaabbbbb".
- "c" does not appear as a substring in "aaaaabbbbb".
2 of the strings in patterns appear as a substring in word.
Example 3:

Input: patterns = ["a","a","a"], word = "ab"
Output: 3
Explanation: Each of the patterns appears as a substring in word "ab".


Constraints:

1 <= patterns.length <= 100
1 <= patterns[i].length <= 100
1 <= word.length <= 100
patterns[i] and word consist of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 45 ms, faster than 42.74% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# Memory Usage: 14.4 MB, less than 40.21% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# class Solution:
#     def numOfStrings(self, patterns: List[str], word: str) -> int:
#         cnt = 0
#         for pat in patterns:
#             if word.find(pat) != -1:
#                 cnt += 1
#         return cnt


# Runtime: 36 ms, faster than 78.63% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
# Memory Usage: 14.2 MB, less than 89.31% of Python3 online submissions for Number of Strings That Appear as Substrings in Word.
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(1 for pat in patterns if word.find(pat) != -1)


tests = [
    [["a","abc","bc","d"], "abc", 3],
    [["a","b","c"], "aaaaabbbbb", 2],
    [["a","a","a"], "ab", 3]
]

run_functional_tests(Solution().numOfStrings, tests)