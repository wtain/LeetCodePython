"""
https://leetcode.com/problems/smallest-integer-divisible-by-k/

Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

Return the length of n. If there is no such n, return -1.

Note: n may not fit in a 64-bit signed integer.



Example 1:

Input: k = 1
Output: 1
Explanation: The smallest answer is n = 1, which has length 1.
Example 2:

Input: k = 2
Output: -1
Explanation: There is no such positive integer n divisible by 2.
Example 3:

Input: k = 3
Output: 3
Explanation: The smallest answer is n = 111, which has length 3.


Constraints:

1 <= k <= 105
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 66 ms, faster than 36.04% of Python3 online submissions for Smallest Integer Divisible by K.
# Memory Usage: 17.9 MB, less than 27.03% of Python3 online submissions for Smallest Integer Divisible by K.
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        rem, ln = 1, 1
        seen = set()
        while rem % k != 0:
            n = 10 * rem + 1
            rem = n % k
            ln += 1
            if rem in seen:
                return -1
            else:
                seen.add(rem)
        return ln


tests = [
    [1, 1],
    [2, -1],
    [3, 3]
]

run_functional_tests(Solution().smallestRepunitDivByK, tests)
