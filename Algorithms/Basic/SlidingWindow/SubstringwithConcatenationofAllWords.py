"""
https://leetcode.com/problems/substring-with-concatenation-of-all-words/

You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.



Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []
Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]


Constraints:

1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from collections import Counter, defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 865 ms, faster than 41.47% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.2 MB, less than 77.75% of Python3 online submissions for Substring with Concatenation of All Words.
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/solution/
# class Solution:
#     def findSubstring(self, s: str, words: List[str]) -> List[int]:
#         n, k = len(s), len(words)
#         word_length = len(words[0])
#         substring_size = word_length * k
#         word_count = Counter(words)
#
#         def check(i):
#             remaining = word_count.copy()
#             words_used = 0
#
#             for j in range(i, i+substring_size, word_length):
#                 sub = s[j: j+word_length]
#                 if remaining[sub] > 0:
#                     remaining[sub] -= 1
#                     words_used += 1
#                 else:
#                     break
#
#             return words_used == k
#
#         result = []
#         for i in range(n-substring_size+1):
#             if check(i):
#                 result.append(i)
#         return result


# Runtime: 142 ms, faster than 83.82% of Python3 online submissions for Substring with Concatenation of All Words.
# Memory Usage: 14.3 MB, less than 16.18% of Python3 online submissions for Substring with Concatenation of All Words.
# https://leetcode.com/problems/substring-with-concatenation-of-all-words/solution/
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n, k = len(s), len(words)
        word_length = len(words[0])
        substring_size = word_length * k
        word_count = Counter(words)

        def sliding_window(left):
            words_found = defaultdict(int)
            words_used = 0
            excess_word = False

            for right in range(left, n, word_length):
                sub = s[right:right+word_length]
                if sub not in word_count:
                    words_found = defaultdict(int)
                    words_used = 0
                    excess_word = False
                    left = right + word_length
                else:
                    while right - left == substring_size or excess_word:
                        leftmost_word = s[left:left+word_length]
                        left += word_length
                        words_found[leftmost_word] -= 1
                        if words_found[leftmost_word] == word_count[leftmost_word]:
                            excess_word = False
                        else:
                            words_used -= 1

                    words_found[sub] += 1
                    if words_found[sub] <= word_count[sub]:
                        words_used += 1
                    else:
                        excess_word = True

                    if words_used == k and not excess_word:
                        result.append(left)

        result = []
        for i in range(word_length):
            sliding_window(i)
        return result


tests = [
    ["barfoothefoobarman", ["foo","bar"], [0,9]],
    ["wordgoodgoodgoodbestword", ["word","good","best","word"], []],
    ["barfoofoobarthefoobarman", ["bar","foo","the"], [6,9,12]]
]

run_functional_tests(Solution().findSubstring, tests)
