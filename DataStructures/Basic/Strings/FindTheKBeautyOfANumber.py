"""
https://leetcode.com/problems/find-the-k-beauty-of-a-number/

The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.



Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.


Constraints:

1 <= num <= 109
1 <= k <= num.length (taking num as a string)
"""
from Common.ObjectTestingUtils import run_functional_tests


# WRONG
# class Solution:
#     def divisorSubstrings(self, num: int, k: int) -> int:
#         cnt = 0
#
#         p = 1
#         while num > p:
#             p *= 10
#
#         p1 = p
#         for i in range(k-1):
#             p1 //= 10
#
#         nn = num
#         v = 0
#         p2 = p
#         for i in range(k):
#             p2 //= 10
#             v *= 10
#             if not p2:
#                 break
#             v += nn // p2
#             nn %= p2
#
#         if v and num % v == 0:
#             cnt += 1
#
#         while p2:
#             v %= p1 // 10
#             v *= 10
#             v += nn // p2
#             nn %= p2
#             if v and num % v == 0:
#                 cnt += 1
#             p2 //= 10
#
#         return cnt


# Runtime: 38 ms, faster than 50.00% of Python3 online submissions for Find the K-Beauty of a Number.
# Memory Usage: 13.8 MB, less than 75.00% of Python3 online submissions for Find the K-Beauty of a Number.
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        cnt = 0

        nn = num
        v = 0
        p = 1
        for i in range(k):
            v += (nn % 10) * p
            nn //= 10
            p *= 10

        if v and num % v == 0:
            cnt += 1

        p //= 10

        while nn:
            v //= 10
            v += (nn % 10) * p
            nn //= 10
            if v and num % v == 0:
                cnt += 1

        return cnt


tests = [
    [10, 1, 1],
    [10, 2, 1],
    [240, 2, 2],
    [430043, 2, 2]
]

run_functional_tests(Solution().divisorSubstrings, tests)
