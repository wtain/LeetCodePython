"""
https://leetcode.com/problems/evaluate-division/

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.



Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 68.06% of Python3 online submissions for Evaluate Division.
# Memory Usage: 14.4 MB, less than 48.31% of Python3 online submissions for Evaluate Division.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        vars = set()
        transitions = defaultdict(dict)
        for (n, d), v in zip(equations, values):
            vars.add(n)
            vars.add(d)
            transitions[n][d] = v
            transitions[d][n] = 1.0 / v
        result = []
        for qn, qd in queries:
            if qn not in vars or qd not in vars:
                result.append(-1.0)
                continue
            q = [(qn, 1.0)]
            visited = set()
            found = False
            while q:
                p, v = q.pop()
                visited.add(p)
                if p == qd:
                    result.append(v)
                    found = True
                    break
                for conn in transitions[p]:
                    if conn not in visited:
                        q.append((conn, v*transitions[p][conn]))
            if not found:
                result.append(-1.0)
        return result


tests = [
    [
        [["a","b"],["c","d"]],
        [1.0,1.0],
        [["a","c"],["b","d"],["b","a"],["d","c"]],
        [-1.00000,-1.00000,1.00000,1.00000]
    ],
    [
        [["a","b"],["b","c"]],
        [2.0,3.0],
        [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]],
        [6.00000,0.50000,-1.00000,1.00000,-1.00000]
    ],
    [
        [["a","b"],["b","c"],["bc","cd"]],
        [1.5,2.5,5.0],
        [["a","c"],["c","b"],["bc","cd"],["cd","bc"]],
        [3.75000,0.40000,5.00000,0.20000]
    ],
    [
        [["a","b"]],
        [0.5],
        [["a","b"],["b","a"],["a","c"],["x","y"]],
        [0.50000,2.00000,-1.00000,-1.00000]
    ]
]

run_functional_tests(Solution().calcEquation, tests)