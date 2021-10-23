"""
https://leetcode.com/problems/hamming-distance/
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""
from Common.ObjectTestingUtils import run_functional_tests

"""
Runtime: 24 ms, faster than 96.62% of Python3 online submissions for Hamming Distance.
Memory Usage: 14 MB, less than 16.24% of Python3 online submissions for Hamming Distance.
"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        while x > 0 or y > 0:
            xi = x & 1
            yi = y & 1
            if xi != yi:
                cnt += 1
            x //= 2
            y //= 2
        return cnt


tests = [
    [1, 4, 2]
]

run_functional_tests(Solution().hammingDistance, tests)
