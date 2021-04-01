"""
https://leetcode.com/problems/word-pattern/
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
"""
from collections.abc import Set
from typing import Dict


"""
Runtime: 48 ms, faster than 14.69% of Python3 online submissions for Word Pattern.
Memory Usage: 13.6 MB, less than 97.02% of Python3 online submissions for Word Pattern.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letterToWord: Dict[chr, str] = {}
        words: Set[str] = set()
        m = len(pattern)
        def checkPair(i: int, cw: str) -> bool:
            if i >= m:
                return False
            if letterToWord.get(pattern[i]):
                word = letterToWord[pattern[i]]
                if word != cw:
                    return False
            else:
                if cw in words:
                    return False
                words.add(cw)
                letterToWord[pattern[i]] = cw
            return True
        i = 0
        cw = ""
        for c in s:
            if c == ' ':
                if not checkPair(i, cw):
                    return False
                i += 1
                cw = ""
            else:
                cw += c
        if not checkPair(i, cw):
            return False
        i += 1
        return i == m


print(Solution().wordPattern("jquery", "jquery"))  # False
print(Solution().wordPattern("abba", "dog cat cat dog"))  # True
print(Solution().wordPattern("abba", "dog cat cat fish"))  # False
print(Solution().wordPattern("aaaa", "dog cat cat dog"))  # False
print(Solution().wordPattern("abba", "dog dog dog dog"))  # False
