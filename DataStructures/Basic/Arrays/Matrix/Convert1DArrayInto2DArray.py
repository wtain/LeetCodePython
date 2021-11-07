"""
https://leetcode.com/problems/convert-1d-array-into-2d-array/

You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.



Example 1:


Input: original = [1,2,3,4], m = 2, n = 2
Output: [[1,2],[3,4]]
Explanation:
The constructed 2D array should contain 2 rows and 2 columns.
The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array.
The second group of n=2 elements in original, [3,4], becomes the second row in the constructed 2D array.
Example 2:

Input: original = [1,2,3], m = 1, n = 3
Output: [[1,2,3]]
Explanation:
The constructed 2D array should contain 1 row and 3 columns.
Put all three elements in original into the first row of the constructed 2D array.
Example 3:

Input: original = [1,2], m = 1, n = 1
Output: []
Explanation:
There are 2 elements in original.
It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D array.
Example 4:

Input: original = [3], m = 1, n = 2
Output: []
Explanation:
There is 1 element in original.
It is impossible to make 1 element fill all the spots in a 1x2 2D array, so return an empty 2D array.


Constraints:

1 <= original.length <= 5 * 104
1 <= original[i] <= 105
1 <= m, n <= 4 * 104
"""
from typing import List


from numpy.core import reshape

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1020 ms, faster than 82.58% of Python3 online submissions for Convert 1D Array Into 2D Array.
# Memory Usage: 21.5 MB, less than 88.81% of Python3 online submissions for Convert 1D Array Into 2D Array.
# class Solution:
#     def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
#         if len(original) != m*n:
#             return []
#         i = j = 0
#         result = [[0] * n for _ in range(m)]
#         for v in original:
#             result[i][j] = v
#             j += 1
#             if j == n:
#                 j = 0
#                 i += 1
#         return result


# Runtime: 1080 ms, faster than 63.51% of Python3 online submissions for Convert 1D Array Into 2D Array.
# Memory Usage: 38.5 MB, less than 5.15% of Python3 online submissions for Convert 1D Array Into 2D Array.
from numpy import array
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        return array(original).reshape([m, n]).tolist()


tests = [
    [[1,2,3,4], 2, 2, [[1,2],[3,4]]],
    [[1,2,3], 1, 3, [[1,2,3]]],
    [[1,2], 1, 1, []],
    [[3], 1, 2, []]
]

run_functional_tests(Solution().construct2DArray, tests)