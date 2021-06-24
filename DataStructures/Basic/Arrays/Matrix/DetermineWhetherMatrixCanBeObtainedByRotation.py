"""
https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.



Example 1:


Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
Example 2:


Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
Example 3:


Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.


Constraints:

n == mat.length == target.length
n == mat[i].length == target[i].length
1 <= n <= 10
mat[i][j] and target[i][j] are either 0 or 1.


"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 40 ms, faster than 93.09% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
# Memory Usage: 14.3 MB, less than 67.65% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def is_rot_1() -> bool:
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[j][n-1-i]:
                        return False
            return True

        def is_rot_2() -> bool:
            for i in range(n):
                for j in range(n):
                    if target[i][j] != mat[j][n-1-i]:
                        return False
            return True

        def is_rot_3() -> bool:
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[n-1-i][n-1-j]:
                        return False
            return True

        return mat == target or is_rot_1() or is_rot_2() or is_rot_3()


tests = [
    [[
        [0,0,0],
        [0,0,1],
        [0,0,1]],
        [[0,0,0],
         [0,0,1],
         [0,0,1]], True],
    [[[0,1],[1,0]], [[1,0],[0,1]], True],
    [[[0,1],[1,1]], [[1,0],[0,1]], False],
    [[[0,0,0],[0,1,0],[1,1,1]], [[1,1,1],[0,1,0],[0,0,0]], True]
]

run_functional_tests(Solution().findRotation, tests)