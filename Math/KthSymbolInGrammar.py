"""
https://leetcode.com/problems/k-th-symbol-in-grammar/

We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.



Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation:
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation:
row 1: 0
row 2: 01


Constraints:

1 <= n <= 30
1 <= k <= 2n - 1
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 60 ms
# Beats
# 26.15%
# Memory
# 13.8 MB
# Beats
# 67.56%
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        negate = False
        while n > 1:
            digits_in_row = 1 << (n-1)
            if k > digits_in_row // 2:
                negate = not negate
                k -= digits_in_row // 2
            n -= 1
        return 1 if negate else 0


tests = [
    [1, 1, 0],
    [2, 1, 0],
    [2, 2, 1],
    [3, 4, 0],
    [30, 536870000, 1],
]

run_functional_tests(Solution().kthGrammar, tests)
