"""
https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3641/

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.



Example 1:

Input: mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
Output: [2,0,3]
Explanation:
The number of soldiers for each row is:
row 0 -> 2
row 1 -> 4
row 2 -> 1
row 3 -> 2
row 4 -> 5
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
Output: [0,2]
Explanation:
The number of soldiers for each row is:
row 0 -> 1
row 1 -> 4
row 2 -> 1
row 3 -> 1
Rows ordered from the weakest to the strongest are [0,2,3,1]


Constraints:

m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
from bisect import bisect_left, bisect
from typing import List


# Runtime: 104 ms, faster than 89.22% of Python3 online submissions for The K Weakest Rows in a Matrix.
# Memory Usage: 14.6 MB, less than 47.53% of Python3 online submissions for The K Weakest Rows in a Matrix.
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        def binsearch_desc(arr: List[int], n: int) -> int:
            l = 0
            r = n
            while l < r:
                m = l + (r - l) // 2
                if arr[m] == 1:
                    l = m + 1
                else:
                    r = m
            return l

        arr = []

        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            j = binsearch_desc(mat[i], n)
            arr.append((j, i))

        return [i for j, i in sorted(arr)][:k]


tests = [
    ([[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 3, [2,0,3]),

    ([[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 2, [0,2])
]

for test in tests:
    result = Solution().kWeakestRows(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))