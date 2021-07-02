"""
https://leetcode.com/problems/merge-strings-alternately/

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.



Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q
merged: a p b q c   d


Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 59.54% of Python3 online submissions for Merge Strings Alternately.
# Memory Usage: 14.2 MB, less than 47.32% of Python3 online submissions for Merge Strings Alternately.
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        words = [word1, word2]
        i = [0, 0]
        n = [len(w) for w in words]
        k = 0
        result = []
        while i[k] < n[k]:
            result.append(words[k][i[k]])
            i[k] += 1
            k = 1 - k
        return "".join(result) + "".join(words[k][i[k]:] for k in range(2))


tests = [
    ["abc", "pqr", "apbqcr"],
    ["ab", "pqrs", "apbqrs"],
    ["abcd", "pq", "apbqcd"]
]

run_functional_tests(Solution().mergeAlternately, tests)