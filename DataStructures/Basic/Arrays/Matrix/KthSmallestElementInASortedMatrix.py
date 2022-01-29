"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3805/
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given an n x n matrix where each of the rows and columns are sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.



Example 1:

Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
Example 2:

Input: matrix = [[-5]], k = 1
Output: -5


Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 300
-109 <= matrix[i][j] <= 109
All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order.
1 <= k <= n2
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         l, r = 1, 2*n
#         while l < r:
#             m = l + (r-l) // 2
#             cnt = m * (m+1) // 2
#             if k > cnt:
#                 l = m+1
#             else:
#                 r = m
#         if l >= n:
#             i0 = l - n
#             j0 = n-1
#         else:
#             i0 = 0
#             j0 = l-1
#
#         k -= l * (l-1) // 2
#         k -= 1
#
#         h = []
#         while i0 < n:
#             h.append(matrix[i0][j0])
#             i0 += 1
#             j0 -= 1
#
#         heapq.heapify(h)
#
#         for i in range(k):
#             heapq.heappop(h)
#
#         return h[0]

# Runtime: 204 ms, faster than 54.40% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20 MB, less than 93.49% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         h = []
#         for i in range(n):
#             for j in range(n):
#                 heapq.heappush(h, -matrix[i][j])
#                 if len(h) > k:
#                     heapq.heappop(h)
#         return -h[0]


# Runtime: 200 ms, faster than 59.31% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20.1 MB, less than 49.80% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         n = len(matrix)
#         h = []
#         for i in range(n):
#             heapq.heappush(h, (matrix[i][0], i, 0))
#
#         for _ in range(k-1):
#             v, i, j = heapq.heappop(h)
#             j += 1
#             if j < n:
#                 heapq.heappush(h, (matrix[i][j], i, j))
#
#         return h[0][0]


# Runtime: 160 ms, faster than 93.08% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# Memory Usage: 20 MB, less than 78.34% of Python3 online submissions for Kth Smallest Element in a Sorted Matrix.
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/1321862/Python-Binary-search-solution-explained
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n, l, r = len(matrix), matrix[0][0], matrix[-1][-1]

        def check(mid: int) -> int:
            i, j, cnt = 0, n-1, 0
            for i in range(n):
                while j >= 0 and matrix[i][j] > mid:
                    j -= 1
                cnt += j + 1
            return cnt

        while l < r:
            mid = l + (r - l) // 2
            if check(mid) < k:
                l = mid + 1
            else:
                r = mid

        return l


tests = [
    [[[1,3,5],[6,7,12],[11,14,14]], 3, 5],
    [[[1,2],[1,3]], 3, 2],
    [[[1,5,9],[10,11,13],[12,13,15]], 8, 13],
    [[[-5]], 1, -5]
]


run_functional_tests(Solution().kthSmallest, tests)