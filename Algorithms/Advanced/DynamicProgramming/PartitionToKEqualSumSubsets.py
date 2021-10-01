"""
https://leetcode.com/explore/featured/card/september-leetcoding-challenge-2021/640/week-5-september-29th-september-30th/3993/
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.



Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false


Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

"""
1) PASS, took: 0.000099 on size=7
2) PASS, took: 0.000023 on size=4

1) PASS, took: 0.000188 on size=7
2) PASS, took: 0.000015 on size=4
"""

# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/1494961/Python-dp-on-subsets-explained

# Runtime: 144 ms, faster than 36.80% of Python3 online submissions for Partition to K Equal Sum Subsets.
# Memory Usage: 15.4 MB, less than 8.90% of Python3 online submissions for Partition to K Equal Sum Subsets.
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        n, S = len(nums), sum(nums)
        if S % k:
            return False
        ps = S // k
        nums.sort(key=lambda x: -x)
        m = 1 << n
        states = [False] * m
        sums = [0] * m
        states[0] = True
        for state in range(m):
            if not states[state]:
                continue
            for i in range(n):
                next_state = state | (1 << i)
                if next_state != state and not states[next_state]:
                    if nums[i] <= ps - sums[state] % ps:
                        states[next_state] = True
                        sums[next_state] = sums[state] + nums[i]
                    else:
                        break
        return states[-1]


tests = [
    [[4,3,2,3,5,2,1], 4, True],
    [[1,2,3,4], 3, False]
]

run_functional_tests(Solution().canPartitionKSubsets, tests)