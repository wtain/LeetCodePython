"""
https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.



Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.
Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".
Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists only of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 108 ms, faster than 56.40% of Python3 online submissions for Find First Palindromic String in the Array.
# Memory Usage: 14.1 MB, less than 69.38% of Python3 online submissions for Find First Palindromic String in the Array.
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_palindrome(w: str) -> bool:
            i, n = 0, len(w)
            i1, i2 = 0, n-1
            while i1 < i2:
                if w[i1] != w[i2]:
                    return False
                i1 += 1
                i2 -= 1
            return True

        for w in words:
            if is_palindrome(w):
                return w

        return ""


tests = [
    [["abc","car","ada","racecar","cool"], "ada"],
    [["notapalindrome","racecar"], "racecar"],
    [["def","ghi"], ""]
]

run_functional_tests(Solution().firstPalindrome, tests)
