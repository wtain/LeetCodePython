"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=daily-question&envId=2023-09-21

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 97ms
# Beats 30.36%of users with Python3
# Memory
# Details
# 17.78MB
# Beats 9.53%of users with Python3
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#
#         def findKthElement(k, b1, e1, b2, e2):
#             l1, l2 = e1 - b1 + 1, e2 - b2 + 1
#             if not l1:
#                 return nums2[b2 + k]
#             if not l2:
#                 return nums1[b1 + k]
#             if not k:
#                 return min(nums1[b1], nums2[b2])
#             mid1 = l1 * k // (l1 + l2)
#             mid2 = k - mid1 - 1
#             mid1 += b1
#             mid2 += b2
#             if nums1[mid1] > nums2[mid2]:
#                 k -= mid2 - b2 + 1
#                 e1 = mid1
#                 b2 = mid2 + 1
#             else:
#                 k -= mid1 - b1 + 1
#                 e2 = mid2
#                 b1 = mid1 + 1
#             return findKthElement(k, b1, e1, b2, e2)
#
#         n1 = len(nums1)
#         n2 = len(nums2)
#         n = n1 + n2
#         k = n // 2
#         if n % 2 == 1:
#             return findKthElement(k, 0, n1-1, 0, n2-1)
#         return (findKthElement(k-1, 0, n1-1, 0, n2-1) + findKthElement(k, 0, n1-1, 0, n2-1)) / 2.0


# Runtime
# Details
# 91ms
# Beats 57.84%of users with Python3
# Memory
# Details
# 16.31MB
# Beats 99.03%of users with Python3
# https://leetcode.com/problems/median-of-two-sorted-arrays/editorial/?envType=daily-question&envId=2023-09-21
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        INF_NEG = float('-inf')
        INF_POS = float('inf')

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partA = (left + right) // 2
            partB = (m + n + 1) // 2 - partA

            maxLeftA = INF_NEG if partA == 0 else nums1[partA - 1]
            minRightA = INF_POS if partA == m else nums1[partA]
            maxLeftB = INF_NEG if partB == 0 else nums2[partB - 1]
            minRightB = INF_POS if partB == n else nums2[partB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m+n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                right = partA - 1
            else:
                left = partA + 1


tests = [
    [[1,3], [2], 2.0],
    [[1,2], [3, 4], 2.5],
]

run_functional_tests(Solution().findMedianSortedArrays, tests)
