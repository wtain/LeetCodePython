"""
https://leetcode.com/problems/count-largest-group/

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.



Example 1:

Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.
Example 2:

Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.
Example 3:

Input: n = 15
Output: 6
Example 4:

Input: n = 24
Output: 5


Constraints:

1 <= n <= 10^4
"""
from collections import defaultdict

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 88 ms, faster than 81.57% of Python3 online submissions for Count Largest Group.
# Memory Usage: 14.3 MB, less than 40.44% of Python3 online submissions for Count Largest Group.
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        max_cnt = 0

        for i in range(1, n+1):
            s = 0
            while i:
                s += i % 10
                i //= 10
            d[s] = d[s] + 1
            max_cnt = max(max_cnt, d[s])

        return sum(1 for v in d.values() if v == max_cnt)


tests = [
    [13, 4],
    [2, 2],
    [15, 6],
    [24, 5]
]

run_functional_tests(Solution().countLargestGroup, tests)