"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/582/week-4-january-22nd-january-28th/3616/
https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
Given an array nums of 0s and 1s and an integer k, return True if all 1's are at least k places away from each other, otherwise return False.



Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true


Constraints:

1 <= nums.length <= 105
0 <= k <= nums.length
nums[i] is 0 or 1
"""
from typing import List


# Runtime: 592 ms, faster than 31.54% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
# Memory Usage: 17 MB, less than 64.65% of Python3 online submissions for Check If All 1's Are at Least Length K Places Away.
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k < 1:
            return True
        last1 = -k-1
        for i, v in enumerate(nums):
            if v == 1:
                if i - last1 <= k:
                    return False
                last1 = i
        return True


tests = [
    ([1,0,0,0,1,0,0,1], 2, True),
    ([1,0,0,1,0,1], 2, False),
    ([1,1,1,1,1], 0, True),
    ([0,1,0,1], 1, True),
]

for test in tests:
    result = Solution().kLengthApart(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL")
