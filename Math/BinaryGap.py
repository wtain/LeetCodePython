"""
https://leetcode.com/problems/binary-gap/
Given a positive integer n, find and return the longest distance between any two adjacent 1's in the binary representation of n. If there are no two adjacent 1's, return 0.

Two 1's are adjacent if there are only 0's separating them (possibly no 0's). The distance between two 1's is the absolute difference between their bit positions. For example, the two 1's in "1001" have a distance of 3.



Example 1:

Input: n = 22
Output: 2
Explanation: 22 in binary is "10110".
The first adjacent pair of 1's is "10110" with a distance of 2.
The second adjacent pair of 1's is "10110" with a distance of 1.
The answer is the largest of these two distances, which is 2.
Note that "10110" is not a valid pair since there is a 1 separating the two 1's underlined.
Example 2:

Input: n = 5
Output: 2
Explanation: 5 in binary is "101".
Example 3:

Input: n = 6
Output: 1
Explanation: 6 in binary is "110".
Example 4:

Input: n = 8
Output: 0
Explanation: 8 in binary is "1000".
There aren't any adjacent pairs of 1's in the binary representation of 8, so we return 0.
Example 5:

Input: n = 1
Output: 0


Constraints:

1 <= n <= 109

Runtime: 32 ms, faster than 51.97% of Python3 online submissions for Binary Gap.
Memory Usage: 14.3 MB, less than 25.33% of Python3 online submissions for Binary Gap.
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        lastPos = -1
        curPos = 0
        maxDist = 0
        while n > 0:
            if n & 1:
                if lastPos != -1:
                    dist = curPos - lastPos
                    maxDist = max(maxDist, dist)
                lastPos = curPos
            curPos += 1
            n >>= 1

        return maxDist


tests = [
    (22, 2),
    (5, 2),
    (6, 1),
    (8, 0),
    (1, 0),
]

for test in tests:
    if test[1] == Solution().binaryGap(test[0]):
        print("PASS")
    else:
        print("FAIL")