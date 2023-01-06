"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].



Example 1:

Input: arr = [1,2,3,5], k = 3
Output: [2,5]
Explanation: The fractions to be considered in sorted order are:
1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
The third fraction is 2/5.
Example 2:

Input: arr = [1,7], k = 1
Output: [1,7]


Constraints:

2 <= arr.length <= 1000
1 <= arr[i] <= 3 * 104
arr[0] == 1
arr[i] is a prime number for i > 0.
All the numbers of arr are unique and sorted in strictly increasing order.
1 <= k <= arr.length * (arr.length - 1) / 2


Follow up: Can you solve the problem with better than O(n2) complexity?
"""
import heapq
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 3297 ms
# Beats
# 37.35%
# Memory
# 105.5 MB
# Beats
# 16.18%
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         n = len(arr)
#         h = []
#         for j in range(n):
#             for i in range(j):
#                 heapq.heappush(h, (-arr[i] / arr[j], [arr[i], arr[j]]))
#                 if len(h) > k:
#                     heapq.heappop(h)
#         return h[0][1]


# DOESN'T WORK
# https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/115819/summary-of-solutions-for-problems-reducible-to-leetcode-378/
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         n = len(arr)
#         index = list(range(n))
#         L = [0] * (12 * n)
#
#         def pick(nums, l, r, k):
#             pos = partition(nums, l, r, medianOfMedians(nums, l, r))
#
#             p, q = pos[0], pos[1]
#
#             if q - l < k:
#                 return pick(nums, q, r, k - (q-l))
#             elif k <= p - l:
#                 return pick(nums, l, p, k)
#             return p
#
#         def partition(nums, l, r, pos):
#             pivot = nums[pos]
#             nums[pos], nums[r-1] = nums[r-1], nums[pos]
#             p, q = l, r - 1
#             i = l
#             while i < q:
#                 if nums[i] < pivot:
#                     nums[p], nums[i] = nums[i], nums[p]
#                     i += 1
#                     p += 1
#                 elif nums[i] > pivot:
#                     nums[i], nums[q] = nums[q], nums[i]
#                     q -= 1
#                 else:
#                     i += 1
#
#             nums[q], nums[r-1] = nums[r-1], nums[q]
#             q += 1
#             return [p, q]
#
#         def medianOfMedians(nums, l, r):
#             if l - r <= 5:
#                 return medianOfFive(nums, l, r)
#
#             rr = l
#
#             for i in range(l, r, 5):
#                 mi = medianOfFive(nums, i, min(i+5, r))
#                 nums[rr], nums[mi] = nums[mi], nums[rr]
#                 rr += 1
#
#             return pick(nums, l, rr, (rr - l + 1) // 2)
#
#         def medianOfFive(nums, l, r):
#             nums[l:r] = sorted(nums[l:r])
#             return l + (r - l - 1) // 2
#
#         def biselect(index, k1: int, k2: int):
#             nonlocal arr, L, n
#             if n <= 2:
#                 nums = [0] * (n * n)
#
#                 k = 0
#                 for i in range(n):
#                     for j in range(i+1, n):
#                         nums[k] = arr[index[i]] / arr[index[j]]
#                         k += 1
#
#                 nums.sort()
#
#                 return [nums[k1-1], nums[k2-1]]
#
#             index_ = [0] * ((n+1)//2+(n-1) % 2)
#             k1_, k2_ = 0, (k2 + 3) // 4
#             k = 0
#             for i in range(0, n, 2):
#                 index_[k] = index[i]
#                 k += 1
#
#             if n % 2 == 0:
#                 index_[-1] = index[n-1]
#                 k1_ = (k1 + 3) // 4 + n + 1
#             else:
#                 k1_ = (k1 + 2*n) // 4 + 1
#
#             pair = biselect(index_, k1_, k2_)
#             a, b = pair[0], pair[1]
#             ra_less, rb_more = 0, 0
#
#             Len = 0
#
#             ja, jb = n, n
#             for i in range(n):
#                 while ja > 0 and arr[index[i]] / arr[index[ja-1]] >= a:
#                     ja -= 1
#                 ra_less += ja
#
#                 while jb > 0 and arr[index[i]] / arr[index[jb-1]] > b:
#                     jb -= 1
#                 rb_more += n - jb
#
#                 for j in range(jb, ja):
#                     L[Len] = arr[index[i]] / arr[index[j]]
#                     Len += 1
#
#             x, y = 0, 0
#
#             if ra_less <= k1 - 1:
#                 x = a
#             elif k1 + rb_more - n * n <= 0:
#                 x = b
#             else:
#                 x = L[pick(L, 0, Len, k1 + rb_more - n*n)]
#
#             if ra_less <= k2 - 1:
#                 y = a
#             elif k2 + rb_more - n*n <= 0:
#                 y = b
#             else:
#                 y = L[pick(L, 0, Len, k2 + rb_more - n*n)]
#
#             return [x, y]
#
#         return biselect(index, k, k)[0]


# Runtime
# 101 ms
# Beats
# 97.10%
# Memory
# 13.9 MB
# Beats
# 97.51%
# https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/115819/summary-of-solutions-for-problems-reducible-to-leetcode-378/
# class Solution:
#     def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
#         l, r = 0, 1
#         p, q = 0, 1
#         n = len(arr)
#         while True:
#             p = 0
#             cnt = 0
#             m = (l + r) / 2
#
#             j = n-1
#             for i in range(n):
#                 while j >= 0 and arr[i] > m * arr[n - 1 - j]:
#                     j -= 1
#                 cnt += (j + 1)
#
#                 if j >= 0 and p * arr[n-1-j] < q * arr[i]:
#                     p = arr[i]
#                     q = arr[n - 1 - j]
#
#             if cnt < k:
#                 l = m
#             elif cnt > k:
#                 r = m
#             else:
#                 return [p, q]


# Runtime
# 5535 ms
# Beats
# 13.29%
# Memory
# 14 MB
# Beats
# 92.12%
# https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/115819/summary-of-solutions-for-problems-reducible-to-leetcode-378/
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        row, col = 0, n-1
        while True:
            cnt_le, cnt_lt = 0, 0
            j = n-1
            p = n-1
            for i in range(n):
                while j >= 0 and arr[i] * arr[n - 1 - col] > arr[n-1-j] * arr[row]:
                    j -= 1
                cnt_le += j + 1

                while p >= 0 and arr[i] * arr[n-1-col] >= arr[n-1-p] * arr[row]:
                    p -= 1
                cnt_lt += p + 1

            if cnt_le < k:
                row += 1
            elif cnt_lt >= k:
                col -= 1
            else:
                return [arr[row], arr[n - 1 - col]]



tests = [
    [[1,2,3,5], 3, [2,5]],
    [[1,7], 1, [1,7]],
]

run_functional_tests(Solution().kthSmallestPrimeFraction, tests)
