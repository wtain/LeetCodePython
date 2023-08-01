"""
https://leetcode.com/problems/combinations/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# Details
# 274ms
# Beats 79.40%of users with Python3
# Memory
# Details
# 18.20mb
# Beats 90.06%of users with Python3
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def impl(k, r, start):
            if not k:
                results.append(r)
                return
            for i in range(start, n):
                impl(k-1, r + [i+1], i+1)

        impl(k, [], 0)

        return results


tests = [
    [4, 2, [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]],
    [1, 1, [[1]]],
]

run_functional_tests(Solution().combine, tests)
