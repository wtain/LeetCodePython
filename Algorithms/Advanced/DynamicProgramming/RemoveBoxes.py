"""
https://leetcode.com/problems/remove-boxes/
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/614/week-2-august-8th-august-14th/3889/

You are given several boxes with different colors represented by different positive numbers.

You may experience several rounds to remove boxes until there is no box left. Each time you can choose some continuous boxes with the same color (i.e., composed of k boxes, k >= 1), remove them and get k * k points.

Return the maximum points you can get.



Example 1:

Input: boxes = [1,3,2,2,2,3,4,3,1]
Output: 23
Explanation:
[1, 3, 2, 2, 2, 3, 4, 3, 1]
----> [1, 3, 3, 4, 3, 1] (3*3=9 points)
----> [1, 3, 3, 3, 1] (1*1=1 points)
----> [1, 1] (3*3=9 points)
----> [] (2*2=4 points)
Example 2:

Input: boxes = [1,1,1]
Output: 9
Example 3:

Input: boxes = [1]
Output: 1


Constraints:

1 <= boxes.length <= 100
1 <= boxes[i] <= 100

"""
from functools import lru_cache
from typing import List


# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#
#         def compress(boxes: List[int]) -> List[List[int]]:
#             n = len(boxes)
#             result = []
#             i = 0
#             while i < n:
#                 j = i + 1
#                 while j < n and boxes[i] == boxes[j]:
#                     j += 1
#                 result.append([boxes[i], j-i])
#                 i = j
#             return result
#
#         boxes_compressed = compress(boxes)
#         # print(boxes_compressed)
#
#         def removeBoxesImpl(boxes_compressed: List[List[int]], i1: int, i2: int) -> int:
#             if i1 == i2:
#                 return boxes_compressed[i1][1] ** 2
#             if i1 > i2:
#                 return 0
#             result = 0
#             for i in range(i1+1, i2):
#                 res = boxes_compressed[i][1] ** 2
#                 if boxes_compressed[i-1][0] == boxes_compressed[i+1][0]:
#                     res += removeBoxesImpl(boxes_compressed, i1, i - 2)
#                     res += removeBoxesImpl(boxes_compressed, i + 2, i2)
#                     res += (boxes_compressed[i-1][1] + boxes_compressed[i+1][1]) ** 2
#                 else:
#                     res += removeBoxesImpl(boxes_compressed, i1, i - 1)
#                     res += removeBoxesImpl(boxes_compressed, i + 1, i2)
#                 result = max(res, result)
#
#             return result
#
#         return removeBoxesImpl(boxes_compressed, 0, len(boxes_compressed)-1)

# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#
#         def compress(boxes: List[int]) -> List[List[int]]:
#             n = len(boxes)
#             result = []
#             i = 0
#             while i < n:
#                 j = i + 1
#                 while j < n and boxes[i] == boxes[j]:
#                     j += 1
#                 result.append([boxes[i], j-i])
#                 i = j
#             return result
#
#         boxes_compressed = compress(boxes)
#         n = len(boxes_compressed)
#         dp = [[0] * n for i in range(n)]
#
#         for i in range(n):
#             dp[i][i] = boxes_compressed[i][1] ** 2
#
#         for l in range(1, n+1):
#             for i in range(n-l+1):
#                 j = i + l
#                 mx = dp[i][j-1]
#                 for k in range(i+1, j-1):
#                     v = boxes_compressed[k][1] ** 2
#                     if boxes_compressed[k-1][0] == boxes_compressed[k+1][0]:
#                         v += (boxes_compressed[k-1][1] + boxes_compressed[k+1][1]) ** 2
#                         v += dp[i][k-2] + dp[k+2][j-1]
#                     else:
#                         v += dp[i][k - 1] + dp[k + 1][j - 1]
#                     mx = max(mx, v)
#                 dp[i][j-1] = mx
#
#         return dp[0][n-1]


# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#
#         def compress(boxes: List[int]) -> List[List[int]]:
#             n = len(boxes)
#             result = []
#             i = 0
#             while i < n:
#                 j = i + 1
#                 while j < n and boxes[i] == boxes[j]:
#                     j += 1
#                 result.append([boxes[i], j-i])
#                 i = j
#             return result
#
#         boxes_compressed = compress(boxes)
#         n = len(boxes_compressed)
#         dp = [[[0] * n for i in range(n)] for i in range(n)]
#
#         for i in range(n):
#             dp[i][i] = boxes_compressed[i][1] ** 2
#
#         for l in range(1, n+1):
#             for i in range(n-l+1):
#                 j = i + l
#                 mx = dp[i][j-1]
#                 for k in range(i+1, j-1):
#                     v = boxes_compressed[k][1] ** 2
#                     if boxes_compressed[k-1][0] == boxes_compressed[k+1][0]:
#                         v += (boxes_compressed[k-1][1] + boxes_compressed[k+1][1]) ** 2
#                         v += dp[i][k-2] + dp[k+2][j-1]
#                     else:
#                         v += dp[i][k - 1] + dp[k + 1][j - 1]
#                     mx = max(mx, v)
#                 dp[i][j-1] = mx
#
#         return dp[0][n-1]


from Common.ObjectTestingUtils import run_functional_tests

# Runtime: 2256 ms, faster than 23.84% of Python3 online submissions for Remove Boxes.
# Memory Usage: 102.8 MB, less than 6.22% of Python3 online submissions for Remove Boxes.
# class Solution:
#     def removeBoxes(self, boxes: List[int]) -> int:
#
#         def compress(boxes: List[int]) -> List[List[int]]:
#             n = len(boxes)
#             result = []
#             i = 0
#             while i < n:
#                 j = i + 1
#                 while j < n and boxes[i] == boxes[j]:
#                     j += 1
#                 result.append([boxes[i], j-i])
#                 i = j
#             return result
#
#         boxes_compressed = compress(boxes)
#         n = len(boxes_compressed)
#
#         if n == 1:
#             return boxes_compressed[0][1] ** 2
#
#         n, m = 100, n
#         dp = [[[-1] * n for i in range(n)] for i in range(n)]
#         n = m
#
#         def impl(boxes_compressed: List[List[int]], l: int, r: int, k: int) -> int:
#             nonlocal dp, n
#             if l > r:  # or k >= n:
#                 return 0
#             if dp[l][r][k] != -1:
#                 return dp[l][r][k]
#
#             res = k ** 2 + impl(boxes_compressed, l+1, r, boxes_compressed[l+1][1] if l < r else 0)
#
#             for i in range(l+1, r+1):
#                 if boxes_compressed[i][0] == boxes_compressed[l][0]:
#                     v = impl(boxes_compressed, i, r, k + boxes_compressed[i][1]) + \
#                         impl(boxes_compressed, l+1, i-1, boxes_compressed[l+1][1])
#                     res = max(res, v)
#
#             dp[l][r][k] = res
#
#             return res
#
#         return impl(boxes_compressed, 0, n-1, boxes_compressed[0][1])


# Runtime: 1084 ms, faster than 75.89% of Python3 online submissions for Remove Boxes.
# Memory Usage: 24.7 MB, less than 77.23% of Python3 online submissions for Remove Boxes.
# Runtime: 913 ms
# Memory Usage: 24.8 MB
class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:

        def compress(boxes: List[int]) -> List[List[int]]:
            n = len(boxes)
            result = []
            i = 0
            while i < n:
                j = i + 1
                while j < n and boxes[i] == boxes[j]:
                    j += 1
                result.append([boxes[i], j-i])
                i = j
            return result

        boxes_compressed = compress(boxes)
        n = len(boxes_compressed)

        if n == 1:
            return boxes_compressed[0][1] ** 2

        n, m = 100, n
        n = m

        @lru_cache(None)
        def impl(l: int, r: int, k: int) -> int:
            nonlocal boxes_compressed, n
            if l > r:  # or k >= n:
                return 0

            res = k ** 2 + impl(l+1, r, boxes_compressed[l+1][1] if l < r else 0)

            for i in range(l+1, r+1):
                if boxes_compressed[i][0] == boxes_compressed[l][0]:
                    v = impl(i, r, k + boxes_compressed[i][1]) + \
                        impl(l+1, i-1, boxes_compressed[l+1][1])
                    res = max(res, v)

            return res

        return impl(0, n-1, boxes_compressed[0][1])


tests = [
    [[1,2,2,1,1,1,2,1,1,2,1,2,1,1,2,2,1,1,2,2,1,1,1,2,2,2,2,1,2,1,1,2,2,1,2,1,2,2,2,2,2,1,2,1,2,2,1,1,1,2,2,1,2,1,2,2,1,2,1,1,1,2,2,2,2,2,1,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,1,1,1,1,2,2,1,1,1,1,1,1,1,2,1,2,2,1], 2758],

    [[1,2], 2],

    [[1,3,2,2,2,3,4,3,1], 23],
    [[1,1,1], 9],
    [[1], 1]
]

run_functional_tests(Solution().removeBoxes, tests)