"""
https://leetcode.com/problems/pascals-triangle/
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/605/week-3-june-15th-june-21st/3786/

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 32 ms, faster than 59.60% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 14 MB, less than 21.61% of Python3 online submissions for Pascal's Triangle.
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]
        for row in range(2, numRows):
            prevRow = result[row-1]
            cnt = row+1
            newRow = [0] * cnt
            for i in range(cnt):
                if i < cnt-1:
                    newRow[i] += prevRow[i]
                if i >= 1:
                    newRow[i] += prevRow[i-1]
            result.append(newRow)
        return result


tests = [
    [5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]]
]

run_functional_tests(Solution().generate, tests)
