"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/
https://leetcode.com/problems/prefix-and-suffix-search/

Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.

Implement the WordFilter class:

WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.


Example 1:

Input
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
Output
[null, 0]

Explanation
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".


Constraints:

1 <= words.length <= 15000
1 <= words[i].length <= 10
1 <= prefix.length, suffix.length <= 10
words[i], prefix and suffix consist of lower-case English letters only.
At most 15000 calls will be made to the function f.
"""
import collections
from typing import List

from Common.Constants import null
from Common.ObjectTestingUtils import run_object_tests


# words = list(set(words))
# Trie = lambda: collections.defaultdict(Trie)
# trie = Trie()
#
# self.nodes1 = [reduce(dict.__getitem__, word, trie) for word in words]
# self.nodes2 = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

# TLE
# class WordFilter:
#
#     # class Trie:
#     #
#     #     def __init__(self):
#     #         self.nodes = collections.defaultdict()
#     #
#     #     def add(self, word: str):
#
#     def __init__(self, words: List[str]):
#         Trie = lambda: [collections.defaultdict(Trie), set()]
#         self.trie1 = Trie()
#         self.trie2 = Trie()
#         self.words = words
#
#         # def step(trie, i : int):
#         #     node, l = trie
#         #     child, lc = node.get(c)
#         #
#         # self.nodes1 = [reduce(dict.__getitem__, word, self.trie1) for word in words]
#         # self.nodes2 = [reduce(dict.__getitem__, word[::-1], self.trie2) for word in words]
#
#         for index, word in enumerate(words):
#             n1, s1 = self.trie1
#             for c in word:
#                 n1, s1 = n1[c]
#                 s1.add(index)
#             n2, s2 = self.trie2
#             for c in word[::-1]:
#                 n2, s2 = n2[c]
#                 s2.add(index)
#
#
#     def f(self, prefix: str, suffix: str) -> int:
#
#
#         n1, s1 = self.trie1
#         for c in prefix:
#             n1, s1 = n1[c]
#             if not s1:
#                 return -1
#
#         n2, s2 = self.trie2
#         for c in suffix[::-1]:
#             n2, s2 = n2[c]
#             if not s2:
#                 return -1
#
#         if s1 and s2:
#             idx = s1.intersection(s2)
#         elif s1:
#             idx = s1
#         else:
#             idx = s2
#
#         maxi = -1
#         maxword = ""
#         for i in idx:
#             if self.words[i] > maxword:
#                 maxword = self.words[i]
#                 maxi = i
#
#         return maxi


# Runtime: 968 ms, faster than 44.08% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 69.6 MB, less than 28.29% of Python3 online submissions for Prefix and Suffix Search.
# class WordFilter:
#
#     def __init__(self, words: List[str]):
#         Trie = lambda: collections.defaultdict(Trie)
#         self.trie = Trie()
#
#         for index, word in enumerate(words):
#             cur = self.trie
#             cur[0] = index
#             for i, c in enumerate(word):
#                 tmp = cur
#                 for d in word[i:]:
#                     tmp = tmp[d, None]
#                     tmp[0] = index
#                 tmp = cur
#                 for d in word[:-i or None][::-1]:
#                     tmp = tmp[None, d]
#                     tmp[0] = index
#
#                 cur = cur[c, word[~i]]
#                 cur[0] = index
#
#     def f(self, prefix: str, suffix: str) -> int:
#         cur = self.trie
#         n1, n2 = len(prefix), len(suffix)
#         n = max(n1, n2)
#         for i in range(n):
#             a = prefix[i] if i < n1 else None
#             b = suffix[~i] if i < n2 else None
#             if (a, b) not in cur:
#                 return -1
#             cur = cur[a, b]
#         return cur[0]


# Runtime: 876 ms, faster than 61.84% of Python3 online submissions for Prefix and Suffix Search.
# Memory Usage: 60.7 MB, less than 40.79% of Python3 online submissions for Prefix and Suffix Search.
class WordFilter:

    def __init__(self, words: List[str]):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

        for index, word in enumerate(words):
            word += "#"
            for i in range(len(word)):
                cur = self.trie
                cur[0] = index
                for j in range(i, 2 * len(word) - 1):
                    cur = cur[word[j % len(word)]]
                    cur[0] = index

    def f(self, prefix: str, suffix: str) -> int:
        cur = self.trie
        for l in suffix + "#" + prefix:
            if l not in cur:
                return -1
            cur = cur[l]
        return cur[0]

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)


tests = [
    [
        ["WordFilter","f","f","f","f","f","f","f","f","f","f"],
        [[
            ["cabaabaaaa","ccbcababac","bacaabccba","bcbbcbacaa","abcaccbcaa",
             "accabaccaa","cabcbbbcca","ababccabcb","caccbbcbab","bccbacbcba"]],
            ["bccbacbcba","a"],["ab","abcaccbcaa"],["a","aa"],["cabaaba","abaaaa"],
            ["cacc","accbbcbab"],["ccbcab","bac"],["bac","cba"],["ac","accabaccaa"],["bcbb","aa"],["ccbca","cbcababac"]],
        [null,9,4,5,0,8,1,2,5,3,1]
    ],
    [
        ["WordFilter", "f"],
        [[["apple"]], ["a", "e"]],
        [null, 0]
    ]
]

run_object_tests(tests, cls=WordFilter)