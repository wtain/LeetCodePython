"""
https://leetcode.com/problems/sort-array-by-parity/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.



Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 104 ms, faster than 51.59% of Python3 online submissions for Sort Array By Parity.
# Memory Usage: 14.7 MB, less than 17.91% of Python3 online submissions for Sort Array By Parity.
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i1, i2 = 0, n-1
        result = [0] * n
        for v in nums:
            if v % 2 == 0:
                result[i1] = v
                i1 += 1
            else:
                result[i2] = v
                i2 -= 1
        return result


tests = [
    [[3,1,2,4], [2,4,3,1]],
    [[0], [0]]
]


def is_sorted_by_parity(arr) -> bool:
    i, n = 0, len(arr)
    while i < n and arr[i] % 2 == 0:
        i += 1
    while i < n and arr[i] % 2 == 1:
        i += 1
    return i == n


def customCheck(test, result) -> bool:
    if sorted(test[0]) != sorted(result):
        return False
    return is_sorted_by_parity(result)

run_functional_tests(Solution().sortArrayByParity, tests, custom_check=customCheck)
