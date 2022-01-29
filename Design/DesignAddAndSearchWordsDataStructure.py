"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.
"""
import collections

from Common.Constants import true, false, null
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 307 ms, faster than 81.24% of Python3 online submissions for Design Add and Search Words Data Structure.
# Memory Usage: 25.8 MB, less than 62.21% of Python3 online submissions for Design Add and Search Words Data Structure.
class WordDictionary:

    def __init__(self):
        Trie = lambda: collections.defaultdict(Trie)
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        word += '#'
        cur = self.trie
        for c in word:
            cur = cur[c]

    def search(self, word: str) -> bool:
        word += '#'
        to_visit = [self.trie]
        for c in word:
            next_level = []
            if c == '.':
                for node in to_visit:
                    for child in node:
                        next_level.append(node[child])
            else:
                for node in to_visit:
                    if c in node:
                        next_level.append(node[c])
            if not next_level:
                return False
            to_visit = next_level
        return True

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


tests = [
    [
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]],
        [null,null,null,null,false,true,true,true]
    ]
]

run_object_tests(tests, cls=WordDictionary)
