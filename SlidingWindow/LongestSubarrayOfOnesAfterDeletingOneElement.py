"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array.

Return 0 if there is no such subarray.



Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0


Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
"""
from typing import List


# Runtime: 396 ms, faster than 52.62% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
# Memory Usage: 16.8 MB, less than 53.81% of Python3 online submissions for Longest Subarray of 1's After Deleting One Element.
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        prev = 0
        curr = 0
        for i in range(n):
            if nums[i] == 1:
                curr += 1
                result = max(result, curr + prev)
            else:
                prev = curr
                curr = 0
        if result == n:
            result -= 1
        return result


tests = [
    ([1,0,0,0,0], 1),

    ([1,1,0,1], 3),
    ([0,1,1,1,0,1,1,0,1], 5),
    ([1,1,1], 2),
    ([1,1,0,0,1,1,1,0,1], 4),
    ([0,0,0], 0)
]

for test in tests:
    result = Solution().longestSubarray(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))