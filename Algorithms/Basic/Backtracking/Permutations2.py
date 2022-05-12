"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""
from collections import defaultdict
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 49 ms, faster than 99.18% of Python3 online submissions for Permutations II.
# Memory Usage: 14.5 MB, less than 10.49% of Python3 online submissions for Permutations II.
# https://leetcode.com/submissions/detail/203996683/
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1

        def impl(current: List[int]):
            nonlocal result, nums, counts
            for p in counts:
                if not counts[p]:
                    continue
                counts[p] -= 1
                current.append(p)
                if len(current) == len(nums):
                    result.append(current.copy())
                else:
                    impl(current)
                current.pop()
                counts[p] += 1

        impl([])

        return result


tests = [
    [
        [1,1,2],
        [[1,1,2],
         [1,2,1],
         [2,1,1]]
    ],
    [
        [1,2,3],
        [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    ]
]

run_functional_tests(Solution().permuteUnique, tests)
