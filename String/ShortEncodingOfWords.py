"""
https://leetcode.com/explore/featured/card/march-leetcoding-challenge-2021/588/week-1-march-1st-march-7th/3662/
https://leetcode.com/problems/short-encoding-of-words/

A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.



Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
Example 2:

Input: words = ["t"]
Output: 2
Explanation: A valid encoding would be s = "t#" and indices = [0].



Constraints:

1 <= words.length <= 2000
1 <= words[i].length <= 7
words[i] consists of only lowercase letters.
"""
import collections
from functools import reduce
from typing import List


# Runtime: 116 ms, faster than 89.53% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 15.3 MB, less than 51.74% of Python3 online submissions for Short Encoding of Words.
# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         good = set(words)
#         for w in words:
#             for k in range(1, len(w)):
#                 good.discard(w[k:])
#         return sum([len(w)+1 for w in good])

# Runtime: 172 ms, faster than 45.35% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 16.5 MB, less than 33.72% of Python3 online submissions for Short Encoding of Words.
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

        return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)



tests = [
    (["time", "me", "bell"], 10),
    (["t"], 2)
]

for test in tests:
    result = Solution().minimumLengthEncoding(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))