"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i < j < nums.length
|nums[i] - nums[j]| == k
Notice that |val| denotes the absolute value of val.



Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).


Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 80 ms, faster than 76.16% of Python3 online submissions for K-diff Pairs in an Array.
# Memory Usage: 15.2 MB, less than 98.31% of Python3 online submissions for K-diff Pairs in an Array.
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        cnt = 0
        for i in range(n-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            a1, a2 = nums[i], nums[i] + k
            idx = bisect.bisect_left(nums, a2, i+1)
            if i+1 <= idx < n and nums[idx] == a2:
                cnt += 1
        return cnt


tests = [
    [[3,1,4,1,5], 2, 2],
    [[1,2,3,4,5], 1, 4],
    [[1,3,1,5,4], 0, 1]
]

run_functional_tests(Solution().findPairs, tests)
