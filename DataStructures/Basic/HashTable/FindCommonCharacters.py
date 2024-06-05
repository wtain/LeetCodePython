"""
https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.



Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 100
words[i] consists of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 45
# ms
# Beats
# 80.00%
# of users with Python3
# Memory
# 16.61
# MB
# Beats
# 67.21%
# of users with Python3
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        cnt = Counter(words[0])
        for i in range(1, n):
            c1 = Counter(words[i])
            for c in cnt.keys():
                cnt[c] = min(cnt[c], c1[c])
        result = []
        for c in cnt.keys():
            for i in range(cnt[c]):
                result.append(c)
        return result


tests = [
    [["bella","label","roller"], ["e","l","l"]],
    [["cool","lock","cook"], ["c","o"]],
]

run_functional_tests(Solution().commonChars, tests)
