"""
https://leetcode.com/problems/next-greater-element-iii/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3578/
Given a positive integer n, find the smallest integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid answer but it does not fit in 32-bit integer, return -1.



Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1


Constraints:

1 <= n <= 231 - 1

Runtime: 28 ms, faster than 74.14% of Python3 online submissions for Next Greater Element III.
Memory Usage: 14.2 MB, less than 31.80% of Python3 online submissions for Next Greater Element III.
"""


# class Solution:
#     def nextGreaterElement(self, n: int) -> int:
#         prev = [-1] * 10
#         counts = [0] * 10
#         d = 1
#         while d <= n:
#             digit = int((n % (d*10)) / d)
#             counts[digit] += 1
#             for i in range(digit+1, 10):
#                 if prev[i] != -1:
#                     result = n + (i - digit) * (d - prev[i])
#                     result1 = int(result / (prev[i] * 10))
#                     dd = prev[i]
#                     counts[i] -= 1
#                     j = 0
#                     while dd > 0:
#                         while counts[j] == 0:
#                             j += 1
#                         result1 = result1 * 10 + j
#                         counts[j] -= 1
#                         dd = int(dd / 10)
#                     result = result1
#                     if result > 2147483647:
#                         return -1
#                     return result
#             prev[digit] = d
#             d *= 10
#         return -1
from typing import List


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        prev = [-1] * 10  # Powers of previous digits
        counts = [0] * 10  # Counts of previously encountered digits
        d = 1 # starting iteration from less-significant digit
        def sortTail(result: int, d: int, counts: List[int]) -> int:
            dd = int(d / 10)
            counts[i] -= 1
            j = 0
            while dd > 0:
                while counts[j] == 0:
                    j += 1
                result = result * 10 + j
                counts[j] -= 1
                dd = int(dd / 10)
            return result

        while d <= n:
            digit = int((n % (d*10)) / d)  # Getting current digit
            counts[digit] += 1  # Counting current digit
            # Iterating over digits we previously met and that are bigger than th current
            for i in range(digit+1, 10):
                if prev[i] != -1:
                    result = n + (i - digit) * (d - prev[i])  # Once found, swapping with the current
                    result = sortTail(int(result / d), d, counts)  # Sorting all the digits on the right
                    if result > 2147483647:
                        return -1
                    return result
            prev[digit] = d
            d *= 10
        return -1


tests = [
    (12443322, 13222344),
    (230241, 230412),

    (2147483647, -1),
    (12, 21),
    (21, -1),
    (123123, 123132),
    (321, -1)
]

for test in tests:
    result = Solution().nextGreaterElement(test[0])
    expected = test[1]
    if expected == result:
        print("PASS")
    else:
        print("FAIL - " + str(result) + ", expected " + str(expected))