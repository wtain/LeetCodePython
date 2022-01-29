"""
https://leetcode.com/problems/word-search-ii/

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


# Runtime: 4444 ms, faster than 64.06% of Python3 online submissions for Word Search II.
# Memory Usage: 14.8 MB, less than 18.18% of Python3 online submissions for Word Search II.
class Solution:
    class Trie:

        class Node:

            def __init__(self):
                self.is_end = False
                self.children = dict()

            def getChild(self, c: chr):
                if c in self.children:
                    return self.children[c]
                return None

        def __init__(self):
            self.root = Solution.Trie.Node()

        def insertWords(self, words: List[str]):
            for w in words:
                self.insert(w)

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

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        h, w = len(board), len(board[0])
        visited = [[False] * w for _ in range(h)]
        trie = Solution.Trie()
        found = set()

        def match(i: int, j: int, word: str, root: Solution.Trie.Node):
            nonlocal h, w, visited, trie, words, board, found
            if i < 0 or j < 0 or i >= h or j >= w:
                return
            if visited[i][j]:
                return
            cnode = root.getChild(board[i][j])
            if not cnode:
                return
            newword = word + board[i][j]
            if cnode.is_end:
                found.add(newword)
            visited[i][j] = True
            match(i - 1, j, newword, cnode)
            match(i + 1, j, newword, cnode)
            match(i, j - 1, newword, cnode)
            match(i, j + 1, newword, cnode)
            visited[i][j] = False


        trie.insertWords(words)
        for i in range(h):
            for j in range(w):
                match(i, j, "", trie.root)
                if len(found) == len(words):
                    break
            if len(found) == len(words):
                break

        return found


tests = [
    [
        [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]],
        ["oa","oaa"],
        ["oa","oaa"]
    ],
    [
        [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        ["oath","pea","eat","rain"],
        ["eat","oath"]
    ],
    [
        [["a","b"],["c","d"]],
        ["abcb"],
        []
    ]
]

run_functional_tests(Solution().findWords, tests, custom_check=compareSets)