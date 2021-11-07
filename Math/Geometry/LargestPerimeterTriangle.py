"""
https://leetcode.com/problems/largest-perimeter-triangle/
Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.



Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8


Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6

Runtime: 256 ms, faster than 7.13% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 15.7 MB, less than 10.60% of Python3 online submissions for Largest Perimeter Triangle.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse=True)
        n = len(A)
        for i in range(n-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0


tests = [
    [[2,1,2], 5],
    [[1,2,1], 0],
    [[3,2,3,4], 10],
    [[3,6,2,3], 8]
]

run_functional_tests(Solution().largestPerimeter, tests)
