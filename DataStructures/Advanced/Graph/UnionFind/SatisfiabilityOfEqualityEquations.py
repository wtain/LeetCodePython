"""
https://leetcode.com/problems/satisfiability-of-equality-equations/

You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.



Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 96 ms, faster than 23.90% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 14.1 MB, less than 69.95% of Python3 online submissions for Satisfiability of Equality Equations.
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        p = { chr(ord('a')+c): chr(ord('a')+c) for c in range(26)}
        rank = { chr(ord('a')+c): 0 for c in range(26)}

        def find(i):
            while p[i] != i:
                i = p[i]
            return i

        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return
            if rank[i] < rank[j]:
                p[i] = j
            elif rank[i] > rank[j]:
                p[j] = i
            else:
                p[j] = i
                rank[i] += 1

        not_eq = []

        for eq in equations:
            v1 = eq[0]
            v2 = eq[-1]
            is_equal = eq[1:3] == "=="
            if is_equal:
                union(v1, v2)
            else:
                not_eq.append([v1, v2])

        for v1, v2 in not_eq:
            if find(v1) == find(v2):
                return False

        return True


tests = [
    [["a==b","c==d","a==c","a!=d"], False],

    [["a==b","b!=a"], False],
    [["b==a","a==b"], True]
]

run_functional_tests(Solution().equationsPossible, tests)
