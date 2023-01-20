"""
https://leetcode.com/problems/non-decreasing-subsequences/description/

array with at least two elements. You may return the answer in any order.



Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]


Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 247 ms
# Beats
# 62.50%
# Memory
# 25.2 MB
# Beats
# 13.91%
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:

        results = []
        solution = []
        hashes = set()

        def impl(start_index, hash):
            nonlocal results, solution, hashes
            if len(solution) >= 2:
                if hash not in hashes:
                    hashes.add(hash)
                    results.append(solution.copy())

            for i in range(start_index, len(nums)):
                if solution and solution[-1] > nums[i]:
                    continue
                solution.append(nums[i])
                impl(i+1, 201 * hash + (101+nums[i]))
                solution.pop()

        impl(0, 0)

        return results


tests = [
    [[4,6,7,7], [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]],
    [[4,4,3,2,1], [[4,4]]],
]

run_functional_tests(Solution().findSubsequences, tests)
