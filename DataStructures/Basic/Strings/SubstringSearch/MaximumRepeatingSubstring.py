"""
https://leetcode.com/problems/maximum-repeating-substring/

For a string sequence, a string word is k-repeating if word concatenated k times is a substring of sequence. The word's maximum k-repeating value is the highest value k where word is k-repeating in sequence. If word is not a substring of sequence, word's maximum k-repeating value is 0.

Given strings sequence and word, return the maximum k-repeating value of word in sequence.



Example 1:

Input: sequence = "ababc", word = "ab"
Output: 2
Explanation: "abab" is a substring in "ababc".
Example 2:

Input: sequence = "ababc", word = "ba"
Output: 1
Explanation: "ba" is a substring in "ababc". "baba" is not a substring in "ababc".
Example 3:

Input: sequence = "ababc", word = "ac"
Output: 0
Explanation: "ac" is not a substring in "ababc".


Constraints:

1 <= sequence.length <= 100
1 <= word.length <= 100
sequence and word contains only lowercase English letters.
"""

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         i, k, n = 0, len(word), len(sequence)
#         res = 0
#         while i < n:
#             j = sequence.find(word, i)
#             if j == -1:
#                 break
#             cnt = 1
#             j += k
#             while j+k < n and sequence[j:j+k] == word:
#                 j += k
#                 cnt += 1
#             res = max(res, cnt)
#             i = j - (k-1)
#         return res

####
# class Solution:
#
#     def prefix(self, s: str) -> List[int]:
#         n = len(s)
#         p = [0] * n
#         for i in range(1, n):
#             k = p[i-1]
#             while k > 0 and s[k] != s[i]:
#                 k = p[k - 1]
#             if s[k] == s[i]:
#                 k += 1
#             p[i] = k
#         return p
#
#     def maxRepeating(self, sequence: str, word: str) -> int:
#         p = self.prefix(word)
#         i, k, n = 0, len(word), len(sequence)
#         res = 0
#         while i < n:
#             j = sequence.find(word, i)
#             if j == -1:
#                 break
#             cnt = 1
#             j += k
#             while j+k < n and sequence[j:j+k] == word:
#                 j += k
#                 cnt += 1
#             res = max(res, cnt)
#             i = j - (k-1)
#         return res


# Runtime: 32 ms, faster than 61.99% of Python3 online submissions for Maximum Repeating Substring.
# Memory Usage: 14.2 MB, less than 71.09% of Python3 online submissions for Maximum Repeating Substring.
class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        k, n = len(word), len(sequence)
        m = n // k
        for i in range(m, 0, -1):
            p = word * i
            if p in sequence:
                return i
        return 0


tests = [
    ["aaabaaaabaaabaaaabaaaabaaaabaaaaba", "aaaba", 5],
    ["ababc", "ab", 2],
    ["ababc", "ba", 1],
    ["ababc", "ac", 0]
]

run_functional_tests(Solution().maxRepeating, tests)