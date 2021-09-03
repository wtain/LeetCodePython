"""
https://leetcode.com/explore/featured/card/august-leetcoding-challenge-2021/617/week-5-august-29th-august-31st/3956/
https://leetcode.com/problems/patching-array/

Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.



Example 1:

Input: nums = [1,3], n = 6
Output: 1
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.
Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].
Example 3:

Input: nums = [1,2,2], n = 5
Output: 0


Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
nums is sorted in ascending order.
1 <= n <= 231 - 1
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 1216 ms, faster than 5.18% of Python3 online submissions for Patching Array.
# Memory Usage: 15.1 MB, less than 5.70% of Python3 online submissions for Patching Array.
# https://leetcode.com/problems/patching-array/discuss/1432422/Python-2-solutions%3A-merge-intervals-%2B-greedy-explained
# class Solution:
#
#     def merge(self, intervals):
#         intervals.sort()
#         merged = []
#         for interval in intervals:
#             if not merged or merged[-1][1] < interval[0] - 1:
#                 merged.append(interval)
#             else:
#                 merged[-1][1] = max(merged[-1][1], interval[1])
#         return merged
#
#     def minPatches(self, nums: List[int], n: int) -> int:
#         ints, patches = [[0,0]], 0
#         for num in nums:
#             ints = self.merge(ints + [[i+num, j+num] for i, j in ints])
#
#         while ints[0][1] < n:
#             ints = self.merge(ints + [[i+ints[0][1]+1, j+ints[0][1]+1] for i,j in ints])
#             patches += 1
#         return patches


# Runtime: 60 ms, faster than 68.39% of Python3 online submissions for Patching Array.
# Memory Usage: 14.4 MB, less than 63.21% of Python3 online submissions for Patching Array.
# https://leetcode.com/problems/patching-array/discuss/1432422/Python-2-solutions%3A-merge-intervals-%2B-greedy-explained
class Solution:

    def minPatches(self, nums: List[int], n: int) -> int:
        reach, result, index = 0, 0, 0
        while reach < n:
            if index < len(nums) and nums[index] <= reach + 1:
                reach += nums[index]
                index += 1
            else:
                result += 1
                reach = 2 * reach + 1
        return result


tests = [
    [[1, 3], 6, 1],
    [[1,5,10], 20, 2],
    [[1,2,2], 5, 0]
]

run_functional_tests(Solution().minPatches, tests)