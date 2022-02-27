"""
https://leetcode.com/problems/combination-sum/

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 85 ms, faster than 74.22% of Python3 online submissions for Combination Sum.
# Memory Usage: 13.7 MB, less than 99.90% of Python3 online submissions for Combination Sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()
        n = len(candidates)
        to_visit = [(0, target, [])]
        while to_visit:
            min_index, tgt, path = to_visit.pop()
            for i in range(min_index, n):
                if candidates[i] > tgt:
                    break
                nx = (i, tgt - candidates[i], path + [candidates[i]])
                if not nx[1]:
                    results.append(nx[2])
                elif nx[1] > 0:
                    to_visit.append(nx)
        return results


tests = [
    [[2,3,6,7], 7,  [[2,2,3],[7]]],
    [[2,3,5], 8,  [[2,2,2,2],[2,3,3],[3,5]]],
    [[2], 1, []]
]

run_functional_tests(Solution().combinationSum, tests, custom_check=compareSets)
