"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/611/week-4-july-22nd-july-28th/3825/
https://leetcode.com/problems/word-ladder-ii/

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 1000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
"""
import collections
import math
from functools import lru_cache
from typing import List, Set

from Common.ObjectTestingUtils import run_functional_tests
from Common.ResultComparators import compareSets


# WRONG
# def decode(v, M) -> str:
#     result = []
#     while v:
#         result.append(v % M)
#         v //= M
#     return ",".join(str(c) for c in result[::-1])
#
#
#
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         if endWord not in wordList:
#             return []
#         self.L = len(beginWord)
#         self.allWords = collections.defaultdict(list)
#         self.M = len(wordList) + 1
#         for j, w in enumerate(wordList):
#             for i in range(self.L):
#                 int_w = w[:i] + "*" + w[i + 1:]
#                 self.allWords[int_w].append((j, w))
#
#         mindist = math.inf
#         result = []
#         do_continue = True
#         codes_added = set()
#
#         def reverse_code(code: int) -> int:
#             result = 0
#             while code:
#                 d = code % self.M
#                 result = self.M * result + d
#                 code //= self.M
#             return result
#
#         def visitNode(toVisit, visited1, visited2, do_reverse):
#             nonlocal mindist, result, do_continue
#             cw, dist, path, path_code = toVisit.popleft()
#
#             for i in range(self.L):
#                 int_w = cw[:i] + "*" + cw[i + 1:]
#                 for j, w in self.allWords[int_w]:
#                     path1 = path + [w]
#                     path1_code = self.M*path_code+j
#                     if w in visited2:
#                         res_path = visited2[w][0] + path[::-1]
#                         if len(res_path) <= mindist:
#                             mindist = len(res_path)
#                             if do_reverse:
#                                 new_path = visited2[w][0] + path[::-1]
#                                 new_path_code = self.M ** len(path) * visited2[w][1] + reverse_code(path_code)
#                             else:
#                                 new_path = path + visited2[w][0][::-1]
#                                 new_path_code = self.M ** len(visited2[w][0]) * path_code + reverse_code(visited2[w][1])
#                             if new_path_code not in codes_added:
#                                 result.append(new_path)
#                                 codes_added.add(new_path_code)
#                         # else:
#                         #     do_continue = False
#                     if w not in visited1:
#                         visited1[w] = (path1, path1_code)
#                         toVisit.append((w, dist + 1, path1, path1_code))
#
#         beginCode = wordList.index(beginWord) if beginWord in wordList else self.M
#         endCode = wordList.index(endWord)
#
#         toVisit1 = collections.deque([(beginWord, 1, [beginWord], beginCode)])
#         toVisit2 = collections.deque([(endWord, 1, [endWord], endCode)])
#         visited1 = {beginWord: ([beginWord], beginCode)}
#         visited2 = {endWord: ([endWord], endCode)}
#         while do_continue and toVisit1 and toVisit2:
#             visitNode(toVisit1, visited1, visited2, False)
#             # print(codes_added)
#             # print(result)
#             visitNode(toVisit2, visited2, visited1, True)
#             # print(codes_added)
#             # print(result)
#             for code in codes_added:
#                 print(decode(code, self.M))
#         return result


# https://leetcode.com/problems/word-ladder-ii/solution/
# Runtime: 86 ms, faster than 33.77% of Python3 online submissions for Word Ladder II.
# Memory Usage: 14.6 MB, less than 73.63% of Python3 online submissions for Word Ladder II.
# class Solution:
#
#     def bfs(self, beginWord: str, endWord: str, wordList: Set[str]):
#         q = [beginWord]
#
#         if beginWord in wordList:
#             wordList.remove(beginWord)
#
#         isEnqueued = set()
#         isEnqueued.add(beginWord)
#         while q:
#             visited = []
#             qs = len(q)
#             for i in range(qs-1, -1, -1):
#                 curr_word = q[0]
#                 q.remove(curr_word)
#                 neighbours = self.findNeighbours(curr_word, wordList)
#                 for word in neighbours:
#                     visited.append(word)
#
#                     self.adjList[curr_word].append(word)
#
#                     if word not in isEnqueued:
#                         q.append(word)
#                         isEnqueued.add(word)
#             for vw in visited:
#                 if vw in wordList:
#                     wordList.remove(vw)
#
#     def backtrack(self, source: str, destination: str):
#         if source == destination:
#             tempPath = self.currPath.copy()
#             self.shortestPaths.append(tempPath)
#         if source not in self.adjList:
#             return
#         adjs = self.adjList[source]
#         for adj in adjs:
#             self.currPath.append(adj)
#             self.backtrack(adj, destination)
#             self.currPath.pop()
#
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         self.currPath = []
#         self.adjList = collections.defaultdict(list)
#         self.shortestPaths = []
#
#         words = set(wordList)
#         self.bfs(beginWord, endWord, words)
#         self.currPath.append(beginWord)
#         self.backtrack(beginWord, endWord)
#
#         return self.shortestPaths
#
#     def findNeighbours(self, word, wordList):
#         neighbours = []
#         m = len(word)
#         for i in range(m):
#             oldChar = word[i]
#             for c in [chr(ord('a')+i) for i in range(26)]:
#                 new_word = word[:i] + c + word[i+1:]
#                 if c == oldChar or new_word not in wordList:
#                     continue
#                 neighbours.append(new_word)
#         return neighbours

# https://leetcode.com/problems/word-ladder-ii/solution/
# Runtime: 48 ms, faster than 79.10% of Python3 online submissions for Word Ladder II.
# Memory Usage: 14.5 MB, less than 87.51% of Python3 online submissions for Word Ladder II.
class Solution:

    def findNeighbours(self, word, wordList):
        neighbours = []
        m = len(word)
        for i in range(m):
            oldChar = word[i]
            for c in [chr(ord('a')+i) for i in range(26)]:
                new_word = word[:i] + c + word[i+1:]
                if c == oldChar or new_word not in wordList:
                    continue
                neighbours.append(new_word)
        return neighbours

    def backtrack(self, source: str, destination: str):
        if source == destination:
            tempPath = self.currPath.copy()
            self.shortestPaths.append(tempPath)
        if source not in self.adjList:
            return
        adjs = self.adjList[source]
        for adj in adjs:
            self.currPath.append(adj)
            self.backtrack(adj, destination)
            self.currPath.pop()

    def addEdge(self, w1: str, w2: str, direction: int):
        if direction == 1:
            self.adjList[w1].append(w2)
        else:
            self.adjList[w2].append(w1)

    def bfs(self, beginWord: str, endWord: str, wordList: Set[str]) -> bool:
        if endWord not in wordList:
            return False

        if beginWord in wordList:
            wordList.remove(beginWord)

        q1 = [beginWord]
        q2 = [endWord]

        found = False
        direction = 1
        while q1:
            visited = set()
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                direction ^= 1
            for curr_word in q1:
                neighbours = self.findNeighbours(curr_word, wordList)
                for word in neighbours:
                    if word in q2:
                        found = True
                        self.addEdge(curr_word, word, direction)
                    elif not found and word in wordList and word not in q1:
                        visited.add(word)
                        self.addEdge(curr_word, word, direction)
            for curr_word in q1:
                if curr_word in wordList:
                    wordList.remove(curr_word)
            if found:
                break

            q1 = visited
        return found

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        self.currPath = []
        self.adjList = collections.defaultdict(list)
        self.shortestPaths = []

        words = set(wordList)
        found = self.bfs(beginWord, endWord, words)
        if not found:
            return self.shortestPaths
        self.currPath.append(beginWord)
        self.backtrack(beginWord, endWord)

        return self.shortestPaths


# UNFINISHED
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         if endWord not in wordList:
#             return []
#         result = []
#         L = len(beginWord)
#
#         words = set(wordList)
#
#         connections = collections.defaultdict(list)
#         for word in wordList:
#             for i in range(L):
#                 w1 = word[:i] + '*' + word[i+1:]
#                 connections[w1].append(word)
#
#         q1, q2 = [beginWord], [endWord]
#         forward = True
#         found = False
#         while q1:
#             if len(q1) > len(q2):
#                 q1, q2 = q2, q1
#                 forward = not forward
#             next_level = []
#             for w in q1:
#                 for i in range(L):
#                     w1 = w[:i] + '*' + w[i + 1:]
#                     for next_word in connections[w1]:
#                         if next_word in q2:
#                             found = True
#                             if forward:
#                                 connections[w].append(next_word)
#                             else:
#                                 connections[next_word].append(w)
#                         elif found and next_word not in q1:
#                             next_level.append(next_word)
#                             if forward:
#                                 connections[w].append(next_word)
#                             else:
#                                 connections[next_word].append(w)
#
#
#         return result


tests = [
    [
        "set",
        "oar",
        ["oar","sat","dip","sir","lap","tat","off","din","caw","hob","lie","tam","wyo","noe","rob","nay","hah","box","mac","low","tin","tip","set","geo","too","tea","fin","tad","zed","key","ray","shy","min","kin","rep","now","ink","fag","fed","pas","huh","bad","oks","pan","kip","inc","bat","pop","pat","aol","cud","tan","car","hut","oat","gap","hes","hen","chi"],
        [["set","sat","oat","oar"]]
    ],
    [
        "ta",
        "if",
        ["ts","sc","ph","ca","jr","hf","to","if","ha","is","io","cf","ta"],
        [["ta","ca","cf","if"],["ta","ha","hf","if"],["ta","to","io","if"],["ta","ts","is","if"]]
    ],
    [
        "hit",
        "cog",
        ["hot","hit","cog","dot","dog"],
        [["hit","hot","dot","dog","cog"]]
    ],
    [
        "red",
        "tax",
        ["ted","tex","red","tax","tad","den","rex","pee"],
        [["red","ted","tad","tax"],["red","ted","tex","tax"],["red","rex","tex","tax"]]
    ],
    [
        "hit", "cog",
        ["hot","dot","dog","lot","log","cog"],
        [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
    ],
    [
        "hit", "cog",
        ["hot","dot","dog","lot","log"],
        []
    ]
]

run_functional_tests(Solution().findLadders, tests, custom_check=compareSets)