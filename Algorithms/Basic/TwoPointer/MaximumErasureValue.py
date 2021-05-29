"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/601/week-4-may-22nd-may-28th/3758/
https://leetcode.com/problems/maximum-erasure-value/

You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).



Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1280 ms, faster than 62.88% of Python3 online submissions for Maximum Erasure Value.
# Memory Usage: 27.6 MB, less than 83.57% of Python3 online submissions for Maximum Erasure Value.
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        h = set()
        s = 0
        max_s = 0
        i1 = 0
        for i2 in range(n):
            while nums[i2] in h and i1 < i2:
                h.remove(nums[i1])
                s -= nums[i1]
                i1 += 1
            h.add(nums[i2])
            s += nums[i2]
            max_s = max(max_s, s)
        return max_s


tests = [
    [[4,2,4,5,6], 17],
    [[5,2,1,2,5,2,1,2,5], 8]
]

run_functional_tests(Solution().maximumUniqueSubarray, tests)