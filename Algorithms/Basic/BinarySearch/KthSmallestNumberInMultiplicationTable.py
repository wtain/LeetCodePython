"""
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.



Example 1:


Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The 5th smallest number is 3.
Example 2:


Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The 6th smallest number is 6.


Constraints:

1 <= m, n <= 3 * 104
1 <= k <= m * n
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def findKthNumber(self, m: int, n: int, k: int) -> int:
#         l, r = 1, n*m
#
#         def check(mid: int) -> int:
#             i, j, cnt = 0, n-1, 0
#             for i in range(n):
#                 while j >= 0 and (i+1)*(j+1) > mid:
#                     j -= 1
#                 cnt += j + 1
#             return cnt
#
#         while l < r:
#             mid = l + (r - l) // 2
#             if check(mid) < k:
#                 l = mid + 1
#             else:
#                 r = mid
#
#         return l


# Runtime: 916 ms, faster than 64.62% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
# Memory Usage: 14.1 MB, less than 94.15% of Python3 online submissions for Kth Smallest Number in Multiplication Table.
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/solution/
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        l, r = 1, n*m

        def check(x: int) -> bool:
            cnt = 0
            for i in range(1, m+1):
                cnt += min(x // i, n)
            return cnt >= k

        while l < r:
            mid = l + (r - l) // 2
            if not check(mid):
                l = mid + 1
            else:
                r = mid

        return l


tests = [
    [3, 3, 5, 3],
    [2, 3, 6, 6]
]

run_functional_tests(Solution().findKthNumber, tests)
