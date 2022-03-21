"""
https://leetcode.com/problems/sort-even-and-odd-indices-independently/


You are given a 0-indexed integer array nums. Rearrange the values of nums according to the following rules:

Sort the values at odd indices of nums in non-increasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [4,3,2,1] after. The values at odd indices 1 and 3 are sorted in non-increasing order.
Sort the values at even indices of nums in non-decreasing order.
For example, if nums = [4,1,2,3] before this step, it becomes [2,1,4,3] after. The values at even indices 0 and 2 are sorted in non-decreasing order.
Return the array formed after rearranging the values of nums.



Example 1:

Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation:
First, we sort the values present at odd indices (1 and 3) in non-increasing order.
So, nums changes from [4,1,2,3] to [4,3,2,1].
Next, we sort the values present at even indices (0 and 2) in non-decreasing order.
So, nums changes from [4,1,2,3] to [2,3,4,1].
Thus, the array formed after rearranging the values is [2,3,4,1].
Example 2:

Input: nums = [2,1]
Output: [2,1]
Explanation:
Since there is exactly one odd index and one even index, no rearrangement of values takes place.
The resultant array formed is [2,1], which is the same as the initial array.


Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""
from functools import reduce
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 60 ms, faster than 83.86% of Python3 online submissions for Sort Even and Odd Indices Independently.
# Memory Usage: 13.8 MB, less than 75.33% of Python3 online submissions for Sort Even and Odd Indices Independently.
# class Solution:
#     def sortEvenOdd(self, nums: List[int]) -> List[int]:
#         odd = nums[1::2]
#         even = nums[::2]
#         n = len(nums)
#         odd.sort(key=lambda x: -x)
#         even.sort()
#         even += [0]
#         odd += [0]
#         return reduce(lambda res, v: res + v, [[e, o] for o, e in zip(odd, even)], [])[:n]


# Runtime: 60 ms, faster than 83.86% of Python3 online submissions for Sort Even and Odd Indices Independently.
# Memory Usage: 13.9 MB, less than 75.33% of Python3 online submissions for Sort Even and Odd Indices Independently.
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        return reduce(lambda res, v: res + v, [[e, o] for o, e in zip(sorted(nums[1::2], key=lambda x: -x) + [0], sorted(nums[::2]) + [0])], [])[:len(nums)]


tests = [
    [[1], [1]],
    [[5,39,33,5,12,27,20,45,14,25,32,33,30,30,9,14,44,15,21], [5,45,9,39,12,33,14,30,20,27,21,25,30,15,32,14,33,5,44]],
    [[4,1,2,3], [2,3,4,1]],
    [[2,1], [2,1]]
]

run_functional_tests(Solution().sortEvenOdd, tests)
