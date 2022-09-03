"""
https://leetcode.com/problems/numbers-with-same-consecutive-differences/

Return all non-negative integers of length n such that the absolute difference between every two consecutive digits is k.

Note that every number in the answer must not have leading zeros. For example, 01 has one leading zero and is invalid.

You may return the answer in any order.



Example 1:

Input: n = 3, k = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.
Example 2:

Input: n = 2, k = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]


Constraints:

2 <= n <= 9
0 <= k <= 9
"""
from typing import List

from Common.Helpers.ResultComparators import compareSets
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 80 ms, faster than 27.21% of Python3 online submissions for Numbers With Same Consecutive Differences.
# Memory Usage: 14.2 MB, less than 73.81% of Python3 online submissions for Numbers With Same Consecutive Differences.
# https://leetcode.com/submissions/detail/382711241/
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = list(range(10))
        for i in range(1, n):
            result_next = []
            for x in result:
                if not x:
                    continue
                d = x % 10
                d1, d2 = d + k, d - k
                if d1 <= 9:
                    result_next.append(10 * x + d1)
                if d2 >= 0 and k:
                    result_next.append(10 * x + d2)
            result = result_next
        return result


tests = [
    [3, 7, [181,292,707,818,929]],
    [2, 1, [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]]
]

run_functional_tests(Solution().numsSameConsecDiff, tests, custom_check=compareSets)
