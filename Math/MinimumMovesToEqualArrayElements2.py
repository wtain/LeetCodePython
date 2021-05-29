"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/600/week-3-may-15th-may-21st/3748/
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.



Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
Example 2:

Input: nums = [1,10,2,9]
Output: 16


Constraints:

n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 64 ms, faster than 96.25% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
# Memory Usage: 15.4 MB, less than 43.75% of Python3 online submissions for Minimum Moves to Equal Array Elements II.
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        n2 = n // 2
        m = nums[n2]
        cnt = 0
        for a in nums:
            cnt += abs(m - a)
        return cnt


tests = [
    [[1,2,3], 2],
    [[1,10,2,9], 16]
]

run_functional_tests(Solution().minMoves2, tests)