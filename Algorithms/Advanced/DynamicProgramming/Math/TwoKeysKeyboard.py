"""
https://leetcode.com/problems/2-keys-keyboard/description/?envType=daily-question&envId=2024-08-19

There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.



Example 1:

Input: n = 3
Output: 3
Explanation: Initially, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.
Example 2:

Input: n = 1
Output: 0


Constraints:

1 <= n <= 1000
"""
from Common.ObjectTestingUtils import run_functional_tests


# Runtime
# 34
# ms
# Beats
# 89.52%
# Analyze Complexity
# Memory
# 16.47
# MB
# Beats
# 88.15%
class Solution:
    def minSteps(self, n: int) -> int:
        result, d = 0, 2
        while n > 1:
            while n % d == 0:
                result += d
                n //= d
            d += 1
        return result


tests = [
    [3, 3],
    [1, 0],
]

run_functional_tests(Solution().minSteps, tests)
