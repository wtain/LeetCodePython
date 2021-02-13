"""
https://leetcode.com/problems/prime-arrangements/
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: n = 5
Output: 12
Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
Example 2:

Input: n = 100
Output: 682289015


Constraints:

1 <= n <= 100
"""
from math import sqrt


# Runtime: 40 ms, faster than 17.97% of Python3 online submissions for Prime Arrangements.
# Memory Usage: 14.2 MB, less than 83.98% of Python3 online submissions for Prime Arrangements.
class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        mod = 10**9 + 7
        facts = [0] * 101
        facts[0] = 1
        for i in range(1, 101):
            facts[i] = i * facts[i-1] % mod

        def isPrime(x: int) -> bool:
            if x == 1:
                return False
            sx = int(sqrt(x))
            for i in range(2, sx+1):
                if x % i == 0:
                    return False
            return True

        np = 0
        nc = 0
        for i in range(1, n+1):
            if isPrime(i):
                np += 1
            else:
                nc += 1

        return facts[np] * facts[nc] % mod


tests = [
    (5, 12),
    (100, 682289015)
]

for test in tests:
    result = Solution().numPrimeArrangements(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL - " + str(result))