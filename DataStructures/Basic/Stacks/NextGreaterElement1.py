"""
https://leetcode.com/problems/next-greater-element-i/
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
"""
from typing import List, Dict

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 44 ms, faster than 94.53% of Python3 online submissions for Next Greater Element I.
Memory Usage: 13.9 MB, less than 72.60% of Python3 online submissions for Next Greater Element I.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greaters : Dict[int, int] = {}
        n = len(nums2)
        i = 0
        st = []
        while i < n:
            while len(st) > 0 and st[-1] < nums2[i]:
                greaters[st[-1]] = nums2[i]
                del st[-1]
            st.append(nums2[i])
            i += 1

        m = len(nums1)
        result = [-1] * m
        for i in range(m):
            res = greaters.get(nums1[i])
            if res:
                result[i] = res

        return result


tests = [
    [[4,1,2], [1,3,4,2], [-1,3,-1]],
    [[2,4], [1,2,3,4], [3,-1]]
]

run_functional_tests(Solution().nextGreaterElement, tests)
