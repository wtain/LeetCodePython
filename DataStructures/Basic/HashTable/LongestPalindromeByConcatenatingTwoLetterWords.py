"""
https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/

You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.



Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".


Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 2966 ms
# Beats
# 54.41%
# Memory
# 38.3 MB
# Beats
# 86.56%
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/2715749/longest-palindrome-by-concatenating-two-letter-words/
# class Solution:
#     def longestPalindrome(self, words: List[str]) -> int:
#         cnt = Counter(words)
#         result, central = 0, False
#         for w, wc in cnt.items():
#             if w[0] == w[1]:
#                 if wc % 2 == 0:
#                     result += wc
#                 else:
#                     result += wc - 1
#                     central = True
#             elif w[0] < w[1]:
#                 result += 2 * min(wc, cnt[w[1] + w[0]])
#         if central:
#             result += 1
#         return 2*result


# Runtime
# 1399 ms
# Beats
# 91.19%
# Memory
# 38.4 MB
# Beats
# 54.38%
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/solutions/2715749/longest-palindrome-by-concatenating-two-letter-words/
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ab_sz = 26
        cnt = [[0 for j in range(ab_sz)] for i in range(ab_sz)]
        for w in words:
            cnt[ord(w[0]) - ord('a')][ord(w[1]) - ord('a')] +=1
        res = 0
        central = False
        for i in range(ab_sz):
            if cnt[i][i] % 2 == 0:
                res += cnt[i][i]
            else:
                res += cnt[i][i] - 1
                central = True
            for j in range(i+1, ab_sz):
                res += 2*min(cnt[i][j], cnt[j][i])
        if central:
            res += 1
        return 2 * res


tests = [
    [["lc","cl","gg"], 6],
    [["ab","ty","yt","lc","cl","ab"], 8],
    [["cc","ll","xx"], 2]
]

run_functional_tests(Solution().longestPalindrome, tests)
