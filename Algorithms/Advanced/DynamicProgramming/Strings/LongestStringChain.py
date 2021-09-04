"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3746/
https://leetcode.com/problems/longest-string-chain/

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".
Example 2:

Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
Output: 5


Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
"""
from collections import defaultdict
from functools import lru_cache
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2960 ms, faster than 5.01% of Python3 online submissions for Longest Strings Chain.
# Memory Usage: 15.2 MB, less than 24.55% of Python3 online submissions for Longest Strings Chain.
# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#
#         @lru_cache()
#         def diff_one_letter(w1: str, w2: str) -> bool:
#             n1, n2 = len(w1), len(w2)
#             if n1 > n2:
#                 return diff_one_letter(w2, w1)
#             if n2 - 1 != n1:
#                 return False
#             foundDiff = False
#             i1, i2 = 0, 0
#             while i1 < n1 and i2 < n2:
#                 if w1[i1] != w2[i2]:
#                     if foundDiff:
#                         return False
#                     foundDiff = True
#                     i2 += 1
#                 else:
#                     i1 += 1
#                     i2 += 1
#             return True
#
#         words.sort(key=lambda w: len(w))
#
#         d = {}
#         for w in words:
#             d[w] = 1
#
#         maxlen = 1
#         n = len(words)
#         for i1 in range(n):
#             w1 = words[i1]
#             for i2 in range(i1):
#                 w2 = words[i2]
#                 if diff_one_letter(w2, w1):
#                     d[w1] = max(d[w1], d[w2] + 1)
#                     maxlen = max(maxlen, d[w1])
#
#         return maxlen


# Runtime: 1892 ms, faster than 9.43% of Python3 online submissions for Longest Strings Chain.
# Memory Usage: 14.6 MB, less than 90.08% of Python3 online submissions for Longest Strings Chain.
# class Solution:
#     def longestStrChain(self, words: List[str]) -> int:
#
#         def diff_one_letter(w1: str, w2: str) -> bool:
#             n1, n2 = len(w1), len(w2)
#             if n2 - 1 != n1:
#                 return False
#             foundDiff = False
#             i1, i2 = 0, 0
#             while i1 < n1 and i2 < n2:
#                 if w1[i1] != w2[i2]:
#                     if foundDiff:
#                         return False
#                     foundDiff = True
#                     i2 += 1
#                 else:
#                     i1 += 1
#                     i2 += 1
#             return True
#
#         words.sort(key=lambda w: len(w))
#
#         d = defaultdict(int)
#
#         maxlen = 1
#         n = len(words)
#         for i1 in range(n):
#             w1 = words[i1]
#             if len(w1) == 1:
#                 continue
#             for i2 in range(i1):
#                 w2 = words[i2]
#                 if diff_one_letter(w2, w1):
#                     d[w1] = max(d.get(w1, 1), d.get(w2, 1) + 1)
#                     maxlen = max(maxlen, d[w1])
#
#         return maxlen


# Runtime: 1764 ms, faster than 10.80% of Python3 online submissions for Longest Strings Chain.
# Memory Usage: 14.8 MB, less than 54.22% of Python3 online submissions for Longest Strings Chain.
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        def diff_one_letter(w1: str, w2: str) -> bool:
            n1, n2 = len(w1), len(w2)
            if n2 - 1 != n1:
                return False
            foundDiff = False
            i1, i2 = 0, 0
            while i1 < n1 and i2 < n2:
                if w1[i1] != w2[i2]:
                    if foundDiff:
                        return False
                    foundDiff = True
                    i2 += 1
                else:
                    i1 += 1
                    i2 += 1
            return True

        words.sort(key=lambda w: len(w))

        d = defaultdict(int)

        maxlen = 1
        n = len(words)
        for i1 in range(n):
            w1 = words[i1]
            n1 = len(w1)
            if n1 == 1:
                continue
            for i2 in range(i1-1, -1, -1):
                w2 = words[i2]
                if len(w2) < n1 - 1:
                    break
                if diff_one_letter(w2, w1):
                    d[w1] = max(d.get(w1, 1), d.get(w2, 1) + 1)
                    maxlen = max(maxlen, d[w1])

        return maxlen


tests = [
    [
        ["a","b","ba","bca","bda","bdca"], 4
    ],
    [
        ["xbc","pcxbcf","xb","cxbc","pcxbc"], 5
    ]
]

run_functional_tests(Solution().longestStrChain, tests)