"""
https://leetcode.com/explore/featured/card/june-leetcoding-challenge-2021/607/week-5-june-29th-june-30th/3796/
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.



Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 640 ms, faster than 48.90% of Python3 online submissions for Max Consecutive Ones III.
# Memory Usage: 14.8 MB, less than 32.26% of Python3 online submissions for Max Consecutive Ones III.
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_len, cnt0 = 0, 0
        l, r = -1, 0
        while r < n:
            if not nums[r]:
                cnt0 += 1
                while l < r and cnt0 > k:
                    l += 1
                    if not nums[l]:
                        cnt0 -= 1
            # print(l, r, cnt0)
            max_len = max(max_len, r - l)
            r += 1
        return max_len


tests = [
    [[0,0,1,1,1,0,0], 0, 3],
    [[1,1,1,0,0,0,1,1,1,1,0], 2, 6],
    [[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3, 10]
]

run_functional_tests(Solution().longestOnes, tests)