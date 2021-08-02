"""
https://leetcode.com/problems/lexicographical-numbers/

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.



Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]


Constraints:

1 <= n <= 5 * 104
"""
from typing import List

from Common.ObjectTestingUtils import run_functional_tests


# Runtime: 108 ms, faster than 71.35% of Python3 online submissions for Lexicographical Numbers.
# Memory Usage: 20.1 MB, less than 80.41% of Python3 online submissions for Lexicographical Numbers.
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        current = 0
        for _ in range(n):
            last_digit = current % 10
            down = current * 10
            if down == 0:
                down = 1
            if down <= n:
                current = down
            elif last_digit < 9 and current+1 <= n:
                current += 1
            else:
                up = current // 10
                while up % 10 == 9:
                    up //= 10
                current = up+1
            result.append(current)
        return result


tests = [
    [13, [1,10,11,12,13,2,3,4,5,6,7,8,9]],
    [2, [1,2]]
]

run_functional_tests(Solution().lexicalOrder, tests)