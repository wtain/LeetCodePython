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
from typing import List, Set, Dict

from Common.ObjectTestingUtils import run_functional_tests
from Common.Helpers.ResultComparators import compareSets


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


# TLE
# https://leetcode.com/problems/word-ladder-ii/solution/
# Runtime: 48 ms, faster than 79.10% of Python3 online submissions for Word Ladder II.
# Memory Usage: 14.5 MB, less than 87.51% of Python3 online submissions for Word Ladder II.
# class Solution:
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
#     def addEdge(self, w1: str, w2: str, direction: int):
#         if direction == 1:
#             self.adjList[w1].append(w2)
#         else:
#             self.adjList[w2].append(w1)
#
#     def bfs(self, beginWord: str, endWord: str, wordList: Set[str]) -> bool:
#         if endWord not in wordList:
#             return False
#
#         if beginWord in wordList:
#             wordList.remove(beginWord)
#
#         q1 = [beginWord]
#         q2 = [endWord]
#
#         found = False
#         direction = 1
#         while q1:
#             visited = set()
#             if len(q1) > len(q2):
#                 q1, q2 = q2, q1
#                 direction ^= 1
#             for curr_word in q1:
#                 neighbours = self.findNeighbours(curr_word, wordList)
#                 for word in neighbours:
#                     if word in q2:
#                         found = True
#                         self.addEdge(curr_word, word, direction)
#                     elif not found and word in wordList and word not in q1:
#                         visited.add(word)
#                         self.addEdge(curr_word, word, direction)
#             for curr_word in q1:
#                 if curr_word in wordList:
#                     wordList.remove(curr_word)
#             if found:
#                 break
#
#             q1 = visited
#         return found
#
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         self.currPath = []
#         self.adjList = collections.defaultdict(list)
#         self.shortestPaths = []
#
#         words = set(wordList)
#         found = self.bfs(beginWord, endWord, words)
#         if not found:
#             return self.shortestPaths
#         self.currPath.append(beginWord)
#         self.backtrack(beginWord, endWord)
#
#         return self.shortestPaths


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


# Runtime: 108 ms, faster than 44.34% of Python3 online submissions for Word Ladder II.
# Memory Usage: 14.3 MB, less than 68.67% of Python3 online submissions for Word Ladder II.
# https://leetcode.com/problems/word-ladder-ii/discuss/2411758/Java-Solution-DFS%2BBFS
class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        master = []
        dictionary = set(wordList)
        if len(beginWord) != len(endWord) or endWord not in dictionary:
            return master
        if beginWord == endWord and endWord in dictionary:
            return [[beginWord]]

        visitedAtLevel = {}
        graph = collections.defaultdict(list)
        self.bfs(beginWord, endWord, dictionary, visitedAtLevel, graph)
        self.currPath = []
        self.visited = set()
        self.dfs(graph, master, beginWord, endWord)
        return master

    def bfs(self, start, end, dictionary, visitedAtLevel: Dict[str, int], graph):
        q = [start]
        visitedAtLevel[start] = 0
        while q:
            currWord = q[0]
            q = q[1:]
            arr = [c for c in currWord]
            for i in range(len(arr)):
                currChar = arr[i]
                for j in "abcdefghijklmnopqrstuvwxyz":
                    if arr[i] == j:
                        continue
                    arr[i] = j
                    temp = "".join(arr)
                    if temp in dictionary:
                        if temp not in visitedAtLevel:
                            v = -1
                            if currWord in visitedAtLevel:
                                v = visitedAtLevel[currWord]
                            visitedAtLevel[temp] = v+1
                            if currWord not in graph:
                                graph[currWord] = []
                            graph[currWord].append(temp)
                            q.append(temp)
                        elif visitedAtLevel[temp] == visitedAtLevel[currWord] + 1:
                            if currWord not in graph:
                                graph[currWord] = []
                            graph[currWord].append(temp)
                arr[i] = currChar

    def dfs(self, graph, master, start, end):
        if start in self.visited:
            return
        if start == end:
            self.currPath.append(start)
            master.append(self.currPath)
            self.currPath = self.currPath[:len(self.currPath)-1]
            self.visited = set()
            return

        if not graph[start]:
            return

        self.visited.add(start)
        for curr in graph[start]:
            self.currPath.append(start)
            self.dfs(graph, master, curr, end)
            if self.currPath:
                self.currPath = self.currPath[:len(self.currPath) - 1]


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
    ],
    [
        "aaaaa", "uuuuu",
        ["aaaaa","waaaa","wbaaa","xaaaa","xbaaa","bbaaa","bbwaa","bbwba","bbxaa","bbxba","bbbba","wbbba","wbbbb","xbbba","xbbbb","cbbbb","cwbbb","cwcbb","cxbbb","cxcbb","cccbb","cccwb","cccwc","cccxb","cccxc","ccccc","wcccc","wdccc","xcccc","xdccc","ddccc","ddwcc","ddwdc","ddxcc","ddxdc","ddddc","wdddc","wdddd","xdddc","xdddd","edddd","ewddd","ewedd","exddd","exedd","eeedd","eeewd","eeewe","eeexd","eeexe","eeeee","weeee","wfeee","xeeee","xfeee","ffeee","ffwee","ffwfe","ffxee","ffxfe","ffffe","wfffe","wffff","xfffe","xffff","gffff","gwfff","gwgff","gxfff","gxgff","gggff","gggwf","gggwg","gggxf","gggxg","ggggg","wgggg","whggg","xgggg","xhggg","hhggg","hhwgg","hhwhg","hhxgg","hhxhg","hhhhg","whhhg","whhhh","xhhhg","xhhhh","ihhhh","iwhhh","iwihh","ixhhh","ixihh","iiihh","iiiwh","iiiwi","iiixh","iiixi","iiiii","wiiii","wjiii","xiiii","xjiii","jjiii","jjwii","jjwji","jjxii","jjxji","jjjji","wjjji","wjjjj","xjjji","xjjjj","kjjjj","kwjjj","kwkjj","kxjjj","kxkjj","kkkjj","kkkwj","kkkwk","kkkxj","kkkxk","kkkkk","wkkkk","wlkkk","xkkkk","xlkkk","llkkk","llwkk","llwlk","llxkk","llxlk","llllk","wlllk","wllll","xlllk","xllll","mllll","mwlll","mwmll","mxlll","mxmll","mmmll","mmmwl","mmmwm","mmmxl","mmmxm","mmmmm","wmmmm","wnmmm","xmmmm","xnmmm","nnmmm","nnwmm","nnwnm","nnxmm","nnxnm","nnnnm","wnnnm","wnnnn","xnnnm","xnnnn","onnnn","ownnn","owonn","oxnnn","oxonn","ooonn","ooown","ooowo","oooxn","oooxo","ooooo","woooo","wpooo","xoooo","xpooo","ppooo","ppwoo","ppwpo","ppxoo","ppxpo","ppppo","wpppo","wpppp","xpppo","xpppp","qpppp","qwppp","qwqpp","qxppp","qxqpp","qqqpp","qqqwp","qqqwq","qqqxp","qqqxq","qqqqq","wqqqq","wrqqq","xqqqq","xrqqq","rrqqq","rrwqq","rrwrq","rrxqq","rrxrq","rrrrq","wrrrq","wrrrr","xrrrq","xrrrr","srrrr","swrrr","swsrr","sxrrr","sxsrr","sssrr","ssswr","sssws","sssxr","sssxs","sssss","wssss","wtsss","xssss","xtsss","ttsss","ttwss","ttwts","ttxss","ttxts","tttts","wttts","wtttt","xttts","xtttt","utttt","uwttt","uwutt","uxttt","uxutt","uuutt","uuuwt","uuuwu","uuuxt","uuuxu","uuuuu","zzzzz","zzzzy","zzzyy","zzyyy","zzyyx","zzyxx","zzxxx","zzxxw","zzxww","zzwww","zzwwv","zzwvv","zzvvv","zzvvu","zzvuu","zzuuu","zzuut","zzutt","zzttt","zztts","zztss","zzsss","zzssr","zzsrr","zzrrr","zzrrq","zzrqq","zzqqq","zzqqp","zzqpp","zzppp","zzppo","zzpoo","zzooo","zzoon","zzonn","zznnn","zznnm","zznmm","zzmmm","zzmml","zzmll","zzlll","zzllk","zzlkk","zzkkk","zzkkj","zzkjj","zzjjj","zzjji","zzjii","zziii","zziih","zzihh","zzhhh","zzhhg","zzhgg","zzggg","zzggf","zzgff","zzfff","zzffe","zzfee","zzeee","zzeed","zzedd","zzddd","zzddc","zzdcc","zzccc","zzccz","azccz","aaccz","aaacz","aaaaz","uuuzu","uuzzu","uzzzu","zzzzu"],
        [["aaaaa","aaaaz","aaacz","aaccz","azccz","zzccz","zzccc","zzdcc","zzddc","zzddd","zzedd","zzeed","zzeee","zzfee","zzffe","zzfff","zzgff","zzggf","zzggg","zzhgg","zzhhg","zzhhh","zzihh","zziih","zziii","zzjii","zzjji","zzjjj","zzkjj","zzkkj","zzkkk","zzlkk","zzllk","zzlll","zzmll","zzmml","zzmmm","zznmm","zznnm","zznnn","zzonn","zzoon","zzooo","zzpoo","zzppo","zzppp","zzqpp","zzqqp","zzqqq","zzrqq","zzrrq","zzrrr","zzsrr","zzssr","zzsss","zztss","zztts","zzttt","zzutt","zzuut","zzuuu","zzvuu","zzvvu","zzvvv","zzwvv","zzwwv","zzwww","zzxww","zzxxw","zzxxx","zzyxx","zzyyx","zzyyy","zzzyy","zzzzy","zzzzu","uzzzu","uuzzu","uuuzu","uuuuu"]]
    ]
]

run_functional_tests(Solution().findLadders, tests, custom_check=compareSets)