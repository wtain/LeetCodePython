"""
https://leetcode.com/problems/number-of-arithmetic-triplets/

You are given a 0-indexed, strictly increasing integer array nums and a positive integer diff. A triplet (i, j, k) is an arithmetic triplet if the following conditions are met:

i < j < k,
nums[j] - nums[i] == diff, and
nums[k] - nums[j] == diff.
Return the number of unique arithmetic triplets.



Example 1:

Input: nums = [0,1,4,6,7,10], diff = 3
Output: 2
Explanation:
(1, 2, 4) is an arithmetic triplet because both 7 - 4 == 3 and 4 - 1 == 3.
(2, 4, 5) is an arithmetic triplet because both 10 - 7 == 3 and 7 - 4 == 3.
Example 2:

Input: nums = [4,5,6,7,8,9], diff = 2
Output: 2
Explanation:
(0, 2, 4) is an arithmetic triplet because both 8 - 6 == 2 and 6 - 4 == 2.
(1, 3, 5) is an arithmetic triplet because both 9 - 7 == 2 and 7 - 5 == 2.


Constraints:

3 <= nums.length <= 200
0 <= nums[i] <= 200
1 <= diff <= 50
nums is strictly increasing.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 70 ms
# Beats
# 75.54%
# Memory
# 13.9 MB
# Beats
# 19.40%
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        h = set(nums)
        cnt = 0
        for v in h:
            if v+diff in h and v+2*diff in h:
                cnt += 1
        return cnt


tests = [
    [[0,1,4,6,7,10], 3, 2],
    [[4,5,6,7,8,9], 2, 2]
]

run_functional_tests(Solution().arithmeticTriplets, tests)
