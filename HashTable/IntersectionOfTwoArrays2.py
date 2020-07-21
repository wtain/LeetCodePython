"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
"""
from bisect import bisect_left
from typing import List, Dict

"""
Runtime: 124 ms, faster than 6.07% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 14 MB, less than 41.55% of Python3 online submissions for Intersection of Two Arrays II.
"""

"""
class Solution:

    @staticmethod
    def intersectHist(h1: Dict[int, int], h2: Dict[int, int]) -> List[int]:
        if len(h1) > len(h2):
            return Solution.intersectHist(h2, h1)
        result = []
        for a in h1:
            cnt = h1[a]
            cnt2 = h2.get(a) or 0
            cnt = min(cnt, cnt2)
            for i in range(cnt):
                result.append(a)
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def getHist(nums: List[int]):
            result = {}
            for a in nums:
                cnt = result.get(a) or 0
                result[a] = cnt + 1
            return result
        h1 = getHist(nums1)
        h2 = getHist(nums2)
        return Solution.intersectHist(h1, h2)
"""

"""
Runtime: 80 ms, faster than 25.06% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.9 MB, less than 56.27% of Python3 online submissions for Intersection of Two Arrays II.
"""
"""
class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = sorted(nums1)
        snums2 = sorted(nums2)
        i2 = 0
        result = []
        for a in snums1:
            i = bisect_left(snums2, a, i2)
            if i < len(snums2) and snums2[i] == a:
                result.append(a)
                i2 = i + 1

        return result
"""

"""
Runtime: 116 ms, faster than 7.30% of Python3 online submissions for Intersection of Two Arrays II.
Memory Usage: 13.9 MB, less than 55.15% of Python3 online submissions for Intersection of Two Arrays II.
"""
class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        snums1 = sorted(nums1)
        snums2 = sorted(nums2)
        i2 = 0
        result = []
        n1 = len(snums1)
        n2 = len(snums2)
        i1 = 0
        while i1 < n1:
            a = snums1[i1]
            cnt1 = 0
            while i1 < n1 and snums1[i1] == a:
                i1 += 1
                cnt1 += 1
            i2 = bisect_left(snums2, a, i2)
            cnt2 = 0
            while i2 < n2 and snums2[i2] == a:
                cnt2 += 1
                if cnt2 <= cnt1:
                    result.append(a)
                i2 += 1

        return result


print(Solution().intersect([1,2,2,1], [2,2]))  # 2 2
print(Solution().intersect([1,2,2,1], [2,2,2]))  # 2 2
print(Solution().intersect([1,2,2,2,1], [2,2,2]))  # 2 2 2
print(Solution().intersect([1,2,2,2,1], [2,2]))  # 2 2
print(Solution().intersect([4,9,5], [9,4,9,8,4]))  # 4 9
