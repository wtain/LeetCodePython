"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3713/
https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The answer is guaranteed to fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000


Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 32 ms, faster than 96.94% of Python3 online submissions for Combination Sum IV.
# Memory Usage: 14.1 MB, less than 98.21% of Python3 online submissions for Combination Sum IV.
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target+1):
            v = 0
            for n in nums:
                if n > i:
                    continue
                v += dp[i-n]
            dp[i] = v
        return dp[target]


tests = [
    [
        [1,2,3], 4, 7
    ],
    [
        [9], 3, 0
    ]
]

run_functional_tests(Solution().combinationSum4, tests)