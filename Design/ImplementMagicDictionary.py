"""
https://leetcode.com/problems/implement-magic-dictionary/

Design a data structure that is initialized with a list of different words. Provided a string, you should determine if you can change exactly one character in this string to match any word in the data structure.

Implement the MagicDictionary class:

MagicDictionary() Initializes the object.
void buildDict(String[] dictionary) Sets the data structure with an array of distinct strings dictionary.
bool search(String searchWord) Returns true if you can change exactly one character in searchWord to match any string in the data structure, otherwise returns false.


Example 1:

Input
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
Output
[null, null, false, true, false, false]

Explanation
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // return False
magicDictionary.search("hhllo"); // We can change the second 'h' to 'e' to match "hello" so we return True
magicDictionary.search("hell"); // return False
magicDictionary.search("leetcoded"); // return False


Constraints:

1 <= dictionary.length <= 100
1 <= dictionary[i].length <= 100
dictionary[i] consists of only lower-case English letters.
All the strings in dictionary are distinct.
1 <= searchWord.length <= 100
searchWord consists of only lower-case English letters.
buildDict will be called only once before search.
At most 100 calls will be made to search.
"""
from collections import defaultdict
from functools import reduce
from typing import List

from Common.Constants import null, false, true
from Common.ObjectTestingUtils import run_object_tests


# Runtime
# 219 ms
# Beats
# 82.95%
# Memory
# 16.6 MB
# Beats
# 56.53%
class MagicDictionary:

    def __init__(self):
        self.trie = None

    def buildDict(self, dictionary: List[str]) -> None:
        Trie = lambda: defaultdict(Trie)

        def build_trie(words: List[str]):
            trie = Trie()
            for w in words:
                w += '#'
                reduce(lambda cur, c: cur[c], w, trie)
            return trie

        self.trie = build_trie(dictionary)

    def search(self, searchWord: str) -> bool:
        searchWord += '#'
        nodes = [(self.trie, 0)]
        for c in searchWord:
            next_level = []
            for node, num_errors in nodes:
                if c in node:
                    if c == '#':
                        if num_errors == 1:
                            return True
                    else:
                        next_level.append((node[c], num_errors))
                if num_errors == 0:
                    for child_c in node:
                        if child_c != c:
                            next_level.append((node[child_c], 1))
            nodes = next_level
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)


tests = [
    [
        ["MagicDictionary", "buildDict", "search", "search", "search", "search"],
        [[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
        [null, null, false, true, false, false]
    ],
    [
        ["MagicDictionary", "buildDict", "search", "search", "search", "search"],
        [[], [["hello","hallo","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]],
        [null,null,true,true,false,false]
    ]
]

run_object_tests(tests, cls=MagicDictionary)
