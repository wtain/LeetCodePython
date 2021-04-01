"""
https://leetcode.com/problems/increasing-triplet-subsequence/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/571/week-3-december-15th-december-21st/3570/
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1


Follow up: Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

Runtime: 56 ms, faster than 46.89% of Python3 online submissions for Increasing Triplet Subsequence.
Memory Usage: 14.9 MB, less than 7.12% of Python3 online submissions for Increasing Triplet Subsequence.
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [0] * n
        maxs = [0] * n
        for i in range(n):
            minv = nums[i]
            if i > 0:
                minv = min(minv, mins[i-1])
            mins[i] = minv
        for i in range(n-1, -1, -1):
            maxv = nums[i]
            if i < n-1:
                maxv = max(maxv, maxs[i+1])
            maxs[i] = maxv
        for i in range(1, n-1):
            if nums[i] > mins[i-1] and nums[i] < maxs[i+1]:
                return True
        return False


print(Solution().increasingTriplet([1,2,3,4,5]))  # true
print(Solution().increasingTriplet([5,4,3,2,1]))  # false
print(Solution().increasingTriplet([2,1,5,0,4,6]))  # true