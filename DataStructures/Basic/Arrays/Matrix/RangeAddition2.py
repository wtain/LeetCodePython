"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/617/week-5-august-29th-august-31st/3957/
https://leetcode.com/problems/range-addition-ii/

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.



Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9


Constraints:

1 <= m, n <= 4 * 104
1 <= ops.length <= 104
ops[i].length == 2
1 <= ai <= m
1 <= bi <= n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 99.62% of Python3 online submissions for Range Addition II.
# Memory Usage: 16.3 MB, less than 22.12% of Python3 online submissions for Range Addition II.
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        ma, mb = m, n
        for a, b in ops:
            ma, mb = min(ma, a), min(mb, b)
        return ma*mb


tests = [
    [3,3,[[2,2],[3,3]],4],
    [3,3,[[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]],4],
    [3,3,[],9]
]

run_functional_tests(Solution().maxCount, tests)