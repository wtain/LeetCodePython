"""
https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/597/week-5-april-29th-april-30th/3726/
https://leetcode.com/problems/powerful-integers/
Given two positive integers x and y, an integer is powerful if it is equal to x^i + y^j for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.



Example 1:

Input: x = 2, y = 3, bound = 10
Output: [2,3,4,5,7,9,10]
Explanation:
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
Example 2:

Input: x = 3, y = 5, bound = 15
Output: [2,4,6,8,10,14]


Note:

1 <= x <= 100
1 <= y <= 100
0 <= bound <= 10^6

Runtime: 28 ms, faster than 84.24% of Python3 online submissions for Powerful Integers.
Memory Usage: 14.2 MB, less than 71.92% of Python3 online submissions for Powerful Integers.
"""
from typing import List


# Runtime: 28 ms, faster than 88.33% of Python3 online submissions for Powerful Integers.
# Memory Usage: 14.2 MB, less than 65.42% of Python3 online submissions for Powerful Integers.
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        i = 0
        result = set()
        while x**i <= bound:
            j = 0
            while x**i + y**j <= bound:
                result.add(x**i + y**j)
                j += 1
                if y == 1:
                    break
            if x == 1:
                break
            i += 1

        return list(result)


tests = [
    (2, 1, 10, [9, 2, 3, 5]),

    (2, 3, 10, [2,3,4,5,7,9,10]),
    (3, 5, 15, [2,4,6,8,10,14])
]

for test in tests:
    result = Solution().powerfulIntegers(test[0], test[1], test[2])
    if sorted(result) == sorted(test[3]):
        print("PASS")
    else:
        print("FAIL - " + str(result))