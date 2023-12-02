"""
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/?envType=daily-question&envId=2023-12-02

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
words[i] and chars consist of lowercase English letters.
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 113
# ms
# Beats
# 69.57%
# of users with Python3
# Memory
# 16.98
# MB
# Beats
# 13.86%
# of users with Python3
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c = Counter(chars)
        result = 0
        for w in words:
            c1 = c.copy()
            add = True
            for ch in w:
                c1[ch] -= 1
                if c1[ch] < 0:
                    add = False
                    break
            if add:
                result += len(w)

        return result


tests = [
    [["cat","bt","hat","tree"], "atach", 6],
    [["hello","world","leetcode"], "welldonehoneyr", 10],
]

run_functional_tests(Solution().countCharacters, tests)
