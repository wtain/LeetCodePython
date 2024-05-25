"""
https://leetcode.com/problems/word-break-ii/description/?envType=daily-question&envId=2024-05-25

Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.



Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []


Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
"""
from functools import cache
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 36
# ms
# Beats
# 47.42%
# of users with Python3
# Memory
# 16.48
# MB
# Beats
# 87.62%
# of users with Python3
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#
#         @cache
#         def impl(s1):
#             n = len(s1)
#             if not n:
#                 return [""]
#             result = []
#             c = ""
#             for i in range(n):
#                 c += s1[i]
#                 if c in wordDict:
#                     r = impl(s1[i+1:])
#                     for ri in r:
#                         r1 = c
#                         if ri:
#                             r1 += " " + ri
#                         result.append(r1)
#             return result
#
#         return impl(s)


# Runtime
# 39
# ms
# Beats
# 26.33%
# of users with Python3
# Memory
# 16.47
# MB
# Beats
# 87.62%
# of users with Python3
# https://leetcode.com/problems/word-break-ii/editorial/?envType=daily-question&envId=2024-05-25
# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
#         dp = {}
#
#         for start_idx in range(len(s), -1, -1):
#             valid_sentences = []
#             for end_idx in range(start_idx, len(s)):
#                 current_word = s[start_idx:end_idx+1]
#
#                 if current_word in wordDict:
#                     if end_idx == len(s) - 1:
#                         valid_sentences.append(current_word)
#                     else:
#                         sentences_from_index = dp.get(end_idx+1, [])
#                         for sentence in sentences_from_index:
#                             valid_sentences.append(current_word + " " + sentence)
#             dp[start_idx] = valid_sentences
#
#         return dp.get(0, [])


# Runtime
# 23
# ms
# Beats
# 98.55%
# of users with Python3
# Memory
# 16.42
# MB
# Beats
# 87.62%
# of users with Python3
# https://leetcode.com/problems/word-break-ii/submissions/1267395716/?envType=daily-question&envId=2024-05-25
class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [None] * 26

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord('a')
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
        dp = {}
        for start_idx in range(len(s), -1, -1):
            valid_sentences = []

            current_node = trie.root

            for end_idx in range(start_idx, len(s)):
                char = s[end_idx]
                index = ord(char) - ord('a')

                if not current_node.children[index]:
                    break

                current_node = current_node.children[index]

                if current_node.is_end:
                    current_word = s[start_idx:end_idx+1]
                    if end_idx == len(s) - 1:
                        valid_sentences.append(current_word)
                    else:
                        sentences_from_index = dp.get(end_idx+1, [])
                        for sentence in sentences_from_index:
                            valid_sentences.append(current_word + " " + sentence)
            dp[start_idx] = valid_sentences

        return dp.get(0, [])


tests = [
    ["catsanddog", ["cat","cats","and","sand","dog"], ["cats and dog","cat sand dog"]],
    ["pineapplepenapple", ["apple","pen","applepen","pine","pineapple"], ["pine apple pen apple","pineapple pen apple","pine applepen apple"]],
    ["catsandog", ["cats","dog","sand","and","cat"], []],
]

run_functional_tests(Solution().wordBreak, tests, custom_check=compareSets)
