"""
https://leetcode.com/problems/minimum-numbers-of-function-calls-to-make-target-array/

You are given an integer array nums. You have an integer array arr of the same length with all values set to 0 initially. You also have the following modify function:


You want to use the modify function to covert arr to nums using the minimum number of calls.

Return the minimum number of function calls to make nums from arr.

The test cases are generated so that the answer fits in a 32-bit signed integer.



Example 1:

Input: nums = [1,5]
Output: 5
Explanation: Increment by 1 (second element): [0, 0] to get [0, 1] (1 operation).
Double all the elements: [0, 1] -> [0, 2] -> [0, 4] (2 operations).
Increment by 1 (both elements)  [0, 4] -> [1, 4] -> [1, 5] (2 operations).
Total of operations: 1 + 2 + 2 = 5.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Increment by 1 (both elements) [0, 0] -> [0, 1] -> [1, 1] (2 operations).
Double all the elements: [1, 1] -> [2, 2] (1 operation).
Total of operations: 2 + 1 = 3.
Example 3:

Input: nums = [4,2,5]
Output: 6
Explanation: (initial)[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5](nums).


Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 831 ms
# Beats
# 47.94%
# Memory
# 24.6 MB
# Beats
# 5.79%
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        arr = [v for v in nums if v]
        while arr:
            # print(" ".join(bin(v).replace("0b", "") for v in arr))
            next_arr = []
            for v in arr:
                if v & 1:
                    result += 1
                v >>= 1
                if v:
                    next_arr.append(v)
            if next_arr:
                result += 1
            arr = next_arr
        return result


tests = [
    [[1,5], 5],
    [[2,2], 3],
    [[4,2,5], 6],
]

run_functional_tests(Solution().minOperations, tests)
