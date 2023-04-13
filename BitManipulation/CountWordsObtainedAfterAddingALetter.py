"""
https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/

You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.



Example 1:

Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
Explanation:
- In order to form targetWords[0] = "tack", we use startWords[1] = "act", append 'k' to it, and rearrange "actk" to "tack".
- There is no string in startWords that can be used to obtain targetWords[1] = "act".
  Note that "act" does exist in startWords, but we must append one letter to the string before rearranging it.
- In order to form targetWords[2] = "acti", we use startWords[1] = "act", append 'i' to it, and rearrange "acti" to "acti" itself.
Example 2:

Input: startWords = ["ab","a"], targetWords = ["abc","abcd"]
Output: 1
Explanation:
- In order to form targetWords[0] = "abc", we use startWords[0] = "ab", add 'c' to it, and rearrange it to "abc".
- There is no string in startWords that can be used to obtain targetWords[1] = "abcd".


Constraints:

1 <= startWords.length, targetWords.length <= 5 * 104
1 <= startWords[i].length, targetWords[j].length <= 26
Each string of startWords and targetWords consists of lowercase English letters only.
No letter occurs more than once in any string of startWords or targetWords.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
#
#         def map_word(w: str) -> int:
#             mask = 0
#             for c in w:
#                 mask |= 1 << (ord(c) - ord('a'))
#             return mask
#
#         def is_power2(n: int) -> bool:
#             return n > 0 and n & (n - 1) == 0
#
#         def mask_includes(m, mask):
#             return m > mask and is_power2(m ^ mask)
#
#         result = 0
#         masks = list(map(map_word, targetWords))
#         for m in masks:
#             for word in startWords:
#                 mask = map_word(word)
#                 if m == mask:
#                     continue
#                 if mask_includes(m, mask):
#                     result += 1
#                     break
#
#         return result

# TLE
# class Solution:
#     def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
#
#         def map_word(w: str) -> int:
#             mask = 0
#             for c in w:
#                 mask |= 1 << (ord(c) - ord('a'))
#             return mask
#
#         def is_power2(n: int) -> bool:
#             return n > 0 and n & (n - 1) == 0
#
#         def mask_includes(m, mask):
#             return m > mask and is_power2(m ^ mask)
#
#         result = 0
#         ms = list(map(map_word, startWords))
#         for target in targetWords:
#             m = map_word(target)
#             for mask in ms:
#                 if mask_includes(m, mask):
#                     result += 1
#                     break
#
#         return result


# Runtime
# 1346 ms
# Beats
# 37.58%
# Memory
# 34.2 MB
# Beats
# 43.31%
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:

        def map_word(w: str) -> int:
            mask = 0
            for c in w:
                mask |= 1 << (ord(c) - ord('a'))
            return mask

        result = 0
        ms = set(map(map_word, startWords))
        for target in targetWords:
            m = map_word(target)
            for i in range(26):
                bit = 1 << i
                if bit & m:
                    m1 = m ^ bit
                    if m1 in ms:
                        result += 1
                        break

        return result


tests = [
    [["ant","act","tack"], ["tack","act","acti"], 2],
    [["ab","a"], ["abc","abcd"], 1],
]

run_functional_tests(Solution().wordCount, tests)
