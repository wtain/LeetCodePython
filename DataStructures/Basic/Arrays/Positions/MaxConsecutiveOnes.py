"""
https://leetcode.com/problems/max-consecutive-ones/
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/638/week-3-september-15th-september-21st/3982/
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 532 ms, faster than 23.19% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14 MB, less than 70.27% of Python3 online submissions for Max Consecutive Ones.
Runtime: 356 ms, faster than 63.20% of Python3 online submissions for Max Consecutive Ones.
Memory Usage: 14.4 MB, less than 48.55% of Python3 online submissions for Max Consecutive Ones.
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        current = 0
        for ni in nums:
            if ni == 1:
                current += 1
                result = max(result, current)
            else:
                current = 0
        return result


tests = [
    [[1,1,0,1,1,1], 3]
]

run_functional_tests(Solution().findMaxConsecutiveOnes, tests)
