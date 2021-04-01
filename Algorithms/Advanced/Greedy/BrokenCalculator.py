"""
https://leetcode.com/explore/featured/card/february-leetcoding-challenge-2021/586/week-3-february-15th-february-21st/3647/
https://leetcode.com/problems/broken-calculator/

On a broken calculator that has a number showing on its display, we can perform two operations:

Double: Multiply the number on the display by 2, or;
Decrement: Subtract 1 from the number on the display.
Initially, the calculator is displaying the number X.

Return the minimum number of operations needed to display the number Y.



Example 1:

Input: X = 2, Y = 3
Output: 2
Explanation: Use double operation and then decrement operation {2 -> 4 -> 3}.
Example 2:

Input: X = 5, Y = 8
Output: 2
Explanation: Use decrement and then double {5 -> 4 -> 8}.
Example 3:

Input: X = 3, Y = 10
Output: 3
Explanation:  Use double, decrement and double {3 -> 6 -> 5 -> 10}.
Example 4:

Input: X = 1024, Y = 1
Output: 1023
Explanation: Use decrement operations 1023 times.


Note:

1 <= X <= 10^9
1 <= Y <= 10^9
"""


# Runtime: 28 ms, faster than 86.05% of Python3 online submissions for Broken Calculator.
# Memory Usage: 14.4 MB, less than 14.95% of Python3 online submissions for Broken Calculator.
class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if Y < X:
            return X - Y
        cnt = 0
        while Y > X:
            if Y % 2 == 1:
                Y += 1
                cnt += 1
            else:
                Y //= 2
                cnt += 1
        return cnt + X - Y


tests = [
    (2, 3, 2),
    (5, 8, 2),
    (3, 10, 3),
    (1024, 1, 1023)
]

for test in tests:
    result = Solution().brokenCalc(test[0], test[1])
    if result == test[2]:
        print("PASS")
    else:
        print("FAIL - " + str(result))