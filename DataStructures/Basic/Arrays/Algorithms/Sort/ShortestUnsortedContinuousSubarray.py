"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/587/week-4-february-22nd-february-28th/3652/
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105


Follow up: Can you solve it in O(n) time complexity?
"""
from typing import List


# Runtime: 204 ms, faster than 68.88% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
# Memory Usage: 15.3 MB, less than 90.56% of Python3 online submissions for Shortest Unsorted Continuous Subarray.
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        nmax, nmin = nums[0], nums[n-1]
        r, l = 0, 1
        for i in range(1, n):
            if nums[i] < nmax:
                r = i
            else:
                nmax = max(nmax, nums[i])
        for i in range(n-2, -1, -1):
            if nums[i] > nmin:
                l = i
            else:
                nmin = min(nmin, nums[i])
        return r - l + 1


tests = [
    ([2,6,4,8,10,9,15], 5),
    ([1,2,3,4], 0),
    ([1], 0)
]

for test in tests:
    result = Solution().findUnsortedSubarray(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))