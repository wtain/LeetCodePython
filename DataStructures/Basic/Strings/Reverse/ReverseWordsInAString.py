"""
https://leetcode.com/problems/reverse-words-in-a-string/

Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 48 ms, faster than 25.05% of Python3 online submissions for Reverse Words in a Strings.
Memory Usage: 14.2 MB, less than 97.87% of Python3 online submissions for Reverse Words in a Strings.
"""
class Solution:

    def addWord(self, result, cw: str):
        if len(cw) > 0:
            if len(result) > 0:
                result = " " + result
            result = cw + result
        return result

    def reverseWords(self, s: str) -> str:
        cw = ""
        result = ""
        for c in s:
            if c == " ":
                result = self.addWord(result, cw)
                cw = ""
            else:
                cw = cw + c
        result = self.addWord(result, cw)
        return result


tests = [
    ["the sky is blue", "blue is sky the"],
    ["  hello world!  ", "world! hello"],
    ["a good   example", "example good a"]
]

run_functional_tests(Solution().reverseWords, tests)
