"""
https://leetcode.com/problems/minimum-genetic-mutation/

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string start to a gene string end where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings start and end and the gene bank bank, return the minimum number of mutations needed to mutate from start to end. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.



Example 1:

Input: start = "AACCGGTT", end = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1
Example 2:

Input: start = "AACCGGTT", end = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
Example 3:

Input: start = "AAAAACCC", end = "AACCCCCC", bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]
Output: 3


Constraints:

start.length == 8
end.length == 8
0 <= bank.length <= 10
bank[i].length == 8
start, end, and bank[i] consist of only the characters ['A', 'C', 'G', 'T'].
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 24 ms, faster than 95.02% of Python3 online submissions for Minimum Genetic Mutation.
# Memory Usage: 14.4 MB, less than 32.25% of Python3 online submissions for Minimum Genetic Mutation.
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        q = [(start, 0)]
        visited = set()
        while q:
            curr, l = q.pop()
            if curr == end:
                return l
            visited.add(curr)
            for nx in bank:
                if nx == curr:
                    continue
                d = 0
                for i in range(len(curr)):
                    if curr[i] != nx[i]:
                        d += 1
                        if d > 1:
                            break
                if d == 1 and nx not in visited:
                    visited.add(nx)
                    q.append((nx, l+1))
        return -1


tests = [
    ["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1],
    ["AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2],
    ["AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3]
]

run_functional_tests(Solution().minMutation, tests)