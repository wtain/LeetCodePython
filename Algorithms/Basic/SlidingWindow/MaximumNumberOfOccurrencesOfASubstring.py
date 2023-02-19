"""
https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.


Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.


Constraints:

1 <= s.length <= 105
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s consists of only lowercase English letters.
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2113 ms
# Beats
# 19.49%
# Memory
# 30.7 MB
# Beats
# 27.67%
# class Solution:
#     def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#
#         def get_number_of_substrings(size: int) -> int:
#             substring_counts = defaultdict(int)
#             char_counts = defaultdict(int)
#             for c in s[:size]:
#                 char_counts[c] += 1
#             if len(char_counts) <= maxLetters:
#                 substring_counts[s[:size]] += 1
#             i1, i2 = 0, size
#             while i2 < len(s):
#                 char_counts[s[i1]] -= 1
#                 if not char_counts[s[i1]]:
#                     del char_counts[s[i1]]
#                 char_counts[s[i2]] += 1
#                 i1 += 1
#                 i2 += 1
#                 if len(char_counts) <= maxLetters:
#                     substring_counts[s[i1:i2]] += 1
#             if not substring_counts:
#                 return 0
#             return max(substring_counts[ss] for ss in substring_counts)
#
#         result = 0
#         for size in range(minSize, maxSize+1):
#             result = max(result, get_number_of_substrings(size))
#
#         return result


# Runtime
# 182 ms
# Beats
# 72.96%
# Memory
# 16.2 MB
# Beats
# 71.38%
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        result = 0
        substring_counts = defaultdict(int)
        char_counts = defaultdict(int)
        for c in s[:minSize]:
            char_counts[c] += 1
        if len(char_counts) <= maxLetters:
            substring_counts[s[:minSize]] += 1
        i1, i2 = 0, minSize
        while i2 < len(s):
            char_counts[s[i1]] -= 1
            if not char_counts[s[i1]]:
                del char_counts[s[i1]]
            char_counts[s[i2]] += 1
            i1 += 1
            i2 += 1
            if len(char_counts) <= maxLetters:
                substring_counts[s[i1:i2]] += 1
        if substring_counts:
            result = max(result, max(substring_counts[ss] for ss in substring_counts))

        return result


tests = [
    ["abcde", 2, 3, 3, 0],
    ["aababcaab", 2, 3, 4, 2],
    ["aaaa", 1, 3, 3, 2],
]

run_functional_tests(Solution().maxFreq, tests)
