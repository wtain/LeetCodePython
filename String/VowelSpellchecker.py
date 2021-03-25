"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/591/week-4-march-22nd-march-28th/3681/
https://leetcode.com/problems/vowel-spellchecker/

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].



Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]


Note:

1 <= wordlist.length <= 5000
1 <= queries.length <= 5000
1 <= wordlist[i].length <= 7
1 <= queries[i].length <= 7
All strings in wordlist and queries consist only of english letters.
"""
import collections
import functools
import itertools
from functools import reduce
from typing import List, Tuple

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 300 ms, faster than 16.73% of Python3 online submissions for Vowel Spellchecker.
# Memory Usage: 31 MB, less than 5.71% of Python3 online submissions for Vowel Spellchecker.
# class Solution:
#     def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
#         result = []
#
#         def is_vowel(c: chr) -> bool:
#             return c in {'a', 'e', 'i', 'o', 'u'}
#
#         def build_trie(wordlist: List[str]):
#             Trie = lambda: (collections.defaultdict(Trie), [])
#             trie = Trie()
#
#             # nodes = [reduce(dict.__getitem__, word[1], trie) for word in wordlist]
#             for word in wordlist:
#                 curr = trie
#                 for c in word:
#                     c = str.lower(c)
#                     if is_vowel(c):
#                         c = '*'
#                     curr = curr[0][c]
#                 curr[1].append(word)
#
#             return trie
#
#         trie = build_trie(wordlist)
#
#         def check(word: str) -> str:
#             nonlocal wordlist, trie
#             curr = trie
#             for c in word:
#                 c = str.lower(c)
#                 if is_vowel(c):
#                     c = '*'
#                 curr = curr[0][c]
#             for ww in curr[1]:
#                 if ww == word:
#                     return ww
#             for ww in curr[1]:
#                 if str.lower(ww) == str.lower(word):
#                     return ww
#             if len(curr[1]) > 0:
#                 return curr[1][0]
#             return ""
#
#         for word in queries:
#             result.append(check(word))
#
#         return result


# Runtime: 176 ms, faster than 80.00% of Python3 online submissions for Vowel Spellchecker.
# Memory Usage: 16.9 MB, less than 73.06% of Python3 online submissions for Vowel Spellchecker.
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def devowel(w: str) -> str:
            return "".join('*' if c in 'aeiou' else c for c in w)

        words_base = set(wordlist)
        words1 = {}
        words2 = {}

        for w in wordlist:
            wl = w.lower()
            words1.setdefault(wl, w)
            words2.setdefault(devowel(wl), w)

        def solve(q: str) -> str:
            if q in words_base:
                return q
            ql = q.lower()
            if ql in words1:
                return words1[ql]
            qlv = devowel(ql)
            if qlv in words2:
                return words2[qlv]
            return ""

        # return map(solve, queries)
        return [solve(q) for q in queries]


# Runtime: 172 ms, faster than 86.94% of Python3 online submissions for Vowel Spellchecker.
# Memory Usage: 18.6 MB, less than 10.61% of Python3 online submissions for Vowel Spellchecker.
# class Solution:
#     def spellchecker(self, wordlist: List[str], queries: List[str]):
#         def devowel(w: str) -> str:
#             return "".join('*' if c in 'aeiou' else c for c in w)
#
#         words_base = set(wordlist)
#         words1 = {}
#         words2 = {}
#
#         for w in wordlist:
#             wl = w.lower()
#             words1.setdefault(wl, w)
#             words2.setdefault(devowel(wl), w)
#
#         def solve(q):
#             if q in words_base:
#                 return q
#             ql = q.lower()
#             if ql in words1:
#                 return words1[ql]
#             qlv = devowel(ql)
#             if qlv in words2:
#                 return words2[qlv]
#             return ""
#
#         return map(solve, queries)


tests = [
    (["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"], ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"])
]

run_functional_tests(Solution().spellchecker, tests);