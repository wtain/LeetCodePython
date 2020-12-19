"""
https://leetcode.com/problems/peak-index-in-a-mountain-array/
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].



Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2


Constraints:

3 <= arr.length <= 104
0 <= arr[i] <= 106
arr is guaranteed to be a mountain array.


Runtime: 76 ms, faster than 49.89% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 15.3 MB, less than 26.91% of Python3 online submissions for Peak Index in a Mountain Array.
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l = 1
        r = n - 1

        def isPos(i: int) -> bool:
            return arr[i] - arr[i - 1] > 0

        while l < r:
            m = l + int((r - l) / 2)
            if isPos(m):
                l = m+1
            else:
                r = m
        return l-1


tests = [
    ([0, 1, 0], 1),
    ([0, 2, 1, 0], 1),
    ([0, 10, 5, 2], 1),
    ([3, 4, 5, 1], 2),
    ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2)
]

for test in tests:
    result = Solution().peakIndexInMountainArray(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL")
