"""
https://leetcode.com/problems/duplicate-zeros/
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.



Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]


Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9
"""
from typing import List


# Runtime: 124 ms, faster than 19.76% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 15 MB, less than 35.10% of Python3 online submissions for Duplicate Zeros.
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # n0 = arr.count(0)
        n0 = 0
        n = len(arr)
        for i in range(n):
            if i >= n-n0:
                break
            if arr[i] == 0:
                if i == n-1-n0:
                    arr[n-1] = 0
                    n -= 1
                    break
                n0 += 1
        w = n-1
        r2 = n-n0-1
        for r in range(r2, -1, -1):
            if arr[r] == 0:
                arr[w] = 0
                w -= 1
            arr[w] = arr[r]
            w -= 1

# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         n = len(arr)
#         w = 0
#         r2 = n-1
#         for i, ai in enumerate(arr):
#             if ai == 0:
#                 w += 1
#                 if w == n:
#                     break
#             w += 1
#             if w == n:
#                 break
#         n0 = w - i
#         r2 = i
#         w = n-1
#         for r in range(r2, -1, -1):
#             if arr[r] == 0 and n0:
#                 arr[w] = 0
#                 w -= 1
#                 n0 -= 1
#             arr[w] = arr[r]
#             w -= 1

# Runtime: 140 ms, faster than 18.72% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.7 MB, less than 96.61% of Python3 online submissions for Duplicate Zeros.
# Runtime: 68 ms, faster than 81.78% of Python3 online submissions for Duplicate Zeros.
# Memory Usage: 14.9 MB, less than 67.00% of Python3 online submissions for Duplicate Zeros.
# class Solution:
#     def duplicateZeros(self, arr: List[int]) -> None:
#         """
#         Do not return anything, modify arr in-place instead.
#         """
#         n = len(arr) - 1
#         dups = 0
#         for l in range(n+1):
#             if l > n - dups:
#                 break
#             if arr[l] == 0:
#                 if l == n - dups:
#                     arr[n] = 0
#                     n -= 1
#                     break
#                 dups += 1
#
#         last = n - dups
#
#         for i in range(last, -1, -1):
#             if arr[i] == 0:
#                 arr[i + dups] = 0
#                 dups -= 1
#                 arr[i + dups] = 0
#             else:
#                 arr[i + dups] = arr[i]



tests = [
    ([8,4,5,0,0,0,0,7], [8,4,5,0,0,0,0,0]),

    ([8,4,5,0,0,0,0,7], [8,4,5,0,0,0,0,0]),

    ([1,0,2,3,0,4,5,0], [1,0,0,2,3,0,0,4]),
    ([1,2,3], [1,2,3])
]

for test in tests:
    arr = test[0]
    Solution().duplicateZeros(arr)
    if arr == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(arr))