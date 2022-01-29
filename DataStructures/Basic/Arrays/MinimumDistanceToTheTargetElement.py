"""
https://leetcode.com/problems/minimum-distance-to-the-target-element/

Given an integer array nums (0-indexed) and two integers target and start, find an index i such that nums[i] == target and abs(i - start) is minimized. Note that abs(x) is the absolute value of x.

Return abs(i - start).

It is guaranteed that target exists in nums.



Example 1:

Input: nums = [1,2,3,4,5], target = 5, start = 3
Output: 1
Explanation: nums[4] = 5 is the only value equal to target, so the answer is abs(4 - 3) = 1.
Example 2:

Input: nums = [1], target = 1, start = 0
Output: 0
Explanation: nums[0] = 1 is the only value equal to target, so the answer is abs(0 - 0) = 0.
Example 3:

Input: nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
Output: 0
Explanation: Every value of nums is 1, but nums[0] minimizes abs(i - start), which is abs(0 - 0) = 0.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
0 <= start < nums.length
target is in nums.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 56 ms, faster than 71.88% of Python3 online submissions for Minimum Distance to the Target Element.
# Memory Usage: 14.5 MB, less than 9.07% of Python3 online submissions for Minimum Distance to the Target Element.
# class Solution:
#     def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
#         min_dist = math.inf
#         for i, v in enumerate(nums):
#             if v != target:
#                 continue
#             dist = abs(i-start)
#             min_dist = min(min_dist, dist)
#         return min_dist

# Runtime: 60 ms, faster than 42.00% of Python3 online submissions for Minimum Distance to the Target Element.
# Memory Usage: 14.4 MB, less than 69.75% of Python3 online submissions for Minimum Distance to the Target Element.
class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        return min(abs(i-start) for i, v in enumerate(nums) if v == target)


tests = [
    [[1,2,3,4,5], 5, 3, 1],
    [[1], 1, 0, 0],
    [[1,1,1,1,1,1,1,1,1,1], 1, 0, 0]
]

run_functional_tests(Solution().getMinDistance, tests)