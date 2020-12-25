"""
https://leetcode.com/problems/diagonal-traverse/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3580/

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.



Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Explanation:



Note:

The total number of elements of the given matrix will not exceed 10,000.

Runtime: 184 ms, faster than 89.90% of Python3 online submissions for Diagonal Traverse.
Memory Usage: 16.8 MB, less than 51.85% of Python3 online submissions for Diagonal Traverse.
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []
        N = len(matrix[0])
        result = []
        i = 0
        j = 0
        direction_up_right = True
        for k in range(M*N):
            result.append(matrix[i][j])
            if direction_up_right:
                if i > 0 and j < N-1:
                    i -= 1
                    j += 1
                else:
                    if j < N-1:
                        j += 1
                    else:
                        i += 1
                    direction_up_right = False
            else:
                if i < M-1 and j > 0:
                    i += 1
                    j -= 1
                else:
                    if i < M-1:
                        i += 1
                    else:
                        j += 1
                    direction_up_right = True

        return result

result0 = Solution().findDiagonalOrder([
])  # []
print(result0)

result1 = Solution().findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])  # [1,2,4,7,5,3,6,8,9]
print(result1)

result2 = Solution().findDiagonalOrder([
 [ 1,  2,  3,  4 ],
 [ 5,  6,  7,  8 ],
 [ 9, 10, 11, 12 ]
])  # [1,2,4,7,5,3,6,8,9]
print(result2)