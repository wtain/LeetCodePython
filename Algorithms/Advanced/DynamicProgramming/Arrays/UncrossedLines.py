"""
https://leetcode.com/problems/uncrossed-lines/submissions/

You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.



Example 1:


Input: nums1 = [1,4,2], nums2 = [1,2,4]
Output: 2
Explanation: We can draw 2 uncrossed lines as in the diagram.
We cannot draw 3 uncrossed lines, because the line from nums1[1] = 4 to nums2[2] = 4 will intersect the line from nums1[2]=2 to nums2[1]=2.
Example 2:

Input: nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]
Output: 3
Example 3:

Input: nums1 = [1,3,7,1,7,5], nums2 = [1,9,2,5,1]
Output: 2


Constraints:

1 <= nums1.length, nums2.length <= 500
1 <= nums1[i], nums2[j] <= 2000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 191 ms
# Beats
# 68.77%
# Memory
# 16.3 MB
# Beats
# 39.63%
class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.maxUncrossedLines(nums2, nums1)
        dp = [[0] * 2 for _ in range(n1+1)]
        for j in range(n2):
            j1 = j % 2
            j2 = 1 - j1
            for i in range(n1):
                if nums1[i] == nums2[j]:
                    dp[i+1][j2] = dp[i][j1] + 1
                else:
                    dp[i+1][j2] = max(dp[i+1][j1], dp[i][j2])
        return dp[n1][n2%2]


tests = [
    [[1,4,2], [1,2,4], 2],
    [[2,5,1,2,5], [10,5,2,1,5,2], 3],
    [[1,3,7,1,7,5], [1,9,2,5,1], 2],
]

run_functional_tests(Solution().maxUncrossedLines, tests)
