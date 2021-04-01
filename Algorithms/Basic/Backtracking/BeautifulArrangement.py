"""
https://leetcode.com/explore/challenge/card/january-leetcoding-challenge-2021/579/week-1-january-1st-january-7th/3591/
https://leetcode.com/problems/beautiful-arrangement/

Suppose you have n integers from 1 to n. We define a beautiful arrangement as an array that is constructed by these n numbers successfully if one of the following is true for the ith position (1 <= i <= n) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Given an integer n, return the number of the beautiful arrangements that you can construct.



Example 1:

Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 15

Runtime: 1464 ms, faster than 43.55% of Python3 online submissions for Beautiful Arrangement.
Memory Usage: 14.2 MB, less than 74.19% of Python3 online submissions for Beautiful Arrangement.
"""
from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        cnt = 0
        mask = [False] * n

        def impl(pos: int, mask: List[int]):
            nonlocal cnt
            if pos == n:
                cnt += 1
                return
            pos1 = pos + 1
            for i in range(n):
                if mask[i]:
                    continue
                i1 = i+1
                if i1 % pos1 == 0 or pos1 % i1 == 0:
                    mask[i] = True
                    impl(pos+1, mask)
                    mask[i] = False

        impl(0, mask)
        return cnt


tests = [
    (2, 2),
    (1, 1),

    (15, 24679)
]

for test in tests:
    result = Solution().countArrangement(test[0])
    if result == test[1]:
        print("PASS")
    else:
        print("FAIL")