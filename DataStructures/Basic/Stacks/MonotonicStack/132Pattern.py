"""
https://leetcode.com/problems/132-pattern/

Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.



Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.
Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Constraints:

n == nums.length
1 <= n <= 2 * 105
-109 <= nums[i] <= 109
"""
import bisect
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def find132pattern(self, nums: List[int]) -> bool:
#         inc = []
#         for v in nums:
#             if len(inc) >= 2:
#                 i = bisect.bisect_right(inc, v)
#                 if 0 < i < len(inc):
#                     if inc[i] != v:
#                         print(inc[i], v, inc[-1])
#                         return True
#             while inc and inc[-1] > v:
#                 inc.pop()
#             inc.append(v)
#         return False


# Runtime: 364 ms, faster than 72.85% of Python3 online submissions for 132 Pattern.
# Memory Usage: 32.6 MB, less than 9.36% of Python3 online submissions for 132 Pattern.
# https://leetcode.com/problems/132-pattern/discuss/1541296/O(n)-or-C%2B%2B-or-Easy-to-understand
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        mins = [0] * n
        mins[0] = nums[0]
        for i in range(1, n):
            mins[i] = min(mins[i-1], nums[i])
        st = []
        for j in range(n-1, -1, -1):
            if nums[j] > mins[j]:
                while st and st[-1] <= mins[j]:
                    st.pop()
                if st and st[-1] < nums[j]:
                    return True
                st.append(nums[j])
        return False


tests = [
    [[1,2,3,4], False],
    [[3,1,4,2], True],
    [[-1,3,2,0], True],

    [[1, 2, 3, 2], True],

    [[3,5,0,3,4], True],

    [[1,0,1,-4,-3], False]
]

run_functional_tests(Solution().find132pattern, tests)