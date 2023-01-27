"""
https://leetcode.com/problems/concatenated-words/description/

Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.



Example 1:

Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
"dogcatsdog" can be concatenated by "dog", "cats" and "dog";
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
Example 2:

Input: words = ["cat","dog","catdog"]
Output: ["catdog"]


Constraints:

1 <= words.length <= 104
1 <= words[i].length <= 30
words[i] consists of only lowercase English letters.
All the strings of words are unique.
1 <= sum(words[i].length) <= 105
"""
from collections import defaultdict
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         Trie = lambda: defaultdict(Trie)
#
#         def build_trie(words: List[str]):
#             trie = Trie()
#             for w in words:
#                 w += '#'
#                 reduce(lambda cur, c: cur[c], w, trie)
#             return trie
#
#         trie = build_trie(words)
#
#         def is_concatenation(word: str) -> bool:
#             nonlocal trie
#             current1, current2 = trie, trie
#             for c in word:
#                 if '#' in current1:
#                     current1 = trie
#                 if c not in current1:
#                     return False
#                 current1 = current1[c]
#                 current2 = current2[c]
#             return True
#
#         return list(word for word in words if is_concatenation(word))


# Runtime
# 800 ms
# Beats
# 37.94%
# Memory
# 16.6 MB
# Beats
# 98.4%
# https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#         dictionary = set(words)
#         result = []
#         for word in words:
#             n = len(word)
#             dp = [False] * (n+1)
#             dp[0] = True
#             for i in range(1, n+1):
#                 for j in range(1 if i == n else 0, i):
#                     if dp[i]:
#                         break
#                     dp[i] = dp[j] and (word[j:i] in dictionary)
#             if dp[n]:
#                 result.append(word)
#         return result


# Runtime
# 346 ms
# Beats
# 91.66%
# Memory
# 27.6 MB
# Beats
# 47.98%
# https://leetcode.com/problems/concatenated-words/solutions/2822170/concatenated-words/
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        dictionary = set(words)

        def dfs(word: str, n: int, visited: List[bool]) -> bool:
            nonlocal dictionary
            if n == len(word):
                return True
            if visited[n]:
                return False
            visited[n] = True
            for i in range(len(word) - (1 if n == 0 else 0), n, -1):
                if word[n:i] in dictionary and dfs(word, i, visited):
                    return True
            return False

        result = []
        for word in words:
            n = len(word)
            visited = [False] * n
            if dfs(word, 0, visited):
                result.append(word)
        return result


tests = [
    [["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], ["catsdogcats","dogcatsdog","ratcatdogcat"]],
    [["cat","dog","catdog"], ["catdog"]],
]

run_functional_tests(Solution().findAllConcatenatedWordsInADict, tests)
