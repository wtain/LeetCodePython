"""
https://leetcode.com/problems/count-vowel-substrings-of-a-string/

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels present in it.

Given a string word, return the number of vowel substrings in word.



Example 1:

Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
Example 2:

Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
Example 3:

Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
Example 4:

Input: word = "bbaeixoubb"
Output: 0
Explanation: The only substrings that contain all five vowels also contain consonants, so there are no vowel substrings.


Constraints:

1 <= word.length <= 100
word consists of lowercase English letters only.
"""
from collections import Counter

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         cnt = 0
#         vowels = "aeiou"
#         c = Counter(word[:5])
#         i1, i2 = 0, 5
#         n = len(word)
#         if all(c[v] for v in vowels):
#             cnt += 1
#         while i2 < n:
#             while i1 < i2 and all(c[v] for v in vowels):
#                 c[word[i1]] -= 1
#                 i1 += 1
#             if all(c[v] for v in vowels):
#                 cnt += 1
#             c[word[i2]] += 1
#             i2 += 1
#         return cnt


# XXX
# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         cnt = 0
#         vowels = "aeiou"
#         c = Counter(word[:5])
#
#         def is_vowel_substring() -> bool:
#             nonlocal c, vowels
#             return all(c[v] for v in vowels)
#
#         i1, i2 = 0, 5
#         n = len(word)
#         while i2 < n and not is_vowel_substring():
#             c[word[i2]] += 1
#             i2 += 1
#         if not is_vowel_substring():
#             return 0
#
#         while i1 < n:
#             j = i2
#             while j < n and word[j] in vowels:
#                 c[word[j]] += 1
#                 j += 1
#             cnt += j - i2
#             while j < n and
#
#         return cnt


# Runtime: 244 ms, faster than 35.15% of Python3 online submissions for Count Vowel Substrings of a String.
# Memory Usage: 14.2 MB, less than 54.19% of Python3 online submissions for Count Vowel Substrings of a String.
# class Solution:
#     def countVowelSubstrings(self, word: str) -> int:
#         cnt, n = 0, len(word)
#         vowels = set("aeiou")
#         c = Counter()
#
#         def is_vowel_substring() -> bool:
#             nonlocal c, vowels
#             return all(c[v] for v in vowels) and len(c.keys()) == 5
#
#         i1 = 0
#
#         while i1 < n:
#             c = Counter()
#             while i1 < n and word[i1] not in vowels:
#                 i1 += 1
#             i2 = i1
#             i0 = -1
#             while i2 < n and word[i2] in vowels:
#                 c[word[i2]] += 1
#                 i2 += 1
#                 if is_vowel_substring():
#                     # print(word[i1:i2])
#                     if i0 == -1:
#                         i0 = i2
#                     cnt += 1
#             # while i1 < i2 and is_vowel_substring():
#             #     c[word[i1]] -= 1
#             #     i1 += 1
#             #     if is_vowel_substring():
#             #         print(word[i1:i2])
#             #         cnt += 1
#             i1 += 1
#         return cnt


# Runtime: 248 ms, faster than 34.45% of Python3 online submissions for Count Vowel Substrings of a String.
# Memory Usage: 14.2 MB, less than 54.19% of Python3 online submissions for Count Vowel Substrings of a String.
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt, n = 0, len(word)
        vowels = set("aeiou")
        c = Counter()

        def is_vowel_substring() -> bool:
            nonlocal c, vowels
            return all(c[v] for v in vowels) and len(c.keys()) == 5

        i1 = 0

        while i1 < n:
            c = Counter()
            while i1 < n and word[i1] not in vowels:
                i1 += 1
            i2 = i1
            while i2 < n and word[i2] in vowels:
                c[word[i2]] += 1
                i2 += 1
                if is_vowel_substring():
                    cnt += 1
            i1 += 1
        return cnt


tests = [
    ["aeiouu", 2],
    ["unicornarihan", 0],
    ["cuaieuouac", 7],
    ["bbaeixoubb", 0]
]

run_functional_tests(Solution().countVowelSubstrings, tests)
