"""
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.



Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.


Constraints:

2 <= k <= 9
1 <= n <= 60
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 53 ms, faster than 29.27% of Python3 online submissions for Combination Sum III.
# Memory Usage: 13.9 MB, less than 79.39% of Python3 online submissions for Combination Sum III.
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def impl(k: int, n: int, current: List[int], low):
            nonlocal results
            if n < 0:
                return
            if not k:
                if not n:
                    results.append(current)
                return
            for i in range(low, 10):
                impl(k-1, n-i, current + [i], i+1)

        impl(k, n, [], 1)
        return results


tests = [
    [3, 7, [[1,2,4]]],
    [3, 9, [[1,2,6],[1,3,5],[2,3,4]]],
    [4, 1, []]
]

run_functional_tests(Solution().combinationSum3, tests)
