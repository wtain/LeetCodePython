"""
https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/

You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.



Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations.
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.


Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
"""
from collections import Counter, defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests



# Runtime
# 1430 ms
# Beats
# 53.97%
# Memory
# 35 MB
# Beats
# 14.29%
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        if n == 2:
            return 0 if nums[0] != nums[1] else 1
        cnt_even, cnt_odd = defaultdict(int), defaultdict(int)
        for i, v in enumerate(nums):
            if i % 2:
                cnt_odd[v] += 1
            else:
                cnt_even[v] += 1
        even = [(cnt_even[v], v) for v in cnt_even]
        odd = [(cnt_odd[v], v) for v in cnt_odd]
        even.sort(reverse=True)
        odd.sort(reverse=True)
        if even[0][1] == odd[0][1]:
            v1 = n - even[0][0] - odd[1][0] if len(odd) > 1 else n // 2
            v2 = n - even[1][0] - odd[0][0] if len(even) > 1 else n // 2
            return min(v1, v2)

        return n - even[0][0] - odd[0][0]


tests = [
    [[2,2,2,2], 2],
    [[2,2], 1],
    [[3,1,3,2,4,3], 3],
    [[1,2,2,2,2], 2],
]

run_functional_tests(Solution().minimumOperations, tests)
