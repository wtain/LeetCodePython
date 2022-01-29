"""
https://leetcode.com/problems/implement-trie-prefix-tree/

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

from Common.Constants import null, true, false
from Common.ObjectTestingUtils import run_object_tests


# Runtime: 188 ms, faster than 59.31% of Python3 online submissions for Implement Trie (Prefix Tree).
# Memory Usage: 32.5 MB, less than 29.66% of Python3 online submissions for Implement Trie (Prefix Tree).
class Trie:

    class Node:

        def __init__(self):
            self.is_end = False
            self.children = dict()

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = self.Node()
            node = node.children[c]
        node.is_end = True

    def searchImpl(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return None
            node = node.children[c]
        return node

    def search(self, word: str) -> bool:
        node = self.searchImpl(word)
        if not node:
            return False
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.searchImpl(prefix)
        if not node:
            return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

tests = [
    [
        ["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
        [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
        [null, null, true, false, true, null, true]
    ]
]

run_object_tests(tests, cls=Trie)