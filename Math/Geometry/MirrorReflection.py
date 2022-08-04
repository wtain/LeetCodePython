"""
https://leetcode.com/problems/mirror-reflection/

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.



Example 1:


Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.
Example 2:

Input: p = 3, q = 1
Output: 1


Constraints:

1 <= q <= p <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 52 ms, faster than 41.58% of Python3 online submissions for Mirror Reflection.
# Memory Usage: 13.9 MB, less than 63.37% of Python3 online submissions for Mirror Reflection.
# https://leetcode.com/problems/mirror-reflection/discuss/2376161/Java-Solution
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1


tests = [
    [2, 1, 2],
    [3, 1, 1]
]

run_functional_tests(Solution().mirrorReflection, tests)
