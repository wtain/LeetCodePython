"""
https://leetcode.com/problems/split-with-minimum-sum/submissions/1738559902/

Given a positive integer num, split it into two non-negative integers num1 and num2 such that:

The concatenation of num1 and num2 is a permutation of num.
In other words, the sum of the number of occurrences of each digit in num1 and num2 is equal to the number of occurrences of that digit in num.
num1 and num2 can contain leading zeros.
Return the minimum possible sum of num1 and num2.

Notes:

It is guaranteed that num does not contain any leading zeros.
The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.


Example 1:

Input: num = 4325
Output: 59
Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59. We can prove that 59 is indeed the minimal possible sum.
Example 2:

Input: num = 687
Output: 75
Explanation: We can split 687 so that num1 is 68 and num2 is 7, which would give an optimal sum of 75.


Constraints:

10 <= num <= 109
"""
from Common.ObjectTestingUtils import run_functional_tests


"""
Runtime
1
ms
Beats
10.17%
Analyze Complexity
Memory
17.88
MB
Beats
36.44%
"""
# class Solution:
#     def splitNum(self, num: int) -> int:
#         v1 = v2 = 0
#         s = list(sorted(str(num)))
#         n = len(s)
#         for i in range(0, n, 2):
#             v1 *= 10
#             v1 += int(s[i])
#             if i+1 < n:
#                 v2 *= 10
#                 v2 += int(s[i+1])
#         return v1 + v2


"""
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
17.61
MB
Beats
84.18%
"""
class Solution:
    def splitNum(self, num: int) -> int:
        v1 = v2 = 0
        s = [int(d) for d in str(num)]
        s.sort()
        n = len(s)
        for i in range(0, n, 2):
            v1 *= 10
            v1 += s[i]
            if i+1 < n:
                v2 *= 10
                v2 += s[i+1]
        return v1 + v2


tests = [
    [4325, 59],
    [687, 75],
]

run_functional_tests(Solution().splitNum, tests)
