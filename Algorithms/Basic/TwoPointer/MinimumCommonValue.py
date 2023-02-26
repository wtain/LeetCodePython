"""
https://leetcode.com/problems/minimum-common-value/

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.



Example 1:

Input: nums1 = [1,2,3], nums2 = [2,4]
Output: 2
Explanation: The smallest element common to both arrays is 2, so we return 2.
Example 2:

Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
Output: 2
Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.


Constraints:

1 <= nums1.length, nums2.length <= 105
1 <= nums1[i], nums2[j] <= 109
Both nums1 and nums2 are sorted in non-decreasing order.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 478 ms
# Beats
# 71.24%
# Memory
# 32.2 MB
# Beats
# 95.18%
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        i1, i2 = 0, 0
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            if nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return -1


tests = [
    [[1,2,3], [2,4], 2],
    [[1,2,3,6], [2,3,4,5], 2],
]

run_functional_tests(Solution().getCommon, tests)
