"""
https://leetcode.com/problems/combination-sum-ii/description/?envType=daily-question&envId=2024-08-13

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 45
# ms
# Beats
# 88.18%
# Analyze Complexity
# Memory
# 16.69
# MB
# Beats
# 30.23%
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def impl(current, t, start):
            if not t:
                result.append(current.copy())
                return
            for i in range(start, len(candidates)):
                if t < candidates[i]:
                    continue
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                current.append(candidates[i])
                impl(current, t - candidates[i], i+1)
                current.pop()

        impl([], target, 0)
        return result


tests = [
    [[10,1,2,7,6,1,5], 8, [
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]],
    [[2,5,2,1,2], 5, [
[1,2,2],
[5]
]],
]

run_functional_tests(Solution().combinationSum2, tests)
