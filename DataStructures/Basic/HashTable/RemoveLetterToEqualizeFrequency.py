"""
https://leetcode.com/problems/remove-letter-to-equalize-frequency/

You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot chose to do nothing.


Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.


Constraints:

2 <= word.length <= 100
word consists of lowercase English letters only.
"""
from collections import Counter
from itertools import count

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         cnt = Counter(word)
#         values = list(cnt.values())
#         vals = set(values)
#         if len(vals) > 2:
#             return False
#         values.sort()
#         if len(vals) == 1:
#             return values[0] == 1
#         cnt2 = Counter(values)
#         if max(vals) == min(vals) + 1 and cnt2[min(vals)] == 1:
#             return True
#         return min(vals) == 1
#         # return max(vals) == min(vals) + 1 or min(vals) == 1 and values[1] != 1


# Runtime
# 57 ms
# Beats
# 47.17%
# Memory
# 13.8 MB
# Beats
# 67.41%
# class Solution:
#     def equalFrequency(self, word: str) -> bool:
#         cnt = Counter(word)
#         if len(cnt.keys()) <= 1:
#             return True
#         values = list(sorted(cnt.values()))
#         distinct_values = set(values)
#         if len(distinct_values) == 1:
#             return distinct_values.pop() == 1
#         cnt2 = Counter(values)
#         if len(distinct_values) > 2:
#             return False
#         if values[0] == 1 and cnt2[values[0]] == 1:
#             return True
#         return values[0] + 1 == values[-1] and cnt2[values[-1]] == 1


# Runtime
# 39 ms
# Beats
# 81.69%
# Memory
# 13.8 MB
# Beats
# 97.84%
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/solutions/2646557/easy-python-solution/
class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i, ch in enumerate(word):
            count = Counter(word[:i] + word[i + 1:])
            s = set(count.values())
            if len(s) == 1:
                return True

        return False


tests = [
    ["aaaabbbbccc", False],
    ["cccd", True],
    ["zz", True],
    ["babbdd", False],
    ["ddaccb", False],
    ["aabbccc", True],
    ["bac", True],
    ["abcc", True],
    ["aazz", False]
]

run_functional_tests(Solution().equalFrequency, tests)
