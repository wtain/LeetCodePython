"""
https://leetcode.com/problems/keep-multiplying-found-values-by-two/

You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.



Example 1:

Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation:
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
Example 2:

Input: nums = [2,7,9], original = 4
Output: 4
Explanation:
- 4 is not found in nums. Thus, 4 is returned.


Constraints:

1 <= nums.length <= 1000
1 <= nums[i], original <= 1000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 123 ms, faster than 21.00% of Python3 online submissions for Keep Multiplying Found Values by Two.
# Memory Usage: 14.3 MB, less than 24.29% of Python3 online submissions for Keep Multiplying Found Values by Two.
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        snums = set(nums)
        v = original
        while v in snums:
            v *= 2
        return v


tests = [
    [[5,3,6,1,12], 3, 24],
    [[2,7,9], 4, 4]
]

run_functional_tests(Solution().findFinalValue, tests)
