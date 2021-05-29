"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3753/
https://leetcode.com/problems/find-the-shortest-superstring/

Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

You may assume that no string in words is a substring of another string in words.



Example 1:

Input: words = ["alex","loves","leetcode"]
Output: "alexlovesleetcode"
Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
Example 2:

Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
Output: "gctaagttcatgcatc"


Constraints:

1 <= words.length <= 12
1 <= words[i].length <= 20
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# WRONG
# class Solution:
#     def shortestSuperstring(self, words: List[str]) -> str:
#         n = len(words)
#
#         dp = [[""] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = words[i]
#
#         def combine(w1: str, w2: str) -> str:
#             n1, n2 = len(w1), len(w2)
#             m = min(n1, n2)
#             for l in range(m, 0, -1):
#                 if w1[-l:] == w2[:l]:
#                     return w1 + w2[l:]
#             return w1 + w2
#
#         for l in range(2, n+1):
#             for i in range(n-l+1):
#                 j = i + l - 1
#                 # dp[i][j] = min(combine(dp[i][j-1], w[j]),
#                 #                combine(w[j], dp[i][j-1],
#                 #                combine(dp[i+1][j], w[i]),
#                 #                combine(w[i], dp[i+1][j]))
#                 u1 = combine(dp[i][j-1], words[j])
#                 u2 = combine(words[j], dp[i][j - 1])
#                 u3 = combine(dp[i+1][j], words[i])
#                 u4 = combine(words[i], dp[i+1][j])
#                 u = [u1, u2, u3, u4]
#                 dp[i][j] = sorted([(len(uk), uk) for uk in u])[0][1]
#
#         return dp[0][n-1]

# class Solution:
#     def shortestSuperstring(self, words: List[str]) -> str:
#         n = len(words)
#
#         dp = [[""] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = words[i]
#
#         def combine(w1: str, w2: str) -> str:
#             n1, n2 = len(w1), len(w2)
#             m = min(n1, n2)
#             for l in range(m, 0, -1):
#                 if w1[-l:] == w2[:l]:
#                     return w1 + w2[l:]
#             return w1 + w2
#
#         for i in range(n-1):
#             w1, w2 = words[i], words[i+1]
#             u1 = combine(w1, w2)
#             u2 = combine(w2, w1)
#             if len(u1) < len(u2):
#                 dp[i][i+1] = u1
#             else:
#                 dp[i][i + 1] = u2
#
#         for l in range(3, n+1):
#             for i in range(n-l+1):
#                 j = i + l - 1
#
#                 umin, ul = "", 2400
#
#                 for k in range(i+1, j):
#                     # i..k-1 k k+1..j
#                     d1 = dp[i][k-1]
#                     d2 = dp[k+1][j]
#                     d12 = combine(d1, d2)
#                     d21 = combine(d2, d1)
#                     if len(d1) < len(d2):
#                         d = d12
#                     else:
#                         d = d21
#                     o1 = combine(words[k], d)
#                     o2 = combine(combine(d1, words[k]), d2)
#                     o3 = combine(d, words[k])
#                     o4 = combine(d1, combine(words[k], d2))
#                     o5 = combine(combine(d2, words[k]), d1)
#                     o6 = combine(d2, combine(words[k], d1))
#                     u1l, u1 = sorted([len(o), o] for o in [o1, o2, o3, o4, o5, o6])[0]
#                     if u1l < ul:
#                         ul = u1l
#                         umin = u1
#
#                 dp[i][j] = umin
#
#         return dp[0][n-1]


# Runtime: 676 ms, faster than 71.43% of Python3 online submissions for Find the Shortest Superstring.
# Memory Usage: 15.5 MB, less than 64.66% of Python3 online submissions for Find the Shortest Superstring.
class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        n = len(words)
        overlaps = [[0] * n for _ in range(n)]
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if i != j:
                    for l in range(min(len(w1), len(w2)), -1, -1):
                        if w1.endswith(w2[:l]):
                            overlaps[i][j] = l
                            break

        P = 1 << n

        dp = [[0] * n for _ in range(P)]
        parent = [[None] * n for _ in range(P)]
        for mask in range(1, P):
            for bit in range(n):
                if (mask >> bit) & 1:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0:
                        continue
                    for i in range(n):
                        if (pmask >> i) & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        perm = []
        mask = P - 1
        i = max(range(n), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        perm = perm[::-1]

        seen = [False] * n
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(n) if not seen[i]])

        result = [words[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            result.append(words[perm[i]][overlap:])

        return "".join(result)


tests = [
    [["sssv","svq","dskss","sksss"], "dsksssvq"],
    [["alex","loves","leetcode"], "alexlovesleetcode"],
    [["catg","ctaagt","gcta","ttca","atgcatc"], "gctaagttcatgcatc"]
]


def customCheck(test, result) -> bool:
    return len(test[-1]) == len(result)

run_functional_tests(Solution().shortestSuperstring, tests, custom_check=customCheck)