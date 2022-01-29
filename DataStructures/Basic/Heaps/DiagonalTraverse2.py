"""
https://leetcode.com/problems/diagonal-traverse-ii/

Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.


Example 1:



Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:



Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]


Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 992 ms, faster than 66.19% of Python3 online submissions for Diagonal Traverse II.
# Memory Usage: 36.8 MB, less than 58.10% of Python3 online submissions for Diagonal Traverse II.
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        h = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                h.append((i+j, -i, nums[i][j]))
        return [v for s, r, v in sorted(h)]


tests = [
    [[[1,2,3],[4,5,6],[7,8,9]], [1,4,2,7,5,3,8,6,9]],
    [[[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]], [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]],
    [[[1,2,3],[4],[5,6,7],[8],[9,10,11]], [1,4,2,5,3,8,6,9,7,10,11]],
    [[[1,2,3,4,5,6]], [1,2,3,4,5,6]]
]

run_functional_tests(Solution().findDiagonalOrder, tests)
