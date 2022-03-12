"""
https://leetcode.com/problems/finding-3-digit-even-numbers/

You are given an integer array digits, where each element is a digit. The array may contain duplicates.

You need to find all the unique integers that follow the given requirements:

The integer consists of the concatenation of three elements from digits in any arbitrary order.
The integer does not have leading zeros.
The integer is even.
For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

Return a sorted array of the unique integers.



Example 1:

Input: digits = [2,1,3,0]
Output: [102,120,130,132,210,230,302,310,312,320]
Explanation: All the possible integers that follow the requirements are in the output array.
Notice that there are no odd integers or integers with leading zeros.
Example 2:

Input: digits = [2,2,8,8,2]
Output: [222,228,282,288,822,828,882]
Explanation: The same digit can be used as many times as it appears in digits.
In this example, the digit 8 is used twice each time in 288, 828, and 882.
Example 3:

Input: digits = [3,7,5]
Output: []
Explanation: No even integers can be formed using the given digits.


Constraints:

3 <= digits.length <= 100
0 <= digits[i] <= 9
"""
from collections import Counter
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 4012 ms, faster than 32.30% of Python3 online submissions for Finding 3-Digit Even Numbers.
# Memory Usage: 14 MB, less than 68.08% of Python3 online submissions for Finding 3-Digit Even Numbers.
# class Solution:
#     def findEvenNumbers(self, digits: List[int]) -> List[int]:
#         result = []
#         digits.sort()
#         n = len(digits)
#         used = [False] * n
#         seen = set()
#         for i in range(n):
#             if not digits[i]:
#                 continue
#             used[i] = True
#             for j in range(n):
#                 if used[j]:
#                     continue
#                 used[j] = True
#                 for l in range(n):
#                     if used[l]:
#                         continue
#                     if digits[l] % 2:
#                         continue
#                     v = 100*digits[i] + 10 * digits[j] + digits[l]
#                     if v not in seen:
#                         result.append(v)
#                         seen.add(v)
#                 used[j] = False
#             used[i] = False
#         return result


# Runtime: 201 ms, faster than 61.52% of Python3 online submissions for Finding 3-Digit Even Numbers.
# Memory Usage: 14 MB, less than 68.08% of Python3 online submissions for Finding 3-Digit Even Numbers.
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        cnt = Counter(digits)
        for v in range(100, 1000):
            if v % 2:
                continue
            d1 = v // 100
            v1 = v % 100
            d2 = v1 // 10
            d3 = v1 % 10
            cnt1 = cnt.copy()
            cnt1[d1] -= 1
            cnt1[d2] -= 1
            cnt1[d3] -= 1
            if any(cnt1[d] < 0 for d in cnt1):
                continue
            result.append(v)
        return result


tests = [
    [[2,1,3,0], [102,120,130,132,210,230,302,310,312,320]],
    [[2,2,8,8,2], [222,228,282,288,822,828,882]],
    [[3,7,5], []]
]

run_functional_tests(Solution().findEvenNumbers, tests)
