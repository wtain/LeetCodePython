"""
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/

You are given three positive integers: n, index, and maxSum. You want to construct an array nums (0-indexed) that satisfies the following conditions:

nums.length == n
nums[i] is a positive integer where 0 <= i < n.
abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
The sum of all the elements of nums does not exceed maxSum.
nums[index] is maximized.
Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.



Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].
Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3


Constraints:

1 <= n <= maxSum <= 109
0 <= index < n
"""
from Common.ObjectTestingUtils import run_functional_tests

# Runtime
# 50 ms
# Beats
# 54.20%
# Memory
# 16.3 MB
# Beats
# 53.44%
# https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/editorial/
class Solution:

    def getsum(self, index, value, n):
        count = 0
        if value > index:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1

        if value >= n - index:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value

        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getsum(index, mid, n) <= maxSum:
                left = mid
            else:
                right = mid - 1
        return left


tests = [
    [4, 2, 6, 2],
    [6, 1, 10, 3],
]

run_functional_tests(Solution().maxValue, tests)
