"""
https://leetcode.com/problems/reach-a-number/
https://leetcode.com/explore/challenge/card/december-leetcoding-challenge/572/week-4-december-22nd-december-28th/3583/
You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].

Runtime: 100 ms, faster than 49.32% of Python3 online submissions for Reach a Number.
Memory Usage: 14 MB, less than 85.62% of Python3 online submissions for Reach a Number.
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        #  1  2  3 ... N -> sum = target
        # sum1 - sum2 = target
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k
        if target % 2 == 0:
            return k
        else:
            return k + 1 + k % 2


tests = [
    (3, 2),
    (2, 3)
]

for test in tests:
    result = Solution().reachNumber(test[0])
    expected = test[1]
    if result == expected:
        print("PASS")
    else:
        print("FAIL - expected " + str(expected) + ", got " + str(result))