"""
https://leetcode.com/problems/find-target-indices-after-sorting-array/

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.



Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.


Constraints:

1 <= nums.length <= 100
1 <= nums[i], target <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 59 ms, faster than 57.62% of Python3 online submissions for Find Target Indices After Sorting Array.
# Memory Usage: 13.8 MB, less than 90.00% of Python3 online submissions for Find Target Indices After Sorting Array.
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        l, e, g = 0, 0, 0
        for v in nums:
            if v < target:
                l += 1
            elif v > target:
                g += 1
            else:
                e += 1
        if not e:
            return []
        return list(range(l, l+e))


tests = [
    [[1,2,5,2,3], 2, [1,2]],
    [[1,2,5,2,3], 3, [3]],
    [[1,2,5,2,3], 5, [4]]
]

run_functional_tests(Solution().targetIndices, tests)
