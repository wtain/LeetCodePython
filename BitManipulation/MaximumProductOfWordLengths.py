"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3757/
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.



Example 1:

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.


Constraints:

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] consists only of lowercase English letters.
"""
from collections import defaultdict
from itertools import combinations
from typing import List, Set

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 2468 ms, faster than 28.24% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 15.2 MB, less than 24.63% of Python3 online submissions for Maximum Product of Word Lengths.
# class Solution:
#     def maxProduct(self, words: List[str]) -> int:
#         max_p = 0
#         n = len(words)
#         dic = defaultdict(lambda: set())
#         for i in range(n):
#             for c in words[i]:
#                 dic[c].add(i)
#         for i in range(n):
#             for j in range(i+1, n):
#                 if not any(j in dic[c] for c in words[i]):
#                     max_p = max(max_p, len(words[i]) * len(words[j]))
#         return max_p


# Runtime: 488 ms, faster than 67.49% of Python3 online submissions for Maximum Product of Word Lengths.
# Memory Usage: 14.4 MB, less than 96.88% of Python3 online submissions for Maximum Product of Word Lengths.
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res, dic = 0, defaultdict(int)
        for w in words:
            for c in w:
                dic[w] |= 1 << (ord(c) - ord('a'))
        for w1, w2 in combinations(dic.keys(), 2):
            if dic[w1] & dic[w2] == 0:
                res = max(res, len(w1)*len(w2))
        return res


tests = [
    [["abcw","baz","foo","bar","xtfn","abcdef"], 16],
    [["a","ab","abc","d","cd","bcd","abcd"], 4],
    [["a","aa","aaa","aaaa"], 0]
]

run_functional_tests(Solution().maxProduct, tests)