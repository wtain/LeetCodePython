"""
https://leetcode.com/problems/extra-characters-in-a-string/description/?envType=daily-question&envId=2023-09-02

You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.

Return the minimum number of extra characters left over if you break up s optimally.



Example 1:

Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1 unused character (at index 4), so we return 1.

Example 2:

Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.


Constraints:

1 <= s.length <= 50
1 <= dictionary.length <= 50
1 <= dictionary[i].length <= 50
dictionary[i] and s consists of only lowercase English letters
dictionary contains distinct words
"""
from functools import cache
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 236ms
# Beats 74.60%of users with Python3
# Memory
# Details
# 16.91MB
# Beats 29.89%of users with Python3
# https://leetcode.com/problems/extra-characters-in-a-string/editorial/?envType=daily-question&envId=2023-09-02
# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n, words = len(s), set(dictionary)
#
#         @cache
#         def dp(start):
#             if start == n:
#                 return 0
#             result = dp(start+1) + 1
#             for end in range(start, n):
#                 curr = s[start:end+1]
#                 if curr in words:
#                     result = min(result, dp(end+1))
#             return result
#
#         return dp(0)


# Runtime
# Details
# 224ms
# Beats 80.69%of users with Python3
# Memory
# Details
# 16.44MB
# Beats 66.40%of users with Python3
# # https://leetcode.com/problems/extra-characters-in-a-string/editorial/?envType=daily-question&envId=2023-09-02
# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n, words = len(s), set(dictionary)
#         dp = [0] * (n + 1)
#         for start in range(n-1, -1, -1):
#             dp[start] = 1 + dp[start+1]
#             for end in range(start, n):
#                 curr = s[start:end+1]
#                 if curr in words:
#                     dp[start] = min(dp[start], dp[end+1])
#         return dp[0]


# Runtime
# Details
# 243ms
# Beats 71.96%of users with Python3
# Memory
# Details
# 26.06MB
# Beats 5.55%of users with Python3
# https://leetcode.com/problems/extra-characters-in-a-string/editorial/?envType=daily-question&envId=2023-09-02
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end = False
#
#
# class Solution:
#     def minExtraChar(self, s: str, dictionary: List[str]) -> int:
#         n, root = len(s), self.build_trie(dictionary)
#
#         @cache
#         def dp(start):
#             if start == n:
#                 return 0
#             result = dp(start+1) + 1
#             node = root
#             for end in range(start, n):
#                 if s[end] not in node.children:
#                     break
#                 node = node.children[s[end]]
#                 if node.is_end:
#                     result = min(result, dp(end+1))
#             return result
#
#         return dp(0)
#
#     def build_trie(self, dictionary):
#         root = TrieNode()
#         for word in dictionary:
#             node = root
#             for c in word:
#                 if c not in node.children:
#                     node.children[c] = TrieNode()
#                 node = node.children[c]
#             node.is_end = True
#         return root


# Runtime
# Details
# 182ms
# Beats 94.97%of users with Python3
# Memory
# Details
# 17.43MB
# Beats 17.99%of users with Python3
# https://leetcode.com/problems/extra-characters-in-a-string/editorial/?envType=daily-question&envId=2023-09-02
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n, root = len(s), self.build_trie(dictionary)
        dp = [0] * (n + 1)
        for start in range(n-1, -1, -1):
            dp[start] = 1 + dp[start+1]
            node = root
            for end in range(start, n):
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_end:
                    dp[start] = min(dp[start], dp[end+1])
        return dp[0]

    def build_trie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.is_end = True
        return root


tests = [
    ["leetscode", ["leet","code","leetcode"], 1],
    ["sayhelloworld", ["hello","world"], 3],
]

run_functional_tests(Solution().minExtraChar, tests)
