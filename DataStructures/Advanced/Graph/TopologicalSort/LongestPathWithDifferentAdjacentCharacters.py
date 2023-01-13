"""
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/description/

You are given a tree (i.e. a connected, undirected graph that has no cycles) rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is represented by a 0-indexed array parent of size n, where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.

You are also given a string s of length n, where s[i] is the character assigned to node i.

Return the length of the longest path in the tree such that no pair of adjacent nodes on the path have the same character assigned to them.



Example 1:


Input: parent = [-1,0,0,1,1,2], s = "abacbe"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters in the tree is the path: 0 -> 1 -> 3. The length of this path is 3, so 3 is returned.
It can be proven that there is no longer path that satisfies the conditions.
Example 2:


Input: parent = [-1,0,0,0], s = "aabc"
Output: 3
Explanation: The longest path where each two adjacent nodes have different characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is returned.


Constraints:

n == parent.length == s.length
1 <= n <= 105
0 <= parent[i] <= n - 1 for all i >= 1
parent[0] == -1
parent represents a valid tree.
s consists of only lowercase English letters.
"""
from collections import defaultdict, deque
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1474 ms
# Beats
# 99.19%
# Memory
# 149 MB
# Beats
# 76.92%
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/2889382/longest-path-with-different-adjacent-characters/
# class Solution:
#     def longestPath(self, parent: List[int], s: str) -> int:
#
#         longestPath = 1
#
#         n = len(parent)
#         children = defaultdict(list)
#         for i in range(1, n):
#             children[parent[i]].append(i)
#
#         def dfs(currentNode: int):
#             nonlocal longestPath, children, s
#             if currentNode not in children:
#                 return 1
#
#             longestChain, secondLongestChain = 0, 0
#             for child in children[currentNode]:
#
#                 longestChainStartingFromChild = dfs(child)
#
#                 if s[child] == s[currentNode]:
#                     continue
#
#                 if longestChainStartingFromChild > longestChain:
#                     secondLongestChain = longestChain
#                     longestChain = longestChainStartingFromChild
#                 elif longestChainStartingFromChild > secondLongestChain:
#                     secondLongestChain = longestChainStartingFromChild
#
#             longestPath = max(longestPath, longestChain + secondLongestChain + 1)
#             return longestChain + 1
#
#         dfs(0)
#
#         return longestPath


# Runtime
# 1657 ms
# Beats
# 91.90%
# Memory
# 32.7 MB
# Beats
# 99.60%
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/solutions/2889382/longest-path-with-different-adjacent-characters/
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        longestPath = 1

        n = len(parent)
        childrenCount = [0] * n
        for node in range(1, n):
            childrenCount[parent[node]] += 1

        q = deque()
        longestPath = 1
        longestChains = [[0] * 2 for _ in range(n)]

        for node in range(1, n):
            if childrenCount[node] == 0:
                longestChains[node][0] = 1
                q.append(node)

        while q:
            currentNode = q.popleft()
            par = parent[currentNode]

            longestChainStartingFromCurrNode = longestChains[currentNode][0]
            if s[currentNode] != s[par]:
                if longestChainStartingFromCurrNode > longestChains[par][0]:
                    longestChains[par][1] = longestChains[par][0]
                    longestChains[par][0] = longestChainStartingFromCurrNode
                elif longestChainStartingFromCurrNode > longestChains[par][1]:
                    longestChains[par][1] = longestChainStartingFromCurrNode

            longestPath = max(longestPath, longestChains[par][0] + longestChains[par][1] + 1)
            childrenCount[par] -= 1

            if childrenCount[par] == 0 and par != 0:
                longestChains[par][0] += 1
                q.append(par)

        return longestPath


tests = [
    [[-1,0,0,1,1,2], "abacbe", 3],
    [[-1,0,0,0], "aabc", 3],
]

run_functional_tests(Solution().longestPath, tests)
