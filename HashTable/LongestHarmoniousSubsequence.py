"""
https://leetcode.com/problems/longest-harmonious-subsequence/
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3628/
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.



Example 1:

Input: nums = [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Example 2:

Input: nums = [1,2,3,4]
Output: 2
Example 3:

Input: nums = [1,1,1,1]
Output: 0


Constraints:

1 <= nums.length <= 2 * 104
-109 <= nums[i] <= 109
"""
from collections import defaultdict
from typing import List


# Runtime: 392 ms, faster than 17.05% of Python3 online submissions for Longest Harmonious Subsequence.
# Memory Usage: 17.7 MB, less than 5.37% of Python3 online submissions for Longest Harmonious Subsequence.
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnts = defaultdict(int)
        maxLen = 0
        for n in nums:
            cnts[n] += 1
            if cnts[n + 1]:
                maxLen = max(maxLen, cnts[n] + cnts[n + 1])
            if cnts[n - 1]:
                maxLen = max(maxLen, cnts[n] + cnts[n - 1])
        return maxLen


tests = [
    ([1,3,2,2,5,2,3,7], 5),
    ([1,2,3,4], 2),
    ([1,1,1,1], 0)
]

for test in tests:
    result = Solution().findLHS(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))