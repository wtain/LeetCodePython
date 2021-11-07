"""
https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

Given an integer array nums and an integer k, return the number of pairs (i, j) where i < j such that |nums[i] - nums[j]| == k.

The value of |x| is defined as:

x if x >= 0.
-x if x < 0.


Example 1:

Input: nums = [1,2,2,1], k = 1
Output: 4
Explanation: The pairs with an absolute difference of 1 are:
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
Example 2:

Input: nums = [1,3], k = 3
Output: 0
Explanation: There are no pairs with an absolute difference of 3.
Example 3:

Input: nums = [3,2,1,5,4], k = 2
Output: 3
Explanation: The pairs with an absolute difference of 2 are:
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
1 <= k <= 99
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 101 ms, faster than 68.15% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
# Memory Usage: 14.2 MB, less than 53.64% of Python3 online submissions for Count Number of Pairs With Absolute Difference K.
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        vals = [0] * 301
        cnt = 0
        for v in nums:
            cnt += vals[100+v-k] + vals[100+v+k]
            vals[100+v] += 1
        return cnt


tests = [
    [[1,2,2,1], 1, 4],
    [[1,3], 3, 0],
    [[3,2,1,5,4], 2, 3],
    [[33,90,62,43,21,96,20,18,84,74,61,100,5,11,4,67,96,18,6,68,82,32,76,33,93,33,71,32,30,63,37,46,95,51,63,77,63,84,52,78,66,76,66,9,73,92,79,65,29,42], 64, 11]
]

run_functional_tests(Solution().countKDifference, tests)