"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/593/week-1-april-1st-april-7th/3694/
https://leetcode.com/problems/ones-and-zeroes/

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.



Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.


Constraints:

1 <= strs.length <= 600
1 <= strs[i].length <= 100
strs[i] consists only of digits '0' and '1'.
1 <= m, n <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 3688 ms, faster than 44.27% of Python3 online submissions for Ones and Zeroes.
# Memory Usage: 14.3 MB, less than 95.49% of Python3 online submissions for Ones and Zeroes.
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        c = len(strs)
        dp = [[0] * (n+1) for _ in range(m+1)]

        def count(si: str) -> List[int]:
            res = [0, 0]
            for t in si:
                res[ord(t) - ord('0')] += 1
            return res

        for si in strs:
            ci = count(si)
            for i in range(m, ci[0]-1, -1):
                for j in range(n, ci[1]-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-ci[0]][j-ci[1]] + 1)

        return dp[m][n]


tests = [
    (["10","0001","111001","1","0"], 5, 3, 4),
    (["10","0","1"], 1, 1, 2)
]

run_functional_tests(Solution().findMaxForm, tests)