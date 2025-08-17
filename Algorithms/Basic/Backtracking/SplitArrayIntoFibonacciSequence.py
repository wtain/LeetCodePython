"""
https://leetcode.com/problems/split-array-into-fibonacci-sequence/description/

You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

0 <= f[i] < 231, (that is, each integer fits in a 32-bit signed integer type),
f.length >= 3, and
f[i] + f[i + 1] == f[i + 2] for all 0 <= i < f.length - 2.
Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.



Example 1:

Input: num = "1101111"
Output: [11,0,11,11]
Explanation: The output [110, 1, 111] would also be accepted.
Example 2:

Input: num = "112358130"
Output: []
Explanation: The task is impossible.
Example 3:

Input: num = "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.


Constraints:

1 <= num.length <= 200
num contains only digits.
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


"""
Runtime
247
ms
Beats
5.64%
Analyze Complexity
Memory
17.63
MB
Beats
94.36%
"""
class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:

        def impl(v1, v2, k):
            v3 = v1 + v2
            v = 0
            k0 = k
            while k < n and (v < v3 or k0 == k):
                v = 10 * v + int(num[k])
                if v > 1 << 31:
                    return []
                k += 1
            if v != 0 and num[k0] == '0':
                return []
            if v == v3:
                if k == n:
                    return [v3]
                else:
                    res = impl(v2, v3, k)
                    if res:
                        return [v3] + res

        n = len(num)
        v1 = 0
        for i in range(n-2):
            v1 = 10*v1 + int(num[i])
            v2 = 0
            for j in range(i+1, n-1):
                v2 = 10 * v2 + int(num[j])
                res = impl(v1, v2, j + 1)
                if res:
                    return [v1, v2] + res
                if v2 == 0:
                    break
            if v1 == 0:
                break

        return []


tests = [
    ["121202436", []],
    ["31326395158253411", [31,32,63,95,158,253,411]],
    ["539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", []],
    ["0000", [0, 0, 0, 0]],
    ["11235813", [1,1,2,3,5,8,13]],
    ["123456579", [123,456,579]],
    ["1101111", [11,0,11,11]],
    ["112358130", []],
    ["0123", []],
]

run_functional_tests(Solution().splitIntoFibonacci, tests)
