"""
https://leetcode.com/problems/smallest-string-with-swaps/

You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# TLE
# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         mins = s
#         to_visit = [s]
#         visited = set()
#         while to_visit:
#             current = to_visit.pop()
#             visited.add(current)
#             mins = min(mins, current)
#             for i,j in pairs:
#                 if i == j:
#                     continue
#                 i1, j1 = min(i,j), max(i,j)
#                 nx = current[:i1] + current[j1] + current[i1+1:j1] + current[i1] + current[j1+1:]
#                 if nx not in visited and nx not in to_visit:
#                     to_visit.append(nx)
#         return mins


# Runtime: 1367 ms, faster than 10.84% of Python3 online submissions for Smallest String With Swaps.
# Memory Usage: 74.1 MB, less than 11.17% of Python3 online submissions for Smallest String With Swaps.
# https://leetcode.com/problems/smallest-string-with-swaps/solution/
# class Solution:
#     def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
#         N = 100001
#         adj = [[] for _ in range(N)]
#         visited = [False] * N
#         arr = [c for c in s]
#
#         def dfs(s: str, vertex: int, chars, inds):
#             chars.append(s[vertex])
#             inds.append(vertex)
#             visited[vertex] = True
#             for adjacent in adj[vertex]:
#                 if not visited[adjacent]:
#                     dfs(s, adjacent, chars, inds)
#
#         for i, j in pairs:
#             adj[i].append(j)
#             adj[j].append(i)
#
#         for i in range(len(s)):
#             if not visited[i]:
#                 chars, inds = [], []
#                 dfs(s, i, chars, inds)
#                 chars.sort()
#                 inds.sort()
#
#                 for j in range(len(chars)):
#                     arr[inds[j]] = chars[j]
#
#         return "".join(arr)

# https://leetcode.com/problems/smallest-string-with-swaps/solution/


# Runtime: 756 ms, faster than 80.23% of Python3 online submissions for Smallest String With Swaps.
# Memory Usage: 50.5 MB, less than 69.64% of Python3 online submissions for Smallest String With Swaps.
class UnionFind:
    def __init__(self, size):
        self.group = list(range(size))
        self.rank = [0] * size

    def find(self, i) -> int:
        if self.group[i] != i:
            self.group[i] = self.find(self.group[i])
        return self.group[i]

    def union(self, i, j) -> bool:
        g1, g2 = self.find(i), self.find(j)
        if g1 == g2:
            return False
        if self.rank[g1] > self.rank[g2]:
            self.group[g2] = g1
        elif self.rank[g1] < self.rank[g2]:
            self.group[g1] = g2
        else:
            self.group[g1] = g2
            self.rank[g2] += 1
        return True

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        uf = UnionFind(len(s))
        for i, j in pairs:
            uf.union(i, j)

        root_to_comp = defaultdict(list)
        for v in range(len(s)):
            root = uf.find(v)
            root_to_comp[root].append(v)

        arr = [" "] * len(s)
        for comp in root_to_comp:
            inds = root_to_comp[comp]
            chars = []
            for i in inds:
                chars.append(s[i])
            chars.sort()
            for i in range(len(inds)):
                arr[inds[i]] = chars[i]

        return "".join(arr)


tests = [
    ["dcab", [[0,3],[1,2]], "bacd"],
    ["dcab", [[0,3],[1,2],[0,2]], "abcd"],
    ["cba", [[0,1],[1,2]], "abc"],
    ["udyyek", [[3,3],[3,0],[5,1],[3,1],[3,4],[3,5]], "deykuy"],
    ["otilzqqoj", [[2,3],[7,3],[3,8],[1,7],[1,0],[0,4],[0,6],[3,4],[2,5]], "ijlooqqtz"]
]

run_functional_tests(Solution().smallestStringWithSwaps, tests)
