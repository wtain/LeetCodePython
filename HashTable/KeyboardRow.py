"""
https://leetcode.com/problems/keyboard-row/
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.






Example:

Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]


Note:

You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
"""
from typing import List


"""
Runtime: 32 ms, faster than 63.79% of Python3 online submissions for Keyboard Row.
Memory Usage: 13.8 MB, less than 58.69% of Python3 online submissions for Keyboard Row.
"""
class Solution:

    def getRow(self, c: chr) -> int:
        c = str.lower(c)
        if "qwertyuiop".find(c) >= 0:
            return 1
        if "asdfghjkl".find(c) >= 0:
            return 2
        if "zxcvbnm".find(c) >= 0:
            return 3
        return 0

    def findWords(self, words: List[str]) -> List[str]:
        result = []
        for w in words:
            canAdd = True
            row = -1
            for c in w:
                if row == -1:
                    row = self.getRow(c)
                elif row != self.getRow(c):
                    canAdd = False
                    break
            if canAdd:
                result.append(w)
        return result


print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))  # ["Alaska", "Dad"]
