"""
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

With respect to a given puzzle string, a word is valid if both the following conditions are satisfied:
word contains the first letter of puzzle.
For each letter in word, that letter is in puzzle.
For example, if the puzzle is "abcdefg", then valid words are "faced", "cabbage", and "baggage", while
invalid words are "beefed" (does not include 'a') and "based" (includes 's' which is not in the puzzle).
Return an array answer, where answer[i] is the number of words in the given word list words that is valid with respect to the puzzle puzzles[i].


Example 1:

Input: words = ["aaaa","asas","able","ability","actt","actor","access"], puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
Output: [1,1,3,2,4,0]
Explanation:
1 valid word for "aboveyz" : "aaaa"
1 valid word for "abrodyz" : "aaaa"
3 valid words for "abslute" : "aaaa", "asas", "able"
2 valid words for "absoryz" : "aaaa", "asas"
4 valid words for "actresz" : "aaaa", "asas", "actt", "access"
There are no valid words for "gaswxyz" cause none of the words in the list contains letter 'g'.
Example 2:

Input: words = ["apple","pleas","please"], puzzles = ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"]
Output: [0,1,3,2,0]


Constraints:

1 <= words.length <= 105
4 <= words[i].length <= 50
1 <= puzzles.length <= 104
puzzles[i].length == 7
words[i] and puzzles[i] consist of lowercase English letters.
Each puzzles[i] does not contain repeated characters.
"""
from collections import defaultdict, Counter
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# NAIVE
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         n, m = len(words), len(puzzles)
#         result = [0] * m
#         for j in range(m):
#             puzzle = puzzles[j]
#             for w in words:
#                 if puzzle[0] not in w:
#                     continue
#                 f = True
#                 for c in w:
#                     if c not in puzzle:
#                         f = False
#                         break
#                 if f:
#                     result[j] += 1
#         return result

# IMPROVED
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         n, m = len(words), len(puzzles)
#         result = [0] * m
#         for j in range(m):
#             puzzle = puzzles[j]
#             letters = [False] * 26
#             for c in puzzle:
#                 letters[ord(c) - ord('a')] = True
#             for w in words:
#                 if puzzle[0] not in w:
#                     continue
#                 f = True
#                 for c in w:
#                     if not letters[ord(c) - ord('a')]:
#                         f = False
#                         break
#                 if f:
#                     result[j] += 1
#         return result


# Runtime: 6848 ms, faster than 5.66% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# Memory Usage: 141.2 MB, less than 5.66% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         n, m = len(words), len(puzzles)
#         result = [0] * m
#         Trie = lambda: [0, defaultdict(Trie)]
#
#         def build_trie(words: List[str]):
#             trie = Trie()
#             for w in words:
#                 w += '#'
#                 cur = trie
#                 for c in w:
#                     cur = cur[1][c]
#                 cur[0] += 1
#             return trie
#
#         trie = build_trie(words)
#
#         for j in range(m):
#             puzzle = puzzles[j]
#             letters = [False] * 26
#             for c in puzzle:
#                 letters[ord(c) - ord('a')] = True
#             to_visit = [(trie, False)]
#             while to_visit:
#                 node, found_first = to_visit.pop()
#                 for c in node[1]:
#                     if c == '#':
#                         if found_first:
#                             result[j] += node[1]['#'][0]
#                     elif letters[ord(c) - ord('a')]:
#                         to_visit.append((node[1][c], found_first or c == puzzle[0]))
#         return result


# Runtime: 524 ms, faster than 94.34% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# Memory Usage: 47.9 MB, less than 50.94% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/solution/
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         def build_bitmask(w: str) -> int:
#             return reduce(lambda bm, c: bm | (1 << (ord(c) - ord('a'))), w, 0)
#
#         def build_map(words: List[str]):
#             res = defaultdict(int)
#             for w in words:
#                 res[build_bitmask(w)] += 1
#             return res
#
#         mp = build_map(words)
#         result = []
#         for j, puzzle in enumerate(puzzles):
#             first = 1 << (ord(puzzle[0]) - ord('a'))
#             cnt = mp[first]
#             mask = build_bitmask(puzzle[1:])
#             submask = mask
#             while submask:
#                 cnt += mp[submask | first]
#                 submask = (submask - 1) & mask
#             result.append(cnt)
#
#         return result


# Runtime: 1880 ms, faster than 18.87% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# Memory Usage: 91.2 MB, less than 5.66% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# class Solution:
#     def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
#         n, m = len(words), len(puzzles)
#         result = [0] * m
#         Trie = lambda: [0, defaultdict(Trie)]
#
#         def build_trie(words: List[str]):
#             trie = Trie()
#             for w in words:
#                 w = sorted(set(w))
#                 w += '#'
#                 cur = trie
#                 for c in w:
#                     cur = cur[1][c]
#                 cur[0] += 1
#             return trie
#
#         trie = build_trie(words)
#
#         for j in range(m):
#             puzzle = puzzles[j]
#             letters = [False] * 26
#             for c in puzzle:
#                 letters[ord(c) - ord('a')] = True
#             to_visit = [(trie, False)]
#             while to_visit:
#                 node, found_first = to_visit.pop()
#                 for c in node[1]:
#                     if c == '#':
#                         if found_first:
#                             result[j] += node[1]['#'][0]
#                     elif letters[ord(c) - ord('a')]:
#                         to_visit.append((node[1][c], found_first or c == puzzle[0]))
#         return result

# Runtime: 1868 ms, faster than 19.81% of Python3 online submissions for Number of Valid Words for Each Puzzle.
# Memory Usage: 91 MB, less than 5.66% of Python3 online submissions for Number of Valid Words for Each Puzzle.
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        n, m = len(words), len(puzzles)
        result = [0] * m
        Trie = lambda: [0, defaultdict(Trie)]

        def build_trie(words: List[str]):
            trie = Trie()
            for w in words:
                w = sorted(set(w))
                if len(w) > 7:
                    continue
                w += '#'
                reduce(lambda cur, c: cur[1][c], w, trie)[0] += 1
            return trie

        trie = build_trie(words)

        for j in range(m):
            puzzle = puzzles[j]
            letters = [False] * 26
            for c in puzzle:
                letters[ord(c) - ord('a')] = True
            to_visit = [(trie, False)]
            while to_visit:
                node, found_first = to_visit.pop()
                for c in node[1]:
                    if c == '#':
                        if found_first:
                            result[j] += node[1]['#'][0]
                    elif letters[ord(c) - ord('a')]:
                        to_visit.append((node[1][c], found_first or c == puzzle[0]))
        return result


tests = [
    [
        ["aaaa","asas","able","ability","actt","actor","access"],
        ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"],
        [1,1,3,2,4,0]
    ],
    [
        ["apple","pleas","please"],
        ["aelwxyz","aelpxyz","aelpsxy","saelpxy","xaelpsy"],
        [0,1,3,2,0]
    ],

    [
        ["kkaz","kaaz","aazk","aaaz","abcdefghijklmnopqrstuvwxyz","kkka","kkkz","aaaa","kkkk","zzzz"],
        ["kazxyuv"],
        [6]
    ]
]

run_functional_tests(Solution().findNumOfValidWords, tests)
