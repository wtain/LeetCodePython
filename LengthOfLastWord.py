"""
https://leetcode.com/problems/length-of-last-word/
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""

"""WRONG"""
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cw = 0
        longest = 0
        for ch in s:
            if ch == ' ':
                longest = max(longest, cw)
                cw = 0
            else:
                cw += 1
        longest = max(longest, cw)
        return longest
"""

"""
Runtime: 40 ms, faster than 22.17% of Python3 online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 43.25% of Python3 online submissions for Length of Last Word.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)

        i = n-1
        while i > 0 and s[i] == ' ':
            i -= 1

        s = s[:i+1]
        n = len(s)

        pos = s.rfind(" ")
        if pos == -1:
            return n
        return n - pos - 1


print(Solution().lengthOfLastWord("a "))  # 1
print(Solution().lengthOfLastWord("Today is a nice day"))  # 3
print(Solution().lengthOfLastWord("Hello World"))  # 5