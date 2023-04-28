"""
https://leetcode.com/problems/similar-string-groups/description/

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?



Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1


Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 260 ms
# Beats
# 78.36%
# Memory
# 16.7 MB
# Beats
# 10.16%
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:

        def is_similar(a, b):
            n = len(a)
            if len(b) != n:
                return False
            c1, c2 = '', ''
            matched = False
            for i in range(n):
                if a[i] != b[i]:
                    if matched:
                        return False
                    if c1:
                        if c1 == b[i] and c2 == a[i]:
                            matched = True
                        else:
                            return False
                    else:
                        c1, c2 = a[i], b[i]
            return True

        n = len(strs)

        p, rank = list(range(n)), [1] * n

        def get(i):
            while i != p[i]:
                i = p[i]
            return i

        def connect(i, j):
            i, j = get(i), get(j)
            if rank[i] > rank[j]:
                p[j] = i
            elif rank[i] < rank[j]:
                p[i] = j
            else:
                p[j] = i
                rank[i] += 1

        for i in range(n):
            for j in range(i+1, n):
                if is_similar(strs[i], strs[j]):
                    connect(i, j)

        return sum(1 for i in range(n) if p[i] == i)


tests = [
    [["tars","rats","arts","star"], 2],
    [["omv","ovm"], 1],
]

run_functional_tests(Solution().numSimilarGroups, tests)
