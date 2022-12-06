"""
https://leetcode.com/problems/number-of-unequal-triplets-in-array/

You are given a 0-indexed array of positive integers nums. Find the number of triplets (i, j, k) that meet the following conditions:

0 <= i < j < k < nums.length
nums[i], nums[j], and nums[k] are pairwise distinct.
In other words, nums[i] != nums[j], nums[i] != nums[k], and nums[j] != nums[k].
Return the number of triplets that meet the conditions.



Example 1:

Input: nums = [4,4,2,4,3]
Output: 3
Explanation: The following triplets meet the conditions:
- (0, 2, 4) because 4 != 2 != 3
- (1, 2, 4) because 4 != 2 != 3
- (2, 3, 4) because 2 != 4 != 3
Since there are 3 triplets, we return 3.
Note that (2, 0, 4) is not a valid triplet because 2 > 0.
Example 2:

Input: nums = [1,1,1,1,1]
Output: 0
Explanation: No triplets meet the conditions so we return 0.


Constraints:

3 <= nums.length <= 100
1 <= nums[i] <= 1000
"""
from collections import Counter
from itertools import accumulate
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 378 ms
# Beats
# 88.27%
# Memory
# 13.9 MB
# Beats
# 16.77%
# class Solution:
#     def unequalTriplets(self, nums: List[int]) -> int:
#         counter = Counter(nums)
#         values = list(counter.values())
#         result = 0
#         n = len(values)
#         if n < 3:
#             return 0
#         for i in range(n-2):
#             for j in range(i+1, n-1):
#                 for k in range(j+1, n):
#                     result += values[i] * values[j] * values[k]
#         return result


# Runtime
# 45 ms
# Beats
# 97.99%
# Memory
# 13.8 MB
# Beats
# 62.67%
# https://leetcode.com/problems/number-of-unequal-triplets-in-array/solutions/2831702/o-n/
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        s = list(accumulate(Counter(nums).values()))
        return sum(s[i-1] * (s[i] - s[i-1]) * (s[-1]-s[i]) for i in range(1, len(s)))


tests = [
    [[4,4,2,4,3], 3],
    [[1,1,1,1,1], 0]
]

run_functional_tests(Solution().unequalTriplets, tests)
