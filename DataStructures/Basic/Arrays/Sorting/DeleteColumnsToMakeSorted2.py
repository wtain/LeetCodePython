"""
https://leetcode.com/problems/delete-columns-to-make-sorted-ii/description/?envType=problem-list-v2&envId=array

You are given an array of n strings strs, all of the same length.

We may choose any deletion indices, and we delete all the characters in those indices for each string.

For example, if we have strs = ["abcdef","uvwxyz"] and deletion indices {0, 2, 3}, then the final array after deletions is ["bef", "vyz"].

Suppose we chose a set of deletion indices answer such that after deletions, the final array has its elements in lexicographic order (i.e., strs[0] <= strs[1] <= strs[2] <= ... <= strs[n - 1]). Return the minimum possible value of answer.length.



Example 1:

Input: strs = ["ca","bb","ac"]
Output: 1
Explanation:
After deleting the first column, strs = ["a", "b", "c"].
Now strs is in lexicographic order (ie. strs[0] <= strs[1] <= strs[2]).
We require at least 1 deletion since initially strs was not in lexicographic order, so the answer is 1.
Example 2:

Input: strs = ["xc","yb","za"]
Output: 0
Explanation:
strs is already in lexicographic order, so we do not need to delete anything.
Note that the rows of strs are not necessarily in lexicographic order:
i.e., it is NOT necessarily true that (strs[0][0] <= strs[0][1] <= ...)
Example 3:

Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: We have to delete every column.


Constraints:

n == strs.length
1 <= n <= 100
1 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         result = 0
#         n = len(strs)
#         m = len(strs[0])
#         skip_comparison = [False] * n
#         for j in range(m):
#             for i in range(1, n):
#                 if skip_comparison[i]:
#                     continue
#                 if strs[i][j] < strs[i-1][j]:
#                     result += 1
#                     break
#                 elif strs[i][j] > strs[i - 1][j]:
#                     skip_comparison[i] = True
#                 else:
#                     skip_comparison[i] = False
#         return result


# Runtime
# 3
# ms
# Beats
# 78.67%
# Analyze Complexity
# Memory
# 17.89
# MB
# Beats
# 64.00%
# https://leetcode.com/problems/delete-columns-to-make-sorted-ii/editorial/?envType=problem-list-v2&envId=array
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        n = len(strs)
        m = len(strs[0])
        skip_comparison = [False] * n
        for j in range(m):
            vioalte = False
            for i in range(1, n):
                if skip_comparison[i]:
                    continue
                if strs[i][j] < strs[i-1][j]:
                    vioalte = True
                    break

            if not vioalte:
                for i in range(1, n):
                    if strs[i][j] > strs[i-1][j]:
                        skip_comparison[i] = True
            else:
                result += 1
        return result


tests = [
    [["vdy","vei","zvc","zld"], 2],
    [["ca","bb","ac"], 1],
    [["xc","yb","za"], 0],
    [["zyx","wvu","tsr"], 3],
]

run_functional_tests(Solution().minDeletionSize, tests)
