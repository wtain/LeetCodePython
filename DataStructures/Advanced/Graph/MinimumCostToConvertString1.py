"""
https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=daily-question&envId=2024-07-27

You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English letters. You are also given two 0-indexed character arrays original and changed, and an integer array cost, where cost[i] represents the cost of changing the character original[i] to the character changed[i].

You start with the string source. In one operation, you can pick a character x from the string and change it to the character y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y.

Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.

Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].



Example 1:

Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
Output: 28
Explanation: To convert the string "abcd" to string "acbe":
- Change value at index 1 from 'b' to 'c' at a cost of 5.
- Change value at index 2 from 'c' to 'e' at a cost of 1.
- Change value at index 2 from 'e' to 'b' at a cost of 2.
- Change value at index 3 from 'd' to 'e' at a cost of 20.
The total cost incurred is 5 + 1 + 2 + 20 = 28.
It can be shown that this is the minimum possible cost.
Example 2:

Input: source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]
Output: 12
Explanation: To change the character 'a' to 'b' change the character 'a' to 'c' at a cost of 1, followed by changing the character 'c' to 'b' at a cost of 2, for a total cost of 1 + 2 = 3. To change all occurrences of 'a' to 'b', a total cost of 3 * 4 = 12 is incurred.
Example 3:

Input: source = "abcd", target = "abce", original = ["a"], changed = ["e"], cost = [10000]
Output: -1
Explanation: It is impossible to convert source to target because the value at index 3 cannot be changed from 'd' to 'e'.


Constraints:

1 <= source.length == target.length <= 105
source, target consist of lowercase English letters.
1 <= cost.length == original.length == changed.length <= 2000
original[i], changed[i] are lowercase English letters.
1 <= cost[i] <= 106
original[i] != changed[i]
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
#         n = len(source)
#         m = len(original)
#         states = [(source, 0)]
#         seen = {source}
#         while states:
#             next_states = []
#             for state in states:
#                 word, score = state
#                 if word == target:
#                     return score
#                 for i in range(m):
#                     indexes = []
#                     for j in range(n):
#                         if word[j] == original[i]:
#                             indexes.append([j, i])
#                     for j, i in indexes:
#                         w1 = word[:j] + changed[i] + word[j+1:]
#                         s1 = score + cost[i]
#                         if w1 not in seen:
#                             next_states.append((w1, s1))
#                             seen.add(w1)
#             states = next_states
#
#         return -1

# Runtime
# 1374
# ms
# Beats
# 69.54%
# Analyze Complexity
# Memory
# 18.46
# MB
# Beats
# 27.92%
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/editorial/?envType=daily-question&envId=2024-07-27
# class Solution:
#     def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
#         adjacent = [[] for _ in range(26)]
#         conversion_count = len(original)
#         for i in range(conversion_count):
#             adjacent[ord(original[i]) - ord('a')].append((ord(changed[i]) - ord('a'), cost[i]))
#
#         min_conversion_cost = [self.dijkstra(i, adjacent) for i in range(26)]
#
#         total_cost = 0
#         for s, t in zip(source, target):
#             if s != t:
#                 char_conv_cost = min_conversion_cost[ord(s) - ord('a')][ord(t) - ord('a')]
#                 if char_conv_cost == float("inf"):
#                     return -1
#                 total_cost += char_conv_cost
#         return total_cost
#
#     def dijkstra(self, start, adj):
#         priority_queue = [(0, start)]
#         min_costs = [float("inf")] * 26
#
#         while priority_queue:
#             curr_cost, curr_char = heapq.heappop(priority_queue)
#
#             if min_costs[curr_char] != float("inf"):
#                 continue
#
#             min_costs[curr_char] = curr_cost
#
#             for target_char, conv_cost in adj[curr_char]:
#                 new_total_cost = curr_cost + conv_cost
#
#                 if min_costs[target_char] == float("inf"):
#                     heapq.heappush(priority_queue, (new_total_cost, target_char))
#
#         return min_costs


# Runtime
# 1944
# ms
# Beats
# 38.07%
# Analyze Complexity
# Memory
# 18.22
# MB
# Beats
# 58.38%
# https://leetcode.com/problems/minimum-cost-to-convert-string-i/editorial/?envType=daily-question&envId=2024-07-27
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        total_cost = 0
        min_cost = [[float("inf")] * 26 for _ in range(26)]

        for orig, chg, cst in zip(original, changed, cost):
            start = ord(orig) - ord('a')
            end = ord(chg) - ord('a')
            min_cost[start][end] = min(min_cost[start][end], cst)

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    min_cost[i][j] = min(min_cost[i][j], min_cost[i][k] + min_cost[k][j])

        for src, tgt in zip(source, target):
            if src == tgt:
                continue
            source_char = ord(src) - ord('a')
            target_char = ord(tgt) - ord('a')

            if min_cost[source_char][target_char] == float("inf"):
                return -1

            total_cost += min_cost[source_char][target_char]

        return total_cost



tests = [
    ["aaaabadaaa", "dbdadddbad", ["c","a","c","a","a","b","b","b","d","d","c"], ["a","c","b","d","b","c","a","d","c","b","d"], [7,8,11,9,7,6,4,6,9,5,9], 56],
    ["abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20], 28],
    ["aaaa", "bbbb", ["a","c"], ["c","b"], [1,2], 12],
    ["abcd", "abce", ["a"], ["e"], [10000], -1],
]

run_functional_tests(Solution().minimumCost, tests)
