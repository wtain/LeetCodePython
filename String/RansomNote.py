"""
https://leetcode.com/problems/ransom-note/
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.



Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:

You may assume that both strings contain only lowercase letters.
"""
from typing import Dict


"""
Runtime: 76 ms, faster than 37.36% of Python3 online submissions for Ransom Note.
Memory Usage: 14.2 MB, less than 9.25% of Python3 online submissions for Ransom Note.
"""
class Solution:

    def getHist(self, s: str) -> Dict[chr, int]:
        result = {}
        for c in s:
            cnt = result.get(c) or 0
            result[c] = cnt + 1
        return result


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        noteH = self.getHist(ransomNote)
        magH = self.getHist(magazine)
        for c in noteH:
            cnt = noteH[c]
            cnt2 = magH.get(c) or 0
            if cnt > cnt2:
                return False
        return True


print(Solution().canConstruct("a", "b"))  # False
print(Solution().canConstruct("aa", "ab"))  # False
print(Solution().canConstruct("aa", "aab"))  # True
