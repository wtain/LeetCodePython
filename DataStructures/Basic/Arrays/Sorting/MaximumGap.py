"""
https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/602/week-5-may-29th-may-31st/3761/
https://leetcode.com/problems/maximum-gap/

Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.



Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 109
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 81.72% of Python3 online submissions for Maximum Gap.
# Memory Usage: 16.6 MB, less than 5.60% of Python3 online submissions for Maximum Gap.
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        lo, hi = min(nums), max(nums)
        if lo == hi:
            return 0
        if n == 2:
            return hi - lo
        buckets = defaultdict(list)
        for ai in nums:
            b = n-2 if ai == hi else (ai-lo) * (n-1) // (hi - lo)
            buckets[b].append(ai)

        cands = [[min(buckets[i]), max(buckets[i])] for i in range(n-1) if buckets[i]]
        return max(y[0] - x[1] for x, y in zip(cands, cands[1:]))


tests = [
    [[3,6,9,1], 3],
    [[10], 0]
]

run_functional_tests(Solution().maximumGap, tests)