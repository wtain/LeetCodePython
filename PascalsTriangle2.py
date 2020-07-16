"""
https://leetcode.com/problems/pascals-triangle-ii/

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""
from typing import List


"""
Runtime: 24 ms, faster than 94.39% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 13.8 MB, less than 65.30% of Python3 online submissions for Pascal's Triangle II.
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        prev = [1, 1]
        for row in range(2, rowIndex+1):
            nextRow = [0] * (row+1)
            nextRow[0] = nextRow[row] = 1
            for i in range(1, row):
                nextRow[i] = prev[i-1] + prev[i]
            prev = nextRow
        return prev


print(Solution().getRow(3))  # [1,3,3,1]

print(Solution().getRow(4))  # [1,4,6,4,1]

