"""
https://leetcode.com/problems/4sum-ii/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3569/
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

Runtime: 284 ms, faster than 58.48% of Python3 online submissions for 4Sum II.
Memory Usage: 34.9 MB, less than 86.51% of Python3 online submissions for 4Sum II.
"""
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1160 ms, faster than 31.61% of Python3 online submissions for 4Sum II.
# Memory Usage: 14.3 MB, less than 90.85% of Python3 online submissions for 4Sum II.
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counts: Dict[int, int] = {}
        for a in A:
            for b in B:
                counts[a+b] = counts.get(a+b, 0) + 1

        result = 0
        for c in C:
            for d in D:
                target = -c - d
                result += counts.get(target, 0)

        return result


tests = [
    [
        [ 1, 2],
        [-2,-1],
        [-1, 2],
        [ 0, 2],
        2
    ]
]

run_functional_tests(Solution().fourSumCount, tests)