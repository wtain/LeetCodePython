"""
https://leetcode.com/problems/find-closest-number-to-zero/

Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.



Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 200 ms, faster than 30.55% of Python3 online submissions for Find Closest Number to Zero.
# Memory Usage: 14.1 MB, less than 41.47% of Python3 online submissions for Find Closest Number to Zero.
# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         return min([(abs(n), -n, n) for n in nums])[2]


# Runtime: 157 ms, faster than 79.34% of Python3 online submissions for Find Closest Number to Zero.
# Memory Usage: 14.1 MB, less than 41.47% of Python3 online submissions for Find Closest Number to Zero.
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return -min([(abs(n), -n) for n in nums])[1]


tests = [
    [[-4,-2,1,4,8], 1],
    [[2,-1,1], 1]
]

run_functional_tests(Solution().findClosestNumber, tests)
