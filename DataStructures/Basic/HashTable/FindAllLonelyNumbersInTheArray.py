"""
https://leetcode.com/problems/find-all-lonely-numbers-in-the-array/

You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.



Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation:
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.
Example 2:

Input: nums = [1,3,5,3]
Output: [1,5]
Explanation:
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 106
"""
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 1440 ms
# Beats
# 76.51%
# Memory
# 48.5 MB
# Beats
# 5.73%
# class Solution:
#     def findLonely(self, nums: List[int]) -> List[int]:
#         lonely, seen = set(), set()
#         for v in nums:
#             if v not in seen:
#                 lonely.add(v)
#             else:
#                 if v-1 in lonely:
#                     lonely.remove(v-1)
#                 if v in lonely:
#                     lonely.remove(v)
#                 if v + 1 in lonely:
#                     lonely.remove(v+1)
#             seen.add(v)
#             seen.add(v - 1)
#             seen.add(v + 1)
#
#         return list(lonely)

# Runtime
# 1485 ms
# Beats
# 67.91%
# Memory
# 52.2 MB
# Beats
# 5.16%
class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        lonely, seen = set(), set()
        for v in nums:
            if v not in seen:
                lonely.add(v)
            else:
                if v-1 in lonely:
                    lonely.remove(v-1)
                if v in lonely:
                    lonely.remove(v)
                if v + 1 in lonely:
                    lonely.remove(v+1)
            seen.add(v)
            seen.add(v - 1)
            seen.add(v + 1)

        return lonely


tests = [
    [[10,6,5,8], [10,8]],
    [[1,3,5,3], [1,5]],
]

run_functional_tests(Solution().findLonely, tests, custom_check=compareSets)
