"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/639/week-4-september-22nd-september-28th/3985/
https://leetcode.com/problems/break-a-palindrome/

Given a palindromic string of lowercase English letters palindrome, replace exactly one character with any lowercase English letter so that the resulting string is not a palindrome and that it is the lexicographically smallest one possible.

Return the resulting string. If there is no way to replace a character to make it not a palindrome, return an empty string.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, a has a character strictly smaller than the corresponding character in b. For example, "abcc" is lexicographically smaller than "abcd" because the first position they differ is at the fourth character, and 'c' is smaller than 'd'.



Example 1:

Input: palindrome = "abccba"
Output: "aaccba"
Explanation: There are many ways to make "abccba" not a palindrome, such as "zbccba", "aaccba", and "abacba".
Of all the ways, "aaccba" is the lexicographically smallest.
Example 2:

Input: palindrome = "a"
Output: ""
Explanation: There is no way to replace a single character to make "a" not a palindrome, so return an empty string.
Example 3:

Input: palindrome = "aa"
Output: "ab"
Example 4:

Input: palindrome = "aba"
Output: "abb"


Constraints:

1 <= palindrome.length <= 1000
palindrome consists of only lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 28 ms, faster than 82.30% of Python3 online submissions for Break a Palindrome.
# Memory Usage: 14.4 MB, less than 14.55% of Python3 online submissions for Break a Palindrome.
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n <= 1:
            return ""
        s1, s2 = "", ""
        center = n // 2
        for i in range(n):
            if palindrome[i] != 'a' and (n % 2 == 0 or i != center):
                s1 = palindrome[:i] + 'a' + palindrome[i+1:]
                break
        for i in range(n-1, -1, -1):
            if palindrome[i] == 'a' and (n % 2 == 0 or i != center):
                s2 = palindrome[:i] + 'b' + palindrome[i+1:]
                break
        if not s1:
            return s2
        if not s2:
            return s1
        return min(s1, s2)


tests = [
    ["abccba", "aaccba"],
    ["a", ""],
    ["aa", "ab"],
    ["aba", "abb"]
]

run_functional_tests(Solution().breakPalindrome, tests)