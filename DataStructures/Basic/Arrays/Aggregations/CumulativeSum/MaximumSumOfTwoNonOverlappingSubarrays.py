"""
https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

Given an array A of non-negative integers, return the maximum sum of elements in two non-overlapping (contiguous) subarrays, which have lengths L and M.  (For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.


Example 1:

Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output: 20
Explanation: One choice of subarrays is [9] with length 1, and [6,5] with length 2.
Example 2:

Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output: 29
Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.
Example 3:

Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output: 31
Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.


Note:

L >= 1
M >= 1
L + M <= A.length <= 1000
0 <= A[i] <= 1000
"""
from typing import List

# Runtime: 108 ms, faster than 27.40% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
# Memory Usage: 14.5 MB, less than 20.51% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
# class Solution:
#     def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
#         n = len(A)
#         ps = [0] * n
#         ps[0] = A[0]
#         for i in range(1, n):
#             ps[i] = ps[i-1] + A[i]
#
#         Msums = [0] * n
#         for i in range(n - M+1):
#             j = i + M
#             Msums[i] = ps[j-1]
#             if i > 0:
#                 Msums[i] -= ps[i-1]
#
#         result = 0
#
#         for i in range(n - L+1):
#             j = i + L
#             Lsum = ps[j-1]  # [i..j-1]
#             if i > 0:
#                 Lsum -= ps[i-1]
#             Msum1 = max(Msums[:i-M+1]) if i-M+1 > 0 else 0
#             Msum2 = max(Msums[j:]) if j < n else 0
#             s = max(Msum1, Msum2)
#             result = max(result, Lsum + s)
#
#         return result


# Runtime: 80 ms, faster than 32.85% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
# Memory Usage: 14.3 MB, less than 77.68% of Python3 online submissions for Maximum Sum of Two Non-Overlapping Subarrays.
class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        ps = [0] * n
        ps[0] = A[0]
        for i in range(1, n):
            ps[i] = ps[i-1] + A[i]

        Msums = [0] * n
        for i in range(n - M+1):
            j = i + M
            Msums[i] = ps[j-1]
            if i > 0:
                Msums[i] -= ps[i-1]

        MsumsMax1 = [0] * n
        MsumsMax2 = [0] * n

        MsumsMax1[0] = Msums[0]
        for i in range(1, n):
            MsumsMax1[i] = max(MsumsMax1[i-1], Msums[i])

        MsumsMax2[n-1] = Msums[n-1]
        for i in range(n-2, -1, -1):
            MsumsMax2[i] = max(MsumsMax2[i + 1], Msums[i])

        result = 0

        for i in range(n - L+1):
            j = i + L
            Lsum = ps[j-1]  # [i..j-1]
            if i > 0:
                Lsum -= ps[i-1]
            # Msum1 = max(Msums[:i-M+1]) if i-M+1 > 0 else 0
            # Msum2 = max(Msums[j:]) if j < n else 0
            Msum1 = MsumsMax1[i-M] if i - M + 1 > 0 else 0
            Msum2 = MsumsMax2[j] if j < n else 0
            s = max(Msum1, Msum2)
            result = max(result, Lsum + s)

        return result


tests = [
    ([8,20,6,2,20,17,6,3,20,8,12], 5, 4, 108),

    ([0,6,5,2,2,5,1,9,4], 1, 2, 20),
    ([3,8,1,3,2,1,8,9,0], 3, 2, 29),
    ([2,1,5,6,0,9,5,0,3,8], 4, 3, 31)
]

for test in tests:
    result = Solution().maxSumTwoNoOverlap(test[0], test[1], test[2])
    if result == test[3]:
        print("PASS")
    else:
        print("FAIL - " + str(result))
