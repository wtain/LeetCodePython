"""
https://leetcode.com/problems/count-nice-pairs-in-an-array/description/?envType=daily-question&envId=2023-11-21

You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

0 <= i < j < nums.length
nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
Return the number of nice pairs of indices. Since that number can be too large, return it modulo 109 + 7.



Example 1:

Input: nums = [42,11,1,97]
Output: 2
Explanation: The two pairs are:
 - (0,3) : 42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121.
 - (1,2) : 11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12.
Example 2:

Input: nums = [13,10,35,24,76]
Output: 4


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 644
# ms
# Beats
# 30.03%
# of users with Python3
# Memory
# 26.94
# MB
# Beats
# 21.53%
# of users with Python3
# https://leetcode.com/problems/count-nice-pairs-in-an-array/editorial/?envType=daily-question&envId=2023-11-21
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        def rev(num):
            result = 0
            while num:
                result = 10 * result + num % 10
                num //= 10
            return result

        arr = []
        for i in range(len(nums)):
            arr.append(nums[i] - rev(nums[i]))
        dic = defaultdict(int)
        result = 0
        MOD = 10 ** 9 + 7
        for num in arr:
            result = (result + dic[num]) % MOD
            dic[num] += 1
        return result


tests = [
    [[42,11,1,97], 2],
    [[13,10,35,24,76], 4],
]

run_functional_tests(Solution().countNicePairs, tests)
