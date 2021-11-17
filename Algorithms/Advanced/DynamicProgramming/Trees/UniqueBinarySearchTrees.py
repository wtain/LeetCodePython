"""
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.



Example 1:


Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 19
"""
from Common.ObjectTestingUtils import run_functional_tests


# https://leetcode.com/submissions/detail/357745841/
# Runtime: 28 ms, faster than 86.81% of Python3 online submissions for Unique Binary Search Trees.
# Memory Usage: 14.4 MB, less than 15.60% of Python3 online submissions for Unique Binary Search Trees.
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            cnt = 0
            for j in range(i):
                cnt += dp[j] * dp[i - 1 - j]
            dp[i] = cnt
        return dp[n]


tests = [
    [3, 5],
    [1, 1]
]

run_functional_tests(Solution().numTrees, tests)
