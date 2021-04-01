"""
https://leetcode.com/problems/intersection-of-two-arrays/
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""
from bisect import bisect_left
from typing import List


"""
Runtime: 60 ms, faster than 39.57% of Python3 online submissions for Intersection of Two Arrays.
Memory Usage: 14 MB, less than 35.93% of Python3 online submissions for Intersection of Two Arrays.
"""
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.intersection(nums2, nums1)
        snums2 = sorted(nums2)
        result = []
        seen = set()
        for a in nums1:
            if a in seen:
                continue
            j = bisect_left(snums2, a)
            if j < len(snums2) and snums2[j] == a:
                result.append(a)
            seen.add(a)
        return result


print(Solution().intersection([1,2,2,1], [2,2]))  # 2
print(Solution().intersection([4,9,5], [9,4,9,8,4]))  # 9 4
