"""
https://leetcode.com/problems/count-prefixes-of-a-given-string/

You are given a string array words and a string s, where words[i] and s comprise only of lowercase English letters.

Return the number of strings in words that are a prefix of s.

A prefix of a string is a substring that occurs at the beginning of the string. A substring is a contiguous sequence of characters within a string.



Example 1:

Input: words = ["a","b","c","ab","bc","abc"], s = "abc"
Output: 3
Explanation:
The strings in words which are a prefix of s = "abc" are:
"a", "ab", and "abc".
Thus the number of strings in words which are a prefix of s is 3.
Example 2:

Input: words = ["a","a"], s = "aa"
Output: 2
Explanation:
Both of the strings are a prefix of s.
Note that the same string can occur multiple times in words, and it should be counted each time.


Constraints:

1 <= words.length <= 1000
1 <= words[i].length, s.length <= 10
words[i] and s consist of lowercase English letters only.
"""
from collections import defaultdict
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 111 ms, faster than 11.71% of Python3 online submissions for Count Prefixes of a Given String.
# Memory Usage: 14.9 MB, less than 8.70% of Python3 online submissions for Count Prefixes of a Given String.
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

        Trie = lambda: [0, defaultdict(Trie)]

        def build_trie(words: List[str]):
            trie = Trie()
            for w in words:
                reduce(lambda cur, c: cur[1][c], w, trie)[0] += 1
            return trie

        trie = build_trie(words)

        result = 0
        current = trie
        for c in s:
            current = current[1][c]
            result += current[0]

        return result


tests = [
    [["gx","v","v","v","sxza","idrt","vo","v","vo","v","v","v","vo","x","v","r","vo","vo","vo","vo","v","vo","v","vo","vo","v","v","vo","v","vo","v","ovc","vo","nsft","v","vo","vo"], "vo", 30],
    [["a","b","c","ab","bc","abc"], "abc", 3],
    [["a","a"], "aa", 2]
]

run_functional_tests(Solution().countPrefixes, tests)
