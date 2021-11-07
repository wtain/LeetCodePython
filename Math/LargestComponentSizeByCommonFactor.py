"""
https://leetcode.com/problems/largest-component-size-by-common-factor/
https://leetcode.com/explore/challenge/card/august-leetcoding-challenge/553/week-5-august-29th-august-31st/3442/
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.



Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 2844 ms, faster than 20.11% of Python3 online submissions for Largest Component Size by Common Factor.
Memory Usage: 18.3 MB, less than 78.84% of Python3 online submissions for Largest Component Size by Common Factor.
"""
import math
from typing import List, Dict


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        roots: Dict[int, int] = {}

        def getRoot(label) -> int:
            if label not in roots:
                roots[label] = label
            while roots[label] != label:
                label = roots[label]
            return label

        def doUnion(num: int, f: int):
            r1 = getRoot(num)
            r2 = getRoot(f)
            if r1 < r2:
                roots[r2] = r1
            else:
                roots[r1] = r2

        for i in range(0, n):
            m = int(math.sqrt(A[i]))
            for j in range(2, m+1):
                if A[i] % j == 0:
                    doUnion(A[i], j)
                    res = int(A[i] / j)
                    if res != j:
                        doUnion(A[i], res)
        sizes: Dict[int, int] = {}
        maxSize = 0
        for i in range(0, n):
            root = getRoot(A[i])
            sizes[root] = sizes.get(root, 0) + 1
            maxSize = max(maxSize, sizes[root])
        return maxSize


tests = [
    [[4, 6, 15, 35], 4],
    [[20, 50, 9, 63], 2],
    [[2,3,6,7,4,12,21,39], 8]
]

run_functional_tests(Solution().largestComponentSize, tests)
