"""
https://leetcode.com/problems/merge-sorted-array/
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]


Constraints:

-10^9 <= nums1[i], nums2[i] <= 10^9
nums1.length == m + n
nums2.length == n
"""
from typing import List

"""
Runtime: 32 ms, faster than 92.32% of Python3 online submissions for Merge Sorted Array.
Memory Usage: 13.8 MB, less than 69.88% of Python3 online submissions for Merge Sorted Array.
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        r1 = m-1
        r2 = n-1
        w = m+n-1
        while r1 >= 0 or r2 >= 0:
            if r1 >= 0 and r2 >= 0:
                if nums1[r1] > nums2[r2]:
                    nums1[w] = nums1[r1]
                    r1 -= 1
                    w -=1
                else:
                    nums1[w] = nums2[r2]
                    r2 -= 1
                    w -= 1
            elif r1 >= 0:
                nums1[w] = nums1[r1]
                r1 -= 1
                w -= 1
            else:
                nums1[w] = nums2[r2]
                r2 -= 1
                w -= 1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]

Solution().merge(nums1, 3, nums2, 3)

print(nums1)  # [1,2,2,3,5,6]

