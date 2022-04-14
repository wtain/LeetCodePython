"""
https://leetcode.com/problems/count-hills-and-valleys-in-an-array/

You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

Return the number of hills and valleys in nums.



Example 1:

Input: nums = [2,4,1,1,6,5]
Output: 3
Explanation:
At index 0: There is no non-equal neighbor of 2 on the left, so index 0 is neither a hill nor a valley.
At index 1: The closest non-equal neighbors of 4 are 2 and 1. Since 4 > 2 and 4 > 1, index 1 is a hill.
At index 2: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 2 is a valley.
At index 3: The closest non-equal neighbors of 1 are 4 and 6. Since 1 < 4 and 1 < 6, index 3 is a valley, but note that it is part of the same valley as index 2.
At index 4: The closest non-equal neighbors of 6 are 1 and 5. Since 6 > 1 and 6 > 5, index 4 is a hill.
At index 5: There is no non-equal neighbor of 5 on the right, so index 5 is neither a hill nor a valley.
There are 3 hills and valleys so we return 3.
Example 2:

Input: nums = [6,6,5,5,4,1]
Output: 0
Explanation:
At index 0: There is no non-equal neighbor of 6 on the left, so index 0 is neither a hill nor a valley.
At index 1: There is no non-equal neighbor of 6 on the left, so index 1 is neither a hill nor a valley.
At index 2: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 2 is neither a hill nor a valley.
At index 3: The closest non-equal neighbors of 5 are 6 and 4. Since 5 < 6 and 5 > 4, index 3 is neither a hill nor a valley.
At index 4: The closest non-equal neighbors of 4 are 5 and 1. Since 4 < 5 and 4 > 1, index 4 is neither a hill nor a valley.
At index 5: There is no non-equal neighbor of 1 on the right, so index 5 is neither a hill nor a valley.
There are 0 hills and valleys so we return 0.


Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 73 ms, faster than 16.63% of Python3 online submissions for Count Hills and Valleys in an Array.
# Memory Usage: 14 MB, less than 25.61% of Python3 online submissions for Count Hills and Valleys in an Array.
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        prev = nums[0]
        i = 1
        while i < n-1:
            current = nums[i]
            while i < n-1 and nums[i] == nums[i+1]:
                i += 1
            if i >= n-1:
                break
            if current < prev and current < nums[i+1] or \
               current > prev and current > nums[i+1]:
                cnt += 1
            prev = current
            i += 1
        return cnt


tests = [
    [[2,4,1,1,6,5], 3],
    [[6,6,5,5,4,1], 0]
]

run_functional_tests(Solution().countHillValley, tests)
