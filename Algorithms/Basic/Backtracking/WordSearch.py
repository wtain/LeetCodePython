"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.



Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false


Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


Follow up: Could you use search pruning to make your solution faster with a larger board?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 5604 ms, faster than 80.10% of Python3 online submissions for Word Search.
# Memory Usage: 14.5 MB, less than 11.68% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        h, w = len(board), len(board[0])
        visited = [[False] * w for _ in range(h)]

        def match(i: int, j: int, startIndex: int) -> bool:
            nonlocal board, visited, h, w, word
            if startIndex == len(word):
                return True
            if i < 0 or j < 0 or i >= h or j >= w:
                return False
            if visited[i][j]:
                return False
            if word[startIndex] != board[i][j]:
                return False
            if startIndex+1 == len(word):
                return True
            visited[i][j] = True
            if match(i-1, j, startIndex+1) or \
               match(i+1, j, startIndex+1) or \
               match(i, j-1, startIndex+1) or \
               match(i, j+1, startIndex+1):
                return True
            visited[i][j] = False
            return False

        for i in range(h):
            for j in range(w):
                if match(i, j, 0):
                    return True

        return False


tests = [
    [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED", True],
    [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE", True],
    [[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB", False]
]

run_functional_tests(Solution().exist, tests)