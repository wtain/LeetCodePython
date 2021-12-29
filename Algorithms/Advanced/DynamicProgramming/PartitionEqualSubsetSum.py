"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests

# https://leetcode.com/submissions/detail/359414597/
# Runtime: 2572 ms, faster than 29.64% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 29.7 MB, less than 38.96% of Python3 online submissions for Partition Equal Subset Sum.
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n, S = len(nums), sum(nums)
#         if S % 2:
#             return False
#         ps = S // 2
#         dp = [[False] * (ps+1) for _ in range(n+1)]
#         dp[0][0] = True
#         for i in range(1, n+1):
#             for j in range(1, ps+1):
#                 if nums[i-1] <= j:
#                     dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]
#                 else:
#                     dp[i][j] = dp[i-1][j]
#         return dp[n][ps]


# Runtime: 2272 ms, faster than 34.14% of Python3 online submissions for Partition Equal Subset Sum.
# Memory Usage: 14.3 MB, less than 89.69% of Python3 online submissions for Partition Equal Subset Sum.
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n, S = len(nums), sum(nums)
        if S % 2:
            return False
        ps = S // 2
        dp = [[False] * (ps+1) for _ in range(2)]
        dp[0][0] = True
        for i in range(1, n+1):
            i1 = i % 2
            i2 = 1 - i1
            for j in range(1, ps+1):
                if nums[i-1] <= j:
                    dp[i1][j] = dp[i2][j] or dp[i2][j - nums[i-1]]
                else:
                    dp[i1][j] = dp[i2][j]
        return dp[n % 2][ps]


# https://leetcode.com/problems/partition-equal-subset-sum/discuss/1624815/C%2B%2B-solved-with-bitset-and-OR-operation-TC-O(n*(n32))-99-faster-space-97-optimized
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         n, S = len(nums), sum(nums)
#         if S % 2:
#             return False
#         ps = S // 2
#         dp = [[False] * (ps+1) for _ in range(2)]
#         dp[0][0] = True
#         for i in range(1, n+1):
#             i1 = i % 2
#             i2 = 1 - i1
#             for j in range(1, ps+1):
#                 if nums[i-1] <= j:
#                     dp[i1][j] = dp[i2][j] or dp[i2][j - nums[i-1]]
#                 else:
#                     dp[i1][j] = dp[i2][j]
#         return dp[n % 2][ps]


tests = [
    [[1,5,11,5], True],
    [[1,2,3,5], False]
]

run_functional_tests(Solution().canPartition, tests)
