"""
https://leetcode.com/explore/featured/card/july-leetcoding-challenge-2021/609/week-2-july-8th-july-14th/3812/
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 104 ms, faster than 6.36% of Python3 online submissions for Find Peak Element.
# Memory Usage: 14.5 MB, less than 11.34% of Python3 online submissions for Find Peak Element.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m+1
        return l


tests = [
    [
        [1,2,3,1], 2
    ],
    [
        [1,2,1,3,5,6,4], 5
    ]
]

run_functional_tests(Solution().findPeakElement, tests)