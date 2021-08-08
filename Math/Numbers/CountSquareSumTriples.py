"""
https://leetcode.com/problems/count-square-sum-triples/

A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.



Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).
Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).


Constraints:

1 <= n <= 250
"""
import math

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 772 ms, faster than 44.53% of Python3 online submissions for Count Square Sum Triples.
# Memory Usage: 14.3 MB, less than 19.90% of Python3 online submissions for Count Square Sum Triples.
class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for a in range(1, n+1):
            for b in range(a, n+1):
                c2 = a**2 + b**2
                c = int(math.sqrt(c2))
                if c**2 == c2 and c <= n:
                    cnt += 1
                    if a != b:
                        cnt += 1
        return cnt


tests = [
    [5, 2],
    [10, 4]
]

run_functional_tests(Solution().countTriples, tests)