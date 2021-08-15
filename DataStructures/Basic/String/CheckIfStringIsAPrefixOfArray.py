"""
https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.



Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 36 ms, faster than 80.03% of Python3 online submissions for Check If String Is a Prefix of Array.
# Memory Usage: 14.3 MB, less than 33.29% of Python3 online submissions for Check If String Is a Prefix of Array.
# class Solution:
#     def isPrefixString(self, s: str, words: List[str]) -> bool:
#         r = ""
#         for w in words:
#             r += w
#             if r == s:
#                 return True
#             if len(r) > len(s):
#                 break
#         return False


# Runtime: 36 ms, faster than 80.03% of Python3 online submissions for Check If String Is a Prefix of Array.
# Memory Usage: 14.3 MB, less than 63.18% of Python3 online submissions for Check If String Is a Prefix of Array.
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        n = len(s)
        j, k = 0, 0
        for i in range(n):
            if j == len(words):
                return False
            if s[i] != words[j][k]:
                return False
            k += 1
            if k == len(words[j]):
                j += 1
                k = 0
        return k == 0


tests = [
    ["ccccccccc", ["c","cc"], False],
    ["iloveleetcode", ["i","love","leetcode","apples"], True],
    ["iloveleetcode", ["apples","i","love","leetcode"], False]
]

run_functional_tests(Solution().isPrefixString, tests)