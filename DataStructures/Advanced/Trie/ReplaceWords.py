"""
https://leetcode.com/problems/replace-words/

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word successor. For example, when the root "an" is followed by the successor word "other", we can form a new word "another".

Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, replace it with the root that has the shortest length.

Return the sentence after the replacement.



Example 1:

Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"
Example 2:

Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"


Constraints:

1 <= dictionary.length <= 1000
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case letters.
1 <= sentence.length <= 106
sentence consists of only lower-case letters and spaces.
The number of words in sentence is in the range [1, 1000]
The length of each word in sentence is in the range [1, 1000]
Every two consecutive words in sentence will be separated by exactly one space.
sentence does not have leading or trailing spaces.
"""
import collections
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 122 ms
# Beats
# 95.80%
# Memory
# 29.2 MB
# Beats
# 46.55%
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        Trie = lambda: collections.defaultdict(Trie)

        trie = Trie()
        for word in dictionary:
            word += '#'
            reduce(lambda cur, c: cur[c], word, trie)

        def get_shortest(word: str) -> str:
            nonlocal trie
            cur = trie
            path = ""
            for c in word:
                if '#' in cur:
                    return path
                path += c
                if c not in cur:
                    return word
                cur = cur[c]
            return path

        return " ".join(get_shortest(w) for w in sentence.split(" "))


tests = [
    [["cat","bat","rat"], "the cattle was rattled by the battery", "the cat was rat by the bat"],
    [["a","b","c"], "aadsfasf absbs bbab cadsfafs", "a a b c"]
]

run_functional_tests(Solution().replaceWords, tests)
